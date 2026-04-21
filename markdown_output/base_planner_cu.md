![\|height="293",width="358"](attachment:base_planner_cu.png)

This node is responsible for calculating a global path, assuming it is
provided with a map, a goal location in that map, and the robot's
current pose.

------------------------------------------------------------------------

## API Documentation

```clearsilver
node.0 {
 name = base_planner_cu
 desc << EOM 
`base_planner_cu` is a 2D path planning system. It is based on a modified version of the Field D* algorithm that uses gradient interpolation when possible to extract shorter paths. It is a re-planner---that is, it is specially designed to update an existing path with a minimum of effort, given new map data. In typical rover applications this translates into 1-2 orders of magnitude speed-up vs. algorithms such as A* that must plan from scratch each time the map changes.
<<BR>> <<BR>>
For more information on the planning algorithm see [[http://ml.cs.colorado.edu/~otte/html_stuff/research.html|Michael Otte's page on path planning]].
<<BR>> <<BR>>
`base_planner_cu` requests the initial map from a service and then updates the map using messages sent over a topic.  It can also request an entire updated map via the service. Robot pose is also requested via a service at critical times. goal and robot pose updates are available from topics.  `base_planner_cu` publishes a path from robot to goal in map coordinates (`/map_cu`).
EOM
param {
  0.name= ~obstacle_cost
  0.default= 10000
  0.type= double
  0.desc= The cost of an obstacle (of probability 1) note: this should be greater than the max path length.
  1.name= ~robot_radius
  1.default= 0.2
  1.type= double
  1.desc= The radius of the robot in meters.
  2.name= ~safety_distance
  2.default= 0.1
  2.type= double
  2.desc= Extra clearance required between robot and obstacles in meters, (this) + robot_radius = dilation radius.
  3.name= ~better_path_ratio
  3.default= 0.95
  3.type= double
  3.desc= If {`better_path_ratio` <= (new path length)/(old path length) <= 1/(`better_path_ratio`)} then use the old path (helps keep paths stable).
  4.name= ~replan_jump
  4.default= 25 (map grids)
  4.type= double
  4.desc= If the robot jumps this much or more since the last re-plan, then just rebuild search tree from scratch, instead of adjusting search tree. Units are in map-grids.
  6.name= ~using_extra_safety_distance
  6.default= true
  6.type= bool
  6.desc= When true, use a linear filter to increase cost within extra_safety_distance of obstacles.
  7.name= ~extra_safety_distance
  7.default= 0.2 (m)
  7.type= double
  7.desc= If using_extra_safety_distance = true, then if cost at grid G_1 is C_1 (after map dilation), and another grid G_2 exists within extra_safety_distance of G_1, then cost C_2 at G_2 is increased to C_1*|G_1 - G_2|/extra_safety_distance. Units are in meters.
 }
pub {
  0.name= /cu/global_path_cu
  0.type= nav_msgs/Path
  0.desc= This is a global path between robot and goal in map coordinates (`/map_cu`).
 }
sub{
  0.name= /cu/pose_cu
  0.type= geometry_msgs/PoseStamped
  0.desc= The robot's best estimate of where it is, given all pose data, in map coordinates (`/map_cu`).
  1.name= /cu/goal_cu
  1.type= geometry_msgs/PoseStamped
  1.desc= Pose of the goal in map coordinates (`/map_cu`).
  2.name= /cu/map_changes_cu
  2.type= sensor_msgs/PointCloud
  2.desc= Each point in the cloud is a triple (x,y,z). x and y are used to denote which map grid is changed (in map coordinates scaled to resolution) and z is the new cost value of that grid. Note: map updates must be positive and non-zero.
 }
srv_called {
  0.name= /cu/get_map_cu
  0.type= nav_msgs/GetMap
  0.desc= Provides a map in map coordinates scaled by resolution.
  1.name= /cu/get_pose_cu
  1.type= localization_cu/GetPose
  1.desc= The robot's best estimate of where it is, given all pose data, in map coordinates (`/map_cu`).
 }
}
```
