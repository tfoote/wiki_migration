The localization system is responsible for merging date from the various
sensors that provide position and orientation information (or pose), and
then publishing the posterior best estimate of the Robot's pose to the
rest of the system. Assumed sensors include the Stargazer (indoor)
global positioning system and wheel odometers. Pose can also be defined
by the user.

------------------------------------------------------------------------

## API Documentation

```clearsilver
node.0 {
 name = localization_cu
 desc << EOM 
`localization_cu` is a node that subscribes to global pose and local pose data, it uses this to update an internal best estimate of the true pose in the `/map_cu` coordinate frame and then publishes that for other nodes to use. 
EOM
param {
  0.name= ~using_gps
  0.default= true
  0.type= bool
  0.desc= When true, causes `localization_cu` to wait for gps data before publishing pose. 
  1.name= ~max_pose_jump_ratio
  1.default= 2 (m)
  1.type= double
  1.desc= (meters) if pose jumps more than `max_pose_jump_ratio` * (local movement), then global pose is dropped (used to prune erroneous gps data). 
  2.name= ~odometer_pose_x_init
  2.default= 0 (m)
  2.type= double
  2.desc= Initial x value (meters) for the odometer pose (in the internal frame used by the irobot create robot). 
  3.name= ~odometer_pose_y_init
  3.default= 0 (m)
  3.type= double
  3.desc= Initial y value (meters) for the odometer pose (in the internal frame used by the irobot create robot). 
  4.name= ~odometer_pose_theta_init
  4.default= 0 (rad)
  4.type= double
  4.desc= Initial theta value (radians) for the odometer pose (in the internal frame used by the irobot create robot).
  5.name= ~posterior_pose_x_init
  5.default= 0 (m)
  5.type= double
  5.desc= Initial x value (meters) for the robot pose in the world coordinate frame (`/world_cu`).
  6.name= ~posterior_pose_y_init
  6.default= 0 (m)
  6.type= double
  6.desc= Initial y value (meters) for the robot pose in the world coordinate frame (`/world_cu`). 
  7.name= ~posterior_pose_theta_init
  7.default= 0 (rad)
  7.type= double
  7.desc= Initial theta value (radians) for the robot pose in the world coordinate frame (`/world_cu`). 

  8.name= prairiedog/using_tf
  8.default= true
  8.type= bool
  8.desc= When true, the tf ROS package is used to facilitate coordinate transformations. 
 }
pub {
  0.name= /cu/pose_cu
  0.type= geometry_msgs/PoseStamped
  0.desc= The robot's best estimate of where it is, given all pose data, in map coordinates (`/map_cu`).
 }
sub {
  0.name= /cu/odometer_pose_cu
  0.type= geometry_msgs/Pose2D
  0.desc= 2D pose created using only the wheel odometers in the local coordinate system used by the irobot create itself.
  1.name= /cu/user_pose_cu
  1.type= geometry_msgs/PoseStamped
  1.desc= a user defined pose, used to manually define the robots starting position with a GUI in map coordinates (`/map_cu`).
  2.name= /cu/stargazer_pose_cu
  2.type= geometry_msgs/Pose2D
  2.desc= Pose from (indoor) global positioning system in world coordinates (`/world_cu`).
 }
srv {
  0.name= /cu/get_pose_cu
  0.type= localization_cu/GetPose
  0.desc= The robot's best estimate of where it is, given all pose data, in map coordinates (`/map_cu`).
 }
prov_tf {
  0.from = /world_cu
  0.to   = /robot_cu
  0.desc = Transformation between world and robot
 }
req_tf {
  0.from = /world_cu
  0.to   = /map_cu
  0.desc = Transformation between world and map
 }
}
```
