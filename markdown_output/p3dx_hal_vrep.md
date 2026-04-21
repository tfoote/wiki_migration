## Overview

Hardware Abstraction Layer (HAL) is specific part of whole p3dx testing
robot platform. It creates bridge between topics published by V-REP and
ROS environment. It carries out task of translating raw data from
simulator into standard timestamped messages of ROS. It also includes
time synchronization. This package should be used with model of
Pioneer3dx from our V-rep
[repository](https://github.com/hrnr/robo-rescue-simulation-vrep).

## Architecture

For more information about whole experimental robot stack and ideas
behind HAL please see our [repo](https://github.com/hrnr/robo-rescue).

## Dependencies

### Packages

#### p3dx_urdf_model

This [package](p3dx_urdf_model) must be included in ROS workspace prior
to generate urdf model of robot and publishing tf tree.

#### vrep_common

Clock server make use of message type from package "vrep_common". This
package is also useful for service type of communication with V-rep
environment.

##### Installation and compilation

1\. Link folder "{V-rep installation
folder}/programming/ros_packages/vrep_common" to your ROS workspace
folder "{ROS workspace folder}/src". 2. Run "catkin_make" in
terminal.

## Nodes



```clearsilver
name = clockServer
desc = This node synchronize time between V-rep simulation time and ROS time. It publish messages from special V-rep's topic "/vrep/info" into ROS dedicated clock topic [[Clock|"/clock"]]. V-rep topic publish special custom type of messages therefore it is needed to build vrep_common messages. More in Dependencies section.  
sub {
  0.name = /vrep/info
  0.type = vrep_common/VrepInfo
  0.desc = publish clock time
  }
pub {
  0.name = /clock
  0.type = rosgraph_msgs/Clock
  0.desc = more info [[Clock|here]]
  }
```

 

```clearsilver
name = accelerometer
desc = Reads data from V-rep accelerometer sensor and publish it to ROS ecosystem
sub {
  0.name = /vrep/i0_Pioneer_p3dx_Accelerometer
  0.type = std_msgs/String
  0.desc = reads accelerometer data from vrep
  }
pub {
  0.name = sensor0/axis_data
  0.type = geometry_msgs/Vector3Stamped
  0.desc = publish stamped vector of accelerations in format [X axis ,Y axis ,Z axis]
```




```clearsilver
name = gyroscope
desc = Reads data from V-rep gyroscope sensor and publish it to ROS ecosystem
sub {
  0.name = /vrep/i0_Pioneer_p3dx_GyroSensor
  0.type = std_msgs/String
  0.desc = reads accelerometer data from vrep
  }
pub {
  0.name = sensor0/axis_data
  0.type = geometry_msgs/Vector3Stamped
  0.desc = publish stamped vector of angular velocities around each axis in format [X axis ,Y axis ,Z axis]
```





```clearsilver
name = bumper
desc = Reads data from all V-rep bumper sensor and publish it to ROS ecosystem. It uses parameter "vrep_index" to identify certain robot. 
sub {
  0.name = /vrep/i0_Pioneer_p3dx_bumper0
  0.type = std_msgs/Int32
  0.desc = subscribed topic is dynamically generated. Part i0 is generated as parameter vrep_index substitution in form i[vrep_index]_Pioneer_p3dx_bumper[ID of sensor]
  }
pub {
  0.name = sensor0/Range
  0.type = sensor_msgs/Range
  0.desc = for each bumper sensor is created publisher in form sensor[ID of sensor]/Range
```

 

```clearsilver
name = ultrasonic
desc = Reads data from all V-rep bumper sensor and publish it to ROS ecosystem. It uses parameter "vrep_index" to identify certain robot. 
sub {
  0.name = /vrep/i0_Pioneer_p3dx_ultrasonicSensor0
  0.type = std_msgs/Float32
  0.desc = subscribed topic is dynamically generated. Part i0 is generated as parameter vrep_index substitution in form i[vrep_index]_Pioneer_p3dx_bumper[ID of sensor]
  }
pub {
  0.name = sensor0/Range
  0.type = sensor_msgs/Range
  0.desc = for each  ultrasonic sensor is created publisher in form sensor[ID of sensor]/Range
```




```clearsilver
name = laser
desc = It uses parameter "vrep_index" to identify certain robot. 
sub {
  0.name = /vrep/i0_Pioneer_p3dx_laserScanner
  0.type = sensor_msgs/LaserScan
  0.desc = subscribed topic is dynamically generated. Part i0 is generated as parameter vrep_index substitution in form i[vrep_index]_Pioneer_p3dx_laserScanner
  }
pub {
  0.name = sensor0/LaserScan
  0.type = sensor_msgs/LaserScan
  0.desc = publish the laser scan received from V-rep.
```





```clearsilver
name = rightMotor
desc = This node makes both way communication for right motor. It receives wheel velocity on topic setVel and sends it to V-rep topic /vrep/i0_Pioneer_p3dx_leftMotor/setVel. In other direction it receives Joint state from V-rep and publish it to getState topic in ROS. It uses parameter "vrep_index" to identify certain robot. 
sub {
  0.name = /vrep/i0_Pioneer_p3dx_rightMotor/getState
  0.type = sensor_msgs/JointState
  0.desc = subscribed topic is dynamically generated. Part i0 is generated as parameter vrep_index substitution in form i[vrep_index]_Pioneer_p3dx_leftMotor.
  1.name = setVel
  1.type = std_msgs/Float64
  1.desc = publish angular velocity for left wheel to V-rep.
  }
pub {
  0.name = getState
  0.type = sensor_msgs/JointState
  0.desc = .

  1.name = /vrep/i0_Pioneer_p3dx_rightMotor/setVel
  1.type = std_msgs/Float64
  1.desc = .
```

 

```clearsilver
name = leftMotor
desc = This node makes both way communication for left motor. It receives wheel velocity on topic setVel and sends it to V-rep topic /vrep/i0_Pioneer_p3dx_leftMotor/setVel. In other direction it receives Joint state from V-rep and publish it to getState topic in ROS. It uses parameter "vrep_index" to identify certain robot. 
sub {
  0.name = /vrep/i0_Pioneer_p3dx_leftMotor/getState
  0.type = sensor_msgs/JointState
  0.desc = subscribed topic is dynamically generated. Part i0 is generated as parameter vrep_index substitution in form i[vrep_index]_Pioneer_p3dx_leftMotor.
  1.name = setVel
  1.type = std_msgs/Float64
  1.desc = publish angular velocity for left wheel to V-rep.
  }
pub {
  0.name = getState
  0.type = sensor_msgs/JointState
  0.desc = .

  1.name = /vrep/i0_Pioneer_p3dx_leftMotor/setVel
  1.type = std_msgs/Float64
  1.desc = .
```



## Parameters

### Dynamically resolved

These parameters are resolved from node_handle namespace up in launch
file hierarchy ending in global namespace. First found occurrence of
parameter is taken.

#### vrep_index

In case of multiple same robots in V-rep environment simulator
automatically adds unique ID's to new instances of same object. Sensor
scripts in
[model repository](https://github.com/hrnr/robo-rescue-simulation-vrep)
publish unique topics for each sensor and each robot. This parameter is
robot's number in V-rep.

#### tf_prefix

Published messages to ROS use [tf_prefixes](tf) to prefix frame_id's in
messages. <Example:%5Btf_prefix%5D/base_link>.

### Global

#### /use_sim_time

This parameter must be set true when using time synchronization with
clockServer.
