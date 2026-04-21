## Overview

A node that tracks dynamic obstacles by polling the simulator (like
[stage](stage)) for their locations. It uses a simple linear
extrapolation to predict where they will be over the next few seconds.
It can track up to four robots (in the future this will be able to track
an arbitrary number).

### ROS API



```clearsilver
pub {
  0.name  = robot_0/dynamic_obstacles
  0.type = dynamic_obs_msgs/DynamicObstacles
  0.desc = The dynamic obstacles' predicted future trajectories.
}
sub {
  0.name  = robot_1/base_pose_ground_truth
  0.type = nav_msgs/Odometry
  0.desc = The location of this robot in the simulator.
  1.name  = robot_2/base_pose_ground_truth
  1.type = nav_msgs/Odometry
  1.desc = The location of this robot in the simulator.
  2.name  = robot_3/base_pose_ground_truth
  2.type = nav_msgs/Odometry
  2.desc = The location of this robot in the simulator.
  3.name  = robot_4/base_pose_ground_truth
  3.type = nav_msgs/Odometry
  3.desc = The location of this robot in the simulator.
}
```


