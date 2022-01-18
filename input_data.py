import numpy as np
from stl import mesh


def get_triangles_data(path):
    """
    Чтение stl-файла
    :param path: путь к файлу
    :return: массив полигонов
    """
    scene = mesh.Mesh.from_file(path)
    vectors = scene.vectors
    triangles_data = [np.array(vector) for vector in vectors]
    return np.array(triangles_data)
