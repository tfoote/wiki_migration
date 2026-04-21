## Overview

The `robotino_node` package implements the `robotino_node` node
which interfaces the Robotino API2 with ROS. The `robotino_node`
publishes the data from Robotino on various topics and also implements a
few services. The `robotino_node` is also subscribed to a few topics
to receive set values.

NOTE: Kinect Support has been removed in the catkin packages. For Kinect
please use the openni packages externally.

## ROS Nodes

```clearsilver
node.0 {
 name = robotino_node
 desc = 
 pub {
  0.name= analog_readings
  0.type= robotino_msgs/AnalogReadings
  0.desc= Readings from the analog sensors on Robotino
  1.name= bumper
  1.type= std_msgs/Bool
  1.desc= Readings from the bumper sensor on Robotino
  2.name= image_raw*
  2.type= sensor_msgs/Image, sensor_msgs/CameraInfo
  2.desc= Images from the camera(s) on Robotino
  3.name= digital_readings
  3.type= robotino_msgs/DigitalReadings
  3.desc= Readings from the digital sensors on Robotino
  4.name= distance_sensors
  4.type= sensor_msgs/PointCloud
  4.desc= Readings from the distance sensors on Robotino
  5.name= gripper_state
  5.type= robotino_msgs/GripperState
  5.desc= Readings from the gripper on Robotino
  6.name= encoder_readings
  6.type= robotino_msgs/EncoderReadings
  6.desc= Encoder readings from Robotino
  7.name= scan*
  7.type= sensor_msgs/LaserScan
  7.desc= Readings from the laser range finder on Robotino
  8.name= motor_readings
  8.type= robotino_msgs/MotorReadings
  8.desc= Readings from the motors on Robotino
  9.name= odom
  9.type= nav_msgs/Odometry
  9.desc= Readings from the north-star sensor on Robotino
  10.name= power_readings
  10.type= robotino_msgs/PowerReadings
  10.desc= Power readings from Robotino
}
sub {
  0.name= set_digital_values
  0.type= robotino_msgs/DigitalReadings
  0.desc= Set digital values for digital output on Robotino
  1.name= cmd_vel
  1.type= geometry_msgs/Twist
  1.desc= Set the velocities for Robotino
}

srv {
  0.name= set_gripper_state
  0.type= robotino_msgs/SetGripperState
  0.desc= Service to open or close the gripper
  1.name= set_encoder_position 
  1.type= robotino_msgs/SetEncoderPosition
  1.desc= Service to set the encoder position
  2.name= reset_odometry
  2.type= robotino_msgs/ResetOdometry
  2.desc= Service to reset the odometry
}
param {
  0.name= ~hostname
  0.default= 192.168.5.5
  0.type= string
  0.desc= Robotino's IP Address
  1.name= ~max_linear_vel
  1.default= 0.2
  1.type= double
  1.desc= Maximum linear velocity in m/s
  2.name= ~min_linear_vel
  2.default= 0.05
  2.type= double
  2.desc= Minimum linear velocity in m/s
  3.name= ~max_angular_vel
  3.default= 1.0
  3.type= double
  3.desc= Maximum angular velocity in rad/s
  4.name= ~min_angular_vel
  4.default= 0.1
  4.type= double
  4.desc= Minimum angular velocity in rad/s
 }
}
```

#### Usage

```
roslaunch robotino_node robotino_node.launch hostname:=IPADDRESS_OF_ROBOTINO
```
