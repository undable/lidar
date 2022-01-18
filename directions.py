import numpy as np
import math


def rotate_z(vector, angle):
    """
    вращение вектора вокруг оси Z
    :param vector: исходный вектор
    :param angle: угол в градусах
    :return: повернутый вектор
    """
    rotate_matrix = np.array([[math.cos(angle), -math.sin(angle), 0], [math.sin(angle), math.cos(angle), 0], [0, 0, 1]])
    rotate_vector = np.dot(vector, rotate_matrix)
    return rotate_vector


def rotate_y(vector, angle):
    """
    вращение вектора вокруг оси Y
    :param vector: исходный вектор
    :param angle: угол в градусах
    :return: повернутый вектор
    """
    rotate_matrix = np.array([[math.cos(angle), 0, math.sin(angle)], [0, 1, 0], [-math.sin(angle), 0, math.cos(angle)]])
    rotate_vector = np.dot(vector, rotate_matrix)
    return rotate_vector


def rotate_x(vector, angle):
    """
    вращение вектора вокруг оси X
    :param vector: исходный вектор
    :param angle: угол в градусах
    :return: повернутый вектор
    """
    rotate_matrix = np.array([[1, 0, 0], [0, math.cos(angle), -math.sin(angle)], [0, math.sin(angle), math.cos(angle)]])
    rotate_vector = np.dot(vector, rotate_matrix)
    return rotate_vector


def rotate_window(window, direction, angle):
    """
    Вращение матрицы вокруг оси
    :param window: матрица
    :param direction: название оси, вокруг которой происходит вращение
    :param angle: угол вращения в градусах
    :return: повернутая матрица
    """
    if direction == 'x':
        for ray_i in range(len(window)):
            window[ray_i] = rotate_x(window[ray_i], math.radians(angle))
    if direction == 'z':
        for ray_i in range(len(window)):
            window[ray_i] = rotate_z(window[ray_i], math.radians(angle))
    return window


def get_direction_data(fov_h, fov_v, step_h, step_v):
    """
    :param fov_h: угол обзора в горизонтальной плоскости
    :param fov_v: угол обзора в вертикальной плоскости
    :param step_h: разрешение в горизонтальной плоскости
    :param step_v: разрешение в вертикальной плоскости
    :return:
    """
    central_dir = np.array([0, 1, 0])  # вектор нормали окна
    lu_dir = np.array(
        [central_dir[1]*math.tan(math.radians(-fov_h/2)), central_dir[1], central_dir[1]*math.tan(math.radians(fov_v/2))])  # левый верхний угол матрицы
    ld_dir = np.array(
        [central_dir[1] * math.tan(math.radians(-fov_h/2)), central_dir[1], central_dir[1] * math.tan(math.radians(-fov_v/2))])  # левый нижний угол матрицы
    ru_dir = np.array(
        [central_dir[1] * math.tan(math.radians(fov_h/2)), central_dir[1], central_dir[1] * math.tan(math.radians(fov_v/2))])  # правый верхний угол матрицы
    rd_dir = np.array(
        [central_dir[1] * math.tan(math.radians(fov_h/2)), central_dir[1], central_dir[1] * math.tan(math.radians(-fov_v/2))])  # правый нижний угол матрицы
    width_win = ru_dir[0] - lu_dir[0]  # ширина матрицы
    height_win = ru_dir[2] - rd_dir[2]  # высота матрицы
    dir_data = []
    # формируем матрицу лучей
    for h in np.arange(0, height_win, height_win/(fov_v/step_v)):
        for w in np.arange(0, width_win, width_win/(fov_h/step_h)):
            dir_data.append(np.array([ld_dir[0]+w, ld_dir[1], ld_dir[2]+h]))
    dir_data = np.asarray(dir_data)
    return dir_data, fov_h/step_h, fov_v/step_v
