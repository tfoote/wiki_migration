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
}
param{
0.name= serialNumber
0.type= int
0.desc= If more than one Phidget Servo controller you can set the serial number of the one you want to use
0.default= -1
}
srv{
0.name= phidgetServo_getEngaged
0.type= corobot_srvs/GetEngaged
0.desc= Get the status of a servo motor connected, to know if it is engaged ( powered on) or not.
1.name= phidgetServo_setEngaged
1.type= corobot_srvs/SetEngaged
1.desc= Set the status of a servo motor, engaged( powered on) or not.
2.name= phidgetServo_getPosition
2.type= corobot_srvs/GetPosition
2.desc= Get the position of a servo motor.
3.name= phidgetServo_setPosition
3.type= corobot_srvs/SetPosition
3.desc= Set the position of a servo motor.
4.name= phidgetServo_getPositionMax
4.type= corobot_srvs/GetPosition
4.desc=Get the maximum position possible of a servo motor.
5.name= phidgetServo_getPositionMin
5.type= corobot_srvs/GetPosition
5.desc= Get the minimum position possible of a servo motor
6.name= phidgetServo_getMotorCount
6.type= corobot_srvs/GetMotorCount
6.desc= Get the maximum number of servo motors that can be connected to this Phidget Servo controller.
7.name= phidgetServo_setServoParameters
7.type= corobot_srvs/SetParam
7.desc= Get the parameters of a servo motor.
8.name= phidgetServo_getSerialNumber
8.type= corobot_srvs/GetSerialNumber
8.desc= Get the serial number of the current phidget servo controller. Useful if there are two phidget servo controllers connected.
9.name= phidgetServo_getServoType
9.type= corobot_srvs/GetType
9.desc= Get the type of servo motor pluged in
10.name= phidgetServo_setServoType
10.type= corobot_srvs/SetType
10.desc= Set the servo motor to one of the defined types
}
}
```
