# ROSWrapper

A ROS wrapper that helps connect functions with ROS

## Install

```
git clone https://github.com/ivaROS/ROSWrapper.git
pip3 install -e ROSWrapper/
```

## Structure:

``subscribers/``: The classes for subscribing to multiple ros topics and register callbacks taking in the same number of inputs

```subscribers/preprocess/```: Contains some preprocess functions served for the callbacks. They typically convert the ROS massage data to the more commonly used python data. 

```publishers/```: The classes for publishing data

```tests/```: The test scripts





## NOTE:

1. The ```tests/test_publishers_*``` and the ```tests/test_subscribers_*``` need the ros environment.

   Please run the following commands before running the test files (assuming the ROS workspace is called ```catkin_ws```):

   ```
   source ~/catkin_ws/devel/setup.bash
   roscore
   ```

2. Before running any ```tests/test_subscribers_*```, please run the ```tests/test_publishers_images.py``` and ```tests/test_publishers_mat.py``` to publish the topics.

   

