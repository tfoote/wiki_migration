\`depth_image_proc\` has found a new home in
[image_pipeline](image_pipeline). In Electric it resided in
[openni_kinect](openni_kinect).

## Overview

\`depth_image_proc\` provides basic processing for depth images, much as
[image_proc](image_proc) does for traditional 2D images. The two
packages are complementary; for example, you can (and should!) rectify
your depth image before converting it to a point cloud.

A variety of camera technologies can produce depth images:

-   The [Kinect](openni_kinect) and related devices
-   Traditional stereo cameras
-   Time-of-flight cameras

See [REP 118](http://www.ros.org/reps/rep-0118.html) for details on
depth image representation. The REP recommends that, wherever possible,
producers and consumers of depth data use depth images (of type
\<\<MsgLink(sensor_msgs/Image)\>\>) instead of
\<\<MsgLink(sensor_msgs/DisparityImage)\>\>.

All nodelets (besides \`convert_metric\`) in this package support both
standard floating point depth images and OpenNI-specific \`uint16\`
depth images. Thus when working with OpenNI cameras (e.g. the Kinect),
you can save a few CPU cycles by using the \`uint16\` raw topics instead
of the \`float\` topics.

For an example of \`depth_image_proc\` in practice, examine the contents
of [openni_launch](openni_launch).

## Nodelets

```clearsilver
node.0 {
  name = depth_image_proc/convert_metric
  desc = Nodelet to convert raw `uint16` depth image in mm to `float` depth image in m.
  sub {
    0.name = image_raw
    0.type = sensor_msgs/Image
    0.desc = `uint16` depth image in mm, the native OpenNI format.
  }
  pub {
    0.name = image
    0.type = sensor_msgs/Image
    0.desc = `float` depth image in m, the recommended format for processing in ROS.
  }
}
node.1 {
  name = depth_image_proc/disparity
  desc = Nodelet to convert depth image to disparity image.
}
```

  -- ------------------------------------------------------------------------------------------ -- ------------------------------------------------------------- --
     \<tablestyle=\"width: 99%; text-align: center\" style=\"width: 50%\"\> \'\'\'Input\'\'\'      \'\'\'Output\'\'\'                                            
     ![Depth\|width=100%](attachment:depth.png)                                                    ![Disparity\|width=100%](attachment:disparity.png)            
     Depth image                                                                                   Disparity image (colorized by [disparity_view](image_view))   
  -- ------------------------------------------------------------------------------------------ -- ------------------------------------------------------------- --

```clearsilver
  sub {
    0.name = left/image_rect
    0.type = sensor_msgs/Image
    0.desc = Rectified depth image.
    1.name = right/camera_info
    1.type = sensor_msgs/CameraInfo
    1.desc = Camera calibration and metadata. Must contain the baseline, which conventionally is encoded in the right camera P matrix.
  }
  pub {
    0.name = left/disparity
    0.type = stereo_msgs/DisparityImage
    0.desc = Disparity image (inversely related to depth), for interop with stereo processing nodes. For all other purposes use depth images instead.
  }
  param {
    0.name = min_range
    0.type = double
    0.default = 0.0
    0.desc = Minimum detectable distance.
    1.name = max_range
    1.type = double
    1.default = +Inf
    1.desc = Maximum detectable distance.
    2.name = delta_d
    2.type = double
    2.default = 0.125
    2.desc = Smallest allowed disparity increment, which relates to the achievable depth range resolution. Defaults to 1/8 pixel.
    3.name = queue_size
    3.type = int
    3.default = 5
    3.desc = Size of message queue for synchronizing subscribed topics.
  }
```

```clearsilver
node.2 {
  name = depth_image_proc/point_cloud_xyz
  desc = Nodelet to convert depth image to XYZ point cloud.
}
```

  -- ------------------------------------------------------------------------------------------ -- ----------------------------------------------------- --
     \<tablestyle=\"width: 99%; text-align: center\" style=\"width: 46%\"\> \'\'\'Input\'\'\'      \'\'\'Output\'\'\'                                    
     ![Depth\|width=100%](attachment:depth.png)                                                    ![Point cloud\|width=100%](attachment:rviz_xyz.png)   
     Depth image                                                                                   Point cloud, colorized by distance along Z-axis       
  -- ------------------------------------------------------------------------------------------ -- ----------------------------------------------------- --

```clearsilver
  sub {
    0.name = camera_info
    0.type = sensor_msgs/CameraInfo
    0.desc = Camera calibration and metadata.
    1.name = image_rect
    1.type = sensor_msgs/Image
    1.desc = Rectified depth image.
  }
  pub {
    0.name = points
    0.type = sensor_msgs/PointCloud2
    0.desc = XYZ point cloud. If using [[pcl_ros|PCL]], subscribe as `PointCloud<PointXYZ>`.
  }
  param {
    0.name = queue_size
    0.type = int
    0.default = 5
    0.desc = Size of message queue for synchronizing subscribed topics.
  }
