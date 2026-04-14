## Overview

The [stair-step-detector](https://index.ros.org/r/stair_step_detector)
allows the detection of stair steps using a LiDAR depth camera.
Currently, the Intel RealSense L515 is supported (see below, hardware
requirements).\
The repository contains packages for ROS2 Galactic Geochelone:

  -- ------------------------- -- -------------------------------------------------------- --
     stair_step_detector_pkg      \- stair-step-detector node, publishes stairs messages   
     stairs_msg                   \- message definition of the stairs data                 
     example_subscriber_pkg       \- example subscriber to stairs messages                 
     stairs_visualizer_pkg        \- offers something for the eye via RViz                 
  -- ------------------------- -- -------------------------------------------------------- --

\
The \_pkg\'s are essentially small Python scripts. The actual detector
is written in C++ and has no dependencies on ROS.

## Hardware Requirements

The stair-step-detector requires a depth camera. It was developed and
tested using the RealSense L515. It can be adapted to use a different
depth camera. The effort involved depends on the features of this
camera. The adaptation is relative easy if the camera (or the SDK) had
the following features:

-   delivers a point cloud in Cartesian coordinates
-   delivers the 3D spatial points for specific 2D image points\*
-   additionally supplies an infrared stream\*
-   ) required for the geometric calibration
