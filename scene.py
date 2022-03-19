import numpy as np
from stl import mesh
import matplotlib.pyplot as plt
from mpl_toolkits import mplot3d

"""
Класс описывающий сцену
"""


class Scene:
    def __init__(self, path):
        self.scene = mesh.Mesh.from_file(path)
        self.vectors = self.scene.vectors
        self.triangles_data = np.array([np.array(vector) for vector in self.vectors]) #массив полигонов
        self.x = self.scene.x
        self.y = self.scene.y
        self.z = self.scene.z

    def create_plot_scene(self, figure=None, canvas=None):
        """
        Функция вывода графика сцены
        :param figure:
        :param canvas:
        :return:
        """
        if figure and canvas:
            figure.clear()
            axes = mplot3d.Axes3D(figure)
            scale = self.scene.points.flatten()
            axes.auto_scale_xyz(scale, scale, scale)
            axes.add_collection3d(mplot3d.art3d.Poly3DCollection(self.triangles_data))
            canvas.draw()
