# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'F:\PythonFiles\Programs\real_time_rate_pitch_change\rate_pitch\MainWindow.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1000, 600)
        MainWindow.setMinimumSize(QtCore.QSize(1000, 600))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.centralwidget.sizePolicy().hasHeightForWidth())
        self.centralwidget.setSizePolicy(sizePolicy)
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.widget = QtWidgets.QWidget(self.centralwidget)
        self.widget.setObjectName("widget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.widget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.tableWidget = QtWidgets.QTableWidget(self.widget)
        self.tableWidget.setRowCount(6)
        self.tableWidget.setColumnCount(2)
        self.tableWidget.setObjectName("tableWidget")
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        item.setFlags(QtCore.Qt.ItemIsSelectable|QtCore.Qt.ItemIsDragEnabled|QtCore.Qt.ItemIsDropEnabled|QtCore.Qt.ItemIsUserCheckable|QtCore.Qt.ItemIsEnabled)
        self.tableWidget.setItem(0, 0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(0, 1, item)
        item = QtWidgets.QTableWidgetItem()
        item.setFlags(QtCore.Qt.ItemIsSelectable|QtCore.Qt.ItemIsDragEnabled|QtCore.Qt.ItemIsDropEnabled|QtCore.Qt.ItemIsUserCheckable|QtCore.Qt.ItemIsEnabled)
        self.tableWidget.setItem(1, 0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(1, 1, item)
        item = QtWidgets.QTableWidgetItem()
        item.setFlags(QtCore.Qt.ItemIsSelectable|QtCore.Qt.ItemIsDragEnabled|QtCore.Qt.ItemIsDropEnabled|QtCore.Qt.ItemIsUserCheckable|QtCore.Qt.ItemIsEnabled)
        self.tableWidget.setItem(2, 0, item)
        item = QtWidgets.QTableWidgetItem()
        item.setFlags(QtCore.Qt.ItemIsSelectable|QtCore.Qt.ItemIsDragEnabled|QtCore.Qt.ItemIsDropEnabled|QtCore.Qt.ItemIsUserCheckable|QtCore.Qt.ItemIsEnabled)
        self.tableWidget.setItem(3, 0, item)
        item = QtWidgets.QTableWidgetItem()
        item.setFlags(QtCore.Qt.ItemIsSelectable|QtCore.Qt.ItemIsDragEnabled|QtCore.Qt.ItemIsDropEnabled|QtCore.Qt.ItemIsUserCheckable|QtCore.Qt.ItemIsEnabled)
        self.tableWidget.setItem(4, 0, item)
        item = QtWidgets.QTableWidgetItem()
        item.setFlags(QtCore.Qt.ItemIsSelectable|QtCore.Qt.ItemIsDragEnabled|QtCore.Qt.ItemIsDropEnabled|QtCore.Qt.ItemIsUserCheckable|QtCore.Qt.ItemIsEnabled)
        self.tableWidget.setItem(5, 0, item)
        self.tableWidget.verticalHeader().setVisible(False)
        self.verticalLayout.addWidget(self.tableWidget)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.verticalLayout.addItem(spacerItem)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.label_time = QtWidgets.QLabel(self.widget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_time.sizePolicy().hasHeightForWidth())
        self.label_time.setSizePolicy(sizePolicy)
        self.label_time.setObjectName("label_time")
        self.horizontalLayout_3.addWidget(self.label_time)
        self.horizontalSlider_time = QtWidgets.QSlider(self.widget)
        self.horizontalSlider_time.setSingleStep(1000)
        self.horizontalSlider_time.setPageStep(60000)
        self.horizontalSlider_time.setTracking(False)
        self.horizontalSlider_time.setOrientation(QtCore.Qt.Horizontal)
        self.horizontalSlider_time.setTickPosition(QtWidgets.QSlider.TicksAbove)
        self.horizontalSlider_time.setTickInterval(60000)
        self.horizontalSlider_time.setObjectName("horizontalSlider_time")
        self.horizontalLayout_3.addWidget(self.horizontalSlider_time)
        self.verticalLayout.addLayout(self.horizontalLayout_3)
        spacerItem1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.verticalLayout.addItem(spacerItem1)
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setVerticalSpacing(14)
        self.gridLayout.setObjectName("gridLayout")
        self.pushButton_pitch = QtWidgets.QPushButton(self.widget)
        self.pushButton_pitch.setObjectName("pushButton_pitch")
        self.gridLayout.addWidget(self.pushButton_pitch, 1, 3, 1, 1)
        self.label_5 = QtWidgets.QLabel(self.widget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_5.sizePolicy().hasHeightForWidth())
        self.label_5.setSizePolicy(sizePolicy)
        self.label_5.setObjectName("label_5")
        self.gridLayout.addWidget(self.label_5, 1, 0, 1, 1)
        self.horizontalSlider_rate = QtWidgets.QSlider(self.widget)
        self.horizontalSlider_rate.setMinimum(-75)
        self.horizontalSlider_rate.setMaximum(200)
        self.horizontalSlider_rate.setSingleStep(5)
        self.horizontalSlider_rate.setProperty("value", 0)
        self.horizontalSlider_rate.setTracking(False)
        self.horizontalSlider_rate.setOrientation(QtCore.Qt.Horizontal)
        self.horizontalSlider_rate.setTickPosition(QtWidgets.QSlider.TicksAbove)
        self.horizontalSlider_rate.setTickInterval(25)
        self.horizontalSlider_rate.setObjectName("horizontalSlider_rate")
        self.gridLayout.addWidget(self.horizontalSlider_rate, 0, 1, 1, 1)
        self.doubleSpinBox_tempo = QtWidgets.QDoubleSpinBox(self.widget)
        self.doubleSpinBox_tempo.setDecimals(0)
        self.doubleSpinBox_tempo.setMinimum(-75.0)
        self.doubleSpinBox_tempo.setMaximum(200.0)
        self.doubleSpinBox_tempo.setSingleStep(5.0)
        self.doubleSpinBox_tempo.setProperty("value", 0.0)
        self.doubleSpinBox_tempo.setObjectName("doubleSpinBox_tempo")
        self.gridLayout.addWidget(self.doubleSpinBox_tempo, 2, 2, 1, 1)
        self.doubleSpinBox_rate = QtWidgets.QDoubleSpinBox(self.widget)
        self.doubleSpinBox_rate.setDecimals(0)
        self.doubleSpinBox_rate.setMinimum(-75.0)
        self.doubleSpinBox_rate.setMaximum(200.0)
        self.doubleSpinBox_rate.setSingleStep(5.0)
        self.doubleSpinBox_rate.setProperty("value", 0.0)
        self.doubleSpinBox_rate.setObjectName("doubleSpinBox_rate")
        self.gridLayout.addWidget(self.doubleSpinBox_rate, 0, 2, 1, 1)
        self.horizontalSlider_pitch = QtWidgets.QSlider(self.widget)
        self.horizontalSlider_pitch.setMinimum(-1200)
        self.horizontalSlider_pitch.setMaximum(1200)
        self.horizontalSlider_pitch.setSingleStep(10)
        self.horizontalSlider_pitch.setPageStep(100)
        self.horizontalSlider_pitch.setTracking(False)
        self.horizontalSlider_pitch.setOrientation(QtCore.Qt.Horizontal)
        self.horizontalSlider_pitch.setTickPosition(QtWidgets.QSlider.TicksAbove)
        self.horizontalSlider_pitch.setTickInterval(100)
        self.horizontalSlider_pitch.setObjectName("horizontalSlider_pitch")
        self.gridLayout.addWidget(self.horizontalSlider_pitch, 1, 1, 1, 1)
        self.label_4 = QtWidgets.QLabel(self.widget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_4.sizePolicy().hasHeightForWidth())
        self.label_4.setSizePolicy(sizePolicy)
        self.label_4.setObjectName("label_4")
        self.gridLayout.addWidget(self.label_4, 0, 0, 1, 1)
        self.doubleSpinBox_pitch = QtWidgets.QDoubleSpinBox(self.widget)
        self.doubleSpinBox_pitch.setMinimum(-12.0)
        self.doubleSpinBox_pitch.setMaximum(12.0)
        self.doubleSpinBox_pitch.setSingleStep(0.1)
        self.doubleSpinBox_pitch.setObjectName("doubleSpinBox_pitch")
        self.gridLayout.addWidget(self.doubleSpinBox_pitch, 1, 2, 1, 1)
        self.label_6 = QtWidgets.QLabel(self.widget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_6.sizePolicy().hasHeightForWidth())
        self.label_6.setSizePolicy(sizePolicy)
        self.label_6.setObjectName("label_6")
        self.gridLayout.addWidget(self.label_6, 2, 0, 1, 1)
        self.pushButton_rate = QtWidgets.QPushButton(self.widget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_rate.sizePolicy().hasHeightForWidth())
        self.pushButton_rate.setSizePolicy(sizePolicy)
        self.pushButton_rate.setObjectName("pushButton_rate")
        self.gridLayout.addWidget(self.pushButton_rate, 0, 3, 1, 1)
        self.horizontalSlider_tempo = QtWidgets.QSlider(self.widget)
        self.horizontalSlider_tempo.setMinimum(-75)
        self.horizontalSlider_tempo.setMaximum(200)
        self.horizontalSlider_tempo.setSingleStep(5)
        self.horizontalSlider_tempo.setProperty("value", 0)
        self.horizontalSlider_tempo.setTracking(False)
        self.horizontalSlider_tempo.setOrientation(QtCore.Qt.Horizontal)
        self.horizontalSlider_tempo.setTickPosition(QtWidgets.QSlider.TicksAbove)
        self.horizontalSlider_tempo.setTickInterval(25)
        self.horizontalSlider_tempo.setObjectName("horizontalSlider_tempo")
        self.gridLayout.addWidget(self.horizontalSlider_tempo, 2, 1, 1, 1)
        self.pushButton_tempo = QtWidgets.QPushButton(self.widget)
        self.pushButton_tempo.setObjectName("pushButton_tempo")
        self.gridLayout.addWidget(self.pushButton_tempo, 2, 3, 1, 1)
        self.verticalLayout.addLayout(self.gridLayout)
        spacerItem2 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.verticalLayout.addItem(spacerItem2)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.radioButton_loop = QtWidgets.QRadioButton(self.widget)
        self.radioButton_loop.setMaximumSize(QtCore.QSize(100, 16777215))
        self.radioButton_loop.setObjectName("radioButton_loop")
        self.horizontalLayout_2.addWidget(self.radioButton_loop)
        self.pushButton_play = QtWidgets.QPushButton(self.widget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_play.sizePolicy().hasHeightForWidth())
        self.pushButton_play.setSizePolicy(sizePolicy)
        self.pushButton_play.setMinimumSize(QtCore.QSize(100, 50))
        self.pushButton_play.setObjectName("pushButton_play")
        self.horizontalLayout_2.addWidget(self.pushButton_play)
        self.pushButton_begin = QtWidgets.QPushButton(self.widget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_begin.sizePolicy().hasHeightForWidth())
        self.pushButton_begin.setSizePolicy(sizePolicy)
        self.pushButton_begin.setMinimumSize(QtCore.QSize(100, 40))
        self.pushButton_begin.setObjectName("pushButton_begin")
        self.horizontalLayout_2.addWidget(self.pushButton_begin)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.horizontalLayout.addWidget(self.widget)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1000, 26))
        self.menubar.setObjectName("menubar")
        self.menu_file = QtWidgets.QMenu(self.menubar)
        self.menu_file.setObjectName("menu_file")
        self.menu_help = QtWidgets.QMenu(self.menubar)
        self.menu_help.setObjectName("menu_help")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.action_open = QtWidgets.QAction(MainWindow)
        self.action_open.setObjectName("action_open")
        self.action_save = QtWidgets.QAction(MainWindow)
        self.action_save.setObjectName("action_save")
        self.action_exit = QtWidgets.QAction(MainWindow)
        self.action_exit.setObjectName("action_exit")
        self.action_aboutqt = QtWidgets.QAction(MainWindow)
        self.action_aboutqt.setObjectName("action_aboutqt")
        self.action_usinghelp = QtWidgets.QAction(MainWindow)
        self.action_usinghelp.setObjectName("action_usinghelp")
        self.menu_file.addAction(self.action_open)
        self.menu_file.addAction(self.action_save)
        self.menu_file.addSeparator()
        self.menu_file.addAction(self.action_exit)
        self.menu_help.addAction(self.action_usinghelp)
        self.menu_help.addAction(self.action_aboutqt)
        self.menubar.addAction(self.menu_file.menuAction())
        self.menubar.addAction(self.menu_help.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        MainWindow.setTabOrder(self.tableWidget, self.horizontalSlider_time)
        MainWindow.setTabOrder(self.horizontalSlider_time, self.horizontalSlider_rate)
        MainWindow.setTabOrder(self.horizontalSlider_rate, self.doubleSpinBox_rate)
        MainWindow.setTabOrder(self.doubleSpinBox_rate, self.pushButton_rate)
        MainWindow.setTabOrder(self.pushButton_rate, self.horizontalSlider_pitch)
        MainWindow.setTabOrder(self.horizontalSlider_pitch, self.doubleSpinBox_pitch)
        MainWindow.setTabOrder(self.doubleSpinBox_pitch, self.pushButton_pitch)
        MainWindow.setTabOrder(self.pushButton_pitch, self.horizontalSlider_tempo)
        MainWindow.setTabOrder(self.horizontalSlider_tempo, self.doubleSpinBox_tempo)
        MainWindow.setTabOrder(self.doubleSpinBox_tempo, self.pushButton_tempo)
        MainWindow.setTabOrder(self.pushButton_tempo, self.radioButton_loop)
        MainWindow.setTabOrder(self.radioButton_loop, self.pushButton_play)
        MainWindow.setTabOrder(self.pushButton_play, self.pushButton_begin)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "实时变速变调"))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "名称"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "值"))
        __sortingEnabled = self.tableWidget.isSortingEnabled()
        self.tableWidget.setSortingEnabled(False)
        item = self.tableWidget.item(0, 0)
        item.setText(_translate("MainWindow", "文件名"))
        item = self.tableWidget.item(1, 0)
        item.setText(_translate("MainWindow", "文件大小"))
        item = self.tableWidget.item(2, 0)
        item.setText(_translate("MainWindow", "持续时间"))
        item = self.tableWidget.item(3, 0)
        item.setText(_translate("MainWindow", "采样率"))
        item = self.tableWidget.item(4, 0)
        item.setText(_translate("MainWindow", "声道数"))
        item = self.tableWidget.item(5, 0)
        item.setText(_translate("MainWindow", "采样比特"))
        self.tableWidget.setSortingEnabled(__sortingEnabled)
        self.label_time.setText(_translate("MainWindow", "00:00:00.000"))
        self.pushButton_pitch.setText(_translate("MainWindow", "重置"))
        self.label_5.setText(_translate("MainWindow", "变调（半音阶）"))
        self.label_4.setText(_translate("MainWindow", "变速（百分比）"))
        self.label_6.setText(_translate("MainWindow", "变拍（百分比）"))
        self.pushButton_rate.setText(_translate("MainWindow", "重置"))
        self.pushButton_tempo.setText(_translate("MainWindow", "重置"))
        self.radioButton_loop.setText(_translate("MainWindow", "循环"))
        self.pushButton_play.setText(_translate("MainWindow", "播放"))
        self.pushButton_begin.setText(_translate("MainWindow", "从头开始"))
        self.menu_file.setTitle(_translate("MainWindow", "文件"))
        self.menu_help.setTitle(_translate("MainWindow", "帮助"))
        self.action_open.setText(_translate("MainWindow", "打开"))
        self.action_open.setShortcut(_translate("MainWindow", "Ctrl+O"))
        self.action_save.setText(_translate("MainWindow", "另存为"))
        self.action_save.setShortcut(_translate("MainWindow", "Ctrl+S"))
        self.action_exit.setText(_translate("MainWindow", "退出"))
        self.action_exit.setShortcut(_translate("MainWindow", "Esc"))
        self.action_aboutqt.setText(_translate("MainWindow", "关于 Qt"))
        self.action_usinghelp.setText(_translate("MainWindow", "使用帮助"))
        self.action_usinghelp.setShortcut(_translate("MainWindow", "F1"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
