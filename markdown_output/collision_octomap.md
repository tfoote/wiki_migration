NOTE: This package is unreleased at this point, the documentation is for
Willow Garage internal use only.

NOTE: At \'\'this\'\' point, this package has been superseded by
[collider](collider).

## Overview

This package contains the \`collision_octomap_node\` node, which builds
a 3D representation of sensed data, much like
[collision_map](collision_map). In fact, this node is designed to be a
\"drop-in\" replacement for \`collision_map_node\`. The difference
between the two is that \`collision_octomap_node\` maintains its
internal representation as an octree of free and occupied space, using
the [octomap2](octomap2) library. This allows the generation collision
maps in a large volume, whereas the implementation of
[collision_map](collision_map) only maintains a collision map in the
space currently visible to the robot\'s sensors.

[Youtube](https://www.youtube.com/watch?v=l6u06j_VsXc)

### Sensor Sources

The sensor sources can be any point cloud of type PointCloud. However,
for reasons explained below, sources that contain a very large number of
points and update relatively rapidly, such as stereo vision points,
should not be used. The overall point cloud insertion time for
\`collision_octomap_node\` is much longer than for \`collision_map\`
because it uses the octree representation, which needs to clear out
freespace as well as inserting occupied cells. If large, rapidly
updating point clouds need to be temporarily incorporated into the
collision map (say, for monitoring of an arm with the stereo vision),
one could add a small modification to the code to allow overlaying
collision boxes from a given point source without actually inserting
them into the octree.

### Development Note

\`collision_octomap_node\` publishes the exact same type of the 3D
collision map as \`collision_map\`, so its output can be used directly
by other nodes for collision checking. However,
\`collision_octomap_node\` will typically publish its collision map in a
world frame (odom_combined, map, etc.) whereas \`collision_map\`
publishes in the base_link frame. While testing
\`collision_octomap_node\`, I noticed that some of the other nodes that
process the collision map would occasionally time out trying to convert
the collision map from the world frame, causing poor performance for
things like arm collision checking. I\'m not sure if this was because I
was heavily loading the system with other processes as well, but it\'s
something to look out for.

## ROS API

### ROS Parameters

```clearsilver
param {
  1.name= ~fixed_frame
  1.default= base_link
  1.type= string
  1.desc= The frame used to maintain the internal octree representation of the collision map, usually some sort of world frame
  2.name= ~resolution
  2.default= 0.1
  2.type= double
  2.desc= The smallest resolution of the internal octree, in meters. Has a large effect on insertion speed. Not recommended to use less than 0.02, at least with the current implementation of octomap2.
  3.name= ~max_range
  3.default= -1.0
  3.type= double
  3.desc= The maximum beam length that will be inserted into the octree. If a point is further than this distance, its only effect will be to clear out freespace. The default of -1.0 means the full beam length.
  4.name= ~pruning_period
  4.default= 5
  4.type= int
  4.desc= The internal octree will be pruned after every x-th data insertion, where x is the pruning period. There is a tradeoff between pruning too often and not often enough that needs to be found.
  5.name= ~dimension_x (dimension_y, dimension_z)
  5.default= 0.0
  5.type= double
  5.desc= The x (y, z) dimension of a workspace. Sensor points outside this workspace will not be inserted into the octree, which can cause problems when it comes to clearing out points from inside the workspace. Not recommended to be used in its current implementation. Default value of 0.0 means workspace is infinitely large (recommended).
  6.name= ~origin_x (origin_y, origin_z)
  6.default= 0.0
  6.type= double
  6.desc= The x (y, z) origin of a workspace in the fixed frame. Sensor points outside this workspace will not be inserted into the octree, which can cause problems when it comes to clearing out points from inside the workspace. Not recommended to be used in its current implementation. 
  7.name= cloud_sources
  7.default= none
  7.type= XmlRpcValue
  7.desc= The cloud point sources which will be used as inputs to `collision_octomap_node`, specified in a YAML file. Details below.
}
```

### cloud_sources YAML file

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
    1.type = sensor_msgs/PointCloud
    1.desc = The output collision map in point cloud form, which is simply the center points of the collision map boxes. Used for nodes that need a point cloud input topic, but should probably be eliminated in the future.
    }
  group.1{
    name = Visualization Topics
    0.name = octomap_insertion_info_array
    0.type = visualization_msgs/MarkerArray
    0.desc = Text information about the latest insertion.
    1.name = octomap_occupied_marker_array
    1.type = visualization_msgs/MarkerArray
    1.desc = Box markers of the current occupied cells in the octree. Useful for debugging.
    2.name = octomap_freespace_marker_array
    2.type = visualization_msgs/MarkerArray
    2.desc = Box markers of the current freespace cells in the octree. Useful for debugging.
    }
}
```

## Example Usage

The \`collision_octomap_node\` should be launched the same way as as
\`collision_map_node\`. An example launch file is shown below.

```
<launch>

  <node pkg="collision_octomap" type="collision_octomap_node" name="collision_octomap_node" respawn="true" output="screen" machine="c2">

    <param name="fixed_frame" type="string" value="map" />
    <param name="resolution" type="double" value="0.025" />
    <param name="max_range" type="double" value="2.5" />
    <param name="pruning_period" type="int" value="10" />

    <remap from="collision_map_out" to="collision_octomap_occ" />
    <remap from="point_cloud_out" to="collision_point_cloud" />

    <!-- cloud sources -->
    <rosparam command="load" file="$(find pr2_arm_navigation_perception)/config/collision_map_sources.yaml" />  
  </node>
</launch>
```

In the above launch file, we are using the \"map\" fixed frame, which is
provided by the navigation stack. Make sure you launch some flavor of
the navigation stack if you wish to use the map frame, otherwise use
something like \"odom_combined\". If you want to insert laser snapshots
(recommended) instead of individual laser scans, you should configure
your assembler with the same fixed frame used by
\`collision_octomap_node\`. Example launch file below.

```
<launch>
  <!-- assemble pointcloud into a full world view -->
  <node pkg="laser_assembler" type="point_cloud_assembler" output="screen"  name="point_cloud_assembler">
    <remap from="cloud" to="tilt_scan_cloud_filtered"/>
    <param name="tf_cache_time_secs" type="double" value="10.0" />
    <param name="tf_tolerance_secs" type="double" value="0.0" />
    <param name="max_clouds" type="int" value="400" />
    <param name="ignore_laser_skew" type="bool" value="true" />
    <param name="fixed_frame" type="string" value="map" />
  </node>
  
  <node pkg="pr2_arm_navigation_perception" type="pr2_laser_snapshotter" output="screen" name="laser_snapshotter">
    <remap from="laser_scanner_signal" to="laser_tilt_controller/laser_scanner_signal"/>
    <remap from="build_cloud" to="point_cloud_assembler/build_cloud" />
    <remap from="full_cloud" to="full_cloud_filtered" />
  </node> 
</launch>
```
