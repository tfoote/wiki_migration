![](attachment:08_PartyOnStairsFront_768.jpg)

## ROS Nodes



```clearsilver
node.0 {
 name = iotbot_node
 desc = ROS interface to the kinematics and the basic sensors of [[https://www.eduart-robotik.com|EduArt]]'s IOTbot.
pub {
  0.name= rpm
  0.type= std_msgs/Float32MultiArray
  0.desc= Revolution speed of wheels in RPM.
  1.name= tof
  1.type= std_msgs/Float32MultiArray
  1.desc= Distance measurements of the infrared sensors integrated in the lighting concept.
  2.name= voltage
  2.type= std_msgs/Float32
  2.desc= Battery voltage
  3.name= imu
  3.type= sensor_msgs/Imu
  3.desc= Measurements of integrated IMU
}
sub{
  0.name= joy
  0.type= sensor_msgs/Joy
  0.desc= Subscriber to standard ROS Joy message. The concept is adjusted to an Extreme 3D Pro. Alternatively, the ROS package [[https://github.com/EduArt-Robotik/iotbot_virtual_joy|iotbot_virtual_joy]] can be used.
  1.name= vel/teleop
  1.type= geometry_msgs/Twist
  1.desc= Subscriber to standard ROS Twist message.
}
srv{
  0{
  name = enable
  type = std_srvs/SetBool
  desc = enables the drive.
  }
}
```



## Basic Installation

This package is intended to be used on the Siemens SIMATIC IOT2050
gateway. It is the core component of the IOTbot. For low-level
interfacing the MRAA library is used. For ROS installation instructions
on the IOT2050, please consult the page
<https://github.com/EduArt-Robotik/iotbot>.
