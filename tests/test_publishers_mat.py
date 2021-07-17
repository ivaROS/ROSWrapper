# ========================================= test_publishers_images.py ================================
"""

    @brief          Test the Matrix publisher class: publishers.Matrix_pub.Matrix_pub

    @Author:        Yiye Chen       yychen2019@gatech.edu
    @date:          07/15/2021

"""
# ========================================= test_publishers_images.py ================================


import os
import sys
import cv2
import numpy as np
import time
import rospy

# setup the environment - add the root path
fpath = os.path.dirname(__file__)
rpath = os.path.dirname(fpath)
dpath = os.path.join(fpath, 'data')
sys.path.append(rpath)

from ROSWrapper.publishers.Matrix_pub import Matrix_pub

def read_npz(filename):
    """
    for the npz file saved with python2,
    python 3 and python 2 read the file differently.

    see: https://stackoverflow.com/a/65414582/5269146
    """
    if(sys.version_info[:3] <3.0):
        data = np.load(filename)
    else:
        data = np.load(filename, 
            allow_pickle=True,fix_imports=True,encoding='latin1')
    return data


if __name__ == "__main__":
    # init the node
    rospy.init_node("Test_Matrix_Publisher")

    # prepare data
    img = cv2.imread(os.path.join(dpath, "empty_desk_0.png"))
    intrinsic_matrix = read_npz(os.path.join(dpath, "empty_desk_data_0.npz"))["intrinsics"]
    print(intrinsic_matrix)

    # prepare publishers
    mat_pub = Matrix_pub("Test_pub_mat")

    # publish
    has_sent_notice = False
    while(True):
        mat_pub.pub(intrinsic_matrix)

        if not has_sent_notice:
            print("\n\n Has published the matrix message to the topics: \n \
                \"Test_pub_mat\" ") 
            print("\nCan type the following command to the terminal to verify: \n \
                \" rostopic echo /Test_pub_mat \" ")
            has_sent_notice = True

        time.sleep(0.05)


