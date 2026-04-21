The goal server remembers the robot's goal and makes this information
available to the rest of the system. It is advantageous to have a single
node in charge of this, in order to keep the overall system consistent.
Whenever a change in the goal is desired, a message containing the new
goal pose is sent to the goal server.

------------------------------------------------------------------------

## API Documentation

```clearsilver
node.0 {
 name = goal_server_cu
 desc << EOM 
`goal_server_cu` keeps track of the current goal and makes this available to the system in the map coordinate frame (`/map_cu`). `goal_server_cu` subscribes to a topic where incoming messages are remembered as the current goal, which is then published and also available via a service.
EOM
param {
  0.name= ~goal_pose_x_init
  0.default= 0 (m)
  0.type= double
  0.desc= Initial x value for the goal pose (`/map_cu`). Units are in meters.
  1.name= ~goal_pose_y_init
  1.default= 0 (m)
  1.type= double
  1.desc= Initial y value for the goal pose (`/map_cu`). Units are in meters.
  2.name= ~goal_pose_theta_init
  2.default= 0 (rad)
  2.type= double
  2.desc= Initial theta value for the odometer pose (`/map_cu`). Units are in radians.
 }
pub {
  0.name= /cu/goal_cu
  0.type= geometry_msgs/PoseStamped
  0.desc= Pose of the goal in map coordinates (`/map_cu`).
 }
sub{
  0.name= /cu/reset_goal_cu
  0.type= geometry_msgs/PoseStamped
  0.desc= A new robot goal in map coordinates (`/map_cu`).
 }
srv {
  0.name= /cu/get_goal_cu
  0.type= localization_cu/GetPose
  0.desc= Pose of the goal in map coordinates (`/map_cu`).
 }
}
```
