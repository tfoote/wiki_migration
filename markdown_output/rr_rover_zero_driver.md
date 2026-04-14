## Description

This code is for those working with the Rover Robotics Rover Zero V1.

![\|width=\"400px\"](attachment:rover-robotics-rover-zero_1024x.jpg)

The Rover Zero V1 uses the
[RoboClaw 2x15 motor controller](https://www.basicmicro.com/RoboClaw-2x15A-Motor-Controller_p_10.html)
which communicates via USB.

![\|width=\"150px\"](attachment:roboclaw-rover-robotics.jpg)

This package abstracts away the USB communications and allows users to
quickly get their robots moving around and doing cool things!

## Nodes

```clearsilver
node.0{
  name = rr_roverzero_driver
  desc = This package serves as a ROS driver for a Rover Robotics Rover Zero Driver which communicates via UART to a host PC running ROS. This package assumes users are using a USB cable.
}
sub {

0{
name=/cmd_vel
type=geometry_msgs/Twist
desc=A topic that controls the linear (m/s) and angular (rad/s) velocity of the robot. cmd_vel/managed should come from a package that can manage multiple sources of control (local joystick, remote keyboard, move_base, etc...) like rr_control_manager. If only one source of input is needed then this can be remapped to cmd_vel.
}
1{
name=soft_estop/enable
type=std_msgs/Bool
desc=When set to True the driver will ignore all input commands until the True message is received on the /rr_openrover_driver/soft_estop/reset topic (even if False is published to this topic). This is very useful to map to a button on a controller. If activated while using the ROS nav stack it acts as a pause button and autonomy can easily be resumed if the estop is reset before your navigation stack timeouts kick in.
}
2{
name=soft_estop/reset
type=std_msgs/Bool
desc=Used to reset the soft_estop. This is also useful to map to a button on a controller
}
}
param{
0{
name=address
type=int
default=128
desc=Roboclaw communication address
}
1{
name=baud
type=int
default=115200
desc=commuincation baudrate
}
2{
name=max_vel
type=double
default=5
desc=software cap on robot's velocity
}
3{
name=max_turn_rate
type=double
default=6.28
desc=software cap on robot's turnrate
}
4{
name=speed_to_duty_coef
type=double
default=1.02
desc=coeficient used to convert speed to duty cycle
}
5{
name=diag_frequency_hz
type=double
default=1.0
desc=diagnostic frequency
}
6{
name=motor_cmd_frequency_hz
type=double
default=30
desc=motor cmd frequency
}
7{
name=odom_frequency_hz
type=double
default=30
desc=odometry frequency
}
8{
name=cmd_vel_timeout
type=double
default=.5
desc=roboclaw communication timeout
}
9{
name=enable_encoder_odom
type=Bool
default=False
desc=enable to publish odometry data to ros
}
10{
name=enable_esc_feedback_controls
type=Bool   
default=False
desc=Enable to turn on PID with current PID settings. Will ignore PID values from PID parameters
}
11{
name=v_pid_overwrite
type=Bool
default=False
desc=Overwrite Hardware PID values with the one from PID parameters
}
12{
name=save_motor_controller_settings
type=Bool
default=false
desc=save changes to motor controller
}
13{
name=m1_v_p
type=Double
default=3
desc=Motor 1 Velocity P
}
14{
name=m1_v_i
type=Double
default=0.35
desc=Motor 1 Velocity I
}
15{
name=m1_v_d
type=Double
default=0
desc=Motor 1 Velocity D
}
16{
name=m1_v_qpps
type=Int
default=10000
desc=Motor 1 Maximum Possible Speed*
}
17{
name=m2_v_p
type=Double
default=3
desc=Motor 2 Velocity P
}
18{
name=m2_v_i
type=Double
default=0.35
desc=Motor 2 Velocity I
}
19{
name=m2_v_d
type=Double
default=0
desc=Motor 2 Velocity D
}
20{
name=m2_v_qpps
type=Int
default=10000
desc=Motor 2 Maximum Possible Speed
}
21{
name=encoder_pulses_per_turn
type=Double
default=5400
desc=Encoder Tick Per Revolution
}
22{
name=left_motor_max_current
type=Double
default=5
desc=Motor 1 Max Current Setting
}
23{
name=right_motor_max_current
type=Double
default=5
desc=Motor 2 Max Current Setting
}
24{
name=active_brake_timeout
type=double
default=1
desc=Active brake timeout
}
25{
name=odom_frame
type=tf
default=odom
desc=Robot TF Frame for Odometry
}
26{
name=base_link_frame
type=tf
default=base_link
desc=Robot TF Frame for Base Link
}
27{
name=wheel_base
type=double
default=0.358775
desc=Distance between center of wheels
}
28{
name=wheel_radius
type=Double
default=0.127
desc=Radius of wheel
}
}
pub {
0{
name=diagnostics
desc=diagnostics settings for roboclaw.
}
1{
name=odom
type=Odometry
desc=Encoder-based odometry
}
}
```
