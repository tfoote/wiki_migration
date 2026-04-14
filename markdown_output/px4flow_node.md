## Package Summary

This package provides a ROS interface to the
[PX4Flow](https://pixhawk.ethz.ch/px4/modules/px4flow) optical flow
board.

-   Authors: Lionel Heng, Dominik Honegger, Lorenz Meier, and Petri
    Tanskanen
-   License: BSD
-   Source: git <https://github.com/cvg/px-ros-pkg>

## Overview

The PX4Flow optical flow board outputs optical flow estimates at up to
250 Hz using the MAVLINK protocol over serial. This package parses the
[MAVLINK](http://qgroundcontrol.org/mavlink/start) messages from the
PX4Flow optical flow board, and converts them to ROS messages before
publishing them.

We currently use the PX4Flow optical flow board on both our PIXHAWK MAV
platform and the AscTec Firefly MAV platform. For more details, refer to
the website: <http://www.cvg.ethz.ch/MAV>

## Installation

Clone this repositoy in your catkin workspace.

```
cd ~/your_workspace/src
git clone https://github.com/cvg/px-ros-pkg.git
```

Note that `px4flow_node` package has the following dependencies.

-   roscpp
-   std_msgs
-   sensor_msgs
-   image_transport
-   px_comm

### Building

Build using `catkin_make` according to the ROS
[instructions](http://wiki.ros.org/catkin/Tutorials).

```
cd ~/your_workspace/
catkin_make
```

## Quick Start

Once you have built the `px4flow_node` package. Connect the PX4Flow
optical flow board to one of the USB ports on your computer.

Run the launch file to start up the ROS interface to the PX4Flow optical
flow board.

```
{#!wiki buildsystem catkin
{{{
$ roslaunch px4flow px4flow.launch
``` }}}} ```
{#!wiki buildsystem rosbuild
{{{
$ roslaunch px4flow_node px4flow.launch
``` }}}} Run
`image_view` to show the current image from the camera.

```
$ rosrun image_view image_view image:=/px4flow/camera_image
``` Run `rostopic` to show the values in the
current message published by the `px4flow_node` node.

```
$ rostopic echo /px4flow/opt_flow
```

## Nodes

```clearsilver
name = px4flow_node
pub {
  0.name = px4flow/opt_flow
  0.type = px_comm/OpticalFlow
  0.desc = Ground distance in meters, optical flow in pixels, and sensor velocity in meters/second

  1.name = px4flow/camera_image
  1.type = sensor_msgs/Image
  1.desc = Image captured from the camera and used for optical flow computation
}

param {
  0.name = ~serial_port
  0.type = string
  0.desc = Serial port used for receiving data from and transmitting data to the PX4FLOW hardware
  0.default = /dev/ttyUSB0

  1.name = ~baudrate
  1.type = int
  1.desc = Baudrate for the serial port
  1.default = 921600
}
```
