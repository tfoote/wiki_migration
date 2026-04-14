## Package Summary

The dmu_ros package:

-   Maintainer status: developed
-   Maintainer: Leo Muhendislik \`\<leo AT leomuhendislik DOT com\>\`
-   Author: Leutrim Gruda \`\<leutrim.gruda AT leomuhendislik DOT
    com\>\`
-   License: BSD
-   Source: <https://github.com/leo-muhendislik/dmu_ros.git>
    (branch:master)
    [Youtube](https://www.youtube.com/watch?v=8bQ-OChcJLg)

## Introduction

DMU11 is a low-cost IMU (6-DOF) produced by Silicon Sensing. It combines
MEMS angular rate and linear acceleration sensors to create a
six-degrees-of-freedom (6-DOF) IMU for complete motion sensing and
control in three-dimensional space. DMU11 is suitable for a wide range
of applications and is calibrated over the full rated temperature range.
For further information regarding the sensor, refer to the official
website(<https://www.siliconsensing.com/products/inertial-modules-systems/dmu11/>).

## Installation from source

The package we have developed, contains the driver of DMU11, and a
launch file which visualizes readings coming from the sensor. This
package is built on Ubuntu 16.04.1 LTS x64 running ROS Kinetic. To
install, clone the repository into catkin workspace.
```
cd ~/catkin_ws/src  
git clone https://github.com/leo-muhendislik/dmu_ros.git
``` After copying source files into src directory,
you build it from root directory as follows:

```
cd ~/catkin_ws
catkin_make
``` After building, you source the setup.bash:
```
source devel/setup.bash
```

## Usage

Now you are ready to go. Connect your sensor to your PC and make sure
which port is assigned to it. Then set the value of device parameter
inside the launch file to the name of the port assigned to your sensor:
```
<param name="device" value="/dev/ttyUSB0"/>
``` Now just run this command:
```
roslaunch dmu_ros dmu11.launch
``` Sensor data is published at a rate of 200Hz on
the /imu/data_raw topic as sensor_msgs/Imu message.
