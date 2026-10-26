# ROS OpenCV camera driver

It is very easy to capture video device if we use cv::VideoCapture of
OpenCV.

## cv_camera_node

This node uses camera_info_manager for dealing with camera_info. If no
calibration data is set, it has dummy values except for width and
height.

### Publish

- image_raw (sensor_msgs/Image)
- camera_info (sensor_msgs/CameraInfo)

### Service

- set_camera_info (sensor_msgs/SetCameraInfo)

### Parameters

- rate (double: default 30.0) publish rate \[Hz\].
- device_id (int: default 0) capture device id.
- frame_id (string: default "camera") frame_id of message header.
- image_width (int) try to set capture image width.
- image_height (int) try to set capture image height.
- camera_info_url (string) url of camera info yaml.
- file (string: default "") if not "" then use movie file instead of
  device.

### Usage



```
rosparam set cv_camera/device_id 0
rosrun cv_camera cv_camera_node
```



- with the first line set the camera device to use
- run the node with the second line

## Nodelet

This node works as nodelet (cv_camera/CvCameraNodelet).
