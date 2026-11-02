

```wiki
'''''[[rtabmap_ros]]:''' [[rtabmap]] | [[rtabmap_conversions]] | [[rtabmap_costmap_plugins]] | [[rtabmap_demos]] | [[rtabmap_examples]] | [[rtabmap_launch]] | [[rtabmap_legacy]] | [[rtabmap_msgs]] | [[rtabmap_odom]] | [[rtabmap_python]] | [[rtabmap_rviz_plugins]] | [[rtabmap_slam]] | [[rtabmap_sync]] | [[rtabmap_util]] | [[rtabmap_viz]]''
```



## Nodes

### Visual and Lidar Odometry

Common odometry stuff for
[rgbd_odometry](#rgbd_odometry),
[stereo_odometry](#stereo_odometry) and
[icp_odometry](#icp_odometry) nodes. These nodes
wrap the various odometry approaches of RTAB-Map. When a transformation
cannot be computed, a null transformation is sent to notify the receiver
that odometry is not updated or lost.

- There are two set of parameters: ROS and RTAB-Map's parameters. The
  ROS parameters are for connection stuff to interface the RTAB-Map
  library with ROS. The RTAB-Map's parameters are those from the
  RTAB-Map library.
- Parameters available for odometry can be shown from the terminal by
  using the "\--params" argument:



```
$ rosrun rtabmap_odom rgbd_odometry --params
or
$ rosrun rtabmap_odom stereo_odometry --params
or
$ rosrun rtabmap_odom icp_odometry --params
```



#### Arguments

- `"\--params"`: Show RTAB-Map's parameters related to this node
  and exit.

#### Subscribed Topics

- `imu`
  ([sensor_msgs/msg/Imu](https://docs.ros.org/en/rolling/p/sensor_msgs/msg/Imu.html)):
  IMU used by VIO approaches (see `rtabmap \--params \| grep
  Odom/Strategy`). For non-VIO approaches, it can be used to initialize
  the odometry to be aligned with gravity (with
  `wait_imu_to_init=true`). For default visual F2M approach, gravity
  constraints will be added in local bundle adjustment, making it as a
  loosely VIO approach. For non-VIO approaches and F2M, the IMU topic
  should contain the quarternion already estimated (see
  [imu_filter_madgwick](https://index.ros.org/p/imu_filter_madgwick) or
  [imu_complementary_filter](https://index.ros.org/p/imu_complementary_filter)).

#### Published Topics

- `odom`
  ([nav_msgs/msg/Odometry](https://docs.ros.org/en/rolling/p/nav_msgs/msg/Odometry.html)):
  Odometry stream. Send null odometry if cannot be computed.
- `odom_info`
  ([rtabmap_msgs/msg/OdomInfo](https://docs.ros.org/en/rolling/p/rtabmap_msgs/msg/OdomInfo.html)):
  Odometry info stream. RTAB-Map's parameter `Odom/FillInfoData`
  should be true to fill features information (default is `true`).
- `odom_last_frame`
  ([sensor_msgs/msg/PointCloud2](https://docs.ros.org/en/rolling/p/sensor_msgs/msg/PointCloud2.html)):
  3D features of the last frame used to estimate the transformation.
- `odom_local_map`
  ([sensor_msgs/msg/PointCloud2](https://docs.ros.org/en/rolling/p/sensor_msgs/msg/PointCloud2.html)):
  Local map of 3D features used as reference to estimate the
  transformation. Only published if RTAB-Map's parameter
  `Odom/Strategy=0`.

#### Services

- `reset_odom`
  ([std_srvs/srv/Empty](https://docs.ros.org/en/rolling/p/std_srvs/srv/Empty.html)):
  Restart odometry to identity transformation.
- `reset_odom_to_pose`
  ([rtabmap_msgs/srv/ResetPose](https://docs.ros.org/en/rolling/p/rtabmap_msgs/srv/ResetPose.html)):
  Restart odometry to specified transformation. Format: `"x y z roll
  pitch yaw"`.
- `pause_odom`
  ([std_srvs/srv/Empty](https://docs.ros.org/en/rolling/p/std_srvs/srv/Empty.html)):
  Pause odometry.
- `resume_odom`
  ([std_srvs/srv/Empty](https://docs.ros.org/en/rolling/p/std_srvs/srv/Empty.html)):
  Resume odometry.

#### Parameters

- `~frame_id` (`string`, default: `"base_link"`): The frame attached
  to the mobile base.
- `~odom_frame_id` (`string`, default: `"odom"`): The odometry
  frame.
- `~publish_tf` (`bool`, default: `"true"`): Publish TF from /odom
  to /base_link.
- `~tf_prefix` (`bool`, default: `""`): Prefix to add to generated
  [tf](https://index.ros.org/p/tf).
- `~wait_for_transform` (`bool`, default: `"false"`): Wait (maximum
  1 sec) for transform when a [tf](https://index.ros.org/p/tf) transform
  is not still available.
- `~initial_pose` (`string`, default: `""`): The initial pose of the
  odometry. Format: `"x y z roll pitch yaw"`.
- `~queue_size` (`int`, default: `10`): Size of message queue for each
  synchronized topic.
- `~publish_null_when_lost` (`bool`, default: `true`): Odometry is
  published with null transform when lost.
- `~ground_truth_frame_id` (`string`, default: `""`): This can be
  used to have odometry initialized at the current ground truth pose.
- `~ground_truth_base_frame_id` (`string`, default: `""`): See
  `ground_truth_frame_id` description.
- `~guess_frame_id` (`string`, default: `""`): Use this frame as
  guess to compute odometry, otherwise odometry guess is done from a
  constant motion model. `tf` published by this node will be the
  correction of actual odometry. If `guess_frame_id` is
  `odom_combined`, `odom_frame_id` is `odom` and `frame_id` is
  `base_footprint`, `odom` -> `odom_combined` is published by
  this node to have a `tf` tree like this: `/odom -> /odom_combined
  -> /base_link`.
- `~guess_min_translation` (`float`, default: `0.0` m): When
  `guess_frame_id` is set, don't update odometry unless the guess
  moved at least as much as this value.
- `~guess_min_rotation` (`float`, default: `0.0` rad): When
  `guess_frame_id` is set, don't update odometry unless the guess
  rotated at least as much as this value.
- `~config_path` (`string`, default: `""`): A config (ini) file with
  RTAB-Map's parameters.
- `~wait_imu_to_init` (`bool`, default: `false`): Make the node waits
  for first imu before starting estimating odometry. This will make sure
  that odometry is aligned with gravity on initialization.

#### Required tf Transforms

- `base_link` → `<the frame attached to sensors of incoming data>`:
  usually a fixed value, broadcast periodically by a
  [robot_state_publisher](https://index.ros.org/p/robot_state_publisher),
  or a `tf` [static_transform_publisher](https://index.ros.org/p/tf).

#### Provided tf Transforms

- `odom` → `base_link`: the current estimate of the robot's pose within
  the odometry frame.

### rgbd_odometry

This node wraps the RGBD odometry approach of RTAB-Map. Using RGBD
images, odometry is computed using visual features extracted from the
RGB images with their depth information from the depth images. Using the
feature correspondences between the images, a RANSAC approach computes
the transformation between the consecutive images.

See also
[Visual Odometry](#visual-and-lidar-odometry)
for common odometry stuff used by this node.

#### Subscribed Topics

- `rgb/image`
  ([sensor_msgs/msg/Image](https://docs.ros.org/en/rolling/p/sensor_msgs/msg/Image.html)):
  RGB/Mono rectified image.
- `rgb/camera_info`
  ([sensor_msgs/msg/CameraInfo](https://docs.ros.org/en/rolling/p/sensor_msgs/msg/CameraInfo.html)):
  RGB camera metadata.
- `depth/image`
  ([sensor_msgs/msg/Image](https://docs.ros.org/en/rolling/p/sensor_msgs/msg/Image.html)):
  Registered depth image.
- `rgbd_image`
  ([rtabmap_msgs/msg/RGBDImage](https://docs.ros.org/en/rolling/p/rtabmap_msgs/msg/RGBDImage.html)):
  RGB-D synchronized image, only when `subscribe_rgbd` is `true` and
  `rgbd_cameras=1`.
- `rgbd_image#`
  ([rtabmap_msgs/msg/RGBDImage](https://docs.ros.org/en/rolling/p/rtabmap_msgs/msg/RGBDImage.html)):
  RGB-D synchronized image, only when `subscribe_rgbd` is `true` and
  `rgbd_cameras>=2`. Index \# starting at 0.
- `rgbd_images`
  ([rtabmap_msgs/msg/RGBDImages](https://docs.ros.org/en/rolling/p/rtabmap_msgs/msg/RGBDImages.html)):
  Multi synchronized cameras, only when `subscribe_rgbd` is `true`
  and `rgbd_cameras=0`

#### Parameters

- `~approx_sync` (`bool`, default: `"true"`): Use approximate time
  synchronization of rgb and depth messages. If false, the rgb and depth
  images must have the same timestamps.
- `~subscribe_rgbd` (`bool`, default: `"false"`): Subsribe to
  `rgbd_image` topic.
- `~rgbd_cameras` (`int`, default: `1`): Number of RGB-D cameras to use
  (when `subscribe_rgbd` is `true`). Well for now, a maximum of 4
  cameras can be synchronized at the same time. If > 1, the
  `rgbd_image` topics should contain the camera index starting with 0.
  For example, if we have 2 cameras, you should set `rgbd_image0` and
  `rgbd_image1` topics. If set to 0, `rgbd_images` (published by a
  [rgbdx_sync](https://index.ros.org/p/rtabmap_sync) node) input is used
  instead, internal images should be RGB-D, not stereo. If they are
  stereo, use `stereo_odometry` node instead.

### stereo_odometry

This node wraps the stereo odometry approach of RTAB-Map. Using stereo
images, odometry is computed using visual features extracted from the
left images with their depth information computed by finding the same
features on the right images. Using the feature correspondences, a
RANSAC approach computes the transformation between the consecutive left
images.

See also
[Visual Odometry](#visual-and-lidar-odometry)
for common odometry stuff used by this node.

#### Subscribed Topics

- `left/image_rect`
  ([sensor_msgs/msg/Image](https://docs.ros.org/en/rolling/p/sensor_msgs/msg/Image.html)):
  Left RGB/Mono rectified image.
- `left/camera_info`
  ([sensor_msgs/msg/CameraInfo](https://docs.ros.org/en/rolling/p/sensor_msgs/msg/CameraInfo.html)):
  Left camera metadata.
- `right/image_rect`
  ([sensor_msgs/msg/Image](https://docs.ros.org/en/rolling/p/sensor_msgs/msg/Image.html)):
  Right Mono rectified image.
- `right/camera_info`
  ([sensor_msgs/msg/CameraInfo](https://docs.ros.org/en/rolling/p/sensor_msgs/msg/CameraInfo.html)):
  Right camera metadata.
- `rgbd_image`
  ([rtabmap_msgs/msg/RGBDImage](https://docs.ros.org/en/rolling/p/rtabmap_msgs/msg/RGBDImage.html)):
  Stereo synchronized image, only when `subscribe_rgbd` is `true`
  and `rgbd_cameras=1`. This topic should contain left image in rgb
  field and right image in depth field (with corresponding camera info).
- `rgbd_image#`
  ([rtabmap_msgs/msg/RGBDImage](https://docs.ros.org/en/rolling/p/rtabmap_msgs/msg/RGBDImage.html)):
  Stereo synchronized image, only when `subscribe_rgbd` is `true`
  and `rgbd_cameras>=2`. Index \# starting at 0. This topic should
  contain left image in rgb field and right image in depth field (with
  corresponding camera info).
- `rgbd_images`
  ([rtabmap_msgs/msg/RGBDImages](https://docs.ros.org/en/rolling/p/rtabmap_msgs/msg/RGBDImages.html)):
  Multi synchronized cameras, only when `subscribe_rgbd` is `true`
  and `rgbd_cameras=0`

#### Parameters

- `~approx_sync` (`bool`, default: `"false"`): Use approximate time
  synchronization of stereo messages. If false, the left/right images
  and the left/right camera infos must have the same timestamps.
- `~subscribe_rgbd` (`bool`, default: `"false"`): Subsribe to
  `rgbd_image` topic.
- `~rgbd_cameras` (`int`, default: `1`): Number of stereo cameras to use
  (when `subscribe_rgbd` is `true`). Well for now, a maximum of 4
  cameras can be synchronized at the same time. If > 1, the
  `rgbd_image` topics should contain the camera index starting with 0.
  For example, if we have 2 cameras, you should set `rgbd_image0` and
  `rgbd_image1` topics. If set to 0, `rgbd_images` (published by a
  [rgbdx_sync](https://index.ros.org/p/rtabmap_sync) node) input is used
  instead, internal images should be stereo, not RGB-D. If they are
  RGB-D, use `rgbd_odometry` node instead.

### icp_odometry

This node wraps the icp odometry approach of RTAB-Map. Using laser scan
or a point cloud, odometry is computed by Iterative Closest Point (ICP)
registration.

See also
[Visual Odometry](#visual-and-lidar-odometry)
for common odometry stuff used by this node.

#### Subscribed Topics

- `scan`
  ([sensor_msgs/msg/LaserScan](https://docs.ros.org/en/rolling/p/sensor_msgs/msg/LaserScan.html)):
  Laser scan, assuming the lidar is installed horizontally. Don't use
  `scan` or `scan_cloud` at the same time.
- `scan_cloud`
  ([sensor_msgs/msg/PointCloud2](https://docs.ros.org/en/rolling/p/sensor_msgs/msg/PointCloud2.html)):
  Point cloud, which can be 2D or 3D. Don't use `scan` or
  `scan_cloud` at the same time.

#### Parameters

- `~scan_cloud_max_points` (`int`, default: `0`): Maximum point in
  laser scan or point cloud. `0` means the maximum is defined by the
  size of ranges vector for laser scan topic.
- `~scan_downsampling_step` (`int`, default: `1`): Downsample the
  laser scan or point cloud. `<=1` means no downsampling, otherwise
  one ray/point each step is kept.
- `~scan_voxel_size` (`float`, default: `0.0` m): Filter the laser
  scan or point cloud using
  [voxel filter](http://pointclouds.org/documentation/tutorials/voxel_grid.php)
  of this size. `0.0` means disabled.
- `~scan_normal_k` (`int`, default: `0`): Estimate normals of the
  laser scan or point cloud by using k nearest points. Useful only if
  `Icp/Point2Plane` parameter is enabled. `0` means disabled.
- `~scan_normal_radius` (`float`, default: `0.0`): Estimate normals of
  the laser scan or point cloud by using nearest points under this fixed
  radius. Useful only if `Icp/Point2Plane` parameter is enabled.
  `0.0` means disabled.
- `~deskewing` (`bool`, default: `false`): For PointCloud2 input
  `scan_cloud` (3D LiDAR), each point will be deskewed based on their
  timestamp during the rotation of the LiDAR by either using
  `guess_frame_id` when provided or using a constant velocity model.
  The PointCloud2 topic should have timestamp channel as `t`, `time`
  or `stamps`. Supported timestamp formats are FLOAT32 (seconds since
  header's timestamp) and UINT32 (nanoseconds since header's
  timestamp). If PointCloud2 input is organized, deskewing will be
  faster (transformed per columns instead per points). Note that for 2D
  LaserScan topic `scan`, it is deskewed only when `guess_frame_id`
  is used or `frame_id` is not the same frame than in the message.
- `~deskewing_slerp` (`bool`, default: `false`): When enable, a lookup
  transform for TF will only be done for the first and last stamp, then
  points with in between timestamps will be deskewed by interpolating
  between the oldest and latest poses. This can be faster than the
  default approach looking for transform for very timestamps (though
  later approach would be more accurate).
