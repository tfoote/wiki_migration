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



```clearsilver
node.0 {
  name = processing.launch.xml
  desc << EOM
Launches many processing nodelets for turning the raw RGB and depth images into useful products, such as point clouds. Allows a number of arguments to streamline processing.
EOM
}
```



#### Arguments



```clearsilver
param {
  no_header=True
  group.0 {
    name = Streamline processing nodelet graph
    0.name = rgb_processing
    0.type = bool
    0.default = true
    0.desc = Launch nodelets for generating raw and rectified monochrome and color images. Given bayer encoded images on the `rgb/image_raw` topic from the RGB-D driver, the rgb processing chain produces `rgb/image_mono`, `rgb/image_rect_mono`, `rgb/image_color` and `rgb/image_rect_color`.
    1.name = debayer_processing
    1.type = bool
    1.default = true
    1.desc = Usage of this parameter requires `rgb_processing` to be true. Debayers the image into monochrome and color. If set to `true` then explanation for `rgb_processing` directly applies. If set to `false` the rgb processing chain only produces `rgb/image_rect_color`.
    2.name = ir_processing
    2.type = bool
    2.default = true
    2.desc = If set to `true`, rectifies the raw IR image (`ir/image_raw` -> `ir/image_rect_raw`)
    3.name = depth_processing
    3.type = bool
    3.default = true
    3.desc = Given the raw depth image, rectifies it, converts both the raw and rectified images to metric format (`uint16` -> `float`), and produces a pointcloud. Requires `depth/image_raw`. Produces `depth/image_rect_raw` (rectified), `depth/image` (metric), `depth/image_rect` (rectified, metric), `depth/points` (pointcloud).
    4.name = depth_registered_processing
    4.type = bool
    4.default = true
    4.desc = Generates a registered RGBD pointcloud from the device data (requires `rgb_processing` to be enabled). A pointcloud can be generated through a software registration pipeline (sw_registered_processing = `true`, used when depth_registration for device driver is set to `false` ) by registering the depth image from the depth frame to an RGB frame and merging with the RGB image. If software registration is being used, `depth_processing` needs to be enabled. Alternatively, the device can be directly asked to generate a registered depth image in the RGB frame with can be merged with the RGB Image through the hardware registration pipeline (hw_registered_processing = `true`, used when depth_registration for device driver is set to `true`)
    5.name = disparity_processing
    5.type = bool
    5.default = true
    5.desc = Generates a disparity image from unregistered depth data (i.e. in the depth frame). Converts `depth/image_rect_raw` and `projector/camera_info` into the disparity image `depth/disparity`. Requires `depth_processing` to be enabled.
    6.name = disparity_registered_processing
    6.type = bool
    6.default = true
    6.desc = Generates a disparity image from registered depth data (i.e. in the RGB frame). Converts `depth_registered/sw_registered/image_rect_raw` OR `depth_registered/hw_registered/image_rect_raw` and `projector/camera_info` into the disparity image `depth_registeres/disparity`. If using the software registration pipeline, requires `depth_processing` and `depth_registered_processing` to be enabled. If using the hardware registration pipeline, requires `depth_registered_processing` to be enabled.
    6.name = sw_registered_processing
    6.type = bool
    6.default = true
    6.desc = Enables the software registration pipeline. `depth/image_rect_raw` -> `depth_registered/sw_registered/image_rect_raw` (registered) -> `depth_registered/points` AND `depth_registered/disparity`.
    7.name = hw_registered_processing
    7.type = bool
    7.default = true
    7.desc = Enables the hardware registration pipeline. `depth/image_raw` -> `depth_registered/hw_registered/image_rect_raw` (rectified) -> `depth_registered/points` AND `depth_registered/disparity`.
    8.name = queue_size
    8.type = int
    8.default = 5
    8.desc = Size of message queue for synchronizing image and camera_info topics. You may need to raise this if images take significantly longer to travel over the network than camera info.
  }
}
```





```clearsilver
param {
  no_header=True
  group.1 {
    name = Remapping
    0.name = rgb
    0.type = string
    0.default = rgb
    0.desc = Remap the `rgb` namespace.
    1.name = ir
    1.type = string
    1.default = ir
    1.desc = Remap the `ir` namespace.
    2.name = depth
    2.type = string
    2.default = depth
    2.desc = Remap the `depth` namespace.
    3.name = depth_registered
    3.type = string
    3.default = depth_registered
    3.desc = Remap the `depth_registered` namespace.
    4.name = projector
    4.type = string
    4.default = projector
    4.desc = Remap the `projector` namespace.
  }
}
```



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
