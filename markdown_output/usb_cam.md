

```wiki
'''This page refers to the development version of the package and releases made AFTER 01.04.2023!'''

The `develop` branch of the repository contains the code that '''IS NOT CURRENTLY RELEASED'''! Please consider it a beta release-candidate version implementing the new API and configuration policy.

ROS binary package repository is now containing '''version 0.3.7''' available for installation!

Please note that the documentation for previously released (`0.3.7` and earlier) versions of this package is available on [[/Old Versions|Old versions' documentation]] subpage
```



## Overview

This package provides a configurable ROS interface to the
[kernel API](https://www.kernel.org/doc/html/v4.9/media/uapi/v4l/v4l2.html)
of `libv4l2` library that implements a common driver for standard USB
web cameras. The module uses a monopolistic way of entry point (virtual
filesystem) access model with the policy "one device = one node". The
ROS node running over the
[libv4l2 API](https://www.kernel.org/doc/html/v4.9/media/uapi/v4l/v4l2.html)
also queries the kernel about the intrinsic parameters of the camera and
provides a flexible configuration model via the standard ROS
configuration model. The camera is polled over the intervals of the
desired framerate, then the images are decoded and published according
to [image_transport](image_transport) package specifications in
sink-on-demand operating mode. Also, the
[dynamic_reconfigure](dynamic_reconfigure) specifications are partially
supported to publish actual frame parameters.

### Supported device access models

- *Memory Mapping* - for the device with direct monopolistic USB port
  access model implemented via `libusb`
- *User Pointer Exchange* - for the devices supporting userspace memory
  pointer requests
- *Virtual Block Device* - for the devices supporting block I/O model
  via virtual userspace filesystem kernel driver

### Published message types

- [sensor_msgs/msg/CameraInfo](https://docs.ros.org/en/rolling/p/sensor_msgs/msg/CameraInfo.html)
  for publishing camera calibration matrices
- [sensor_msgs/msg/Image](https://docs.ros.org/en/rolling/p/sensor_msgs/msg/Image.html)
  for uncompressed OpenCV-compatible images
- [sensor_msgs/msg/CompressedImage](https://docs.ros.org/en/rolling/p/sensor_msgs/msg/CompressedImage.html)
  for binary packets containing PNG/JPEG-compressed images published
  under the `compressed` topic suffix. **NOTE**: also on-the-fly
  encoding of the images into 16-bit depth matrices is supported. The
  PNG-compressed frames are published under `compressedDepth` topic
  suffix.
- [theora_image_transport/msg/Packet](https://docs.ros.org/en/rolling/p/theora_image_transport/msg/Packet.html)
  for binary packages containing Theora/H.263 YUV420-encoded stacks of
  images published under `theora` topic suffix
- [dynamic_reconfigure/msg/Config](https://docs.ros.org/en/rolling/p/dynamic_reconfigure/msg/Config.html)
  for publishing actual frame parameters under `parameter_updates`
  topic suffix
- [dynamic_reconfigure/msg/ConfigDescription](https://docs.ros.org/en/rolling/p/dynamic_reconfigure/msg/ConfigDescription.html)
  for publishing [dynamic_reconfigure](dynamic_reconfigure) description
  messages under `parameter_descriptions` topic suffix

### Topic names abbreviation policy

The node formulates topic namespaces and affixes using the following
policy: 1. **Node name** taken from ROS launch server 2. **Transport
suffix** configured with `camera_transport_suffix` parameter 3.
**[image_transport](image_transport) mode suffix** 4. **Description
suffix** provided from [dynamic_reconfigure](dynamic_reconfigure) API
For example, if the node runs under the name `usb_cam` and
`camera_transport_suffix` is set to `image_raw` (default invocation
case), the node will publish the following list of topics:



```
/usb_cam/camera_info
/usb_cam/image_raw
/usb_cam/image_raw/compressed
/usb_cam/image_raw/compressed/parameter_descriptions
/usb_cam/image_raw/compressed/parameter_updates
/usb_cam/image_raw/compressedDepth
/usb_cam/image_raw/compressedDepth/parameter_descriptions
/usb_cam/image_raw/compressedDepth/parameter_updates
/usb_cam/image_raw/theora
/usb_cam/image_raw/theora/parameter_descriptions
/usb_cam/image_raw/theora/parameter_updates
```



### Hardware-accelerated decoder

The support for a hardware-accelerated decoder in the package is now
**experimental**. It is implemented in the dedicated
[branch](https://github.com/ros-drivers/usb_cam/tree/hardware-decoder)
in the repository. The feature is not enabled by default and it is
supported only from `libavcodec` library version `52.00.100`.

## Nodes



```wiki
The names mentioned <in brackets> are actually the names of '''parameters''' configuring the really used names in the ROS system namespace. Thus, most of the names of topics and services mentioned here are '''configurable'''. Please see [[https://github.com/ros-drivers/usb_cam/blob/develop/config/usb_cam.yml|sample config file]] for reference.
```





```clearsilver
node.0{
name=usb_cam_node
desc=Opens the V4L device handler to poll the camera, recompress and publish the images on demand

pub {
  0.name= /<node_name>/camera_info
  0.type= sensor_msgs/CameraInfo
  0.desc= Camera calibration matrices from the specified calibration YAML file provided by the camera's vendor, or obtained with tools from [[camera_calibration]] package
  1.name= /<node_name>/<camera_transport_suffix>
  1.type= sensor_msgs/Image
  1.desc= Uncompressed frames
  2.name= /<node_name>/<camera_transport_suffix>/compressed
  2.type= sensor_msgs/CompressedImage
  2.desc= PNG/JPEG compressed frames according to [[image_transport]] specifications
  3.name= /<node_name>/<camera_transport_suffix>/compressed/parameter_descriptions
  3.type= dynamic_reconfigure/ConfigDescription
  3.desc= Latched topic providing compressed frame's parameter descriptions for the nodes supporting [[image_transport]] specification and [[dynamic_reconfigure]]
  4.name= /<node_name>/<camera_transport_suffix>/compressed/parameter_updates
  4.type= dynamic_reconfigure/Config
  4.desc= Latched topic providing compressed frame's actual parameters for the nodes supporting [[image_transport]] specification and [[dynamic_reconfigure]]
  5.name= /<node_name>/<camera_transport_suffix>/compressedDepth
  5.type= sensor_msgs/CompressedImage
  5.desc= PNG-compressed 16-bit depth frames
  6.name= /<node_name>/<camera_transport_suffix>/compressedDepth/parameter_descriptions
  6.type= dynamic_reconfigure/ConfigDescription
  6.desc= Latched topic providing compressed frame's parameter descriptions for [[depth_image_proc]]
  7.name= /<node_name>/<camera_transport_suffix>/compressedDepth/parameter_updates
  7.type= dynamic_reconfigure/Config
  7.desc= Latched topic providing compressed frame's actual parameters for [[depth_image_proc]]
  8.name= /<node_name>/<camera_transport_suffix>/theora
  8.type= theora_image_transport/Packet
  8.desc= Incrementally encoded stacks of frames compatible with [[theora_image_transport]] package specification
  9.name= /<node_name>/<camera_transport_suffix>/theora/parameter_descriptions
  9.type= dynamic_reconfigure/ConfigDescription
  9.desc= Latched topic providing compressed frame's parameter descriptions for the nodes supporting [[theora_image_transport]] specification and [[dynamic_reconfigure]]
  10.name= /<node_name>/<camera_transport_suffix>/theora/parameter_updates
  10.type= dynamic_reconfigure/Config
  10.desc= Latched topic providing compressed frame's actual parameters for the nodes supporting [[theora_image_transport]] specification and [[dynamic_reconfigure]]
}

srv{
  0.name = /<node_name>/<start_service_name>
  0.type = std_srvs/Empty
  0.desc = Call this service to start the suspended capture of frames from the device

  1.name = /<node_name>/<stop_service_name>
  1.type = std_srvs/Empty
  1.desc = Call this service to stop the active capture of frames from the device

  2.name = /<node_name>/supported_controls
  2.type = std_srvs/Trigger
  2.desc = <<Anchor(intrinsic_control_names)>>Returns the `"|"`-separated string containing the list of intrinsic controls (parameters) the camera supports, queried from V4L kernel driver. In case of presence, the first `"|"` symbol should be ignored.

  3.name = /<node_name>/supported_formats
  3.type = std_srvs/Trigger
  3.desc = <<Anchor(img_formats)>>Returns the `"|"`-separated string containing the list of image formats/encodings the camera supports, queried from V4L kernel driver. In case of presence, the first `"|"` symbol should be ignored.
}

param {
  0.name= start_service_name 
  0.default= `start_capture`
  0.type= string
  0.desc= Defines name suffix for <<SrvLink(std_srvs/Empty)>> service which restarts suspended streaming

  1.name= stop_service_name
  1.default= `stop_capture`
  1.type= string
  1.desc= Defines name suffix for  <<SrvLink(std_srvs/Empty)>> service which suspends camera polling timer

  2.name= video_device
  2.default=`/dev/video0`
  2.type= string
  2.desc= Device driver's entry point in Linux kernel's virtual filesystem

  3.name= io_method
  3.default=`mmap`
  3.type= string
  3.desc= I/O method (see [[#io_modes|Available I/O methods]] for value reference)

  4.name= pixel_format
  4.default=`yuyv`
  4.type= string
  4.desc= Pixel format for Video4linux device (also selects decoder mode). See [[#pixel_formats|Pixel formats]] for value reference 

  5.name= color_format
  5.default=`yuv422p`
  5.type= string
  5.desc= On-chip color representation mode for the input frame encoded by hardware. See [[#color_formats|Color formats]] for value reference

  6.name= create_suspended
  6.default=`false`
  6.type= bool
  6.desc= Instructs the node whether to start streaming immediately after launch or to wait until the `<start_service_name>` service will be triggered

  7.name= full_ffmpeg_log
  7.default=`false`
  7.type= bool
  7.desc= When set to `false` allows to suppress warning messages generated by `libavcodec` during MJPEG decoding, cleans log files

  8.name= camera_name
  8.default=`head_camera`
  8.type= string
  8.desc= ROS internal name for the camera, used to generate <<MsgLink(sensor_msgs/CameraInfo)>> message

  9.name= camera_frame_id
  9.default=`head_camera`
  9.type= string
  9.desc= Frame ID used to generate coordinate transformations

  10.name= camera_transport_suffix
  10.default=`image_raw`
  10.type= string
  10.desc= Suffix used by [[image_transport]] to generate topic names

  11.name= camera_info_url
  11.default=`""`
  11.type= string
  11.desc= URI for camera calibration data (likely a YML file obtained from [[camera_calibration]] tools)

  12.name= image_width
  12.default=`640`
  12.type= integer
  12.desc= Frame width in pixels, '''should be supported by hardware'''! Please refer to [[#img_formats|supported_formats]] service for list of possible values

  13.name= image_height
  13.default=`480`
  13.type= integer
  13.desc= Frame height in pixels, '''should be supported by hardware'''! Please refer to [[#img_formats|supported_formats]] service for list of possible values

  14.name= framerate
  14.default=`30`
  14.type= integer
  14.desc= Camera polling frequency, Hz (integer)

  15.name= intrinsic_controls
  15.default= refer to [[https://github.com/ros-drivers/usb_cam/blob/develop/config/usb_cam.yml|sample config file]]
  15.type= multilist
  15.desc= Intrinsic controls queried from V4L kernel driver. See [[#intrinsics|Intrinsic Controls]] to learn how to configure this list, and [[#intrinsic_control_names|supported_controls]] service to retrieve possible values.
}
```



### I/O modes reference ===The node supports the following I/O mode names for the given device:

- `read` - for devices supporting virtual filesystem or block I/O
- `mmap` - for devices supporting direct `libusb` memory mapping
- `userptr` - for DMA devices supporting userspace pointer exchange

### Pixel formats/encodings reference ===Selection of the pixel format name automatically selects the decoder library and pixel representation for FFMPEG/`libavcodec` processing. The node supports the following pixel format names and decoders (all names are case-sensitive):

- `yuyv` - YUV420
- `yuv` - synonym for `yuyv`
- `uyvy` - UVY240, MESECAM
- `yuvmono10` - Monochrome 10-bit pseudo-YUV
- `rgb24` - Linear 8-bit RGB matrix
- `bgr24` - OpenCV-compatible 8-bit BGR
- `grey` - Grayscale 8-bit linear monochrome matrix
- `yu12` - YU-reversed YUV420
- `mjpeg` - FFMPEG-decoded MotionJPEG. Requires compatible hardware
- `h264` - FFMPEG-decoded H.264. Requires compatible hardware. May
  also require setting `color_format` parameter to `yuv420p`

**NOTE**: In its current state, the node does not support
hardware-accelerated decoding!

### Color representation formats reference ===The node supports the following color representation mode names (case-sensitive):

- `yuv422p` - YUV422 - default, compatible with most MJPEG hardware
  encoders
- `yuv420p` - YUV420 - may be required by H.264 and H.265 hardware
  encoders

### Intrinsic control configuration ===The node queries V4L kernel driver for available intrinsic control names and data types they require, in the same way, that one can query from terminal with the following command:



```
v4l2-ctl --device=/dev/video<ID> -L
```

 The node supports the following types of
intrinsic controls provided by `libv4l2`:

- Booleans (`true/false`)
- Integers (32-bit)
- Integers (64-bit)
- Menus (integer-indexed sets of operating modes)
- Integer/Menu multiparams (menus with manual adjustment possibility)
  The data type for the given parameter is determined automatically.

The queried names become ROS parameters and are placed under
`intrinsic_controls` multilist of the configuration file. Its main
namespace contains:

- Unique names of the generated ROS parameters. **NOTE**: if the
  parameter name reported from V4L kernel driver **exists but not
  mentioned here**, it will be processed and set up with *default
  value*, also provided by the driver.
- `ignore` - the string list containing control names that should be
  **ignored**. If the existing intrinsic control is mentioned here, its
  value will be **left intact**.

#### Example configuration

This example configuration is obtained using *Logitech HD Pro Webcam
C920* web camera with standard `V4L2` kernel driver from Ubuntu 22.04
with 5.15.0 kernel installed. The manually queried control names:


```
v4l2-ctl --device=/dev/video0 -L
                     brightness 0x00980900 (int)    : min=0 max=255 step=1 default=128 value=128
                       contrast 0x00980901 (int)    : min=0 max=255 step=1 default=128 value=128
                     saturation 0x00980902 (int)    : min=0 max=255 step=1 default=128 value=128
 white_balance_temperature_auto 0x0098090c (bool)   : default=1 value=1
                           gain 0x00980913 (int)    : min=0 max=255 step=1 default=0 value=155
           power_line_frequency 0x00980918 (menu)   : min=0 max=2 default=2 value=1 (50 Hz)
				0: Disabled
				1: 50 Hz
				2: 60 Hz
      white_balance_temperature 0x0098091a (int)    : min=2000 max=6500 step=1 default=4000 value=5485 flags=inactive
                      sharpness 0x0098091b (int)    : min=0 max=255 step=1 default=128 value=128
         backlight_compensation 0x0098091c (int)    : min=0 max=1 step=1 default=0 value=0
                  exposure_auto 0x009a0901 (menu)   : min=0 max=3 default=3 value=3 (Aperture Priority Mode)
				1: Manual Mode
				3: Aperture Priority Mode
              exposure_absolute 0x009a0902 (int)    : min=3 max=2047 step=1 default=250 value=200 flags=inactive
         exposure_auto_priority 0x009a0903 (bool)   : default=0 value=1
                   pan_absolute 0x009a0908 (int)    : min=-36000 max=36000 step=3600 default=0 value=0
                  tilt_absolute 0x009a0909 (int)    : min=-36000 max=36000 step=3600 default=0 value=0
                 focus_absolute 0x009a090a (int)    : min=0 max=250 step=5 default=0 value=0 flags=inactive
                     focus_auto 0x009a090c (bool)   : default=1 value=1
                  zoom_absolute 0x009a090d (int)    : min=100 max=500 step=1 default=100 value=100
```

 The corresponding YAML configuration multilist
looks like: 

```
intrinsic_controls:                 
    focus_auto: true
    exposure_auto_priority: true
    exposure_auto: 3
    white_balance_temperature_auto: true
    power_line_frequency: 1
    ignore: [
        brightness,
        contrast,
        saturation,
        gain,
        sharpness,
        backlight_compensation,
        white_balance_temperature,
        exposure_absolute,
        pan_absolute,
        tilt_absolute,
        focus_absolute,
        zoom_absolute
    ]
```

 Here are the following intrinsic
controls that are mentioned in the **root namespace** of the
`intrinsic_controls` multilist, so they will be processed and set up:

- `focus_auto` (boolean)
- `exposure_auto_priority` (boolean)
- `exposure_auto` (menu)
- `white_balance_temperature_auto` (boolean)
- `power_line_frequency` (menu)

All the other intrinsic control names reported by `v4l2-ctl` are
enumerated in the `ignore` string list, so their values will be left
intact.
