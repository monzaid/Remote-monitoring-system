import os, sys, time, cv2, monitor, threading
import socket
import struct

import numpy
from PyQt5 import QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox, QFileDialog

# 定义opencv图像转PyQt图像的函数
def cvImgtoQtImg(cvImg):
    QtImgBuf = cv2.cvtColor(cvImg, cv2.COLOR_BGR2BGRA)
    QtImg = QtGui.QImage(QtImgBuf.data,
                         QtImgBuf.shape[1],
                         QtImgBuf.shape[0],
                         QtGui.QImage.Format_RGB32)
    return QtImg

class mainwin(QtWidgets.QMainWindow,monitor.Ui_monitor):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.bClose = False
        self.out = 1  # 视频文件
        self.cap = 1  # 视频帧
        # 当前状态
        self.type = {'enable':1, 'display':2, 'ensave':3, 'relink':4}
        self.status = self.type['enable']
        # 信号与槽
        self.pushButton_3.clicked.connect(self.openMonitor)  # 建立菜单点击的信号与方法openMonitor连接
        self.pushButton.clicked.connect(self.openVideo)  # 建立菜单点击的信号与方法openVideo连接
        self.pushButton_2.clicked.connect(self.saveVideo)  # 建立菜单点击的信号与方法saveVideo连接
        self.pushButton_4.clicked.connect(self.monitor)

    def runing(self):
        self.client, self.addr = self.Server.accept()
        fps = 24  # 设置帧率
        while True:
            tempdata = self.client.recv(8)
            if len(tempdata) == 0:
                print("+1")
                continue
            info = struct.unpack('lhh', tempdata)
            buf_size = int(info[0])

            if buf_size:
                try:
                    # 把数据解码为opencv图像
                    self.buf = b""
                    self.temp_buf = self.buf
                    while buf_size:
                        self.temp_buf = self.client.recv(buf_size)
                        buf_size -= len(self.temp_buf)
                        self.buf += self.temp_buf
                    data = numpy.fromstring(self.buf, dtype='uint8')

                    frame = cv2.imdecode(data, 1)
                    # 录制视频
                    if self.status == self.type['ensave']:
                        self.out.write(frame)
                    elif self.status == self.type['display']:
                        ret, frame = self.cap.read()
                        if not ret:
                            print('结束了')
                            # break
                    elif self.status == self.type['relink']:
                        self.status = self.type['enable']
                        break
                    # opencv图像转换pyqt图像
                    QtImg = cvImgtoQtImg(frame)  # 将帧数据转换为PyQt图像格式
                    self.label.setPixmap(QtGui.QPixmap.fromImage(QtImg))  # 在ImgDisp显示图像
                    size = QtImg.size()
                    self.label.resize(size)  # 根据帧大小调整标签大小
                    self.label.show()  # 刷新界面
                    cv2.waitKey(int(1000 / fps))  # 休眠一会，确保每秒播放fps帧
                except Exception as e:
                    print(e.args)

        # 完成所有操作后，释放捕获器
        cv2.destroyAllWindows()

    # 实时监控
    def openMonitor(self):
        if self.status == self.type['display']:
            self.status = self.type['enable']
            t = threading.Thread(target=self.runing)
            t.start()

    # 录制视频
    def saveVideo(self):
        if self.status == self.type['enable']:  # 录制
            print('a')
            self.status = self.type['ensave']
            filename = time.strftime("%Y-%m-%d-%H-%M-%S.avi", time.localtime())  # 视频文件名
            self.pushButton_2.setText('保存')
            fourcc = cv2.VideoWriter_fourcc(*'XVID')
            self.out = cv2.VideoWriter(filename, fourcc, 20.0, (640, 480))
        elif self.status == self.type['ensave']:  # 保存
            self.status = self.type['enable']
            self.pushButton_2.setText('录制')
            self.out.release()

    # 回放
    def openVideo(self):
        if self.status == self.type['ensave']:  #打开文件
            self.status = self.type['enable']
            self.pushButton_2.setText('录制')
            self.out.release()
        fileName_choose, filetype = QFileDialog.getOpenFileName(self,
                                                                "选取文件",
                                                                os.getcwd(),  # 起始路径
                                                                "avi Files (*.avi)")  # 设置文件扩展名过滤,用双分号间隔

        if fileName_choose == "":
            print("\n取消选择")
            return

        self.status = self.type['display']
        # 回放
        self.cap = cv2.VideoCapture(fileName_choose)  # 播放视频
        if not self.cap.isOpened():
            print("Cannot open monitor")
            QMessageBox.question(self, '警告', '找不到文件！')
            exit()

    def monitor(self):
        # 上传服务器
        self.TargetIP = ('127.0.0.1', 6666)
        self.Server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # 生成新的套接字对象
        self.Server.bind(self.TargetIP)
        self.Server.listen(5)
        # 线程
        t = threading.Thread(target=self.runing)
        t.start()


    def closeEvent(self, event):
        """
        重写closeEvent方法，实现dialog窗体关闭时执行一些代码
        :param event: close()触发的事件
        :return: None
        """
        reply = QtWidgets.QMessageBox.question(self,
                                               '本程序',
                                               "是否要退出程序？",
                                               QtWidgets.QMessageBox.Yes | QtWidgets.QMessageBox.No,
                                               QtWidgets.QMessageBox.No)
        if reply == QtWidgets.QMessageBox.Yes:
            # 完成所有操作后，释放捕获器
            self.cap.release()
            cv2.destroyAllWindows()
            self.Server.shutdown(2)
            self.Server.close()
            event.accept()
        else:
            event.ignore()

if __name__=='__main__':
    app = QtWidgets.QApplication(sys.argv)
    w = mainwin()
    w.show()
    sys.exit(app.exec_())