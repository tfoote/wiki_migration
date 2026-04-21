## Overview

This is [ARToolKit](http://www.hitl.washington.edu/artoolkit/) packaged
for a local ROS installation. This package is primarily to make it
easier to install [ar_pose](ar_pose). More information about
[ARToolKit](http://www.hitl.washington.edu/artoolkit/) can be found at
their home page.

### Troubleshooting Installation

In Ubuntu 11.04 and 11.10, you may encounter errors related to
*videoLinuxV4L*. A possible workaround is to patch the header files
manually with: . ```
$ roscd artoolkit
$ sed -i 's,#include <linux/videodev.h>,#include <libv4l1-videodev.h>,g' ./build/artoolkit/include/AR/sys/videoLinuxV4L.h
$ sed -i 's,#include <linux/videodev.h>,#include <libv4l1-videodev.h>,g' ./build/artoolkit/lib/SRC/VideoLinuxV4L/video.c
```
