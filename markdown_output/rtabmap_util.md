\<\<Include(rtabmap_ros/menu)\>\>

## Nodes

### map_assembler

\'\'\'Note\'\'\': It is recommend to use directly \`cloud_map\` or
\`proj_map\` published topics from [rtabmap](rtabmap_slam#rtabmap) node
instead of using this node.

This node subscribes to [rtabmap](rtabmap_slam#rtabmap) output topic
\`\"mapData\"\` and assembles the 3D map incrementally, then publishes
the same maps than [rtabmap](rtabmap_slam#rtabmap). See all
\'\'\'\'\'Mapping\'\'\'\'\' related topics and parameters of
[rtabmap](rtabmap_slam#rtabmap) node. You can also use all \`Grid\`
parameters from rtabmap:

```
$ rosrun rtabmap_slam rtabmap --params | grep Grid/
```

For example, setting the voxel sixe of the resulting grid/point cloud to
10 cm: ```
<launch>
<node name="map_assembler" pkg="rtabmap_util" type="map_assembler">
   <param name="Grid/CellSize" type="double" value="0.1"/>
</node>
</launch>
```

```clearsilver
sub {
  0.name = mapData
  0.type = rtabmap_msgs/MapData
  0.desc = RTAB-Map's graph and latest node data.
}

srv {
  0.name = ~reset
  0.type = std_srvs/Empty
  0.desc = Reset the cache.
}

param {
  0.name = ~regenerate_local_grids
  0.type = bool
  0.default = `"false"`
  0.desc = (>=0.20.5) If local occupancy grids are already included in `mapData`, set this to `true` to regenerate them. For example, this can be used to generate the local occupancy grids with a different sensor (e.g., `Grid/FromDepth` is different than one used in `rtabmap`).
}
```

### map_optimizer

This node is for \'\'\'advanced usage only\'\'\' as it is preferred to
use graph optimization already inside [rtabmap](rtabmap_slam#rtabmap)
node (which is the default). See related parameters in
[rtabmap](rtabmap_slam#rtabmap): ```
$rosrun rtabmap_slam rtabmap --params | grep Optimize
```

This node subscribes to [rtabmap](rtabmap_slam#rtabmap) output topic
\`\"mapData\"\` and optimize the graph, then republishes the optimized
\`\"mapData\"\`.

-   This node can be used to optimize the graph outside
    [rtabmap](rtabmap_slam#rtabmap) node. The benefice to do that is
    that we can keep optimized the global map instead of the local map
    of [rtabmap](rtabmap_slam#rtabmap). You can then connect output
    \`mapData_optimized\` to [map_assembler](rtabmap_util#map_assembler)
    to get the optimized grid, proj and cloud maps assembled again.
    \'\'\'Note that processing time for map optimization using this node
    is not bounded\'\'\' (which is the case in
    [rtabmap](rtabmap_slam#rtabmap) node).

```{=html}
<!-- -->
```
-   You could also use your own graph optimization approach instead of
    this node by modifying \`poses\` values of the
    \<\<MsgLink(rtabmap_msgs/MapData)\>\> msg. However, implementing
    your graph optimization approach inside
    [rtabmap](rtabmap_slam#rtabmap) is preferred (inherit
    [Optimizer](https://github.com/introlab/rtabmap/blob/463a5d973c3bab96382356dd763a98caf9beec34/corelib/include/rtabmap/core/Graph.h#L44-L109)
    class and add it
    [here](https://github.com/introlab/rtabmap/blob/463a5d973c3bab96382356dd763a98caf9beec34/corelib/src/Graph.cpp#L124-L137)
    with a new number, then you could select it after using the
    parameter \`RGBD/OptimizeStrategy\`).

```{=html}
<!-- -->
```
-   When using graph optimization outside
    [rtabmap](rtabmap_slam#rtabmap) node, you should set parameters
    \`RGBD/OptimizeIterations\` to \`0\`, \`RGBD/OptimizeMaxError\` to
    \`0\` and \`publish_tf\` to \`false\` for
    [rtabmap](rtabmap_slam#rtabmap) node.

```{=html}
<!-- -->
```
-   This node should not be used if [rtabmap](rtabmap_slam#rtabmap) node
    is in localization mode.

```clearsilver
sub {
  0.name = mapData
  0.type = rtabmap_msgs/MapData
  0.desc = RTAB-Map's graph and latest node data.
}

