"""
    @brief:     Subscribe to the multiarray topics from the ROS, turn the message into numpy, 
                and then trigger the callback
        
    @Author: Yiye Chen              yychen2019@gatech.edu
    @date: 02/25/2022

    TODO: currently I have to made the callback to accept only the argument list as input:
            def callback([img1, img2, ...])
        where ideally the callback should be able to be like:
            def callback(img1, img2, ...)
        Not sure whether there is a way to make this happen
"""

import rospy

from ROSWrapper.subscribers.Base import Base
from ROSWrapper.subscribers.preprocess.matrix import multiArray_to_np
from std_msgs.msg import Float64MultiArray


# NOTE: error occurs when using the synchronizer for the multiarray message (i.e. use the base like the images_sub):
# AttributeError: 'Float64MultiArray' object has no attribute 'header'
# this message has no timestamp?

class Matrix_sub():
    def __init__(self, matrix_topic, matrix_msgType=None, shape=None, callback_np=None):
        """
        @param[in] callback_np     should be a function accepting *args
        @param[in] shape            The list of shapes (tuple)
                                    If not None, will ignore the dimension stored in the message and directly reshape to it.
                                    Else will reconstruct the matrix according to the dimension stored in the message
        """
        if matrix_msgType == None:
            matrix_msgType = Float64MultiArray

        self.shape = shape
        self.callback_np = callback_np

        self.sub = rospy.Subscriber(matrix_topic, matrix_msgType, callback=self.process)

    def process(self, multiarray_msg):
        mat_p = self._preprocess(multiarray_msg, self.shape)
        return self.callback_np(mat_p)

    def _preprocess(self, multiarray_msg, shape):
        array_np = multiArray_to_np(multiarray_msg, shape)
        return array_np