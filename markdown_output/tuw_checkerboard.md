## Overview

This package detects one checkerboard in camera images and computes the
3D pose. The current 3D pose estimation is based on the OpenCV
[solvePnP](http://docs.opencv.org/2.4/modules/calib3d/doc/camera_calibration_and_3d_reconstruction.html#solvepnp)
function. Various Parameter and algorithm used to detect the
checkerboard can be tuned via ROS shared parameters or by using the
dynamic reconfigure interface. This package allows you to publish the
checkerboard pose as tf, marker msg, or pose.

## Examples

-   First of all you need a camera publisher with calibration
    information (see MonocularCalibration to calibrate your camera) and
    lets assume you ar publishing your camera under */camera/image_raw*
    and */camera/camera_info*
-   Secound you can start the checkerboard detection\
    ```
rosrun tuw_checkerboard tuw_checkerboard_node image:=/camera/image_raw camera_info:=/camera/camera_info
```
-   running the reconfigure module allows you to tune parameters
    ```
rosrun rqt_reconfigure rqt_reconfigure
```

## Screenshots

  -- ----------------------------------------------------------------------------------- --
     <tablewidth="100%"> ![\|width="100%"](attachment:tuw_checkerboard_rviz.png)   
     Detected checkerboard with projection and rviz visualization in the background.     
  -- ----------------------------------------------------------------------------------- --

  -- ------------------------------------------------------------------------------------------------- --
     <tablewidth="100%"> ![\|width="400"](attachment:tuw_checkerboard_dynamic_reconfigure.png)   
     Dynamic reconfigure interface                                                                     
  -- ------------------------------------------------------------------------------------------------- --

\
