

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

#### Published Topics

- `image`
  ([sensor_msgs/msg/Image](https://docs.ros.org/en/rolling/p/sensor_msgs/msg/Image.html)):
  Image stream.

#### Services

- `stop_camera`
  ([std_srvs/srv/Empty](https://docs.ros.org/en/rolling/p/std_srvs/srv/Empty.html)):
  Stop the camera.
- `start_camera`
  ([rtabmap_msgs/srv/ResetPose](https://docs.ros.org/en/rolling/p/rtabmap_msgs/srv/ResetPose.html)):
  Start the camera.

#### Parameters

- `~frame_id` (`string`, default: `"camera"`): The frame attached to
  the camera.

### rtabmap_legacy/data_odom_sync

Synchronize odometry with RGB-D images. Useful to correctly show clouds
in RVIZ when odometry refresh rate is low comparatively to clouds to
show.

#### Subscribed Topics

- `odom_in`
  ([nav_msgs/msg/Odometry](https://docs.ros.org/en/rolling/p/nav_msgs/msg/Odometry.html)):
  Odometry stream.
- `rgb/image_in`
  ([sensor_msgs/msg/Image](https://docs.ros.org/en/rolling/p/sensor_msgs/msg/Image.html)):
  RGB image stream.
- `depth/image_in`
  ([sensor_msgs/msg/Image](https://docs.ros.org/en/rolling/p/sensor_msgs/msg/Image.html)):
  Registered depth image stream.
- `rgb/camera_info_in`
  ([sensor_msgs/msg/CameraInfo](https://docs.ros.org/en/rolling/p/sensor_msgs/msg/CameraInfo.html)):
  RGB camera metadata.

#### Published Topics

- `odom_out`
  ([nav_msgs/msg/Odometry](https://docs.ros.org/en/rolling/p/nav_msgs/msg/Odometry.html)):
  Odometry stream.
- `rgb/image_out`
  ([sensor_msgs/msg/Image](https://docs.ros.org/en/rolling/p/sensor_msgs/msg/Image.html)):
  RGB image stream.
- `depth/image_out`
  ([sensor_msgs/msg/Image](https://docs.ros.org/en/rolling/p/sensor_msgs/msg/Image.html)):
  Registered depth image stream.
- `rgb/camera_info_out`
  ([sensor_msgs/msg/CameraInfo](https://docs.ros.org/en/rolling/p/sensor_msgs/msg/CameraInfo.html)):
  RGB camera metadata.

#### Parameters

- `~queue_size` (`int`, default: `10`): Size of message queue for each
  synchronized topic.

### rtabmap_legacy/data_throttle

Throttle at a specified rate the OpenNI data. See also
[rtabmap_sync/rgbd_sync](https://index.ros.org/p/rtabmap_sync), which is
now preferred when publishing remotely.

#### Subscribed Topics

- `rgb/image_in`
  ([sensor_msgs/msg/Image](https://docs.ros.org/en/rolling/p/sensor_msgs/msg/Image.html)):
  RGB image stream.
- `depth/image_in`
  ([sensor_msgs/msg/Image](https://docs.ros.org/en/rolling/p/sensor_msgs/msg/Image.html)):
  Registered depth image stream.
- `rgb/camera_info_in`
  ([sensor_msgs/msg/CameraInfo](https://docs.ros.org/en/rolling/p/sensor_msgs/msg/CameraInfo.html)):
  RGB camera metadata.

#### Published Topics

- `rgb/image_out`
  ([sensor_msgs/msg/Image](https://docs.ros.org/en/rolling/p/sensor_msgs/msg/Image.html)):
  RGB image stream.
- `depth/image_out`
  ([sensor_msgs/msg/Image](https://docs.ros.org/en/rolling/p/sensor_msgs/msg/Image.html)):
  Registered depth image stream.
- `rgb/camera_info_out`
  ([sensor_msgs/msg/CameraInfo](https://docs.ros.org/en/rolling/p/sensor_msgs/msg/CameraInfo.html)):
  RGB camera metadata.

#### Parameters

- `~queue_size` (`int`, default: `10`): Size of message queue for each
  synchronized topic.
- `~rate` (`double`, default: `0`): Maximum frame rate (Hz).
- `~approx_sync` (`bool`, default: `"True"`): Use approximate
  synchronization for the input topics. If false, the RGB and depth
  images and the camera info must have the same timestamp.
- `~decimation` (`double`, default: `1`): Optional decimation of the RGB
  and depth images (with corresponding modifications in
  `camera_info_out`).

### rtabmap_legacy/stereo_throttle

Throttle at a specified rate the stereo data.

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

#### Published Topics

- `[left/image_rect]_throttle`
  ([sensor_msgs/msg/Image](https://docs.ros.org/en/rolling/p/sensor_msgs/msg/Image.html)):
  Left RGB/Mono rectified image.
- `[left/camera_info]_throttle`
  ([sensor_msgs/msg/CameraInfo](https://docs.ros.org/en/rolling/p/sensor_msgs/msg/CameraInfo.html)):
  Left camera metadata.
- `[right/image_rect]_throttle`
  ([sensor_msgs/msg/Image](https://docs.ros.org/en/rolling/p/sensor_msgs/msg/Image.html)):
  Right Mono rectified image.
- `[right/camera_info]_throttle`
  ([sensor_msgs/msg/CameraInfo](https://docs.ros.org/en/rolling/p/sensor_msgs/msg/CameraInfo.html)):
  Right camera metadata.

#### Parameters

- `~queue_size` (`int`, default: `10`): Size of message queue for each
  synchronized topic.
- `~rate` (`double`, default: `0`): Maximum frame rate (Hz).
- `~approx_sync` (`bool`, default: `"false"`): Use approximate time
  synchronization of stereo messages. If false, the left/right images
  and the left/right camera infos must have the same timestamp.
- `~decimation` (`double`, default: `1`): Optional decimation of the
  left and right images (with corresponding modifications in camera
  infos).
