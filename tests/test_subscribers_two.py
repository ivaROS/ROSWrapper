# ================================= test_sensors_RGB_D ===============================
"""
            @brief         Test the functionality of the sensors/Image class on multiple
                            Image topics
            
            @Author: Yiye Chen          yychen2019@gatech.edu
            @Date: 07/13/2021

            Apply it on the task of subscribing to a RGB and a D topic, 
            and trigger a toy callback that shows both images. 
            Requires such two topics exist from ROS
"""
# ================================= test_sensors_RGB_D ===============================

import numpy as np
import cv2

from ROSWrapper.subscribers.Images_sub import Image

topic_name_RGB = "sensor/rgb"
topic_name_D = "sensor/dep"

def callback(RGB_np, D_np):
    # scale to 255, convert to 3-channel
    depth_colormap = cv2.applyColorMap(cv2.convertScaleAbs(D_np, alpha=255./D_np.max(), beta=0), cv2.COLORMAP_JET)
    # resize
    depth_colormap = cv2.resize(depth_colormap, (RGB_np.shape[1], RGB_np.shape[0]) )
    #  Stack both images horizontally
    images = np.hstack((RGB_np, depth_colormap))

    # show
    cv2.imshow("test_sensors_RGB_D", images)
    cv2.waitKey()


if __name__=="__main__":
    RGB_sub = Image([topic_name_RGB, topic_name_D], callback_np=callback)
    while(True):
        RGB_sub.receive()