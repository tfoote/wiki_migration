## Installation

This package requires SwiftNav's
[libsbp python library](https://github.com/swift-nav/libsbp). Install
before installing this package.

**Option 1 (Recommended)** Install binaries via aptitude package manager


```
sudo apt install ros-kinetic-rr-swiftnav-piksi
```



**Option 2** Install source from github (only use if you want to make
custom changes to the source code) 

```
cd ~/catkin_ws/src/
git clone https://github.com/RoverRobotics/rr_swiftnav_piksi.git
cd ~/catkin_ws/
catkin_make
source devel/setup.bash
```



## Nodes



```clearsilver
node{
  0.name = swiftnav_piksi_tcp.py
  0.desc = The `swiftnav_piksi_tcp_node` provides a ROS driver for SwiftNav Piksi's that are connected via ethernet cable. This node will calculate the heading of a robot when moving. In order to get the orientation correct well travelling in reverse, the cmd_vel/managed topic from the rr_control_input_manager node is needed.
}
pub{
  0.name= /swift_gps/llh/position
  0.type= sensor_msgs/NavSatFix
  0.desc= Outputs the current Latitude and Longitude
  1.name= /swift_gps/llh/fix_mode
  1.type= std_msgs/Int32
  1.desc= Outputs an integer that corresponds to the current fix mode 0: Invalid 1: Single Point Position (SSP) 2: Differential GNSS (DGNSS) 3: Float RTK 4: Fixed RTK 5: Dead Reckoning 6: Satellite-Base Augmentation System(SBAS)
  2.name= /swift_gps/llh/n_sats
  2.type= std_msgs/Int32
  2.desc= Outputs the number of satellites currently being used.
  3.name= /swift_gps/baseline/ecef/position
  3.type= nav_msgs/Odometry
  3.desc= Outputs x, y distance in meters away from the basestation. This is a cm level accurate measurement when fix mode is 'rtk_fix' and should be used as input into a kalman filter (robot_localization is a good package for this). This topic also includes heading information calculated from the last two RTK positions. Heading will only be updated if distance traveled is greater than 4cm in 0.1 seconds, which corresponds with going 0.4m/s.
  4.name= /swift_gps/imu/raw
  4.type= sensor_msgs/Imu
  4.desc= Raw IMU values.
}

sub {
  0.name= /swift_nav/enable_comms
  0.type= std_msgs/Bool
  0.desc= When set to true the node will start an NCAT processs that will forward IP traffic from base station to the Piksi. Setting this false when idle is a good idea to reduce network traffic. 
  1.name= /cmd_vel/managed
  1.type= geometry_msgs/TwistStamped
  1.desc= Used to calculate heading correctly while moving
}

param {
  0.name= ~piksi_ip_address
  0.type= string
  0.default= `1.2.3.10`
  0.desc= IP Address of the SwiftNav Piksi
  1.name= ~piksi_port
  1.type= string
  1.default= '55555'
  1.desc= TCP port of the SwiftNav Piksi
  2.name= ~base_station_ip_address
  2.type= string
  2.default= `111.111.111.111`
  2.desc= IP Address or URL of the Base Station
  3.name= ~piksi_port
  3.type= string
  3.default= '55555'
  3.desc= TCP port of the Base Station
  4.name= ~computer_ip_address
  4.type= string
  4.default= `1.2.3.55`
  4.desc= IP Address of the computer connected to the Piksi
}
```



## Running

Example using rosrun 

```
rosrun rr_swiftnav_piksi swiftnav_piksi_tcp.py
```


