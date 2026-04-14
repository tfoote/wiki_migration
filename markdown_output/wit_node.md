## Package Summary

Maintainer status: maintained

Maintainer: Rocwang \<825213566@qq.com\>

Download: <https://github.com/yowlings/wit_node.git>

Author: Rocwang

License: BSD

This is the ROS nodelet package for wit motion company imu and gps
sensor. Providing driver, ros driver and nodelet intergrating
program.The wit motion 9-axies IMU and GPS module provides abundant
types of data for user, including nine axises data, atmosphere pressure,
temperature, latitude,longitude, altitude, satellites number .etc

![\|width=\"100%\"](attachment:wit.jpg)

## Usage

Launch the only ROS launch file:

```
roslaunch wit_node wit.launch
```

## Dependencies and Install

1\. ROS

2\. ros-\<distro\>-ecl

Install ecl by

```
sudo apt install ros-<distro>-ecl
```

## Nodes

```clearsilver
node.0{
name=wit
desc= The wit ros node for getting IMU&GPS module data and publishing related topics. 
param {
  0.name=~port
  0.default=`/dev/ttyUSB0`
  0.type= string
  0.desc= the device port name.
}
pub {
  0.name= ~<name>/raw_data
  0.type= wit_node/ImuGpsRaw
  0.desc= All raw data provided by the wit device, including nine axises data, atmosphere pressure, temperature, latitude,longitude, altitude, satellites number .etc
  1.name= /imu
  1.type= sensor_msgs/Imu
  1.desc= The standard ROS imu sensor msg which include orientation by filtered RPY.
  2.name= /gps
  2.type= sensor_msgs/NavSatFix
  2.desc= The standard ROS gps or navigation satellites msg.
  3.name= ~<name>/related_yaw
  3.type= std_msgs/Float64
  3.desc= The offseted imu yaw data, which means the zero direction is start direction.
}
sub {
  0.name= ~<name>/reset_offset
  0.type= std_msgs/Empty
  0.desc= Reset the offset yaw angle to current yaw,  so the zero direction is turned to current direction.
}
```
