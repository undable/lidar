import matplotlib.pyplot as plt
from mpl_toolkits import mplot3d
import numpy as np
from stl import mesh


def create_image(image_array, size_v, size_h):
    """
    формирование дальностного изображения
    :param image_array:
    :param size_v:
    :param size_h:
    :return:
    """
    image_array = np.reshape(image_array, (size_v, size_h))
    image_array = np.flipud(image_array)
    plt.imshow(image_array)
    plt.colorbar()
    plt.show()


def create_plots(path, *args):
    """
    вывод облака точек
    :param path: путь к исходной сцене, необходим для сопоставления масштабов сцены и облака точек
    :param args:
    :return:
    """
    figure = plt.figure()
    scene = mesh.Mesh.from_file(path)
    axes = mplot3d.Axes3D(figure)
    for arg in args:
        axes.scatter(arg[:, 0], arg[:, 1], arg[:, 2], c='orange')
    axes.scatter(0, 0, 0, c='black')
    axes.scatter(100, 0, 0, c='red')
    axes.scatter(0, 100, 0, c='green')
    axes.scatter(0, 0, 100, c='blue')

    scale = scene.points.flatten()
    axes.auto_scale_xyz(scale, scale, scale)

    plt.show()


def create_scene(path):
    """
    вывод сцены
    :param path: путь к сцене
    :return:
    """
    figure = plt.figure()
    scene = mesh.Mesh.from_file(path)
    axes = mplot3d.Axes3D(figure)

    scale = scene.points.flatten()
    axes.auto_scale_xyz(scale, scale, scale)
    axes.add_collection3d(mplot3d.art3d.Poly3DCollection(scene.vectors))
    axes.scatter(0, 0, 0, c='black')
    axes.scatter(100, 0, 0, c='red')
    axes.scatter(0, 100, 0, c='green')
    axes.scatter(0, 0, 100, c='blue')
    plt.show()
