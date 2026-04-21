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

```clearsilver
node.0 {
  name = image_publisher
  desc = Node to publish sensor_msgs/Image, requires filename argument.
  pub {
    0.name = image_raw
    0.type = sensor_msgs/Image
    0.desc = ROS Image message of your input file.
    1.name = camera_info
    1.type = sensor_msgs/CameraInfo
    1.desc = CameraInfo published along with Image
  }

  param {
    0.name = filename
    0.type = string
    0.default = ""
    0.desc = Name of image file to be published.
    1.name = flip_horizontal
    1.type = bool
    1.default = false
    1.desc = Flip output image horizontally.
    2.name = flip_vertical
    2.type = bool
    2.default = false
    2.desc = Flip output image vertically.
    3.name = frame_id
    3.type = string
    3.default = "camera"
    3.desc = Frame id inserted in published image and camera_info.
    4.name = publish_rate
    4.type = double
    4.default = 10
    4.desc = Rate to publish image (hz).
    5.name = camera_info_uri
    5.type = string
    5.default = ""
    5.desc = Path to camera info.
  }

}
```

## Nodelets

```clearsilver
node.0 {
  name = image_publisher/image_publisher
  desc = Nodelet to publish sensor_msgs/Image
  pub {
    0.name = image_raw
    0.type = sensor_msgs/Image
    0.desc = ROS Image message of your input file.
    1.name = camera_info
    1.type = sensor_msgs/CameraInfo
    1.desc = CameraInfo published along with Image
  }
  param {
    0.name = Same as image_publisher node
  }
```
