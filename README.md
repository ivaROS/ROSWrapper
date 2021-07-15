# ROSWrapper

A ROS wrapper that helps connect functions with ROS



## Structure:

``subscribers/``: The classes for subscribing to multiple ros topics and register callbacks taking in the same number of inputs

```subscribers/callbacks/```: Contains some callback functions. Some of them might be better to put somewhere else.

```publishers/```: The classes for publishing data

```tests/```: The test scripts





## NOTE:

1. The ```tests/test_publishers_*``` and the ```tests/test_subscribers_*``` need the ros environment.

   Please run the following commands before running the test files (assuming the ROS workspace is called ```catkin_ws```):

   ```
   source ~/catkin_ws/devel/setup.bash
   roscore
   ```

   

