**Fuerte (or older ROS release) checkout:** git clone
<https://github.com/anqixu/ueye_cam.git> \--branch fuerte

## Overview

This package provides a ROS interface for the
[UEye digital cameras from IDS Imaging Development Systems GMBH](http://www.ids-imaging.com/frontend/groups.php).
This ROS interface exposes many of the features of the underlying
[Linux camera API from IDS](http://www.ids-imaging.com/drivers.php?cat=2),
and is compatible with [image_pipeline](image_pipeline),
[camera_calibration](camera_calibration), and
[image_geometry](image_geometry).

This package has been tested with the **Software Package for USB and
GigE uEye Cameras Version 4.20 64 Bit for Linux**, on **Ubuntu 12.04 x64
& Ubuntu 13.04 x64**, operating with **UEye UI122xLE-C USB 2.0**
cameras.

The package with the version 1.0.17
([Github Release](https://github.com/anqixu/ueye_cam/releases/tag/1.0.17))
has been tested with the **Software Package for USB uEye Cameras Version
4.94 64 Bit for Linux** and **ROS Noetic**, on **Ubuntu 20.04 x64**,
operating with **UEye UI-3240LE-M-GL USB 3.0** camera.

(side-note: it is technically possible to
[run ueye_cam on ARM devices](http://youtu.be/nU1u6vHoZ-I); see video
caption for outline of instructions)

This implementation makes use of certain C++11 features (such as
std::thread, std::to_string, etc), although the CMakeLists.txt is
configured for GCC \>= 4.6 (and hence uses the *-std=c++0x* flag).

## Features

-   implemented as a [nodelet](nodelet)
-   supports loading from IDS camera parameter files (e.g. obtained from
    *ueyedemo*)
-   supports publishing frames as \"rgb8\", \"mono8\", and
    \"bayer_rggb8\" (depending on camera model)
-   camera is deactivated unless there is a subscriber to the published
    image topic
-   supports dynamic tuning of various camera parameters via
    [dynamic_reconfigure](dynamic_reconfigure); e.g. gain, exposure,
    frame rate, etc\...
-   supports external triggering mode, and can allow multiple cameras to
    synchronize exposure and frame grabs (with hardware modifications)

![](attachment:Screenshot-Reconfigure.png)

### Clock Rate

The IDS camera API allows users to have fine-grain control over the
camera on-board processor\'s clock rate, which determines the range of
values for frame rates, exposures, and other camera settings. This can
be adjusted at runtime alongside other parameters, via
[dynamic_reconfigure](dynamic_reconfigure). It is however not
recommended to operate the camera at a fast clock rate for extended
periods of time, as the onboard processor may get excessively hot. Thus,
ideally one should adjust the clock rate to match a target frame rate
and exposure setting.

### Bayer Decoding

You may choose to use the underlying IDS camera API to perform bayer
decoding and publish images as \'rgb8\' or \'mono8\', or alternatively
choose to publish images as \'bayer_rggb8\' and rely on the standard ROS
[image_pipeline](image_pipeline) package for decoding. Currently, this
ROS interface does not expose fine-grain control over the bayer decoding
engine from the underlying IDS camera API.

### Reduced Area of Interest (AOI) vs. Down-sampled Images

A common mistake is to interpret the \'image_width\' and
\'image_height\' ROS parameters as the width and height of the resulting
ROS image. Unfortunately, these names were chosen to be consistent with
official camera interfaces provided by IDS, and they refer to the width
and height of the camera sensor\'s Area of Interest (AOI). Therefore,
values for \'image_width\' and \'image_height\' that are smaller than
your camera\'s maximum values will result in **cropped field of view**
(a.k.a. reduced AOI).

For typical use cases, one should modify values for \'sensor_scaling\' /
\'binning\' / \'subsampling\' parameters, in order to down-sample the
resulting ROS image to the desired dimensions without reducing the field
of view.

Note that all parameters (both rosparam, roslaunch, and dynamic
reconfigure) will be automatically capped to valid ranges / values for
your camera\'s model, upon change. You can also run the \'ueyedemo\'
official camera interface to obtain bounds and current values for the
camera\'s onboard parameters (which ueye_cam tries faithfully to
replicate in ROS).

## Build Instructions

1\. Install the IDS Software Suite 4.xx for Linux from
[here](http://en.ids-imaging.com/download-ueye.html)

-   Pay attention to start the UEye daemon after installation is
    complete, by running *sudo /etc/init.d/ueye\<usb/eth\>drc start*.
    This is not necessary after a system reboot.
-   **update**: even though ueye_cam will automatically download a
    barebone version of the IDS driver if not present for compilation,
    the daemon (and thus the official IDS driver) is still needed in
    order to connect and grab frames from an uEye camera 2. create
    catkin workspace *mkdir -p \<your_ueye_cam_ws\>/src*.

3\. initialize and download source code

*cd \<your_ueye_cam_ws\>/src && wstool init && wstool set ueye_cam
\--git <https://github.com/anqixu/ueye_cam> && wstool update && cd ..*.

4\. Run *catkin_make* under *\<your_ueye_cam_ws\>*.

## ROS API

```clearsilver
node.0 {
name=ueye_cam
desc=ROS interface node for UEye digital cameras from IDS Imaging Development Systems. '''No longer available from ROS Groovy onwards; use nodelet + launch files directly.'''
pub{
0.name=<camera_name>/<camera_topic>
0.type=sensor_msgs/Image
0.desc=A stream of images from the camera.
1.name=<camera_name>/camera_info
1.type=sensor_msgs/CameraInfo
1.desc=Camera intrinsic parameters associated to published images on `<~camera_name>/<~camera_topic>`, with matching time stamps and frame IDs.
}
srv{
1.name=<~camera_name>/set_camera_info
1.type=sensor_msgs/SetCameraInfo
1.desc=Updates the camera's intrinsic parameters for calibration purposes, and saves to <~camera_intrinsics_file>.
}

param {
group.0 {
name=Load-time Parameters
desc=Static parameters loaded during initialization of the interface. Please refer to ''launch/rgb8.launch'' for an example.
0.name= ~camera_name
0.default= camera
0.type= string
0.desc=Camera name, used as the local ROS namespace.
1.name= ~camera_topic
1.default= image_raw
1.type= string
1.desc=Images will be published on <~camera_name>/<~camera_topic>.
2.name= ~camera_id
2.default= 0
2.type= int
2.desc= Camera ID (when interfacing with multiple connected UEye cameras). 0 = first / any available camera.
3.name= ~camera_parameters_file
3.default= ''<ueye_cam_path>/camera_conf/<~camera_name>.ini''
3.type= string
3.desc='''(OPTIONAL)''' Path to IDS camera parameter file. These parameters are loaded prior to the subset of paramters that are exposed by the ROS interface.
4.name= ~camera_intrinsics_file
4.default= ''<ueye_cam_path>/camera_info/<~camera_name>.yaml''
4.type= string
4.desc='''(OPTIONAL)''' Path to the camera intrinsics file.
}
# Autogenerated param section. Do not hand edit.
group.1 {
name=Dynamically Reconfigurable Parameters
desc=See the [[dynamic_reconfigure]] package for details on dynamically reconfigurable parameters.
0.name= ~image_width
0.default= 640
0.type= int
0.desc=Width of camera's area of interest (prior to subsampling, binning, or sensor scaling) Range: 16 to 2560
1.name= ~image_height
1.default= 480
1.type= int
1.desc=Height of camera's area of interest (prior to subsampling, binning, or sensor scaling) Range: 4 to 1920
2.name= ~image_left
2.default= -1
2.type= int
2.desc=Left index for camera's area of interest (-1: center) Range: -1 to 2544
3.name= ~image_top
3.default= -1
3.type= int
3.desc=Top index for camera's area of interest (-1: center) Range: -1 to 1916
4.name= ~color_mode
4.default= mono8
4.type= str
4.desc=Output image color mode Possible values are: MONO8 (mono8): 8-bit Monochrome, RGB8 (rgb8): 24-bit Red/Green/Blue, BAYER_RGGB8 (bayer_rggb8): 8-bit Raw Bayer (RGGB)
5.name= ~subsampling
5.default= 1
5.type= int
5.desc=Output image subsampling ratio Possible values are: SUB_1X (1): 1X Subsampling, SUB_2X (2): 2X Subsampling, SUB_4X (4): 4X Subsampling, SUB_8X (8): 8X Subsampling, SUB_16X (16): 16X Subsampling
6.name= ~binning
6.default= 1
6.type= int
6.desc=Output image binning ratio Possible values are: BIN_1X (1): 1X Binning, BIN_2X (2): 2X Binning, BIN_4X (4): 4X Binning, BIN_8X (8): 8X Binning, BIN_16X (16): 16X Binning
7.name= ~sensor_scaling
7.default= 1.0
7.type= double
7.desc=Output image scaling ratio (Internal Image Scaling) Possible values are: SS_1X (1.0): 1X Internal Image Scaling, SS_2X (2.0): 2X Internal Image Scaling, SS_4X (4.0): 4X Internal Image Scaling, SS_8X (8.0): 8X Internal Image Scaling, SS_16X (16.0): 16X Internal Image Scaling
8.name= ~auto_gain
8.default= False
8.type= bool
8.desc=Auto gain (overruled by auto framerate) 
9.name= ~master_gain
9.default= 0
9.type= int
9.desc=Master gain percentage Range: 0 to 100
10.name= ~red_gain
10.default= 0
10.type= int
10.desc=Gain percentage for red channel Range: 0 to 100
11.name= ~green_gain
11.default= 0
11.type= int
11.desc=Gain percentage for red channel Range: 0 to 100
12.name= ~blue_gain
12.default= 0
12.type= int
12.desc=Gain percentage for red channel Range: 0 to 100
13.name= ~gain_boost
13.default= False
13.type= bool
13.desc=Analog gain boost 
14.name= ~auto_exposure
14.default= False
14.type= bool
14.desc=Auto exposure (a.k.a. auto shutter) 
15.name= ~exposure
15.default= 33.0
15.type= double
15.desc=Exposure value (ms) Range: 0.0 to 300.0
16.name= ~auto_white_balance
16.default= False
16.type= bool
16.desc=Auto white balance 
17.name= ~white_balance_red_offset
17.default= 0
17.type= int
17.desc=Red level offset for white balance Range: -50 to 50
18.name= ~white_balance_blue_offset
18.default= 0
18.type= int
18.desc=Blue level offset for white balance Range: -50 to 50
19.name= ~flash_delay
19.default= 0
19.type= int
19.desc=Flash output delay (us) [not applicable in external trigger mode] Range: -1000000 to 1000000
20.name= ~flash_duration
20.default= 1000
20.type= int
20.desc=Flash output duration (us) (0: set to exposure duration) [not applicable in external trigger mode] Range: 0 to 1000000
21.name= ~ext_trigger_mode
21.default= False
21.type= bool
21.desc=Toggle between external trigger mode and free-run mode 
22.name= ~auto_frame_rate
22.default= False
22.type= bool
22.desc=Auto frame rate (requires auto exposure, supercedes auto gain) [not applicable in external trigger mode] 
23.name= ~frame_rate
23.default= 10.0
23.type= double
23.desc=Frame rate (Hz) [not applicable in external trigger mode] Range: 0.01 to 200.0
24.name= ~pixel_clock
24.default= 25
24.type= int
24.desc=Pixel clock (MHz) Range: 1 to 100
}
}
# End of autogenerated section. You may edit below.
```

### ueye_cam_nodelet

This is a fully compatible nodelet version of ueye_cam. In fact,
ueye_cam is implemented as a standalone nodelet manager running this
nodelet.

## Sample Launch Files

All launch files are commented to facilitate modifications. Ideally, you
should have a quick look at each launch file before execution.

### launch/rgb8.launch

Most straight-forward use case \-- uses the UEye drivers to convert to
RGB (3\*8-bit) images, and publishes on /camera/image_raw.

### launch/bayer_rggb_image_proc.launch

Returns raw Bayer-encoded (RGGB encoding) images from the UEye camera,
and uses [image_proc](http://wiki.ros.org/image_proc) to convert to RGB
images. Also publishes on /camera/image_raw.

### launch/debug.launch

Same as rgb8.launch, but spawns the nodelet (manager) in gdb on a
separate screen. **Not recommended for typical use.**

### launch/master_slaves_rgb8.launch

Sample launch file to demonstrate external triggering mode for
synchronizing multiple UEye cameras. You will need to add additional
physical modifications to the cameras for this to work; see \'Camera
Synchronization\' section for more details.

**Do not use this launch file to operate a single UEye camera! Also, any
camera with the ROS parameter *external_trigger_mode* set to *True*, and
does not have a valid triggering signal, will not return valid images
and will behave unpredictably.**

## Camera Calibration

The ueye_cam wrapper fully supports
[camera_calibration](http://wiki.ros.org/camera_calibration). You can
refer to
[camera_calibration](http://www.ros.org/wiki/camera_calibration/Tutorials/MonocularCalibration)
for info on calibrating your own UEye cameras.

All calibration files are stored by default under:
*/.ros/camera_info/\<camera_name\>.yaml*

### Camera Synchronization

You can enable (falling-edge) external trigger mode via
dynamic_reconfigure. You will also need to connect a corresponding
trigger signal to the digital input pin on your cameras. If you would
like one camera in free-run mode to trigger other camera(s) in external
trigger mode, you can connect the digital output pin (flash) of the
master camera to the digital input pin(s) of the slave(s). Note that
currently, you will also need to either logically negate the active-high
flash output in hardware, or change the code slightly so that the flash
output emits active-low.

We have connected multiple cameras in hardware to an Arduino-compatible
device (a [TinyLily](http://tiny-circuits.com/products/tinylily/)),
which allows any camera to act as master and any number of other cameras
to act as slaves, and achieve synchronization seamlessly with unified
hardware add-on required. Please see
[here](http://github.com/anqixu/duino_projects/blob/master/ueye_cam_ext_trigger/ueye_cam_ext_trigger.ino)
for further documentation and instructions. A video demonstration of
UEye camera synchronization can be seen
[here](http://youtu.be/4wSGdMJMci4).

Please contact us if you would like further instructions on
synchronizing cameras.

## Footnote: Relationship to other ROS wrappers for UEye cameras

Historically speaking, ueye_cam was based on an earlier ROS package for
interfacing with PointGrey cameras. Given that the initial work on
ueye_cam was done prior to the release of other similar ROS wrappers
like [ueye](ueye) and [ueyecamera](ueyecamera), the original intention
was to keep this code internal so as to avoid contention. Nevertheless,
this code has since been released as result of a number of recent
requests, with the sole hope that it may benefit the ROS community.
Please check out the other packages to see which one will best suite
your needs.
