# Description

[visp_bridge](visp_bridge) is a small interface between ViSP library and
ROS. For instance it converts between the different data types used by
each library. To date, the supported functionnality sums up to:

-   ViSP
    [vpImage](http://visp-doc.inria.fr/doxygen/visp-daily/classvpImage.html)
    / ROS
    [sensor_msgs::Image](http://www.ros.org/doc/api/sensor_msgs/html/msg/Image.html)
    conversion
-   ViSP
    [vpCameraParameter](http://visp-doc.inria.fr/doxygen/visp-daily/classvpCameraParameter.html)
    / ROS
    [sensor_msgs::CameraInfo](http://www.ros.org/doc/api/sensor_msgs/html/msg/CameraInfo.html)
    conversion
-   ViSP
    [vpHomogeneousMatrix](http://visp-doc.inria.fr/doxygen/visp-daily/classvpHomogeneousMatrix.html)
    / ROS
    [geometry_msgs::Transform](http://www.ros.org/doc/api/geometry_msgs/html/msg/Transform.html)
    conversion
-   ViSP
    [vpHomogeneousMatrix](http://visp-doc.inria.fr/doxygen/visp-daily/classvpHomogeneousMatrix.html)
    / ROS
    [geometry_msgs::Pose](http://www.ros.org/doc/api/geometry_msgs/html/msg/Pose.html)
    conversion

For usage, see the
[code API](http://ros.org/doc/api/visp_bridge/html/namespacemembers.html).

# Installation

[visp_bridge](visp_bridge) is part of [vision_visp](vision_visp) stack.

-   To install [visp_bridge](visp_bridge) package run
    

```
sudo apt-get install ros-$ROS_DISTRO-visp-bridge
```



```{=html}
<!-- -->
```
-   Or to install the complete stack run 

```
sudo apt-get install ros-$ROS_DISTRO-vision-visp
```


