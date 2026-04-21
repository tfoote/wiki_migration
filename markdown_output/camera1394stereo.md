## Overview

This package provides a ROS interface for Firewire based stereo cameras
such as Point Grey Bumblebee2. These cameras meet the
[IEEE 1394 IIDC standard](http://damien.douxchamps.net/ieee1394/libdc1394/iidc/IIDC_1.31.pdf)
using [libdc1394](http://damien.douxchamps.net/ieee1394/libdc1394/),
which supports
[many camera and models](http://damien.douxchamps.net/ieee1394/cameras/).

This package is based on [camera1394](camera1394), and it uses the same
parameters and topics. See [camera1394](camera1394) for more information
on parameters and options.

## Differences to camera1394

First, it interfaces stereo cameras compliant to IEEE 1394 IIDC
standard. In order to do that, the readData function has been changed to
support two images and their corresponding deinterlace using dc1394 lib.
Finally, debayering on format7 modes has been allowed.

### Stereo methods

**Supported methods**: Interlaced stereo, field stereo.

## Examples

Launch the driver as a node: 

```
<launch>
  <node pkg="camera1394stereo" type="camera1394stereo_node" name="camera1394stereo_node" output="screen" >
    <param name="video_mode" value="format7_mode3" />
    <param name="format7_color_coding" value="raw16" />
    <param name="bayer_pattern" value="grbg" />
    <param name="bayer_method" value="" />
    <param name="stereo_method" value="Interlaced" />
    <param name="camera_info_url_left" value="" />
    <param name="camera_info_url_right" value="" />
  </node>
</launch>
```



as a nodelet:



```
<launch>
  <arg name="camera" default="stereo"/>
  <arg name="base_topic" default="$(arg camera)" />
  <arg name="manager" default="manager" />

  <node pkg="nodelet" type="nodelet" name="$(arg base_topic)_node" output="screen"
      args="load camera1394stereo/driver $(arg manager)">
    <param name="frame_id" value="$(arg base_topic)_optical" />
    <param name="camera_info_url_left" value="/path/to/calibration_left.yaml" />
    <param name="camera_info_url_right" value="/path/to/calibration_right.yaml" />
    <remap from="stereo_camera" to="$(arg base_topic)" />
  </node>
</launch>
```



## Report a Bug

Please use the issue tracker at Github to report bugs or request
features: <https://github.com/srv/camera1394stereo/issues>
