## Overview

This package provides a ROS interface to the Microsoft Kinect using the
libfreenect library from
[OpenKinect](http://openkinect.org/wiki/Main_Page). Other devices using
the [OpenNI standard](http://www.openni.org) are currently not
supported. Please see the section on
[other OpenNI devices](#Other_OpenNI_devices) for more information:

[freenect_launch](freenect_launch) contains some convenience scripts
that can be used to run this driver.

The goal of this libfreenect based driver is to provide a substitute to
the OpenNI based ROS driver ([openni_camera](openni_camera)). Migration
is easy and documented [below](#Migration_guide).

Dev Mailing List: ros-freenect-dev@googlegroups.com

## ROS API

The ROS API is extremely similar to that of
[openni_camera](openni_camera). Any differences are described in the API
and the [migration guide](#Migration_guide).

```clearsilver
node.0 {
  name = freenect_node
  desc = libfreenect camera driver.
  pub {
    group.0 {
      name = RGB camera
      0.name = rgb/camera_info
      0.type = sensor_msgs/CameraInfo
      0.desc = Camera calibration and metadata.
      1.name = rgb/image_raw
      1.type = sensor_msgs/Image
      1.desc = Raw image from device. Format is Bayer GRBG for Kinect.
    }
    group.1 {
      name = Depth camera
      desc = Published only when `~depth_registration` is false (device registration disabled).
      0.name = depth/camera_info
      0.type = sensor_msgs/CameraInfo
      0.desc = Camera calibration and metadata.
      1.name = depth/image_raw
      1.type = sensor_msgs/Image
      1.desc = Raw image from device. Contains `uint16` depths in mm.
    }
    group.2 {
      name = Registered depth camera (aligned with RGB camera)
      desc = Published directly by driver only when `~depth_registration` is true (device registration enabled).
      0.name = depth_registered/camera_info
      0.type = sensor_msgs/CameraInfo
      0.desc = Camera calibration and metadata. Same as `rgb/camera_info` but time-synced to `depth_registered/image_raw`.
      1.name = depth_registered/image_raw
      1.type = sensor_msgs/Image
      1.desc = Raw image from device. Contains `uint16` depths in mm.
    }
    group.3 {
      name = IR camera
      desc = Published by the driver only when no subscriptions to the rgb image exist.
      0.name = ir/camera_info
      0.type = sensor_msgs/CameraInfo
      0.desc = Camera calibration and metadata.
      1.name = ir/image_raw
      1.type = sensor_msgs/Image
      1.desc = Raw `uint16` IR image.
    }
    group.4 {
      name = IR projector
      0.name = projector/camera_info
      0.type = sensor_msgs/CameraInfo
      0.desc = Faked calibration for the IR projector. Identical to `depth/camera_info`, but with the baseline encoded in the P matrix. Stereo processing nodes can use the `depth` and `projector` infos as a left/right pair.
    }
    group.5 {
      name = [new in freenect_camera] Diagnostics
      0.name = /diagnostics
      0.type = diagnostic_msgs/DiagnosticArray
      0.desc = Simple topic frequency diagnostics for RGB, Depth and IR images. Only published if enabled through parameters described below. 

    }
  }
  param {
    group.0 {
      0.name = ~device_id
      0.type = string
      0.default = #1
      0.desc << EOM
'''[different in freenect_camera]''' Specifies which device to open. The following formats are recognized:
    ||#1              ||Use first device found             ||
    ||B00367707227042B||Use device with given serial number||
EOM
      1.name = ~rgb_frame_id
      1.default = `/openni_rgb_optical_frame`
      1.type = string
      1.desc = The [[tf]] frame of the RGB camera.
      2.name = ~depth_frame_id
      2.default = `/openni_depth_optical_frame`
      2.type = string
      2.desc = The [[tf]] frame of the IR/depth camera.
      3.name = ~rgb_camera_info_url
      3.type = string
      3.default = `file://${ROS_HOME}/camera_info/${NAME}.yaml`
      3.desc = [[camera_info_manager#URL_Names|Calibration URL]] for the RGB camera. By default, looks in your ROS home directory for calibration identified by the device serial number, e.g. `$HOME/.ros/camera_info/rgb_B00367707227042B`. If no calibration is found, uses a default camera model with a typical focal length and distortion unmodeled.
      4.name = ~depth_camera_info_url
      4.type = string
      4.default = `file://${ROS_HOME}/camera_info/${NAME}.yaml`
      4.desc = [[camera_info_manager#URL_Names|Calibration URL]] for the IR/depth camera. By default, looks in your ROS home directory for calibration identified by the device serial number, e.g. `$HOME/.ros/camera_info/depth_B00367707227042B`. If no calibration is found, uses a default camera model with the focal length reported by the device and distortion unmodeled.
      5.name = ~time_out
      5.type = double
      5.desc = If set, checks every `~time_out` seconds whether active cameras have streamed new data.
      6.name = ~debug
      6.type = bool
      6.default = false
      6.desc = '''[new in freenect_camera]''' If set, enables verbose libfreenect output useful for debugging errors.
    }
    group.1 {
      name = [new in freenect_camera] Diagnostics Parameters
      0.name = enable_rgb_diagnostics
      0.type = bool
      0.default = false
      0.desc = If set, enables simple frequency based topic diagnostics on RGB Image publication (`rgb/image_raw`) that can be viewed through `robot_monitor`.
      1.name = enable_ir_diagnostics
      1.type = bool
      1.default = false
      1.desc = If set, enables simple frequency based topic diagnostics on IR Image publication (`ir/image_raw`) that can be viewed through `robot_monitor`.
      2.name = enable_depth_diagnostics
      2.type = bool
      2.default = false
      2.desc = If set, enables simple frequency based topic diagnostics on Depth Image publication (`depth/image_raw` OR `depth_registered/image_raw`) that can be viewed through `robot_monitor`.
      3.name = diagnostics_max_frequency
      3.type = double
      3.default = 30.0
      3.desc = The maximum frequency expected by diagnostics for any enabled topic (in hz).
      4.name = diagnostics_min_frequency
      4.type = double
      4.default = 30.0
      4.desc = The minimum frequency expected by diagnostics for any enabled topic (in hz).
      5.name = diagnostics_tolerance
      5.type = double
      5.default = 0.05
      5.desc = The amount beyond min/max where diagnostics won't generate a warning. For the default values. this means a frequency between 28.5 and 31.5 hz.
      6.name = diagnostics_window_time
      6.type = double
      6.default = 5.0
      6.desc = The duration of the window that diagnostics uses to monitor a topic (in seconds).
    }
    group.2 {
# Autogenerated param section. Do not hand edit.
name=Dynamically Reconfigurable Parameters
desc=See the [[dynamic_reconfigure]] package for details on dynamically reconfigurable parameters.
0.name= ~image_mode
0.default= 2
0.type= int
0.desc='''[different in freenect_camera]''' Image output mode Possible values are: SXGA (1): 1280x1024, VGA (2): 640x480. '''SXGA should be considered unstable'''
1.name= ~depth_mode
1.default= 2
1.type= int
1.desc='''[different in freenect_camera]''' Depth output mode Possible values are: SXGA (1): 1280x1024, VGA (2): 640x480. '''SXGA is not supported for depth mode'''
2.name= ~depth_registration
2.default= True
2.type= bool
2.desc=Depth data registration 
3.name= ~data_skip
3.default= 0
3.type= int
3.desc=Skip N images for every image published (rgb/depth/depth_registered/ir) Range: 0 to 10
4.name= ~depth_time_offset
4.default= 0.0
4.type= double
4.desc=depth image time offset in seconds Range: -1.0 to 1.0
5.name= ~image_time_offset
5.default= 0.0
5.type= double
5.desc=image time offset in seconds Range: -1.0 to 1.0
6.name= ~depth_ir_offset_x
6.default= 5.0
6.type= double
6.desc=X offset between IR and depth images Range: -10.0 to 10.0
7.name= ~depth_ir_offset_y
7.default= 4.0
7.type= double
7.desc=Y offset between IR and depth images Range: -10.0 to 10.0
8.name= ~z_offset_mm
8.default= 0
8.type= int
8.desc=Z offset in mm Range: -50 to 50
# End of autogenerated section. You may edit below.
    }
  }
  srv {
    0.name = rgb/set_camera_info
    0.type = sensor_msgs/SetCameraInfo
    0.desc = Set the RGB camera calibration.
    1.name = ir/set_camera_info
    1.type = sensor_msgs/SetCameraInfo
    1.desc = Set the IR camera calibration.
  }
}
node.1 {
  name = freenect_camera/driver nodelet
  desc = Nodelet version of the freenect driver. Has the same ROS API as `freenect_node` above.
}
```

## Migration guide

This guide assumes that you are using the
[freenect_launch](freenect_launch) package to launch the driver. If not,
migration is non-trivial but not overly difficult, and can be done by
studying the differences between [freenect_launch](freenect_launch) and
[openni_launch](openni_launch).

### Migrating to openni_camera

1\. Replace the freenect launch file in your code with the corresponding
openni launch file. (\`\$(find freenect_launch)/launch/freenect.launch\`
-\> \`\$(find openni_launch)/launch/openni.launch\`). No other
modifications should be necessary. 2. openni_launch does not support
diagnostics or appending a namespace as of v1.8.3. Modify your system
accordingly. \'\'Note: A ticket for ns addition to openni_launch has
been filed [#63](https://kforge.ros.org/openni/trac/ticket/63)
[#64](https://kforge.ros.org/openni/trac/ticket/64)\'\'

### Migrating from openni_camera

1\. Replace the openni launch file in your code with the corresponding
freenect launch file. (\`\$(find openni_launch)/launch/openni.launch\`
-\> \`\$(find freenect_launch)/launch/freenect.launch\`). 2. If you were
using the default \`image_mode\` or \`depth_mode\` parameters in the
openni_camera driver, then please skip this step. \`freenect_camera\`
does not support a number of image/depth modes supported by the
[openni_camera](openni_camera) driver. Please use one of modes mentioned
in the parameters above (SXGA equivalent to SXGA_15Hz), or (VGA
equivalent to VGA_30Hz). SXGA should be considered unstable. 3. If you
were using the bus/address method of searching for the device, then it
is no longer supported. Please consult the parameters above on other
methods of selecting devices.

## Other OpenNI devices

There are a couple of reasons why other devices using the OpenNI
standard (namely the Primesense PSDK, Asus Xtion Pro and Pro Live) are
not currently supported: 1. \`libfreenect\` hardcodes information about
the Kinect in a way that makes it difficult to gain access to different
types of OpenNI devices using the same code. It might be easy to patch
libfreenect to use these other devices, generate separate libraries for
each device, and make multiple binaries of the driver linking against
each library separately. 2. Information about each device will have to
be reverse engineered from the OpenNI driver to modify \`libfreenect\`.
A port for the Asus Xtion Pro is available
[here](https://github.com/zarvox/libfreenect/tree/xtion) (thanks for
pointing to this Ivan!). A read through the differences reveal that the
changes are not big, but require knowledge about the commands that need
to be passed to each device using libusb. It is currently not clear how
easy this task is.
