## Overview

This is a driver package for the WITHROBOT's
[myAHRS+](http://www.withrobot.com/myahrs_plus_en/) from
[lilliputdirect](http://www.lilliputdirect.com/odroid-myahrs) and
[hardkernel](http://www.hardkernel.com/main/products/prdt_info.php?g_code=G141464363369)
. The myAHRS+ is a low cost high performance AHRS(Attitude Heading
Reference System) with USB/UART/I2C interface. The myAHRS+ board
contains a 3-axis 16-bit gyroscope, a 3-axis 16-bit accelerometer and a
3-axis 13-bit magnetometer. The driver should also work with USB port.

### Axes Convention

![\|align=right,width=320](attachment:myahrs_plus_axes.png)

The myAHRS+ board used NED type. The myahrs_driver contained in this
package converts to the frame conventions of ROS (use the east north up
(ENU) convention and right hand rule) before publishing the msgs. The
driver use the coordinate frame below. Please see
[REP-0103](http://www.ros.org/reps/rep-0103.html#axis-orientation) for
more information.

-   x forward
-   y left
-   z up

```{=html}
<!-- -->
```
-   NED type IMU: x-north, y-east, z-down, relative to magnetic north.
-   ENU type IMU: x-east, y-north, z-up, relative to magnetic north.

### Original Source

The original source (not support ROS) is maintained github below and
tutorials are on the corresponding wiki page. A 3D visualization test
like 3D-box is included in this original source. This package used the
myAHRS+ SDK below.

<https://github.com/withrobot/myAHRS_plus>

## Video

This is a visualization demonstration using RViz.

[Youtube](https://www.youtube.com/watch?v=j5v5fKppcQo)

## Installation

Install the package:



```
sudo apt-get install ros-indigo-myahrs-driver
```



Install the package from the github:



```
cd ~/catkin_ws/src
git clone https://github.com/robotpilot/myahrs_driver.git
cd ~/catkin_ws && catkin_make
```



## Run

Run the driver like so:



```
rosrun myahrs_driver myahrs_driver _port:=/dev/ttyACM0
```



or



```
roslaunch myahrs_driver myahrs_driver.launch
```



## Nodes



```clearsilver
node.0 {
 name = myahrs_driver
 desc = myahrs_driver node is a driver for the myAHRS+ Inertial Measurement Unit(IMU). It publishes orientation, angular velocity and linear acceleration as well as their covariances, and complies with the [[http://www.ros.org/reps/rep-0103.html#axis-orientation|REP103]] and [[https://github.com/paulbovbel/rep/blob/master/rep-0145.rst|REP145]] (draft) about conventions for IMU sensor drivers.
 pub {
  0.name = imu/data_raw
  0.type = sensor_msgs/Imu
  0.desc = raw data of linear_acceleration and angular_velocity from device.
  1.name = imu/data
  1.type = sensor_msgs/Imu
  1.desc = orientation, linear_acceleration, and angular_velocity data from device.
  2.name = imu/mag
  2.type = sensor_msgs/MagneticField
  2.desc = magnetic_field data from device.
  3.name = imu/temperature
  3.type = std_msgs/Float64
  3.desc = Temperature sensed from device, in degrees centigrade.
 }
 param {
  0.name = ~port
  0.type = string
  0.desc = The port the imu is running on.
  0.default= /dev/ttyACM0
  1.name = ~baud_rate
  1.type = int
  1.desc = Baud rate of serial device.
  1.default = 115200
  2.name = ~frame_id
  2.type = string
  2.desc = The frame ID to set in outgoing messages.
  2.default = imu_link
  3.name = ~parent_frame_id_
  3.type = string
  3.desc = The parent frame ID of frame_id(imu_link) to use the tf.
  3.default = base_link
  4.name = ~linear_acceleration_stddev
  4.type = double
  4.desc = Square root of the linear_acceleration_covariance diagonal elements in m/s^2.
  4.default = 0.026831
  5.name = ~angular_velocity_stddev
  5.type = double
  5.desc = Square root of the angular_velocity_covariance diagonal elements in rad/s.
  5.default = 0.002428
  6.name = ~magnetic_field_stddev
  6.type = double
  6.desc = Square root of the magnetic_field_covariance diagonal elements in Tesla.
  6.default = 0.00000327486
  7.name = ~orientation_stddev
  7.type = double
  7.desc = Square root of the orientation_covariance diagonal elements in rad.
  7.default = 0.002143
 }
}
```



## Communication Protocol Manual and Forum

The myAHRS+ protocol can be found
[here](https://github.com/withrobot/myAHRS_plus/tree/master/tutorial).
The Forum for myAHRS+ user can be found
[here](http://forum.odroid.com/viewforum.php?f=109).

## Report a bug

<https://github.com/robotpilot/myahrs_driver/issues>
