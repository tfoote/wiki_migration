## Overview

-   Contact: [Zdenek Materna (Robo@FIT)](mailto:imaterna@fit.vutbr.cz)
-   URL: <https://github.com/ZdenekM/microstrain_3dm_gx3_45>

This package implements
[MIP protocol](http://files.microstrain.com/3DM-GX3-45-Data-Communications-Protocol.pdf)
used by
[Microstrain 3DM-GX3-45](http://www.microstrain.com/inertial/3dm-gx3-45)
sensor which is inertial device fusing IMU and GPS. It contains
implementation of driver and ROS node. The driver has been written from
scratch using Boost ASIO library.

## Installation

[Download](https://github.com/ZdenekM/microstrain_3dm_gx3_45) and
compile (rosbuild-based) package.

## Supported Hardware

Driver has been tested only with Microstrain 3DM-GX3-45, under ROS
Groovy.

## API Stability

Driver, node and their API are in experimental phase.

## ROS API

```clearsilver
node.0 {
name=imu_driver
desc=`imu_driver` is a driver for the device. On different topics it provides raw GPS data, AHRS data and fused data. Any topic is advertised only if it's enabled. If enabled and someone is subscribed, node publishes data on that particular topic.
pub{
0.name= ~imu/data
0.type= sensor_msgs/Imu
0.desc= Orientation, angular velocity, linear acceleration and corresponding covariances.

1.name= ~imu/pose
1.type= geometry_msgs/PoseStamped
1.desc= Orientation from IMU in form of PoseStamped which can be for instance easily visualized in RVIZ.

2.name= ~gps/fix
2.type= sensor_msgs/NavSatFix
2.desc= Raw GPS data.

3.name= ~gps/odom
3.type= nav_msgs/Odometry
3.desc= Raw GPS data in form of Odometry (can be used as input for robot_pose_ekf).

4.name= ~nav/fix
4.type= sensor_msgs/NavSatFix
4.desc= Fused data.

4.name= ~nav/odom
4.type= nav_msgs/Odometry
4.desc= Fused data in form of Odometry.

4.name= ~nav/pose
4.type= geometry_msgs/PoseStamped
4.desc= Orientation from fused data.

}

srv{

0.name= ~reset_kf
0.type= std_srvs/Empty
0.desc= Reset of Kalman filter used in device for sensor fusion.
}

param {
0.name= ~port
0.default= /dev/ttyACM0
0.type= string
0.desc= The port the imu is running on.

1.name= ~baud_rate
1.default= 115200
1.type= integer
1.desc= Baud rate of the sensor.

2.name= ~declination
2.default= 3.8
2.type= double
2.desc= Magnetic declination for given area.

3.name= ~frame_id
3.default= /imu
3.type= string
3.desc= All data will be published with this frame_id.

3.name= ~child_frame_id
3.default= /base_footprint
3.type= string
3.desc= Odometry data will be published with this child_frame_id.

4.name= ~publish_pose
4.default= true
4.type= bool
4.desc= Sets if ~imu/pose should be advertised or not.

5.name= ~publish_imu
5.default= true
5.type= bool
5.desc= Sets if ~imu/data should be advertised or not.

6.name= ~publish_gps
6.default= true
6.type= bool
6.desc= Sets if ~gps/fix should be advertised or not.

7.name= ~publish_gps_as_odom
7.default= true
7.type= bool
7.desc= Sets if ~gps/odom should be advertised or not.

8.name= ~publish_nav_odom
8.default= true
8.type= bool
8.desc= Sets if ~nav/odom should be advertised or not.

9.name= ~publish_nav_pose
9.default= true
9.type= bool
9.desc= Sets if ~nav/pose should be advertised or not.

10.name= ~publish_nav_fix
10.default= true
10.type= bool
10.desc= Sets if ~nav/fix should be advertised or not.

11.name= ~linear_acceleration_stdev
11.default= 0.098
11.type= double
11.desc= Standard deviation of linear acceleration. This value is used to calculate covariance matrix.

12.name= ~orientation_stdev
12.default= 0.035
12.type= double
12.desc= Standard deviation of orientation. This value is used to calculate covariance matrix.

13.name= ~angular_velocity_stdev
13.default= 0.012
13.type= double
13.desc= Standard deviation of angular velocity. This value is used to calculate covariance matrix.

}
}
```
