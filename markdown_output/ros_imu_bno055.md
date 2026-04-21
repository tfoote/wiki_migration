# Package Summary

ROS driver for the BNO055 IMU using UART communication. It allows the
configuration and calibration of the IMU

-   Maintainer status: maintained
-   Maintainer: Robert Vasquez Zavaleta <roboticarts1 AT gmail DOT
    com>
-   Author: Robert Vasquez zavaleta <roboticarts1 AT gmail DOT com>
-   License: BSD
-   Bug / feature tracker:
    [ https://github.com/RoboticArts/ros_imu_bno055/issues ]( https://github.com/RoboticArts/ros_imu_bno055/issues )
-   Source: git
    [ https://github.com/RoboticArts/ros_imu_bno055.git ](https://github.com/RoboticArts/ros_imu_bno055.git )

```wiki
'''IMPORTANT:''' This wiki offers a starter guide. See the readme of the [[  https://github.com/RoboticArts/ros_imu_bno055 |  RoboticArts/ros_imu_bno055 ]] repository for complete documentation
```

## Overview

The [ros_imu_bno055](ros_imu_bno055) package contains a ROS driver for
the
[ BNO055](https://www.bosch-sensortec.com/products/smart-sensors/bno055.html )
IMU sensor. This package communicates with the IMU BNO055 using UART
communication through a USB Serial Converter. It allows IMU calibration
and configuration

![this\|width=60%](attachment:bno055_setup.jpeg)

The driver publishes the following data:

-   linear acceleration, angular velocities and quaternion orientation
    as <<MsgLink(sensor_msgs/Imu)>>
-   magnetic field as <<MsgLink(sensor_msgs/MagneticField)>>
-   temperature as <<MsgLink(sensor_msgs/Temperature)>>

## Requisites

1\. Ubuntu with ROS 2. Python 3 3. Bosch IMU BNO055 4. USB Serial
Converter

## Hardware setup

There are different boards that incorporate the BNO055 IMU. The cheapest
one is from Aliexpress. This board has two solder bridges called PS0 and
PS1 used to select the type of communication.

**To use the IMU in this package, it must be configured in UART mode **
to be able to communicate with the serial to USB converter. Therefore
PS0 = 0 and PS1 = 1. Remember that on this board the solder bridges are
inverted, so the PS1 bridge must be unsolder.

![this\|width=40%](attachment:bno055_uart.jpg)
![this\|width=40%](attachment:bno055_aliexpress.jpg)

```wiki
'''Note:''' For different board, for example the Adafruit board or a different Chinese board, use [[https://gr33nonline.wordpress.com/2019/04/19/dont-get-the-wrong-bno055/ | this link]]
``` __

Finally, connect the IMU to the serial to USB converter. The Rx and Tx
cables are crossed. The power of the BNO055 module is 5V

![this\|width=60%](attachment:bno055_schematic.png)

## Installation

To install ros_imu_bno055 package:

```
$ cd ~/catkin_ws/src
$ git clone https://github.com/RoboticArts/ros_imu_bno055.git
```

It is important to compile the package so that the libraries are added
correctly

```
$ cd ~/catkin_ws
$ catkin_make --only-pkg-with-deps ros_imu_bno055
$ source devel/setup.bash
```

Finally pyserial must be installed if it is not on the computer. This
dependency is normally included in the standard ROS installation

```
$ pip install pyserial
```

## Launch IMU

1\. Make sure to connect the IMU well to the computer. Check the
Hardware Setup section for more information

2\. In a terminal, launch the following command to display the IMU in
RVIZ

```
$ roslaunch ros_imu_bno055 view_imu.launch
```

3\. Move the IMU to view its orientation in RVIZ

![this\|width=90%](attachment:bno055_rviz.png)

## IMU Calibration

BNO055 IMU has an internal factory calibration, however, it is highly
recommended to calibrate it. The node imu_calibration takes care of it.
To launch it:

```
$ roslaunch ros_imu_bno055 imu_calibration.launch operation_mode:=NDOF_FMC_OFF
```

This will generate a calibration file that will be used by the driver.
Note that the calibration depends on the operating mode used, therefore
it must be indicated.

![this\|width=60%](attachment:calibration_mode.png)

```wiki
'''Note:''' For more detailed instructions see [[https://github.com/RoboticArts/ros_imu_bno055 | readme ]]
```

## ROS API

```clearsilver
name = ros_imu_bno055 / imu_ros
desc = The `imu_ros` node publishes IMU data: 

pub {
   0{
    name = imu/data
    type = sensor_msgs/Imu
    desc = Includes linear accelerations and angular velocities and orientations.
    }
   1{
    name = imu/magnetometer
    type = sensor_msgs/MagneticField
    desc = The magnetic orientation vector
    }
   2{
    name = imu/temperature
    type = sensor_msgs/Temperature
    desc = Temperature ºC
    }
  }

srv{
  0.name= imu/reset_device
  0.type= std_srvs/Empty
  0.desc= Resets the orientation of the axis that is located perpendicular to the ground plane.
  1.name= imu/calibration_status
  1.type= std_srvs/Trigger
  1.desc= Returns the current status of the calibration
}

param{
    0.name = ~serial_port
    0.type = string
    0.default = `"/dev/ttyUSB0"`
    0.desc = USB port where the IMU is connected (using a USB Serial Converter )

    1.name = ~frame_id
    1.type = string
    1.default = `"imu_link"`
    1.desc = Name of the link that the tf will use
 
    2.name = ~operation_mode
    2.type = string
    2.default = IMU
    2.desc = Type of sensory fusion used by the IMU. See [[https://github.com/RoboticArts/ros_imu_bno055 | readme ]]  for more information
 
    3.name = ~oscillator
    3.type = string
    3.default = INTERNAL
    3.desc = Set external oscillator to get more accurate clock vary for lower sensitivity error

    4.name = ~reset_orientation
    4.type = bool
    4.default = true
    4.desc = Resets the IMU to resets the orientation of the axis that is located perpendicular to the ground plane. 

    5.name = ~frequency
    5.type = double
    5.default = 50
    5.desc = Frequency of reading the IMU and publication in ROS. The maximum frequency reached by the IMU is 50 Hz.

    6.name = ~use_magnetometer
    6.type = bool
    6.default = false
    6.desc = Enables topic imu/magnetometer

    7.name = ~use_temperature
    7.type = bool
    7.default = false
    7.desc = Enables topic imu/temperature
 }
```
