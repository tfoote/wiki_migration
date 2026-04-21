## Overview

A very simple (and not robust) node that uses lidar to track moving
people. This package does a basic clustering of points from a scan. It
then matches the new clusters with clusters from the previous iteration
(based on distance). The position, velocity, and size of a cluster is
updated using a simple constant velocity motion model and through
observations by using a weighted average from cluster matches. Clusters
are declared if they are moving above a minimum speed and below a
maximum. It can also uses a static [costmap_2d](costmap_2d) to help
prune out static obstacles that appear to be moving due to error (this
can be a blank map but the tracker will return more false positives). On
each iteration, after determining what clusters are considered "moving
obstacles" the node runs a basic linear extrapolation to predict where
the dynamic obstacles will be over the next few seconds and publishes a
message with this information.

The tracker's performance isn't too bad when the robot is standing
still. Once the robot is moving, the tracker's performance becomes
pretty bad especially if there is localization error. In my experience,
this becomes particularly bad when the robot is turning, and so there is
an option to disable observation updates when the robot is turning too
fast (the motion model still runs).

### ROS API



```clearsilver
pub {
  0.name  = dynamic_obstacles
  0.type = dynamic_obs_msgs/DynamicObstacles
  0.desc = The detected dynamic obstacles and their predicted future trajectories.
  1.name  = visualization_marker_array
  1.type = visualization_msgs/MarkerArray
  1.desc = Visualization markers that can be seen using [[rviz]]. It shows the clusters (blue), the dynamic obstacles (red), and the predicted future trajectories (fading red).
}
sub {
  0.name  = scan
  0.type = sensor_msgs/LaserScan
  0.desc = This message provides the laser scans used for tracking.
  1.name  = cmd_vel
  1.type = geometry_msgs/Twist
  1.desc = If the track_when_turning parameter is false, the node doesn't use observations when the robot is primarily turning. 
}
```





```clearsilver
param {
  0.name = laser_link
  0.default = "base_laser_link"
  0.type = string
  0.desc = The frame of the laser scans.
}
param {
  1.name = map_frame
  1.default = "map"
  1.type = string
  1.desc = The frame of the map.
}
param {
  2.name = use_costmap
  2.default = true
  2.type = bool
  2.desc = Whether to use a [[costmap_2d]] named tracking_costmap, to help get rid of false positives.
}
param {
  3.name = track_when_turning
  3.default = true
  3.type = bool
  3.desc = Whether to use observations while the robot is turning. Setting this to false is useful if the robot's localization is poor while turning.
}
```