```

```clearsilver
node.3 {
  name = depth_image_proc/point_cloud_xyzrgb
  desc = Nodelet to combine registered depth image and RGB image into XYZRGB point cloud.
}
```

  -- ------------------------------------------------------------------------------------------ -- -------------------- ------------------------------------------------------------ --
     \<tablestyle=\"width: 99%; text-align: center\" style=\"width: 40%\"\> \'\'\'Input\'\'\'      \'\'\'Output\'\'\'                                                                
     ![Depth\|width=100%](attachment:depth_reg.png)                                                \<                   3\> ![Point cloud\|width=100%](attachment:rviz_xyzrgb.png)   
     Registered depth image                                                                                                                                                          
     ![RGB\|width=100%](attachment:rgb.jpg)                                                                                                                                          
     RGB image                                                                                     Color point cloud                                                                 
  -- ------------------------------------------------------------------------------------------ -- -------------------- ------------------------------------------------------------ --

```clearsilver
  sub {
    0.name = rgb/camera_info
    0.type = sensor_msgs/CameraInfo
    0.desc = Camera calibration and metadata.
    1.name = rgb/image_rect_color
    1.type = sensor_msgs/Image
    1.desc = Rectified color image.
    2.name = depth_registered/image_rect
    2.type = sensor_msgs/Image
    2.desc = Rectified depth image, registered to the RGB camera.
  }
  pub {
    0.name = depth_registered/points
    0.type = sensor_msgs/PointCloud2
    0.desc = XYZRGB point cloud. If using [[pcl_ros|PCL]], subscribe as `PointCloud<PointXYZRGB>`.
  }
  param {
    0.name = queue_size
    0.type = int
    0.default = 5
    0.desc = Size of message queue for synchronizing subscribed topics.
  }
```

```clearsilver
node.4 {
  name = depth_image_proc/register
  desc = Nodelet to "register" a depth image to another camera frame. Reprojecting the depths requires the calibration parameters of both cameras and, from [[tf]], the extrinsic transform between them.
}
```

  -- ------------------------------------------------------------------------------------------ -- ----------------------------------------------------------- --
     \<tablestyle=\"width: 99%; text-align: center\" style=\"width: 50%\"\> \'\'\'Input\'\'\'      \'\'\'Output\'\'\'                                          
     ![Depth\|width=100%](attachment:depth.png)                                                    ![Registered depth\|width=100%](attachment:depth_reg.png)   
     Depth image as captured by depth sensor                                                       Depth image registered to frame of separate RGB camera      
  -- ------------------------------------------------------------------------------------------ -- ----------------------------------------------------------- --

```clearsilver
  sub {
    0.name = rgb/camera_info
    0.type = sensor_msgs/CameraInfo
    0.desc = RGB camera calibration and metadata.
    1.name = depth/camera_info
    1.type = sensor_msgs/CameraInfo
    1.desc = Depth camera calibration and metadata.
    2.name = depth/image_rect
    2.type = sensor_msgs/Image
    2.desc = Rectified depth image.
  }
  pub {
    0.name = depth_registered/camera_info
    0.type = sensor_msgs/CameraInfo
    0.desc = Camera calibration and metadata. Same as `rgb/camera_info` but time-synced to `depth_registered/image_rect`.
    1.name = depth_registered/image_rect
    1.type = sensor_msgs/Image
    1.desc = Reprojected depth image in the RGB camera frame.
  }
  param {
    0.name = queue_size
    0.type = int
    0.default = 5
    0.desc = Size of message queue for synchronizing subscribed topics.
  }
  req_tf {
    0.from = /depth_optical_frame
    0.to = /rgb_optical_frame
    0.desc = The transform between the depth and RGB camera optical frames as specified in the headers of the subscribed topics (rendered here as `/depth_optical_frame` and `/rgb_optical_frame`).
  }
```

## Execution

Since the package is made of \'nodelet\'s, \'nodelet\' execution method
is used as:
<http://wiki.ros.org/nodelet/Tutorials/Running%20a%20nodelet>

For example, the launch file to execute a \'point_cloud_xyz\' nodelet is
like as:

```
<launch>
  <node pkg="nodelet" type="nodelet" name="nodelet_manager" args="manager" />

  <node pkg="nodelet" type="nodelet" name="nodelet1"
        args="load depth_image_proc/point_cloud_xyz nodelet_manager">
    <remap from="camera_info" to="/camera/depth/camera_info"/>
    <remap from="image_rect" to="/camera/depth/image_rect_raw"/>
    <remap from="points" to="/camera/depth/points"/>
  </node>
</launch>
```
