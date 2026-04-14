This node facilitates interaction with the iRobot create in high level
ways. For example, via a path message and/or user defined speed/turn.

------------------------------------------------------------------------

## API Documentation

```clearsilver
node.0 {
 name = base_planner_cu
 desc << EOM 
`irobot_create_cu` provides a high level interface between all other nodes and the iRobot create robot. It also keeps track of the system state (i.e. user is in control, vs. autonomous mode, etc.) and published data about the state to the rest of the system. In autonomous mode, `irobot_create_cu` controls the robot to follow paths sent to it in the `/map_cu` coordinate frame. If the user is controlling the robot via the `visualization_cu` node (or the `/cu/user_control_cu` topic), then it sends appropriate drive commands to the robot. If there is a bumper hit, then `irobot_create_cu` is in-charge of reacting and sending bumper data to the rest of the system. 
EOM
param {
  0.name= ~bumper_backup_distance
  0.default= 0.015 (m)
  0.type= double
  0.desc= After a bumper hit, the robot backs-up this distance (meters) before moving again.
  1.name= ~backup_speed
  1.default= -0.2 (m/s)
  1.type= double
  1.desc= After a bumper hit the robot moves at this speed to back up (m/s).
  2.name= ~bumper_theta_offset
  2.default= PI/6 (rad)
  2.type= double
  2.desc= Left and right bumper hits are represented as being this many radians away from local x axis.
  3.name= ~bumper_distance
  3.default= 0.35 (m)
  3.type= double
  3.desc=  Bumper hits are represented as being this far away (in meters) from the center of the robot.
  4.name= prairiedog/using_tf
  4.default= true
  4.type= bool
  4.desc= When true, the tf ROS package is used to facilitate coordinate transformations. 
 }
pub {
  0.name= /cu/odometer_pose_cu
  0.type= geometry_msgs/Pose2D
  0.desc= 2D pose created using only the wheel odometers in the local coordinate system used by the irobot create itself.
  1.name= /cu/bumper_pose_cu
  1.type= geometry_msgs/PoseStamped or geometry_msgs/Pose2D (using tf or not using tf, respectively)
  1.desc= The position of a bumper hit in map coordinates (`/map_cu` in tf).
  2.name= /cu/system_state_cu
  2.type= std_msgs/Int32
  2.desc<< EOF
A flag indicating what state `irobot_create_cu` is in: 
   . 0 = initial state (havn't recieved enough info to start moving)
   . 1 = planning and moving normally
   . 2 = bumper hit, backing up
   . 3 = no path to goal exists
   . 4 = manual stop
   . 5 = manual control
EOF
 }
sub {
  0.name= /cu/user_control_cu
  0.type= geometry_msgs/Pose2D
  0.desc= This is a simple control message for the robot base, x is forward speed and theta is turn in robot coordinates (/robot_cu).
  1.name= /cu/pose_cu
  1.type= geometry_msgs/PoseStamped
  1.desc= The robot's best estimate of where it is, given all pose data, in map coordinates (`/map_cu`).
  2.name= /cu/global_path_cu
  2.type= nav_msgs/Path
  2.desc= This is a global path between robot and goal in map coordinates (`/map_cu`).
  3.name= /cu/goal_cu
  3.type= geometry_msgs/PoseStamped
  3.desc= Pose of the goal in map coordinates (`/map_cu`).

  4.name= /cu/system_update_cu
  4.type= std_msgs/Int32
  4.desc<< EOF
A flag containing information from the base_planner_cu node: 
   . 1 = no path to goal exists.
EOF
  5.name= /cu/user_state_cu
  5.type= std_msgs/Int32
  5.desc<< EOF
A flag indicating what the user is doing via the `visualization_cu` node: 
   . 0 = passive, doing nothing
   . 1 = manual stop
   . 2 = manual control
EOF
 }
srv_called {
  0.name= /cu/get_map_cu
  0.type= nav_msgs/GetMap
  0.desc= Waits for this on boot so that `irobot_create_cu` knows `mapper_cu` is up and running before attempting interaction with it.
 }
req_tf {
  0.from = /robot_cu
  0.to   = /map_cu
  0.desc = Transform from robot to map coordinates.
 }
}
```
