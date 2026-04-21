## Overview

The rmp_base package provides a ros interface to control a Segway
Robotics Mobility Platform (<http://rmp.segway.com/>). It supports USB
and UDP interfaces.

Please refer to the RMP documentation for a description of the sensors'
coordinate system.

This package has only been tested on the RMP 440LE
(<http://rmp.segway.com/about-segway-robotics/segway-rmp440-le-and-se/>).

## Quick Start



```
$ roslaunch rmp_base rmp440le.launch
```



## Node



```clearsilver
node.0 {
 name = rmp_440le_node
 desc = ros interface to control a Segway RMP 440LE.
 sub {
  1.name= /rmp440le/base/vel_cmd
  1.type= geometry_msgs/TwistStamped
  1.desc= velocity command
  2.name= /rmp440le/deadman
  2.type= rmp_msgs/BoolStamped
  2.desc= deadman, needs to be pressed (true) for velocity commands to be processed. 
  3.name= /rmp440le/audio_cmd
  3.type= rmp_msgs/AudioCommand
  3.desc= audio command
}
 pub {
  1.name= /rmp440le/odom
  1.type= nav_msgs/Odometry
  1.desc= odometry
  2.name= /rmp440le/joint_states
  2.type= sensor_msgs/JointState
  2.desc= joint states
  3.name= /rmp440le/inertial
  3.type= sensor_msgs/Imu
  3.desc= inertial measurements
  4.name= /rmp440le/pse
  4.type= sensor_msgs/Imu
  4.desc= pitch state estimate
  5.name= /rmp440le/motor_status
  5.type= rmp_msgs/MotorStatus
  5.desc= motor status (current, power, ...)
  6.name= /rmp440le/battery
  6.type= rmp_msgs/Battery
  6.desc= battery status (charge level, temperature, ...)
  7.name= /rmp440le/fault_status
  7.type= rmp_msgs/FaultStatus
  7.desc= report faults
}
param {
  1.name= transport_type
  1.type= string
  1.desc= specify transport type: udb, usb
  1.default=udp
  2.name= ip_address
  2.type= string
  2.desc= specify the ip address of the rmp. This parameter is only used when transport_type is set to udp.
  2.default=192.168.0.40
  3.name= port_number
  3.type= int
  3.desc= specify the port number of the rmp. This parameter is only used when transport_type is set to udp.
  3.default=8080
  4.name= device_port
  4.type= string
  4.desc= specify a serial device. This parameter is only used when transport_type is set to usb.
  4.default=/dev/ttyACM0
  5.name= update_frequency
  5.type= double
  5.desc= specify the node process rate, [0.5, 100.0][Hz]
  5.default= 50.0
  6.name= odometry_topic
  6.type= string
  6.desc= odometry topic
  6.default= /rmp440le/odom
  7.name= joint_states_topic
  7.type= string
  7.desc= joint states topic
  7.default= /rmp440le/joint_states
  8.name= inertial_topic
  8.type= string
  8.desc= inertial topic
  8.default= /rmp440le/inertial
  9.name= pse_topic
  9.type= string
  9.desc= pse topic
  9.default= /rmp440le/pse
  10.name= motor_status_topic
  10.type= string
  10.desc= motor status topic
  10.default= /rmp440le/motor_status
  11.name= battery_topic
  11.type= string
  11.desc= battery topic
  11.default= /rmp440le/battery
  12.name= velocity_command_topic
  12.type= string
  12.desc= velocity command topic
  12.default= /rmp440le/base/vel_cmd
  13.name= deadman_topic
  13.type= string
  13.desc= deadman topic
  13.default= /rmp440le/deadman
  14.name= audio_command_topic
  14.type= string
  14.desc= audio command topic
  14.default= /rmp440le/audio_cmd
  15.name= fault_status_topic
  15.type= string
  15.desc= fault status topic
  15.default= /rmp440le/fault_status
  16.name= max_translational_velocity
  16.type= double
  16.desc= maximum translational velocity [0.0, 8.047][m/s]
  16.default= 8.0
  17.name= max_turn_rate
  17.type= string
  17.desc= maximum turn rate [0.0, 4.5][rad/s]
  17.default= 4.4
 }
}
```


