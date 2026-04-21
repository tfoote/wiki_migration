## Overview

This package contains launch files for using Intel RealSense camera
devices in ROS.

It supports the Intel(R) RealSense(TM) 3D Camera (Front F200) Depth.

[realsense_camera on github](https://github.com/BlazingForests/realsense_camera.git)

## New

Infrared raw stream for realsense camera.

![\|width="100%"](attachment:realsense_ir.png)

## Screenshot

![\|width="100%"](attachment:point_cloud_hand.jpg)

![\|width="100%"](attachment:pen_robot.jpg)

## Usage

### launch realsense camera and rviz

```
roslaunch realsense_camera realsense_rviz.launch
```

### launch realsense camera only

```
roslaunch realsense_camera realsense_camera.launch
```
