

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



#### Subscribed Topics

- `mapData`
  ([rtabmap_msgs/msg/MapData](https://docs.ros.org/en/rolling/p/rtabmap_msgs/msg/MapData.html)):
  RTAB-Map's graph and latest node data.

#### Services

- `~reset`
  ([std_srvs/srv/Empty](https://docs.ros.org/en/rolling/p/std_srvs/srv/Empty.html)):
  Reset the cache.

#### Parameters

- `~regenerate_local_grids` (`bool`, default: `"false"`):
  (>=0.20.5) If local occupancy grids are already included in
  `mapData`, set this to `true` to regenerate them. For example,
  this can be used to generate the local occupancy grids with a
  different sensor (e.g., `Grid/FromDepth` is different than one used
  in `rtabmap`).

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

#### Subscribed Topics

- `mapData`
  ([rtabmap_msgs/msg/MapData](https://docs.ros.org/en/rolling/p/rtabmap_msgs/msg/MapData.html)):
  RTAB-Map's graph and latest node data.

#### Published Topics

- `[mapData]_optimized`
  ([rtabmap_msgs/msg/MapData](https://docs.ros.org/en/rolling/p/rtabmap_msgs/msg/MapData.html)):
  RTAB-Map's optimized graph and latest node data.
- `[mapData]Graph_optimized`
  ([rtabmap_msgs/msg/MapGraph](https://docs.ros.org/en/rolling/p/rtabmap_msgs/msg/MapGraph.html)):
  RTAB-Map's optimized graph.

#### Parameters

- `~map_frame_id` (`string`, default: `"map"`): The frame attached
  to the map.
- `~odom_frame_id` (`string`, default: `"odom"`): The frame attached
  to odometry.
- `~strategy` (`int`, default: `0`): Optimization approach used: 0=TORO,
  1=g2o and 2=GTSAM.
- `~slam_2d` (`bool`, default: `"false"`): 3DoF (x,y,yaw)
  optimization instead of 6DoF (x,y,z,roll,pitch,yaw).
- `~robust` (`bool`, default: `"true"`): Activate Vertigo robust
  graph optimization when g2o or GTSAM `strategy` is used.
- `~global_optimization` (`bool`, default: `"true"`): Optimize the
  global map. If false, only the local map is optimized.
- `~iterations` (`int`, default: `100`): Map optimization iterations.
- `~epsilon` (`double`, default: `0.0`): Stop graph optimization when
  error is less than `epsilon` (0=ignore epsilon).
- `~ignore_variance` (`bool`, default: `"false"`): Ignore
  constraints' variance. If checked, identity information matrix is
  used for each constraint in TORO. Otherwise, an information matrix is
  generated from the variance saved in the links.
- `~optimize_from_last_node` (`bool`, default: `"false"`): Optimize
  from the last node. If false, the graph is optimized from the oldest
  node linked to the current map.
- `~publish_tf` (`bool`, default: `"true"`): Publish TF from /map to
  /odom.
- `~tf_delay` (`double`, default: `0.05`): Rate at which the TF from
  /map to /odom is published (20 Hz).

## Nodelets

### rtabmap_util/rgbd_relay

A relay for
[rtabmap_msgs/RGBDImage](http://docs.ros.org/api/rtabmap_msgs/html/msg/RGBDImage.html)
messages. It works like a
[topic_tools/relay](http://wiki.ros.org/topic_tools/relay), but can also
compress or uncompress data for convenience.

#### Subscribed Topics

- `rgbd_image`
  ([rtabmap_msgs/msg/RGBDImage](https://docs.ros.org/en/rolling/p/rtabmap_msgs/msg/RGBDImage.html)):
  RGB-D image input stream.

#### Published Topics

- `[rgbd_image]_relay`
  ([rtabmap_msgs/msg/RGBDImage](https://docs.ros.org/en/rolling/p/rtabmap_msgs/msg/RGBDImage.html)):
  RGB-D image output stream.

#### Parameters

- `~queue_size` (`int`, default: `10`): Size of message queue.
- `~compress` (`bool`, default: `"False"`): Publish compressed RGB-D
  image data.
- `~uncompress` (`bool`, default: `"False"`): Publish uncompressed
  RGB-D image data.

### rtabmap_util/point_cloud_xyzrgb

Construct a point cloud from RGB and depth images or stereo images.
Optional decimation, depth, voxel and noise filtering can be applied.

#### Subscribed Topics

- `rgb/image`
  ([sensor_msgs/msg/Image](https://docs.ros.org/en/rolling/p/sensor_msgs/msg/Image.html)):
  RGB image stream.
- `depth/image`
  ([sensor_msgs/msg/Image](https://docs.ros.org/en/rolling/p/sensor_msgs/msg/Image.html)):
  Registered depth image stream.
- `rgb/camera_info`
  ([sensor_msgs/msg/CameraInfo](https://docs.ros.org/en/rolling/p/sensor_msgs/msg/CameraInfo.html)):
  RGB camera metadata.
- `left/image`
  ([sensor_msgs/msg/Image](https://docs.ros.org/en/rolling/p/sensor_msgs/msg/Image.html)):
  Left RGB/Mono rectified image.
- `left/camera_info`
  ([sensor_msgs/msg/CameraInfo](https://docs.ros.org/en/rolling/p/sensor_msgs/msg/CameraInfo.html)):
  Left camera metadata.
- `right/image`
  ([sensor_msgs/msg/Image](https://docs.ros.org/en/rolling/p/sensor_msgs/msg/Image.html)):
  Right Mono rectified image.
- `right/camera_info`
  ([sensor_msgs/msg/CameraInfo](https://docs.ros.org/en/rolling/p/sensor_msgs/msg/CameraInfo.html)):
  Right camera metadata.

#### Published Topics

- `cloud`
  ([sensor_msgs/msg/PointCloud2](https://docs.ros.org/en/rolling/p/sensor_msgs/msg/PointCloud2.html)):
  Generated RGB point cloud.

#### Parameters

- `~queue_size` (`int`, default: `10`): Size of message queue for each
  synchronized topic.
- `~approx_sync` (`bool`, default: `"true"`): Use approximate time
  synchronization of the input topics. If false, the input topics must
  have the same timestamp (set to `"false"` for stereo images).
- `~decimation` (`int`, default: `1`): Decimation of the images before
  creating the point cloud. Set to 1 to not decimate the images.
- `~voxel_size` (`double`, default: `0.0`): Voxel size (m) of the
  generated cloud. Set `0.0` to deactivate voxel filtering.
- `~min_depth` (`double`, default: `0.0`): Min depth (m) of the
  generated cloud.
- `~max_depth` (`double`, default: `0.0`): Max depth (m) of the
  generated cloud. Set `0.0` to deactivate depth filtering.
- `~noise_filter_radius` (`double`, default: `0.0`): Max radius (m) for
  searching point neighbors. Set `0.0` to deactivate noise filtering.
- `~noise_filter_min_neighbors` (`int`, default: `5`): Minimum neighbors
  of a point to keep it.
- `~normal_k` (`int`, default: `0`): Compute normals using k nearest
  neighbors (0=disabled).
- `~normal_radius` (`double`, default: `0.0`): Compute normals using
  nearest neighbors inside the radius (m) (0=disabled).
- `~filter_nans` (`bool`, default: `"false"`): Remove NaNs points
  from output cloud (convert organized to dense point cloud)
- `~roi_ratios` (`string`, default: `"0.0 0.0 0.0 0.0"`): Region of
  interest ratios \[left, right, top, bottom\] (e.g., `"0 0 0 0.2"`
  will cut 20% of the bottom of the image).

### rtabmap_util/point_cloud_xyz

Construct a point cloud from a depth or disparity image. Optional
decimation, depth, voxel and noise filtering can be applied.

#### Subscribed Topics

- `depth/image`
  ([sensor_msgs/msg/Image](https://docs.ros.org/en/rolling/p/sensor_msgs/msg/Image.html)):
  Depth image stream.
- `depth/camera_info`
  ([sensor_msgs/msg/CameraInfo](https://docs.ros.org/en/rolling/p/sensor_msgs/msg/CameraInfo.html)):
  Depth camera metadata.
- `disparity/image`
  ([stereo_msgs/msg/DisparityImage](https://docs.ros.org/en/rolling/p/stereo_msgs/msg/DisparityImage.html)):
  Disparity image stream.
- `disparity/camera_info`
  ([sensor_msgs/msg/CameraInfo](https://docs.ros.org/en/rolling/p/sensor_msgs/msg/CameraInfo.html)):
  Disparity camera metadata.

#### Published Topics

- `cloud`
  ([sensor_msgs/msg/PointCloud2](https://docs.ros.org/en/rolling/p/sensor_msgs/msg/PointCloud2.html)):
  Generated point cloud.

#### Parameters

- `~queue_size` (`int`, default: `10`): Size of message queue for each
  synchronized topic.
- `~approx_sync` (`bool`, default: `"true"`): Use approximate time
  synchronization of messages. If false, the image and camera info must
  have the same timestamps.
- `~decimation` (`int`, default: `1`): Decimation of the RGB/depth
  images before creating the point cloud. Set to 1 to not decimate the
  images.
- `~voxel_size` (`double`, default: `0.0`): Voxel size (m) of the
  generated cloud. Set `0.0` to deactivate voxel filtering.
- `~min_depth` (`double`, default: `0.0`): Min depth (m) of the
  generated cloud.
- `~max_depth` (`double`, default: `0.0`): Max depth (m) of the
  generated cloud. Set `0.0` to deactivate depth filtering.
- `~noise_filter_radius` (`double`, default: `0.0`): Max radius (m) for
  searching point neighbors. Set `0.0` to deactivate noise filtering.
- `~noise_filter_min_neighbors` (`int`, default: `5`): Minimum neighbors
  of a point to keep it.
- `~normal_k` (`int`, default: `0`): Compute normals using k nearest
  neighbors (0=disabled).
- `~normal_radius` (`double`, default: `0.0`): Compute normals using
  nearest neighbors inside the radius (m) (0=disabled).
- `~filter_nans` (`bool`, default: `"false"`): Remove NaNs points
  from output cloud (convert organized to dense point cloud)
- `~roi_ratios` (`string`, default: `"0.0 0.0 0.0 0.0"`): Region of
  interest ratios \[left, right, top, bottom\] (e.g., `"0 0 0 0.2"`
  will cut 20% of the bottom of the image).

### rtabmap_util/disparity_to_depth

Convert a disparity image to a depth image.

#### Subscribed Topics

- `disparity`
  ([stereo_msgs/msg/DisparityImage](https://docs.ros.org/en/rolling/p/stereo_msgs/msg/DisparityImage.html)):
  Disparity image stream.

#### Published Topics

- `depth`
  ([sensor_msgs/msg/Image](https://docs.ros.org/en/rolling/p/sensor_msgs/msg/Image.html)):
  Depth image stream in m. Format TYPE_32FC1.
- `depth_raw`
  ([sensor_msgs/msg/Image](https://docs.ros.org/en/rolling/p/sensor_msgs/msg/Image.html)):
  Depth image stream in mm. Format TYPE_16UC1.

### rtabmap_util/pointcloud_to_depthimage

Reproject a point cloud into a camera frame to create a depth image.
When `fixed_frame_id` is set (e.g., "odom"), movement is taken into
account by transforming the point cloud accordingly to camera timestamp.
An example of usage of this nodelet can be found in the
[Tango ROS Streamer](http://wiki.ros.org/rtabmap_ros/Tutorials/Tango%20ROS%20Streamer)
tutorial.

#### Subscribed Topics

- `camera_info`
  ([stereo_msgs/msg/CameraInfo](https://docs.ros.org/en/rolling/p/stereo_msgs/msg/CameraInfo.html)):
  Camera info in which we want to reproject the points.
- `cloud`
  ([sensor_msgs/msg/PointCloud2](https://docs.ros.org/en/rolling/p/sensor_msgs/msg/PointCloud2.html)):
  The cloud to reproject in the camera.

#### Published Topics

- `image`
  ([sensor_msgs/msg/Image](https://docs.ros.org/en/rolling/p/sensor_msgs/msg/Image.html)):
  Depth image stream in m. Format TYPE_32FC1.
- `image_raw`
  ([sensor_msgs/msg/Image](https://docs.ros.org/en/rolling/p/sensor_msgs/msg/Image.html)):
  Depth image stream in mm. Format TYPE_16UC1.

#### Parameters

- `~queue_size` (`int`, default: `10`): Size of message queue for each
  synchronized topic.
- `~fixed_frame_id` (`string`, default: `""`): This frame should be set
  when using approximate time synchronization (`approx` is `true`).
  If the robot is moving, it could be "odom". If not moving, it could
  be "base_link".
- `~approx` (`bool`, default: `"true"`): Approximate time
  synchronization.
- `~wait_for_transform` (`double`, default: `0.1`): Wait duration for
  transform when a [tf](https://index.ros.org/p/tf) transform is not
  still available.
- `~decimation` (`int`, default: `1`): Scale down image size of the
  camera info received (creating smaller depth image).
- `~fill_holes_size` (`int`, default: `0`): Fill holes of empty pixels
  up to this size. Values are interpolated from neighbor depth values. 0
  means disabled.
- `~fill_holes_error` (`double`, default: `0.1`): Maximum depth
  error (m) to interpolate.
- `~fill_iterations` (`int`, default: `1`): Number of iterations to fill
  holes.

### rtabmap_util/point_cloud_assembler

This nodelet can assemble a number of clouds (`max_clouds` or for a
time `assembling_time`) coming from the same topic, taking into
account the displacement of the robot based on `fixed_frame_id`, then
publish the resulting cloud. If `fixed_frame_id` is set to `""`
(empty), the nodelet will subscribe to an odom topic that should have
the exact same stamp than to input cloud. The output cloud has the same
stamp and frame than the last assembled cloud.

#### Subscribed Topics

- `cloud`
  ([sensor_msgs/msg/PointCloud2](https://docs.ros.org/en/rolling/p/sensor_msgs/msg/PointCloud2.html)):
  Point cloud topic to assemble.
- `odom`
  ([nav_msgs/msg/Odometry](https://docs.ros.org/en/rolling/p/nav_msgs/msg/Odometry.html)):
  Odometry topic used to assembled clouds, when `fixed_frame_id` is
  not set. Assuming exact synchronization with input cloud.
- `odom_info`
  ([rtabmap_msgs/msg/OdometryInfo](https://docs.ros.org/en/rolling/p/rtabmap_msgs/msg/OdometryInfo.html)):
  Used to assemble only keyframe scans from `icp_odometry`, when
  `subscribe_odom_info` is `true`. Assuming exact synchronization
  with input cloud.

#### Published Topics

- `assembled_cloud`
  ([sensor_msgs/msg/PointCloud2](https://docs.ros.org/en/rolling/p/sensor_msgs/msg/PointCloud2.html)):
  The assembled cloud.

#### Parameters

- `~queue_size` (`int`, default: `10`): Size of message queue for each
  synchronized topic.
- `~fixed_frame_id` (`string`, default: `"odom"`): The fixed frame used
  to estimate displacement between assembled clouds. If not set, an
  odometry topic will be required.
- `~frame_id` (`string`, default: `""`): Frame id of the output
  assembled cloud. If not set, same frame id as input cloud is used.
- `~max_clouds` (`int`, default: `0`): The assembled cloud is published
  after reaching this number of input clouds received. `max_clouds` or
  `assembling_time` should be set.
- `~assembling_time` (`double`, default: `0`): The assembled cloud is
  published after the assembling time (seconds). `max_clouds` or
  `assembling_time` should be set.
- `~skip_clouds` (`int`, default: `0`): Number of input clouds to skip.
- `~circular_buffer` (`bool`, default: `"false"`): Instead of
  accumulating all the clouds before publishing the assembled cloud, the
  input clouds are kept in a circular buffer (of size `max_clouds` or
  a `assembling_time`) and the assebmled cloud is published every time
  a new scan is received. When `circular_buffer` is false, the
  temporary buffer to accumulate the clouds is cleared after each
  publishing.
- `~linear_update` (`double`, default: `0`): If displacement between the
  last cloud and the new cloud received is under this value (meters),
  the new cloud is skipped. If `circular_buffer` is enabled, the
  assembled cloud is still published with the new cloud, but the new
  cloud is removed from the circular buffer instead of the oldest one. 0
  means disabled.
- `~angular_update` (`double`, default: `0`): If rotation between the
  last cloud and the new cloud received is under this value (rad), the
  new cloud is skipped. If `circular_buffer` is enabled, the assembled
  cloud is still published with the new cloud, but the new cloud is
  removed from the circular buffer instead of the oldest one. 0 means
  disabled.
- `~wait_for_transform_duration` (`double`, default: `0.1`): Time to
  wait to get TF value between fixed frame and cloud frame at the stamp
  of the input cloud.
- `~range_min` (`double`, default: `0`): Filter input clouds with a
  minimum range. 0 means disabled.
- `~range_max` (`double`, default: `0`): Filter input clouds with a
  maximum range. 0 means disabled.
- `~voxel_size` (`double`, default: `0`): Apply voxel filter to output
  assembled cloud. 0 means disabled.
- `~noise_radius` (`double`, default: `0`): Apply radius outlier filter
  to output assembled cloud (meters). 0 means disabled.
- `~noise_min_neighbors` (`int`, default: `5`): Apply radius outlier
  filter to output assembled cloud (minimum number of neighbors of a
  point in `noise_radius` to keep it). 0 means disabled,
  `noise_radius` should also be set.
- `~remove_z` (`bool`, default: `"false"`): Remove z field from
  assembled cloud before publishing it to make it 2D. Useful if you are
  assembling laser scans created with
  [laser_geometry](https://index.ros.org/p/laser_geometry) scan to cloud
  (or
  [hector_laserscan_to_pointcloud](https://github.com/tu-darmstadt-ros-pkg/hector_laserscan_to_pointcloud)).

### rtabmap_util/point_cloud_aggregator

Nodelet used to merge point clouds from different sensors into a single
assembled cloud. If `fixed_frame_id` is set and `approx_sync` is
true, the clouds are adjusted to include the displacement of the robot
in the output cloud.

#### Subscribed Topics

- `cloud1`
  ([sensor_msgs/msg/PointCloud2](https://docs.ros.org/en/rolling/p/sensor_msgs/msg/PointCloud2.html)):
  Point cloud topic to combine. This is the reference topic for output
  timestamp (and `frame_id` if not overridden by parameter).
- `cloud2`
  ([sensor_msgs/msg/PointCloud2](https://docs.ros.org/en/rolling/p/sensor_msgs/msg/PointCloud2.html)):
  Second point cloud topic to combine.
- `cloud3`
  ([sensor_msgs/msg/PointCloud2](https://docs.ros.org/en/rolling/p/sensor_msgs/msg/PointCloud2.html)):
  Third point cloud topic to combine. Optional, only if `count>=3`.
- `cloud4`
  ([sensor_msgs/msg/PointCloud2](https://docs.ros.org/en/rolling/p/sensor_msgs/msg/PointCloud2.html)):
  Second point cloud topic to combine. Optional, only if `count=4`.

#### Published Topics

- `combined_cloud`
  ([sensor_msgs/msg/PointCloud2](https://docs.ros.org/en/rolling/p/sensor_msgs/msg/PointCloud2.html)):
  The combined cloud.

#### Parameters

- `~queue_size` (`int`, default: `10`): Size of message queue for each
  synchronized topic.
- `~fixed_frame_id` (`string`, default: `""`): The fixed frame used
  to estimate displacement between combined clouds. Recommended if
  `approx_sync` is `true`.
- `~frame_id` (`string`, default: `""`): Frame id of the output
  combined cloud. If not set, same frame id as input `cloud1` is used.
- `~approx_sync` (`bool`, default: `"true"`): Use approximate time
  policy to synchronize input topics.
- `~count` (`int`, default: `2`): Number of input topics to combine.
- `~wait_for_transform_duration` (`double`, default: `0.1`): Time to
  wait to get TF value between fixed frame and cloud frame at the stamp
  of the input cloud.

### rtabmap_util/imu_to_tf

Nodelet used to convert orientation set in a
[sensor_msgs/IMU](http://docs.ros.org/en/noetic/api/sensor_msgs/html/msg/Imu.html)
msg into a TF in a target frame (that may be or not the frame of the IMU
msg). For example, the resulting TF could be used as fixed or guess
frame for
[lidar deskewing](#rtabmap_utillidar_deskewing)
or [rtabmap_odom](https://index.ros.org/p/rtabmap_odom) respectively.

#### Subscribed Topics

- `imu/data`
  ([sensor_msgs/msg/IMU](https://docs.ros.org/en/rolling/p/sensor_msgs/msg/IMU.html)):
  The IMU topic to get orientation from. The orientation should be
  already estimated. If not, you may use an IMU filter package to
  estimate the orientation (e.g.,
  [imu_filter_madgwick](https://index.ros.org/p/imu_filter_madgwick) or
  [imu_complementary_filter](https://index.ros.org/p/imu_complementary_filter)).

#### Parameters

- `~fixed_frame_id` (`string`, default: `"odom"`): Parent frame of the
  output tf.
- `~base_frame_id` (`string`, default: `""`): The target child frame
  of the output tf (e.g., `base_link`). IMU orientation will be
  transformed to estimate orientation of that frame (not the IMU frame).
  If not set, frame inside IMU topic is used.
- `~wait_for_transform_duration` (`double`, default: `0.1`): Time to
  wait to get TF value between `base_frame_id` and the IMU frame at
  the stamp of the IMU.

#### Required tf Transforms

- `base_frame_id` → `<the frame attached to sensors of incoming data>`:
  usually a fixed value, broadcast periodically by a
  [robot_state_publisher](https://index.ros.org/p/robot_state_publisher),
  or a `tf` [static_transform_publisher](https://index.ros.org/p/tf).

#### Provided tf Transforms

- `fixed_frame_id` → `base_frame_id`: the resulting tf representing the
  IMU orientation.

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
[rtabmap_util/point_cloud_xyz](#rtabmap_utilpoint_cloud_xyz)
nodelet can be used to generate a downsampled cloud from a depth image
(e.g. decimating the depth image by 4 before creating a cloud). That
filtered point cloud would be fed to `obstacles_detection`.

  -- ----------------------- -- ----------------------- --
     ![obs1](doc/obs1.png)      ![obs2](doc/obs2.png)   
     ![obs0](doc/obs0.png)      ![obs4](doc/obs4.png)   
  -- ----------------------- -- ----------------------- --

#### Subscribed Topics

- `cloud`
  ([sensor_msgs/msg/PointCloud2](https://docs.ros.org/en/rolling/p/sensor_msgs/msg/PointCloud2.html)):
  A point cloud generated from a RGB-D camera or a stereo camera.

#### Published Topics

- `ground`
  ([sensor_msgs/msg/PointCloud2](https://docs.ros.org/en/rolling/p/sensor_msgs/msg/PointCloud2.html)):
  The segmented ground.
- `obstacles`
  ([sensor_msgs/msg/PointCloud2](https://docs.ros.org/en/rolling/p/sensor_msgs/msg/PointCloud2.html)):
  The segmented obstacles.

#### Parameters

- `~frame_id` (`string`, default: `"base_link"`): The frame attached
  to the mobile base.
- `~queue_size` (`int`, default: `10`): Size of message queue for each
  synchronized topic.
- `~normal_estimation_radius` (`double`, default: `0.05`): Normal
  estimation radius (m).
- `~ground_normal_angle` (`double`, default: `PI/4`): Maximum angle from
  the +z axis of the point's normal to be labelled as ground.
- `~min_cluster_size` (`int`, default: `20`): Minimum size of the
  segmented clusters to keep.
- `~max_obstacles_height` (`double`, default: `0.0`): Maximum height of
  obstacles.

#### Required tf Transforms

- `base_link` → `<the frame attached to sensors of incoming data>`:
  usually a fixed value, broadcast periodically by a
  [robot_state_publisher](https://index.ros.org/p/robot_state_publisher),
  or a `tf` [static_transform_publisher](https://index.ros.org/p/tf).

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

#### Subscribed Topics

- `input_scan`
  ([sensor_msgs/msg/LaserScan](https://docs.ros.org/en/rolling/p/sensor_msgs/msg/LaserScan.html)):
  A laser scan (2D LiDAR). Use either `input_scan` or `input_cloud`.
- `input_cloud`
  ([sensor_msgs/msg/PointCloud2](https://docs.ros.org/en/rolling/p/sensor_msgs/msg/PointCloud2.html)):
  A point cloud generated from one rotation of a 3D LiDAR. Use either
  `input_scan` or `input_cloud`.

#### Published Topics

- `[input_scan]/deskewed`
  ([sensor_msgs/msg/PointCloud2](https://docs.ros.org/en/rolling/p/sensor_msgs/msg/PointCloud2.html)):
  The deskewed laser scan converted to a point cloud. Output frame is
  the same than the frame of the input topic.
- `[input_cloud]/deskewed`
  ([sensor_msgs/msg/PointCloud2](https://docs.ros.org/en/rolling/p/sensor_msgs/msg/PointCloud2.html)):
  The deskewed point cloud. Output frame is the same than the frame of
  the input topic.

#### Parameters

- `~fixed_frame_id` (`string`, default: `""`): The fixed frame used
  for deskewing (e.g., `"odom"`).
- `~wait_for_transform` (`double`, default: `0.01`): How much time to
  wait for TF to be ready.
- `~slerp` (`bool`, default: `false`): When enable, a lookup transform
  for TF will only be done for the first and last stamp, then points
  with in between timestamps will be deskewed by interpolating between
  the oldest and latest poses. This can be faster than the default
  approach looking for transform for very timestamps (though later
  approach would be more accurate).

#### Required tf Transforms

- `fixed_frame_id` → `<the frame attached to sensors of incoming data>`:
  high frame rate (faster than LiDAR rate) and locally accurate
  transform, e.g., IMU TF or odometry TF.
