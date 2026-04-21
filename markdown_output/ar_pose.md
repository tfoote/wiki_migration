![](attachment:arsingle.jpg) ![](attachment:armulti.jpg)

## Overview

This package is an ROS wrapper for
[ARToolkit](http://www.hitl.washington.edu/artoolkit/).

[ar_pose](ar_pose) provides two nodes you can run. The program
`ar_single` provides a transform between the camera and a single AR
Marker. The program `ar_multi` provides an array of transforms for
multiple markers.

## Calibration Requirements

Currently the [ar_pose](ar_pose) package requires calibration
information from a camera_info topic. If there is no camera_info topic
the marker pose estimation will not start.

## Examples

You can run [ar_pose](ar_pose) on a live video from a camera, or on a
pre-recorded bag file that comes with the package. First, make sure you
have [ar_tools](ar_tools) metapackage downloaded and installed and
built.

### Prerecorded Demo: Tracking a single marker

This demo uses `ar_single` to track the location of an
[AR Marker](http://www.artoolworks.com/support/library/Creating_and_training_new_ARToolKit_markers)
relative to the location of a fixed camera. The position of the camera
in the world frame is published by `static_tf_publisher` as a static
transform. The tracking process is visualized in [rviz](rviz).



```wiki
'''Download Warning'''
The `setup_single.sh` script currently downloads a '''350MB''' file.
```

 First, make sure you have built the additional
packages necessary for the demo:



```shell
rosmake rviz rosbag
```

 Next, download the example image data and run
the demo.



```shell
roscd ar_pose/demo
./setup_single.sh
roslaunch ar_pose demo_single.launch
```

 You should then see something similar to the
video below:

[Youtube](https://www.youtube.com/watch?v=K6ytrF-YKh4)

### Prerecorded Demo: Tracking the camera position

This demo uses `ar_single` to track the position of the camera
relative to the location of an
[AR Marker](http://www.artoolworks.com/support/library/Creating_and_training_new_ARToolKit_markers).
The position of the marker in the world frame is published by
`static_tf_publisher` as a static transform. The tracking process is
visualized in [rviz](rviz).



```wiki
'''Download Warning'''
The `setup_reverse.sh` script currently downloads a '''177MB''' file.
```

 First, make sure you have built the additional
packages necessary for the demo:



```shell
rosmake rviz rosbag
```

 Next, download the example image data and run
the demo.



```shell
roscd ar_pose/demo
./setup_reverse.sh
roslaunch ar_pose demo_reverse.launch
```

 You should then see something similar to the
video below:

[Youtube](https://www.youtube.com/watch?v=rrzlVRwhy6I)

### Prerecorded Demo: Tracking multiple markers

This demo uses `ar_multi` to track the location of multiple
[AR Markers](http://www.artoolworks.com/support/library/Creating_and_training_new_ARToolKit_markers)
relative to the location of a fixed camera. The position of the camera
in the world frame is published by `static_tf_publisher` as a static
transform. The tracking process is visualized in [rviz](rviz).



```wiki
'''Download Warning'''
The `setup_multi.sh` script currently downloads a '''177MB''' file.
```

 First, make sure you have built the additional
packages necessary for the demo:



```shell
rosmake rviz rosbag
```

 Next, download the example image data and run
the demo.



```shell
roscd ar_pose/demo
./setup_multi.sh
roslaunch ar_pose demo_multi.launch
```


[Youtube](https://www.youtube.com/watch?v=b_WYO1QIYtc)

### Live video examples

Two examples are provided that are configured and calibrated for use
with a Logitech C600 webcam and the [usb_cam](usb_cam) driver.

The single-marker example that is provided uses the patt.hiro marker. A
.pdf of this marker can be found in
/ros/stacks/ccny-ros-pkg/ccny_vision/artoolkit/build/artoolkit-svn/patterns/pattHiro.pdf



```shell
roslaunch ar_pose ar_pose_single.launch
```

 A multi-marker configuration can be started as
well. The Markers used in this example are found in
/ros/stacks/ccny-ros-pkg/ccny_vision/data/4x4/4x4_ps.tar.gz The 4x4
patterns were created with
[patternMaker](http://www.cs.utah.edu/gdc/projects/augmentedreality/download.html)
which was developed by David Johnson, Christopher Berthiaume and Bryan
Witkowski. These patterns are distributed with this software under the
GPL with permission.



```shell
rosmake rviz rosbag
```

0

## Nodes

FIXME: The nodes section of this page is not displaying.



```shell
rosmake rviz rosbag
```

1

## Troubleshooting

### Ubuntu 11.10

A workaround for undefined references in libARgsub.a with Ubuntu 11.10:

-   delete #include <AR/gsub.h> on line 29 in ar_multi.h
-   remove "argCleanup();" on line 159 in ar_multi.cpp

## Bug Reports & Feature Requests

We appreciate the time and effort spent submitting bug reports.

Please use our [Trac](http://robotics.ccny.cuny.edu/trac/) to
[report bugs](http://robotics.ccny.cuny.edu/trac/newticket?component=ccny_vision/ar_pose&type=defect)
or
[request features](http://robotics.ccny.cuny.edu/trac/newticket?component=ccny_vision/ar_pose&type=enhancement).
