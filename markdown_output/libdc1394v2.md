## Overview

This is a third party package with
[external documentation](http://damien.douxchamps.net/ieee1394/libdc1394/).

This experimental package is provided to paper over different versions
of the library provided on various supported systems, especially Ubuntu
Hardy with the ROS Box Turtle release. It will remain until support for
those releases is dropped.

Future ROS releases will not support Hardy, which does not have
particularly reliable 1394 kernel drivers, anyway.

## ROS drivers

This package just wraps the libdc1394v2 library. It provides no ROS
nodes.

The [camera1394](camera1394) ROS driver is a candidate for inclusion in
the next ROS release, completely integrated into the
[image_pipeline](image_pipeline). To run it with Box Turtle, check out
this entire stack, it has internal dependencies including a copy of the
`libdc1394` package: 

```
svn co https://code.ros.org/svn/ros-pkg/branches/trunk_boxturtle/stacks/camera_drivers_experimental
```



Another generic Firewire driver with ROS bindings and many useful
features can be found in the
[cameradc1394 package](http://openrave.programmingvision.com/index.php?title=Working_with_Cameras)
in the [CMU repository](http://cmu-ros-pkg.sourceforge.net/). You can
download the source with: 

```
svn co `roslocate svn cameradc1394` cameradc1394
```


