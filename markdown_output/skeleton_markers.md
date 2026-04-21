## Works Only With Microsoft Kinect

Please note that as of ROS Indigo, this package no longer supports the
Asus Xtion Pro Live or other Primesense cameras. These cameras generally
fail to work with the openni_tracker node due to USB 3.0
incompatibilities on newer machines.

## Install Kinect Drivers for Ubuntu 14.04 and ROS Indigo

To make this package work with ROS Indigo, you will need the Kinect
drivers for Ubuntu 14.04. The following instructions were taken from
[here](http://blog.justsophie.com/installing-kinect-nite-drivers-on-ubuntu-14-04-and-ros-indigo/).
The steps below are for a 64-bit system. Use the 32-bit files for a
32-bit system.

```
$ mkdir ~/src
 $ cd ~/src
 $ git clone https://github.com/avin2/SensorKinect
 $ cd SensorKinect/Bin
 $ tar xjf SensorKinect093-Bin-Linux-x64-v5.1.2.1.tar.bz2
 $ cd Sensor-Bin-Linux-x64-v5.1.2.1
 $ sudo ./install.sh
```

## Overview

{}

{}

{}

[Youtube](https://www.youtube.com/watch?v=nTRi_kIgGW0)

## Installation

{ }}}}

{ }}}}

{ }}}}

## How To Use

### Method 1

To easiest way to use skeleton markers is as follows:

{ }}}}

{ }}}}

Then assume the \"Psi Pose\" in front of the camera while keeping an eye
on RViz until calibration is complete and tracking begins.

### Method 2

You can also view the TF frames for each joint:

{ }}}}

{ }}}}

Then assume the \"Psi Pose\" in front of the camera while keeping an eye
on RViz until calibration is complete and tracking begins.

{ }}}}

{ }}}}

{ }}}}

{ }}}}

## Skeleton Markers From tf Node

```clearsilver
node.0 {
name = markers_from_tf.py
desc = A ROS node for displaying the skeleton joints returned by the [[openni_tracker]] package as markers in RViz.
}

pub {
  0.name = /skeleton_markers
  0.type = visualization_msgs/Marker
  0.desc = Point type markers that can be displayed in RViz.
}
param {
  0.name = ~fixed_frame
  0.type = str
  0.desc = Fixed reference frame
  0.default = /openni_depth_frame

  1.name = ~rate
  1.type = int
  1.desc = Update rate
  1.default = 20

  2.name = ~scale
  2.type = float
  2.desc = Height and width of markers in meters.
  2.default = 0.07

  3.name = ~lifetime
  3.type = float
  3.desc = Duration of markers as displayed in RViz.
  3.default = 0 (forever)

  4.name = ~ns
  4.type = str
  4.desc = Namespace for markers.
  4.default = skeleton_markers

  5.name = ~id
  5.type = int
  5.desc = Marker ID within namespace.
  5.default = 0

  6.name = ~color
  6.type = dictionary
  6.desc = Marker color.
  6.default = green: { 'r': 0.0, 'g': 1.0, 'b': 0.0, 'a': 1.0 }

  7.name = ~tf_prefix
  7.type = str
  7.desc = tf_prefix for identifying skeleton frames
  7.default = skeleton
```

### Example Launch File

Use the **markers_from_tf.launch** file: ```
<launch>
  <include file="$(find openni_camera)/launch/openni_node.launch" />
  
  <node pkg="openni_tracker" name="openni_tracker" type="openni_tracker" output="screen">
    <param name="tf_prefix" value="skeleton" />
  </node>
  
  <node pkg="skeleton_markers" name="skeleton_markers" type="markers_from_tf.py" output="screen">
    <rosparam file="$(find skeleton_markers)/params/marker_params.yaml" command="load" />
  </node>
</launch>
```
