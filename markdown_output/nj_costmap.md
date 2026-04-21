## Overview

The `nj_costmap` package implements a navigation jockey for the Large
Maps Framework ([LaMa](Large Maps Framework)) based on a local costmap
such as those provided by the [local_map](local_map) package (costmap
position is relative to the sensor but orientation is absolute).

The role of this jockey is to travel to the next crossing. The action is
done when the robot reaches the crossing center. It is considered to be
memory-less because it uses only an internal memory (in form of a local
map) and do not interact with the large map.

Implemented actions:

-   TRAVERSE: will start navigating to the next crossing (place with at
    least three frontiers) and will succeed when the crossing center is
    reached.
-   STOP: will stop
-   INTERRUPT: same as STOP
-   CONTINUE: same as TRAVERSE

## Usage

### ROS API



```clearsilver
sub {
   0.name= ~<name>/local_costmap
   0.type= nav_msgs/OccupancyGrid
   0.desc= local cost map which orientation is global
}
pub {
   0.name= ~<name>/cmd_vel
   0.type= geometry_msgs/Twist
   0.desc= robot set velocity
   1.name= ~<name>/crossing_marker
   1.type= visualization_msgs/Marker
   1.desc= a sphere at the crossing center.
   2.name= ~<name>/exits_marker
   2.type= visualization_msgs/Marker
   2.desc= lines from crossing center towards exits.
   3.name= ~<name>/ place_profile
   3.type= sensor_msgs/PointCloud
   3.desc= point cloud representing the place profile.
   4.name= ~<name>/abs_crossing
   4.type= lama_msgs/Crossing
   4.desc= Crossing with absolute frontier angles
}
param {
  0.name= ~<name>/odom_frame
  0.default= "/odom"
  0.type= String
  0.desc= this is the laser scan frame from which the map relative orientation is computed

  1.name= ~<name>/frontier_width
  1.type= Float
  1.desc= free space through which the robot can go

  2.name= ~<name>/robot_radius
  2.default= ~frontier_width/2
  2.type= Float
  2.desc= robot radius

  3.name= ~<name>/laser_frame
  3.default= "/base_laser_link"
  3.type= String
  3.desc= name of the laser scan frame for the obstacle avoider

  4.name= ~<name>/navigating_jockey_server_name
  4.default= node_name + "_server"
  4.type= String
  4.desc= Jockey name
}
```


