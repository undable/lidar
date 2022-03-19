# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'design2.ui'
##
## Created by: Qt User Interface Compiler version 6.2.3
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QGridLayout, QHBoxLayout, QLabel,
    QLineEdit, QMainWindow, QPushButton, QSizePolicy,
    QSpacerItem, QSpinBox, QTabWidget, QVBoxLayout,
    QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(889, 849)
        font = QFont()
        font.setPointSize(9)
        MainWindow.setFont(font)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout_3 = QVBoxLayout(self.centralwidget)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.lineEdit = QLineEdit(self.centralwidget)
        self.lineEdit.setObjectName(u"lineEdit")

        self.gridLayout.addWidget(self.lineEdit, 1, 1, 1, 1)

        self.openfileButton = QPushButton(self.centralwidget)
        self.openfileButton.setObjectName(u"openfileButton")
        font1 = QFont()
        font1.setFamilies([u"Times New Roman"])
        font1.setPointSize(10)
        self.openfileButton.setFont(font1)

        self.gridLayout.addWidget(self.openfileButton, 1, 2, 1, 1)

        self.modelingButton = QPushButton(self.centralwidget)
        self.modelingButton.setObjectName(u"modelingButton")
        self.modelingButton.setFont(font1)

        self.gridLayout.addWidget(self.modelingButton, 2, 1, 1, 2)


        self.verticalLayout.addLayout(self.gridLayout)


        self.verticalLayout_2.addLayout(self.verticalLayout)

        self.horizontalLayout_7 = QHBoxLayout()
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.label_2 = QLabel(self.centralwidget)
        self.label_2.setObjectName(u"label_2")

        self.horizontalLayout_7.addWidget(self.label_2)

        self.spinBox_angle = QSpinBox(self.centralwidget)
        self.spinBox_angle.setObjectName(u"spinBox_angle")
        self.spinBox_angle.setMaximum(360)
        self.spinBox_angle.setSingleStep(10)
        self.spinBox_angle.setValue(20)

        self.horizontalLayout_7.addWidget(self.spinBox_angle)


        self.verticalLayout_2.addLayout(self.horizontalLayout_7)

        self.horizontalLayout_6 = QHBoxLayout()
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")

        self.horizontalLayout_6.addWidget(self.label)

        self.spinBox_distance = QSpinBox(self.centralwidget)
        self.spinBox_distance.setObjectName(u"spinBox_distance")
        self.spinBox_distance.setMaximum(1000)
        self.spinBox_distance.setSingleStep(10)

        self.horizontalLayout_6.addWidget(self.spinBox_distance)


        self.verticalLayout_2.addLayout(self.horizontalLayout_6)

        self.horizontalLayout_10 = QHBoxLayout()
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.label_4 = QLabel(self.centralwidget)
        self.label_4.setObjectName(u"label_4")

        self.horizontalLayout_10.addWidget(self.label_4)

        self.lineEdit_2 = QLineEdit(self.centralwidget)
        self.lineEdit_2.setObjectName(u"lineEdit_2")
        self.lineEdit_2.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.horizontalLayout_10.addWidget(self.lineEdit_2)


        self.verticalLayout_2.addLayout(self.horizontalLayout_10)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.rotate_upButton = QPushButton(self.centralwidget)
        self.rotate_upButton.setObjectName(u"rotate_upButton")

        self.horizontalLayout_4.addWidget(self.rotate_upButton)

        self.rotate_downButton = QPushButton(self.centralwidget)
        self.rotate_downButton.setObjectName(u"rotate_downButton")

        self.horizontalLayout_4.addWidget(self.rotate_downButton)


        self.verticalLayout_2.addLayout(self.horizontalLayout_4)

        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.rotate_rightButton = QPushButton(self.centralwidget)
        self.rotate_rightButton.setObjectName(u"rotate_rightButton")

        self.horizontalLayout_5.addWidget(self.rotate_rightButton)

        self.rotate_leftButton = QPushButton(self.centralwidget)
        self.rotate_leftButton.setObjectName(u"rotate_leftButton")

        self.horizontalLayout_5.addWidget(self.rotate_leftButton)


        self.verticalLayout_2.addLayout(self.horizontalLayout_5)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.upButton = QPushButton(self.centralwidget)
        self.upButton.setObjectName(u"upButton")

        self.horizontalLayout_2.addWidget(self.upButton)

        self.downButton = QPushButton(self.centralwidget)
        self.downButton.setObjectName(u"downButton")

        self.horizontalLayout_2.addWidget(self.downButton)


        self.verticalLayout_2.addLayout(self.horizontalLayout_2)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.forwardButton = QPushButton(self.centralwidget)
        self.forwardButton.setObjectName(u"forwardButton")

        self.horizontalLayout_3.addWidget(self.forwardButton)

        self.backwardButton = QPushButton(self.centralwidget)
        self.backwardButton.setObjectName(u"backwardButton")

        self.horizontalLayout_3.addWidget(self.backwardButton)


        self.verticalLayout_2.addLayout(self.horizontalLayout_3)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.leftButton = QPushButton(self.centralwidget)
        self.leftButton.setObjectName(u"leftButton")

        self.horizontalLayout.addWidget(self.leftButton)

        self.rightButton = QPushButton(self.centralwidget)
        self.rightButton.setObjectName(u"rightButton")

        self.horizontalLayout.addWidget(self.rightButton)


        self.verticalLayout_2.addLayout(self.horizontalLayout)


        self.verticalLayout_3.addLayout(self.verticalLayout_2)

        self.horizontalLayout_9 = QHBoxLayout()
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.spinBox_chanel_v = QSpinBox(self.centralwidget)
        self.spinBox_chanel_v.setObjectName(u"spinBox_chanel_v")

        self.horizontalLayout_9.addWidget(self.spinBox_chanel_v)

        self.spinBox_chanel_h = QSpinBox(self.centralwidget)
        self.spinBox_chanel_h.setObjectName(u"spinBox_chanel_h")

        self.horizontalLayout_9.addWidget(self.spinBox_chanel_h)

        self.spinBox = QSpinBox(self.centralwidget)
        self.spinBox.setObjectName(u"spinBox")
        self.spinBox.setMaximum(99999)

        self.horizontalLayout_9.addWidget(self.spinBox)

        self.single_chanelButton = QPushButton(self.centralwidget)
        self.single_chanelButton.setObjectName(u"single_chanelButton")

        self.horizontalLayout_9.addWidget(self.single_chanelButton)


        self.verticalLayout_3.addLayout(self.horizontalLayout_9)

        self.tabWidget = QTabWidget(self.centralwidget)
        self.tabWidget.setObjectName(u"tabWidget")
        self.tab_5 = QWidget()
        self.tab_5.setObjectName(u"tab_5")
        self.verticalLayoutWidget = QWidget(self.tab_5)
        self.verticalLayoutWidget.setObjectName(u"verticalLayoutWidget")
        self.verticalLayoutWidget.setGeometry(QRect(0, 0, 701, 421))
        self.verticalLayout_4 = QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.tabWidget.addTab(self.tab_5, "")
        self.tab_6 = QWidget()
        self.tab_6.setObjectName(u"tab_6")
        self.verticalLayoutWidget_2 = QWidget(self.tab_6)
        self.verticalLayoutWidget_2.setObjectName(u"verticalLayoutWidget_2")
        self.verticalLayoutWidget_2.setGeometry(QRect(0, 0, 691, 431))
        self.verticalLayout_5 = QVBoxLayout(self.verticalLayoutWidget_2)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.tabWidget.addTab(self.tab_6, "")
        self.tab_7 = QWidget()
        self.tab_7.setObjectName(u"tab_7")
        self.verticalLayoutWidget_3 = QWidget(self.tab_7)
        self.verticalLayoutWidget_3.setObjectName(u"verticalLayoutWidget_3")
        self.verticalLayoutWidget_3.setGeometry(QRect(0, 0, 691, 431))
        self.verticalLayout_6 = QVBoxLayout(self.verticalLayoutWidget_3)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.verticalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.tabWidget.addTab(self.tab_7, "")
        self.tab = QWidget()
        self.tab.setObjectName(u"tab")
        self.verticalLayoutWidget_4 = QWidget(self.tab)
        self.verticalLayoutWidget_4.setObjectName(u"verticalLayoutWidget_4")
        self.verticalLayoutWidget_4.setGeometry(QRect(0, 0, 691, 421))
        self.verticalLayout_7 = QVBoxLayout(self.verticalLayoutWidget_4)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.verticalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QWidget()
        self.tab_2.setObjectName(u"tab_2")
        self.verticalLayoutWidget_5 = QWidget(self.tab_2)
        self.verticalLayoutWidget_5.setObjectName(u"verticalLayoutWidget_5")
        self.verticalLayoutWidget_5.setGeometry(QRect(0, 0, 711, 421))
        self.verticalLayout_8 = QVBoxLayout(self.verticalLayoutWidget_5)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.verticalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.tabWidget.addTab(self.tab_2, "")
        self.tab_3 = QWidget()
        self.tab_3.setObjectName(u"tab_3")
        self.verticalLayoutWidget_6 = QWidget(self.tab_3)
        self.verticalLayoutWidget_6.setObjectName(u"verticalLayoutWidget_6")
        self.verticalLayoutWidget_6.setGeometry(QRect(0, 0, 691, 431))
        self.verticalLayout_9 = QVBoxLayout(self.verticalLayoutWidget_6)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.verticalLayout_9.setContentsMargins(0, 0, 0, 0)
        self.tabWidget.addTab(self.tab_3, "")
        self.tab_4 = QWidget()
        self.tab_4.setObjectName(u"tab_4")
        self.verticalLayoutWidget_7 = QWidget(self.tab_4)
        self.verticalLayoutWidget_7.setObjectName(u"verticalLayoutWidget_7")
        self.verticalLayoutWidget_7.setGeometry(QRect(0, 0, 691, 421))
        self.verticalLayout_10 = QVBoxLayout(self.verticalLayoutWidget_7)
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.verticalLayout_10.setContentsMargins(0, 0, 0, 0)
        self.tabWidget.addTab(self.tab_4, "")
        self.tab_8 = QWidget()
        self.tab_8.setObjectName(u"tab_8")
        self.verticalLayoutWidget_8 = QWidget(self.tab_8)
        self.verticalLayoutWidget_8.setObjectName(u"verticalLayoutWidget_8")
        self.verticalLayoutWidget_8.setGeometry(QRect(0, 0, 641, 441))
        self.verticalLayout_11 = QVBoxLayout(self.verticalLayoutWidget_8)
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.verticalLayout_11.setContentsMargins(0, 0, 0, 0)
        self.verticalLayoutWidget_9 = QWidget(self.tab_8)
        self.verticalLayoutWidget_9.setObjectName(u"verticalLayoutWidget_9")
        self.verticalLayoutWidget_9.setGeometry(QRect(650, 10, 201, 301))
        self.verticalLayout_12 = QVBoxLayout(self.verticalLayoutWidget_9)
        self.verticalLayout_12.setObjectName(u"verticalLayout_12")
        self.verticalLayout_12.setContentsMargins(0, 0, 0, 0)
        self.getallout_Button = QPushButton(self.verticalLayoutWidget_9)
        self.getallout_Button.setObjectName(u"getallout_Button")

        self.verticalLayout_12.addWidget(self.getallout_Button)

        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_12.addItem(self.verticalSpacer_2)

        self.pluschanel_Button = QPushButton(self.verticalLayoutWidget_9)
        self.pluschanel_Button.setObjectName(u"pluschanel_Button")

        self.verticalLayout_12.addWidget(self.pluschanel_Button)

        self.minuschanel_Button = QPushButton(self.verticalLayoutWidget_9)
        self.minuschanel_Button.setObjectName(u"minuschanel_Button")

        self.verticalLayout_12.addWidget(self.minuschanel_Button)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_12.addItem(self.verticalSpacer)

        self.label_3 = QLabel(self.verticalLayoutWidget_9)
        self.label_3.setObjectName(u"label_3")

        self.verticalLayout_12.addWidget(self.label_3)

        self.chanelR_spinBox = QSpinBox(self.verticalLayoutWidget_9)
        self.chanelR_spinBox.setObjectName(u"chanelR_spinBox")
        self.chanelR_spinBox.setMaximum(999)

        self.verticalLayout_12.addWidget(self.chanelR_spinBox)

        self.chanelR_Button = QPushButton(self.verticalLayoutWidget_9)
        self.chanelR_Button.setObjectName(u"chanelR_Button")

        self.verticalLayout_12.addWidget(self.chanelR_Button)

        self.tabWidget.addTab(self.tab_8, "")

        self.verticalLayout_3.addWidget(self.tabWidget)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        self.tabWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Lidar", None))
        self.openfileButton.setText(QCoreApplication.translate("MainWindow", u"\u0412\u044b\u0431\u0440\u0430\u0442\u044c \u0444\u0430\u0439\u043b", None))
        self.modelingButton.setText(QCoreApplication.translate("MainWindow", u"\u041c\u043e\u0434\u0435\u043b\u0438\u0440\u043e\u0432\u0430\u043d\u0438\u0435", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"\u0423\u0433\u043e\u043b \u043f\u043e\u0432\u043e\u0440\u043e\u0442\u0430", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"\u0412\u0435\u043b\u0438\u0447\u0438\u043d\u0430 \u0441\u043c\u0435\u0449\u0435\u043d\u0438\u044f", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"\u0418\u043d\u0442\u0435\u0440\u0432\u0430\u043b \u0434\u0438\u0441\u043a\u0440\u0435\u0442\u0438\u0437\u0430\u0446\u0438\u0438", None))
        self.lineEdit_2.setText(QCoreApplication.translate("MainWindow", u"5e-8", None))
        self.rotate_upButton.setText(QCoreApplication.translate("MainWindow", u"\u041f\u043e\u0432\u0435\u0440\u043d\u0443\u0442\u044c \u0432\u0432\u0435\u0440\u0445", None))
        self.rotate_downButton.setText(QCoreApplication.translate("MainWindow", u"\u041f\u043e\u0432\u0435\u0440\u043d\u0443\u0442\u044c \u0432\u043d\u0438\u0437", None))
        self.rotate_rightButton.setText(QCoreApplication.translate("MainWindow", u"\u041f\u043e\u0432\u0435\u0440\u043d\u0443\u0442\u044c \u0432\u043f\u0440\u0430\u0432\u043e", None))
        self.rotate_leftButton.setText(QCoreApplication.translate("MainWindow", u"\u041f\u043e\u0432\u0435\u0440\u043d\u0443\u0442\u044c \u0432\u043b\u0435\u0432\u043e", None))
        self.upButton.setText(QCoreApplication.translate("MainWindow", u"\u0412\u0432\u0435\u0440\u0445", None))
        self.downButton.setText(QCoreApplication.translate("MainWindow", u"\u0412\u043d\u0438\u0437", None))
        self.forwardButton.setText(QCoreApplication.translate("MainWindow", u"\u0412\u043f\u0435\u0440\u0451\u0434", None))
        self.backwardButton.setText(QCoreApplication.translate("MainWindow", u"\u041d\u0430\u0437\u0430\u0434", None))
        self.leftButton.setText(QCoreApplication.translate("MainWindow", u"\u0412\u043b\u0435\u0432\u043e", None))
        self.rightButton.setText(QCoreApplication.translate("MainWindow", u"\u0412\u043f\u0440\u0430\u0432\u043e", None))
        self.single_chanelButton.setText(QCoreApplication.translate("MainWindow", u"\u041c\u043e\u0434\u0435\u043b\u0438\u0440\u043e\u0432\u0430\u043d\u0438\u0435 1 \u043a\u0430\u043d\u0430\u043b\u0430", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_5), QCoreApplication.translate("MainWindow", u"\u0414\u0430\u043b\u044c\u043d\u043e\u0441\u0442\u043d\u044b\u0439 \u043f\u043e\u0440\u0442\u0440\u0435\u0442", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_6), QCoreApplication.translate("MainWindow", u"\u041e\u0431\u043b\u0430\u043a\u043e \u0442\u043e\u0447\u0435\u043a", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_7), QCoreApplication.translate("MainWindow", u"\u0421\u0446\u0435\u043d\u0430", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), QCoreApplication.translate("MainWindow", u"\u0412\u0445. \u0441\u0438\u0433\u043d\u0430\u043b", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), QCoreApplication.translate("MainWindow", u"\u0418\u0425", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_3), QCoreApplication.translate("MainWindow", u"\u0412\u044b\u0445. \u0441\u0438\u0433\u043d\u0430\u043b", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_4), QCoreApplication.translate("MainWindow", u"\u0414\u041f", None))
        self.getallout_Button.setText(QCoreApplication.translate("MainWindow", u"\u0421\u043e\u0431\u0440\u0430\u0442\u044c \u0434\u0430\u043d\u043d\u044b\u0435", None))
        self.pluschanel_Button.setText(QCoreApplication.translate("MainWindow", u"+1 \u043a\u0430\u043d\u0430\u043b", None))
        self.minuschanel_Button.setText(QCoreApplication.translate("MainWindow", u"-1 \u043a\u0430\u043d\u0430\u043b", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"\u0412\u044b\u0431\u0440\u0430\u0442\u044c \u043a\u0430\u043d\u0430\u043b", None))
        self.chanelR_Button.setText(QCoreApplication.translate("MainWindow", u"\u0412\u044b\u0431\u0440\u0430\u0442\u044c \u043a\u0430\u043d\u0430\u043b", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_8), QCoreApplication.translate("MainWindow", u"\u0414\u0421", None))
    # retranslateUi

