"""
            @brief         Test the functionality of the matrix publisher
            
            @Author: Yiye Chen          yychen2019@gatech.edu
            @Date: 02/25/2022

"""

import numpy as np
import cv2
import rospy
from std_msgs.msg import Float64MultiArray

from ROSWrapper.subscribers.Matrix_sub import Matrix_sub 
from ROSWrapper.subscribers.preprocess.matrix import multiArray_to_np

def callback(mat):
    print(mat)

def callback_msg(matrix_msg):
    mat_np = multiArray_to_np(matrix_msg, (3,3))
    print(mat_np) 


topic_name = "Test_pub_mat" 


if __name__=="__main__":
    rospy.init_node("test_sub_matrix")
    matrix_sub = Matrix_sub(topic_name, shape=(3, 3), callback_np = callback)
    #matrix_sub = rospy.Subscriber(topic_name, Float64MultiArray, callback=callback_msg)
    rospy.spin()