## Node

### mrpt_local_obstacles_node

A node that maintains a local obstacle map (point cloud, voxels or
occupancy grid) from recent sensor readings within a configurable time
window.

```clearsilver
pub {
  0.name= local_map_pointcloud
  0.type= sensor_msgs/PointCloud
  0.desc= The local map as a point cloud. The frame_id is <frameid_robot> (default: `odom`). 
}
param{
    0.name = ~frameid_reference
    0.type = string
    0.default = `"odom"`
    0.desc = TF frame name for the reference frame

    1.name = ~frameid_robot
    1.type = string
    1.default = `"base_link"`
    1.desc =  TF frame name for the robot

    2.name = ~source_topics_2dscan
    2.type = string
    2.default = `"scan,laser1"`
    2.desc = A comma-separate list of topics to subscribe to for 2D <<MsgLink(sensor_msgs/LaserScan)>> messages.

    3.name = ~topic_local_map_pointcloud
    3.type = string
    3.default = `"local_map_pointcloud"`
    3.desc = Name of the topic where to publish the local map

    4.name = ~time_window
    4.type = double
    4.default = 0.2
    4.desc = For how long past observations will be stored in the local map (seconds)

    5.name = ~publish_period
    5.type = double
    5.default = 0.1
    5.desc = How often to publish the local map (seconds)

    6.name = ~show_gui
    6.type = bool
    6.default = true
    6.desc = Show an independent window with a 3D view of the local obstacles map
}
req_tf {
    0.from = <value of ~frameid_robot> (typ: `base_link`)
    0.to = <each sensor frameid> (typ: `scan`, etc)
    0.desc = local pose of each sensor on the robot

    1.from = <value of ~frameid_reference> (typ: `odom`)
    1.to = <value of ~frameid_robot> (typ: `base_link`)
    1.desc = pose of the robot on the reference frame
}
```

## Demo

This demo requires [mvsim](mvsim). It simulates one robot with 2 laser
scanners and builds and publish the local obstacle maps to
\`/local_map_pointcloud\`:

```
roslaunch mrpt_local_obstacles demo_with_mvsim.launch
```

![](attachment:local_obstacle_maps_screenshot.png)
