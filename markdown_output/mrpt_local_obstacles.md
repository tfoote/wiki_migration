## Node

### mrpt_local_obstacles_node

A node that maintains a local obstacle map (point cloud, voxels or
occupancy grid) from recent sensor readings within a configurable time
window.

#### Published Topics

- `local_map_pointcloud`
  ([sensor_msgs/msg/PointCloud](https://docs.ros.org/en/rolling/p/sensor_msgs/msg/PointCloud.html)):
  The local map as a point cloud. The frame_id is <frameid_robot>
  (default: `odom`).

#### Parameters

- `~frameid_reference` (`string`, default: `"odom"`): TF frame name
  for the reference frame
- `~frameid_robot` (`string`, default: `"base_link"`): TF frame name
  for the robot
- `~source_topics_2dscan` (`string`, default: `"scan,laser1"`): A
  comma-separate list of topics to subscribe to for 2D
  [sensor_msgs/msg/LaserScan](https://docs.ros.org/en/rolling/p/sensor_msgs/msg/LaserScan.html)
  messages.
- `~topic_local_map_pointcloud` (`string`, default:
  `"local_map_pointcloud"`): Name of the topic where to publish the
  local map
- `~time_window` (`double`, default: `0.2`): For how long past
  observations will be stored in the local map (seconds)
- `~publish_period` (`double`, default: `0.1`): How often to publish the
  local map (seconds)
- `~show_gui` (`bool`, default: `true`): Show an independent window with
  a 3D view of the local obstacles map

#### Required tf Transforms

- <value of frameid_robot> (typ: `base_link`) → <each sensor
  frameid> (typ: `scan`, etc): local pose of each sensor on the robot
- <value of frameid_reference> (typ: `odom`) → <value of
  frameid_robot> (typ: `base_link`): pose of the robot on the
  reference frame

## Demo

This demo requires [mvsim](https://index.ros.org/p/mvsim). It simulates
one robot with 2 laser scanners and builds and publish the local
obstacle maps to `/local_map_pointcloud`:



```
roslaunch mrpt_local_obstacles demo_with_mvsim.launch
```



![attachment:local_obstacle_maps_screenshot.png](doc/local_obstacle_maps_screenshot.png)
