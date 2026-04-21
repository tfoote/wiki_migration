## ROS API



```clearsilver
node.0 {
name=joystick_control
desc=`joystick_control` is a package interpreting the user commands taken from a joystick driver package.
sub{
0.name= joy
0.type= sensor_msgs/Joy
0.desc= Joystick command
1.name= velocityValue
1.type= corobot_msgs/velocityValue
1.desc= Maximum speed order than can be given by the corobot_teleop node
}
pub{
0.name= PhidgetMotor
0.type= corobot_msgs/MotorCommand
0.desc= Command the movement of the robot
1.name= takepicture
1.type= corobot_msgs/takepic
1.desc= Command the order to take a screenshot
2.name= pantilt
2.type= corobot_msgs/PanTilt
2.desc= Command the movement of the pantilt camera
3.name= armPosition
3.type= corobot_msgs/MoveArm
3.desc= Command the movement of the arm
}
}
}
```


