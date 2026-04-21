![\|align=right,width=240](attachment:um6.jpg)

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

-   x forward
-   y left
-   z up

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
provided via the [imu_compass](imu_compass) package.

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



```clearsilver
node.0 {
 name = um6_driver
 desc = Basic serial driver.
 pub {
  0.name = imu/data
  0.type = sensor_msgs/Imu
  0.desc = Filtered orientation, rotation, and acceleration data from device.
  1.name = imu/mag
  1.type = geometry_msgs/Vector3Stamped
  1.desc = Filtered magnetometer data from device.
  2.name = imu/rpy
  2.type = geometry_msgs/Vector3Stamped
  2.desc = Roll, pitch, and yaw angle for sensed orientation.
  3.name = imu/temperature
  3.type = std_msgs/Float32
  3.desc = Temperature sensed from device, in degrees centigrade.
 }
 param {
  0.name = ~port
  0.type = string
  0.desc = Serial device to connect to.
  0.default = /dev/ttyUSB0
  1.name = ~baud
  1.type = int
  1.desc = Baud rate of serial link.
  1.default = 115200
  2.name = ~mag_updates
  2.type = bool
  2.desc = Include magnetometer data in pose estimate.
  2.default = true
  3.name = ~accel_updates
  3.type = bool
  3.desc = Include accelerometer data in pose estimate.
  3.default = true
  4.name = ~mag_ref/[x,y,z]
  4.type = float
  4.desc = Set magnetometer reference vector to device.
  4.default = ''value from flash memory''
  5.name = ~accel_ref/[x,y,z]
  5.type = float
  5.desc = Set accelerometer reference vector to device.
  5.default = ''value from flash memory''
  6.name = ~mag_bias/[x,y,z]
  6.type = float
  6.desc = Set magnetometer bias vector to device.
  6.default = ''value from flash memory''
  7.name = ~accel_bias/[x,y,z]
  7.type = float
  7.desc = Set accelerometer bias vector to device.
  7.default = ''value from flash memory''
  8.name = ~gyro_bias/[x,y,z]
  8.type = float
  8.desc = Set gyroscope bias vector to device.
  8.default = ''value from flash memory''
 }
}
```


