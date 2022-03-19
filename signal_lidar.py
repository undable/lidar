import numpy as np
import matplotlib.pyplot as plt

"""
Описывает сигналы источника излучения
"""

class SignalGauss:
    def __init__(self, T, a, t_d):
        """
        :param T: интервал наблюдения
        :param a: параметр сигнала
        :param t_d: интервал дискретизации
        """
        self.T = T
        self.t_d = t_d
        self.time_axis = np.linspace(0, self.T, int(T/t_d))
        self.signal = np.exp(-(self.time_axis - self.T/2) ** 2 * a ** 2)

    def get_plot(self, figure=None, canvas=None):
        """
        Построение графика сигнала
        :param figure:
        :param canvas:
        :return:
        """
        if figure and canvas:
            figure.clear()
            ax = figure.add_subplot(111)
            ax.plot(self.time_axis, self.signal)
            ax.grid()
            ax.set_xlabel('Время, с')
            ax.set_ylabel('Амплитуда')
            ax.set_title('Входной сигнал')
            canvas.draw()
