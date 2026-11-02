## Overview

This package contains launch files for using RGB-D devices such as the
Microsoft Kinect in ROS. It creates a
[nodelet](https://index.ros.org/p/nodelet) graph to transform raw data
from the device driver into point clouds, disparity images, and other
products suitable for processing and visualization.

`rgbd_launch` contains all the common launch files required by a
driver specific launch package such as
[openni_launch](https://index.ros.org/p/openni_launch) or
[freenect_launch](https://index.ros.org/p/freenect_launch). There are 2
important launch files:

- `processing.launch.xml` - Top-level launch file not designed for
  direct execution, but should be included from driver-specific launch
  files. This file launches a constellation of nodelets to process data
  from a RGB-D driver such as
  [openni_camera](https://index.ros.org/p/openni_camera) or
  [freenect_camera](https://index.ros.org/p/freenect_camera). This file
  also accepts a number of arguments designed to streamline the
  constellation of nodelets.
- `kinect_frames.launch` - Launch the tf tree for a Kinect. This file
  can also be launched internally from
  [openni_launch](https://index.ros.org/p/openni_launch) or
  [freenect_launch](https://index.ros.org/p/freenect_launch).

## Launch Files

`rgbd_launch` contains many internal launch files to split up
processing. Only the following launch files should be used externally:

### processing.launch.xml

Launches many processing nodelets for turning the raw RGB and depth
images into useful products, such as point clouds. Allows a number of
arguments to streamline processing.

#### Arguments

##### Streamline processing nodelet graph

- `rgb_processing` (`bool`, default: `true`): Launch nodelets for
  generating raw and rectified monochrome and color images. Given bayer
  encoded images on the `rgb/image_raw` topic from the RGB-D driver,
  the rgb processing chain produces `rgb/image_mono`,
  `rgb/image_rect_mono`, `rgb/image_color` and
  `rgb/image_rect_color`.
- `debayer_processing` (`bool`, default: `true`): Usage of this
  parameter requires `rgb_processing` to be true. Debayers the image
  into monochrome and color. If set to `true` then explanation for
  `rgb_processing` directly applies. If set to `false` the rgb
  processing chain only produces `rgb/image_rect_color`.
- `ir_processing` (`bool`, default: `true`): If set to `true`,
  rectifies the raw IR image (`ir/image_raw` ->
  `ir/image_rect_raw`)
- `depth_processing` (`bool`, default: `true`): Given the raw depth
  image, rectifies it, converts both the raw and rectified images to
  metric format (`uint16` -> `float`), and produces a pointcloud.
  Requires `depth/image_raw`. Produces `depth/image_rect_raw`
  (rectified), `depth/image` (metric), `depth/image_rect`
  (rectified, metric), `depth/points` (pointcloud).
- `depth_registered_processing` (`bool`, default: `true`): Generates a
  registered RGBD pointcloud from the device data (requires
  `rgb_processing` to be enabled). A pointcloud can be generated
  through a software registration pipeline (sw_registered_processing =
  `true`, used when depth_registration for device driver is set to
  `false` ) by registering the depth image from the depth frame to an
  RGB frame and merging with the RGB image. If software registration is
  being used, `depth_processing` needs to be enabled. Alternatively,
  the device can be directly asked to generate a registered depth image
  in the RGB frame with can be merged with the RGB Image through the
  hardware registration pipeline (hw_registered_processing = `true`,
  used when depth_registration for device driver is set to `true`)
- `disparity_processing` (`bool`, default: `true`): Generates a
  disparity image from unregistered depth data (i.e. in the depth
  frame). Converts `depth/image_rect_raw` and
  `projector/camera_info` into the disparity image
  `depth/disparity`. Requires `depth_processing` to be enabled.
- `sw_registered_processing` (`bool`, default: `true`): Enables the
  software registration pipeline. `depth/image_rect_raw` ->
  `depth_registered/sw_registered/image_rect_raw` (registered) ->
  `depth_registered/points` AND `depth_registered/disparity`.
- `hw_registered_processing` (`bool`, default: `true`): Enables the
  hardware registration pipeline. `depth/image_raw` ->
  `depth_registered/hw_registered/image_rect_raw` (rectified) ->
  `depth_registered/points` AND `depth_registered/disparity`.
- `queue_size` (`int`, default: `5`): Size of message queue for
  synchronizing image and camera_info topics. You may need to raise this
  if images take significantly longer to travel over the network than
  camera info.

##### Remapping

- `rgb` (`string`, default: `rgb`): Remap the `rgb` namespace.
- `ir` (`string`, default: `ir`): Remap the `ir` namespace.
- `depth` (`string`, default: `depth`): Remap the `depth` namespace.
- `depth_registered` (`string`, default: `depth_registered`): Remap the
  `depth_registered` namespace.
- `projector` (`string`, default: `projector`): Remap the `projector`
  namespace.

#### Example Parameter Configurations

[freenect_launch](https://index.ros.org/p/freenect_launch) contains some
example configurations that you can run and test running nodelets in the
system: 

```
roslaunch freenect_launch freenect-xyz.launch
roslaunch freenect_launch freenect-registered-xyzrgb.launch
```

 The first launch files only produces a
pointcloud from depth data. The second launch file produces a registered
pointcloud using hardware registration on the device.
