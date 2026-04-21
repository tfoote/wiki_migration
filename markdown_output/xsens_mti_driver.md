## Overview

The official ROS driver for Xsens industrial Motion Trackers (MTi) can
be found in the Linux installation package of the
[MT Software Suite](https://www.xsens.com/mt-software-suite/) (versions
2019.0 and later). Extract the downloaded installation package, execute
the mtsdk_linux-x##\_####.#.sh and locate the xsens_ros_mti_driver
folder.

Full documentation for the ROS node and XDA library is available at:

*\[MTSDK folder\]/doc/xsensdeviceapi/doc/html/index.html *

## Supported devices

This ROS driver is actively supported and maintained in order to be
compatible with the latest generation MTi\'s.

-   MTi 1-series
-   MTi 10-series
-   MTi 100-series
-   MTi 600-series

## Workflow

The MTi node only receives data from an MTi device and publishes it to
ROS, it is **not** capable of configuring a device. Topics will be
filled with zero-values if the MTi is not configured to output that
specific data type. To configure (the output data of) an MTi you can
either use MT Manager, Xsens Device API (XDA), Low Level Communication
Protocol or by extending the MTi node.

The Xsens MTi driver uses the Public Xsens Device API for scanning,
connecting, packet parsing and log file handling. The implementation of
this driver is done in C/C++, so you can build and run it on a different
platforms. You can also configure an MTi using Public XDA by extending
XdaInterface class, for more information about how to do that have a
look at the \'Public XDA receive data example\', found in the MT SDK
folder of the MT Software Suite.

## Requirements

-   MT SDK from Xsens MT Software Suite 2019.0.1 or later
-   ROS Kinetic or Melodic (compatible with Noetic, but not officially
    supported)
-   C/C++ Compiler: GCC 5.4.0 or MSVC 14.0
-   C++11

## Running the Xsens MTi node

-   Configure your MTi device to output desired data (e.g. orientation
    output) using MT Manager or the MT SDK example codes.
-   Copy xsens_mti_driver folder from your MT SDK directory into your
    catkin workspace \'src\' folder. Make sure the permissions are set
    to o+rw on your files and directories. For details on creating a
    catkin workspace environment refer to
    [Creating a workspace for catkin](catkin/Tutorials/create_a_workspace).
-   Build xspublic from your catkin workspace:

```
$ pushd src/xsens_ros_mti_driver/lib/xspublic && make && popd
```

-   Build Xsens MTi driver package:

```
$ catkin_make
```

-   Source workspace:

```
$ source devel/setup.bash
```

-   Launch the Xsens MTi driver. Display example (orientation data
    should be enabled):

```
$ roslaunch xsens_mti_driver display.launch
``` . Simple example:

```
$ roslaunch xsens_mti_driver xsens_mti_node.launch
```

## Configuring the Xsens MTi node

To change the configuration of the Xsens MTi node you can edit the
*xsens_mti_node.yaml* file. The following parameters can be configured:

-   Device settings for finding a defined MTi device
-   Log file recording option
-   Publishers queue size
-   Message publishers
-   Standard deviation values to be added to published topics (optional,
    default 0)

## Published topics

**Important:** Published topics will be filled with zeros if the MTi is
not configured to output the corresponding data messages. Refer to the
**Workflow** section of this page for more details.

-   ***imu/data*** (sensor_msgs/Imu)\
    quaternion, angular velocity and linear acceleration
-   ***imu/acceleration* **(geometry_msgs/Vector3Stamped)\
    calibrated linear acceleration
-   ***imu/angular_velocity* **(geometry_msgs/Vector3Stamped)\
    calibrated angular velocity
-   ***imu/mag* **(geometry_msgs/Vector3Stamped)\
    calibrated magnetic field
-   ***imu/dq*** (geometry_msgs/QuaternionStamped)\
    integrated angular velocity from sensor (in quaternion
    representation)
-   ***imu/dv* **(geometry_msgs/Vector3Stamped)\
    integrated linear acceleration from sensor
-   ***imu/time_ref ***(sensor_msgs/TimeReference)\
    timestamp from device
