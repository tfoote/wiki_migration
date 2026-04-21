**Wiki** <https://github.com/gbr1/ros_openvino/wiki>.

A ROS package to wrap openvino inference engine and get it working with
**Myriad** and **Intel CPU/GPUs**\<br\> The main topic is to accelerate
robotics developing using ROS with OpenVINO.

This package is designed on async api of Intel
OpenVINOhttps:*software.intel.com/en-us/openvino-toolkit. and allows an
easy setup for **object detection**.*

Entire package is born to support Myriad X, so it works perfectly with:

-   Movidius Neural Compute Stick 2
-   Ai Core X
-   Movidius Neural Compute Stick
-   Ai Core

**object detection** node allows you to use a standard image topic and
obtain a new topic with live result image. If you enable *depth
analysis* you can add depth image topic to obtain 3d boxes, visible as
markers in rviz.
