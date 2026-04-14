## Overview

[image_geometry](image_geometry) contains Python and C++ libraries that
simplifies interpreting images geometrically using the parameters from
\<\<MsgLink(sensor_msgs/CameraInfo)\>\>. Although \`CameraInfo\`
contains all the information required to rectify a raw image and project
points onto it, \'\'\'it is highly recommended that you use this
library\'\'\', since performing these operations correctly over the
space of all camera options can be non-trivial.

The camera parameters in \`CameraInfo\` are for a full-resolution image;
region-of-interest alone significantly complicates the creation of
rectification maps and requires adjusting the projection matrix. Adding
options such as subsampling (binning) to \`CameraInfo\` would further
complicate the correct interpretation of the corresponding Images. Using
\`image_geometry\` simplifies and future-proofs imaging code.

The \`image_geometry\` classes are written to be used in an
\`Image\`/\`CameraInfo\` message callback similar to
[cv_bridge](cv_bridge).

In order to maintain invariance, the \`CameraModel\` classes offer
read-only access to specific parameters and matrices. Setting a
\`CameraModel\` can only be performed with full information using the
\`fromCameraInfo()\` functions.

These classes use the OpenCV camera model (
[OpenCV functions for 3d reconstruction](http://opencv.willowgarage.com/documentation/camera_calibration_and_3d_reconstruction.html)).
Accessors to camera matrices in the format expected by OpenCV are
provided for easy integration.

## Tutorials

## C++ API

Please see the
[image_geometry C++ API](http://www.ros.org/doc/api/image_geometry/html/c++/)
documentation.

## Python API

Please see the
[image_geometry Python API](http://www.ros.org/doc/api/image_geometry/html/python/)
documentation.
