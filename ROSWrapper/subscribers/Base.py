# =============================== Base ===============================
"""
    @brief      A base class that subscribe to multiple topics 
                 and trigger the callback
    
    @author: Yiye Chen          yychen2019@gatech.edu
    @date: 07/12/2021 (created)

    Use the message_filters.TimySynchronizer to achieve the goal of 
    triggering a callback on multiple subscribers
"""
# =============================== Base ===============================

from message_filters import ApproximateTimeSynchronizer, Subscriber
import rospy

class Base(object):

    def __init__(self, topic_list, messageType_list, callback):
        self.subs = [self.subscribe(topic, messageType) 
                for (topic, messageType) in zip(topic_list, messageType_list)]
        self.ts = ApproximateTimeSynchronizer(self.subs, 10, 0.1)
        self.ts.registerCallback(callback)

    def subscribe(self, topic, messageType):
        """
        Wait until an topic is published and then subscribe
        """
        return Subscriber(topic, messageType)

    def receive(self):
        """
        a way to trigger it?
        """
        return None
        