-   ***filter/quaternion*** (geometry_msgs/QuaternionStamped)\
    quaternion from filter
-   ***filter/free_acceleration*** (geometry_msgs/Vector3Stamped)\
    linear acceleration from filter
-   ***filter/twist** *(geometry_msgs/TwistStamped)\
    velocity and angular velocity
-   ***filter/positionlla*** (geometry_msgs/Vector3Stamped)
    (MTSS2019.3.2 and later)\
    filtered position output in latitude (x), longitude (y) and
    altitude (z) as Vector3
-   ***filter/velocity*** (MTSS2019.3.2 and later)\
    filtered velocity output as Vector3
-   ***temperature*** (sensor_msgs/Temperature)\
    temperature from device
-   ***pressure*** (sensor_msgs/FluidPressure)\
    barometric pressure from device
-   ***gnss** *(sensor_msgs/NavSatFix)\
    raw 4 Hz latitude, longitude, altitude and status data from GNSS
    receiver
-   ***tf** *(geometry_msgs/TransformStamped)\
    transformed orientation

## Troubleshooting

**The published topics do not reach the expected data output rate (e.g.
400 Hz). **\
We have noticed that the ROS node can cause a high CPU load, leading to
lower data output rates. This issue has been fixed in ROS nodes
available in MTSS2019.3.2 and later. We recommend migrating to the
latest version.

If you have connected the MTi via a USB interface, we recommend enabling
the low latency mode using setserial:

-   Install setserial if not already installed
-   Enable low latency mode: ```
$ setserial [/path/to/xsens/port] low_latency
```
-   Check the output rate of the published topics, e.g:
    ```
$ rostopic hz imu/data
```
-   Note that the low_latency mode is lost after rebooting, so you will
    probably need to create a udev rule for this.

**The MTi-1 (Motion Tracker Development Board) is not recognized.**\
Support for the Development Board is present in recent kernels. (Since
June 12, 2015). If your kernel does not support the Board, you can add
this manually:

```
$ sudo /sbin/modprobe ftdi_sio $ echo 2639 0300 | sudo tee /sys/bus/usb-serial/drivers/ftdi_sio/new_id
``` **The device is recognized, but I cannot ever
access the device.**\
Make sure you are in the correct group (often dialout or uucp) in order
to access the device. You can test this with:

```
$ ls -l /dev/ttyUSB0

crw-rw---- 1 root dialout 188, 0 May  6 16:21 /dev/ttyUSB0

$ groups

dialout audio video usb users plugdev
``` If you aren\'t in the correct group, you can
fix this in two ways:

1\) Add yourself to the correct group. You can add yourself to it by
using your distributions user management tool, or call:

```
$ sudo usermod -G dialout -a $USER
``` . Be sure to replace dialout with the actual
group name if it is different. After adding yourself to the group,
either relogin to your user, or add the current terminal session to the
group:

```
$ catkin_make
```0 2) Use udev rules. Alternatively, put the
following rule into /etc/udev/rules.d/99-custom.rules:

```
$ catkin_make
```1 . Change \$GROUP into your desired group (e.g.
adm, plugdev, or usb). .

**The device is inaccessible for a while after plugging it in.**\
When having problems with the device being busy the first 20 seconds
after plugin, purge the modemmanager application.

**RViz doesn\'t show an MTi model.**\
It is a known issue with urdfdom in ROS Melodic. A workaround is to
unset/modify the LC_NUMERIC environment variable:

```
$ catkin_make
```2

**Error \"Skipping incompatible xxx when searching for xxx\" after
catkin_make.**\
Try inserting the following at the end of your CMakeLists.txt:
```
$ catkin_make
```3

## Bug Reports & Feature Requests

We appreciate the time and effort spent submitting bug reports. Please
note that Xsens cannot support any ROS packages other than the ROS
driver included in the MT Software Suite.

Please visit us at [BASE](https://base.xsens.com/hc/en-us). BASE is our
online support platform where you can find knowledge base articles,
frequently asked questions and an active community forum where you can
get in touch with our engineers and product specialists.
