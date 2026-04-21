## Overview

The package laserscan_kinect converts depth image to laser scan
(<<MsgLink(sensor_msgs/LaserScan)>>). It allows to use RGB-D sensor
(for example Microsoft Kinect) for navigation purposes. Package
laserscan_kinect finds the smallest value of distance in each column of
the depth image and converts it to polar coordinates.

Moreover, the package provides features like a ground removing from the
scan and a sensor tilt compensation in distance values, but it is
necessary to know a height of sensor optical center and a tilt angle in
the frame of ground.

### Example

![](attachment:laserscan_kinect_detection.jpg) The picture shows a
comparison between the laser scan based on converted depth image from
Microsoft Kinect (blue points) and a laser scan from the scanner Hokuyo
URG-04LX-UG01 (black points). Moreover, the picture contains the RBG
image and the depth image.

### Tuning

During the tuning process additional debug image can be used. It
contains lines that represent the lower and upper bounds of the
detection area. Also, closest points in each image column are visible.
![](attachment:laserscan_kinect_dbg.png)

## Usage

The file /config/params.yaml contains example parameters values. To
start the node laserscan_kinect it can be used a following file
/launch/laserscan.launch .

## Node



```clearsilver
name = laserscan_kinect
desc = 
sub {
  0.name = image
  0.type = sensor_msgs/Image
  0.desc = Depth image which will be converted to laserscan.
  1.name = camera_info
  1.type = sensor_msgs/CameraInfo
  1.desc = Additional information about the depth sensor.
}
pub {
  0.name = /scan
  0.type = sensor_msgs/LaserScan
  0.desc = Converted depthimage. It contains information about the robot surrounding in a planar scan.
  1.name = /debug_image
  1.type = sensor_msgs/Image
  1.desc = Debug image used during the tuning process.
}
param {
  0.name = ~output_frame_id
  0.type = str
  0.desc = Frame id for the output laserscan message.
  0.default = camera_depth_frame
  1.name = ~range_min
  1.type = double
  1.desc = Minimum sensor range (in meters). Pixels in the depth image with values smaller than this parameter are ignored during the processing.
  1.default = 0.5
  2.name = ~range_max
  2.type = double
  2.desc = Maximum sensor range (in meters). Pixels in the depth image with values greater than this parameter are ignored during the processing.
  2.default = 5.0
  3.name = ~depth_img_row_step
  3.type = int
  3.desc = Row step in the depth image processing. By increasing this parameter the computational complexity of the algorithm is decreased but some of data are losted.
  3.default = 2
  4.name = ~scan_height
  4.type = int
  4.desc = Height of used part of the depth image (in pixels).
  4.default = 440
  5.name = ~cam_model_update
  5.type = bool
  5.desc = Determines if continuously camera model data update is necessary. If it's true, then camera model (<<MsgLink(sensor_msgs/CameraInfo)>>) from topic camera_info is updated with each new depth image message. Otherwise, the camera model and parameters associated with it are updated only at the beginning of the node or when the node parameter is changed by dynamic_reconfigure.
  5.default = false
  6.name = ~ground_remove_en
  6.type = bool
  6.desc = Determines if a ground removal from the output scan feature is enabled. The ground removal method to work needs correctly defined values of parameters like a sensor_tilt_angle and sensor_mount_height.
  6.default = false
  7.name = ~sensor_mount_height
  7.type = double
  7.desc = Height of the depth sensor optical center mount (in meters). Parameter is necessary for the ground removal feature. It should be measured from the ground to the optical center of the depth sensor.
  7.default = 0.4
  8.name = ~sensor_tilt_angle
  8.type = double
  8.desc = Depth sensor tilt angle (in degrees). If the sensor is leaning towards the ground the tilt angle should be positive. Otherwise, the value of the angle should be negative.
  8.default = 0.0
  9.name = ~ground_margin
  9.type = double
  9.desc = Margin in the ground removal feature (in meters).
  9.default = 0.05
  10.name = ~tilt_compensation_en
  10.type = bool
  10.desc = Parameter determines if sensor tilt angle compensation is enabled.
  10.default = false
  11.name = ~publish_dbg_info
  11.type = bool
  11.desc = Publish a debug image that can be used during the parameters tuning process.
  11.default = true
}
```



## Report a Bug
