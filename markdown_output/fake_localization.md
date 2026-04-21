## Description

The `fake_localization` package provides a single node,
`fake_localization`, which substitutes for a localization system,
providing a subset of the ROS API used by [amcl](amcl). This node is
most frequently used during simulation as a method to provide perfect
localization in a computationally inexpensive manner.

Specifically, `fake_localization` converts odometry data into pose,
particle cloud, and transform data of the form published by
[amcl](amcl).

## Nodes

```clearsilver
node.0 {
  name=fake_localization
  desc=`fake_localization` substitutes for a localization system, providing a subset of the ROS API used by [[amcl]]. 
  sub{
    0.name= base_pose_ground_truth
    0.type= nav_msgs/Odometry
    0.desc= The position of the robot as published by a simulator.
    1.name = initialpose
    1.type = geometry_msgs/PoseWithCovarianceStamped
    1.desc = Allows for setting the pose of fake_localization using tools like [[rviz]] or [[nav_view]] to give a custom offset from the ground truth source being published. '''New in 1.1.3'''
  }
  pub{
    0.name= amcl_pose
    0.type= geometry_msgs/PoseWithCovarianceStamped
    0.desc= Just passes through the pose reported by a simulator.
    1.name= particlecloud
    1.type= geometry_msgs/PoseArray
    1.desc=  A particle cloud used to visualize the robot's pose in [[rviz]] and [[nav_view]].
  }
  param{
    0.name=~odom_frame_id
    0.default = `"odom"`
    0.type= string
    0.desc= The name of the odometric frame of the robot.
    1.name=~delta_x
    1.default = 0.0
    1.type = double
    1.desc = The x offset between the origin of the simulator coordinate frame and the map coordinate frame published by `fake_localization`.
    2.name=~delta_y
    2.default = 0.0
    2.type = double
    2.desc = The y offset between the origin of the simulator coordinate frame and the map coordinate frame published by `fake_localization`.
    3.name=~delta_yaw
    3.default = 0.0
    3.type = double
    3.desc = The yaw offset between the origin of the simulator coordinate frame and the map coordinate frame published by `fake_localization`.
    4.name=~global_frame_id
    4.default=/map
    4.type = string
    4.desc = The frame in which to publish the `global_frame_id`&rarr;`odom_frame_id` transform over [[tf]]. '''New in 1.1.3'''
    5.name=~base_frame_id
    5.default=base_link
    5.type = string
    5.desc = The base frame of the robot. '''New in 1.1.3'''
  }
  prov_tf{
    0.from=/map
    0.to= <value of odom_frame_id parameter>
    0.desc=Passed on from the simulator over [[tf]].
}
```
