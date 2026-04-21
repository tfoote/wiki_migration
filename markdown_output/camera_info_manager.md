## Overview

This package contains no ROS nodes or utility commands.

It provides a C++ class used by many camera drivers to manage the
[camera calibration data](image_pipeline/CameraInfo) required by the
[ROS image pipeline](image_pipeline).

For camera drivers written in Python, the
[camera_info_manager_py](camera_info_manager_py) package provides a
similar interface.

## Roadmap

For ROS Diamondback, this package moved to the
[image_common](image_common) stack. For C Turtle, it was part of
[camera_drivers](camera_drivers).

In ROS Diamondback the \`CameraInfoManager\` class moved to the
\`camera_info_manager\` namespace. For compatibility with ROS C Turtle,
the global \`CameraInfoManager\` class name is still supported. It is
deprecated in Electric Emys and removed in Fuerte.

## Camera Names

The API includes a camera name, which is written when \`CameraInfo\` is
saved, and checked when data are loaded, with a warning logged if the
name read does not match.

Camera driver authors should refer to the
[API documentation](http://www.ros.org/doc/api/camera_info_manager/html/classcamera__info__manager_1_1CameraInfoManager.html#_details)
for syntax details and recommendations for assigning camera names.

## URL Names

The location for getting and saving calibration data is expressed by
Uniform Resource Locator (URL). These URLs are commonly used in the APIs
of this package and may also contain substitution variables to refer to
common locations. Please see the
[API documentation](http://www.ros.org/doc/api/camera_info_manager/html/classcamera__info__manager_1_1CameraInfoManager.html#_details)
for supported URLs, file formats and substitution variables.: the URL
may now contain substitution variables, including the camera name and
\`\${ROS_HOME}\`.

## ROS API

### CameraInfoManager

This C++ class provides the following ROS interfaces, when instantiated
in a camera driver node:

#### Services

-   \`set_camera_info\` (\<\<SrvLink(sensor_msgs/SetCameraInfo)\>\>) for
    calibration information

#### Parameters

This package does not read ROS parameters directly. Where appropriate,
we recommend that drivers provide a \`camera_info_url\` parameter for
the URL string passed to !CameraInfoManager.

## C++ API

[camera_info_manager::CameraInfoManager](http://www.ros.org/doc/api/camera_info_manager/html/classcamera__info__manager_1_1CameraInfoManager.html)
class

For compatibility with C Turtle, the global \`CameraInfoManager\` class
name was still supported, but it was **deprecated** in Electric.: the
global \`CameraInfoManager\` class is no longer available, use
\`camera_info_manager::CameraInfoManager\` instead.: a new
\`setCameraInfo()\` method allows the caller to set \`CameraInfo\`
parameters directly.

### Examples

The camera_info_manager is used in the [camera1394](camera1394) driver.
Search for \`cinfo\_\` in the source code to see where the
!CameraInfoManager class is used. In particular, note the handling of
Header time stamps and transform frame IDs.

-   [camera1394](https://github.com/ros-drivers/camera1394/blob/master/src/nodes/driver1394.cpp#L80)
