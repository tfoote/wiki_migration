## Supported Hardware

This driver works with a Phidgets Interface Kit, Phidget Spatial and
Phidget Encoders board

## ROS API

```clearsilver
node.0 {
name=corobot_phidget
desc=`corobot_phidget` is a driver for Phidgets Phidget Interface Kit, Phidget Spatial and phidget Encoders, adapted for the Corobot. This driver was designed to get different kind of data for the corobot. 
pub{
0.name= position_data
0.type= corobot_msgs/PosMsg
0.desc= This topic sends every 50ms the position of the robot
1.name= infrared_data
1.type= corobot_msgs/IrMsg
1.desc= This topic sends every 50ms the voltage value of both infrared sensors. It also send the conversion in meters.
2.name= power_data
2.type= corobot_msgs/PowerMsg
2.desc= This topic sends every 50ms the power of battery left(in Volt)
3.name= bumper_data
3.type= corobot_msgs/BumperMsg
3.desc= This topic sends every 50ms information coming from the Bumper to tell if an obstacle has been hit or not.
4.name= gripper_data
4.type= corobot_msgs/GrippergMsg
4.desc= This topic sends every 50ms information coming from the gripper.
5.name= spatial_data
5.type= corobot_msgs/spatial
5.desc= This topic sends every 50ms information coming from the imu.
6.name= imu_data
6.type= sensor_msgs/Imu
6.desc= This topic sends every 50ms information coming from the imu.
7.name= phidget_info
7.type= corobot_msgs/phidget_info
7.desc= This topic sends once at the creation of the node information related the initialization of the phidget device.
8.name= sonar_data
8.type= corobot_msgs/RangeSensor
8.desc= This topic sends every 50ms the range in meters of every sonar sensors connected, if any.
}
srv{
0.name= phidgetnode_set_odom
0.type= corobot_srvs/SetOdom
0.desc= This service is used to set the odometer
}
param{
0.name= rearBumper
0.default = false
0.type = bool
0.desc= Defines if some bumpers are present at the rear of the robot.
1.name= bwOutput
1.type= int
1.default = -1
1.desc= pin number where the bw Output sonar connector is connected to the phidget Interface Kit, if any sonar is present.
2.name= strobeOutput
2.type= int
2.default = -1
2.desc= pin number where the strobe Output sonar connector is connected to the phidget Interface Kit, if any sonar is present.
3.name= firstSonarInput
3.type= int
3.default = -1
3.desc= pin number where the first sonar is connected to
4.name= lastSonarInput
4.type= int
4.default = -1
4.desc= pin number where the last sonar is connected to
5.name= battery
5.type= int
5.default = 0
5.desc= pin number where the battery sensor is connected
6.name= irFront
6.type= int
6.default = 1
6.desc= pin number where the front infrared sensor is connected
7.name= irBack
7.type= int
7.default = 2
7.desc= pin number where the back infrared sensor is connected
8.name= gripper
8.type= int
8.default = 3
8.desc= pin number where gripper is connected

}
}
}
```
