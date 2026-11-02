

```wiki
'''''[[rtabmap_ros]]:''' [[rtabmap]] | [[rtabmap_conversions]] | [[rtabmap_costmap_plugins]] | [[rtabmap_demos]] | [[rtabmap_examples]] | [[rtabmap_launch]] | [[rtabmap_legacy]] | [[rtabmap_msgs]] | [[rtabmap_odom]] | [[rtabmap_python]] | [[rtabmap_rviz_plugins]] | [[rtabmap_slam]] | [[rtabmap_sync]] | [[rtabmap_util]] | [[rtabmap_viz]]''
```



## Nodes

### map_assembler

**Note**: It is recommend to use directly `cloud_map` or `proj_map`
published topics from [rtabmap](https://index.ros.org/p/rtabmap_slam)
node instead of using this node.

This node subscribes to [rtabmap](https://index.ros.org/p/rtabmap_slam)
output topic `"mapData"` and assembles the 3D map incrementally,
then publishes the same maps than
[rtabmap](https://index.ros.org/p/rtabmap_slam). See all
**`'Mapping`**' related topics and parameters of
[rtabmap](https://index.ros.org/p/rtabmap_slam) node. You can also use
all `Grid` parameters from rtabmap:



```
$ rosrun rtabmap_slam rtabmap --params | grep Grid/
```



For example, setting the voxel sixe of the resulting grid/point cloud to
10 cm: 

```
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

This node is for **advanced usage only** as it is preferred to use graph
optimization already inside
[rtabmap](https://index.ros.org/p/rtabmap_slam) node (which is the
default). See related parameters in
[rtabmap](https://index.ros.org/p/rtabmap_slam):


```
$rosrun rtabmap_slam rtabmap --params | grep Optimize
```



This node subscribes to [rtabmap](https://index.ros.org/p/rtabmap_slam)
output topic `"mapData"` and optimize the graph, then republishes
the optimized `"mapData"`.

- This node can be used to optimize the graph outside
  [rtabmap](https://index.ros.org/p/rtabmap_slam) node. The benefice to
  do that is that we can keep optimized the global map instead of the
  local map of [rtabmap](https://index.ros.org/p/rtabmap_slam). You can
  then connect output `mapData_optimized` to
  [map_assembler](#map_assembler) to get the
  optimized grid, proj and cloud maps assembled again. **Note that
  processing time for map optimization using this node is not bounded**
  (which is the case in [rtabmap](https://index.ros.org/p/rtabmap_slam)
  node).

<!-- -->

- You could also use your own graph optimization approach instead of
  this node by modifying `poses` values of the
  [rtabmap_msgs/msg/MapData](https://docs.ros.org/en/rolling/p/rtabmap_msgs/msg/MapData.html)
  msg. However, implementing your graph optimization approach inside
  [rtabmap](https://index.ros.org/p/rtabmap_slam) is preferred (inherit
  [Optimizer](https://github.com/introlab/rtabmap/blob/463a5d973c3bab96382356dd763a98caf9beec34/corelib/include/rtabmap/core/Graph.h#L44-L109)
  class and add it
  [here](https://github.com/introlab/rtabmap/blob/463a5d973c3bab96382356dd763a98caf9beec34/corelib/src/Graph.cpp#L124-L137)
  with a new number, then you could select it after using the parameter
  `RGBD/OptimizeStrategy`).

<!-- -->

- When using graph optimization outside
  [rtabmap](https://index.ros.org/p/rtabmap_slam) node, you should set
  parameters `RGBD/OptimizeIterations` to `0`,
  `RGBD/OptimizeMaxError` to `0` and `publish_tf` to `false` for
  [rtabmap](https://index.ros.org/p/rtabmap_slam) node.

<!-- -->

- This node should not be used if
  [rtabmap](https://index.ros.org/p/rtabmap_slam) node is in
  localization mode.



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





```clearsilver
node {
  name = rtabmap_util/point_cloud_assembler
  desc = This nodelet can assemble a number of clouds (`max_clouds` or for a time `assembling_time`) coming from the same topic, taking into account the displacement of the robot based on `fixed_frame_id`, then publish the resulting cloud. If `fixed_frame_id` is set to `""` (empty), the nodelet will subscribe to an odom topic that should have the exact same stamp than to input cloud. The output cloud has the same stamp and frame than the last assembled cloud.
  sub {
    0.name = cloud
    0.type = sensor_msgs/PointCloud2
    0.desc = Point cloud topic to assemble.
    1.name = odom
    1.type = nav_msgs/Odometry
    1.desc = Odometry topic used to assembled clouds, when `fixed_frame_id` is not set. Assuming exact synchronization with input cloud.
    2.name = odom_info
    2.type = rtabmap_msgs/OdometryInfo
    2.desc = Used to assemble only keyframe scans from `icp_odometry`, when `subscribe_odom_info` is `true`. Assuming exact synchronization with input cloud.
  }
  pub {
    0.name = assembled_cloud
    0.type = sensor_msgs/PointCloud2
    0.desc = The assembled cloud.
  }
  param {
    0.name = ~queue_size
    0.type = int
    0.desc = Size of message queue for each synchronized topic.
    0.default = 10
    1.name = ~fixed_frame_id
    1.type = string
    1.desc = The fixed frame used to estimate displacement between assembled clouds. If not set, an odometry topic will be required.  
    1.default = "odom"
    2.name = ~frame_id
    2.type = string
    2.desc = Frame id of the output assembled cloud. If not set, same frame id as input cloud is used.
    2.default = `""`
    3.name = ~max_clouds
    3.type = int
    3.desc = The assembled cloud is published after reaching this number of input clouds received. `max_clouds` or `assembling_time` should be set.
    3.default = 0
    4.name = ~assembling_time
    4.type = double
    4.desc = The assembled cloud is published after the assembling time (seconds). `max_clouds` or `assembling_time` should be set.
    4.default = 0
    5.name = ~skip_clouds
    5.type = int
    5.desc = Number of input clouds to skip.
    5.default = 0
    6.name = ~circular_buffer
    6.type = bool
    6.desc = Instead of accumulating all the clouds before publishing the assembled cloud, the input clouds are kept in a circular buffer (of size `max_clouds` or a `assembling_time`) and the assebmled cloud is published every time a new scan is received. When `circular_buffer` is false, the temporary buffer to accumulate the clouds is cleared after each publishing.
    6.default = `"false"`
    7.name = ~linear_update
    7.type = double
    7.desc = If displacement between the last cloud and the new cloud received is under this value (meters), the new cloud is skipped. If `circular_buffer` is enabled, the assembled cloud is still published with the new cloud, but the new cloud is removed from the circular buffer instead of the oldest one. 0 means disabled.
    7.default = 0
    8.name = ~angular_update
    8.type = double
    8.desc = If rotation between the last cloud and the new cloud received is under this value (rad), the new cloud is skipped. If `circular_buffer` is enabled, the assembled cloud is still published with the new cloud, but the new cloud is removed from the circular buffer instead of the oldest one. 0 means disabled.
    8.default = 0
    9.name = ~wait_for_transform_duration
    9.type = double
    9.desc = Time to wait to get TF value between fixed frame and cloud frame at the stamp of the input cloud.
    9.default = 0.1
    10.name = ~range_min
    10.type = double
    10.desc = Filter input clouds with a minimum range. 0 means disabled.
    10.default = 0
    11.name = ~range_max
    11.type = double
    11.desc = Filter input clouds with a maximum range. 0 means disabled.
    11.default = 0
    12.name = ~voxel_size
    12.type = double
    12.desc = Apply voxel filter to output assembled cloud. 0 means disabled.
    12.default = 0
    13.name = ~noise_radius
    13.type = double
    13.desc = Apply radius outlier filter to output assembled cloud (meters). 0 means disabled.
    13.default = 0
    14.name = ~noise_min_neighbors
    14.type = int
    14.desc = Apply radius outlier filter to output assembled cloud (minimum number of neighbors of a point in `noise_radius` to keep it). 0 means disabled, `noise_radius` should also be set.
    14.default = 5
    15.name = ~remove_z
    15.type = bool
    15.desc = Remove z field from assembled cloud before publishing it to make it 2D. Useful if you are assembling laser scans created with [[laser_geometry]] scan to cloud (or [[https://github.com/tu-darmstadt-ros-pkg/hector_laserscan_to_pointcloud|hector_laserscan_to_pointcloud]]).
    15.default = `"false"`
  }
}
```





```clearsilver
node {
  name = rtabmap_util/point_cloud_aggregator
  desc = Nodelet used to merge point clouds from different sensors into a single assembled cloud. If `fixed_frame_id` is set and `approx_sync` is true, the clouds are adjusted to include the displacement of the robot in the output cloud.
  sub {
    0.name = cloud1
    0.type = sensor_msgs/PointCloud2
    0.desc = Point cloud topic to combine. This is the reference topic for output timestamp (and `frame_id` if not overridden by parameter).
    1.name = cloud2
    1.type = sensor_msgs/PointCloud2
    1.desc = Second point cloud topic to combine.
    2.name = cloud3
    2.type = sensor_msgs/PointCloud2
    2.desc = Third point cloud topic to combine. Optional, only if `count>=3`.
    3.name = cloud4
    3.type = sensor_msgs/PointCloud2
    3.desc = Second point cloud topic to combine. Optional, only if `count=4`.
  }
  pub {
    0.name = combined_cloud
    0.type = sensor_msgs/PointCloud2
    0.desc = The combined cloud.
  }
  param {
    0.name = ~queue_size
    0.type = int
    0.desc = Size of message queue for each synchronized topic.
    0.default = 10
    1.name = ~fixed_frame_id
    1.type = string
    1.desc = The fixed frame used to estimate displacement between combined clouds. Recommended if `approx_sync` is `true`.
    1.default = `""`
    2.name = ~frame_id
    2.type = string
    2.desc = Frame id of the output combined cloud. If not set, same frame id as input `cloud1` is used.
    2.default = `""`
    3.name = ~approx_sync
    3.type = bool
    3.desc = Use approximate time policy to synchronize input topics.
    3.default = `"true"`
    4.name = ~count
    4.type = int
    4.desc = Number of input topics to combine.
    4.default = 2
    5.name = ~wait_for_transform_duration
    5.type = double
    5.desc = Time to wait to get TF value between fixed frame and cloud frame at the stamp of the input cloud.
    5.default = 0.1
  }
}
```





```clearsilver
node {
  name = rtabmap_util/imu_to_tf
  desc = Nodelet used to convert orientation set in a [[http://docs.ros.org/en/noetic/api/sensor_msgs/html/msg/Imu.html|sensor_msgs/IMU]] msg into a TF in a target frame (that may be or not the frame of the IMU msg). For example, the resulting TF could be used as fixed or guess frame for [[rtabmap_util#rtabmap_util.2Flidar_deskewing|lidar deskewing]] or [[rtabmap_odom]] respectively.
  sub {
    0.name = imu/data
    0.type = sensor_msgs/IMU
    0.desc = The IMU topic to get orientation from. The orientation should be already estimated. If not, you may use an IMU filter package to estimate the orientation (e.g., [[imu_filter_madgwick]] or [[imu_complementary_filter]]).
  }
  param {
    0.name = ~fixed_frame_id
    0.type = string
    0.desc = Parent frame of the output tf.
    0.default = "odom"
    1.name = ~base_frame_id
    1.type = string
    1.desc = The target child frame of the output tf (e.g., `base_link`). IMU orientation will be transformed to estimate orientation of that frame (not the IMU frame). If not set, frame inside IMU topic is used.
    1.default = `""`
    2.name = ~wait_for_transform_duration
    2.type = double
    2.desc = Time to wait to get TF value between `base_frame_id` and the IMU frame at the stamp of the IMU.
    2.default = 0.1
  }
  req_tf {
    0{
     from = base_frame_id
     to = <the frame attached to sensors of incoming data>
     desc = usually a fixed value, broadcast periodically by a [[robot_state_publisher]], or a `tf` [[tf#static_transform_publisher|static_transform_publisher]].
     }
  }
  prov_tf {
    0.from = fixed_frame_id
    0.to = base_frame_id
    0.desc = the resulting tf representing the IMU orientation.
  }
}
```



### rtabmap_util/obstacles_detection

This nodelet extracts obstacles and the ground from a point cloud. The
camera must see the ground to work reliably. Since the ground is not
even, the ground is segmented by normal filtering: all points with
normal in the +z direction (+- fixed angle) are labelled as ground, all
the others are labelled as obstacles. The images below show an example.

**Warning**: this node will use a lot of CPU ressources if the raw point
clouds are fed to it directly. A
[pcl::VoxelGrid](http://wiki.ros.org/pcl_ros/Tutorials/VoxelGrid%20filtering)
can be used to downsample the raw point cloud (e.g. like 5 cm voxel) or
rtabmap_util/point_cloud_xyz
nodelet can be used to generate a downsampled cloud from a depth image
(e.g. decimating the depth image by 4 before creating a cloud). That
filtered point cloud would be fed to `obstacles_detection`.

  -- ----------------------- -- ----------------------- --
     ![obs1](doc/obs1.png)      ![obs2](doc/obs2.png)   
     ![obs0](doc/obs0.png)      ![obs4](doc/obs4.png)   
  -- ----------------------- -- ----------------------- --



```clearsilver
sub {
  0.name = cloud
  0.type = sensor_msgs/PointCloud2
  0.desc = A point cloud generated from a RGB-D camera or a stereo camera.
}

pub {
  0.name = ground
  0.type = sensor_msgs/PointCloud2
  0.desc = The segmented ground.
  1.name = obstacles
  1.type = sensor_msgs/PointCloud2
  1.desc = The segmented obstacles.
}

param {
  0.name = ~frame_id
  0.type = string
  0.default = `"base_link"`
  0.desc = The frame attached to the mobile base.
  1.name = ~queue_size
  1.type = int
  1.default = 10
  1.desc = Size of message queue for each synchronized topic.
  2.name = ~normal_estimation_radius
  2.type = double
  2.default = 0.05
  2.desc = Normal estimation radius (m).
  3.name = ~ground_normal_angle
  3.type = double
  3.default = PI/4
  3.desc = Maximum angle from the +z axis of the point's normal to be labelled as ground.
  4.name = ~min_cluster_size
  4.type = int
  4.default = 20
  4.desc = Minimum size of the segmented clusters to keep.
  5.name = ~max_obstacles_height
  5.type = double
  5.default = 0.0
  5.desc = Maximum height of obstacles.
}

req_tf {
  0.from = base_link
  0.to = <the frame attached to sensors of incoming data>
  0.desc = usually a fixed value, broadcast periodically by a [[robot_state_publisher]], or a `tf` [[tf#static_transform_publisher|static_transform_publisher]].
}
```



### rtabmap_util/lidar_deskewing

For
[sensor_msgs/PointCloud2](http://docs.ros.org/en/noetic/api/sensor_msgs/html/msg/PointCloud2.html)
`input_cloud` (3D LiDAR), each point will be deskewed based on their
timestamp during the rotation of the LiDAR using `fixed_frame_id`
fixed frame. The `input_cloud` topic should have timestamp channel as
`t`, `time` or `stamps`. Supported timestamp formats are FLOAT32
(seconds since header's timestamp) and UINT32 (nanoseconds since
header's timestamp). If `input_cloud` is organized, deskewing will be
faster (transformed per columns instead per points). For
[sensor_msgs/LaserScan](http://docs.ros.org/en/noetic/api/sensor_msgs/html/msg/LaserScan.html)
`input_scan` (2D LiDAR),
[laser_geometry::LaserProjection](https://docs.ros.org/en/noetic/api/laser_geometry/html/classlaser__geometry_1_1LaserProjection.html)
class is used directly to project the scan while accounting for robot
motion.



```clearsilver
sub {
  0.name = input_scan
  0.type = sensor_msgs/LaserScan
  0.desc = A laser scan (2D LiDAR). Use either `input_scan` or `input_cloud`.
}
sub {
  1.name = input_cloud
  1.type = sensor_msgs/PointCloud2
  1.desc = A point cloud generated from one rotation of a 3D LiDAR. Use either `input_scan` or `input_cloud`.
}

pub {
  0.name = [input_scan]/deskewed
  0.type = sensor_msgs/PointCloud2
  0.desc = The deskewed laser scan converted to a point cloud. Output frame is the same than the frame of the input topic.
  1.name = [input_cloud]/deskewed
  1.type = sensor_msgs/PointCloud2
  1.desc = The deskewed point cloud. Output frame is the same than the frame of the input topic.
}

param {
  0.name = ~fixed_frame_id
  0.type = string
  0.default = `""`
  0.desc = The fixed frame used for deskewing (e.g., `"odom"`).
  1.name = ~wait_for_transform
  1.type = double
  1.default = 0.01
  1.desc = How much time to wait for TF to be ready.
  2.name = ~slerp
  2.type = bool
  2.default = false
  2.desc = When enable, a lookup transform for TF will only be done for the first and last stamp, then points with in between timestamps will be deskewed by interpolating between the oldest and latest poses. This can be faster than the default approach looking for transform for very timestamps (though later approach would be more accurate). 
}

req_tf {
  0.from = fixed_frame_id
  0.to = <the frame attached to sensors of incoming data>
  0.desc = high frame rate (faster than LiDAR rate) and locally accurate transform, e.g., IMU TF or odometry TF.
}
```
