## Overview

This package contains launch files for using OpenNI-compliant devices in
ROS. It supports the Asus Xtion, Xtion Pro, and multiple version of the
Primesense 1.08 and 1.09 cameras. It does NOT support any versions of
the Kinect. [freenect_launch](freenect_launch) or
[openni_launch](openni_launch) is the recommended package for using a
Kinect with ROS.

There is very little actual code/etc in openni2_launch, it is mostly a
thin wrapper around [openni2_camera](openni2_camera) and
[rgbd_launch](rgbd_launch).

## Usage

Quick start: Launch the OpenNI2 driver. This will launch the full
constellation of nodelets: ```
roslaunch openni2_launch openni2.launch
```

More is documented <http://docs.ros.org/api/openni2_launch/html/>
