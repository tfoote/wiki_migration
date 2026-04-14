## Overview

This package is used to calculate the external parameter of the camera
and the sick using the angular point of the image and the angular point
of the point cloud.

## Usage

1.Get four groups of camera image and point cloud of the calibration
board.

1.1 Run the following command to get the angular point of the camera
image.

rosrun camera_laser_calibration detect_image_corners \[image_file_name\]
\[p1\] \[p2\] \[p3\]

\[image_file_name\] :the image file name of the calibration board.

\[p1\] : the red channel value

\[p2\] : the blue channel value and the green channel value

\[p3\] : the difference between the the blue channel value and the green
channel value

And this command will output a file called \"visionpts\*.txt\" which
contains the angular points of the camera image.

1.2 Run the following command to get the angular point of the point
cloud.

rosrun camera_laser_calibration detect_laser_corners \[pcd_file_name\]

\[pcd_file_name\] : the point cloud\'s file name.

And this command will output a file called \"laserpts\*.txt\" which
contains the angular point of the point cloud.

2.Run the following command to get the rotating tran slational matrix:

rosrun camera_laser_calibration calculate_RT \[first_file_number\]
\[all_file_number\]

\[first_file_number\] : the serial number of the first group of angular
points.

\[all_file_number\] : the number of the groups of angular points.

And this command will output a file called \"rotation.xml\" containing
the rotation matrix and a file called \"translation.xml\" containing the
translation matrix.

## Bug Reports & Feature Requests

We appreciate the time and effort spent submitting bug reports.
