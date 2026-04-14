NOTE: This package is unreleased at this point, the documentation is for
Willow Garage internal use only.

## Overview

This package contains the \`multi_table_node\`, which is a node that
processes point clouds of type PointCloud2 to detect tables and objects,
and generates good pick and place poses around the tables. Good pick
poses are defined as those that are near high object density areas, and
good place poses are those that are located far from table corners and
near areas of low object density. The \`multi_table_node\` is invoked
with a service call, typically from a high level application such as one
implemented in [SMACH](smach).

## ROS API

\`multi_table_node\` contains many parameters for tweaking many aspects
of the table and object detection, as well as the manipulation pose
generation. In addition, the node needs to connect to the navigation
stack in order to test the reachability of possible manipulation poses.

### ROS Parameters

```clearsilver
param {
  group.0{
    name = General
  1.name= ~processing_frame
  1.default= ""
  1.type= string
  1.desc= The frame that incoming points will be converted to before being processed. Empty string means no conversion will take place.
  2.name= ~up_direction
  2.default= 1.0
  2.type= double
  2.desc= The direction of the positive z axis in the processing frame.
  }
  group.1{
    name = Table Detection
  1.name= ~table_z_filter_min, ~table_z_filter_max
  1.default= 0.4, 1.25
  1.type= double
  1.desc= The minimum and maximum heights for points to pass through the initial filter.
  2.name= ~table_detection_voxel_size
  2.default= 0.01
  2.type= double
  2.desc= The size of the bins when downsampling points before clustering.
  3.name= ~min_table_cluster_size
  3.default= 300
  3.type= int
  3.desc= The minimum number of points in a cluster for it to be considered a possible table.
  4.name= ~table_cluster_distance
  4.default= 0.06
  4.type= double
  4.desc= The threshold for clustering when trying to find tables in the point cloud.
  5.name= ~table_inlier_threshold
  5.default= 300
  5.type= int
  5.desc= The minimum number of inliers in the plane fit to be considered a likely table.
  }
  group.2{
    name = Object Detection
  1.name= ~object_z_filter_min, ~object_z_filter_max
  1.default= 0.01, 0.50
  1.type= double
  1.desc= The minimum and maximum heights above the table top (expressed in the table top frame) that will be considered for object detection.
  2.name= ~object_detection_voxel_size
  2.default= 0.003
  2.type= double
  2.desc= The size of the bins when downsampling potential object points before clustering.
  3.name= ~min_object_cluster_size, ~max_object_cluster_size
  3.default= 20, 100
  3.type= int
  3.desc= The minimum and maximum number of points in a cluster for it to be considered an object. The maximum size is there to prevent large objects from being considered, as the robot will not be able to pick these up anyway.
  4.name= ~object_cluster_distance
  4.default= 0.03
  4.type= double
  4.desc= The threshold for clustering when trying to find object clusters.
  }
  group.3{
    name = Pose Generation
  1.name= ~table_edge_padding
  1.default= 0.4
  1.type= double
  1.desc= The amount by which the hull of a detected table is expanded outwards.
  2.name= ~pose_resolution
  2.default= 0.05
  2.type= double
  2.desc= The distance along the expanded hull between subsequent manipulation poses that will be generated.
  3.name= ~robot_side_padding
  3.default= 0.2
  3.type= double
  3.desc= For a manipulation pose to be considered reachable, poses that are +/- robot_side_padding away from the pose must be found reachable by the navigation stack. This provides an extra level of safety to prevent the choosing of poses that are considered reachable but the robot would have a hard time actually getting there.
  4.name= ~edge_angle_neighbor
  4.default= 2
  4.type= int
  4.desc= The edge angle of the expanded hull at each pose point is computed as the angle formed by that pose point plus the x-th neighbor before and after the pose point, where x is edge_angle_neighbor. Larger values of edge_angle_neighbor minimize the effect of a "jagged" table hull, but also has the effect of smoothing table corners.
  5.name= ~max_planner_tries
  5.default= 5
  5.type= int
  5.desc= The maximum number of times the navigation stack planner will be called to compute the reachability of a pose (in case the service call return an error) before marking that pose as unreachable. Needed when robot loads are high and the planner has a hard time responding 100% of the time.
  6.name= ~object_distance_max
  6.default= 1.1
  6.type= double
  6.desc= The maximum distance an object can be from a pose point and be considered reachable by the robot.
  }
}
```

### Required Services

\`multi_table_node\` requires an external service to test the
reachability of candidate poses, which is usually done with the
navigation stack. In a launch file, the topic name below should be
remapped to the appropriate service, such as the one given.

```clearsilver
pub {
  no_header= True
  0.name= nav_plan_service
  0.type= nav_msgs/GetPlan
  0.desc= The navigation plan service. On the PR2, typically /move_base_node/make_plan
}
```

### Subscribed Topics

```clearsilver
pub {
  no_header= True
  0.name= cloud_new_in
  0.type= sensor_msgs/PointCloud2
  0.desc= The point cloud that will be processed for table and object detection.
}
```

### Published Topics

```clearsilver
pub {
  no_header= True
  0.name= markers_out
  0.type= visualization_msgs/Marker
  0.desc= Various markers that show the state of table and object detection.
}
```

### Provided Services

```clearsilver
pub {
  no_header= True
  0.name= multi_table_detection
  0.type= multi_table_detector/MultiTableDetection
  0.desc= Service call to initiate the multi table detection. The request is empty and the response contains details on the tables detected, as well as the final status of the detection.
}
```

## Example Usage

Before launching the \`multi_table_node\`, you should make sure to
correctly configure the source of the point clouds that will be
processed. Although any point cloud source could work, the best results
are obtained when a persistent collision map, such as
[collision_octomap](collision_octomap), is used as the point cloud
source.

### Example Launch File

```
<launch>

  <node pkg="point_cloud_converter" type="point_cloud_converter" name="point_cloud_converter" respawn="false" output="screen">
    <remap from="points_in" to="collision_point_cloud" />
    <remap from="points2_out" to="collision_point_cloud2" />
  </node>

  <node pkg="multi_table_detector" name="multi_table_node" type="multi_table_node" respawn="false" output="screen">

    <!--topic remapping-->
    <remap from="cloud_new_in" to="collision_point_cloud2" />
    <remap from="markers_out" to="tabletop_detector_markers" />
    <remap from="nav_plan_service" to="move_base_node/make_plan" />

    <param name="up_direction" value="1.0" />
    <param name="table_detection_voxel_size" value="0.04" />
    <param name="object_detection_voxel_size" value="0.02" />
    <param name="min_table_cluster_size" value="200" />
    <param name="min_object_cluster_size" value="10" />
    <param name="object_cluster_distance" value="0.04" />
    <param name="table_z_filter_min" value="0.6" />
    <param name="table_z_filter_max" value="1.2" />
    <param name="object_z_filter_min" value="0.03" />
    <param name="object_z_filter_max" value="0.5" />
    <param name="object_distance_max" value="0.9" />
    <param name="table_edge_padding" value="0.55" />
    <param name="pose_resolution" value="0.3" />
    <param name="robot_side_padding" value="0.25" />	
    <param name="edge_angle_neighbor" value="3" />
	
  </node>

</launch>
```
