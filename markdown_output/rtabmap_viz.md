

```wiki
'''''[[rtabmap_ros]]:''' [[rtabmap]] | [[rtabmap_conversions]] | [[rtabmap_costmap_plugins]] | [[rtabmap_demos]] | [[rtabmap_examples]] | [[rtabmap_launch]] | [[rtabmap_legacy]] | [[rtabmap_msgs]] | [[rtabmap_odom]] | [[rtabmap_python]] | [[rtabmap_rviz_plugins]] | [[rtabmap_slam]] | [[rtabmap_sync]] | [[rtabmap_util]] | [[rtabmap_viz]]''
```



## Nodes

### rtabmap_viz

This node starts the visualization interface of RTAB-Map. It is a
wrapper of the RTAB-Map GUI library. It has the same purpose as
[rviz](https://index.ros.org/p/rviz) but with specific options for
RTAB-Map.

![RGB-D Mapping](doc/rgbd_mapping.png)

#### Arguments

- `-d "config.ini"`: Set a RTAB-Map ini file for GUI interface
  parameters. Default is `"/.ros/rtabmapGUI.ini"`.

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
  Laser scan stream. Required if parameter `subscribe_scan_cloud` is
  true.
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
- `odom_info`
  ([rtabmap_msgs/msg/OdomInfo](https://docs.ros.org/en/rolling/p/rtabmap_msgs/msg/OdomInfo.html)):
  Odometry info. Required if parameter `subscribe_odom_info` is true.
- `info`
  ([rtabmap_msgs/msg/Info](https://docs.ros.org/en/rolling/p/rtabmap_msgs/msg/Info.html)):
  RTAB-Map's statistics info.
- `mapData`
  ([rtabmap_msgs/msg/MapData](https://docs.ros.org/en/rolling/p/rtabmap_msgs/msg/MapData.html)):
  RTAB-Map's graph and latest node data.
- `rgbd_image`
  ([rtabmap_msgs/msg/RGBDImage](https://docs.ros.org/en/rolling/p/rtabmap_msgs/msg/RGBDImage.html)):
  RGB-D synchronized image, only when `subscribe_rgbd` is `true`.

#### Parameters

- `~subscribe_depth` (`bool`, default: `"false"`): Subscribe to
  depth image
- `~subscribe_scan` (`bool`, default: `"false"`): Subscribe to laser
  scan
- `~subscribe_scan_cloud` (`bool`, default: `"false"`): Subscribe to
  laser scan point cloud
- `~subscribe_stereo` (`bool`, default: `"false"`): Subscribe to
  stereo images
- `~subscribe_odom_info` (`bool`, default: `"false"`): Subscribe to
  odometry info messages
- `~subscribe_rgbd` (`bool`, default: `"false"`): Subsribe to
  `rgbd_image` topic.
- `~frame_id` (`string`, default: `"base_link"`): The frame attached
  to the mobile base.
- `~odom_frame_id` (`string`, default: `""`): The frame attached to
  odometry. If empty, rtabmapviz will subscribe to `odom` topic to get
  odometry. If set, odometry is got from
  [tf](https://index.ros.org/p/tf).
- `~tf_prefix` (`string`, default: `""`): Prefix to add to generated
  [tf](https://index.ros.org/p/tf).
- `~wait_for_transform` (`bool`, default: `"false"`): Wait (maximum
  1 sec) for transform when a [tf](https://index.ros.org/p/tf) transform
  is not still available.
- `~queue_size` (`int`, default: `10`): Size of message queue for each
  synchronized topic.
- `~rgbd_cameras` (`int`, default: `1`): Number of RGB-D cameras to use
  (when `subscribe_rgbd` is `true`). Well for now, a maximum of 4
  cameras can be synchronized at the same time. If > 1, the rgbd_image
  topics should contain the camera index starting with 0. For example,
  if we have 2 cameras, you should set `rgbd_image0` and
  `rgbd_image1` topics.

#### Required tf Transforms

- `base_link` → `<the frame attached to sensors of incoming data>`:
  usually a fixed value, broadcast periodically by a
  [robot_state_publisher](https://index.ros.org/p/robot_state_publisher),
  or a `tf` [static_transform_publisher](https://index.ros.org/p/tf).
- `odom` → `base_link`: usually provided by the odometry system (e.g.,
  the driver for the mobile base).
- `map` → `odom`: the current odometry correction.
