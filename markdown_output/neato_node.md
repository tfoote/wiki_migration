## Overview

This package provides a node wrapper for the neato_driver code. It
allows control of the Neato XV-11.

## ROS API

```clearsilver
name=neato.py
desc=Provides an ROS interface to the Neato XV-11 robot.  
pub {
  0.name = /base_scan
  0.type = sensor_msgs/LaserScan
  0.desc = Laser output from the Neato robot. 
  1.name = /odom
  1.type = nav_msgs/Odometry
  1.desc = Odometry output from the Neato robot.
}
sub {
  0.name = /cmd_vel
  0.type = geometry_msgs/Twist
  0.desc = Velocity commands for the mobile base
}
param {
  0.name = ~port
  0.type = str
  0.desc = Name of serial port to use.
  0.default = /dev/ttyUSB0
}
```

## Running

Plug in your neato. Then run: ```
lsusb
``` Find the neato
device (ours was ID 2108:780b). Then: ```
sudo modprobe usbserial vendor=0x2108 product=0x780b
``` You
should now have a /dev/ttyUSBX like device connected. You can start the
neato node by: ```
roslaunch neato_node bringup.launch
``` This loads the node and a static
TF transformer for base_laser to base_link.
