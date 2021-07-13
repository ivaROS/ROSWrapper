# ================================= test_sensors_RGB ===============================
"""
            @brief         Test the functionality of the sensors/Image class on one 
                            Image topic
            
            @Author: Yiye Chen          yychen2019@gatech.edu
            @Date: 07/13/2021

            Apply it on subscribe it to an RGB image topic and trigger a toy callback 
            that shows the image. Requires an topic publishing an Image exists
"""
# ================================= test_sensors_RGB ===============================

import numpy as np
import cv2

from sensors import Image

def callback(RGB_np):
    cv2.imshow("test_sensors_RGB", RGB_np)
    cv2.waitKey()

topic_name = "sensor/rgb"

if __name__=="__main__":
    RGB_sub = Image([topic_name], callback_np=callback)
    while(True):
        RGB_sub.receive()