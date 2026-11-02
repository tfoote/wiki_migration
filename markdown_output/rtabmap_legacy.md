

```wiki
'''''[[rtabmap_ros]]:''' [[rtabmap]] | [[rtabmap_conversions]] | [[rtabmap_costmap_plugins]] | [[rtabmap_demos]] | [[rtabmap_examples]] | [[rtabmap_launch]] | [[rtabmap_legacy]] | [[rtabmap_msgs]] | [[rtabmap_odom]] | [[rtabmap_python]] | [[rtabmap_rviz_plugins]] | [[rtabmap_slam]] | [[rtabmap_sync]] | [[rtabmap_util]] | [[rtabmap_viz]]''
```



## Nodes

### camera

A node for image acquisition from an USB camera (OpenCV is used). A
special option for this node is that it can be configured to read images
from a directory or a video file. Parameters can be changed with the
[dynamic_reconfigure](https://index.ros.org/p/dynamic_reconfigure) GUI
from ROS. For dynamic parameters, see
[Camera.cfg](https://github.com/introlab/rtabmap_ros/blob/master/rtabmap_legacy/cfg/Camera.cfg)



```clearsilver
pub {
  0.name = image
  0.type = sensor_msgs/Image
  0.desc = Image stream.
}

srv {
  0.name = stop_camera
  0.type = std_srvs/Empty
  0.desc = Stop the camera.
  1.name = start_camera
  1.type = rtabmap_msgs/ResetPose
  1.desc = Start the camera.
}

param {
  0.name = ~frame_id
  0.type = string
  0.default = `"camera"`
  0.desc = The frame attached to the camera.
}
```





```clearsilver
node {
  name = rtabmap_legacy/data_odom_sync
  desc = Synchronize odometry with RGB-D images. Useful to correctly show clouds in RVIZ when odometry refresh rate is low comparatively to clouds to show.
  sub {
    0.name = odom_in
    0.type = nav_msgs/Odometry
    0.desc = Odometry stream.
    1.name = rgb/image_in
    1.type = sensor_msgs/Image
    1.desc = RGB image stream.
    2.name = depth/image_in
    2.type = sensor_msgs/Image
    2.desc = Registered depth image stream.
    3.name = rgb/camera_info_in
    3.type = sensor_msgs/CameraInfo
    3.desc = RGB camera metadata.
  }
  pub {
    0.name = odom_out
    0.type = nav_msgs/Odometry
    0.desc = Odometry stream.
    1.name = rgb/image_out
    1.type = sensor_msgs/Image
    1.desc = RGB image stream.
    2.name = depth/image_out
    2.type = sensor_msgs/Image
    2.desc = Registered depth image stream.
    3.name = rgb/camera_info_out
    3.type = sensor_msgs/CameraInfo
    3.desc = RGB camera metadata.
  }
  param {
    0.name = ~queue_size
    0.type = int
    0.desc = Size of message queue for each synchronized topic.
    0.default = 10
  }
}
```





```clearsilver
node {
  name = rtabmap_legacy/data_throttle
  desc = Throttle at a specified rate the OpenNI data. See also [[rtabmap_sync#rgbd_sync|rtabmap_sync/rgbd_sync]], which is now preferred when publishing remotely.
  sub {
    0.name = rgb/image_in
    0.type = sensor_msgs/Image
    0.desc = RGB image stream.
    1.name = depth/image_in
    1.type = sensor_msgs/Image
    1.desc = Registered depth image stream.
    2.name = rgb/camera_info_in
    2.type = sensor_msgs/CameraInfo
    2.desc = RGB camera metadata.
  }
  pub {
    0.name = rgb/image_out
    0.type = sensor_msgs/Image
    0.desc = RGB image stream.
    1.name = depth/image_out
    1.type = sensor_msgs/Image
    1.desc = Registered depth image stream.
    2.name = rgb/camera_info_out
    2.type = sensor_msgs/CameraInfo
    2.desc = RGB camera metadata.
  }
  param {
    0.name = ~queue_size
    0.type = int
    0.desc = Size of message queue for each synchronized topic.
    0.default = 10
    1.name = ~rate
    1.type = double
    1.desc = Maximum frame rate (Hz).
    1.default = 0
    2.name = ~approx_sync
    2.type = bool
    2.desc = Use approximate synchronization for the input topics. If false, the RGB and depth images and the camera info must have the same timestamp.
    2.default = `"True"`
    3.name = ~decimation
    3.type = double
    3.desc = Optional decimation of the RGB and depth images (with corresponding modifications in `camera_info_out`).
    3.default = 1
  }
}
```





```clearsilver
node {
  name = rtabmap_legacy/stereo_throttle
  desc = Throttle at a specified rate the stereo data.
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
  }
  pub {
    0.name = [left/image_rect]_throttle
    0.type = sensor_msgs/Image
    0.desc = Left RGB/Mono rectified image.
    1.name = [left/camera_info]_throttle
    1.type = sensor_msgs/CameraInfo
    1.desc = Left camera metadata.
    2.name = [right/image_rect]_throttle
    2.type = sensor_msgs/Image
    2.desc = Right Mono rectified image.
    3.name = [right/camera_info]_throttle
    3.type = sensor_msgs/CameraInfo
    3.desc = Right camera metadata.
  }
  param {
    0.name = ~queue_size
    0.type = int
    0.desc = Size of message queue for each synchronized topic.
    0.default = 10
    1.name = ~rate
    1.type = double
    1.desc = Maximum frame rate (Hz).
    1.default = 0
    2.name = ~approx_sync
    2.type = bool
    2.default = `"false"`
    2.desc = Use approximate time synchronization of stereo messages. If false, the left/right images and the left/right camera infos must have the same timestamp.
    3.name = ~decimation
    3.type = double
    3.desc = Optional decimation of the left and right images (with corresponding modifications in camera infos).
    3.default = 1
  }
}
```
