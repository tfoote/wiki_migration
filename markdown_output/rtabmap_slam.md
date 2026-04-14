\<\<Include(rtabmap_ros/menu)\>\>

## Nodes

### rtabmap

This is the main node of this package. It is a wrapper of the RTAB-Map
Core library. This is where the graph of the map is incrementally built
and optimized when a loop closure is detected. The online output of the
node is the local graph with the latest added data to the map. The
default location of the RTAB-Map database is \"/.ros/rtabmap.db\" and
the workspace is also set to \"/.ros\". To get a 3D point cloud or a 2D
occupancy grid of the environment, subscribe to \`cloud_map\` or
\`grid_map\` topics.

-   There are two set of parameters: ROS and RTAB-Map\'s parameters. The
    ROS parameters are for connection stuff to interface the RTAB-Map
    library with ROS. The RTAB-Map\'s parameters are those from the
    RTAB-Map library.

```{=html}
<!-- -->
```
-   One way to know RTAB-Map\'s parameters is to look at this file :
    [Parameters.h](https://github.com/introlab/rtabmap/blob/master/corelib/include/rtabmap/core/Parameters.h#L161).
    There is a description for each parameter. Here two examples (use
    string type for all RTAB-Map\'s parameters) by either using
    \`param\` member or by passing as arguments:
    ```
<launch>
<node name="rtabmap" pkg="rtabmap_slam" type="rtabmap" args="--Grid/RangeMax 5">
   <param name="Optimizer/Iterations" type="int" value="50"/>
</node>
</launch>
```

```{=html}
<!-- -->
```
-   Another way to show available parameters from the terminal is to
    call the node with \"\--params\" argument: ```
$ rosrun rtabmap_slam rtabmap --params
or
$ rtabmap --params
```

```{=html}
<!-- -->
```
-   By default, rtabmap is in mapping mode. To set in localization mode
    with a previously created map, you should set the memory not
    incremental (make sure that arguments don\'t contain
    \`\"\--delete_db_on_start\"\` too!): ```
<launch>
<node name="rtabmap" pkg="rtabmap_slam" type="rtabmap" args="">
   <!-- LOCALIZATION MODE -->
   <param name="Mem/IncrementalMemory" type="string" value="false"/>
