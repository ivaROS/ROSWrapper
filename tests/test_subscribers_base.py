# ================================= test_sensors_RGB ===============================
"""
            @brief         Test the functionality of the base subscriber class: Base
            
            @Author: Yiye Chen          yychen2019@gatech.edu
            @Date: 07/13/2021

            Subscribe to an RGB image topic and trigger a toy callback 
            that shows the image. 
"""
# ================================= test_sensors_RGB ===============================

import numpy as np
import cv2
from sensor_msgs.msg import Image
from cv_bridge import CvBridge
import rospy

from ROSWrapper.subscribers.Base import Base

bridge = CvBridge()
def callback(img_msg):
    img_np = bridge.imgmsg_to_cv2(img_msg, "rgb8") 
    cv2.imshow("test_sensors_RGB", img_np[:, :, ::-1])
    cv2.waitKey()

topic_name = "Test_pub_image_rgb"

if __name__=="__main__":
    rospy.init_node("test_sub_base")
    RGB_sub = Base([topic_name], [Image], callback = callback)
    rospy.spin()