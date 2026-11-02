## Overview

`image_publisher` provides a node/nodelets for publishing image as a
ROS image topic.

Simplest example are



```
rosrun image_publisher image_publisher /opt/ros/indigo/share/rviz/images/splash.png
```



Complex launchfile example



```
<launch>                                                                        
  <node pkg="image_publisher" type="image_publisher" name="image_publisher"
        args="$(find rviz)/images/splash.png" >
    <param name="flip_horizontal" value="false" />
    <param name="flip_vertical" value="false" />
    <param name="frame_id" value="my_camera" />
    <param name="publish_rate" value="1" />
    <param name="camera_info_url" value="file:///$(env HOME)/.ros/camera_info/camera.yaml" />   <!-- relative to ~/.ros/ -->
  </node>
</launch>
```



More complex nodelet example using launch file



```
<launch>                                                                        
  <node pkg="nodelet" type="nodelet" name="manager" args="manager"/>

  <node pkg="nodelet" type="nodelet" name="image_publisher"
        args="load image_publisher/image_publisher manager">
    <param name="filename" value="$(find rviz)/images/splash.png" />
    <param name="flip_horizontal" value="false" />
    <param name="flip_vertical" value="false" />
  </node>
  <param name="/manager/frame_id" value="my_camera" />
  <param name="/manager/publish_rate" value="1" />
  <param name="camera_info_url" value="file:///$(env HOME)/.ros/camera_info/camera.yaml" />  <!-- relative to ~/.ros/ -->
</launch>
```



## Node

### image_publisher

Node to publish sensor_msgs/Image, requires filename argument.

#### Published Topics

- `image_raw`
  ([sensor_msgs/msg/Image](https://docs.ros.org/en/rolling/p/sensor_msgs/msg/Image.html)):
  ROS Image message of your input file.
- `camera_info`
  ([sensor_msgs/msg/CameraInfo](https://docs.ros.org/en/rolling/p/sensor_msgs/msg/CameraInfo.html)):
  CameraInfo published along with Image

#### Parameters

- `filename` (`string`, default: `""`): Name of image file to be
  published.
- `flip_horizontal` (`bool`, default: `false`): Flip output image
  horizontally.
- `flip_vertical` (`bool`, default: `false`): Flip output image
  vertically.
- `frame_id` (`string`, default: `"camera"`): Frame id inserted in
  published image and camera_info.
- `publish_rate` (`double`, default: `10`): Rate to publish image (hz).
- `camera_info_uri` (`string`, default: `""`): Path to camera info.

## Nodelets

### image_publisher/image_publisher

Nodelet to publish sensor_msgs/Image

#### Published Topics

- `image_raw`
  ([sensor_msgs/msg/Image](https://docs.ros.org/en/rolling/p/sensor_msgs/msg/Image.html)):
  ROS Image message of your input file.
- `camera_info`
  ([sensor_msgs/msg/CameraInfo](https://docs.ros.org/en/rolling/p/sensor_msgs/msg/CameraInfo.html)):
  CameraInfo published along with Image

#### Parameters

- `Same as image_publisher node`