</node>
</launch>
```

#### Arguments

-   \`\"\--delete_db_on_start\"\` or \`\"-d\"\`: Delete the database
    before starting, otherwise the previous mapping session is loaded.
-   \`\"\--udebug\"\`: Show RTAB-Map\'s debug/info/warning/error logs.
-   \`\"\--uinfo\"\`: Show RTAB-Map\'s info/warning/error logs.
-   \`\"\--params\"\`: Show RTAB-Map\'s parameters related to this node
    and exit.

```clearsilver
sub {
  0{
   name = odom
   type = nav_msgs/Odometry
   desc = Odometry stream. Required if parameters `subscribe_depth` or `subscribe_stereo` are true '''and''' `odom_frame_id` is not set.
   }
  1{
   name = rgb/image
   type = sensor_msgs/Image
   desc = RGB/Mono image. Should be rectified when `subscribe_depth` is true. Not required if parameter `subscribe_stereo` is true (use `left/image_rect` instead).
   }
  2{
   name = rgb/camera_info
   type = sensor_msgs/CameraInfo
   desc = RGB camera metadata. Not required if parameter `subscribe_stereo` is true (use `left/camera_info` instead).
   }
  3{
   name = depth/image
   type = sensor_msgs/Image
   desc = Registered depth image. Required if parameter `subscribe_depth` is true.
   }
  4{
   name = scan
   type = sensor_msgs/LaserScan
   desc = Laser scan stream. Required if parameter `subscribe_scan` is true.
   }
  5{
   name = scan_cloud
   type = sensor_msgs/PointCloud2
   desc = Laser scan point cloud stream. Required if parameter `subscribe_scan_cloud` is true.
   }
  6{
   name = left/image_rect
   type = sensor_msgs/Image
   desc = Left RGB/Mono rectified image. Required if parameter `subscribe_stereo` is true.
   }
  7{
   name = left/camera_info
   type = sensor_msgs/CameraInfo
   desc = Left camera metadata. Required if parameter `subscribe_stereo` is true.
   }
  8{
   name = right/image_rect
   type = sensor_msgs/Image
   desc = Right Mono rectified image. Required if parameter `subscribe_stereo` is true.
   }
  9{
   name = right/camera_info
   type = sensor_msgs/CameraInfo
   desc = Right camera metadata. Required if parameter `subscribe_stereo` is true.
   }
  10{
   name = goal
   type = geometry_msgs/PoseStamped
   desc =  '''''Planning ''''' Plan a path to reach this goal using the current online map. The goal should be close enough to the map's graph to be accepted (see RTAB-Map's parameter `RGBD/LocalRadius`). Note that only nodes in Working Memory are used, for exploration it may be ok, but it would be better to use service `set_goal` if you are coming back in a previously mapped area. See  '''''Planning ''''' published topics for corresponding generated outputs.
   }
 11{
   name = rgbd_image
   type = rtabmap_msgs/RGBDImage
   desc = RGB-D synchronized image, only when `subscribe_rgbd` is `true` and `rgbd_cameras=1`
   }
 12{
   name = rgbd_image#
   type = rtabmap_msgs/RGBDImage
   desc = RGB-D synchronized image, only when `subscribe_rgbd` is `true` and `rgbd_cameras>=2`
   }
 13{
   name = rgbd_images
   type = rtabmap_msgs/RGBDImages
   desc = RGB-D/Stereo synchronized images (published by a [[rtabmap_sync#rtabmap_sync.2Frgbdx_sync|rgbdx_sync]] node), only when `subscribe_rgbd` is `true` and `rgbd_cameras=0`.
   }
 14{
   name = imu
   type = sensor_msgs/Imu
   desc = Can be used to add gravity constraints in the graph. The whole map will then be aligned with gravity. The quaternion should be already computed (see [[imu_filter_madgwick]] to compute it). 
   }
 15{
   name = gps/fix
   type = sensor_msgs/NavSatFix
   desc = Can be used to add GPS constraints in the graph. This could eventually be used to export poses in GPS format. With `Optimizer/PriorsIgnored` parameter set to `false`, the graph can be also optimized using the GPS values. See also this [[https://github.com/introlab/rtabmap/wiki/Robust-Graph-Optimization#multi-session|page]] on how GPS can be used to limit loop closure detection radius.
   }
 16{
   name = global_pose
   type = geometry_msgs/PoseWithCovarianceStamped
   desc = Can be used to add global prior constraints in the graph. With `Optimizer/PriorsIgnored` parameter set to `false`, the graph can be optimized using the prior values.
   }
 17{
   name = tag_detections
   type = apriltag_ros/AprilTagDetectionArray
   desc = Can be used to add landmark constraints in the graph. Landmarks are used in graph optimization and also for loop closure detection. See also [[https://github.com/AprilRobotics/apriltag_ros|apriltag_ros]] repository.
   }
 18{
   name = fiducial_transforms
   type = fiducial_msgs/FiducialTransformArray
   desc = Can be used to add landmark constraints in the graph. Landmarks are used in graph optimization and also for loop closure detection. See also [[https://github.com/UbiquityRobotics/fiducials|fiducials]] repository.
   }
}
pub {
  0{
   name = info
   type = rtabmap_msgs/Info
   desc = RTAB-Map's info.
   }
  1{
   name = mapData
   type = rtabmap_msgs/MapData
   desc = RTAB-Map's graph and latest node data.
   }
  2{
   name = mapGraph
   type = rtabmap_msgs/MapGraph
   desc = RTAB-Map's graph only.
   }
  3{
   name = grid_map
   type = nav_msgs/OccupancyGrid
   desc = '''''Mapping''''' Occupancy grid generated with laser scans. Use parameters in '''''Mapping''''' group below and RTAB-Map's parameters starting with `Grid/` prefix. Do `rtabmap --params | grep Grid/` to see all of them.
   }
  4{
   name = proj_map
   type = nav_msgs/OccupancyGrid
   desc = '''''Mapping''''' DEPRECATED: use `/grid_map` topic instead with `Grid/FromDepth=true`.
   }
  5{
   name = cloud_map
   type = sensor_msgs/PointCloud2
   desc = '''''Mapping''''' 3D point cloud generated from the assembled local grids. Use parameters with prefixes `map_` and `cloud_` below.
   }
  6{
   name = cloud_obstacles
   type = sensor_msgs/PointCloud2
   desc = '''''Mapping''''' 3D point cloud of obstacles generated from the assembled local grids. Use parameters with prefixes `map_` and `cloud_` below.
   }
  7{
   name = cloud_ground
   type = sensor_msgs/PointCloud2
   desc = '''''Mapping''''' 3D point cloud of ground generated from the assembled local grids. Use parameters with prefixes `map_` and `cloud_` below.
   }
  8{
   name = scan_map
   type = sensor_msgs/PointCloud2
   desc = '''''Mapping''''' 3D point cloud generated with the 2D scans or 3D scans. Use parameters with prefixes `map_` and `scan_` below.
   }
  9{
   name = labels
   type = visualization_msgs/MarkerArray
   desc = Convenient way to show graph's labels in RVIZ.
   }
  10{
   name = global_path
   type = nav_msgs/Path
   desc =  '''''Planning ''''' Poses of the planned global path. Published only once for each path planned.
   }
  11{
   name = local_path
   type = nav_msgs/Path
   desc =  '''''Planning ''''' Upcoming local poses corresponding to those of the global path. Published on every map update.
   }
  12{
   name = goal_reached
   type = std_msgs/Bool
   desc =  '''''Planning ''''' Status message if the goal is successfully reached or not.
   }
  13{
   name = goal_out
   type = geometry_msgs/PoseStamped
   desc =  '''''Planning ''''' Current metric goal sent from the rtabmap's topological planner. For example, this can be connected to `move_base_simple/goal` topic of [[move_base]].
   }
  14{
   name = octomap_full
   type = octomap_msgs/Octomap
   desc = Get an OctoMap. ''Available only if rtabmap_slam is built with octomap''.
   }
  15{
   name = octomap_binary
   type = octomap_msgs/Octomap
   desc = Get an OctoMap. ''Available only if rtabmap_slam is built with octomap''.
   }
  16{
   name = octomap_occupied_space
   type = sensor_msgs/PointCloud2
   desc = A point cloud of the occupied space (obstacles and ground) of the OctoMap. ''Available only if rtabmap_slam is built with octomap''.
   }
  17{
   name = octomap_obstacles
   type = sensor_msgs/PointCloud2
   desc = A point cloud of the obstacles of the OctoMap. ''Available only if rtabmap_slam is built with octomap''.
   }
  18{
   name = octomap_ground
   type = sensor_msgs/PointCloud2
   desc = A point cloud of the ground of the OctoMap. ''Available only if rtabmap_slam is built with octomap''.
   }
  19{
   name = octomap_empty_space
   type = sensor_msgs/PointCloud2
   desc = A point cloud of empty space of the OctoMap. ''Available only if rtabmap_slam is built with octomap''.
   }
  20{
   name = octomap_grid
   type = nav_msgs/OccupancyGrid
   desc = The projection of the OctoMap into a 2D occupancy grid map. ''Available only if rtabmap_slam is built with octomap''.
   }
}

srv {
  1{
   name = get_map
   type = nav_msgs/GetMap
   desc = Call this service to get the standard 2D occupancy grid
  }
  2{
   name = get_map_data
   type = rtabmap_msgs/GetMap
   desc = Call this service to get the map data
  }
  4{
   name = publish_map
   type = rtabmap_msgs/PublishMap
   desc = Call this service to publish the map data
   }
  5{
   name = list_labels
   type = rtabmap_msgs/ListLabels
   desc = Get current labels of the graph.
   }
  6{
   name = update_parameters
   type = std_srvs/Empty
   desc = The node will update with current parameters of the rosparam server
   }
  7{
   name = reset
   type = std_srvs/Empty
   desc = Delete the map
   }
  8{
   name = pause
   type = std_srvs/Empty
   desc = Pause mapping
   }
  9{
   name = resume
   type = std_srvs/Empty
   desc = Resume mapping
   }
  10{
   name = trigger_new_map
   type = std_srvs/Empty
   desc = The node will begin a new map
   }
 11{
   name = backup
   type = std_srvs/Empty
   desc = Backup the database to "`database_path`.back" (default `~/.ros/rtabmap.db.back`)
   }
 12{
   name = set_mode_localization
   type = std_srvs/Empty
   desc = Set localization mode
   }
 13{
   name = set_mode_mapping
   type = std_srvs/Empty
   desc = Set mapping mode
   }
 14{
   name = set_label
   type = rtabmap_msgs/SetLabel
   desc = Set a label to latest node or a specified node.
   }
 15{
   name = set_goal
   type = rtabmap_msgs/SetGoal
   desc =  '''''Planning ''''' Set a topological goal (a node id or a node label in the graph). Plan a path to reach this goal using the whole map contained in memory (including nodes in Long-Term Memory). See  '''''Planning ''''' published topics for corresponding generated outputs.
   }
 16{
   name = octomap_full
   type = octomap_msgs/GetOctomap
   desc = Get an OctoMap. ''Available only if rtabmap_slam is built with octomap''.
   }
 17{
   name = octomap_binary
   type = octomap_msgs/GetOctomap
   desc = Get an OctoMap. ''Available only if rtabmap_slam is built with octomap''.
   }
}

param {
  0{
   name = ~subscribe_depth
   type = bool
   default = `"true"`
   desc = Subscribe to depth image
   }
  1{
   name = ~subscribe_scan
   type = bool
   default = `"false"`
   desc = Subscribe to laser scan
   }
  2{
   name = ~subscribe_scan_cloud
   type = bool
   default = `"false"`
   desc = Subscribe to laser scan point cloud
   }
  3{
   name = ~subscribe_stereo
   type = bool
   default = `"false"`
   desc = Subscribe to stereo images
   }
  4{
   name = ~subscribe_rgbd
   type = bool
   default = `"false"`
   desc = Subsribe to `rgbd_image` topic.
   }
  5{
   name = ~frame_id
   type = string
   default = `"base_link"`
   desc = The frame attached to the mobile base.
   }
  6{
   name = ~map_frame_id
   type = string
   default = `"map"`
   desc = The frame attached to the map.
   }
  7{
   name = ~odom_frame_id
   type = string
   default = `""`
   desc = The frame attached to odometry. If empty, rtabmap will subscribe to `odom` topic to get odometry. If set, odometry is got from [[tf]] (in this case, the covariance value is fixed by `odom_tf_angular_variance` and `odom_tf_linear_variance`).
   }
  8{
   name = ~odom_tf_linear_variance
   type = double
   default = `0.001`
   desc = When `odom_frame_id` is used, the first 3 values of the diagonal of the 6x6 covariance matrix are set to this value.
   }
  9{
   name = ~odom_tf_angular_variance
   type = double
   default = `0.001`
   desc = When `odom_frame_id` is used, the last 3 values of the diagonal of the 6x6 covariance matrix are set to this value.
   }
  10{
   name = ~queue_size
   type = int
   default = 10
   desc = Size of message queue for each synchronized topic.
   }
  11{
   name = ~publish_tf
   type = bool
   default = `"true"`
   desc = Publish TF from /map to /odom.
   }
  12{
   name = ~tf_delay
   type = double
   default = 0.05
   desc = Rate at which the TF from /map to /odom is published (20 Hz).
   }
  13{
   name = ~tf_prefix
   type = string
   default = `""`
   desc = Prefix to add to generated [[tf]].
   }
  14{
   name = ~wait_for_transform
   type = bool
   default = `"true"`
   desc = Wait (maximum `wait_for_transform_duration` sec) for transform when a [[tf]] transform is not still available.
   }
  15{
   name = ~wait_for_transform_duration
   type = double
   default = 0.1
   desc = Wait duration for `wait_for_transform`.
   }
  16{
   name = ~config_path
   type = string
   default = `""`
   desc = Path of a config files containing RTAB-Map's parameters. Parameters set in the launch file overwrite those in the config file.
   }
  17{
   name = ~database_path
   type = string
   default = `"~/.ros/rtabmap.db"`
   desc = Path of the RTAB-Map's database.
   }
  18{
   name = ~gen_scan
   type = bool
   default = `"false"`
   desc = Generate laser scans from depth images (using the middle horizontal line of the depth image). Not generated if `subscribe_scan` or `subscribe_scan_cloud` are true.
   }
 19{
   name = ~gen_scan_max_depth
   type = double
   default = 4.0
   desc = Maximum depth of the laser scans generated.
   }
 20{
   name = ~approx_sync
   type = bool
   default = `"false"`
   desc = Use approximate time synchronization of input messages. If false, note that the odometry input must have also exactly the same timestamps than the input images.
   }
 21{
   name = ~rgbd_cameras
   type = int
   default = 1
   desc = Number of RGB-D cameras to use (when `subscribe_rgbd` is `true`). Well for now, a maximum of 4 cameras can be synchronized at the same time. If > 1, the rgbd_image topics should contain the camera index starting with 0. For example, if we have 2 cameras, you should set `rgbd_image0` and `rgbd_image1` topics. If you set to 0, the input `rgbd_images` topic is used instead.
   }
 22{
   name = ~use_action_for_goal
   type = bool
   default = `"false"`
   desc =  '''''Planning ''''' Use [[actionlib]] to send the metric goals to [[move_base]]. The advantage over just connecting `goal_out` to `move_base_simple/goal` is that rtabmap can have a feedback if the goal is reached or if [[move_base]] has failed. See [[move_base#Action_API|move_base Action API]] for more info.
   }
 23{
   name = ~odom_sensor_sync
   type = bool
   default = `"false"`
   desc = Adjust image and scan poses relatively to odometry pose for each node added to graph. For example, if an image received at t=1s has been synchronized with a scan at t=1.1s (and our reference stamp is the scan) and the robot is moving forward at 1 m/s, then we will ask TF to know the motion between t=1s and t=1.1s (which would be 0.1 m) for the camera to adjust its local transform (-10 cm) relative to scan frame at scan stamp. This also applies to multi-camera synchronization.
   }
 30{
   name = ~gen_depth
   type = bool
   desc = Generate depth image from `scan_cloud` projection into RGB camera, taking into account displacement of the RGB camera accordingly to odometry and lidar frames. It works like [[http://wiki.ros.org/rtabmap_util#rtabmap_util.2Fpointcloud_to_depthimage|pointcloud_to_depthimage]] node, but at slam frequency.
   default = `"false"`
   }
 31{
   name = ~gen_depth_decimation
   type = int
   desc = Scale down image size of the camera info received (creating smaller depth image).
   default = 1
   }
 32{
   name = ~gen_depth_fill_holes_size
   type = int
   desc = Fill holes of empty pixels up to this size. Values are interpolated from neighbor depth values. 0 means disabled.
   default = 0
   }
 33{
   name = ~gen_depth_fill_iterations
   type = double
   desc = Maximum depth error (m) to interpolate.
   default = 0.1
   }
 34{
   name = ~gen_depth_fill_holes_error
   type = int
   desc = Number of iterations to fill holes.
   default = 1
   }


  100{
   name = ~map_filter_radius
   type = double
   default = 0.0
   desc =  '''''Mapping''''' Filter nodes before creating the maps. Only load data for one node in the filter radius (the latest data is used) up to filter angle (`map_filter_angle`). Set to 0.0 to disable node filtering. Used for all published maps.
   }
  101{
   name = ~map_filter_angle
   type = double
   default = 30.0
   desc =  '''''Mapping''''' Angle used when filtering nodes before creating the maps. See also `map_filter_radius`. Used for all published maps.
   }
  102{
   name = ~map_cleanup
   type = bool
   default = `"true"`
   desc =  '''''Mapping''''' If there is no subscription to any map `cloud_map`, `grid_map` or `proj_map`, clear the corresponding data.
   }
  103{
   name = ~latch
   type = bool
   default = `"true"`
   desc =  '''''Mapping''''' If true, the last message published on the map topics will be saved and sent to new subscribers when they connect.
   }
  112{
   name = ~map_always_update
   type = bool
   default = `"false"`
   desc =   '''''Mapping''''' Always update the occupancy grid map even if the graph has not been updated (e.g., by default when the robot is not moving, the graph is not growing). For example, if the environment is dynamic, we may want to update the map even when to robot is not moving. Another approach would be to force rtabmap to always update the graph (by setting `RGBD/LinearUpdate` to 0), which can be not efficient over time as the map will grow even if the robot doesn't move.
   }
  113{
   name = ~map_empty_ray_tracing
   type = bool
   default = `"true"`
   desc =   '''''Mapping''''' Do ray tracing to fill unknown space for invalid 2D scan's rays (assuming invalid rays to be infinite). Used only when `map_always_update` is also `true`. 
   }
  114{
   name = ~cloud_output_voxelized
   type = bool
   default = `"true"`
   desc =   '''''Mapping''''' Do a final voxel filtering after all clouds are assembled with a voxel size equals to `Grid/CellSize`. Used for `cloud_map` published topic. 
   }
  116{
   name = ~cloud_subtract_filtering
   type = bool
   default = `"true"`
   desc =   '''''Mapping''''' When appending a new cloud to `cloud_map`, filter points that have less neighbors than `cloud_subtract_filtering_min_neighbors` in the radius `Grid/CellSize`. This will helps to reconstruct the whole map's cloud faster when a loop closure happens. Used for `cloud_map` published topic.
   }
  117{
   name = ~cloud_subtract_filtering_min_neighbors
   type = int
   default = 2
   desc =   '''''Mapping''''' See `cloud_subtract_filtering` parameter's description.
   }
}

req_tf {
  0{
   from = base_link
   to = <the frame attached to sensors of incoming data>
   desc = usually a fixed value, broadcast periodically by a [[robot_state_publisher]], or a `tf` [[tf#static_transform_publisher|static_transform_publisher]].
   }
  1{
   from = odom
   to = base_link
   desc = usually provided by the odometry system (e.g., the driver for the mobile base).
   }
}
prov_tf {
  0.from = map
  0.to = odom
  0.desc = the current odometry correction.
}
```
