## Overview

`compressed_depth_image_transport` is a plugin package for
[image_transport](https://index.ros.org/p/image_transport). It enables
any node using `image_transport` classes to publish and subscribe to
compressed depth image/map topics. Compression parameters can be changed
on the fly using the dynamic_reconfigure package.

`compressed_depth_image_transport` works only with floating-point or
16-bit integer encoded depth images.

**`'Before reading this page, make sure you understand the [[https://index.ros.org/p/image_transport|image_transport]] package`**'

## Tutorials

See [Tutorials](https://index.ros.org/p/image_transport) for general
instruction on using `image_transport`.
`compressed_depth_image_transport` works similar to
`compressed_image_transport` which is featured in the
`image_transport` tutorial
[Examining the Simple Image Publisher and Subscriber](https://index.ros.org/p/image_transport).

## ROS API



```clearsilver
name = Publisher plugin
desc =
pub {
  0.name = <base_topic>/compressedDepth
  0.type = sensor_msgs/CompressedImage
  0.desc = Compressed depth transport subtopic.
}
```





```
{{#!wiki version diamondback_and_newer
{{{{#!wiki version melodic_and_older
{{{
#!clearsilver CS/NodeAPI
param {
group.0 {
  name=Reconfigurable parameters
  desc=Starting in Diamondback, all publisher parameters are dynamically reconfigurable per-topic. See [[dynamic_reconfigure]] for details on dynamically reconfigurable parameters.
  0.name = <base_topic>/compressedDepth/depth_max
  0.type = double
  0.default = 10.0
  0.desc = Maximum depth value (meter), in the range [1, 100]
  1.name = <base_topic>/compressedDepth/depth_quantization
  1.type = double
  1.default = 100
  1.desc = Depth value at which the sensor accuracy is 1 m (Kinect: >75), in the range [1, 150].
  2.name = <base_topic>/compressedDepth/png_level
  2.type = int
  2.default = 9 (or 1 since 2023)
  2.desc = PNG compression level, in the range [1, 9]. Higher values trade computation time for space savings.
}
}
```

 }}}}



```
{#!wiki version noetic_and_newer
{{{
#!clearsilver CS/NodeAPI
param {
group.0 {
  name=Reconfigurable parameters
  desc=Starting in Diamondback, all publisher parameters are dynamically reconfigurable per-topic. See [[dynamic_reconfigure]] for details on dynamically reconfigurable parameters.
  0.name = <base_topic>/compressedDepth/format
  0.type = enum [png | rvl]
  0.default = png
  0.desc = Compression format. The RVL format has been added in Noetic and is not available on previous ROS versions. Previous ROS versions have always used PNG. <<Version(Noetic)>>
  1.name = <base_topic>/compressedDepth/depth_max
  1.type = double
  1.default = 10.0
  1.desc = Maximum depth value (meter), in the range [1, 100]
  2.name = <base_topic>/compressedDepth/depth_quantization
  2.type = double
  2.default = 100
  2.desc = Depth value at which the sensor accuracy is 1 m (Kinect: >75), in the range [1, 150].
  3.name = <base_topic>/compressedDepth/png_level
  3.type = int
  3.default = 9 (or 1 since 2023)
  3.desc = PNG compression level, in the range [1, 9]. Higher values trade computation time for space savings.
}
}
```

 }}}} }}}}}



```clearsilver
name = Subscriber plugin
desc =
sub {
  0.name = <base_topic>/compressedDepth
  0.type = sensor_msgs/CompressedImage
  0.desc = Compressed depth transport subtopic.
}
```
