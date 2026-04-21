------------------------------------------------------------------------

**Please note: This package has been superseeded by
[nerian_stereo](nerian_stereo)**

------------------------------------------------------------------------

## Introduction

The
[SP1 stereo vision sensor](http://nerian.com/products/sp1-stereo-vision/)
by Nerian Vision Technologies is a stand-alone processing system for
performing stereo matching in real time. It is connected to two
industrial USB cameras that provide input image data. The SP1 correlates
the images of both cameras and produces a disparity map, which is
transmitted through gigabit ethernet. The disparity map describes a
mapping of image points from the left camera image to corresponding
image points in the right camera image. With this information it is
possible to reconstruct the 3D location of the corresponding scene
points.

[Youtube](https://www.youtube.com/watch?v=vVVjFqUkG4E)

## Installation

On Ubuntu Linux, please use the following commands to install the
official package for your current ROS version.

```
sudo apt-get update
sudo apt-get install ros-`rosversion -d`-nerian-sp1
``` Should there not be an appropriate package for
your system and ROS version, please checkout the git repository and
compile the code using catkin.

## ROS Node

The data delivered by the SP1 can be received using the available open
source API. Using the API directly is recommended for high performance
applications. Alternatively the `nerian_sp1` ROS node can be used for
publishing the received data as ROS messages.

![](https://nerian.com/blog/articles/images/sp1-ros.jpg)

### Published Topics

The node can publish the received data through three different topics:

```clearsilver

pub {
  no_header=True
  0.name = /nerian_sp1/point_cloud
  0.type = sensor_msgs/PointCloud2
  0.desc = A point cloud, which is obtained by reconstructing the 3D location of each pixel in the disparity map. Optionally, the point cloud can include an intensity channel, which contains intensity data from the left rectified camera image.

  1.name = /nerian_sp1/disparity_map
  1.type = sensor_msgs/Image
  1.desc = The stereo disparity map that is computed by SP1. The disparity map is transmitted as an image message with mono16 encoding. Please note that the disparity map has a 4-bit subpixel resolution. This means that its values have to be divided by 16 in order to receive the true pixel disparity. Optionally, the disparity map can be color coded for visualization. In this case the encoding will be bgr8.

  2.name = /nerian_sp1/left_image
  2.type = sensor_msgs/Image
  2.desc = The rectified image of the left camera with mono8 encoding, if the SP1 is configured in stereo matching or rectify mode. If the SP1 is configured in pass-through mode the unrectified left camera image will be published through this topic.

  3.name = /nerian_sp1/right_image
  3.type = sensor_msgs/Image
  3.desc = If the SP1 is configured in pass-through or rectify mode, then the (un)rectified right camera image will be published through this topic in mono8 encoding

  4.name = /nerian_sp1/stereo_camera_info
  4.type = nerian_sp1/StereoCameraInfo
  4.desc = Camera calibration information for both cameras.
}
```

### Parameters

The behaviour of the node can be configured through various parameters.
An example parameterization can be found in the included launch file
`nerian_sp1.launch`. The following parameters are supported:

```clearsilver

param {
  no_header=True
  0.name = ~point_cloud_intensity_channel
  0.type = bool
  0.default = `"true"`
  0.desc = If enabled, an intensity channel will be added to the point cloud.

  1.name = ~ros_coordinate_system
  1.type = bool
  1.default = `"true"`
  1.desc = If enabled, the typical ROS coordinate system is used, with the x-axis pointing forward, the y-axis pointing left and the z-axis pointing upwards. If disabled, the SP1's default coordinate system is used, with the x-axis pointing right, the y-axis pointing downwards, and the z-axis pointing forward.

  2.name = ~color_code_disparity_map
  2.type = bool
  2.default = `"false"`
  2.desc = If enabled, the disparity map will be color coded in a red/blue color scheme.

  3.name = ~color_code_legend
  3.type = bool
  3.default = `"true"`
  3.desc = If enabled, a legend will be added to the color coded disparity map.

  4.name = ~frame
  4.type = string
  4.default = `"world"`
  4.desc = ID of the frame that will be set for all transmitted messages.

  5.name = ~remote_host
  5.type = string
  5.default = `"0.0.0.0"`
  5.desc = Host name or IP address of the SP1, which is used for network communication. This parameter is only recessionary when using TCP as the underlying network protocol.

  6.name = ~remote_port
  6.type = string
  6.default = `"7681"`
  6.desc = Remote port number or service name that is used for network communicating with SP1. This parameter is only recessionary when using TCP as the underlying network protocol.

  7.name = ~local_host
  7.type = string
  7.default = `"0.0.0.0"`
  7.desc = Local interface address that is used for communication. If not specified, the default interface is used.

  8.name = ~local_port
  8.type = string
  8.default = `"7681"`
  8.desc = The local port that shall be used for network communication, provided as port number or as textual service name.

  9.name = ~use_tcp
  9.type = bool
  9.default = `"false"`
  9.desc = If enabled, TCP is used rather than UDP as underlying network protocol.

  10.name = ~calibration_file
  10.type = string
  10.default = `""`
  10.desc = Location of a YAML-file containing camera calibration data. This file can be obtained from the SP1 web interface. An example calibration file is provided in the repository. If this parameter is omitted, the published camera calibration information only contains the q-Matrix.

  11.name = ~delay_execution
  11.type = double
  11.default = `0`
  11.desc = Allows the configuration of an initial delay in seconds when launching the node. This option can be used to delay the node launch while the calibration information is downloaded.

  12.name = ~max_depth
  12.type = double
  12.default = `-1`
  12.desc = If set to a positive value, all points in the point cloud with a higher depth will be set to invalid.
}
```

### Testing

The topics published by the nerian_sp1 node can be viewed with
[rviz](rviz). The disparity map can also be visualized with the
[image_view](image_view) node. In this case color coding should be
activated such that the disparity map can be displayed on a screen. In
order to do so, please launch the image_view node as follows:

```
rosrun image_view image_view image:=/nerian_sp1/disparity_map
```

![](https://nerian.com/blog/articles/images/image_view.jpg)

For displaying the left camera image, please run the image_view node
with the following command line:

```
rosrun image_view image_view image:=/nerian_sp1/left_image
```

## Further Information

-   [SP1 product page](https://nerian.com/products/sp1-stereo-vision/)
-   [Github project page](https://github.com/nerian-vision/nerian_sp1)
-   [API documentation](https://nerian.com/products/sp1-stereo-vision/api-doc/)
-   [SP1 user manual](https://nerian.com/products/sp1-stereo-vision/downloads/sp1_manual.pdf)

![\|display=\"none ! important\",hidden=\"\"](http://c.statcounter.com/10599048/0/906ae443/1/)
