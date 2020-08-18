print("offline mode start...")

import numpy as np
import cv2
import matplotlib.pyplot as plt
from IPython.display import clear_output
import time
import PowerSensor as ps
import glob
import apriltag

cam1 = ps.ImageSensor()
s1 = ps.UsartPort()

camera_para_mtx = np.array([[576.56511716,   0.        ,  376.48483532],
                    [  0.        , 575.95185476, 238.84099889],
                    [  0.        ,   0.        ,   1.        ]])
camera_para = (camera_para_mtx[0, 0], camera_para_mtx[1, 1], camera_para_mtx[0, 2], camera_para_mtx[2, 2])

ps.CommonFunction.led_spark(2)
detector = apriltag.Detector()
for i in range(200):
    imgMat = cam1.read_img_ori()    

    start = time.time()    

    img_gray = cv2.cvtColor(imgMat, cv2.COLOR_BGR2GRAY)
    img_mid = cv2.medianBlur(img_gray, 3)
    ret,img_binary = cv2.threshold(img_mid, 90, 255, cv2.THRESH_BINARY)
    detections = detector.detect(img_binary)
    result = 'Not Found:\n'

    for det in detections:
        pose_mtx, init_error, final_error = detector.detection_pose(det, camera_para, tag_size=4)
        x = pose_mtx[0][3]
        y = pose_mtx[1][3]
        z = pose_mtx[2][3]
        result = 'ApritagCheck:' + str(round(x,2)) + "\t" + str(round(y)) + "\t" + str(round(z)) + "\n"
        
    end = time.time()        
    s1.u_print(result)
    time.sleep(0.1)
    
