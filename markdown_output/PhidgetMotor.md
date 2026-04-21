## Supported Hardware

This driver works with a Phidgets Motor Controller

## ROS API



```clearsilver
node.0 {
name=PhidgetMotor
desc=`PhidgetMotor` is a driver for Phidgets Motor Controller. This driver was designed to control the movement of a Corobot.
sub{
0.name= PhidgetMotor
0.type= corobot_msgs/MotorCommand
0.desc= Command the movement of the robot
}
srv{
0.name= PhidgetMotor
0.type= corobot_srvs/Move
0.desc= Command the movement of the robot
}
}
}
```


