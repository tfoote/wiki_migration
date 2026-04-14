## Supported Hardware

This driver works with a Phidgets Servo Controller

## ROS API

```clearsilver
node.0 {
name=PhidgetServo
desc=`PhidgetServo` is a driver for Phidgets Servo Controller. This driver was designed to control the movement of the arm of a Corobot.
sub{
0.name= phidgetServo_setPosition
0.type= corobot_msgs/ServoPosition
0.desc= Set the position of a servo motor
1.name= phidgetServo_setType
1.type= corobot_msgs/ServoType
1.desc= Set the type of a servo motor
}
pub{
0.name= phidgetServo_getPosition
0.type= corobot_msgs/ServoPosition
0.desc= get new position of a servo motor
1.name= diagnostics
1.type= diagnostic_msgs/DiagnosticArray
1.desc= Diagnostic messages
}
param{
0.name= serialNumber
0.type= int
0.desc= If more than one Phidget Servo controller you can set the serial number of the one you want to use
0.default= -1
}
}
```
