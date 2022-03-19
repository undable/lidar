import numpy as np
import math
import matplotlib.pyplot as plt
from mpl_toolkits import mplot3d
from stl import mesh
import pyopencl as cl
import pylas


"""
Описывает основной функционал работы модели канала ЛЛС
"""

class Lidar:
    def __init__(self, fov_h, fov_v, step_h, step_v):
        """
        :param fov_h: ширина сканирования по азимуту
        :param fov_v: ширина сканирования по углу места
        :param step_h: разрешение по азимуиу
        :param step_v: разрешение по углу места
        """
        self.fov_h = fov_h
        self.fov_v = fov_v
        self.step_h = step_h
        self.step_v = step_v
        self.central_dir = np.array([0, 1, 0])  # вектор нормали окна
        self.position = np.array([0, 0, 0]).astype(np.float32)
        # self.lu_dir = self.rotate_x(self.rotate_z(self.central_dir, self.fov_h / 2), -self.fov_v/2)
        # self.ld_dir = self.rotate_x(self.rotate_z(self.central_dir, self.fov_h / 2), self.fov_v / 2)
        # self.ru_dir = self.rotate_x(self.rotate_z(self.central_dir, -self.fov_h / 2), -self.fov_v / 2)
        # self.rd_dir = self.rotate_x(self.rotate_z(self.central_dir, -self.fov_h / 2), self.fov_v / 2)
        # self.lu_dir = self.rotate_z(self.rotate_x(self.central_dir, self.fov_v / 2), -self.fov_h/2)
        # self.ld_dir = self.rotate_z(self.rotate_x(self.central_dir, -self.fov_v / 2), -self.fov_h / 2)
        # self.ru_dir = self.rotate_z(self.rotate_x(self.central_dir, self.fov_v / 2), self.fov_h / 2)
        # self.rd_dir = self.rotate_z(self.rotate_x(self.central_dir, -self.fov_v / 2), self.fov_h / 2)
        self.lu_dir = np.array(
            [self.central_dir[1] * math.tan(math.radians(-self.fov_h / 2)), self.central_dir[1],
             self.central_dir[1] * math.tan(math.radians(self.fov_v / 2))])  # левый верхний угол матрицы
        self.ld_dir = np.array(
            [self.central_dir[1] * math.tan(math.radians(-self.fov_h / 2)), self.central_dir[1],
             self.central_dir[1] * math.tan(math.radians(-self.fov_v / 2))])  # левый нижний угол матрицы
        self.ru_dir = np.array(
            [self.central_dir[1] * math.tan(math.radians(self.fov_h / 2)), self.central_dir[1],
             self.central_dir[1] * math.tan(math.radians(self.fov_v / 2))])  # правый верхний угол матрицы
        self.rd_dir = np.array(
            [self.central_dir[1] * math.tan(math.radians(self.fov_h / 2)), self.central_dir[1],
             self.central_dir[1] * math.tan(math.radians(-self.fov_v / 2))])  # правый нижний угол матрицы
        self.width_win = self.ru_dir[0] - self.lu_dir[0]  # ширина матрицы
        self.height_win = self.ru_dir[2] - self.rd_dir[2]  # высота матрицы
        self.dir_data = []
        self.quantity_rays_v = np.around(self.fov_v / self.step_v).astype(np.int32)
        self.quantity_rays_h = np.around(self.fov_h / self.step_h).astype(np.int32)
        self.single_qr_v = 50
        self.single_qr_h = 50
        self.step_win_v = self.height_win / self.quantity_rays_v
        self.step_win_h = self.width_win / self.quantity_rays_h

        # формируем матрицу лучей
        for h in np.linspace(self.step_win_v / 2, self.height_win + self.step_win_v / 2, self.quantity_rays_v):
            for w in np.linspace(self.step_win_h / 2, self.width_win + self.step_win_h / 2, self.quantity_rays_h):
                self.dir_data.append(np.array([self.ld_dir[0] + w, self.ld_dir[1], self.ld_dir[2] + h]))
        self.dir_data = np.asarray(self.dir_data).astype(np.float32)
        self.dir_matrix = np.flipud(np.reshape(self.dir_data, (self.quantity_rays_v, self.quantity_rays_h, 3)))
        self.cloud_points = np.array([])
        self.dp = np.array([])
        self.single_dp = np.array([])
        self.matrix_delay = np.array([])
        self.ih = np.array([])
        self.ih_time = np.array([])
        self.out_signal = np.array([])
        self.out_signal_time = np.array([])
        self.t_d = .0

    @staticmethod
    def rotate_x(vector, angle):
        rotate_matrix = np.array(
            [[1, 0, 0], [0, math.cos(angle), -math.sin(angle)], [0, math.sin(angle), math.cos(angle)]])
        rotate_vector = np.dot(vector, rotate_matrix)
        return rotate_vector

    @staticmethod
    def rotate_y(vector, angle):
        rotate_matrix = np.array(
            [[math.cos(angle), 0, math.sin(angle)], [0, 1, 0], [-math.sin(angle), 0, math.cos(angle)]])
        rotate_vector = np.dot(vector, rotate_matrix)
        return rotate_vector

    @staticmethod
    def rotate_z(vector, angle):
        rotate_matrix = np.array(
            [[math.cos(angle), -math.sin(angle), 0], [math.sin(angle), math.cos(angle), 0], [0, 0, 1]])
        rotate_vector = np.dot(vector, rotate_matrix)
        return rotate_vector

    def rotate_window(self, direction, angle):
        if direction == 'x':
            for ray_i in range(len(self.dir_data)):
                self.dir_data[ray_i] = Lidar.rotate_x(self.dir_data[ray_i], math.radians(angle))
        if direction == 'z':
            for ray_i in range(len(self.dir_data)):
                self.dir_data[ray_i] = Lidar.rotate_z(self.dir_data[ray_i], math.radians(angle))
        return self.dir_data

    def set_position(self, x, y, z):
        """
        Переместить ЛЛС в точку с координатами x,y,z
        :param x:
        :param y:
        :param z:
        :return:
        """
        delta = np.array([x - self.position[0], y - self.position[1], z - self.position[2]]).astype(np.float32)
        self.position = np.array([x, y, z]).astype(np.float32)
        for ray in self.dir_data:
            ray = ray + delta

    def move_position(self, delta_x, delta_y, delta_z):
        """
        Переместить ЛЛС на delta_x, delta_y, delta_z
        :param delta_x:
        :param delta_y:
        :param delta_z:
        :return:
        """
        delta = np.array([delta_x, delta_y, delta_z]).astype(np.float32)
        self.position = self.position + delta
        # print(delta)
        # print(self.position)
        for ray in self.dir_data:
            ray = ray + delta

    def show_matrix(self, path):
        figure = plt.figure()
        scene = mesh.Mesh.from_file(path)
        axes = mplot3d.Axes3D(figure)
        axes.scatter(self.central_dir[0], self.central_dir[1], self.central_dir[2], c='green')
        axes.scatter(self.lu_dir[0], self.lu_dir[1], self.lu_dir[2], c='orange')
        axes.scatter(self.ru_dir[0], self.ru_dir[1], self.ru_dir[2], c='orange')
        axes.scatter(self.ld_dir[0], self.ld_dir[1], self.ld_dir[2], c='orange')
        axes.scatter(self.rd_dir[0], self.rd_dir[1], self.rd_dir[2], c='orange')
        axes.scatter(self.position[0], self.position[1], self.position[2], c='black')
        scale = scene.points.flatten()
        axes.auto_scale_xyz(scale, scale, scale)
        plt.show()

    def create_plot_cloud_points(self, figure=None, canvas=None):
        """
        Отображение графика облака точек
        :param figure:
        :param canvas:
        :return:
        """
        if figure and canvas:
            figure.clear()
            axes = mplot3d.Axes3D(figure)
            axes.scatter(self.cloud_points[:, 0], self.cloud_points[:, 1], self.cloud_points[:, 2], c='orange')
            axes.scatter(0, 0, 0, c='black')
            axes.scatter(100, 0, 0, c='red')
            axes.scatter(0, 100, 0, c='green')
            axes.scatter(0, 0, 100, c='blue')
            axes.scatter(self.position[0], self.position[1], self.position[2], c='black', s=40)
            axes.auto_scale_xyz([-800, 800], [-100, 750], [-600, 600])
            canvas.draw()

    def create_plot_dp(self, image_array, mode=None, figure=None, canvas=None):
        """
        Построение дальностной матрицы
        :param image_array: дальностная матрица
        :param mode: 'single' для одного канала
        :param figure:
        :param canvas:
        :return:
        """
        if mode == 'single':
            image_array = np.reshape(image_array, (self.single_qr_v, self.single_qr_h))
        else:
            image_array = np.reshape(image_array, (self.quantity_rays_v, self.quantity_rays_h))
        image_array = np.flipud(image_array)
        if figure and canvas:
            figure.clear()
            ax = figure.add_subplot(111)
            plot = ax.imshow(image_array)
            figure.colorbar(plot)
            canvas.draw()
        else:
            figure = plt.figure()
            plt.imshow(image_array)
            plt.colorbar()
            plt.show()

    def scan(self, polygons, mode=None, directions=None):
        """
        Определение пересечения лучей и сцены, формирование облака точек и дальностной матрицы
        :param polygons: полигоны сцены
        :param mode: 'single' для одного канала
        :param directions: массив лучей, указывается в случае сканирования одного канала
        :return:
        """
        polygons = polygons.astype(np.float32)
        n_poly = len(polygons)
        ctx = cl.create_some_context()
        queue = cl.CommandQueue(ctx)
        mf = cl.mem_flags
        prg = cl.Program(ctx, """
         __kernel void rti(
         __global const float *start_cl, __global const float *directions_cl, __global const float *poly_cl, 
         int const n_poly, int eps, __global float *res, __global float *dis_array)
         {
          int gid = get_global_id(0);
          float3 start = (float3)(start_cl[0], start_cl[1], start_cl[2]);
          float3 dir = (float3)(directions_cl[gid*3], directions_cl[gid*3+1], directions_cl[gid*3+2]);
          float t_min = 1000;
          for (int poly_i = 0; poly_i < n_poly; poly_i++){
            float3 v0 = (float3)(poly_cl[poly_i*9], poly_cl[poly_i*9+1], poly_cl[poly_i*9+2]);
            float3 v1 = (float3)(poly_cl[poly_i*9+3], poly_cl[poly_i*9+4], poly_cl[poly_i*9+5]);
            float3 v2 = (float3)(poly_cl[poly_i*9+6], poly_cl[poly_i*9+7], poly_cl[poly_i*9+8]);
            float3 e1 = v1 - v0;
            float3 e2 = v2 - v0;
            float3 pvec = cross(dir, e2);
            float det = dot(e1, pvec);
            if (det > eps || det < -eps) {
              float inv_det = 1 / det;
              float3 tvec = start - v0;
              float u = dot(tvec, pvec) * inv_det;
              if (u >= 0 && u <= 1) {
                float3 qvec = cross(tvec, e1);
                float v = dot(dir, qvec) * inv_det;
                if (v >= 0 && u + v <= 1) {
                  float t = dot(e2, qvec) * inv_det;
                  if (t>eps && t<t_min){
                    //printf("%.3f", t);
                    t_min = t;
                  }
                }
              } 
            }
          }
          if (t_min != 1000){
            float3 point = start+t_min*dir;
            //printf("%.3f", t_min);
            res[gid*3] = point.x;
            res[gid*3+1] = point.y;
            res[gid*3+2] = point.z;
            dis_array[gid] = length(point-start);
          }
          if (t_min == 1000){
            //float3 point = start+t_min*dir;
            //printf("%.3f", t_min);
            dis_array[gid] = 0;
          }  
         }
         """).build()
        eps = 0.00001
        start = self.position
        start_cl = cl.Buffer(ctx, mf.READ_ONLY | mf.COPY_HOST_PTR, hostbuf=start)
        if mode == 'single':
            direction_data = directions
        else:
            direction_data = self.dir_data
        n_dir = len(direction_data)
        direction_data_cl = cl.Buffer(ctx, mf.READ_ONLY | mf.COPY_HOST_PTR, hostbuf=direction_data)
        poly_cl = cl.Buffer(ctx, mf.READ_ONLY | mf.COPY_HOST_PTR, hostbuf=polygons)
        res_g = cl.Buffer(ctx, mf.WRITE_ONLY, direction_data.nbytes)
        dis_array = cl.Buffer(ctx, mf.WRITE_ONLY, direction_data.nbytes)
        knl = prg.rti  # Use this Kernel object for repeated calls
        knl(queue, (n_dir, 1), None, start_cl, direction_data_cl, poly_cl, np.int32(n_poly), np.int32(eps), res_g,
            dis_array)
        size_res = (np.empty([n_dir, 3])).astype(np.float32)
        size_res_dis = (np.empty([n_dir, 1])).astype(np.float32)
        if mode == 'single':
            self.single_dp = np.empty_like(size_res_dis)
            cl.enqueue_copy(queue, self.single_dp, dis_array)
            self.single_dp[self.single_dp == 0] = np.inf
        else:
            self.dp = np.empty_like(size_res_dis)
            cl.enqueue_copy(queue, self.dp, dis_array)
            self.dp[self.dp == 0] = np.inf
        res_np = np.empty_like(size_res)
        cl.enqueue_copy(queue, res_np, res_g)
        cloud_points = []
        for point in res_np:
            if (point != 0.).any():
                cloud_points.append(point)
        self.cloud_points = np.asarray(cloud_points)

    def write_las(self, name):
        """
        Запись облака точек в файл
        :param name: имя файла
        :return:
        """
        las = pylas.create()
        las.x = self.cloud_points[:, 0]
        las.y = self.cloud_points[:, 1]
        las.z = self.cloud_points[:, 2]
        las.write(name)

    def get_ih(self, dp):
        """
        Получение импульсной характеристики
        :param dp: дальностная матрица
        :return:
        """
        matrix_delay = 2 * dp / (3e8)
        delay_flatten = matrix_delay.flatten()
        delay_flatten = delay_flatten[delay_flatten != np.inf]
        delay_flatten = np.append(delay_flatten, [0])
        delay_flatten = np.append(delay_flatten, [5e-6])
        delay_flatten.sort()
        self.ih, bins = np.histogram(delay_flatten, int((np.amax(delay_flatten)-np.amin(delay_flatten))/(self.t_d)))
        self.ih_time = np.empty_like(self.ih).astype(np.float32)
        for i in range(len(self.ih)):
            self.ih_time[i] = (bins[i] + bins[i + 1]) / 2
        self.ih = self.ih / (self.single_qr_v*self.single_qr_h)

    def create_plot_ih(self, figure=None, canvas=None):
        """
        Построение графика ИХ
        :param figure:
        :param canvas:
        :return:
        """
        if figure and canvas:
            figure.clear()
            ax = figure.add_subplot(111)
            ax.plot(self.ih_time, self.ih)
            ax.grid()
            ax.set_xlabel('Время, с')
            ax.set_ylabel('Амплитуда')
            ax.set_title('Импульсная характеристика')
            canvas.draw()

    def create_plot_out_signal(self, in_signal, figure=None, canvas=None):
        """
        Формирование выходного сигнала и построение его графика
        :param in_signal: входной сигнал
        :param figure:
        :param canvas:
        :return:
        """
        if figure and canvas:
            figure.clear()
            ax = figure.add_subplot(111)
            self.out_signal = np.convolve(self.ih, in_signal) + np.random.normal(0, 0.2, len(self.ih)+len(in_signal)-1)
            self.out_signal_time = np.linspace(0, (len(self.ih)+len(in_signal)-1)*(self.t_d),
                                               len(self.ih)+len(in_signal)-1)
            ax.plot(self.out_signal_time, self.out_signal)
            # ax.plot(self.out_signal + np.random.normal(0, 10, np.size(self.out_signal)))
            ax.grid()
            ax.set_xlabel('Время, с')
            ax.set_ylabel('Амплитуда')
            ax.set_title('Выходной сигнал')
            canvas.draw()
        else:
            self.out_signal = np.convolve(self.ih, in_signal)
            self.out_signal_time = np.linspace(0, (len(self.ih) + len(in_signal) - 1) * (self.t_d),
                                               len(self.ih) + len(in_signal) - 1)

    def get_single_dir(self, ch_h, ch_v):
        """
        Формирование массива лучей для одного канала
        :param ch_h: номер канала по азимуту
        :param ch_v: номер канала по углу места
        :return:
        """
        single_central_dir = self.dir_matrix[ch_v][ch_h]
        single_ld_dir = np.array(
            [single_central_dir[0] - self.step_win_h / 2, single_central_dir[1], single_central_dir[2]
             - self.step_win_v / 2])
        single_dir_data = []
        for v in np.linspace(0, self.step_win_v, self.single_qr_v):
            for h in np.linspace(0, self.step_win_h, self.single_qr_h):
                single_dir_data.append(np.array([single_ld_dir[0] + h, single_ld_dir[1], single_ld_dir[2] + v]))
        single_dir_data = np.asarray(single_dir_data).astype(np.float32)
        return single_dir_data

    def get_all_out_signal(self, triangles_data, in_signal):
        """
        формирование выходного сигнала для всех каналов ЛЛС
        :param triangles_data:
        :param in_signal:
        :return:
        """
        len_out = len(self.ih)+len(in_signal)-1
        all_out = np.zeros((len_out, self.quantity_rays_v, self.quantity_rays_h))
        for v in range(self.quantity_rays_v):
            for h in range(self.quantity_rays_h):
                directions = self.get_single_dir(h, v)
                self.scan(triangles_data, 'single', directions)
                self.get_ih(self.single_dp)
                self.create_plot_out_signal(in_signal)
                all_out[:, v, h] = self.out_signal
                print(f'Канал {v}, {h} обработан')
        return all_out


