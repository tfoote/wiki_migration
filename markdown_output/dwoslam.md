# Package Summary

dwoslam is a VSLAM system that is able to track an RGB-D camera, like
the Microsoft Kinect, combining visual features and realtime ICP to
achieve high performance and accuracy. Then, it looks for connections
between key-frames and uses a double-window technique to globally
optimize the whole graph.

-   Author: Nicola Fioraio, Kurt Konolige, Boris Lau\
-   License: BSD\
-   Source: svn <https://kforge.ros.org/dwoslam/svn/trunk>

# Overview

The package is still under development. At the time of writing, it
provides an easy-to-use interface to add Generalized-ICP constraints to
an existing [g2o](g2o) graph and a KLT+ICP camera tracker to effectively
combine those constraints with 2D features in a uniform framework.

# Getting Started

First, get the code from kforge.ros.org and rosinstall some
dependencies: ```
mkdir overlays
svn co https://kforge.ros.org/dwoslam/svn/trunk overlays/dwoslam
rosinstall overlays /opt/ros/diamondback overlays/dwoslam/dwoslam.rosinstall
``` Then, build everything:
```
source overlays/setup.sh
rosmake --rosdep-install dwoslam
```

## Run The Realtime GICP Demo

To run a simple realtime GICP demo, launch your Kinect (see
[openni_kinect](openni_kinect)), or start playing a bagfile; then:
```
rosrun dwoslam realtime_gicp_demo rgb:=/image_color/topic depth:=/depth/topic info:=/rgb/camera_info/topic
``` To see a complete list of options:
```
rosrun dwoslam realtime_gicp_demo --help
``` The known commands are shown in the terminal
and are caught by the OpenCV window: spacebar:: start/pause r:: reset
(restart from scratch) c:: close the loop (experimental)

## Run The KLT+ICP Tracker

To run the KLT+ICP tracker: ```
rosrun dwoslam dwo_node [file.bag] --topics /camera/rgb/image_color /camera/depth/image /camera/rgb/camera_info --harris --do-icp
``` If no bagfile is
provided it starts an online session. To see a complete list of options:
```
rosrun dwoslam dwo_node --help
``` Commands caught by the OpenCV window:\
*online session* spacebar:: restart g:: write the graph to pdf *testing
session* spacebar:: restart g:: write the graph to pdf s:: skip frame
c:: continue (track this frame) f:: go to frame no\...(write the frame
number in the terminal window) t:: go to timestamp\...(write the
timestamp -ns- in the terminal window) e:: exit

When the graph is drawn in the viewer, the program could stop: simply
press 'q' in the 3D window.

# C++ API

The code is still under development, the API is subject to change and
therefore the code is not yet publicly available. If you are a developer
and want to contribute, please ask to be added to the developer list.
