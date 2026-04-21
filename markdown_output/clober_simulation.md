*ROS Software Maintainer: [Clobot](http://wiki.ros.org/clobot)*

## Clober Simulation Package

![Clober Robot\|width=400](attachment:clober/clober_right.png)

**Clober Simulation** package contains the launch files needed for
simulation of the Clober Research Platform. Simulation within the
virtual world would mitigate the risks and likelihood of failure of
systems when it is applied into the real world. We aim to provide more
realistic environments such that more accurate results can be reproduced
in the future.

## Clober e-Manual

-   [Clober e-manual on gitbook](https://app.gitbook.com/@clobot-git/s/clober-manual/)

## ROS API



```clearsilver
node.0 {
name= gazebo
desc= This package is used [[http://wiki.ros.org/gazebo_ros|gazebo_ros]].
}
pub {
  0.name = joint_states
  0.type = sensor_msgs/JointState
  0.desc = Joint State for each non-fixed joint in the robot
  1.name = imu
  1.type = sensor_msgs/Imu
  1.desc = orientation data, including raw data of linear_acceleration and angular_velocity.
  2.name = odom
  2.type = nav_msgs/Odometry
  2.desc = estimation data of a position and velocity in free space
  3.name = scan
  3.type = sensor_msgs/LaserScan
  3.desc = single scan data from a planar laser range-finder
  4.name = tf
  4.type = tf2_msgs/TFMessage
  4.desc = maintains the relationship between coordinate frames in a tree structure buffered in time.
}
sub {
  0.name = cmd_vel
  0.type = geometry_msgs/Twist
  0.desc = Twist has a linear component, for the (x,y,z) velocities, and an angular component for the angular rate about the (x,y,z) axes.
}
```





```clearsilver
node.1 {
name= joint_state_publisher
desc= This package is used [[http://wiki.ros.rog/joint_state_publisher|joint_state_publisher]]
}
pub {
  0.name = joint_states
  0.type = sensor_msgs/JointState
  0.desc = Joint State for each non-fixed joint in the robot
}
```





```clearsilver
node.2 {
name= robot_state_publisher
desc= This package is used [[http://wiki.ros.rog/robot_state_publisher|robot_state_publisher]]
}
sub {
  0.name = joint_states
  0.type = sensor_msgs/JointState
  0.desc = joint position information
  1.name = tf
  1.type = tf2_msgs/TFMessage
  1.desc = maintains the relationship between coordinate frames in a tree structure buffered in time.
```


