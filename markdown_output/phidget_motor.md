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
1.name= lmotor_cmd
1.type= std_msgs/Float32
1.desc= Command the velocity of the left motor. The Value has to be between -100 and 100.
2.name= rmotor_cmd
2.type= std_msgs/Float32
2.desc= Command the velocity of the right motor. The Value has to be between -100 and 100.
}
pub{
0.name= position_data
0.type= corobot_msgs/PosMsg
0.desc= Encoders position
1.name= lwheel
1.type= std_msgs/Int16
1.desc= Left encoder position
2.name= rwheel
2.type= std_msgs/Int16
2.desc= Right encoder position
3.name= diagnostics
3.type= diagnostic_msgs/DiagnosticArray
3.desc= Diagnostic message
}
param{
0.name= motors_inverted
0.type= Bool
0.desc= True if the left and right motors are inverted
1.name= encoders_inverted
1.type= Bool
1.desc= True if the left and right encoders are inverted
}
}
}
```
