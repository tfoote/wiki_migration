## About

The \`ros_ethernet_rmp\` package is used to bridge ROS and a Segway RMP.
It will convert \`cmd_vel\` topic messages to the RMPCommand format and
then publish the feedback from the RMP. There is also a joint state
publisher to read in the feedback and publish the changing joint states
as necessary.

## Nodes

```clearsilver
node.0 {
  name = ethernet_rmp.py
  desc = `ethernet_rmp.py` interfaces ROS with the RMP drivers.
  sub {
    0.name = cmd_vel
    0.type = 'geometry_msgs/Twist'
    0.desc = Control the movement of the robot using movement and speed commands 
  }
  sub {
    1.name = rmp_command
    1.type = 'rmp_msgs/RMPCommand'
    1.desc = message to take RMP formatted commands to configure, set velocities and set modes of the RMP. All default values definitions for the RMP can be found in 'python_ethernet_rmp/system_defines.py'
  }
  pub {
    1.name = rmp_feedback
    1.type = 'rmp_msgs/RMPFeedback'
    1.desc = publishes all of the feedback from the RMP as arrays 
  }
  param {
    0.name = ~update_delay_sec
    0.type = `double`
    0.default = 0.05
    0.desc = time in seconds at which commands will be sent and feedback received from the RMP. Minimum value is 0.01 seconds
    1.name = ~log_data
    1.type = `bool`
    1.default = False
    1.desc = flag to log data from segway or not
    2.name = ~current_rmp_ip_addr
    2.type = `string`
    2.default = DEFAULT_IP_ADDRESS
    2.desc = The ip address of the RMP currently
    3.name = ~current_rmp_port_num
    3.type = `int`
    3.default = DEFAULT_PORT_NUMBER
    3.desc = The current port number of the RMP
    4.name = ~is_omni
    4.type = `bool`
    4.default = False
    4.desc = Flag set if the RMP is omni-directional
    5.name = ~my_velocity_limit_mps
    5.type = `double`
    5.default = DEFAULT_MAXIMUM_VELOCITY_MPS
    5.desc = the velocity limit for the RMP in meters per second
    6.name = ~my_accel_limit_mps2
    6.type = `double`
    6.default = DEFAULT_MAXIMUM_ACCELERATION_MPS2
    6.desc = the maximum acceleration for the RMP in meters per second squared
    7.name = ~my_decel_limit_mps2
    7.type = `double`
    7.default = DEFAULT_MAXIMUM_DECELERATION_MPS2
    7.desc = the maximum deceleration for the RMP in meters per second squared
    8.name = ~my_dtz_rate_mps2
    8.type = `double`
    8.default = DEFAULT_MAXIMUM_DTZ_DECEL_RATE_MPS2
    8.desc = the maximum down to zero deceleration rate for the RMP in meters per second squared
    9.name = ~my_coastdown_accel_mps2
    9.type = `double`
    9.default = DEFAULT_COASTDOWN_ACCEL_MPS2
    9.desc = The coastdown to zero acceleration, in meters per second squared.
    10.name = ~my_yaw_rate_limit_rps
    10.type = `double`
    10.default = DEFAULT_MAXIMUM_YAW_RATE_RPS
    10.desc = The maximum yaw rate in radians per second.
    11.name = ~my_yaw_accel_limit_rps2
    11.type = `double`
    11.default = DEFAULT_MAX_YAW_ACCEL_RPS2
    11.desc = The maximum yaw acceleration in radians per second squared.
    12.name = ~my_tire_diameter_m
    12.type = `double`
    12.default = DEFAULT_TIRE_DIAMETER_M
    12.desc = The tire diameter for the RMP.
    13.name = ~my_wheel_base_length_m
    13.type = `double`
    13.default = DEFAULT_WHEEL_BASE_LENGTH_M
    13.desc = The wheel base length, front to back
    14.name = ~my_wheel_track_width_m
    14.type = `double`
    14.default = DEFAULT_WHEEL_TRACK_WIDTH_M
    14.desc = The wheel track width center of left wheels to center of right wheels
    15.name = ~my_gear_ratio
    15.type = `double`
    15.default = DEFAULT_TRANSMISSION_RATIO
    15.desc = The gear ratio between the motors and the wheels 
    16.name = ~my_config_bitmap
    16.type = `int`
    16.default = DEFAULT_CONFIG_BITMAP
    16.desc = the configuration bitmap used to set the parameters 
    17.name = ~my_ip_address
    17.type = `string`
    17.default = DEFAULT_IP_ADDRESS
    17.desc = the desired ip address for the RMP. The current address is in effect until after this IP is loaded and the RMP restarted.
    18.name = ~my_port_num
    18.type = `int`
    18.default = DEFAULT_PORT_NUMBER
    18.desc = the desired port number for the RMP. The current port number is in effect until after this number is loaded and the RMP restarted.
    19.name = ~my_subnet_mask
    19.type = `string`
    19.default = DEFAULT_SUBNET_MASK
    19.desc = the subnet mask for the RMP
    20.name = ~my_gateway
    20.type = `string`
    20.default = DEFAULT_GATEWAY
    20.desc = the gateway for the RMP
    21.name = ~my_user_defined_feedback_bitmap_1
    21.type = `double`
    21.default = DEFAULT_USER_FB_1_BITMAP
    21.desc = the first user defined bitmap used to configure what feedback is sent back
    22.name = ~my_user_defined_feedback_bitmap_2
    22.type = `double`
    22.default = DEFAULT_USER_FB_2_BITMAP
    22.desc = the second user defined bitmap used to configure what feedback is sent back
    23.name = ~my_user_defined_feedback_bitmap_3
    23.type = `double`
    23.default = DEFAULT_USER_FB_3_BITMAP
    23.desc = the third user defined bitmap used to configure what feedback is sent back
    24.name = ~my_user_defined_feedback_bitmap_4
    24.type = `double`
    24.default = DEFAULT_USER_FB_4_BITMAP
    24.desc = the four user defined bitmap used to configure what feedback is sent back 
  }
}
node.1 {
  name = rmp_pose_updater.py
  desc = `rmp_pose_updater.py` publishes odom information based on the feedback from the RMP
  sub {
    0.name = rmp_feedback
    0.type = 'rmp_msgs/RMPFeedback'
    0.desc = all of the feedback from the RMP as arrays 
  }
  pub {
    0.name = odom
    0.type = 'nav_msgs/Odometry'
    0.desc = odometry of the robot based on the feedback from the RMP
  }
  param {
    0.name = ~publish_tf
    0.type = `bool`
    0.default = True
    0.desc = Flag to determine if the tf should be published 
  }
}
```

#### Transforms

\`rmp_pose_updater\` broadcasts the robot frame (\'/base_footprint\')
with respect to the odometry frame (\`/odom\`).

```clearsilver
node.2 {
  name = rmp_joint_state.py
  desc = `rmp_joint_state.py` publishes joint state information based on the feedback from the RMP
  sub {
    0.name = rmp_feedback
    0.type = 'rmp_msgs/RMPFeedback'
    0.desc = all of the feedback from the RMP as arrays 
  }
  pub {
    0.name = rmp_joint_states
    0.type = 'sensor_msgs/JointState'
    0.desc = joint state of the driving wheels are published 
  }
  param {
    0.name = ~has_two_wheels
    0.type = `bool`
    0.default = True
    0.desc = Flag to determine if the robot has two or four wheels
    1.name = ~link_left_front
    1.type = `string`
    1.default = base_link_left_wheel_joint
    1.desc = the link name of the wheel in the robot model 
    2.name = ~link_right_front
    2.type = `string`
    2.default = base_link_left_wheel_joint
    2.desc = the link name of the wheel in the robot model 
    3.name = ~link_left_rear
    3.type = `string`
    3.default = base_link_left_rear_wheel_joint
    3.desc = the link name of the wheel in the robot model 
    4.name = ~link_right_rear
    4.type = `string`
    4.default = base_link_right_rear_wheel_joint
    4.desc = the link name of the wheel in the robot model    
  }
}
```

## Installation

To install the \`ros_ethernet_rmp\` package, you can choose to either
install from source, or from the Ubuntu package:

### Source

To install from source, execute the following: ```shell
cd /path/to/your/catkin/workspace/src
git clone https://github.com/WPI-RAIL/ros_ethernet_rmp.git
cd /path/to/your/catkin/workspace
catkin_make 
catkin_make install
```

### Ubuntu Package

To install the Ubuntu package, execute the following:
```
sudo apt-get install ros-indigo-ros-ethernet-rmp
```

### Startup

The \`ros_ethernet_rmp\` package contains a \`ros_ethernet_rmp.launch\`
file. This file launches an instance of the \`ethernet_rmp.py\`,
\'rmp_pose_updater.py\' and \`rmp_joint_states.py\` nodes.
\'battery_monitor_rmp.launch\' from \'battery_monitor_rmp\' will also be
launched if the argument, include_batt_monitor, is true. It is defaulted
to true. To launch these nodes, \'\'\'with\'\'\' the battery monitor the
following command can be used:

```
roslaunch ros_ethernet_rmp ros_ethernet_rmp.launch
```

To launch these nodes \'\'\'without\'\'\' the battery monitor, the
following command can be used:

```
roslaunch ros_etehrnet_rmp ros_ethernet_rmp.launch include_batt_monitor:=false
```

## Support

Please send bug reports to the
[GitHub Issue Tracker](https://github.com/WPI-RAIL/rovio/issues). Feel
free to contact me at any point with questions and comments.

-   [Russell Toris](Russell Toris)
-   <rctoris@wpi.edu>
-   [Academic Website](http://users.wpi.edu/~rctoris/)
