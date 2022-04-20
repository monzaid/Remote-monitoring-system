import socket
import struct
import sys
import time
import cv2
import numpy


class Config(object):
    def __init__(self, TargetIP=('127.0.0.1', 6666)):
        self.TargetIP = TargetIP
        self.resolution = (640, 480)  # 分辨率
        self.img_fps = 15  # 帧率
        self.server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # 生成新的套接字对象
        self.server.connect(self.TargetIP)
        self.img = ''
        self.img_data = ''

    def RT_Image(self):
        camera = cv2.VideoCapture(0)  # 打开摄像头
        img_param = [int(cv2.IMWRITE_JPEG_QUALITY), self.img_fps]

        while True:
            time.sleep(0.1)  # sleep for 0.1 seconds
            _, self.img = camera.read()

            self.img = cv2.resize(self.img, self.resolution)  # 获取图像

            # 把图像编码.jpg
            _, img_encode = cv2.imencode('.jpg', self.img, img_param)
            img_code = numpy.array(img_encode)
            self.img_data = img_code.tostring()  # bytes data
            try:
                # 传输数据到客户端
                packet = struct.pack(b'lhh', len(self.img_data), self.resolution[0],
                                     self.resolution[1])
                self.server.send(packet)
                self.server.send(self.img_data)

            except Exception as e:
                print(e.args)
                camera.release()
                return


if __name__ == '__main__':
    TargetIP = ('127.0.0.1', 6666)
    if len(sys.argv) == 3:
        TargetIP = (sys.argv[1], sys.argv[2])
    config = Config(TargetIP)
    config.RT_Image()
