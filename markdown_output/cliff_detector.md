## Overview

The package cliff_detector detects negative obstacles like a cliff or
downstairs based on depth image. It is necessary to define height and
tilt angle of depth sensor. It was tested with Microsoft Kinect v1 and
v2 sensors.

## Usage

The file /config/params.yaml constains example parameters values. To
start node cliff_detector can be used a following file
/launch/cliff_detector.launch .

## Node



```clearsilver
name = cliff_detector
desc =
sub {
  0.name = image
  0.type = sensor_msgs/Image
  1.name = camera_info
  1.type = sensor_msgs/CameraInfo
}
pub {
  0.name = /cliff_points
  0.type = depth_nav_msgs/Point32List
}
param {
  0.name = ~range_min
  0.type = double
  0.desc = Minimum sensor range (in meters). Pixels in depth image with values smaller  than this parameter are ignored in processing.
  0.default = 0.5
  1.name = ~range_max
  1.type = double
  1.desc = Maximum sensor range (in meters). Pixels in depth image with values greater  than this parameter are ignored in processing.
  1.default = 5.0
  2.name = ~depth_img_row_step
  2.type = int
  2.desc = Row step in depth image processing. Increasing this parameter we decrease computational complexity of algorithm but some of data are losted.
  2.default = 2
  3.name = ~scan_height
  3.type = int
  3.desc = Height of used part of depth image (in pixels).
  3.default = 440
  4.name = ~cam_model_update
  4.type = bool
  4.desc = Determines if continuously camera model data update is neccessary. If it is true, then camera model (<<MsgLink(sensor_msgs/CameraInfo)>>) from topic camera_info is updated with each new depth image message. Otherwise, camera model and parameters associated with it are updated only at the start of node or when node parameter are changed by dynamic_reconfigure.
  4.default = false
  5.name = ~sensor_mount_height
  5.type = double
  5.desc = Height of depth sensor optical center mount (in meters). Parameter is necessary for ground removing featrue. It should be measured from ground to depth sensor optical center.
  5.default = 0.4
  6.name = ~sensor_tilt_angle
  6.type = double
  6.desc = Depth sensor tilt angle (in degrees). If the sensor is leaning towards the ground the tilt angle should be positive. Otherwise, the value of angle should be negative.
  6.default = 0.0
  7.name = ~ground_margin
  7.type = double
  7.desc = Margin in ground removing feature (in meters).
  7.default = 0.05
}
```



## Report a Bug
