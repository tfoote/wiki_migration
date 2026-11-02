

```wiki
'''''[[rtabmap_ros]]:''' [[rtabmap]] | [[rtabmap_conversions]] | [[rtabmap_costmap_plugins]] | [[rtabmap_demos]] | [[rtabmap_examples]] | [[rtabmap_launch]] | [[rtabmap_legacy]] | [[rtabmap_msgs]] | [[rtabmap_odom]] | [[rtabmap_python]] | [[rtabmap_rviz_plugins]] | [[rtabmap_slam]] | [[rtabmap_sync]] | [[rtabmap_util]] | [[rtabmap_viz]]''
```



## Nodes

### rtabmap

This is the main node of this package. It is a wrapper of the RTAB-Map
Core library. This is where the graph of the map is incrementally built
and optimized when a loop closure is detected. The online output of the
node is the local graph with the latest added data to the map. The
default location of the RTAB-Map database is "/.ros/rtabmap.db" and
the workspace is also set to "/.ros". To get a 3D point cloud or a 2D
occupancy grid of the environment, subscribe to `cloud_map` or
`grid_map` topics.

- There are two set of parameters: ROS and RTAB-Map's parameters. The
  ROS parameters are for connection stuff to interface the RTAB-Map
  library with ROS. The RTAB-Map's parameters are those from the
  RTAB-Map library.

<!-- -->

