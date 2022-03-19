import sys
import os
from PySide6.QtWidgets import QApplication, QMainWindow, QFileDialog
from design import Ui_MainWindow
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.backends.backend_qt5agg import NavigationToolbar2QT as NavigationToolbar
from directions import Lidar
from scene import Scene
from signal_lidar import SignalGauss
import numpy as np
import matplotlib.pyplot as plt

file_path = None
scene_lidar = None


class Gui(QMainWindow):
    def __init__(self):
        super(Gui, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.openfileButton.clicked.connect(self.browsefiles)
        self.ui.modelingButton.clicked.connect(self.modeling)
        self.ui.rotate_rightButton.clicked.connect(self.rotate_right)
        self.ui.rotate_leftButton.clicked.connect(self.rotate_left)
        self.ui.rotate_upButton.clicked.connect(self.rotate_up)
        self.ui.rotate_downButton.clicked.connect(self.rotate_down)
        self.ui.forwardButton.clicked.connect(self.move_forward)
        self.ui.backwardButton.clicked.connect(self.move_backward)
        self.ui.leftButton.clicked.connect(self.move_left)
        self.ui.rightButton.clicked.connect(self.move_right)
        self.ui.upButton.clicked.connect(self.move_up)
        self.ui.downButton.clicked.connect(self.move_down)
        self.ui.single_chanelButton.clicked.connect(self.single_modeling)
        self.ui.getallout_Button.clicked.connect(self.get_all_out)
        self.ui.pluschanel_Button.clicked.connect(self.swipe_chanel_plus)
        self.ui.minuschanel_Button.clicked.connect(self.swipe_chanel_minus)
        self.ui.chanelR_Button.clicked.connect(self.set_chanel)
        self.figure_dp = plt.figure()
        self.canvas_dp = FigureCanvas(self.figure_dp)
        self.toolbar_dp = NavigationToolbar(self.canvas_dp, self)
        layout_dp = self.ui.verticalLayout_4
        layout_dp.addWidget(self.toolbar_dp)
        layout_dp.addWidget(self.canvas_dp)
        self.figure_cp = plt.figure()
        self.canvas_cp = FigureCanvas(self.figure_cp)
        self.toolbar_cp = NavigationToolbar(self.canvas_cp, self)
        layout_cp = self.ui.verticalLayout_5
        layout_cp.addWidget(self.toolbar_cp)
        layout_cp.addWidget(self.canvas_cp)
        self.figure_sc = plt.figure()
        self.canvas_sc = FigureCanvas(self.figure_sc)
        self.toolbar_sc = NavigationToolbar(self.canvas_sc, self)
        layout_sc = self.ui.verticalLayout_6
        layout_sc.addWidget(self.toolbar_sc)
        layout_sc.addWidget(self.canvas_sc)
        self.figure_in = plt.figure()
        self.canvas_in = FigureCanvas(self.figure_in)
        self.toolbar_in = NavigationToolbar(self.canvas_in, self)
        layout_in = self.ui.verticalLayout_7
        layout_in.addWidget(self.toolbar_in)
        layout_in.addWidget(self.canvas_in)
        self.figure_ih = plt.figure()
        self.canvas_ih = FigureCanvas(self.figure_ih)
        self.toolbar_ih = NavigationToolbar(self.canvas_ih, self)
        layout_ih = self.ui.verticalLayout_8
        layout_ih.addWidget(self.toolbar_ih)
        layout_ih.addWidget(self.canvas_ih)
        self.figure_out = plt.figure()
        self.canvas_out = FigureCanvas(self.figure_out)
        self.toolbar_out = NavigationToolbar(self.canvas_out, self)
        layout_out = self.ui.verticalLayout_9
        layout_out.addWidget(self.toolbar_out)
        layout_out.addWidget(self.canvas_out)
        self.figure_dps = plt.figure()
        self.canvas_dps = FigureCanvas(self.figure_dps)
        self.toolbar_dps = NavigationToolbar(self.canvas_dps, self)
        layout_dps = self.ui.verticalLayout_10
        layout_dps.addWidget(self.toolbar_dps)
        layout_dps.addWidget(self.canvas_dps)
        self.figure_ao = plt.figure()
        self.canvas_ao = FigureCanvas(self.figure_ao)
        self.toolbar_ao = NavigationToolbar(self.canvas_ao, self)
        layout_ao = self.ui.verticalLayout_11
        layout_ao.addWidget(self.toolbar_ao)
        layout_ao.addWidget(self.canvas_ao)
        self.i = 0

    def browsefiles(self):
        # scene = QFileDialog.getOpenFileName(self, 'Open file', 'C:\\Users\\pasha\\Desktop\\lidar with classes',
        #                                     'STL files (*.stl)')
        scene = QFileDialog.getOpenFileName(self, 'Open file', os.getcwd(),
                                            'STL files (*.stl)')
        self.ui.lineEdit.setText(scene[0])
        global file_path
        global scene_lidar
        file_path = self.ui.lineEdit.text()
        scene_lidar = Scene(file_path)
        # print(scene_lidar.vectors[0][0])
        # print(scene_lidar.triangles_data[0][0])

    def modeling(self):
        self.signal = SignalGauss(5e-6, 1e6, float(self.ui.lineEdit_2.text()))
        lidar.scan(scene_lidar.triangles_data)
        lidar.t_d = float(self.ui.lineEdit_2.text())
        # lidar.scan(sphere.triangles)
        lidar.create_plot_dp(lidar.dp, figure=self.figure_dp, canvas=self.canvas_dp)
        lidar.create_plot_cloud_points(figure=self.figure_cp, canvas=self.canvas_cp)
        scene_lidar.create_plot_scene(figure=self.figure_sc, canvas=self.canvas_sc)
        self.signal.get_plot(figure=self.figure_in, canvas=self.canvas_in)
        # print(float(self.ui.lineEdit_2.text()))

    def single_modeling(self):
        directions = lidar.get_single_dir(int(self.ui.spinBox_chanel_v.value()), int(self.ui.spinBox_chanel_h.value()))
        lidar.scan(scene_lidar.triangles_data, 'single', directions)
        # lidar.scan(sphere.triangles, 'single', directions)
        lidar.get_ih(lidar.single_dp)
        lidar.create_plot_dp(lidar.single_dp, mode='single', figure=self.figure_dps, canvas=self.canvas_dps)
        lidar.create_plot_ih(figure=self.figure_ih, canvas=self.canvas_ih)
        lidar.create_plot_out_signal(self.signal.signal, figure=self.figure_out, canvas=self.canvas_out)

    def rotate_right(self):
        lidar.rotate_window('z', int(self.ui.spinBox_angle.value()))
        self.modeling()

    def rotate_left(self):
        lidar.rotate_window('z', -int(self.ui.spinBox_angle.value()))
        self.modeling()

    def rotate_up(self):
        lidar.rotate_window('x', -int(self.ui.spinBox_angle.value()))
        self.modeling()

    def rotate_down(self):
        lidar.rotate_window('x', int(self.ui.spinBox_angle.value()))
        self.modeling()

    @staticmethod
    def position():
        lidar.set_position(10, 20, 30)

    def move_forward(self):
        lidar.move_position(0, int(self.ui.spinBox_distance.value()), 0)
        # self.plot_dp.canvas.draw()
        self.modeling()

    def move_backward(self):
        lidar.move_position(0, -int(self.ui.spinBox_distance.value()), 0)
        self.modeling()

    def move_right(self):
        lidar.move_position(int(self.ui.spinBox_distance.value()), 0, 0)
        self.modeling()

    def move_left(self):
        lidar.move_position(-int(self.ui.spinBox_distance.value()), 0, 0)
        self.modeling()

    def move_up(self):
        lidar.move_position(0, 0, int(self.ui.spinBox_distance.value()))
        self.modeling()

    def move_down(self):
        lidar.move_position(0, 0, -int(self.ui.spinBox_distance.value()))
        self.modeling()

    def get_all_out(self):
        self.all_out = lidar.get_all_out_signal(scene_lidar.triangles_data, self.signal.signal)
        # self.all_out = self.all_out/(lidar.single_qr_h*lidar.single_qr_v)
        print(np.amax(self.all_out))
        self.figure_ao.clear()
        ax = self.figure_ao.add_subplot(111)
        plot = ax.imshow(self.all_out[self.i], vmax=np.amax(self.all_out))
        self.figure_ao.colorbar(plot)
        self.canvas_ao.draw()

    def swipe_chanel_plus(self):
        self.i += 1
        self.figure_ao.clear()
        ax = self.figure_ao.add_subplot(111)
        plot = ax.imshow(self.all_out[self.i], vmax=np.amax(self.all_out))
        self.figure_ao.colorbar(plot)
        self.canvas_ao.draw()
        self.ui.chanelR_spinBox.setValue(int(self.i))

    def swipe_chanel_minus(self):
        self.i -= 1
        self.figure_ao.clear()
        ax = self.figure_ao.add_subplot(111)
        plot = ax.imshow(self.all_out[self.i], vmax=np.amax(self.all_out))
        self.figure_ao.colorbar(plot)
        self.canvas_ao.draw()
        self.ui.chanelR_spinBox.setValue(int(self.i))

    def set_chanel(self):
        self.i = int(self.ui.chanelR_spinBox.value())
        self.figure_ao.clear()
        ax = self.figure_ao.add_subplot(111)
        plot = ax.imshow(self.all_out[self.i], vmax=np.amax(self.all_out))
        self.figure_ao.colorbar(plot)
        self.canvas_ao.draw()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    lidar = Lidar(45, 45, 1, 1)
    window = Gui()
    window.show()
    sys.exit(app.exec())


