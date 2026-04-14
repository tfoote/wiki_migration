## Nodes

```clearsilver
node {
 0{
 name = turtlebot_node
 desc = `turtlebot_node` provides output from the [[turtlebot_driver]] over ROS and includes the diagnostics, gyro, and laptop battery integration.  
 param{
  0{
  name = ~port
  type = string
  default = `/dev/ttyUSB0`
  desc = Linux USB device from which to read the data.
  }
  1{
  name = ~update_rate
  type = float
  default = `30.0`
  desc = Rate, in Hz, at which to communicate with the Create.
  }
  2{
  name = ~drive_mode
  type = string
  default = `twist`
  desc << EOM 
The desired drive mode (twist, turtle, or drive).  
  . `twist` : Takes a <<MsgLink(geometry_msgs/Twist)>> message and is [[navigation]]  compatible. 
  . `turtle` : Takes a <<MsgLink(turtlebot_node/Turtle)>> message and is [[turtlesim]] compatible.
  . `drive` : Takes a <<MsgLink(turtlebot_node/Drive)>> message which drives the TurtleBot as described in the iRobot Create manual. 
EOM
  }
  3{
  name = ~has_gyro
  type = bool
  default = `True`
  desc = Enables or disables the gyro.
  }
  4{
  name = ~odom_angular_scale_correction
  type = double
  default = `1.0`
  desc = A correction applied to the computation of the rotation in the odometry.  
  }
  5{
  name = ~odom_linear_scale_correction
  type = double
  default = `1.0`
  desc = A correction applied to the computation of the translation in odometry.  
  }
  6{
  name = ~cmd_vel_timeout
  type = double
  default = `0.6`
  desc = If a new command isn't received within this many seconds, the Create is stopped.
  }
  7{
  name = ~stop_motors_on_bump
  type = bool
  default = `True`
  desc = If True, then disallow forward motion if any bumper or wheeldrop sensor is activated (backing up and rotating are allowed).
  }
  8{
  name = ~min_abs_yaw_vel
  type = float
  default = `None`
  desc = If defined, it is the minimum (non-zero) absolute rotational velocity, in radians / second, that will be commanded.  Set this parameter if you want to avoid commanding very low rotational velocities, which can cause trouble with odometry.
  }
  9{
  name = ~bonus
  type = bool
  default = `False`
  desc = Plays Mario Bros. theme song.
  }
  3{
  name = ~gyro_scale_correction
  type = double
  default = 1.35
  desc = Scaling factor for correct gyro operation.
  }
  10{
  name = ~publish_tf
  type = bool
  default = `False`
  desc = Causes node to publish TF for odom to base_link, use only when no gyro exists.
  }
  11{
  name = ~odom_frame
  type = string
  default = odom
  desc = Name of the odometry TF frame.
  }
  12{
  name = ~base_frame
  type = string
  default = base_footprint
  desc = Name of the base TF frame.
  }
  13{
  name = ~robot_type
  type = string
  default = create
  desc = The type of the robot. Can be set to `create` or `roomba` at the moment.
  }
}
pub{
  0{
  name = ~sensor_state
  type = turtlebot_node/TurtlebotSensorState 
  desc = The sensor state updated at 10Hz.
  }
  1{
  name = odom
  type = nav_msgs/Odometry
  desc = The odometry of the robot based on the gyro and sensor_state.
  }
  2{
  name = imu/data
  type = sensor_msgs/Imu
  desc = The angular velocity and integrated position of the gryo.
  }
  3{
  name = /diagnostics
  type = diagnostic_msgs/DiagnosticArray
  desc = The system diagnostic information published at 1Hz.
  }
 }
 sub{
  0{
  name = cmd_vel
  type = geometry_msgs/Twist
  desc << EOM 
The desired velocity of the robot. The type of this message is determined by the drive_mode parameter. Default is <<MsgLink(geometry_msgs/Twist)>>.
EOM
  }
 }
 srv{
  0{
  name = ~set_digital_outputs
  type = turtlebot_node/SetDigitalOutputs
  desc = Enables and disables the three digital outputs. 
  }
  1{
  name = ~set_operation_mode
  type = turtlebot_node/SetTurtlebotMode 
  desc <<EOM
Set the operation mode of the iRobot Create. The message values for digital out and operation mode are found in <<MsgLink(turtlebot_node/TurtlebotSensorState)>>.
  . `passive`: The robot can only be charged in this mode but cannot be commanded in this mode.  
  . `safe`: The robot cannot be commanded in this mode or be charged in this mode.
  . `full`: The robot cannot be charged in this mode but can be commanded. 
EOM
  }
 }
 } 
 1{
 name = laptop_battery_monitor.py
 desc = `laptop_battery_monitor.py` provides the laptop battery status to the diagnostics.  
 pub{
  1{
  name = /diagnostics
  type = diagnostic_msgs/DiagnosticArray
  desc = The laptop battery diagnostic information published at 1Hz.
  }
  2{
  name = laptop_charge
  type = turtlebot_node/LaptopChargeStatus
  desc = Machine readable laptop charge status at 1Hz.
  }
 }
 } 
 2{
 name = kinect_breaker_enabler
 desc = `kinect_breaker_enabler` enables the kinect breaker (0) for powering the kinect by putting the create in full mode and turning breaker 0 on.  
 }
}
```
