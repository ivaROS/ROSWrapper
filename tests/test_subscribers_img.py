# ================================= test_sensors_RGB ===============================
"""
            @brief         Test the functionality of the sensors/Image class on one 
                            Image topic
            
            @Author: Yiye Chen          yychen2019@gatech.edu
            @Date: 07/13/2021

            Apply it on subscribe it to an RGB image topic and trigger a toy callback 
            that shows the image. 
            Comparing the the test_sub_base script, the callback function here should 
            be able to directly accept the numpy img as input
"""
# ================================= test_sensors_RGB ===============================

import numpy as np
import cv2
import rospy

from ROSWrapper.subscribers.Images_sub import Images_sub

def callback(img_list):
    cv2.imshow("test_sensors_RGB", img_list[0])
    cv2.waitKey()

topic_name = "Test_pub_image_rgb"

if __name__=="__main__":
    rospy.init_node("test_sub_one")
    RGB_sub = Images_sub([topic_name], callback_np = callback)
    rospy.spin()