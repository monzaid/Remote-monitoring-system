from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QPixmap

class Ui_monitor(object):
    def setupUi(self, monitor):
        monitor.setObjectName("monitor")
        monitor.resize(648, 620)
        self.centralwidget = QtWidgets.QWidget(monitor)
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(0, 490, 641, 41))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.pushButton_3 = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.pushButton_3.setObjectName("pushButton_3")
        self.horizontalLayout.addWidget(self.pushButton_3)
        self.pushButton_2 = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.pushButton_2.setObjectName("pushButton_2")
        self.horizontalLayout.addWidget(self.pushButton_2)
        self.pushButton = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.pushButton.setObjectName("pushButton")
        self.horizontalLayout.addWidget(self.pushButton)
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(0, 0, 641, 481))
        self.label.setObjectName("label")
        self.horizontalLayoutWidget_2 = QtWidgets.QWidget(self.centralwidget)
        self.horizontalLayoutWidget_2.setGeometry(QtCore.QRect(0, 530, 641, 51))
        self.horizontalLayoutWidget_2.setObjectName("horizontalLayoutWidget_2")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_2)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_3 = QtWidgets.QLabel(self.horizontalLayoutWidget_2)
        self.label_3.setObjectName("label_3")
        self.horizontalLayout_2.addWidget(self.label_3)
        self.lineEdit = QtWidgets.QLineEdit(self.horizontalLayoutWidget_2)
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit.setText('127.0.0.1')
        self.horizontalLayout_2.addWidget(self.lineEdit)
        self.label_2 = QtWidgets.QLabel(self.horizontalLayoutWidget_2)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_2.addWidget(self.label_2)
        self.lineEdit_2 = QtWidgets.QLineEdit(self.horizontalLayoutWidget_2)
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.lineEdit_2.setText('6666')
        self.horizontalLayout_2.addWidget(self.lineEdit_2)
        self.pushButton_4 = QtWidgets.QPushButton(self.horizontalLayoutWidget_2)
        self.pushButton_4.setObjectName("pushButton_4")
        self.horizontalLayout_2.addWidget(self.pushButton_4)
        monitor.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(monitor)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 648, 23))
        self.menubar.setObjectName("menubar")
        monitor.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(monitor)
        self.statusbar.setObjectName("statusbar")
        monitor.setStatusBar(self.statusbar)

        self.retranslateUi(monitor)
        QtCore.QMetaObject.connectSlotsByName(monitor)

    def retranslateUi(self, monitor):
        _translate = QtCore.QCoreApplication.translate
        monitor.setWindowTitle(_translate("monitor", "MainWindow"))
        self.pushButton_3.setText(_translate("monitor", "实时监控"))
        self.pushButton_2.setText(_translate("monitor", "录制"))
        self.pushButton.setText(_translate("monitor", "回放"))
        self.label.setText(_translate("monitor", "请开始你的表演！"))
        self.label_3.setText(_translate("monitor", "IP地址"))
        self.label_2.setText(_translate("monitor", "端口"))
        self.pushButton_4.setText(_translate("monitor", "监听"))
        self.label.setPixmap(QPixmap('./load.jpg'))