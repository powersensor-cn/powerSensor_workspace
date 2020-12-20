print("offline mode start...")

import numpy as np
import cv2
import time
import numpy as np
import struct
import socket
import TcpUdpHelper
import PowerSensor as ps


class PowersensorPara_ex(TcpUdpHelper.PowersensorPara):
    def __init__(self, debug=False):
        super(PowersensorPara_ex, self).__init__()
        self.paraSwitch = [False, False, False, False, False, False, False, False]
        self.paraInt = np.array(np.zeros(2), dtype=np.int32)
        self.paraFloat = np.array(np.zeros(8), dtype=np.float32)
    
    def unpackBuffer(self, data_buf):
        for i in range(8):
            # print(data_buf[4 + i] )
            if data_buf[4 + i] > 0:
                self.paraSwitch[i] = True
            else:
                self.paraSwitch[i] = False    
        temp = struct.unpack('ii', data_buf[12:20])
        self.paraInt = np.array(temp, np.int32)
        temp = struct.unpack('ffffffff', data_buf[20:52])
        self.paraFloat = np.array(temp, np.float32)
        
    def packParas(self):
        buffer = struct.pack("iiffffffff", self.paraInt[0], self.paraInt[1], self.paraFloat[0], self.paraFloat[1],
                            self.paraFloat[2], self.paraFloat[3], self.paraFloat[4], self.paraFloat[5],
                            self.paraFloat[6], self.paraFloat[7])
        cmd_buf = bytearray(52)
        cmd_buf[0] = 0xfa
        cmd_buf[1] = 0xf5
        cmd_buf[2] = 0
        cmd_buf[3] = 0x02
        for i in range(8):
            if self.paraSwitch[i]:
                cmd_buf[i + 4] = 1
            else:
                cmd_buf[i + 4] = 0
        for i in range(len(buffer)):
            cmd_buf[i + 12] = buffer[i]
        return cmd_buf

    
x = PowersensorPara_ex()
server = TcpUdpHelper.PowersensorServer(port=10775, para=x)
x = server.startServer()

cam1 = ps.ImageSensor()

for i in range(1000): 
    start = time.time() 
    imgMat = cam1.read_img_ori() 
    tempImg = cv2.resize(imgMat, (320,240)) 
    x.img = tempImg
    time.sleep(0.1)

    
