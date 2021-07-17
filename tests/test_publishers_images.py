# ========================================= test_publishers_images.py ================================
"""

    @brief          Test the Image publisher class: publishers.Image_pub.Image_pub

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

from ROSWrapper.publishers.Image_pub import Image_pub

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
    rospy.init_node("Test_Image_Pulisher")

    # prepare data
    img = cv2.imread(os.path.join(dpath, "empty_desk_0.png"))
    img = img[:, :, ::-1]    #bgr to rgb

    depth = read_npz(os.path.join(dpath, "empty_desk_data_0.npz"))["depth_frame"]

    # prepare publishers
    rgb_pub = Image_pub("Test_pub_image_rgb", encoding="rgb8")
    dep_pub = Image_pub("Test_pub_image_dep")

    # publish
    has_sent_notice = False
    while(True):
        rgb_pub.pub(img)
        dep_pub.pub(depth)

        if not has_sent_notice:
            print("\n\nHas published the rgb and the depth message to the topics: \n \
                \"Test_pub_image_rgb\" and \"Test_pub_image_dep\" ") 
            print("Can visualize the published rgb image typing the following command in the terminal: \n \
                rosrun image_view image_view image:=Test_pub_image_rgb")
            has_sent_notice = True

        time.sleep(0.05)