- One way to know RTAB-Map's parameters is to look at this file :
  [Parameters.h](https://github.com/introlab/rtabmap/blob/master/corelib/include/rtabmap/core/Parameters.h#L161).
  There is a description for each parameter. Here two examples (use
  string type for all RTAB-Map's parameters) by either using `param`
  member or by passing as arguments: 

```
<launch>
<node name="rtabmap" pkg="rtabmap_slam" type="rtabmap" args="--Grid/RangeMax 5">
   <param name="Optimizer/Iterations" type="int" value="50"/>
</node>
</launch>
```



<!-- -->

- Another way to show available parameters from the terminal is to call
  the node with "\--params" argument: 

```
$ rosrun rtabmap_slam rtabmap --params
or
$ rtabmap --params
```



<!-- -->

- By default, rtabmap is in mapping mode. To set in localization mode
  with a previously created map, you should set the memory not
  incremental (make sure that arguments don't contain
  `"\--delete_db_on_start"` too!): 

```
<launch>
<node name="rtabmap" pkg="rtabmap_slam" type="rtabmap" args="">
   <!-- LOCALIZATION MODE -->
   <param name="Mem/IncrementalMemory" type="string" value="false"/>
</node>
</launch>
```



#### Arguments

- `"\--delete_db_on_start"` or `"-d"`: Delete the database
  before starting, otherwise the previous mapping session is loaded.
- `"\--udebug"`: Show RTAB-Map's debug/info/warning/error logs.
- `"\--uinfo"`: Show RTAB-Map's info/warning/error logs.
- `"\--params"`: Show RTAB-Map's parameters related to this node
  and exit.

#### Subscribed Topics

- `odom`
  ([nav_msgs/msg/Odometry](https://docs.ros.org/en/rolling/p/nav_msgs/msg/Odometry.html)):
  Odometry stream. Required if parameters `subscribe_depth` or
  `subscribe_stereo` are true **and** `odom_frame_id` is not set.
- `rgb/image`
  ([sensor_msgs/msg/Image](https://docs.ros.org/en/rolling/p/sensor_msgs/msg/Image.html)):
  RGB/Mono image. Should be rectified when `subscribe_depth` is true.
  Not required if parameter `subscribe_stereo` is true (use
  `left/image_rect` instead).
- `rgb/camera_info`
  ([sensor_msgs/msg/CameraInfo](https://docs.ros.org/en/rolling/p/sensor_msgs/msg/CameraInfo.html)):
  RGB camera metadata. Not required if parameter `subscribe_stereo` is
  true (use `left/camera_info` instead).
- `depth/image`
  ([sensor_msgs/msg/Image](https://docs.ros.org/en/rolling/p/sensor_msgs/msg/Image.html)):
  Registered depth image. Required if parameter `subscribe_depth` is
  true.
- `scan`
  ([sensor_msgs/msg/LaserScan](https://docs.ros.org/en/rolling/p/sensor_msgs/msg/LaserScan.html)):
  Laser scan stream. Required if parameter `subscribe_scan` is true.
- `scan_cloud`
  ([sensor_msgs/msg/PointCloud2](https://docs.ros.org/en/rolling/p/sensor_msgs/msg/PointCloud2.html)):
  Laser scan point cloud stream. Required if parameter
  `subscribe_scan_cloud` is true.
- `left/image_rect`
  ([sensor_msgs/msg/Image](https://docs.ros.org/en/rolling/p/sensor_msgs/msg/Image.html)):
  Left RGB/Mono rectified image. Required if parameter
  `subscribe_stereo` is true.
- `left/camera_info`
  ([sensor_msgs/msg/CameraInfo](https://docs.ros.org/en/rolling/p/sensor_msgs/msg/CameraInfo.html)):
  Left camera metadata. Required if parameter `subscribe_stereo` is
  true.
- `right/image_rect`
  ([sensor_msgs/msg/Image](https://docs.ros.org/en/rolling/p/sensor_msgs/msg/Image.html)):
  Right Mono rectified image. Required if parameter `subscribe_stereo`
  is true.
- `right/camera_info`
  ([sensor_msgs/msg/CameraInfo](https://docs.ros.org/en/rolling/p/sensor_msgs/msg/CameraInfo.html)):
  Right camera metadata. Required if parameter `subscribe_stereo` is
  true.
- `goal`
  ([geometry_msgs/msg/PoseStamped](https://docs.ros.org/en/rolling/p/geometry_msgs/msg/PoseStamped.html)):
  **`'Planning `**' Plan a path to reach this goal using the current
  online map. The goal should be close enough to the map's graph to be
  accepted (see RTAB-Map's parameter `RGBD/LocalRadius`). Note that
  only nodes in Working Memory are used, for exploration it may be ok,
  but it would be better to use service `set_goal` if you are coming
  back in a previously mapped area. See **`'Planning `**' published
  topics for corresponding generated outputs.
- `rgbd_image`
  ([rtabmap_msgs/msg/RGBDImage](https://docs.ros.org/en/rolling/p/rtabmap_msgs/msg/RGBDImage.html)):
  RGB-D synchronized image, only when `subscribe_rgbd` is `true` and
  `rgbd_cameras=1`
- `rgbd_image#`
  ([rtabmap_msgs/msg/RGBDImage](https://docs.ros.org/en/rolling/p/rtabmap_msgs/msg/RGBDImage.html)):
  RGB-D synchronized image, only when `subscribe_rgbd` is `true` and
  `rgbd_cameras>=2`
- `rgbd_images`
  ([rtabmap_msgs/msg/RGBDImages](https://docs.ros.org/en/rolling/p/rtabmap_msgs/msg/RGBDImages.html)):
  RGB-D/Stereo synchronized images (published by a
  [rgbdx_sync](https://index.ros.org/p/rtabmap_sync) node), only when
  `subscribe_rgbd` is `true` and `rgbd_cameras=0`.
- `imu`
  ([sensor_msgs/msg/Imu](https://docs.ros.org/en/rolling/p/sensor_msgs/msg/Imu.html)):
  Can be used to add gravity constraints in the graph. The whole map
  will then be aligned with gravity. The quaternion should be already
  computed (see
  [imu_filter_madgwick](https://index.ros.org/p/imu_filter_madgwick) to
  compute it).
- `gps/fix`
  ([sensor_msgs/msg/NavSatFix](https://docs.ros.org/en/rolling/p/sensor_msgs/msg/NavSatFix.html)):
  Can be used to add GPS constraints in the graph. This could eventually
  be used to export poses in GPS format. With
  `Optimizer/PriorsIgnored` parameter set to `false`, the graph can
  be also optimized using the GPS values. See also this
  [page](https://github.com/introlab/rtabmap/wiki/Robust-Graph-Optimization#multi-session)
  on how GPS can be used to limit loop closure detection radius.
- `global_pose`
  ([geometry_msgs/msg/PoseWithCovarianceStamped](https://docs.ros.org/en/rolling/p/geometry_msgs/msg/PoseWithCovarianceStamped.html)):
  Can be used to add global prior constraints in the graph. With
  `Optimizer/PriorsIgnored` parameter set to `false`, the graph can
  be optimized using the prior values.
- `tag_detections`
  ([apriltag_ros/msg/AprilTagDetectionArray](https://docs.ros.org/en/rolling/p/apriltag_ros/msg/AprilTagDetectionArray.html)):
  Can be used to add landmark constraints in the graph. Landmarks are
  used in graph optimization and also for loop closure detection. See
  also [apriltag_ros](https://github.com/AprilRobotics/apriltag_ros)
  repository.
- `fiducial_transforms`
  ([fiducial_msgs/msg/FiducialTransformArray](https://docs.ros.org/en/rolling/p/fiducial_msgs/msg/FiducialTransformArray.html)):
  Can be used to add landmark constraints in the graph. Landmarks are
  used in graph optimization and also for loop closure detection. See
  also [fiducials](https://github.com/UbiquityRobotics/fiducials)
  repository.

#### Published Topics

- `info`
  ([rtabmap_msgs/msg/Info](https://docs.ros.org/en/rolling/p/rtabmap_msgs/msg/Info.html)):
  RTAB-Map's info.
- `mapData`
  ([rtabmap_msgs/msg/MapData](https://docs.ros.org/en/rolling/p/rtabmap_msgs/msg/MapData.html)):
  RTAB-Map's graph and latest node data.
- `mapGraph`
  ([rtabmap_msgs/msg/MapGraph](https://docs.ros.org/en/rolling/p/rtabmap_msgs/msg/MapGraph.html)):
  RTAB-Map's graph only.
- `grid_map`
  ([nav_msgs/msg/OccupancyGrid](https://docs.ros.org/en/rolling/p/nav_msgs/msg/OccupancyGrid.html)):
  **`'Mapping`**' Occupancy grid generated with laser scans. Use
  parameters in **`'Mapping`**' group below and RTAB-Map's parameters
  starting with `Grid/` prefix. Do `rtabmap \--params \| grep Grid/`
  to see all of them.
- `proj_map`
  ([nav_msgs/msg/OccupancyGrid](https://docs.ros.org/en/rolling/p/nav_msgs/msg/OccupancyGrid.html)):
  **`'Mapping`**' DEPRECATED: use `/grid_map` topic instead with
  `Grid/FromDepth=true`.
- `cloud_map`
  ([sensor_msgs/msg/PointCloud2](https://docs.ros.org/en/rolling/p/sensor_msgs/msg/PointCloud2.html)):
  **`'Mapping`**' 3D point cloud generated from the assembled local
  grids. Use parameters with prefixes `map_` and `cloud_` below.
- `cloud_obstacles`
  ([sensor_msgs/msg/PointCloud2](https://docs.ros.org/en/rolling/p/sensor_msgs/msg/PointCloud2.html)):
  **`'Mapping`**' 3D point cloud of obstacles generated from the
  assembled local grids. Use parameters with prefixes `map_` and
  `cloud_` below.
- `cloud_ground`
  ([sensor_msgs/msg/PointCloud2](https://docs.ros.org/en/rolling/p/sensor_msgs/msg/PointCloud2.html)):
  **`'Mapping`**' 3D point cloud of ground generated from the assembled
  local grids. Use parameters with prefixes `map_` and `cloud_`
  below.
- `scan_map`
  ([sensor_msgs/msg/PointCloud2](https://docs.ros.org/en/rolling/p/sensor_msgs/msg/PointCloud2.html)):
  **`'Mapping`**' 3D point cloud generated with the 2D scans or 3D
  scans. Use parameters with prefixes `map_` and `scan_` below.
- `labels`
  ([visualization_msgs/msg/MarkerArray](https://docs.ros.org/en/rolling/p/visualization_msgs/msg/MarkerArray.html)):
  Convenient way to show graph's labels in RVIZ.
- `global_path`
  ([nav_msgs/msg/Path](https://docs.ros.org/en/rolling/p/nav_msgs/msg/Path.html)):
  **`'Planning `**' Poses of the planned global path. Published only
  once for each path planned.
- `local_path`
  ([nav_msgs/msg/Path](https://docs.ros.org/en/rolling/p/nav_msgs/msg/Path.html)):
  **`'Planning `**' Upcoming local poses corresponding to those of the
  global path. Published on every map update.
- `goal_reached`
  ([std_msgs/msg/Bool](https://docs.ros.org/en/rolling/p/std_msgs/msg/Bool.html)):
  **`'Planning `**' Status message if the goal is successfully reached
  or not.
- `goal_out`
  ([geometry_msgs/msg/PoseStamped](https://docs.ros.org/en/rolling/p/geometry_msgs/msg/PoseStamped.html)):
  **`'Planning `**' Current metric goal sent from the rtabmap's
  topological planner. For example, this can be connected to
  `move_base_simple/goal` topic of
  [move_base](https://index.ros.org/p/move_base).
- `octomap_full`
  ([octomap_msgs/msg/Octomap](https://docs.ros.org/en/rolling/p/octomap_msgs/msg/Octomap.html)):
  Get an OctoMap. *Available only if rtabmap_slam is built with
  octomap*.
- `octomap_binary`
  ([octomap_msgs/msg/Octomap](https://docs.ros.org/en/rolling/p/octomap_msgs/msg/Octomap.html)):
  Get an OctoMap. *Available only if rtabmap_slam is built with
  octomap*.
- `octomap_occupied_space`
  ([sensor_msgs/msg/PointCloud2](https://docs.ros.org/en/rolling/p/sensor_msgs/msg/PointCloud2.html)):
  A point cloud of the occupied space (obstacles and ground) of the
  OctoMap. *Available only if rtabmap_slam is built with octomap*.
- `octomap_obstacles`
  ([sensor_msgs/msg/PointCloud2](https://docs.ros.org/en/rolling/p/sensor_msgs/msg/PointCloud2.html)):
  A point cloud of the obstacles of the OctoMap. *Available only if
  rtabmap_slam is built with octomap*.
- `octomap_ground`
  ([sensor_msgs/msg/PointCloud2](https://docs.ros.org/en/rolling/p/sensor_msgs/msg/PointCloud2.html)):
  A point cloud of the ground of the OctoMap. *Available only if
  rtabmap_slam is built with octomap*.
- `octomap_empty_space`
  ([sensor_msgs/msg/PointCloud2](https://docs.ros.org/en/rolling/p/sensor_msgs/msg/PointCloud2.html)):
  A point cloud of empty space of the OctoMap. *Available only if
  rtabmap_slam is built with octomap*.
- `octomap_grid`
  ([nav_msgs/msg/OccupancyGrid](https://docs.ros.org/en/rolling/p/nav_msgs/msg/OccupancyGrid.html)):
  The projection of the OctoMap into a 2D occupancy grid map. *Available
  only if rtabmap_slam is built with octomap*.

#### Services

- `get_map`
  ([nav_msgs/srv/GetMap](https://docs.ros.org/en/rolling/p/nav_msgs/srv/GetMap.html)):
  Call this service to get the standard 2D occupancy grid
- `get_map_data`
  ([rtabmap_msgs/srv/GetMap](https://docs.ros.org/en/rolling/p/rtabmap_msgs/srv/GetMap.html)):
  Call this service to get the map data
- `publish_map`
  ([rtabmap_msgs/srv/PublishMap](https://docs.ros.org/en/rolling/p/rtabmap_msgs/srv/PublishMap.html)):
  Call this service to publish the map data
- `list_labels`
  ([rtabmap_msgs/srv/ListLabels](https://docs.ros.org/en/rolling/p/rtabmap_msgs/srv/ListLabels.html)):
  Get current labels of the graph.
- `update_parameters`
  ([std_srvs/srv/Empty](https://docs.ros.org/en/rolling/p/std_srvs/srv/Empty.html)):
  The node will update with current parameters of the rosparam server
- `reset`
  ([std_srvs/srv/Empty](https://docs.ros.org/en/rolling/p/std_srvs/srv/Empty.html)):
  Delete the map
- `pause`
  ([std_srvs/srv/Empty](https://docs.ros.org/en/rolling/p/std_srvs/srv/Empty.html)):
  Pause mapping
- `resume`
  ([std_srvs/srv/Empty](https://docs.ros.org/en/rolling/p/std_srvs/srv/Empty.html)):
  Resume mapping
- `trigger_new_map`
  ([std_srvs/srv/Empty](https://docs.ros.org/en/rolling/p/std_srvs/srv/Empty.html)):
  The node will begin a new map
- `backup`
  ([std_srvs/srv/Empty](https://docs.ros.org/en/rolling/p/std_srvs/srv/Empty.html)):
  Backup the database to "`database_path`.back" (default
  `/.ros/rtabmap.db.back`)
- `set_mode_localization`
  ([std_srvs/srv/Empty](https://docs.ros.org/en/rolling/p/std_srvs/srv/Empty.html)):
  Set localization mode
- `set_mode_mapping`
  ([std_srvs/srv/Empty](https://docs.ros.org/en/rolling/p/std_srvs/srv/Empty.html)):
  Set mapping mode
- `set_label`
  ([rtabmap_msgs/srv/SetLabel](https://docs.ros.org/en/rolling/p/rtabmap_msgs/srv/SetLabel.html)):
  Set a label to latest node or a specified node.
- `set_goal`
  ([rtabmap_msgs/srv/SetGoal](https://docs.ros.org/en/rolling/p/rtabmap_msgs/srv/SetGoal.html)):
  **`'Planning `**' Set a topological goal (a node id or a node label
  in the graph). Plan a path to reach this goal using the whole map
  contained in memory (including nodes in Long-Term Memory). See
  **`'Planning `**' published topics for corresponding generated
  outputs.
- `octomap_full`
  ([octomap_msgs/srv/GetOctomap](https://docs.ros.org/en/rolling/p/octomap_msgs/srv/GetOctomap.html)):
  Get an OctoMap. *Available only if rtabmap_slam is built with
  octomap*.
- `octomap_binary`
  ([octomap_msgs/srv/GetOctomap](https://docs.ros.org/en/rolling/p/octomap_msgs/srv/GetOctomap.html)):
  Get an OctoMap. *Available only if rtabmap_slam is built with
  octomap*.

#### Parameters

- `~subscribe_depth` (`bool`, default: `"true"`): Subscribe to depth
  image
- `~subscribe_scan` (`bool`, default: `"false"`): Subscribe to laser
  scan
- `~subscribe_scan_cloud` (`bool`, default: `"false"`): Subscribe to
  laser scan point cloud
- `~subscribe_stereo` (`bool`, default: `"false"`): Subscribe to
  stereo images
- `~subscribe_rgbd` (`bool`, default: `"false"`): Subsribe to
  `rgbd_image` topic.
- `~frame_id` (`string`, default: `"base_link"`): The frame attached
  to the mobile base.
- `~map_frame_id` (`string`, default: `"map"`): The frame attached
  to the map.
- `~odom_frame_id` (`string`, default: `""`): The frame attached to
  odometry. If empty, rtabmap will subscribe to `odom` topic to get
  odometry. If set, odometry is got from
  [tf](https://index.ros.org/p/tf) (in this case, the covariance value
  is fixed by `odom_tf_angular_variance` and
  `odom_tf_linear_variance`).
- `~odom_tf_linear_variance` (`double`, default: `0.001`): When
  `odom_frame_id` is used, the first 3 values of the diagonal of the
  6x6 covariance matrix are set to this value.
- `~odom_tf_angular_variance` (`double`, default: `0.001`): When
  `odom_frame_id` is used, the last 3 values of the diagonal of the
  6x6 covariance matrix are set to this value.
- `~queue_size` (`int`, default: `10`): Size of message queue for each
  synchronized topic.
- `~publish_tf` (`bool`, default: `"true"`): Publish TF from /map to
  /odom.
- `~tf_delay` (`double`, default: `0.05`): Rate at which the TF from
  /map to /odom is published (20 Hz).
- `~tf_prefix` (`string`, default: `""`): Prefix to add to generated
  [tf](https://index.ros.org/p/tf).
- `~wait_for_transform` (`bool`, default: `"true"`): Wait (maximum
  `wait_for_transform_duration` sec) for transform when a
  [tf](https://index.ros.org/p/tf) transform is not still available.
- `~wait_for_transform_duration` (`double`, default: `0.1`): Wait
  duration for `wait_for_transform`.
- `~config_path` (`string`, default: `""`): Path of a config files
  containing RTAB-Map's parameters. Parameters set in the launch file
  overwrite those in the config file.
- `~database_path` (`string`, default: `"/.ros/rtabmap.db"`): Path
  of the RTAB-Map's database.
- `~gen_scan` (`bool`, default: `"false"`): Generate laser scans
  from depth images (using the middle horizontal line of the depth
  image). Not generated if `subscribe_scan` or
  `subscribe_scan_cloud` are true.
- `~gen_scan_max_depth` (`double`, default: `4.0`): Maximum depth of the
  laser scans generated.
- `~approx_sync` (`bool`, default: `"false"`): Use approximate time
  synchronization of input messages. If false, note that the odometry
  input must have also exactly the same timestamps than the input
  images.
- `~rgbd_cameras` (`int`, default: `1`): Number of RGB-D cameras to use
  (when `subscribe_rgbd` is `true`). Well for now, a maximum of 4
  cameras can be synchronized at the same time. If > 1, the rgbd_image
  topics should contain the camera index starting with 0. For example,
  if we have 2 cameras, you should set `rgbd_image0` and
  `rgbd_image1` topics. If you set to 0, the input `rgbd_images`
  topic is used instead.
- `~use_action_for_goal` (`bool`, default: `"false"`):
  **`'Planning `**' Use [actionlib](https://index.ros.org/p/actionlib)
  to send the metric goals to
  [move_base](https://index.ros.org/p/move_base). The advantage over
  just connecting `goal_out` to `move_base_simple/goal` is that
  rtabmap can have a feedback if the goal is reached or if
  [move_base](https://index.ros.org/p/move_base) has failed. See
  [move_base Action API](https://index.ros.org/p/move_base) for more
  info.
- `~odom_sensor_sync` (`bool`, default: `"false"`): Adjust image and
  scan poses relatively to odometry pose for each node added to graph.
  For example, if an image received at t=1s has been synchronized with a
  scan at t=1.1s (and our reference stamp is the scan) and the robot is
  moving forward at 1 m/s, then we will ask TF to know the motion
  between t=1s and t=1.1s (which would be 0.1 m) for the camera to
  adjust its local transform (-10 cm) relative to scan frame at scan
  stamp. This also applies to multi-camera synchronization.
- `~gen_depth` (`bool`, default: `"false"`): Generate depth image
  from `scan_cloud` projection into RGB camera, taking into account
  displacement of the RGB camera accordingly to odometry and lidar
  frames. It works like
  [pointcloud_to_depthimage](http://wiki.ros.org/rtabmap_util#rtabmap_util.2Fpointcloud_to_depthimage)
  node, but at slam frequency.
- `~gen_depth_decimation` (`int`, default: `1`): Scale down image size
  of the camera info received (creating smaller depth image).
- `~gen_depth_fill_holes_size` (`int`, default: `0`): Fill holes of
  empty pixels up to this size. Values are interpolated from neighbor
  depth values. 0 means disabled.
- `~gen_depth_fill_iterations` (`double`, default: `0.1`): Maximum depth
  error (m) to interpolate.
- `~gen_depth_fill_holes_error` (`int`, default: `1`): Number of
  iterations to fill holes.
- `~map_filter_radius` (`double`, default: `0.0`): **`'Mapping`**'
  Filter nodes before creating the maps. Only load data for one node in
  the filter radius (the latest data is used) up to filter angle
  (`map_filter_angle`). Set to 0.0 to disable node filtering. Used for
  all published maps.
- `~map_filter_angle` (`double`, default: `30.0`): **`'Mapping`**'
  Angle used when filtering nodes before creating the maps. See also
  `map_filter_radius`. Used for all published maps.
- `~map_cleanup` (`bool`, default: `"true"`): **`'Mapping`**' If
  there is no subscription to any map `cloud_map`, `grid_map` or
  `proj_map`, clear the corresponding data.
- `~latch` (`bool`, default: `"true"`): **`'Mapping`**' If true,
  the last message published on the map topics will be saved and sent to
  new subscribers when they connect.
- `~map_always_update` (`bool`, default: `"false"`):
  **`'Mapping`**' Always update the occupancy grid map even if the
  graph has not been updated (e.g., by default when the robot is not
  moving, the graph is not growing). For example, if the environment is
  dynamic, we may want to update the map even when to robot is not
  moving. Another approach would be to force rtabmap to always update
  the graph (by setting `RGBD/LinearUpdate` to 0), which can be not
  efficient over time as the map will grow even if the robot doesn't
  move.
- `~map_empty_ray_tracing` (`bool`, default: `"true"`):
  **`'Mapping`**' Do ray tracing to fill unknown space for invalid 2D
  scan's rays (assuming invalid rays to be infinite). Used only when
  `map_always_update` is also `true`.
- `~cloud_output_voxelized` (`bool`, default: `"true"`):
  **`'Mapping`**' Do a final voxel filtering after all clouds are
  assembled with a voxel size equals to `Grid/CellSize`. Used for
  `cloud_map` published topic.
- `~cloud_subtract_filtering` (`bool`, default: `"true"`):
  **`'Mapping`**' When appending a new cloud to `cloud_map`, filter
  points that have less neighbors than
  `cloud_subtract_filtering_min_neighbors` in the radius
  `Grid/CellSize`. This will helps to reconstruct the whole map's
  cloud faster when a loop closure happens. Used for `cloud_map`
  published topic.
- `~cloud_subtract_filtering_min_neighbors` (`int`, default: `2`):
  **`'Mapping`**' See `cloud_subtract_filtering` parameter's
  description.

#### Required tf Transforms

- `base_link` → `<the frame attached to sensors of incoming data>`:
  usually a fixed value, broadcast periodically by a
  [robot_state_publisher](https://index.ros.org/p/robot_state_publisher),
  or a `tf` [static_transform_publisher](https://index.ros.org/p/tf).
- `odom` → `base_link`: usually provided by the odometry system (e.g.,
  the driver for the mobile base).

#### Provided tf Transforms

- `map` → `odom`: the current odometry correction.
