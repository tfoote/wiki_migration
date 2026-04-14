The mapping node is responsible for updating the world map with sensor
information. Initially it receives data from the robot base node (bumper
hits) and the laser scanner. It can also load data from a bitmap at
startup.

\`mapper_cu\` is responsible for accumulating sensor data in a map. It
provides a service that allows other nodes to request and receive a copy
of the current map. It also publishes map updates, thus allowing other
nodes to maintain a current version of the map with limited overhead.

------------------------------------------------------------------------

## API Documentation

```clearsilver
name = mapper_cu
desc << EOF
`mapper_cu` subscribes to sensor data from the `hokuyo_listener_cu` and `irobot_create_cu` nodes, and accumulates it in a map. It provides a map service and publishes map updates. The former sends the entire map to a requesting node, while the latter publishes recent updates to a topic. The map service and map update messages are sent in the map coordinate system scaled by the map resolution. Therefore, they are technically NOT in the `/map_cu` frame. This is done to facilitate speedy map updates between `mapper_cu` and `base_planner_cu` (and also `visualization_cu`), who use similar internal map representations. 
<<BR>> <<BR>>
Two probabilistic occupancy grid maps are used (one each for laser and bumper data) and then merged before being sent to the rest of the system. The maximum probability of obstacle from either map is used during the merge. The laser map uses a predefined number of reading about a particular grid to calculated its obstacle probability. The bumper map associates a predefined obstacle probability with a bumper hit, and also resets a grid's obstacle probability to 0 whenever the robot occupies it. 
EOF
param {
  0.name = ~map_x_size
  0.type = double
  0.desc = Map goes from 0 to this distance (meters) in the x direction.
  0.default = 20 (m)
  1.name = ~map_y_size
  1.type = double 
  1.desc = Map goes from 0 to this distance (meters) in the y direction.
  1.default = 20 (m)
  2.name = ~map_resolution
  2.type = double
  2.desc = Each map grid spans this much real-world distance (meters).
  2.default = 0.08 (m)
  3.name = ~obstacle_prior
  3.type = double
  3.desc = The prior_probability of an obstacle in the laser map.
  3.default = 0.2
  4.name = ~map_attention_span
  4.type = int
  4.desc = The last `map_attention_span` readings of a particular grid are used to calculate probability of obstacle there.
  4.default = 100
  5.name = ~scanner_range
  5.type = double
  5.desc = The range of the laser scanner in meters (used to identify safe grids within range and also prune bad data).
  5.default = 5.5 (m)
  6.name = ~bumper_obstacle_posterior
  6.type = double
  6.desc = The probability of obstacle associated with a bumper hit.
  6.default = 1.0
  7.name = ~robot_radius
  7.type = double
  7.desc = Grids within this distance (meters) of the robot origin are labeled as safe.
  7.default = 0.2 (m)
  8.name = ~global_map_x_offset
  8.type = double
  8.desc = The map (`/map_cu`) coordinate system is this far off of the world coordinate system (`/world_cu`) in the x direction. Units are in meters.
  8.default = 0 (m)
  9.name = ~global_map_y_offset
  9.type = double
  9.desc = The map (`/map_cu`) coordinate system is this far off of the world coordinate system (`/world_cu`) in the y direction. Units are in meters.
  9.default = 0 (m)
  10.name = ~global_map_theta_offset
  10.type = double
  10.desc = the map (`/map_cu`) coordinate system is this far off of the world coordinate system (`/world_cu`) rotationally. Units are in radians.
  10.default = 0 (rad)
  11.name = ~map_file
  11.type = string
  11.desc = A bitmap in this file is loaded as the initial bumper map.
  11.default = ../blank.bmp
  12.name = prairiedog/using_tf
  12.type = bool
  12.desc = When true, the tf ROS package is used to facilitate coordinate transformations.
  12.default = true
 }
pub {
  0.name = /cu/map_changes_cu
  0.type = sensor_msgs/PointCloud
  0.desc = Where each point in the cloud is a triple (x,y,z). x and y are used to denote which map grid is changed (in map coordinates scaled to resolution) and z is the new cost value of that grid. Note: map updates must be positive and non-zero.
 }
sub {
  0.name = /cu/laser_scan_cu
  0.type = hokuyo_listener_cu/PointCloudWithOrigin
  0.desc = This is a list of laser scan hits, along with the pose of the laser scanner when it captured them. Coordinates are in the map coordinate system (`/map_cu`).
  1.name = /cu/pose_cu
  1.type = geometry_msgs/PoseStamped
  1.desc = The robot's best estimate of where it is, given all pose data, in map coordinates (`/map_cu`).
  2.name = /cu/bumper_pose_cu
  2.type = geometry_msgs/PoseStamped or geometry_msgs/Pose2D  (using tf or not using tf, respectively)
  2.desc = The position of a bumper hit in map coordinates (`/map_cu`).
 }
srv {
  0.name = /cu/get_map_cu
  0.type = nav_msgs/GetMap
  0.desc = Provides a map in map coordinates scaled by resolution.
 }

srv_called {
  0.name = /cu/get_pose_cu
  0.type = localization_cu/GetPose
  0.desc = Waits for this service at boot so that `mapper_cu` knows `localization_cu` is up and running before using data provided by it.
 }
prov_tf {
  0.from = /world_cu
  0.to   = /map_cu
  0.desc = Transform between world and map coordinates.
 }
}
```
