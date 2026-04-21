[Included page rtabmap_ros/menu not found](Included page rtabmap_ros/menu not found)

## Nodes

### rtabmap_viz

This node starts the visualization interface of RTAB-Map. It is a
wrapper of the RTAB-Map GUI library. It has the same purpose as
[rviz](rviz) but with specific options for RTAB-Map.

![RGB-D Mapping\|width="800"](attachment:rgbd_mapping.png)

#### Arguments

-   `-d "config.ini"`: Set a RTAB-Map ini file for GUI interface
    parameters. Default is `"/.ros/rtabmapGUI.ini"`.



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
   desc = Laser scan stream. Required if parameter `subscribe_scan_cloud` is true.
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
   name = odom_info
   type = rtabmap_msgs/OdomInfo
   desc = Odometry info. Required if parameter `subscribe_odom_info` is true.
   }
 11{
   name = info
   type = rtabmap_msgs/Info
   desc = RTAB-Map's statistics info.
   }
 12{
   name = mapData
   type = rtabmap_msgs/MapData
   desc = RTAB-Map's graph and latest node data.
   }
 13{
   name = rgbd_image
   type = rtabmap_msgs/RGBDImage
   desc = RGB-D synchronized image, only when `subscribe_rgbd` is `true`.
   }
}

param {
  0{
   name = ~subscribe_depth
    type = bool
    default = `"false"`
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
   name = ~subscribe_odom_info
    type = bool
    default = `"false"`
    desc = Subscribe to odometry info messages
   }
  5{
   name = ~subscribe_rgbd
   type = bool
   default = `"false"`
   desc = Subsribe to `rgbd_image` topic.
   }
  6{
   name = ~frame_id
    type = string
    default = `"base_link"`
    desc = The frame attached to the mobile base.
   }
  7{
   name = ~odom_frame_id
    type = string
    default = `""`
    desc = The frame attached to odometry. If empty, rtabmapviz will subscribe to `odom` topic to get odometry. If set, odometry is got from [[tf]].
   }
  8{
   name = ~tf_prefix
   type = string
   default = `""`
   desc = Prefix to add to generated [[tf]].
   }
  9{
   name = ~wait_for_transform
   type = bool
   default = `"false"`
   desc = Wait (maximum 1 sec) for transform when a [[tf]] transform is not still available.
   }
  10{
   name = ~queue_size
    type = int
    default = 10
    desc = Size of message queue for each synchronized topic.
   }
  11{
   name = ~rgbd_cameras
    type = int
    default = 1
    desc = Number of RGB-D cameras to use (when `subscribe_rgbd` is `true`). Well for now, a maximum of 4 cameras can be synchronized at the same time. If > 1, the rgbd_image topics should contain the camera index starting with 0. For example, if we have 2 cameras, you should set `rgbd_image0` and `rgbd_image1` topics.
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
  2{
   from = map
   to = odom
   desc = the current odometry correction.
   }
}
```


