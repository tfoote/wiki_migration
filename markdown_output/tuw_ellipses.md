## Overview

This package detects ellipses in camera images and computes the 3D pose
of the related circle if the radius of the circle is given. The current
3D pose estimation is based on the \[Chen2004\] and the successor of the
[v4r_ellipses](http://wiki.ros.org/v4r_ellipses) package. Various
Parameter and algorithm used to find ellipses can be tuned via ROS
shared parameters or by using the dynamic reconfigure interface.

Chen2004) Chen, Q.; Wu, H. & Wada, T. Pajdla, T. & Matas, J. (Eds.)
Camera Calibration with Two Arbitrary Coplanar Circles Computer Vision -
ECCV 2004, Springer Berlin Heidelberg, 2004, 3023, 521-532,
<http://link.springer.com/chapter/10.1007/978-3-540-24672-5_41>

## Examples

-   First of all you need a camera publisher with calibration
    information (see MonocularCalibration to calibrate your camera) and
    lets assume you ar publishing your camera under
    \'\'/camera/image_raw\'\' and \'\'/camera/camera_info\'\'
-   Secound you can start the ellipse detection\
    ```
rosrun tuw_ellipses tuw_ellipses_node image:=/camera/image_raw camera_info:=/camera/camera_info
```
-   running the reconfigure module allows you to tune parameters
    ```
rosrun rqt_reconfigure rqt_reconfigure
```

## Screenshots

  -- -------------------------------------------------------------------------------------------------------------------------------------------------------------- -- ---------------------------------------------------------------------------------------- --
     \<tablewidth=\"100%\"\> ![\|height=360](attachment:tuw_ellipses_screenshot.png) Detected Ellipses with projected normals of the two possible pose solutions.      ![\|height=360](attachment:tuw_ellipses_reconfigure.png) Dynamic reconfigure interface   
  -- -------------------------------------------------------------------------------------------------------------------------------------------------------------- -- ---------------------------------------------------------------------------------------- --

\
