import pyopencl as cl
import numpy as np
import pylas


def scan(polygons, directions):
    """
    сканирование сцены
    :param polygons: массив полигонов объектов сцены
    :param directions: массив лучей
    :return: облако точек, массив расстояний
    """
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
        dis_array[gid] = length(point);
      }
      if (t_min == 1000){
        //float3 point = start+t_min*dir;
        //printf("%.3f", t_min);
        dis_array[gid] = 0;
      }  
     }
     """).build()
    eps = 0.00001
    start = np.array([0, 0, 0]).astype(np.float32)
    start_cl = cl.Buffer(ctx, mf.READ_ONLY | mf.COPY_HOST_PTR, hostbuf=start)
    # nul_direction = np.array([-1., 0., 0.])
    # points_cloud = []
    direction_data = directions
    n_dir = len(direction_data)
    direction_data_cl = cl.Buffer(ctx, mf.READ_ONLY | mf.COPY_HOST_PTR, hostbuf=direction_data)
    poly_cl = cl.Buffer(ctx, mf.READ_ONLY | mf.COPY_HOST_PTR, hostbuf=polygons)
    res_g = cl.Buffer(ctx, mf.WRITE_ONLY, direction_data.nbytes)
    dis_array = cl.Buffer(ctx, mf.WRITE_ONLY, direction_data.nbytes)
    knl = prg.rti  # Use this Kernel object for repeated calls
    knl(queue, (n_dir, 1), None, start_cl, direction_data_cl, poly_cl, np.int32(n_poly), np.int32(eps), res_g, dis_array)
    size_res = (np.empty([n_dir, 3])).astype(np.float32)
    size_res_dis = (np.empty([n_dir, 1])).astype(np.float32)
    res_dis = np.empty_like(size_res_dis)
    res_np = np.empty_like(size_res)
    cl.enqueue_copy(queue, res_np, res_g)
    cl.enqueue_copy(queue, res_dis, dis_array)
    res_np1 = []
    for point in res_np:
        if (point != 0.).any():
            res_np1.append(point)

    res_np1 = np.asarray(res_np1)
    return res_np1, res_dis


def write_las(points_cloud, name):
    """
    запись облака точек в файл формата las
    :param points_cloud:
    :param name:
    :return:
    """
    las = pylas.create()
    las.x = points_cloud[:, 0]
    las.y = points_cloud[:, 1]
    las.z = points_cloud[:, 2]
    las.write(name)

