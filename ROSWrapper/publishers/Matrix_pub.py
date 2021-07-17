# ============================ Matrix_pub =============================
"""
    @brief      The matrix publisher. Turn the matrix in to row-first vector

    @author     Yiye Chen,  yychen2019@gatech.edu
    @date       07/14/2021

    TODO: start with only publishing the float data. Add others in the future.
"""
# ============================ Matrix_pub =============================

import rospy
from std_msgs.msg import Float64MultiArray
import numpy as np

class Matrix_pub():
    """
    The matrix data publisher class.
    Will publish the matrix as the row-first vector

    @param[in]  topic_name          String. 
    """

    def __init__(self, topic_name):
        self.publisher = rospy.Publisher(topic_name, Float64MultiArray)

    def pub(self, mat):
        mat_pub = Float64MultiArray()
        mat_pub.data = self._mat_to_row_vec(mat).tolist()

        self.publisher.publish(mat_pub)
    
    def _mat_to_row_vec(self, mat):
        """
        Turn a mat into the row-first vector
        Use row-first since it seems to be the ROS convention. See the sensor_msgs/CameraInfo for example:
        http://docs.ros.org/en/melodic/api/sensor_msgs/html/msg/CameraInfo.html
        """
        if isinstance(mat, list):
            mat_return = np.asarray(mat)
        elif isinstance(mat, np.ndarray):
            mat_return = mat
        else:
            raise NotImplementedError("Only list or np.ndarray data is acceptable")

        return mat_return.flatten().squeeze()