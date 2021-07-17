# =================================== Images_sub.py ==================================
"""
    @brief:     Subscribe image topics from the ROS, turn into numpy, 
                and then trigger the callback
        
    @Author: Yiye Chen              yychen2019@gatech.edu
    @date: 07/13/2021

    TODO: currently I have to made the callback to accept only the argument list as input, 
            def callback([img1, img2, ...])
        where ideally the callback should be able to be like:
            def callback(img1, img2, ...)
        Not sure whether there is a way to make this happen
"""
# =================================== Images_sub.py ==================================
from ROSWrapper.subscribers.Base import Base
from sensor_msgs.msg import Image
from cv_bridge import CvBridge

class Images_sub(Base):
    def __init__(self, image_topic_list, messageType_list=None, callback_np=None):
        """
        @param[in] callback_np     should be a function accepting *args
        """
        if messageType_list == None:
            messageType_list = [Image] * len(image_topic_list)
        self.callback_np = callback_np

        super(Images_sub, self).__init__(image_topic_list, messageType_list, self.process)
        self.bridge = CvBridge()

    def process(self, *args):
        args_p = [self._preprocess(img_ROS) for img_ROS in args]
        return self.callback_np(args_p)

    def _preprocess(self, img_ROS):
        img_np = self.bridge.imgmsg_to_cv2(img_ROS)
        return img_np
