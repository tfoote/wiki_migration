## Overview

This package provides a ROS interface for ethernet cameras conforming to
the GenICam standard. It is based on the
[Aravis library](https://wiki.gnome.org/Aravis). You can
[get the driver here](https://github.com/ssafarik/camera_aravis). NOTE!
API of aravis changed in versions 0.3.4 and 0.3.6. When using aravis
0.3.4-0.3.6 you can use the
[driver from here](https://github.com/takiaine/camera_aravis). When
using aravis version 0.3.6 or newer you can use
[driver from here](https://github.com/CaeruleusAqua/camera_aravis).

## Features

### Messages

This ROS node publishes messages `image_raw` and `camera_info` for a
specified camera.

### Parameters

Camera settings are supported via ROS parameters and
dynamic_reconfigure, including the following:

-   `ExposureAuto` (string: "`Off`", "`Once`",
    "`Continuous`")
-   `GainAuto` (string: "`Off`", "`Once`", "`Continuous`")
-   `ExposureTimeAbs` (float)
-   `Gain` (float)
-   `AcquisitionMode` (string: "`Continuous`",
    "`SingleFrame`", "`MultiFrame`")
-   `AcquisitionFrameRate` (float)
-   `TriggerMode` (string: "`Off`", "`On`")
-   `TriggerSource` (string: "`Software`", "`Line1`",
    "`Line2`")
-   `softwaretriggerrate` (float)
-   `frame_id` (string)
-   `FocusPos` (integer)
-   `mtu` (integer)

In addition to the above features, this driver supports (almost) every
feature of every camera, you just have to know how the feature is
specified. Each GenICam-based camera contains an XML file onboard, and
by viewing this file you can determine which ROS parameters to use for
the particular feature. You can use arv-tool-0.4 to see the feature list
and the XML file (e.g. "`arv-tool-0.4 \--name=Basler-21285878
features`")

Note that for this special feature access, the ROS parameter type must
match the feature type. For example, a Basler ac640 has a boolean
feature called "`GammaEnable`", an integer feature called
"`BlackLevelRaw`", and a string enum feature called
"`PixelFormat`" that takes values ("`Mono8`", "`Mono12`",
"`Mono12Packed`", "`YUV422Packed`", etc). The ROS params that
you set for these must be, respectively, a bool, an integer and a
string. Also note that boolean features must be specified as ROS params
false/true, not as integer 0/1.



```
$ rosparam set /camera_aravis/GammaEnable false
$ rosparam set /camera_aravis/BlackLevelRaw 5
$ rosparam set /camera_aravis/PixelFormat Mono12
$ rosrun camera_aravis cam_aravis
```



### Multiple Cameras

camera_aravis supports multiple cameras, each of which may be specified
on the command-line, or via parameter. It runs one camera per node.

To specify which camera to open, via the command-line:



```
$ rosrun camera_aravis cam_aravis _guid:=Basler-21237813
```

 To specify which camera to open, via a
parameter:



```
$ rosparam set /camera_aravis/guid Basler-21237813
$ rosrun camera_aravis cam_aravis
```



### Timestamps

There is an additional nice feature related to timestamps that unifies
ROS time with camera time. The issue is that we want a stable timestamp
on the images that the camera delivers, giving a nice smooth time delta
from frame to frame. If we were to use the ROS clock on the PC, by the
time we get the image packets from the camera a variable amount of time
has passed on the PC's clock due to variable network and system delays.
The camera's onboard clock is stable but it doesn't match with the ROS
clock on the PC, and furthermore since it comes from a different piece
of hardware, the two clock's rates are slightly different.

The solution is to start with a base of ROS time, and to accumulate the
dt's from the camera clock. To accomodate the difference in clock
rates, a PID controller gently pulls the result toward ROS time.

## Examples

The basic command to run camera_aravis:



```
$ rosrun camera_aravis cam_aravis
```

 To run it in a given namespace:



```
$ ROS_NAMESPACE=cam1 rosrun camera_aravis cam_aravis
```


