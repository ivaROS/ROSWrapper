# =================================== Image.py ==================================
"""
    @brief:     Subscribe image topics from the ROS, turn to numpy image, 
                and then trigger the callback
        
    @Author: Yiye Chen              yychen2019@gatech.edu
    @date: 07/13/2021
"""
# =================================== Image.py ==================================
from Base import Base

class Images(Base):
    def __init__(self, image_topic_list, messageType_list=None, callback_np=None):
        """
        @param[in] callback_np     should be a function on numpy image array
        """
        super().__init__(image_topic_list, messageType_list, 
                        lambda images: self.process(images, callback_np))

    def process(self, images_ROS, callback_np):
        image_np = self._preprocess(images_ROS)
        callback_np(image_np)

    def _preprocess(self, images_ROS):
        image_np = images_ROS
        return image_np

    