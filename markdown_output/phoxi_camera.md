## Introduction

The phoxi_camera driver provides a ROS interface for PhoXi devices.

## Installation

Get the package from github and put it in your catkin workspace src
folder:

```
$ cd ~/catkin_ws/src
$ git clone https://github.com/photoneo/phoxi_camera
```

## ROS Node

### Published Topics

The node can publish the received data through different topics:

```clearsilver

pub {
  no_header=True
  0.name = /phoxi_camera/pointcloud
  0.type = sensor_msgs/PointCloud2
  0.desc = Point cloud

  1.name = /phoxi_camera/confidence_map
  1.type = sensor_msgs/Image
  1.desc = Confidence map

  2.name = /phoxi_camera/normal_map
  2.type = sensor_msgs/Image
  2.desc = Normal map

  3.name = /phoxi_camera/texture
  3.type = sensor_msgs/Image
  3.desc = Texture
}
```

### Parameters

The following parameters are supported:

```clearsilver

param {
  no_header=True
  0.name = ~vertical_resolution
  0.type = int
  0.desc = Desired vertical resolution of the camera image: [full resolution (1), half resolution (2)]

  1.name = ~horizontal_resolution
  1.type = int
  1.desc = Desired horizontal resolution of the camera image: [full resolution (1), half resolution (2)]

  2.name = ~scan_multiplier
  2.type = int
  2.desc = Defines the number of scans that will be taken and merged to single output.

  3.name = ~shutter_multiplier
  3.type = int
  3.desc = Multiplication of the Basic scanner shutter time.

  4.name = ~trigger_mode
  4.type = int
  4.desc = Defines the trigger mode of the device. Currently, only Freerun and Software  Trigger are supported  [Freerun (0), Software (1)]

  5.name = ~timeout
  5.type = int
  5.desc = PhoXiTimeout is used in all calls when Timeout have sense calls Like GetFrame takes Timeout as optional parameters to wait for the frame [ZeroTimeout (-0), Infinity (1), LastStored (-2), Default (-3)]

  6.name = ~confidence
  6.type = double
  6.desc = Confidence

  7.name = ~send_point_cloud
  7.type = bool
  7.desc = If enabled, an point cloud will be captured and published from the camera

  8.name = ~send_normal_map
  8.type = bool
  8.desc = If enabled, an normal map will be captured and published from the camera

  9.name = ~send_texture
  9.type = bool
  9.desc = If enabled, an texture will be captured and published from the camera

  10.name = ~send_confidence_map
  10.type = bool
  10.desc = If enabled, an confidence map will be captured and published from the camera
}
```

### Testing

The point cloud published by the phoxi_camera node can be viewed with
[rviz](rviz).

```
roslaunch phoxi_camera phoxi_camera.launch
```
