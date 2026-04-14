## Overview

The \`nj_laser\` package implements a navigation jockey for the Large
Maps Framework ([LaMa](Large Maps Framework)) based on a
\<\<MsgSrv(sensor_msgs/LaserScan)\>\>.

The role of this jockey is to travel to the next crossing. The action is
done when the robot reaches the crossing center. It is a reactive
memory-less because it does not interact with the large map.

Implemented actions:

-   TRAVERSE: will start navigating to the next crossing (place with at
    least three frontiers) and will succeed when the crossing center is
    reached.
-   STOP: will stop
-   INTERRUPT: same as CONTINUE
-   CONTINUE: same as TRAVERSE

## Usage

### ROS API

```clearsilver
sub {
   0.name= ~<name>/local_costmap
   0.type= sensor_msg/LaserScan
   0.desc= 360-degree laser scan
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
   3.name= ~<name>place_profile
   3.type= sensor_msgs/PointCloud
   3.desc= profile of the surroundings
   4.name= ~<name>/crossing
   4.type= lama_msgs/Crossing
   4.desc= computed crossing
}
param {
  0.name= ~<name>/frontier_width
  0.type= Float
  0.desc= free space through which the robot can go

  1.name= ~<name>/robot_radius
  1.default= frontier_width/2
  1.type= Float
  1.desc= robot radius

  2.name= ~<name>/max_frontier_distance
  2.type= Float
  2.desc= points farther than this are cut and frontier may exist

  3.name= ~<name>/navigating_jockey_server_name
  3.default= node_name + "_server"
  3.type= String
  3.desc= Jockey name
}
```
