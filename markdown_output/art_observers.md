## Overview

This is an experimental package. Significant interface changes are
anticipated. Some are outlined below.

It provides ROS nodes for publishing observations about obstacles in the
road.

## ROS Nodes



```clearsilver
node.0 {
 name = observers_node
 desc = Observers for obstacles in lanes.
 sub {
  0.name = velodyne/obstacles
  0.type = sensor_msgs/PointCloud
  0.desc = known obstacles from Velodyne
  1.name = obstacles
  1.type = sensor_msgs/PointCloud2
  1.desc = all known obstacles
  2.name = roadmap_local
  2.type = art_msgs/ArtLanes
  2.desc = local road map
 }
 pub {
  0.name = observations
  0.type = art_msgs/ObservationArray
  0.desc = An array of current observations.
  2.name = visualization_marker_array
  2.type = visualization_msgs/MarkerArray
  2.desc = Marks for occupied map polygons.
 }
 param {
  0.name = map_frame_id
  0.type = str
  0.desc = Absolute frame ID of road map.
  0.default = "/map"
  1.name = robot_frame_id
  1.type = str
  1.desc = Frame ID of robot (resolved using `tf_prefix` if defined).
  1.default = "vehicle"
  2.name = max_range
  2.type = double
  2.desc = Maximum valid obstacle range (meters).
  2.default = 80.0
}
```

 

```clearsilver
node.0 {
 name = points_on_road
 desc = Publish point cloud of obstacles detected on the road.
 sub {
  0.name = velodyne/obstacles
  0.type = sensor_msgs/PointCloud
  0.desc = current obstacles from Velodyne
  1.name = roadmap_local
  1.type = art_msgs/ArtLanes
  1.desc = local road map
 }
 pub {
  0.name = obstacles/points_on_road
  0.type = sensor_msgs/PointCloud
  0.desc = Point cloud with each lane quadrilateral containing an obstacle.
 }
}
```



#### To Do List

-   Read input in <<MsgLink(sensor_msgs/PointCloud2)>> format.
-   Publish output in <<MsgLink(sensor_msgs/PointCloud2)>> format.
-   Make better topic names.