pub {
  0.name = [mapData]_optimized
  0.type = rtabmap_msgs/MapData
  0.desc = RTAB-Map's optimized graph and latest node data.

  1.name = [mapData]Graph_optimized
  1.type = rtabmap_msgs/MapGraph
  1.desc = RTAB-Map's optimized graph.
}

param {
  0.name = ~map_frame_id
  0.type = string
  0.default = `"map"`
  0.desc = The frame attached to the map.
  
  1.name = ~odom_frame_id
  1.type = string
  1.default = `"odom"`
  1.desc = The frame attached to odometry.

  2.name = ~strategy
  2.type = int
  2.default = 0
  2.desc = Optimization approach used: 0=TORO, 1=g2o and 2=GTSAM.

  3.name = ~slam_2d
  3.type = bool
  3.default = `"false"`
  3.desc = 3DoF (x,y,yaw) optimization instead of 6DoF (x,y,z,roll,pitch,yaw).

  4.name = ~robust
  4.type = bool
  4.default = `"true"`
  4.desc = Activate Vertigo robust graph optimization when g2o or GTSAM `strategy` is used.

  5.name = ~global_optimization
  5.type = bool
  5.default = `"true"`
  5.desc = Optimize the global map. If false, only the local map is optimized.	

  7.name = ~iterations
  7.type = int
  7.default = 100
  7.desc = Map optimization iterations.

  8.name = ~epsilon
  8.type = double
  8.default = 0.0
  8.desc = Stop graph optimization when error is less than `epsilon` (0=ignore epsilon).

  9.name = ~ignore_variance
  9.type = bool
  9.default = `"false"`
  9.desc = Ignore constraints' variance. If checked, identity information matrix is used for each constraint in TORO. Otherwise, an information matrix is generated from the variance saved in the links.

  11.name = ~optimize_from_last_node
  11.type = bool
  11.default = `"false"`
  11.desc = Optimize from the last node. If false, the graph is optimized from the oldest node linked to the current map.

  12.name = ~publish_tf
  12.type = bool
  12.default = `"true"`
  12.desc = Publish TF from /map to /odom.

  13.name = ~tf_delay
  13.type = double
  13.default = 0.05
  13.desc = Rate at which the TF from /map to /odom is published (20 Hz).
}
```

## Nodelets

```clearsilver
node {
  name = rtabmap_util/rgbd_relay
  desc = A relay for [[http://docs.ros.org/api/rtabmap_msgs/html/msg/RGBDImage.html|rtabmap_msgs/RGBDImage]] messages. It works like a [[http://wiki.ros.org/topic_tools/relay|topic_tools/relay]], but can also compress or uncompress data for convenience.
  sub {
    0.name = rgbd_image
    0.type = rtabmap_msgs/RGBDImage
    0.desc = RGB-D image input stream.
  }
  pub {
    0.name = [rgbd_image]_relay
    0.type = rtabmap_msgs/RGBDImage
    0.desc = RGB-D image output stream.
  }
  param {
    0.name = ~queue_size
    0.type = int
    0.desc = Size of message queue.
    0.default = 10
    1.name = ~compress
    1.type = bool
    1.desc = Publish compressed RGB-D image data.
    1.default = `"False"`
    2.name = ~uncompress
    2.type = bool
    2.desc = Publish uncompressed RGB-D image data.
    2.default = `"False"`
  }
}
```

```clearsilver
node {
  name = rtabmap_util/point_cloud_xyzrgb
  desc = Construct a point cloud from RGB and depth images or stereo images. Optional decimation, depth, voxel and noise filtering can be applied.
  sub {
    0.name = rgb/image
    0.type = sensor_msgs/Image
    0.desc = RGB image stream.
    1.name = depth/image
    1.type = sensor_msgs/Image
    1.desc = Registered depth image stream.
    2.name = rgb/camera_info
    2.type = sensor_msgs/CameraInfo
    2.desc = RGB camera metadata.
    3.name = left/image
    3.type = sensor_msgs/Image
    3.desc = Left RGB/Mono rectified image.
    4.name = left/camera_info
    4.type = sensor_msgs/CameraInfo
    4.desc = Left camera metadata.
    5.name = right/image
    5.type = sensor_msgs/Image
    5.desc = Right Mono rectified image.
    6.name = right/camera_info
    6.type = sensor_msgs/CameraInfo
    6.desc = Right camera metadata.
  }
  pub {
    0.name = cloud
    0.type = sensor_msgs/PointCloud2
    0.desc = Generated RGB point cloud.
  }
  param {
    0.name = ~queue_size
    0.type = int
    0.desc = Size of message queue for each synchronized topic.
    0.default = 10
    1.name = ~approx_sync
    1.type = bool
    1.default = `"true"`
    1.desc = Use approximate time synchronization of the input topics. If false, the input topics must have the same timestamp (set to `"false"` for stereo images).
    2.name = ~decimation
    2.type = int
    2.default = 1
    2.desc = Decimation of the images before creating the point cloud. Set to 1 to not decimate the images.
    3.name = ~voxel_size
    3.type = double
    3.default = 0.0
    3.desc = Voxel size (m) of the generated cloud. Set `0.0` to deactivate voxel filtering.
    4.name = ~min_depth
    4.type = double
    4.default = 0.0
    4.desc = Min depth (m) of the generated cloud.
    5.name = ~max_depth
    5.type = double
    5.default = 0.0
    5.desc = Max depth (m) of the generated cloud. Set `0.0` to deactivate depth filtering.
    6.name = ~noise_filter_radius
    6.type = double
    6.default = 0.0
    6.desc = Max radius (m) for searching point neighbors. Set `0.0` to deactivate noise filtering.
    7.name = ~noise_filter_min_neighbors
    7.type = int
    7.default = 5
    7.desc = Minimum neighbors of a point to keep it.
    8.name = ~normal_k
    8.type = int
    8.default = 0
    8.desc = Compute normals using k nearest neighbors (0=disabled).
    9.name = ~normal_radius
    9.type = double
    9.default = 0.0
    9.desc = Compute normals using nearest neighbors inside the radius (m) (0=disabled).
    10.name = ~filter_nans
    10.type = bool
    10.default = `"false"`
    10.desc = Remove NaNs points from output cloud (convert organized to dense point cloud)
    11.name = ~roi_ratios
    11.type = string
    11.default = `"0.0 0.0 0.0 0.0"`
    11.desc = Region of interest ratios [left, right, top, bottom] (e.g., `"0 0 0 0.2"` will cut 20% of the bottom of the image).
}
```

```clearsilver
node {
  name = rtabmap_util/point_cloud_xyz
  desc = Construct a point cloud from a depth or disparity image. Optional decimation, depth, voxel and noise filtering can be applied.
  sub {
    0.name = depth/image
    0.type = sensor_msgs/Image
    0.desc = Depth image stream.
    1.name = depth/camera_info
    1.type = sensor_msgs/CameraInfo
    1.desc = Depth camera metadata.
    2.name = disparity/image
    2.type = stereo_msgs/DisparityImage
    2.desc = Disparity image stream.
    3.name = disparity/camera_info
    3.type = sensor_msgs/CameraInfo
    3.desc = Disparity camera metadata.
  }
  pub {
    0.name = cloud
    0.type = sensor_msgs/PointCloud2
    0.desc = Generated point cloud.
  }
  param {
    0.name = ~queue_size
    0.type = int
    0.desc = Size of message queue for each synchronized topic.
    0.default = 10
    1.name = ~approx_sync
    1.type = bool
    1.default = `"true"`
    1.desc = Use approximate time synchronization of messages. If false, the image and camera info must have the same timestamps.
    2.name = ~decimation
    2.type = int
    2.default = 1
    2.desc = Decimation of the RGB/depth images before creating the point cloud. Set to 1 to not decimate the images.
    3.name = ~voxel_size
    3.type = double
    3.default = 0.0
    3.desc = Voxel size (m) of the generated cloud. Set `0.0` to deactivate voxel filtering.
    4.name = ~min_depth
    4.type = double
    4.default = 0.0
    4.desc = Min depth (m) of the generated cloud.
    5.name = ~max_depth
    5.type = double
    5.default = 0.0
    5.desc = Max depth (m) of the generated cloud. Set `0.0` to deactivate depth filtering.
    6.name = ~noise_filter_radius
    6.type = double
    6.default = 0.0
    6.desc = Max radius (m) for searching point neighbors. Set `0.0` to deactivate noise filtering.
    7.name = ~noise_filter_min_neighbors
    7.type = int
    7.default = 5
    7.desc = Minimum neighbors of a point to keep it.
    8.name = ~normal_k
    8.type = int
    8.default = 0
    8.desc = Compute normals using k nearest neighbors (0=disabled).
    9.name = ~normal_radius
    9.type = double
    9.default = 0.0
    9.desc = Compute normals using nearest neighbors inside the radius (m) (0=disabled).
    10.name = ~filter_nans
    10.type = bool
    10.default = `"false"`
    10.desc = Remove NaNs points from output cloud (convert organized to dense point cloud)
    11.name = ~roi_ratios
    11.type = string
    11.default = `"0.0 0.0 0.0 0.0"`
    11.desc = Region of interest ratios [left, right, top, bottom] (e.g., `"0 0 0 0.2"` will cut 20% of the bottom of the image).
  }
}
```

```clearsilver
node {
  name = rtabmap_util/disparity_to_depth
  desc = Convert a disparity image to a depth image.
  sub {
    0.name = disparity
    0.type = stereo_msgs/DisparityImage
    0.desc = Disparity image stream.
  }
  pub {
    0.name = depth
    0.type = sensor_msgs/Image
    0.desc = Depth image stream in m. Format TYPE_32FC1.
    1.name = depth_raw
    1.type = sensor_msgs/Image
    1.desc = Depth image stream in mm. Format TYPE_16UC1.
  }
}
```

```clearsilver
node {
  name = rtabmap_util/pointcloud_to_depthimage
  desc = Reproject a point cloud into a camera frame to create a depth image. When `fixed_frame_id` is set (e.g., "odom"), movement is taken into account by transforming the point cloud accordingly to camera timestamp. An example of usage of this nodelet can be found in the [[http://wiki.ros.org/rtabmap_ros/Tutorials/Tango%20ROS%20Streamer|Tango ROS Streamer]] tutorial.
  sub {
    0.name = camera_info
    0.type = stereo_msgs/CameraInfo
    0.desc = Camera info in which we want to reproject the points.
    1.name = cloud
    1.type = sensor_msgs/PointCloud2
    1.desc = The cloud to reproject in the camera.
  }
  pub {
    0.name = image
    0.type = sensor_msgs/Image
    0.desc = Depth image stream in m. Format TYPE_32FC1.
    1.name = image_raw
    1.type = sensor_msgs/Image
    1.desc = Depth image stream in mm. Format TYPE_16UC1.
  }
  param {
    0.name = ~queue_size
    0.type = int
    0.desc = Size of message queue for each synchronized topic.
    0.default = 10
    1.name = ~fixed_frame_id
    1.type = string
    1.desc = This frame should be set when using approximate time synchronization (`approx` is `true`). If the robot is moving, it could be "odom". If not moving, it could be "base_link". 
    1.default = ""
    2.name = ~approx
    2.type = bool
    2.desc = Approximate time synchronization.
    2.default = `"true"`
    3.name = ~wait_for_transform
    3.type = double
    3.desc = Wait duration for transform when a [[tf]] transform is not still available.
    3.default = 0.1
    4.name = ~decimation
    4.type = int
    4.desc = Scale down image size of the camera info received (creating smaller depth image).
    4.default = 1
    5.name = ~fill_holes_size
    5.type = int
    5.desc = Fill holes of empty pixels up to this size. Values are interpolated from neighbor depth values. 0 means disabled.
    5.default = 0
    6.name = ~fill_holes_error
    6.type = double
    6.desc = Maximum depth error (m) to interpolate.
    6.default = 0.1
    7.name = ~fill_iterations
    7.type = int
    7.desc = Number of iterations to fill holes.
    7.default = 1
  }
}
```

```
<launch>
<node name="map_assembler" pkg="rtabmap_util" type="map_assembler">
   <param name="Grid/CellSize" type="double" value="0.1"/>
</node>
</launch>
```0

```
<launch>
<node name="map_assembler" pkg="rtabmap_util" type="map_assembler">
   <param name="Grid/CellSize" type="double" value="0.1"/>
</node>
</launch>
```1

```
<launch>
<node name="map_assembler" pkg="rtabmap_util" type="map_assembler">
   <param name="Grid/CellSize" type="double" value="0.1"/>
</node>
</launch>
```2

### rtabmap_util/obstacles_detection

This nodelet extracts obstacles and the ground from a point cloud. The
camera must see the ground to work reliably. Since the ground is not
even, the ground is segmented by normal filtering: all points with
normal in the +z direction (+- fixed angle) are labelled as ground, all
the others are labelled as obstacles. The images below show an example.

\'\'\'Warning\'\'\': this node will use a lot of CPU ressources if the
raw point clouds are fed to it directly. A
[pcl::VoxelGrid](http://wiki.ros.org/pcl_ros/Tutorials/VoxelGrid%20filtering)
can be used to downsample the raw point cloud (e.g. like 5 cm voxel) or
[rtabmap_util/point_cloud_xyz](rtabmap_util#rtabmap_util.2Fpoint_cloud_xyz)
nodelet can be used to generate a downsampled cloud from a depth image
(e.g. decimating the depth image by 4 before creating a cloud). That
filtered point cloud would be fed to \`obstacles_detection\`.

  -- --------------------------------------------- -- --------------------------------------------- --
     ![obs1\|width=\"300\"](attachment:obs1.png)      ![obs2\|width=\"300\"](attachment:obs2.png)   
     ![obs0\|width=\"300\"](attachment:obs0.png)      ![obs4\|width=\"300\"](attachment:obs4.png)   
  -- --------------------------------------------- -- --------------------------------------------- --

```
<launch>
<node name="map_assembler" pkg="rtabmap_util" type="map_assembler">
   <param name="Grid/CellSize" type="double" value="0.1"/>
</node>
</launch>
```3

### rtabmap_util/lidar_deskewing

For
[sensor_msgs/PointCloud2](http://docs.ros.org/en/noetic/api/sensor_msgs/html/msg/PointCloud2.html)
\`input_cloud\` (3D LiDAR), each point will be deskewed based on their
timestamp during the rotation of the LiDAR using \`fixed_frame_id\`
fixed frame. The \`input_cloud\` topic should have timestamp channel as
\`t\`, \`time\` or \`stamps\`. Supported timestamp formats are FLOAT32
(seconds since header\'s timestamp) and UINT32 (nanoseconds since
header\'s timestamp). If \`input_cloud\` is organized, deskewing will be
faster (transformed per columns instead per points). For
[sensor_msgs/LaserScan](http://docs.ros.org/en/noetic/api/sensor_msgs/html/msg/LaserScan.html)
\`input_scan\` (2D LiDAR),
[laser_geometry::LaserProjection](https://docs.ros.org/en/noetic/api/laser_geometry/html/classlaser__geometry_1_1LaserProjection.html)
class is used directly to project the scan while accounting for robot
motion.

```
<launch>
<node name="map_assembler" pkg="rtabmap_util" type="map_assembler">
   <param name="Grid/CellSize" type="double" value="0.1"/>
</node>
</launch>
```4
