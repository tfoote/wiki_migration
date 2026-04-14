## Supported Hardware

This driver works with a Phidgets Interface Kit, Phidget Spatial

## ROS API

```clearsilver
node.0 {
name=corobot_phidget
desc=`corobot_phidget` is a driver for Phidgets Phidget Interface Kit, Phidget Spatial and phidget Encoders, adapted for the Corobot. This driver was designed to get different kind of data for the corobot. 
pub{
0.name= infrared_data
0.type= corobot_msgs/IrMsg
0.desc= This topic sends every 50ms the voltage value of both infrared sensors. It also send the conversion in meters.
1.name= power_data
1.type= corobot_msgs/PowerMsg
1.desc= This topic sends every 50ms the power of battery left(in Volt)
2.name= bumper_data
2.type= corobot_msgs/BumperMsg
2.desc= This topic sends every 50ms information coming from the Bumper to tell if an obstacle has been hit or not.
3.name= sensor_data
3.type= corobot_msgs/SensorMsg
3.desc= This topic send the data of the various sensors that can be connected to the board
4.name= imu_data
4.type= sensor_msgs/Imu
4.desc= This topic sends every 50ms information coming from the imu.
5.name= magnetic_data
5.type= sensor_msgs/MagneticField
5.desc= This topic sends every 50ms information coming from the magnetometer in the IMU.
6.name= sonar_data
6.type= corobot_msgs/RangeSensor
6.desc= This topic sends every 50ms the range in meters of every sonar sensors connected, if any.
}
srv{
0.name=calibrate_gyroscope
0.type= std_srvs/Empty
0.desc= Calibrate the gyroscope. The process takes about 2 seconds and the IMU shouldn't move during that time.
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
8.name= imu
8.type= bool
8.default = true
8.desc= specify if there is an imu connected or not

}
}
}
```
