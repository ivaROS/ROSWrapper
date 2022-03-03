# ============================ Image_pub =============================
"""
    @brief      The image publisher 

    @author     Yiye Chen,  yychen2019@gatech.edu
    @date       07/14/2021
"""
# ============================ Image_pub =============================

import rospy
from sensor_msgs.msg import Image
from cv_bridge import CvBridge
import numpy as np

class Image_pub():
    """
    The image data publisher class

    @param[in]  topic_name          
        String. 

    @param[in]  encoding:
        String. The image format. Default is "passthrough"
        Note that this is just a label, will not converge the image. See the link below:
        http://wiki.ros.org/cv_bridge/Tutorials/ConvertingBetweenROSImagesAndOpenCVImagesPython
    """

    def __init__(self, topic_name, encoding="passthrough"):
        self.publisher = rospy.Publisher(topic_name, Image, queue_size=100)
        self.encoding = encoding

        self.bridge = CvBridge()

    def pub(self, img_data):
        if isinstance(img_data, np.ndarray):
            self.publisher.publish(
                self.bridge.cv2_to_imgmsg(img_data, encoding=self.encoding)
            )
        else:
            raise NotImplementedError("Only the opencv image (numpy.ndarray) is accepted for now")