## Overview

The wit_imu package is a ROS driver for WIT IMU devices. Support device:
JY901 WT901C.

## Node API



```clearsilver
name = Topic
pub {
  0.name = /mag_data
  0.type = sensor_msgs/MagneticField
  0.desc = Topic of publish Magnetometer topic.
  1.name = /imu_data
  1.type = sensor_msgs/Imu
  1.desc = Topic of publish IMU topic.
}
```

 

```clearsilver
name = Param
desc = The launch file should set these params.


param{
  0.name = ~<name>/port
  0.default = ttyUSB0
  0.type = string
  0.desc = Serial port of the device.
  1.name = ~<name>/baudrate
  1.default = 115200
  1.type = int32
  1.desc = Baud rate.
  2.name = ~<name>/publish_rate
  2.default = 20
  2.type = int32
  2.desc = Publish frequency.
  3.name = ~<name>/publish_mag
  3.default = true
  3.type = bool
  3.desc = Whether to publish magnetometer news.
  4.name = ~<name>/imu_topic
  4.default = imu_data
  4.type = string
  4.desc = Topic of publish IMU topic.
  5.name = ~<name>/mag_topic
  5.default = mag_data
  5.type = string
  5.desc = Topic of publish Magnetometer topic.
  6.name = ~<name>/imu_frame
  6.default = imu_link
  6.type = string
  6.desc = Frame of publish IMU topic.
}
```


