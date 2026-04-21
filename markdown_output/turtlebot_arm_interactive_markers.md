## Documentation

See this
[Tutorial](turtlebot_arm_interactive_markers/Tutorials/UsingArmInteractiveMarkers)
for instructions on how to use rviz interactive markers to control the
arm.

## Video

[Youtube](https://www.youtube.com/watch?v=3QbuSb3unRc)

## Requirements

`arm.launch` and `simple_arm_server.launch` from the
[turtlebot_arm_bringup](turtlebot_arm_bringup) package have to be
running.

To start up the markers, run: 

```
roslaunch turtlebot_arm_interactive_markers arm_markers.launch
```



## Files

`launch/arm_markers.launch` This launch file will bring up the
interactive marker server.

## Nodes



```clearsilver
name = turtlebot_arm_marker_server
desc = Hosts an [[interactive_markers]] server to let the user control the TurtleBot arm through rviz.

pub {
  0.name = /<joint_name>/command
  0.type = std_msgs/Float64
  0.desc = For each joint indicated in the ~/joints parameter, this publishes to the joint's command topic for the joint control mode.
}
srv_called {
  0.name = /<joint_name>/relax
  0.type = arbotix_msgs/Relax
  0.desc = For each joint indicated in the ~/joints parameter, this calls a service to relax (unpower) a particular joint servo.
}
param {
  0.name = ~root_link
  0.type = string
  0.desc = The root link of the arm. This should be the bottom link of the arm.
  0.default = /arm_base_link

  1.name = ~tip_link
  1.type = string
  1.desc = The tip link of the arm. This should be the last joint ''before'' the gripper, and the gripper will be offset from here.
  1.default = /gripper_link

  2.name = ~move_time
  2.type = double
  2.desc = The amount of time to request for the trajectory move, in seconds. Having this value be higher will make the motion slower but smoother.
  2.default = 2.0

  3.name = ~joints
  3.type = list of strings
  3.desc = The name of all the joints in the arm, including the gripper joint, for individual joint control.

  4.name = ~links
  4.type = list of strings
  4.desc = The name of all the links in the arm, including the gripper link, for individual joint control. These should be ''in the same order'' as the ~/joints parameter.

  5.name = ~gripper/marker_offset/x
  5.type = double
  5.desc = In trajectory control mode, the offset for the gripper marker. This is determined by gripper dimensions.
  5.default = 0.02

  6.name = ~gripper/marker_offset/y
  6.type = double
  6.desc = In trajectory control mode, the offset for the gripper marker. This is determined by gripper dimensions.
  6.default = 0.025

  7.name = ~gripper/marker_offset/z
  7.type = double
  7.desc = In trajectory control mode, the offset for the gripper marker. This is determined by gripper dimensions.
  7.default = 0.0

  8.name = ~gripper/box_offset/x
  8.type = double
  8.desc = In trajectory control mode, the offset for the gripper box from the gripper marker. This is determined by gripper dimensions.
  8.default = -0.017

  9.name = ~gripper/box_offset/y
  9.type = double
  9.desc = In trajectory control mode, the offset for the gripper box from the gripper marker. This is determined by gripper dimensions.
  9.default = -0.008

  10.name = ~gripper/box_offset/z
  10.type = double
  10.desc = In trajectory control mode, the offset for the gripper box from the gripper marker. This is determined by gripper dimensions.
  10.default = 0.0
}
req_tf {
  0.from = <root_link>
  0.to   = <tip_link>
  0.desc = This transform is necessary for visualizing the correct position of the arm marker.
}
```


