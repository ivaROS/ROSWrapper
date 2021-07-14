# ROSWrapper

A ROS wrapper that helps connect functions with ROS



## Structure:

``Base.py``: The base class for subscribing to multiple ros topics and register callbacks taking in the same number of inputs

```sensors/```: Contains the child classes for sensor-related topics 

```callbacks/```: Contains some callback functions. Some of them might be better to put somewhere else.