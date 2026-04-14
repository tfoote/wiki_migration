\<\<Include(rtabmap_ros/menu)\>\>

## Nodes

### Visual and Lidar Odometry

Common odometry stuff for [rgbd_odometry](rtabmap_odom#rgbd_odometry),
[stereo_odometry](rtabmap_odom#stereo_odometry) and
[icp_odometry](rtabmap_odom#icp_odometry) nodes. These nodes wrap the
various odometry approaches of RTAB-Map. When a transformation cannot be
computed, a null transformation is sent to notify the receiver that
odometry is not updated or lost.

-   There are two set of parameters: ROS and RTAB-Map\'s parameters. The
    ROS parameters are for connection stuff to interface the RTAB-Map
    library with ROS. The RTAB-Map\'s parameters are those from the
    RTAB-Map library.
-   Parameters available for odometry can be shown from the terminal by
    using the \"\--params\" argument:

```
$ rosrun rtabmap_odom rgbd_odometry --params
or
$ rosrun rtabmap_odom stereo_odometry --params
or
$ rosrun rtabmap_odom icp_odometry --params
```

#### Arguments

-   \`\"\--params\"\`: Show RTAB-Map\'s parameters related to this node
    and exit.

```clearsilver
pub {
  0{
   name = odom
   type = nav_msgs/Odometry
   desc = Odometry stream. Send null odometry if cannot be computed.
   }
  1{
   name = odom_info
   type = rtabmap_msgs/OdomInfo
   desc = Odometry info stream. RTAB-Map's parameter `Odom/FillInfoData` should be true to fill features information (default is `true`).
   }
  2{
   name = odom_last_frame
   type = sensor_msgs/PointCloud2
   desc = 3D features of the last frame used to estimate the transformation.
   }
  3{
   name = odom_local_map
   type = sensor_msgs/PointCloud2
   desc = Local map of 3D features used as reference to estimate the transformation. Only published if RTAB-Map's parameter `Odom/Strategy=0`.
   }
}

sub {
  0.name = imu
  0.type = sensor_msgs/Imu
  0.desc = IMU used by VIO approaches (see `rtabmap --params | grep Odom/Strategy`). For non-VIO approaches, it can be used to initialize the odometry to be aligned with gravity (with `wait_imu_to_init=true`). For default visual F2M approach, gravity constraints will be added in local bundle adjustment, making it as a loosely VIO approach. For non-VIO approaches and F2M, the IMU topic should contain the quarternion already estimated (see [[imu_filter_madgwick]] or [[imu_complementary_filter]]).
}

srv {
  0.name = reset_odom
  0.type = std_srvs/Empty
  0.desc = Restart odometry to identity transformation.
  1.name = reset_odom_to_pose
  1.type = rtabmap_msgs/ResetPose
  1.desc = Restart odometry to specified transformation. Format: `"x y z roll pitch yaw"`.
  2.name = pause_odom
  2.type = std_srvs/Empty
  2.desc = Pause odometry.
  3.name = resume_odom
  3.type = std_srvs/Empty
  3.desc = Resume odometry.
}


param {
  0{
   name = ~frame_id
   type = string
   default = `"base_link"`
   desc = The frame attached to the mobile base.
   }
  1{
   name = ~odom_frame_id
   type = string
   default = `"odom"`
   desc = The odometry frame.
   }
  2{
   name = ~publish_tf
   type = bool
   default = `"true"`
   desc = Publish TF from /odom to /base_link.
   }
  3{
   name = ~tf_prefix
   type = bool
   default = `""`
   desc = Prefix to add to generated [[tf]].
   }
  4{
   name = ~wait_for_transform
   type = bool
   default = `"false"`
   desc = Wait (maximum 1 sec) for transform when a [[tf]] transform is not still available.
   }
  5{
   name = ~initial_pose
   type = string
   default = `""`
   desc = The initial pose of the odometry. Format: `"x y z roll pitch yaw"`.
   }
  6{
   name = ~queue_size
   type = int
   default = 10
   desc = Size of message queue for each synchronized topic.
   }
  7{
   name = ~publish_null_when_lost
   type = bool
   default = true
   desc = Odometry is published with null transform when lost.
   }
  8{
   name = ~ground_truth_frame_id
   type = string
   default = `""`
   desc = This can be used to have odometry initialized at the current ground truth pose.
   }
  9{
   name = ~ground_truth_base_frame_id
   type = string
   default = `""`
   desc = See `ground_truth_frame_id` description.
   }
  10{
   name = ~guess_frame_id
   type = string
   default = `""`
   desc = Use this frame as guess to compute odometry, otherwise odometry guess is done from a constant motion model. `tf` published by this node will be the correction of actual odometry. If `guess_frame_id` is `odom_combined`, `odom_frame_id` is `odom` and `frame_id` is `base_footprint`, `odom` -> `odom_combined` is published by this node to have a `tf` tree like this: `/odom -> /odom_combined -> /base_link`.
   }
  11{
   name = ~guess_min_translation
   type = float
   default = `0.0` m
   desc = When `guess_frame_id` is set, don't update odometry unless the guess moved at least as much as this value.
   }
  12{
   name = ~guess_min_rotation
   type = float
   default = `0.0` rad
   desc = When `guess_frame_id` is set, don't update odometry unless the guess rotated at least as much as this value.
   }
  13{
   name = ~config_path
   type = string
   default = `""`
   desc = A config (ini) file with RTAB-Map's parameters.
   }
  14{
   name = ~wait_imu_to_init
   type = bool
   default = false
   desc = Make the node waits for first imu before starting estimating odometry. This will make sure that odometry is aligned with gravity on initialization.
   }
}

req_tf {
  0.from = base_link
  0.to = <the frame attached to sensors of incoming data>
  0.desc = usually a fixed value, broadcast periodically by a [[robot_state_publisher]], or a `tf` [[tf#static_transform_publisher|static_transform_publisher]].

}

prov_tf {
  0.from = odom
  0.to = base_link
  0.desc = the current estimate of the robot's pose within the odometry frame.
}
```

### rgbd_odometry

This node wraps the RGBD odometry approach of RTAB-Map. Using RGBD
images, odometry is computed using visual features extracted from the
RGB images with their depth information from the depth images. Using the
feature correspondences between the images, a RANSAC approach computes
the transformation between the consecutive images.

See also [Visual Odometry](rtabmap_odom#Visual_and_Lidar_Odometry) for
common odometry stuff used by this node. ```clearsilver
sub {
  0.name = rgb/image
  0.type = sensor_msgs/Image
  0.desc = RGB/Mono rectified image.
  1.name = rgb/camera_info
  1.type = sensor_msgs/CameraInfo
  1.desc = RGB camera metadata.
  2.name = depth/image
  2.type = sensor_msgs/Image
  2.desc = Registered depth image.
  3.name = rgbd_image
  3.type = rtabmap_msgs/RGBDImage
  3.desc = RGB-D synchronized image, only when `subscribe_rgbd` is `true` and `rgbd_cameras=1`.
  4.name = rgbd_image#
  4.type = rtabmap_msgs/RGBDImage
  4.desc = RGB-D synchronized image, only when `subscribe_rgbd` is `true` and `rgbd_cameras>=2`. Index # starting at 0.
  5.name = rgbd_images
  5.type = rtabmap_msgs/RGBDImages
  5.desc = Multi synchronized cameras, only when `subscribe_rgbd` is `true` and `rgbd_cameras=0`
}

param {
  0{
   name = ~approx_sync
   type = bool
   default = `"true"`
   desc = Use approximate time synchronization of rgb and depth messages. If false, the rgb and depth images must have the same timestamps.
   }
  1{
   name = ~subscribe_rgbd
   type = bool
   default = `"false"`
   desc = Subsribe to `rgbd_image` topic.
   }
  2{
   name = ~rgbd_cameras
   type = int
   default = 1
   desc = Number of RGB-D cameras to use (when `subscribe_rgbd` is `true`). Well for now, a maximum of 4 cameras can be synchronized at the same time. If > 1, the `rgbd_image` topics should contain the camera index starting with 0. For example, if we have 2 cameras, you should set `rgbd_image0` and `rgbd_image1` topics. If set to 0, `rgbd_images` (published by a [[rtabmap_sync#rtabmap_sync.2Frgbdx_sync|rgbdx_sync]] node) input is used instead, internal images should be RGB-D, not stereo. If they are stereo, use `stereo_odometry` node instead.
   }
}
```

### stereo_odometry

This node wraps the stereo odometry approach of RTAB-Map. Using stereo
images, odometry is computed using visual features extracted from the
left images with their depth information computed by finding the same
features on the right images. Using the feature correspondences, a
RANSAC approach computes the transformation between the consecutive left
images.

See also [Visual Odometry](rtabmap_odom#Visual_and_Lidar_Odometry) for
common odometry stuff used by this node. ```clearsilver
sub {
  0.name = left/image_rect
  0.type = sensor_msgs/Image
  0.desc = Left RGB/Mono rectified image.
  1.name = left/camera_info
  1.type = sensor_msgs/CameraInfo
  1.desc = Left camera metadata.
  2.name = right/image_rect
  2.type = sensor_msgs/Image
  2.desc = Right Mono rectified image.
  3.name = right/camera_info
  3.type = sensor_msgs/CameraInfo
  3.desc = Right camera metadata.
  4.name = rgbd_image
  4.type = rtabmap_msgs/RGBDImage
  4.desc = Stereo synchronized image, only when `subscribe_rgbd` is `true` and `rgbd_cameras=1`. This topic should contain left image in rgb field and right image in depth field (with corresponding camera info).
  5.name = rgbd_image#
  5.type = rtabmap_msgs/RGBDImage
  5.desc = Stereo synchronized image, only when `subscribe_rgbd` is `true` and `rgbd_cameras>=2`. Index # starting at 0. This topic should contain left image in rgb field and right image in depth field (with corresponding camera info).
  6.name = rgbd_images
  6.type = rtabmap_msgs/RGBDImages
  6.desc = Multi synchronized cameras, only when `subscribe_rgbd` is `true`  and `rgbd_cameras=0`
}

param {
  0{
   name = ~approx_sync
   type = bool
   default = `"false"`
   desc = Use approximate time synchronization of stereo messages. If false, the left/right images and the left/right camera infos must have the same timestamps.
   }
  1{
   name = ~subscribe_rgbd
   type = bool
   default = `"false"`
   desc = Subsribe to `rgbd_image` topic.
   }
  2{
   name = ~rgbd_cameras
   type = int
   default = 1
   desc = Number of stereo cameras to use (when `subscribe_rgbd` is `true`). Well for now, a maximum of 4 cameras can be synchronized at the same time. If > 1, the `rgbd_image` topics should contain the camera index starting with 0. For example, if we have 2 cameras, you should set `rgbd_image0` and `rgbd_image1` topics. If set to 0, `rgbd_images` (published by a [[rtabmap_sync#rtabmap_sync.2Frgbdx_sync|rgbdx_sync]] node) input is used instead, internal images should be stereo, not RGB-D. If they are RGB-D, use `rgbd_odometry` node instead.
   }
}
```

### icp_odometry

This node wraps the icp odometry approach of RTAB-Map. Using laser scan
or a point cloud, odometry is computed by Iterative Closest Point (ICP)
registration.

See also [Visual Odometry](rtabmap_odom#Visual_and_Lidar_Odometry) for
common odometry stuff used by this node. ```clearsilver
sub {
  0.name = scan
  0.type = sensor_msgs/LaserScan
  0.desc = Laser scan, assuming the lidar is installed horizontally. Don't use `scan` or `scan_cloud` at the same time. 
  1.name = scan_cloud
  1.type = sensor_msgs/PointCloud2
  1.desc = Point cloud, which can be 2D or 3D. Don't use `scan` or `scan_cloud` at the same time. 
}

param {
  0{
   name = ~scan_cloud_max_points
   type = int
   default = `0`
   desc = Maximum point in laser scan or point cloud. `0` means the maximum is defined by the size of ranges vector for laser scan topic.
   }
  1{
   name = ~scan_downsampling_step
   type = int
   default = `1`
   desc = Downsample the laser scan or point cloud. `<=1` means no downsampling, otherwise one ray/point each step is kept.
   }
  2{
   name = ~scan_voxel_size
   type = float
   default = `0.0` m
   desc = Filter the laser scan or point cloud using [[http://pointclouds.org/documentation/tutorials/voxel_grid.php|voxel filter]] of this size. `0.0` means disabled.
   }
  3{
   name = ~scan_normal_k
   type = int
   default = `0`
   desc = Estimate normals of the laser scan or point cloud by using k nearest points. Useful only if `Icp/Point2Plane` parameter is enabled. `0` means disabled.
   }
  4{
   name = ~scan_normal_radius
   type = float
   default = `0.0`
   desc = Estimate normals of the laser scan or point cloud by using nearest points under this fixed radius. Useful only if `Icp/Point2Plane` parameter is enabled. `0.0` means disabled.
   }
  5{
   name = ~deskewing
   type = bool
   default = false
   desc = For PointCloud2 input `scan_cloud` (3D LiDAR), each point will be deskewed based on their timestamp during the rotation of the LiDAR by either using `guess_frame_id` when provided or using a constant velocity model. The PointCloud2 topic should have timestamp channel as `t`, `time` or `stamps`. Supported timestamp formats are FLOAT32 (seconds since header's timestamp) and UINT32 (nanoseconds since header's timestamp). If PointCloud2 input is organized, deskewing will be faster (transformed per columns instead per points). Note that for 2D LaserScan topic `scan`, it is deskewed only when `guess_frame_id` is used or `frame_id` is not the same frame than in the message. 
   }
  6{
   name = ~deskewing_slerp
   type = bool
   default = false
   desc = When enable, a lookup transform for TF will only be done for the first and last stamp, then points with in between timestamps will be deskewed by interpolating between the oldest and latest poses. This can be faster than the default approach looking for transform for very timestamps (though later approach would be more accurate).
   }
}
```
