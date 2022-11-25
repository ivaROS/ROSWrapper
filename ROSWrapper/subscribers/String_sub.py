"""
    @brief:     Subscribe to the string topics from the ROS, and then trigger the callback
        
    @Author: Yunzhi Lin              yunzhi.lin@gatech.edu
    @date: 11/24/2022
"""

import rospy

from ROSWrapper.subscribers.Base import Base
from std_msgs.msg import String


class String_sub():
    def __init__(self, string_topic, string_msgType=None, callback_np=None):
        """
        @param[in] callback_np     should be a function accepting *args
        @param[in] shape            The list of shapes (tuple)
        """
        
        if string_msgType == None:
            string_msgType = String

        self.callback_np = callback_np

        self.sub = rospy.Subscriber(string_topic, string_msgType, callback=self.process)

    def process(self, msg):
        return self.callback_np(msg)