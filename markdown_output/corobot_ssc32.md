## Supported Hardware

This driver works with a SSC-32 Servo controller.

## ROS API



```clearsilver
node.0 {
name=ssc32_motor
desc=`ssc32_motor` is used to control the movement of both the robot and the arm in the case the robot has a ssc32 device.
sub{
0.name= /ssc32_velocity
0.type= corobot_msgs/MotorCommand
0.desc= Set the speed of the robot
1.name= setPositionServo
1.type= corobot_msgs/ServoPosition
1.desc= Set the angle of one servo
}
param{
0.name= ssc32_port
0.default = /dev/ttyS1
0.type= string
0.desc= port to the ssc32 device

}
}
}
```


