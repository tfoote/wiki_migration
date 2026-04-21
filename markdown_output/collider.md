## Overview

*NOTE: This package is currently unreleased and contains experimental
code. The documentation below describes the current version in the
[arm_navigation_metrics branch](https://code.ros.org/svn/wg-ros-pkg/stacks/motion_planning_common/branches/arm_navigation_metrics/collider)
of motion_planning_common*, *which might be released in E-turtle.*

`collider` provides a collision map for tabletop manipulation. Various
sources of input data (e.g. laser and textured stereo) are fused and
integrated into an [octomap](octomap) with raycasting in 3D. This
enables a dynamically updated collision map for manipulation and serves
as a drop-in replacement for [collision_map](collision_map). collider
supersedes [collision_octomap](collision_octomap).

## ROS API

### ROS Parameters



```clearsilver
param {
  2.name= ~resolution
  2.default= 0.1
  2.type= double
  2.desc= The smallest resolution of the internal octree in meters. This directly influences the update speed.
  3.name= ~max_range
  3.default= -1.0
  3.type= double
  3.desc= The maximum beam length that will be inserted into the octree. If a point is further than this distance, freespace will be cleared only up to the distance. The default of -1.0 means the full beam length. This directly influences the update speed.
  4.name= ~pruning_period
  4.default= 5
  4.type= int
  4.desc= The internal octree will be pruned after every x-th data insertion, where x is the pruning period. There is a tradeoff between pruning too often and not often enough that needs to be found.

  5.name= cloud_sources
  5.default= none
  5.type= XmlRpcValue
  5.desc= The !PointCloud2 data sources which will be used as inputs to `collider`. Details below.

  6.name=sensor_model_hit
  6.type=double
  6.default=0.7
  6.desc= Octomap sensor model: probablity for a hit

  7.name=sensor_model_miss
  7.type=double
  7.default=0.4
  7.desc= Octomap sensor model: probablity for a hit

  8.name=sensor_model_min
  8.type=double
  8.default=0.12
  8.desc= Octomap sensor model: Minimum clamping value

  7.name=sensor_model_max
  7.type=double
  7.default=0.97
  7.desc= Octomap sensor model: Maximum clamping value


}
```



### cloud_sources parameter

An example of the cloud_sources YAML file is given below. Note that this
is the same format used for the regular [collision_map](collision_map).


```
cloud_sources:
  - name: full_cloud_filtered
    frame_subsample: 1
    point_subsample: 1
    sensor_frame: laser_tilt_mount_link
```



### Published Topics



```clearsilver
sub{
  no_header = True
  group.0{
    name = Data Topics
    0.name = collision_map_out
    0.type = mapping_msgs/CollisionMap
    0.desc = The output collision map, defined as a set of boxes with a given center point and edge lengths.

    1.name = point_cloud_out
    1.type = sensor_msgs/PointCloud2
    1.desc = The output collision map in point cloud form, which is simply the center points of the collision map boxes. Used for nodes that need a point cloud input topic, but should probably be eliminated in the future.
    }
  group.1{
    name = Visualization Topics
    0.name = octomap_insertion_info_array
    0.type = visualization_msgs/MarkerArray
    0.desc = Text information about the latest insertion.
    1.name = occupied_cells
    1.type = visualization_msgs/Marker
    1.desc = Box markers of the current occupied cells in the octree. Useful for debugging.
    2.name = free_cells
    2.type = visualization_msgs/Marker
    2.desc = Box markers of the current freespace cells in the octree. Useful for debugging - but generates and displays huge amounts of data!
    }
}
```


