- ROS2 repository: <https://github.com/nerian-vision/nerian_stereo_ros2>

## Introduction

![](https://nerian.com/nerian-images/scarlet-ros-wiki.jpg)

Nerian's
[Scarlet](https://nerian.com/products/scarlet-3d-depth-camera/) and
[SceneScan](https://nerian.com/products/scenescan-stereo-vision/)
product lines are stereo vision based 3D imaging systems for real-time
3d sensing. While Scarlet is a fully integrated unit with image sensors
and image processing in one device, SceneScan connects to two industrial
USB cameras that provide input image data. Both devices correlate the
images of both cameras / sensors and produce a disparity map, which is
transmitted through gigabit Ethernet. The disparity map describes a
mapping of image points from the left camera image to corresponding
image points in the right camera image. With this information it is
possible to reconstruct the 3D location of every observed scene points.

------------------------------------------------------------------------

**Please note: since version 3.0.0 this node is no longer compatible to
SP1 -- the predecessor of SceneScan. Please use an older version with
SP1 or the now discontinued [nerian_sp1](nerian_sp1) node**

------------------------------------------------------------------------

[Youtube](https://www.youtube.com/watch?v=mJ5UlXNguvg)

## Installation on ROS1 and ROS2

On Ubuntu Linux, please use the following commands to install the
official package for your current ROS version.



```
sudo apt-get update
sudo apt-get install ros-`rosversion -d`-nerian-stereo
```

 These commands work for both, ROS1 and ROS2
distributions.

Should there not be an appropriate package for your system and ROS
version, please checkout the git repository and compile the code using
catkin/colcon.

## ROS Node

The data delivered by Scarlet / SceneScan can be received using the
available open source API. Using the API directly is recommended for
high performance applications with ROS1. Alternatively the
`nerian_stereo` ROS node can be used for publishing the received data as
ROS messages. A Nodelet version is also provided for ROS1.

![](https://nerian.com/nerian-images/ros-rviz.png)

### Published Topics

The node can publish the received data through three different topics:



```clearsilver

pub {
  no_header=True
  0.name = /nerian_stereo/point_cloud
  0.type = sensor_msgs/PointCloud2
  0.desc = A point cloud, which is obtained by reconstructing the 3D location of each pixel in the disparity map. Optionally, the point cloud can include an intensity channel, which contains intensity data from the left rectified camera image.

  1.name = /nerian_stereo/disparity_map
  1.type = sensor_msgs/Image
  1.desc = The stereo disparity map that is computed by SceneScan. The disparity map is transmitted as an image message with mono16 encoding. Please note that the disparity map has a 4-bit subpixel resolution. This means that its values have to be divided by 16 in order to receive the true pixel disparity. Optionally, the disparity map can be color coded for visualization. In this case the encoding will be bgr8.

  2.name = /nerian_stereo/left_image
  2.type = sensor_msgs/Image
  2.desc = The rectified image of the left camera with mono8 or mono12 encoding, if SceneScan is configured in stereo matching or rectify mode. If the device is configured in pass-through mode the unrectified left camera image will be published through this topic.

  3.name = /nerian_stereo/right_image
  3.type = sensor_msgs/Image
  3.desc = If the SceneScan is configured in pass-through or rectify mode, then the (un)rectified right camera image will be published through this topic in mono8 encoding

  4.name = /nerian_stereo/stereo_camera_info
  4.type = nerian_stereo/StereoCameraInfo
  4.desc = Camera calibration information for both cameras.
}
```



### Launching and parameters

Example launch files are included for the ROS1 node and nodelet and for
ROS2. You can run several nodes in parallel if you use more than one
device, specifying the respective device address and a desired ROS node
name in case of ROS1:



```
# For ROS1:
roslaunch nerian_stereo nerian_stereo.launch device_address:=192.168.10.10 node_name:=nerian_stereo_01

# For ROS2:
ros2 launch nerian_stereo nerian_stereo.launch.py
```



The behaviour of the node can be configured through various parameters.
An example parameterization can be found in the included launch file
`nerian_stereo.launch`. The following parameters are supported:



```clearsilver

param {
  no_header=True
  0.name = ~point_cloud_intensity_channel
  0.type = string
  0.default = `"mono8"`
  0.desc = Specifies if and how the intensity channel is encoded in the published point cloud. Available options are: none, mono8, rgb8, rgb32f.

  1.name = ~ros_coordinate_system
  1.type = bool
  1.default = `"true"`
  1.desc = If enabled, the typical ROS coordinate system is used, with the x-axis pointing forward, the y-axis pointing left and the z-axis pointing upwards. If disabled, SceneScan's default coordinate system is used, with the x-axis pointing right, the y-axis pointing downwards, and the z-axis pointing forward.

  2.name = ~ros_timestamps
  2.type = bool
  2.default = `"true"`
  2.desc = If enabled, the ROS system time will be used for timestamping the generated messages. If disabled, the timestamp transmitted by SceneScan will be used for all messages that carry sensor data. When using timestamps from SceneScan, it should be ensured that SceneScan is synchronizing its clock to an external reference .

  3.name = ~color_code_disparity_map
  3.type = string
  3.default = `"none"`
  3.desc = Selects the color scale for color coding of the disparity map. Possible values are "none", "rainbow" and "red_blue".

  4.name = ~color_code_legend
  4.type = bool
  4.default = `"true"`
  4.desc = If enabled, a legend will be added to the color coded disparity map.

  5.name = ~frame
  5.type = string
  5.default = `"world"`
  5.desc = ID of the frame that will be set for all transmitted messages.

  6.name = ~remote_host
  6.type = string
  6.default = `"0.0.0.0"`
  6.desc = Host name or IP address of SceneScan, which is used for network communication.

  7.name = ~remote_port
  7.type = string
  7.default = `"7681"`
  7.desc = Remote port number or service name that is used for network communicating with SceneScan.

  8.name = ~use_tcp
  8.type = bool
  8.default = `"false"`
  8.desc = If enabled, TCP is used rather than UDP as underlying network protocol.

  9.name = ~calibration_file
  9.type = string
  9.default = `""`
  9.desc = Location of a YAML-file containing camera calibration data. This file can be obtained from the SceneScan webinterface. An example calibration file is provided in the repository. If this parameter is omitted, the published camera calibration information only contains the q-Matrix.

  10.name = ~delay_execution
  10.type = double
  10.default = `0`
  10.desc = Allows the configuration of an initial delay in seconds when launching the node. This option can be used to delay the node launch while the calibration information is downloaded.

  11.name = ~max_depth
  11.type = double
  11.default = `-1`
  11.desc = If set to a positive value, all points in the point cloud with a higher depth will be set to invalid.
}
```



### Testing

The topics published by the nerian_stereo node can be viewed with
[rviz](rviz). The disparity map can also be visualized with the
[image_view](image_view) node in ROS1 or showimage from ROS2. To do so,
use can use one of the following commands:



```
# For ROS1:
rosrun image_view image_view image:=/nerian_stereo/disparity_map

# For ROS2:
ros2 run image_tools showimage image:=/nerian_stereo/disparity_map
```



In this case color coding should be activated such that the disparity
map can be displayed on a screen.

![](https://nerian.com/nerian-images/image_view.jpg)

For displaying the left camera image, please run the image_view node
with the following command line:



```
#For ROS1:
rosrun image_view image_view image:=/nerian_stereo/left_image

#For ROS2:
ros2 run image_tools showimage image:=/nerian_stereo/left_image
```



### Dynamic reconfiguration in ROS1

At launch time, the ROS1 node (and nodelet) publishes the current
configuration reported by the respective device to the ROS parameter
server, and can be reconfigured at run time using ROS
dynamic_reconfigure, for example using the GUI:



```
rosrun rqt_reconfigure rqt_reconfigure
```



## Further Information

- [Scarlet product page](https://nerian.com/products/scarlet-3d-depth-camera/)
- [SceneScan product page](https://nerian.com/products/scenescan-stereo-vision/)
- [Github project page](https://github.com/nerian-vision/nerian_stereo)
- [API documentation](https://nerian.com/support/documentation/api-doc/html/index.html)

![\|display="none ! important",hidden=""](http://c.statcounter.com/10599048/0/906ae443/1/)
