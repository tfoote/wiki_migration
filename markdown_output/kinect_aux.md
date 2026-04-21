`kinect_aux` is now a standalone package. In Electric it was a package
in [kinect](kinect), which is deprecated.

## Overview

This driver provides access to additional features present in the Kinect
sensor: accelerometer, tilt, and LED. One may use it in parallel with
the [openni_camera](openni_camera) driver.

## Installation

### Ubuntu

If you are using Ubuntu, simply install the package using apt-get: {
}}}} { }}}} { }}}}

### From source

Alternatively, install the package from source as described below.

Assuming a catkin workspace has been created as described in
[catkin/Tutorials/create_a_workspace](catkin/Tutorials/create_a_workspace),
follow the steps below.

Firstly, install the system dependencies (if not yet installed):



```
$ sudo apt-get install libusb-1.0-0 libusb-1.0-0-dev
```

 Next, download the source code to your catkin
workspace and build it:

{ }}}} { }}}} { }}}} Lastly, run the node (remember to run roscore if it
is not yet running):



```
$ rosrun kinect_aux kinect_aux_node
```



## Quick tests

To set the the tilt angle to, e.g., -15 degrees (Kinect facing
downwards), simply publish a message on the topic (see API below):



```
$ rostopic pub /tilt_angle std_msgs/Float64 -- -15
```

 To view current tilt angle, run:



```
$ rostopic echo /cur_tilt_angle
```



## API



```clearsilver
name = kinect_aux_node
pub {
  0.name = /imu
  0.type = sensor_msgs/Imu
  0.desc = accelerometer data, you might want to change the topic to something like "imu_kinect" to not conflict with the main imu.
  1.name = /cur_tilt_angle
  1.type = std_msgs/Float64
  1.desc = current tilt angle
  2.name = /cur_tilt_status
  2.type = std_msgs/UInt8
  2.desc = current tilt status
}
sub {
  0.name = /tilt_angle
  0.type = std_msgs/Float64
  0.desc = set the tilt angle, must be within [-31:31] degrees
  1.name = /led_option
  1.type = std_msgs/UInt16
  1.desc = set the LED option, must be within [0:7]
}
param {
  0.name = device_index
  0.type = int
  0.desc = index of device, if multiple Kinects are connected
  0.default = 0
}
```



## Bug reports and feature requests
