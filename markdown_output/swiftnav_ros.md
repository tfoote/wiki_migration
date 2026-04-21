## Description

This package is a ROS release of an SBP driver for
[Swift Navigation\'s](http://swiftnav.com) localization devices - Piksi
Multi and Duro. A connected pair of these devices can provide the
location of each receiver relative to the other with accuracy as good as
a couple of centimetres. Additionally, each Piksi module provides its
location with typical GPS accuracy (about 3 meters). Typically one
module is a stationary base station, which may be located at a surveyed
point, while the other is mounted on a rover and provides ROS navigation
software with a highly accurate position relative to the base station.

See Wikipedia\'s
[Real Time Kinematic](https://en.wikipedia.org/wiki/Real_Time_Kinematic)
article for an explanation of RTK GPS. It is important to understand
that RTK GPS does not give a 2cm-precision absolute position
(lattitude/longitude). It gives a 2cm-precision position of a rover
relative to a base-station. If the base station is at a surveyed point
the relative position of the rover can be converted to an absolution
position, but the RTK position reported by a rover is its position
relative to the base station.

Other configurations of two modules are possible, such as placing both
on moving platforms. Each device computes its position relative to the
other. This symmetry of operation enables the robot\'s position to be
found using position data from either the base station or the rover.

In a configuration with a base station and a rover, one unit can be
standalone (no attached computer, only a power supply) while the other
is connected to a computer that guides a robot.

This driver also publishes major status and diagnostic information on
diagnostic topics.

For a successful integration, it is crucial that you understand the
specifications of your device. Refer to the
[Swift Navigation Support Portal](https://support.swiftnav.com/) for
more information.

## Published data

This driver publishes the following data on the ROS topics listed.

  -- ------------ -- ---------------------------- -- -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- --
     **Topic**       **Message Type**                **Notes**                                                                                                                                                                                                                                                                                                                                          
     gps/fix         sensor_msgs::NavSatFix          GPS lat/long. Variance is populated with the Horizontal Dilution of Precision (HDOP) squared.                                                                                                                                                                                                                                                      
     gps/rtkfix      nav_msgs::Odometry              Position relative to base station. See [REP-103](http://www.ros.org/reps/rep-0103.html) for the definition of the ENU coordinate frame, in which the relative position is expressed. If Piksi is in Fixed Mode (has an rtk fix), variance is populated with the reported rtk horizontal accuracy; otherwise it is populated with the value 1000.   
     gps/time        sensor_msgs::TimeReference      GPS time                                                                                                                                                                                                                                                                                                                                           
  -- ------------ -- ---------------------------- -- -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- --

The frame_id field of messages is populated with \"gps\".

## Software

The swiftnav_ros package has been test on ROS Lunar Loggerhead.
Currently, you must build it from source, and also build a supporting
non-ROS library: libsbp, from source.

### Build And Install libsbp

The following steps build and install libsbp, which is needed to support
the swiftnav_ros package.

Clone libsbp into a local directory, and build and install it.

Comments follow a \# below - they explain the step; do not type them.

Caution: do not build libsbp in your catkin workspace - it is not
\"catkinized\".

```
cd mysrc       # cd to a directory where you will download and build libsbp
git clone https://github.com/swift-nav/libsbp
cd libsbp/c
mkdir build
cd build
cmake ../
make
sudo make install   # install headers and libraries into /usr/local
```

### Build and Install the swiftnav_piksi driver

The following steps build and install this package into your catkin
workspace.

```
cd catkin_ws/src       # your catkin workspace
git clone https://github.com/swift-nav/swiftnav_ros
cd ..
catkin_make
```

### Build and Install the Swift Console

The
[Swift Console](https://support.swiftnav.com/customer/en/portal/articles/2492795-swift-console-piksi-console-)
is an important utility for monitoring and verifying correct operation
of Swift Navigation devices. Binaries are available for 64-bit Linux -
they have been tested under Ubuntu.

## Running Piksi with ROS

### Start the ROS Driver & Diagnostics

The demo script launches both the driver, which publishes data from
device, and also a diagnotic monitor.

Note: the Swift Navigation device is assumed to be at /dev/ttyUSB0.

If the Swift Navigation device serial port is different, edit the port
parameter in swiftnav_ros/launch/swiftnav_ros.launch.

```
roslaunch swiftnav_ros swiftnav_ros.launch
```

## Using Multi/Duro swiftnav_ros driver with Ethernet

### Create virtual port

Assuming the Piksi is set at the default adddress of
192.168.0.222:55555, use socat to create virtualcom0. This must go in
/tmp instead of /dev to avoid permission issues. Run this command in a
separate terminal.

```
socat pty,link=/tmp/virtualcom0,raw tcp:192.168.0.222:55555
```

You can test the conection with Swift Console. Start the Swift Console
and connect with serial to /tmp/virtualcom0 and verfiy it runs.

### Configure swiftnav_ros driver

Change the device name in the launch file. The default was /dev/ttyUSB0.
Change it to /tmp/virtualcom0.

```
<param name="port" value="/tmp/virtualcom0" />
```

This has been tested on Duro and on Piksi Multi eval boards.
