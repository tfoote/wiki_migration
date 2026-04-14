## Overview

This package provides a ROS interface for digital cameras meeting the
[IEEE 1394 IIDC standard](http://damien.douxchamps.net/ieee1394/libdc1394/iidc/IIDC_1.31.pdf)
using [libdc1394](http://damien.douxchamps.net/ieee1394/libdc1394/),
which supports
[many camera makes and models](http://damien.douxchamps.net/ieee1394/cameras/).
Of the thousands of IIDC models, we are accumulating a
[list of cameras tested](camera1394/CameraList) with this driver.

It works with the ROS [image_pipeline](image_pipeline) like other
streaming [camera_drivers](camera_drivers).

This is a purely monocular driver, stereo applications need a separate
driver node for each camera of the pair.

No C++ API is provided. There are no utility commands or launch files.

## Support

For help, please check
[http://answers.ros.org](http://answers.ros.org/questions/scope:all/sort:activity-desc/tags:camera1394/page:1/).
If your question is not answered, open a new one with the \`camera1394\`
tag, so we can see it and respond.

To report problems or request new features:
<https://github.com/ros-drivers/camera1394/issues>

## Road Map

The [camera1394_node](#Camera1394Node) driver was first released with
ROS C-Turtle. That API is stable.

Additional features have been added since. They are all compatible with
the previous release, except for the default \`reset_on_open\` value.

-   There is now a [version of the driver](#camera1394_nodelet) that
    runs as a [nodelet](nodelet).
-   Format7 modes.
-   Focus and Zoom features.
-   The \`reset_on_open\` parameter now defaults to \`False\`.
-   The driver will only set \`video_mode\` or \`frame_rate\` parameters
    to values supported by the device.
-   : \`camera1394\` is now released as a separate, unary stack.
    Previously, it was included in the [camera_drivers](camera_drivers)
    stack.
-   : pan feature.
-   : the driver is now built using [catkin](catkin). If you are
    building that version from source, put it in a catkin workspace.
-   : added support for software and hardware triggering. Does not yet
    [provide a ROS polled_camera](https://github.com/ros-drivers/camera1394/issues/13)
    interface, or trigger commands to the device, but a separate node
    can do it.
-   : added
    [get_control_registers](http://docs.ros.org/indigo/api/camera1394/html/srv/GetCameraRegisters.html)
    and
    [set_control_registers](http://docs.ros.org/indigo/api/camera1394/html/srv/SetCameraRegisters.html)
    service calls to access device-specific registers.

### Limitations

#### IIDC Options

IIDC options still not supported:

-   Format6 modes
-   Trigger support

#### Stereo Image Synchronization

It is possible to combine two monocular 1394 cameras to produce a stereo
image if they are configured to trigger together. Some IIDC cameras
provide trigger synchronization over the 1394 bus or via external
hardware.

By default, [stereo_image_proc](stereo_image_proc) requires the message
timestamps for both images to match exactly, which the \`camera1394\`
driver cannot do. The Diamondback release of \`stereo_image_proc\`
provided a solution for this problem (enhancement
[#4217](https://code.ros.org/trac/ros-pkg/ticket/4217)).

### C-Turtle Version

The [initial C-Turtle release](camera1394/Cturtle) had some significant
limitations. Some have been removed in later releases. Please check the
specific documentation for that release, if you are still using ROS
C-Turtle.

## Features

The IIDC specification lists a number of optional features that may be
provided by conforming camera implementations. Many are supported by the
driver as parameters. While the spec mentions the names of these
features, it does not define what they do. Consult the technical
specifications of the camera: manufacturers have great latitude in
determining which features to support, what values they can take, and
the meanings of those values.

For each supported feature there is a corresponding \`auto\_\` parameter
providing user control. Different cameras handle these controls in
various ways.

The control states are:

-   \'\'\'Off\'\'\'(0): turns the feature off (if possible)
-   \'\'\'Query\'\'\'(1): returns the current mode and (if possible) the
    value of the feature, with no change to the device
-   \'\'\'Auto\'\'\'(2): the camera sets the value continuously (if
    possible)
-   \'\'\'Manual\'\'\'(3): sets a specific value from the corresponding
    parameter (if possible)
-   \'\'\'!OnePush\'\'\'(4): the camera sets the value once, then holds
    it constant (if possible)
-   \'\'\'None\'\'\'(5): the camera does not provide this feature

When setting an IIDC feature to a specific value, it is necessary to set
the corresponding control state to \'\'\'Manual\'\'\' (3), otherwise the
corresponding value will be ignored unless the device is already in the
\'\'\'Manual\'\'\' state when the driver starts.

For example, to set \`brightness\` to 256 on the command line:
```
$ rosrun camera1394 camera1394_node _auto_brightness:=3 _brightness:=256.0
```

## Bayer filtering

Many IIDC cameras use
[Bayer filtering](http://en.wikipedia.org/wiki/Bayer_filter) to provide
color information. For cameras of this type, set \`video_mode\` to an
appropriate \`mono8\` value, and select the correct \`bayer_pattern\`.
If the \`bayer_pattern\` is \`\"\"\`, all \`mono8\` images are
monochrome.

This driver provides two alternate mechanisms for decoding Bayer color
information:

-   Standard ROS [image_pipeline](image_pipeline) decoding.

To use this, set the \`bayer_method\` parameter to \`\"\"\` (the
default). This is the preferred method, it behaves like the other ROS
camera drivers.

-   Built-in decoding provided by
    [libdc1394 conversions](http://damien.douxchamps.net/ieee1394/libdc1394/v2.x/api/conversions)
    (\'\'now Deprecated\'\').

To use this, select one of the other \`bayer_method\` options. They may
have less CPU overhead in some systems, in others they may slow down the
camera frame rate since decoding is done in the main driver thread.
Performance depends on image size, decoding method, CPU speed and number
of processors available. Experimenting with the different options may
reveal the best setting for a specific camera and system.

Best performance is likely to come from using the default
\`bayer_decoding\` method while running \`image_proc/debayer\` and
\`camera1394/driver\` nodelets both in a single process (see the
[camera1394_nodelet](#camera1394_nodelet) example below).

In both cases the \`camera/image_raw\` image stream is compatible with
the ROS \`image_pipeline\`.

## Format7

IIDC Format7 provides more flexible control of the image. Available
options and modes vary greatly between different camera makes and
models. Some do not support Format7 at all. Consult the documentation
for your particular device to see what it provides.

Format7 parameters specify image size, position and pixel format. Some
Format7 modes may provide binning, combining groups of hardware pixels
into a single image pixel. The Format7 Region of Interest (ROI) selects
a rectangular subset from the full hardware image. These options
sometimes allow the camera to send images at a faster rate. (The
\`frame_rate\` parameter has no effect in Format7.)

With an available \`video_mode\` selected, a number of Format7-specific
parameters \'\'may\'\' be supported, depending on the device:

-   \`binning_x\` and \`binning_y\` are typically determined by the
    specific Format7 mode selected, but may need to be provided if the
    driver fails to automatically detect them.
-   \`roi_width\` and \`roi_height\` specify ROI size in units of
    unbinned pixels.
-   \`x_offset\` and \`y_offset\` specify top left corner of the ROI, in
    unbinned pixels.
-   \`format7_color_coding\` defines the pixel format.

For devices providing Bayer color coding, use the \`raw8\` coding and
specify the default \`bayer_method\`, \'\'the other Bayer methods are
not supported for Format7\'\'. The camera should normally define its own
\`bayer_pattern\` in this mode.

All these parameters are ignored when \`video_mode\` is not one of the
Format7 options.

## ROS API

```clearsilver
node.0 {
name=camera1394_node
desc=IEEE 1394 digital camera driver.
pub{
0.name=camera/image_raw
0.type=sensor_msgs/Image
0.desc=A stream of images from the camera.
1.name=camera/camera_info
1.type=sensor_msgs/CameraInfo
1.desc=Camera intrinsics for images published on `camera/image_raw` with matching time stamps and frame IDs. If !CameraInfo calibration is not available or is incompatible with the current `video_mode`, uncalibrated data will be provided instead.
2.name=diagnostics
2.type=diagnostic_msgs/DiagnosticStatus
2.desc=Diagnostic status, with camera frame rate (<<Version(fuerte)>>).
}
srv{
1.name=camera/set_camera_info
1.type=sensor_msgs/SetCameraInfo
1.desc=Set the camera's calibration.
}
# Autogenerated param section. Lightly edit by hand...
# Autogenerated param section. Lightly hand edited.
param {
group.0 {
name=Dynamically Reconfigurable Parameters
desc=See the [[dynamic_reconfigure]] package for details on dynamically reconfigurable parameters.
0.name= ~guid
0.default= 
0.type= str
0.desc=Global Unique ID of camera, 16 hex digits (use first camera if null). 
1.name= ~reset_on_open
1.default= False
1.type= bool
1.desc=Reset camera when opening the device. 
2.name= ~video_mode
2.default= 640x480_mono8
2.type= str
2.desc=IIDC video mode. Possible values are: Format0_Mode0 (160x120_yuv444): , Format0_Mode1 (320x240_yuv422): , Format0_Mode2 (640x480_yuv411): , Format0_Mode3 (640x480_yuv422): , Format0_Mode4 (640x480_rgb8): , Format0_Mode5 (640x480_mono8): , Format0_Mode6 (640x480_mono16): , Format1_Mode0 (800x600_yuv422): , Format1_Mode1 (800x600_rgb8): , Format1_Mode2 (800x600_mono8): , Format1_Mode6 (800x600_mono16): , Format1_Mode3 (1024x768_yuv422): , Format1_Mode4 (1024x768_rgb8): , Format1_Mode5 (1024x768_mono8): , Format1_Mode7 (1024x768_mono16): , Format2_Mode0 (1280x960_yuv422): , Format2_Mode1 (1280x960_rgb8): , Format2_Mode2 (1280x960_mono8): , Format2_Mode6 (1280x960_mono16): , Format2_Mode3 (1600x1200_yuv422): , Format2_Mode4 (1600x1200_rgb8): , Format2_Mode5 (1600x1200_mono8): , Format2_Mode7 (1600x1200_mono16): , Format7_Mode0 (format7_mode0): , Format7_Mode1 (format7_mode1): , Format7_Mode2 (format7_mode2): , Format7_Mode3 (format7_mode3): , Format7_Mode4 (format7_mode4): , Format7_Mode5 (format7_mode5): , Format7_Mode6 (format7_mode6): , Format7_Mode7 (format7_mode7): 
3.name= ~frame_id
3.default= camera
3.type= str
3.desc=ROS tf frame of reference, resolved with tf_prefix unless absolute. 
4.name= ~frame_rate
4.default= 15.0
4.type= double
4.desc=Camera speed (frames per second). Range: 1.875 to 240.0
5.name= ~iso_speed
5.default= 400
5.type= int
5.desc=Total IEEE 1394 bus bandwidth (Megabits/second). Range: 100 to 3200
6.name= ~camera_info_url
6.default= 
6.type= str
6.desc=Camera [[camera_info_manager#URL_Names|calibration URL]] for this video_mode (uncalibrated if null). 
7.name= ~binning_x
7.default= 0
7.type= int
7.desc=Number of pixels combined for Format7 horizontal binning, use device hints if zero. Range: 0 to 4
8.name= ~binning_y
8.default= 0
8.type= int
8.desc=Number of pixels combined for Format7 vertical binning, use device hints if zero. Range: 0 to 4
9.name= ~roi_width
9.default= 0
9.type= int
9.desc=Width of Format7 Region of Interest in unbinned pixels, full width if zero. Range: 0 to 65535
10.name= ~roi_height
10.default= 0
10.type= int
10.desc=Height of Format7 Region of Interest in unbinned pixels, full height if zero. Range: 0 to 65535
11.name= ~x_offset
11.default= 0
11.type= int
11.desc=Horizontal offset for left side of Format7 ROI in unbinned pixels. Range: 0 to 65535
12.name= ~y_offset
12.default= 0
12.type= int
12.desc=Vertical offset for top of Format7 ROI in unbinned pixels. Range: 0 to 65535
13.name= ~format7_packet_size
13.default= 0
13.type= int
13.desc=Format7 packet size (bytes), device-recommended size if zero. Range: 0 to 39320
14.name= ~format7_color_coding
14.default= mono8
14.type= str
14.desc=Color coding (only for Format7 modes) Possible values are: "mono8", "mono16", "mono16s", "raw8", "raw16", "rgb8", "rgb16", "rgb16s", "yuv411", "yuv422", "yuv444"
15.name= ~bayer_pattern
15.default= 
15.type= str
15.desc=Bayer color encoding pattern (default: ""). Possible values are: "": No Bayer encoding, "rggb", "gbrg", "grbg", "bggr". 
16.name= ~bayer_method
16.default= 
16.type= str
16.desc=Bayer decoding method (default: ROS image_proc). Possible values are: "": Decode via ROS image_proc, "!DownSample", "Simple", "Bilinear", "HQ", "VNG", "AHD"
17.name= ~auto_brightness
17.default= 1
17.type= int
17.desc=Brightness control state. Possible values are: Off (0): Use fixed value, Query (1): Query current values, Auto (2): Camera sets continuously, Manual (3): Use explicit value, !OnePush (4): Camera sets once, None (5): Feature not available
18.name= ~brightness
18.default= 0.0
18.type= double
18.desc=Black level offset. Range: 0.0 to 4095.0
19.name= ~auto_exposure
19.default= 1
19.type= int
19.desc=Combined Gain, Iris & Shutter control. Possible values are: Off (0): Use fixed value, Query (1): Query current values, Auto (2): Camera sets continuously, Manual (3): Use explicit value, !OnePush (4): Camera sets once, None (5): Feature not available
20.name= ~exposure
20.default= 0.0
20.type= double
20.desc=Auto exposure value (like contrast). Range: -10.0 to 4095.0
21.name= ~auto_focus
21.default= 1
21.type= int
21.desc=Focus control state. Possible values are: Off (0): Use fixed value, Query (1): Query current values, Auto (2): Camera sets continuously, Manual (3): Use explicit value, !OnePush (4): Camera sets once, None (5): Feature not available
22.name= ~focus
22.default= 0.0
22.type= double
22.desc=Focus control. Range: 0.0 to 4095.0
23.name= ~auto_gain
23.default= 1
23.type= int
23.desc=Gain control state. Possible values are: Off (0): Use fixed value, Query (1): Query current values, Auto (2): Camera sets continuously, Manual (3): Use explicit value, !OnePush (4): Camera sets once, None (5): Feature not available
24.name= ~gain
24.default= 0.0
24.type= double
24.desc=Relative circuit gain. Range: -10.0 to 4095.0
25.name= ~auto_gamma
25.default= 1
25.type= int
25.desc=Gamma control state. Possible values are: Off (0): Use fixed value, Query (1): Query current values, Auto (2): Camera sets continuously, Manual (3): Use explicit value, !OnePush (4): Camera sets once, None (5): Feature not available
26.name= ~gamma
26.default= 2.2
26.type= double
26.desc=Gamma expansion exponent. Range: 0.0 to 10.0
27.name= ~auto_hue
27.default= 1
27.type= int
27.desc=Hue control state. Possible values are: Off (0): Use fixed value, Query (1): Query current values, Auto (2): Camera sets continuously, Manual (3): Use explicit value, !OnePush (4): Camera sets once, None (5): Feature not available
28.name= ~hue
28.default= 0.0
28.type= double
28.desc=Color phase. Range: 0.0 to 4095.0
29.name= ~auto_iris
29.default= 1
29.type= int
29.desc=Iris control state. Possible values are: Off (0): Use fixed value, Query (1): Query current values, Auto (2): Camera sets continuously, Manual (3): Use explicit value, !OnePush (4): Camera sets once, None (5): Feature not available
30.name= ~iris
30.default= 8.0
30.type= double
30.desc=Iris control. Range: 0.0 to 4095.0
31.name= ~auto_saturation
31.default= 1
31.type= int
31.desc=Saturation control state. Possible values are: Off (0): Use fixed value, Query (1): Query current values, Auto (2): Camera sets continuously, Manual (3): Use explicit value, !OnePush (4): Camera sets once, None (5): Feature not available
32.name= ~saturation
32.default= 1.0
32.type= double
32.desc=Color saturation. Range: 0.0 to 4095.0
33.name= ~auto_sharpness
33.default= 1
33.type= int
33.desc=Sharpness control state. Possible values are: Off (0): Use fixed value, Query (1): Query current values, Auto (2): Camera sets continuously, Manual (3): Use explicit value, !OnePush (4): Camera sets once, None (5): Feature not available
34.name= ~sharpness
34.default= 1.0
34.type= double
34.desc=Image sharpness. Range: 0.0 to 4095.0
35.name= ~auto_shutter
35.default= 1
35.type= int
35.desc=Shutter control state. Possible values are: Off (0): Use fixed value, Query (1): Query current values, Auto (2): Camera sets continuously, Manual (3): Use explicit value, !OnePush (4): Camera sets once, None (5): Feature not available
36.name= ~shutter
36.default= 1.0
36.type= double
36.desc=Shutter speed. Range: 0.0 to 4095.0
37.name= ~auto_white_balance
37.default= 1
37.type= int
37.desc=White balance control state. Possible values are: Off (0): Use fixed value, Query (1): Query current values, Auto (2): Camera sets continuously, Manual (3): Use explicit value, !OnePush (4): Camera sets once, None (5): Feature not available
38.name= ~white_balance_BU
38.default= 0.0
38.type= double
38.desc=Blue or U component of white balance. Range: 0.0 to 4095.0
39.name= ~white_balance_RV
39.default= 0.0
39.type= double
39.desc=Red or V component of white balance. Range: 0.0 to 4095.0
40.name= ~auto_zoom
40.default= 1
40.type= int
40.desc=Zoom control state. Possible values are: Off (0): Use fixed value, Query (1): Query current values, Auto (2): Camera sets continuously, Manual (3): Use explicit value, !OnePush (4): Camera sets once, None (5): Feature not available
41.name= ~zoom
41.default= 0.0
41.type= double
41.desc=Zoom control. Range: 0.0 to 4095.0
50.name= ~num_dma_buffers
50.default= 4
50.type= int
50.desc= Number of frames in the DMA ring buffer (<<Version(indigo)>>).
51.name= ~max_consecutive_errors
51.default= 0 (disabled)
51.type= int
51.desc= Max number of consecutive read errors before attempting reconnection (0 to disable)
}
}
# End of autogenerated section. You may edit below.
```

### camera1394_nodelet

Nodelet version of the camera1394 driver.

This driver publishes the same topics and provides the same parameters
as the [camera1394_node](#camera1394_node) version.

#### Examples

Run a standalone \`camera1394_nodelet\`, this behaves almost the same as
running \`camera1394_node\`. \'\'Running the nodelet standalone does not
provide zero-copy message sharing.\'\' For that, see the following
example. ```
$ rosrun nodelet nodelet standalone camera1394/driver
```

To run the driver nodelet and [image_proc](image_proc) all in a single
address space with zero-copy message passing between those nodelets, use
a [roslaunch XML file](roslaunch/XML) like this:

```
<launch>

  <!-- nodelet manager process -->
  <node pkg="nodelet" type="nodelet" name="camera_nodelet_manager"
        args="manager" />

  <!-- camera driver nodelet -->
  <node pkg="nodelet" type="nodelet" name="camera1394_nodelet"
        args="load camera1394/driver camera_nodelet_manager" />
    
  <!-- Bayer color decoding -->
  <node pkg="nodelet" type="nodelet" name="image_proc_debayer"
	args="load image_proc/debayer camera_nodelet_manager">
    <remap from="image_color" to="camera/image_color" />
    <remap from="image_mono" to="camera/image_mono" />
    <remap from="image_raw" to="camera/image_raw" />
  </node>

  <!-- mono rectification -->
  <node pkg="nodelet" type="nodelet" name="image_proc_rect"
	args="load image_proc/rectify camera_nodelet_manager">
    <remap from="image_mono" to="camera/image_mono" />
    <remap from="image_rect" to="camera/image_rect" />
  </node>

  <!-- color rectification -->
  <node pkg="nodelet" type="nodelet" name="image_proc_rect_color"
	args="load image_proc/rectify camera_nodelet_manager">
    <remap from="image_mono" to="camera/image_color" />
    <remap from="image_rect" to="camera/image_rect_color" />
  </node>

</launch>
```

Depending on specific needs, some of the \`image_proc\` nodelets could
be omitted. But, they do not incur much overhead when not being used.
