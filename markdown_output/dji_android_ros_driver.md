Source code at:
<https://github.com/Indoor-Robotics/dji_android_ros_driver>

## Overview

This package is an android mobile application for using DJI advanced
consumer drones with the ROS system.

The DJI driver is a mobile (android) application. It uses the Android
(Java) implementation of ROS and the DJI Mobile SDK to communicate with
a ROS machine and DJI drone respectfully. It exposes standard interfaces
for command velocities (twist commands) and some specific API (services)
for tasks like takeoff, landing etc. The mobile device itself should be
connected to the remote control.

Having the remote control in the loop is actually very important. It
provides extra information on its display and most importantly, a safety
mechanism to take manual control over the drone (it saved our lives
several times when the SW or sensors failed...)

## ROS API

```clearsilver
node.0 {
  name = dji_ros_driver
  desc = Bridge between ROS API to DJI Mobile SDK
  pub {
    group.0 {
      name = Status 
      0.name = /dji/status
      0.type = std_msgs/String
      0.desc = Formatted telemetry data: "battery=[batteryLevelAvg];isConnected=[isConnected];areMotorsOn=[areMotorsOn];isFlying=[isFlying];altitude=[altitude]"
   }
   group.1 {
      name = Done 
      1.name = /flight_commands/done
      1.type = std_msgs/Empty
      1.desc = an indication when a command (takeoff, land...) has finished.
   }
  }

 sub {
    group.0 {
      name = Velocity commands 
      0.name = /cmd_vel
      0.type = geometry_msgs/Twist
      0.desc = Velocity commands
    }
  }

srv {
    0.name = /flight_commands/takeoff
    0.type = std_srvs/Empty
    0.desc = A takeoff command to the drone

    1.name = /flight_commands/land
    1.type = std_srvs/Empty
    1.desc = A land command to the drone

    2.name = /flight_commands/stop
    2.type = std_srvs/Empty
    2.desc = A stop command to the drone

    3.name = /flight_commands/rotate
    3.type = std_srvs/Empty
    3.desc = Make the drone rotate in its place
}
}
node.1 {
  name = ros_connected
  desc = Internal node for connectivity checks to the ROS master.
}
```
