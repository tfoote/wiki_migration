

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
to [image_transport](https://index.ros.org/p/image_transport) package
specifications in sink-on-demand operating mode. Also, the
[dynamic_reconfigure](https://index.ros.org/p/dynamic_reconfigure)
specifications are partially supported to publish actual frame
parameters.

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
  for publishing
  [dynamic_reconfigure](https://index.ros.org/p/dynamic_reconfigure)
  description messages under `parameter_descriptions` topic suffix

### Topic names abbreviation policy

The node formulates topic namespaces and affixes using the following
policy: 1. **Node name** taken from ROS launch server 2. **Transport
suffix** configured with `camera_transport_suffix` parameter 3.
**[image_transport](https://index.ros.org/p/image_transport) mode
suffix** 4. **Description suffix** provided from
[dynamic_reconfigure](https://index.ros.org/p/dynamic_reconfigure) API
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



### usb_cam_node

Opens the V4L device handler to poll the camera, recompress and publish
the images on demand

#### Published Topics

- `/<node_name>/camera_info`
  ([sensor_msgs/msg/CameraInfo](https://docs.ros.org/en/rolling/p/sensor_msgs/msg/CameraInfo.html)):
  Camera calibration matrices from the specified calibration YAML file
  provided by the camera's vendor, or obtained with tools from
  [camera_calibration](https://index.ros.org/p/camera_calibration)
  package
- `/<node_name>/<camera_transport_suffix>`
  ([sensor_msgs/msg/Image](https://docs.ros.org/en/rolling/p/sensor_msgs/msg/Image.html)):
  Uncompressed frames
- `/<node_name>/<camera_transport_suffix>/compressed`
  ([sensor_msgs/msg/CompressedImage](https://docs.ros.org/en/rolling/p/sensor_msgs/msg/CompressedImage.html)):
  PNG/JPEG compressed frames according to
  [image_transport](https://index.ros.org/p/image_transport)
  specifications
- `/<node_name>/<camera_transport_suffix>/compressed/parameter_descriptions`
  ([dynamic_reconfigure/msg/ConfigDescription](https://docs.ros.org/en/rolling/p/dynamic_reconfigure/msg/ConfigDescription.html)):
  Latched topic providing compressed frame's parameter descriptions for
  the nodes supporting
  [image_transport](https://index.ros.org/p/image_transport)
  specification and
  [dynamic_reconfigure](https://index.ros.org/p/dynamic_reconfigure)
- `/<node_name>/<camera_transport_suffix>/compressed/parameter_updates`
  ([dynamic_reconfigure/msg/Config](https://docs.ros.org/en/rolling/p/dynamic_reconfigure/msg/Config.html)):
  Latched topic providing compressed frame's actual parameters for the
  nodes supporting
  [image_transport](https://index.ros.org/p/image_transport)
  specification and
  [dynamic_reconfigure](https://index.ros.org/p/dynamic_reconfigure)
- `/<node_name>/<camera_transport_suffix>/compressedDepth`
  ([sensor_msgs/msg/CompressedImage](https://docs.ros.org/en/rolling/p/sensor_msgs/msg/CompressedImage.html)):
  PNG-compressed 16-bit depth frames
- `/<node_name>/<camera_transport_suffix>/compressedDepth/parameter_descriptions`
  ([dynamic_reconfigure/msg/ConfigDescription](https://docs.ros.org/en/rolling/p/dynamic_reconfigure/msg/ConfigDescription.html)):
  Latched topic providing compressed frame's parameter descriptions for
  [depth_image_proc](https://index.ros.org/p/depth_image_proc)
- `/<node_name>/<camera_transport_suffix>/compressedDepth/parameter_updates`
  ([dynamic_reconfigure/msg/Config](https://docs.ros.org/en/rolling/p/dynamic_reconfigure/msg/Config.html)):
  Latched topic providing compressed frame's actual parameters for
  [depth_image_proc](https://index.ros.org/p/depth_image_proc)
- `/<node_name>/<camera_transport_suffix>/theora`
  ([theora_image_transport/msg/Packet](https://docs.ros.org/en/rolling/p/theora_image_transport/msg/Packet.html)):
  Incrementally encoded stacks of frames compatible with
  [theora_image_transport](https://index.ros.org/p/theora_image_transport)
  package specification
- `/<node_name>/<camera_transport_suffix>/theora/parameter_descriptions`
  ([dynamic_reconfigure/msg/ConfigDescription](https://docs.ros.org/en/rolling/p/dynamic_reconfigure/msg/ConfigDescription.html)):
  Latched topic providing compressed frame's parameter descriptions for
  the nodes supporting
  [theora_image_transport](https://index.ros.org/p/theora_image_transport)
  specification and
  [dynamic_reconfigure](https://index.ros.org/p/dynamic_reconfigure)
- `/<node_name>/<camera_transport_suffix>/theora/parameter_updates`
  ([dynamic_reconfigure/msg/Config](https://docs.ros.org/en/rolling/p/dynamic_reconfigure/msg/Config.html)):
  Latched topic providing compressed frame's actual parameters for the
  nodes supporting
  [theora_image_transport](https://index.ros.org/p/theora_image_transport)
  specification and
  [dynamic_reconfigure](https://index.ros.org/p/dynamic_reconfigure)

#### Services

- `/<node_name>/<start_service_name>`
  ([std_srvs/srv/Empty](https://docs.ros.org/en/rolling/p/std_srvs/srv/Empty.html)):
  Call this service to start the suspended capture of frames from the
  device
- `/<node_name>/<stop_service_name>`
  ([std_srvs/srv/Empty](https://docs.ros.org/en/rolling/p/std_srvs/srv/Empty.html)):
  Call this service to stop the active capture of frames from the device
- `/<node_name>/supported_controls`
  ([std_srvs/srv/Trigger](https://docs.ros.org/en/rolling/p/std_srvs/srv/Trigger.html)):
  <a id="intrinsic_control_names"></a>Returns
  the `"\|"`-separated string containing the list of intrinsic
  controls (parameters) the camera supports, queried from V4L kernel
  driver. In case of presence, the first `"\|"` symbol should be
  ignored.
- `/<node_name>/supported_formats`
  ([std_srvs/srv/Trigger](https://docs.ros.org/en/rolling/p/std_srvs/srv/Trigger.html)):
  <a id="img_formats"></a>Returns the
  `"\|"`-separated string containing the list of image
  formats/encodings the camera supports, queried from V4L kernel driver.
  In case of presence, the first `"\|"` symbol should be ignored.

#### Parameters

- `start_service_name` (`string`, default: `start_capture`): Defines
  name suffix for
  [std_srvs/srv/Empty](https://docs.ros.org/en/rolling/p/std_srvs/srv/Empty.html)
  service which restarts suspended streaming
- `stop_service_name` (`string`, default: `stop_capture`): Defines
  name suffix for
  [std_srvs/srv/Empty](https://docs.ros.org/en/rolling/p/std_srvs/srv/Empty.html)
  service which suspends camera polling timer
- `video_device` (`string`, default: `/dev/video0`): Device driver's
  entry point in Linux kernel's virtual filesystem
- `io_method` (`string`, default: `mmap`): I/O method (see
  [Available I/O methods](#io_modes) for value
  reference)
- `pixel_format` (`string`, default: `yuyv`): Pixel format for
  Video4linux device (also selects decoder mode). See
  [Pixel formats](#pixel_formats) for value reference
- `color_format` (`string`, default: `yuv422p`): On-chip color
  representation mode for the input frame encoded by hardware. See
  [Color formats](#color_formats) for value reference
- `create_suspended` (`bool`, default: `false`): Instructs the node
  whether to start streaming immediately after launch or to wait until
  the `<start_service_name>` service will be triggered
- `full_ffmpeg_log` (`bool`, default: `false`): When set to `false`
  allows to suppress warning messages generated by `libavcodec` during
  MJPEG decoding, cleans log files
- `camera_name` (`string`, default: `head_camera`): ROS internal name
  for the camera, used to generate
  [sensor_msgs/msg/CameraInfo](https://docs.ros.org/en/rolling/p/sensor_msgs/msg/CameraInfo.html)
  message
- `camera_frame_id` (`string`, default: `head_camera`): Frame ID used
  to generate coordinate transformations
- `camera_transport_suffix` (`string`, default: `image_raw`): Suffix
  used by [image_transport](https://index.ros.org/p/image_transport) to
  generate topic names
- `camera_info_url` (`string`, default: `""`): URI for camera
  calibration data (likely a YML file obtained from
  [camera_calibration](https://index.ros.org/p/camera_calibration)
  tools)
- `image_width` (`integer`, default: `640`): Frame width in pixels,
  **should be supported by hardware**! Please refer to
  [supported_formats](#img_formats) service for list
  of possible values
- `image_height` (`integer`, default: `480`): Frame height in pixels,
  **should be supported by hardware**! Please refer to
  [supported_formats](#img_formats) service for list
  of possible values
- `framerate` (`integer`, default: `30`): Camera polling frequency, Hz
  (integer)
- `intrinsic_controls` (`multilist`, default: refer to
  [sample config file](https://github.com/ros-drivers/usb_cam/blob/develop/config/usb_cam.yml)):
  Intrinsic controls queried from V4L kernel driver. See
  [Intrinsic Controls](#intrinsics) to learn how to
  configure this list, and
  [supported_controls](#intrinsic_control_names)
  service to retrieve possible values.

### I/O modes reference

<a id="io_modes"></a>The node supports the
following I/O mode names for the given device:

- `read` - for devices supporting virtual filesystem or block I/O
- `mmap` - for devices supporting direct `libusb` memory mapping
- `userptr` - for DMA devices supporting userspace pointer exchange

### Pixel formats/encodings reference

<a id="pixel_formats"></a>Selection of the
pixel format name automatically selects the decoder library and pixel
representation for FFMPEG/`libavcodec` processing. The node supports
the following pixel format names and decoders (all names are
case-sensitive):

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

### Color representation formats reference

<a id="color_formats"></a>The node supports
the following color representation mode names (case-sensitive):

- `yuv422p` - YUV422 - default, compatible with most MJPEG hardware
  encoders
- `yuv420p` - YUV420 - may be required by H.264 and H.265 hardware
  encoders

### Intrinsic control configuration

<a id="intrinsics"></a>The node queries V4L
kernel driver for available intrinsic control names and data types they
require, in the same way, that one can query from terminal with the
following command: 

```
v4l2-ctl --device=/dev/video<ID> -L
```

 The node supports the
following types of intrinsic controls provided by `libv4l2`:

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

## Troubleshooting

### FFMPEG: MJPEG output buffer size mismatch

If you see repeated groups of messages like this:


```
FFMPEG: MJPEG output buffer size mismatch: 460800 (614400 expected)
2D processing operation fault
[ERROR] [1680887653.104109599]: Video4linux: frame grabber failed
```

 it means that the color representation obtained
from the MJPEG decoder does not match the representation configured in
the configuration file. Try to change `color_format` parameter to
another value. Then try to check if the configured frame size
(`image_width` and `image_height` parameters) is actually supported
by your camera querying `/<node_name>/supported_formats` service.

### Determining correct pixel_format value for the device

If the output of the node is images of the correct size but the pixel
format is literally mismatching the spec, like this:
![](https://user-images.githubusercontent.com/34397296/47157450-ee46df80-d31b-11e8-9009-18da5510ecac.png)

try to use the following command: 

```
v4l2-ctl --list-formats-ext --device=/dev/video0 | grep -e '^[[:space:]]*\[[0-9]*\]'
```

 to have the
list of available pixel formats and encodings, then select the proper
format according to
[Pixel formats/encodings reference](#pixel-formatsencodings-reference).
The example output of this command for *Logitech HD Pro Webcam C920*
look like: 

```
[0]: 'YUYV' (YUYV 4:2:2)
	[1]: 'H264' (H.264, compressed)
	[2]: 'MJPG' (Motion-JPEG, compressed)
```



### Distinguish between several identical USB devices

This case usually happens when several sensors (not always they are
identical themselves) are connected to the same machine via identical
USB-to-serial adaptors. Linux kernel does not have an ID persistence
policy when the USB devices are enumerated during the boot, so the
referral paths like `/dev/ttyUSB0`, and `/dev/ttyUSB1` may easily
change on the next boot when the identical device is connected to the
same machine on the different USB port, despite the physical ports
themselves are never changed.

To distinguish between such devices there are several ways to do. The
most convenient way is to find a detailed description of the USB
connection the device has through `udevadm`: 

```
lsusb
udevadm info -a -n /dev/<DEVICE> | grep -e '{serial}'
```


The output will include a list of vendor IDs, product IDs and the serial
numbers assigned to the device. Repeating this for all the devices
connected to the machine, the different serial numbers would be
revealed. Then the `udev` rules list could be created as something
like this: 

```
SUBSYSTEM=="tty", ATTRS{idVendor}=="<VendorID>", ATTRS{idProduct}=="<ProductID>", ATTRS{serial}=="<SerialNumber>", SYMLINK+="device_name"
```

 This will create the dedicated
virtual file with the name `/dev/device_name` persistent for the
device with the mentioned `SerialNumber`. However, some cheap devices
(especially, USB-RS232 adaptors) do not have identical serial numbers,
so this approach is not always usable.

------------------------------------------------------------------------

The second approach is to examine the USB bus ID assigned to the device:


```
lsusb -tvv
```

 This will show the tree of USB bus connections
with paths assigned in `/dev/bus` and `/sys/bus` namespaces. Then it
is possible to access the device directly by the listed path.

------------------------------------------------------------------------

The third approach is to examine the driver subsystem name to
distinguish the devices by a unique name. To do that, examine the
`/dev` directory for subdirectories created by the driver, like, for
example, `serial/` for TTY devices, or `v4l/` for web cameras. Then
enter the subdirectory to access the device by its persistent ID, like
this: 

```
/dev/v4l/by-id/usb-046d_HD_Pro_Webcam_C920_919E375F-video-index0
```





```wiki
The approaches described here are '''not portable!'''

All the described approaches described here to distinguish between several identical USB devices are not portable. Usage of them makes the setup always machine-specific. Please thoroughly revise your setup and enumerate your devices correctly to avoid changing IDs and indices!
```



### Video4linux: frame mapping timeout (11)

This error is emitted when the camera does not respond on the USB port
for 5 seconds or more being polled by the node. It may happen with some
old camera chipsets incompatible with the given USB hub controller. In
this case, it is needed to use a different controller or to check the
motherboard for possible USB bridge malfunction. In the simplest case
even reconnecting the camera to a different USB port may work.
