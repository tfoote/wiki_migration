## Introduction

This node provides a ROS service that manipulates
[Blink(1)](https://blink1.thingm.com/). Accompanies the node an API that
facilitates the use of the service.

The code depends on libUSB. To install libUSB:



```
sudo apt-get install libusb-dev
```



## Installing the package

Create a catkin workspace. For instructions on how to create the
workspace go
[here](http://wiki.ros.org/catkin/Tutorials/create_a_workspace).
Download and compile the package:



```
catkin_ws/src
git clone git@bitbucket.org:castacks/blink1_node.git
cd ..
catkin_make
```



If cloning does not work, try 

```
catkin_ws/src
git clone  https://bitbucket.org/castacks/blink1_node.git
cd ..
catkin_make
```



## Running and testing the node

To run and test the node you must have permission to access the Blink(1)
device. For a first test you may change to root (sudo -s) and run:



```
source devel/setup.bash
roslaunch blink1 blink1.launch
```

 In another terminal:



```
source devel/setup.bash
rosrun blink1 blink1_example
```

 The LED should turn on and blink with several
colors. See the examples folder to the code of this example.

To permanently change the permissions of the device and run the node in
the user mode, please refer to the
[instructions of the device's manufacturer](https://github.com/todbot/blink1/blob/master/commandline/hidapi/udev/99-hid.rules).
