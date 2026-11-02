`depth_image_proc` has found a new home in
[image_pipeline](https://index.ros.org/p/image_pipeline). In Electric it
resided in [openni_kinect](openni_kinect).

## Overview

`depth_image_proc` provides basic processing for depth images, much as
[image_proc](https://index.ros.org/p/image_proc) does for traditional 2D
images. The two packages are complementary; for example, you can (and
should!) rectify your depth image before converting it to a point cloud.

A variety of camera technologies can produce depth images:

- The [Kinect](openni_kinect) and related devices
- Traditional stereo cameras
- Time-of-flight cameras

See [REP 118](http://www.ros.org/reps/rep-0118.html) for details on
depth image representation. The REP recommends that, wherever possible,
producers and consumers of depth data use depth images (of type
[sensor_msgs/msg/Image](https://docs.ros.org/en/rolling/p/sensor_msgs/msg/Image.html))
instead of
[sensor_msgs/msg/DisparityImage](https://docs.ros.org/en/rolling/p/sensor_msgs/msg/DisparityImage.html).

All nodelets (besides `convert_metric`) in this package support both
standard floating point depth images and OpenNI-specific `uint16`
depth images. Thus when working with OpenNI cameras (e.g. the Kinect),
you can save a few CPU cycles by using the `uint16` raw topics instead
of the `float` topics.

For an example of `depth_image_proc` in practice, examine the contents
of [openni_launch](https://index.ros.org/p/openni_launch).

## Nodelets

### depth_image_proc/convert_metric

Nodelet to convert raw `uint16` depth image in mm to `float` depth
image in m.

#### Subscribed Topics

- `image_raw`
  ([sensor_msgs/msg/Image](https://docs.ros.org/en/rolling/p/sensor_msgs/msg/Image.html)):
  `uint16` depth image in mm, the native OpenNI format.

#### Published Topics

- `image`
  ([sensor_msgs/msg/Image](https://docs.ros.org/en/rolling/p/sensor_msgs/msg/Image.html)):
  `float` depth image in m, the recommended format for processing in
  ROS.

### depth_image_proc/disparity

Nodelet to convert depth image to disparity image.

  -- ---------------------------------------------------------------------------------- -- ------------------------------------------------------------------------------------- --
     <tablestyle="width: 99%; text-align: center" style="width: 50%"> **Input**      **Output**                                                                            
     ![Depth](doc/depth.png)                                                               ![Disparity](doc/disparity.png)                                                       
     Depth image                                                                           Disparity image (colorized by [disparity_view](https://index.ros.org/p/image_view))   
  -- ---------------------------------------------------------------------------------- -- ------------------------------------------------------------------------------------- --

#### Subscribed Topics

- `left/image_rect`
  ([sensor_msgs/msg/Image](https://docs.ros.org/en/rolling/p/sensor_msgs/msg/Image.html)):
  Rectified depth image.
- `right/camera_info`
  ([sensor_msgs/msg/CameraInfo](https://docs.ros.org/en/rolling/p/sensor_msgs/msg/CameraInfo.html)):
  Camera calibration and metadata. Must contain the baseline, which
  conventionally is encoded in the right camera P matrix.

#### Published Topics

- `left/disparity`
  ([stereo_msgs/msg/DisparityImage](https://docs.ros.org/en/rolling/p/stereo_msgs/msg/DisparityImage.html)):
  Disparity image (inversely related to depth), for interop with stereo
  processing nodes. For all other purposes use depth images instead.

#### Parameters

- `min_range` (`double`, default: `0.0`): Minimum detectable distance.
- `max_range` (`double`, default: `+Inf`): Maximum detectable distance.
- `delta_d` (`double`, default: `0.125`): Smallest allowed disparity
  increment, which relates to the achievable depth range resolution.
  Defaults to 1/8 pixel.
- `queue_size` (`int`, default: `5`): Size of message queue for
  synchronizing subscribed topics.

### depth_image_proc/point_cloud_xyz

Nodelet to convert depth image to XYZ point cloud.

  -- ---------------------------------------------------------------------------------- -- ------------------------------------------------- --
     <tablestyle="width: 99%; text-align: center" style="width: 46%"> **Input**      **Output**                                        
     ![Depth](doc/depth.png)                                                               ![Point cloud](doc/rviz_xyz.png)                  
     Depth image                                                                           Point cloud, colorized by distance along Z-axis   
  -- ---------------------------------------------------------------------------------- -- ------------------------------------------------- --

#### Subscribed Topics

- `camera_info`
  ([sensor_msgs/msg/CameraInfo](https://docs.ros.org/en/rolling/p/sensor_msgs/msg/CameraInfo.html)):
  Camera calibration and metadata.
- `image_rect`
  ([sensor_msgs/msg/Image](https://docs.ros.org/en/rolling/p/sensor_msgs/msg/Image.html)):
  Rectified depth image.

#### Published Topics

- `points`
  ([sensor_msgs/msg/PointCloud2](https://docs.ros.org/en/rolling/p/sensor_msgs/msg/PointCloud2.html)):
  XYZ point cloud. If using [PCL](https://index.ros.org/p/pcl_ros),
  subscribe as `PointCloud<PointXYZ>`.

#### Parameters

- `queue_size` (`int`, default: `5`): Size of message queue for
  synchronizing subscribed topics.

### depth_image_proc/point_cloud_xyzrgb

Nodelet to combine registered depth image and RGB image into XYZRGB
point cloud.

  -- ---------------------------------------------------------------------------------- -- ------------------- ----------------------------------------- --
     <tablestyle="width: 99%; text-align: center" style="width: 40%"> **Input**      **Output**                                                    
     ![Depth](doc/depth_reg.png)                                                           <                  3> ![Point cloud](doc/rviz_xyzrgb.png)   
     Registered depth image                                                                                                                              
     ![RGB](doc/rgb.jpg)                                                                                                                                 
     RGB image                                                                             Color point cloud                                             
  -- ---------------------------------------------------------------------------------- -- ------------------- ----------------------------------------- --

#### Subscribed Topics

- `rgb/camera_info`
  ([sensor_msgs/msg/CameraInfo](https://docs.ros.org/en/rolling/p/sensor_msgs/msg/CameraInfo.html)):
  Camera calibration and metadata.
- `rgb/image_rect_color`
  ([sensor_msgs/msg/Image](https://docs.ros.org/en/rolling/p/sensor_msgs/msg/Image.html)):
  Rectified color image.
- `depth_registered/image_rect`
  ([sensor_msgs/msg/Image](https://docs.ros.org/en/rolling/p/sensor_msgs/msg/Image.html)):
  Rectified depth image, registered to the RGB camera.

#### Published Topics

- `depth_registered/points`
  ([sensor_msgs/msg/PointCloud2](https://docs.ros.org/en/rolling/p/sensor_msgs/msg/PointCloud2.html)):
  XYZRGB point cloud. If using [PCL](https://index.ros.org/p/pcl_ros),
  subscribe as `PointCloud<PointXYZRGB>`.

#### Parameters

- `queue_size` (`int`, default: `5`): Size of message queue for
  synchronizing subscribed topics.

### depth_image_proc/register

Nodelet to "register" a depth image to another camera frame.
Reprojecting the depths requires the calibration parameters of both
cameras and, from [tf](https://index.ros.org/p/tf), the extrinsic
transform between them.

  -- ---------------------------------------------------------------------------------- -- -------------------------------------------------------- --
     <tablestyle="width: 99%; text-align: center" style="width: 50%"> **Input**      **Output**                                               
     ![Depth](doc/depth.png)                                                               ![Registered depth](doc/depth_reg.png)                   
     Depth image as captured by depth sensor                                               Depth image registered to frame of separate RGB camera   
  -- ---------------------------------------------------------------------------------- -- -------------------------------------------------------- --

#### Subscribed Topics

- `rgb/camera_info`
  ([sensor_msgs/msg/CameraInfo](https://docs.ros.org/en/rolling/p/sensor_msgs/msg/CameraInfo.html)):
  RGB camera calibration and metadata.
- `depth/camera_info`
  ([sensor_msgs/msg/CameraInfo](https://docs.ros.org/en/rolling/p/sensor_msgs/msg/CameraInfo.html)):
  Depth camera calibration and metadata.
- `depth/image_rect`
  ([sensor_msgs/msg/Image](https://docs.ros.org/en/rolling/p/sensor_msgs/msg/Image.html)):
  Rectified depth image.

#### Published Topics

- `depth_registered/camera_info`
  ([sensor_msgs/msg/CameraInfo](https://docs.ros.org/en/rolling/p/sensor_msgs/msg/CameraInfo.html)):
  Camera calibration and metadata. Same as `rgb/camera_info` but
  time-synced to `depth_registered/image_rect`.
- `depth_registered/image_rect`
  ([sensor_msgs/msg/Image](https://docs.ros.org/en/rolling/p/sensor_msgs/msg/Image.html)):
  Reprojected depth image in the RGB camera frame.

#### Parameters

- `queue_size` (`int`, default: `5`): Size of message queue for
  synchronizing subscribed topics.

#### Required tf Transforms

- `/depth_optical_frame` → `/rgb_optical_frame`: The transform between
  the depth and RGB camera optical frames as specified in the headers of
  the subscribed topics (rendered here as `/depth_optical_frame` and
  `/rgb_optical_frame`).

## Execution

Since the package is made of 'nodelet's, 'nodelet' execution method
is used as:
<http://wiki.ros.org/nodelet/Tutorials/Running%20a%20nodelet>

For example, the launch file to execute a 'point_cloud_xyz' nodelet is
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
