![align=right,width=240](doc/um6.jpg)

## Overview

This package provides a comprehensive, C++ driver for the UM6
orientation device produced by CH Robotics.

The UM6 is available for purchase
[directly from CH Robotics](http://www.chrobotics.com/products/inertial-and-orientation-sensors).
Alternatively, the UM6 is available as a standard supported accessory
from Clearpath Robotics---for example, for use with
[Husky](Robots/Husky).

For further information about this device and its configuration, please
see its [datasheet](https://www.chrobotics.com/docs/UM6_datasheet.pdf).

### Axes Convention

As an avionics device, the UM6's serial protocol reports values in NED.
The driver contained in this package converts vectors and quaternions to
the ROS convention (ENU) before publishing, which is:

- x forward
- y left
- z up

Please see
[REP-0103](http://www.ros.org/reps/rep-0103.html#axis-orientation) for
more information.

### Internal Compass

The UM6 contains a MEMS magnetometer, but accurately calibrating it to
achieve a robust heading report has been found to be a tricky business,
especially if the device is mounted in a configuration other than level
to the ground.

At [ClearpathRobotics](ClearpathRobotics), we use a configuration which
subscribes to the magnetometer as a raw data feed, and fuses it into the
orientation as a process external to the device. This functionality is
provided via the [imu_compass](https://index.ros.org/p/imu_compass)
package.

## Installation

Install the package from debians:



```
sudo apt-get install ros-$ROS_DISTRO-um6
```



Run the driver like so:



```
rosrun um6 um6_driver _port:=/dev/ttyUSB0
```



**Note:** A rosbuild branch is also available in the repository, for
users working with rosbuild workspaces under Fuerte or Groovy.

## Nodes

### um6_driver

Basic serial driver.

#### Published Topics

- `imu/data`
  ([sensor_msgs/msg/Imu](https://docs.ros.org/en/rolling/p/sensor_msgs/msg/Imu.html)):
  Filtered orientation, rotation, and acceleration data from device.
- `imu/mag`
  ([geometry_msgs/msg/Vector3Stamped](https://docs.ros.org/en/rolling/p/geometry_msgs/msg/Vector3Stamped.html)):
  Filtered magnetometer data from device.
- `imu/rpy`
  ([geometry_msgs/msg/Vector3Stamped](https://docs.ros.org/en/rolling/p/geometry_msgs/msg/Vector3Stamped.html)):
  Roll, pitch, and yaw angle for sensed orientation.
- `imu/temperature`
  ([std_msgs/msg/Float32](https://docs.ros.org/en/rolling/p/std_msgs/msg/Float32.html)):
  Temperature sensed from device, in degrees centigrade.

#### Parameters

- `~port` (`string`, default: `/dev/ttyUSB0`): Serial device to connect
  to.
- `~baud` (`int`, default: `115200`): Baud rate of serial link.
- `~mag_updates` (`bool`, default: `true`): Include magnetometer data in
  pose estimate.
- `~accel_updates` (`bool`, default: `true`): Include accelerometer data
  in pose estimate.
- `~mag_ref/[x,y,z]` (`float`, default: *value from flash memory*): Set
  magnetometer reference vector to device.
- `~accel_ref/[x,y,z]` (`float`, default: *value from flash memory*):
  Set accelerometer reference vector to device.
- `~mag_bias/[x,y,z]` (`float`, default: *value from flash memory*): Set
  magnetometer bias vector to device.
- `~accel_bias/[x,y,z]` (`float`, default: *value from flash memory*):
  Set accelerometer bias vector to device.
- `~gyro_bias/[x,y,z]` (`float`, default: *value from flash memory*):
  Set gyroscope bias vector to device.
