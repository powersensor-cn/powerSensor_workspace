print("offline mode start...")

# import numpy as np
# import cv2
# import matplotlib.pyplot as plt
# from IPython.display import clear_output
# import time
# import PowerSensor as ps

# # 这个对象用于操作摄像头
# cam1 = ps.ImageSensor()
# # 这个对象用于操作串口
# s1 = ps.UsartPort()
# s1.set_baudrate(115200)
# # 引用库
# import apriltag

# detector = apriltag.Detector()

# for i in range(5000):
    
# #     clear_output(wait=True)    # 清除图片，在同一位置显示，不使用会打印多张图片
#     imgMat = cam1.read_img_ori()       # 读入图像
    
#     # 缩小图像为320x240尺寸
#     origin = cv2.resize(imgMat, (320,240))
    
#     # ---------------------  图像处理开始  ----------------------------------------
#     start = time.time()        # 记录开始时间
    
#     # 把图片转换为灰度图
#     img_gray = cv2.cvtColor(origin, cv2.COLOR_BGR2GRAY)
#     # 中值滤波
#     img_mid = cv2.medianBlur(img_gray, 3)
#     # 二值化
#     ret,img_binary = cv2.threshold(img_mid, 120, 255, cv2.THRESH_BINARY) # 全局二值化
#     # 识别二维码
#     result = detector.detect(img_binary)
        
#     end = time.time()        # 记录结束时间
#     # ---------------------  图像处理结束  ----------------------------------------       
    
# #     # 把图像拼接在一起显示
# #     img_combine = np.hstack([img_gray])
# #     ps.CommonFunction.show_img_jupyter(img_combine)# 打印用于差分的两张图片
#     if len(result) > 0:
#         res = 'Res:' + str(result[0][6])
#         s1.u_print(res)
# #         print(result[0][6])
# #     print(end - start)
#     tim_str = 'Tim:' + str((int)((end - start)*1000))
#     s1.u_print(tim_str)
#     time.sleep(0.1)