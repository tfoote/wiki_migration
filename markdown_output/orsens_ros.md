\<\<Include(orsens_ros/menu)\>\>
![OrSens camera\|align=\"right\",width=\"434\"](attachment:orsens_v1_1.png)

## Overview

This package is a ROS wrapper of
[SDK](https://github.com/Oriense/orsens) for
[OrSens](http://oriense.com) 3D-camera.

## Usage

[launch](https://github.com/Oriense/orsens_ros/blob/master/launch)
folder contains several files for different purposes:

-   [orsens.launch](https://github.com/Oriense/orsens_ros/blob/master/launch/orsens.launch) -
    basic launch
-   [orsens_stereo.launch](https://github.com/Oriense/orsens_ros/blob/master/launch/orsens_stereo.launch) -
    launch in stereo mode, for some ROS solutions, i.e. RTAB-Map stereo
    mapping and navigation.
-   [orsens_calibration.launch](https://github.com/Oriense/orsens_ros/blob/master/launch/orsens_calibration.launch) -
    launch ROS stereo calibration.

## Nodes

### orsens_node

Main node that publishes camera\'s data, as well as some results of
SDK\'s integrated CV functions.

```clearsilver

pub {
  0.name = disp
  0.type = sensor_msgs/Image
  0.desc = Disparity image, mono8, values in range 0-255, brighter is closer.
  1.name = depth
  1.type = sensor_msgs/Image
  1.desc = Depth image, 16UC1, values in millimetres.
  2.name = left/image_raw
  2.type = sensor_msgs/Image
  2.desc = Left RGB image, bgr8.
  3.name = left/camera_info
  3.type = sensor_msgs/CameraInfo
  3.desc = Left camera info.
  4.name = right/image_raw
  4.type = sensor_msgs/Image
  4.desc = Right RGB image, bgr8.
  5.name = right/camera_info
  5.type = sensor_msgs/CameraInfo
  5.desc = Right camera info.
  6.name = cloud
  6.type = pcl/PCLPointCloud2 
  6.desc = Point cloud.
  7.name = nearest_obstacle
  7.type = orsens/NearestObstacle
  7.desc = information about nearest obstacle: centre, width, height, direction from camera etc.
  8.name = segmentation_mask
  8.type = sensor_msgs/CameraInfo
  8.desc = Image mask which represents scene regions (currently floor only)
}

param {
  0.name = ~capture_mode
  0.type = string
  0.default = `"depth_only"`
  0.desc = Determines which data to capture from the camera. Possible values are `"depth_only"`- capture just depth stream, `"depth_left"` - capture both streams, `"left_only"` and `"left_right"`.
  1.name = ~data_path
  1.type = string
  1.default = `"data"`
  1.desc = Path to the data folder.
  2.name = ~left_camera_info_url
  2.type = string
  2.default = `"data_path/calibration/caminfo_left.yml"`
  2.desc = An url to the left camera calibration file that will be published as left/camera_info.
  3.name = ~right_camera_info_url
  3.type = string
  3.default = `"data_path/calibration/caminfo_right.yml"`
  3.desc = An url to the right camera calibration file that will be published as right/camera_info.
  4.name = ~frame_id
  4.type = string
  4.default = `"orsens_camera"`
  4.desc = The camera's tf frame.
  5.name = ~color_width
  5.type = int
  5.default = 640
  5.desc = Request to capture RGB stream with this image width.
  5.name = ~depth_width
  5.type = int
  5.default = 640
  5.desc = Same for depth stream.
  6.name = ~color_rate
  6.type = int
  6.default = 15
  6.desc = Request RGB stream framerate.
  7.name = ~depth_rate
  7.type = int
  7.default = 15
  7.desc = Request depth stream framerate.
  8.name = ~compress_color
  8.type = bool
  8.default = false
  8.desc = Request compressed RGB stream (may solve USB bandwidth problems).
  9.name = ~compress_depth
  9.type = bool
  9.default = false
  9.desc = Same for depth stream, but for future use, not working now.
  10.name = ~publish_depth
  10.type = bool
  10.default = true
  10.desc = Publish depth image.
  11.name = ~publish_cloud
  11.type = bool
  11.default = false
  11.desc = Publish pointcloud.
  12.name = ~publish_left_camera_info
  12.type = bool
  12.default = false
  12.desc = Publish left camera metadata.
  13.name = ~publish_right_camera_info
  13.type = bool
  13.default = false
  13.desc = Publish right camera metadata.
  14.name = ~publish_nearest_obstacle
  14.type = bool
  14.default = false
  14.desc = Publish information about nearest obstacle.
  15.name = ~publish_segmentation_mask
  15.type = bool
  15.default = false
  15.desc = Publish mask with scene regions.
}
```

## Demos

### Stereo visual odometry and mapping

[Youtube](https://www.youtube.com/watch?v=G-rsnz4bMZo)

### Running samples and ROS nodes

[Youtube](https://www.youtube.com/watch?v=91DyxcnwOBM)

### OrSens vs. two web-cameras with stereo-matching

[Youtube](https://www.youtube.com/watch?v=5-4dGjAnU8E)

## Calibration

1\. Camera\'s depth engine is precalibrated, but if you need to
recalibrate it for some reason, please contact us at
support@oriense-tech.com for instructions and software.

2\. To get ROS [CameraInfo](image_pipeline/CameraInfo) use
[camera calibration tool](camera_calibration) via
[this launch file](https://github.com/Oriense/orsens_ros/blob/master/launch/orsens_calibrate.launch).
