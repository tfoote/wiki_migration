## Overview

A ROS driver for the
[Advanced Navigation Orientus IMU](http://www.advancednavigation.com.au/product/orientus).

## Nodes



```clearsilver
node.0 {
  name = orientus_node
  desc = Node to communicate with an Orientus IMU.
  pub {
    0.name = imu/data
    0.type = sensor_msgs/Imu
    0.desc = The filtered orientation and sensor data output of the IMU.
    1.name = imu/raw
    1.type = sensor_msgs/Imu
    1.desc = The raw accelerator and sensor data from the IMU. The orientation field is not filled in.
    2.name = imu/mag
    2.type = sensor_msgs/MagneticField
    2.desc = The raw magnetics sensor output.
    3.name = imu/temp
    3.type = sensor_msgs/Temperature
    3.desc = The raw imu temperature.
    4.name = /diagnostics
    4.type = diagnostic_msgs/DiagnosticArray
    4.desc = Diagnostic information about the sensor.
  }
  param {
    0.name = ~port
    0.type = string
    0.default = /dev/ttyUSB0
    0.desc = The serial port to use to communicate with the device.
    1.name = ~frame_id
    1.type = string
    1.default = imu
    1.desc = The name of the tf frame that messages are published with.
  }
}
```


