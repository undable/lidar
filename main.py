import numpy as np
import time
import graphics
import directions
import scanning
import input_data


def main(scene):
    triangles_data = input_data.get_triangles_data(scene)  # получить массив полигонов
    dir_data, size_h, size_v = directions.get_direction_data(45, 45, 0.5, 0.5)  # получить массив лучей
    dir_data = dir_data.astype(np.float32)
    size_h = int(size_h)
    size_v = int(size_v)
    dir_data = directions.rotate_window(dir_data, 'z', 0)  # вращение локатора
    start_time = time.time()
    cloud_points, distance_array = scanning.scan(triangles_data, dir_data)  # получение облака точек
    print("--- %s seconds ---" % (time.time() - start_time))
    graphics.create_scene(scene)   # выводим сцену
    graphics.create_plots(scene, cloud_points)  # выводим облако точек
    # graphics.create_plots('scene4.stl', cloud_points)
    graphics.create_image(distance_array, size_v, size_h)  # выводим дальностное изображение
    scanning.write_las(cloud_points, 'test.las')  # запись файла


if __name__ == '__main__':
    main('scene.stl')
