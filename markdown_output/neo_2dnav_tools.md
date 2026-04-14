## Tools

this package contains the following tools:

### multiple goal navigation

A tool for setting multiple waypoints which the robot should visit (in
an infinite loop). ```clearsilver
sub {
  0.name = /clear_way_points
  0.type = std_msgs/Empty
  0.desc = clears the path
  1.name = /multi_goal_path
  1.type = nav_msgs/Path
  1.desc = sets a path consisting of waypoints
  2.name = /add_way_point
  2.type = geometry_msgs/PoseStamped
  2.desc = adds a way point at the end of the path
  3.name = /odom
  3.type = nav_msgs/Odometry
  3.desc = needed to get twist
  4.name = /goal_sleep_time
  4.type = std_msgs/Float32
  4.desc = how long should the robot stay at each waypoint?
}
pub {
  0.name = /move_base_simple/goal
  0.type = geometry_msgs/PoseStamped
  0.desc = publishes the current goal
  1.name = /get_multi_path
  1.type = nav_msgs/Path
  1.desc = publishes the current path
  2.name = /cmd_vel
  2.type = geometry_msgs/Twist
  2.desc = sets the robots twist to 0 if the robot plans a new path
  3.name = deltaWay
  3.type = std_msgs/Float32
  3.desc = publishes total travelled distance
}
req_tf {
  0.from = /map
  0.to = /base_link
}
```
