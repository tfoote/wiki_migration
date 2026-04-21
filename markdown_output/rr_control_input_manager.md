## Description

rr_control_input_manager serves two purposes

1\) It allows remapping of PS4 and Xbox 360 controllers from ROS
packages such as ds4_drv and joy. Those packages publish all button
presses and joystick commands onto a single topic. Sometimes you want
those to remap those to specific topics to be ingested by other
packages. For example we create a topic called /soft-estop. When either
the X-button on the PS4 controller or A-button on the Xbox 360
controller is pressed, a TRUE command to published to the /soft_estop
topic which is then sent to the twist_mux package which sets all
/cmd_vel to 0, functionally disabling the controller, and and remote
sources Freedom Robotics.

2\) The second is to allow acceptance of both Twist and TwistStamped
messages and checks that the time stamp is not expired, and if the
message stamp is expired discard the message.

## Default PS4 Controller and Xbox 360 Controller Button Mapping

![\|width="600px"](attachment:Xbox360_controller-button-mapping.jpg)
![\|width="600px"](attachment:rover_robotics_ps4_controller_mapping.png)

## Nodes



```clearsilver
node {
  0.name = control_input_manager
  0.desc = This package allows remapping of PS4 and Xbox 360 controllers from ROS packages such as ds4_drv and joy. Those packages publish all button presses and joystick commands onto a single topic. Sometimes you want those to remap those to specific topics to be ingested by other packages. For example we create a topic called /soft-estop. 
When either the X-button on the PS4 controller or A-button on the Xbox 360 controller is pressed, a TRUE command to published to the /soft_estop topic which is then sent to the twist_mux package which sets all /cmd_vel to 0, functionally disabling the controller, and and remote sources Freedom Robotics.  
}
sub {
  0.name= cmd_vel/joystick
  0.type= geometry_msgs/Twist
  0.desc= input from a ROS controller driver such as ds4_driver or joy
  1.name= /cmd_vel/keyboard
  1.type= geometry_msgs/Twist
  1.desc= input from a keyboard teleop package
  2.name= /cmd_vel/freedom
  2.type= geometry_msgs/Twist
  2.desc= input from Freedom Robotics client
  3.name= /cmd_vel/move_base
  3.type= geometry_msgs/Twist
  3.desc= inputs from ROS move_base
}
pub {
  0.name= /managed/joystick
  0.type= geometry_msgs/TwistStamped
  0.desc= This message is sent to the rr_openrover_basic packages to control the robot
  1.name= /managed/keyboard
  1.type= geometry_msgs/TwistStamped
  1.desc= This message is sent to the rr_openrover_basic packages to control the robot
  2.name= /managed/freedom
  2.type= geometry_msgs/TwistStamped
  2.desc= This message is sent to the rr_openrover_basic packages to control the robot
  3.name= /managed/move_base
  3.type= geometry_msgs/TwistStamped
  3.desc= This message is sent to the rr_openrover_basic packages to control the robot
}
param {
0{
name= ~max_vel_fwd
default=`2.6`
type= float
desc= Max forward velocity in m/s 
}
1{
name= ~max_vel_turn
default=`9.0`
type= float
desc= Max desired turning speed in rad/s 
}
2{
name= ~max_vel_flipper
default=`1.4`
type= float
desc= Max desired speed of flipper motor in rad/s
}
3{
name= ~default_drive_throttle
default=`0.15`
type= integer
desc= The value the throttle starts at. If max_drive_speed is set to 2.6m/s and default_drive_throttle is set 0.15, then the robot will start off going 0.39m/s
}
4{
name= ~default_flipper_throttle
default=`0.6`
type= integer
desc= The value the flipper throttle starts at. 
}
5{
name= ~adjustable_throttle
default=`true`
type= bool
desc= If set to true, the dpad will change the speed of the robot
}
}

node {
  1.name = xbox_mapper_node
  1.desc = This package allows remapping of Xbox 360 controllers from ROS packages such as joy. The joy package publishes all button presses and joystick commands onto a single topic named /joy. Sometimes you want those to remap those to specific topics to be ingested by other packages. For example by default we use this package to create a topic called /soft_estop. 
When either the A-button on the Xbox 360 controller is pressed, a TRUE command to published to the /soft_estop topic which is then sent to the twist_mux package which sets all /cmd_vel to 0, functionally disabling the controller and all other input sources like move_base or Freedom Robotics.  
}
sub {
  1.name= /joystick
  1.type= sensor_msgs/Joy
  1.desc= Joystick topic from ros joy (http://wiki.ros.org/joy)

}
pub {
  0.name= /cmd_vel/joystick
  0.type= geometry_msgs/TwistStamped
  0.desc= A cmd_vel topic reserved for joystick input
  1.name= /a_button
  1.type= std_msgs/Bool
  1.desc= True is published to this topic once when the a_button is pressed
  2.name= /b_button
  2.type= std_msgs/Bool
  2.desc= True is published to this topic once when the b_button is pressed
  3.name= /x_button
  3.type= std_msgs/Bool
  3.desc= True is published to this topic once when the x_button is pressed
  4.name= /y_button
  4.type= std_msgs/Bool
  4.desc= True is published to this topic once when the y_button is pressed
  5.name= /joystick/delay
  5.type= std_msgs/Float32
  5.desc= Joystick delay
}

node {
  2.name = ps4_mapper_node
  2.desc = This package allows remapping of PS4 controllers from ROS packages such as ds4_driver. The ds4_driver package publishes all button presses and joystick commands onto a single topic named /status. Sometimes you want those to remap those to specific topics to be ingested by other packages. For example by default we use this package to create a topic called /soft_estop. 
When either the X-button on the PS4 controller is pressed, a TRUE command to published to the /soft_estop topic which is then sent to the twist_mux package which sets all /cmd_vel to 0, functionally disabling the controller and all other input sources like move_base or Freedom Robotics.  
}
sub {
  2.name= /joystick
  2.type= sensor_msgs/Joy
  2.desc= Joystick topic from ros joy (http://wiki.ros.org/joy)
}
pub {
  0.name= /cmd_vel/joystick
  0.type= geometry_msgs/TwistStamped
  0.desc= A cmd_vel topic reserved for joystick input
  1.name= /a_button
  1.type= std_msgs/Bool
  1.desc= True is published to this topic once when the a_button is pressed
  2.name= /b_button
  2.type= std_msgs/Bool
  2.desc= True is published to this topic once when the b_button is pressed
  3.name= /x_button
  3.type= std_msgs/Bool
  3.desc= True is published to this topic once when the x_button is pressed
  4.name= /y_button
  4.type= std_msgs/Bool
  4.desc= True is published to this topic once when the y_button is pressed
  5.name= /joystick/delay
  5.type= std_msgs/Float32
  5.desc= Joystick delay
}
```


