## Overview

This package provides ROS node(s) for using the Intel® RealSense™ R200,
F200 and SR300 cameras.

## Installation

### Installation Prerequisites

This package requires the [librealsense](librealsense) package as the
underlying camera drivers for all Intel® RealSense™ cameras. **BEFORE**
installing the realsense-camera package, follow the
[Install Prerequisites for librealsense](librealsense#Installation_Prerequisites).

### ROS Debian Package

Most users should only need to install the prebuilt ROS Debian packages.


```
sudo apt-get install 'ros-*-realsense-camera'
```

 This will also install the required
ros-<\*distro\*>-librealsense library on your system.

### Build from Source (rare usage)

If a user needs to debug this package or contribute changes/bug fixes to
the package, only then should the package need to be built from source.
Please closely follow the directions provided on the
[Building from sources](realsense_camera/Tutorials/Building_from_Sources)
page.

### Intel® RealSense™ Camera Firmware

To ensure you camera has the most current, supported firmware, please
review the
[librealsense compatible device information](https://github.com/IntelRealSense/librealsense#compatible-devices).
If the camera requires a firmware upgrade, please refer to the
[Intel® RealSense™ Camera software support](http://www.intel.com/realsense)
page. **Note**: Currently there is no native Linux tool for FW updates;
all updates require a system with Microsoft Windows.

### Supported Camera Types

-   Intel® RealSense™ R200
-   Intel® RealSense™ F200
-   Intel® RealSense™ SR300
-   Intel® RealSense™ ZR300

## Support / Feature Requests

Please
[submit requests or report bugs](https://github.com/intel-ros/realsense/issues)
concerning this package to the realsense_camera GitHub Issues.

## ROS API



```clearsilver
node.0 {
  name = realsense_camera_nodelet
  desc = The Intel® RealSense™ camera driver. <<BR>> '''Note''': By default, the driver uses a '''preset''' [[#Parameters|mode]] for each camera. To change the stream width, height, or FPS, see the [[http://wiki.ros.org/realsense_camera/Tutorials/change_camera_parameters|Changing Camera Parameters from the Default Presets]] tutorial.
  pub {
    group.0 {
      name = Color camera
      0.name = color/camera_info
      0.type = sensor_msgs/CameraInfo
      0.desc = Camera calibration and metadata.
      1.name = color/image_raw
      1.type = sensor_msgs/Image
      1.desc = Color rectified image. RGB format.
    }
    group.1 {
      name = Depth camera
      0.name = depth/camera_info
      0.type = sensor_msgs/CameraInfo
      0.desc = Camera calibration and metadata.
      1.name = depth/image_raw
      1.type = sensor_msgs/Image
      1.desc = Raw image from device. Contains `uint16` depths in mm.
      2.name = depth/points
      2.type = sensor_msgs/PointCloud2
      2.desc = Registered XYZRGB point cloud. By default, pointcloud is disabled.
    }
    group.2 {
      name = IR camera
      desc = Infra Red camera image
      0.name = ir/camera_info
      0.type = sensor_msgs/CameraInfo
      0.desc = Camera calibration and metadata.
      1.name = ir/image_raw
      1.type = sensor_msgs/Image
      1.desc = Raw `uint16` IR image.
    }
    group.3 {
      name = IR2 camera
      desc = Infra Red secondary camera image. Available only for '''R200''' and '''ZR300''' cameras.
      0.name = ir/camera_info
      0.type = sensor_msgs/CameraInfo
      0.desc = Camera calibration and metadata.
      1.name = ir/image_raw
      1.type = sensor_msgs/Image
      1.desc = Raw `uint16` IR image.
    }
    group.4 {
      name = Fisheye camera
      desc = Available only for '''ZR300''' cameras.
      0.name = fisheye/camera_info
      0.type = sensor_msgs/CameraInfo
      0.desc = Camera calibration and metadata.
      1.name = ir/image_raw
      1.type = sensor_msgs/Image 
      1.desc = Raw `uint16` fisheye view image.
    }
    group.5 {
      name = IMU
      desc = Available only for '''ZR300''' cameras.
      0.name = imu/data_raw 
      0.type = sensor_msgs/Imu
      0.desc = Each IMU topic message will either contain angular velocity or linear acceleration data. The element 0 of the associated covariance matrix will be set to -1 to indicate the absence of data. E.g. If the topic message does not contain angular velocity data, then the element 0 of the angular velocity covariance matrix will be set to -1.This topic message does not contain orientation data and hence the element 0 of the orientation covariance matrix will always be -1.
    }
  }
  param {
    group.0 {
name=Static Parameters
      0.name = mode
      0.type = string
      0.default = `preset`
      0.desc = Specify the mode to start camera streams. Mode comprises of height, width and fps. Preset mode enables default values whereas Manual mode enables the specified parameter values.
      1.name = serial_no
      1.type = string
      1.default = `blank`
      1.desc = Specify the serial_no to uniquely connect to a camera, especially if multiple cameras are detected by the nodelet. You may get the serial_no from the info stream by launching the default launch file.
      2.name = usb_port_id
      2.default = `blank`
      2.type = string
      2.desc = Alternatively to serial_no, this can be used to connect to a camera by its USB Port ID, which is a Bus Number-Port Number in the format "Bus#-Port#". If used with serial_no, both must match correctly for camera to be connected.
      3.name = camera_type
      3.default = `blank`
      3.type = string
      3.desc = Specify the type of the camera - "R200", "F200", "SR300" or "ZR300".
      4.name = enable_ir
      4.type = bool
      4.default = false
      4.desc = Specify if to enable or not the infrared camera(s). Note: On cameras with two Infrared streams, both will be enabled or disabled together.
      5.name = enable_depth
      5.type = bool
      5.default = true
      5.desc = Specify if to enable or not the depth camera.
      6.name = depth_width
      6.type = int
      6.default = 480 (R200/ZR300), 640 (F200/SR300)
      6.desc = Specify the depth camera width resolution.
      7.name = depth_height
      7.type = int
      7.default = 360 (R200/ZR300), 480 (F200/SR300)
      7.desc = Specify the depth camera height resolution.
      8.name = depth_fps
      8.type = int
      8.default = 60
      8.desc = Specify the depth camera FPS.
      9.name = enable_color
      9.type = bool
      9.default = true
      9.desc = Specify if to enable or not the color camera.
     10.name = color_width
     10.type = int
     10.default = 640
     10.desc = Specify the color camera width resolution.
     11.name = color_height
     11.type = int
     11.default = 480
     11.desc = Specify the color camera height resolution.
     12.name = color_fps
     12.type = int
     12.default = 60
     12.desc = Specify the color camera FPS.
     13.name = enable_fisheye
     13.type = bool
     13.default = true
     13.desc = Available only for '''ZR300''' cameras. Specify if to enable or not the fisheye camera.
     14.name = fisheye_width
     14.type = int
     14.default = 640
     14.desc = Available only for '''ZR300''' cameras. Specify the fisheye camera width resolution.
     15.name = fisheye_height
     15.type = int
     15.default = 480
     15.desc = Available only for '''ZR300''' cameras. Specify the fisheye camera height resolution.
     16.name = fisheye_fps
     16.type = int
     16.default = 60
     16.desc = Available only for '''ZR300''' cameras. Specify the fisheye camera FPS.
     17.name = enable_imu
     17.type = bool
     17.default = true
     17.desc = Available only for '''ZR300''' cameras. Specify if to enable or not the IMU sensor.
     18.name = enable_pointcloud
     18.type = bool
     18.default = false
     18.desc = Specify if to enable or not the native pointcloud. By default, it is set to false due to performance issues. '''This option is depreciated in favor of the [[rgbd_launch]] pointcloud and will be removed in the near future.'''
     19.name = enable_tf
     19.type = bool
     19.default = true
     19.desc = Specify if to enable or not the transform frames publication.
     20.name = enable_tf_dynamic ('''Added in 1.7.0''')
     20.type = bool
     20.default = false
     20.desc = Publish transform frames as dynamic; default is false = Static, true = Dynamic.
     21.name = base_frame_id
     21.type = string
     21.default = camera_link
     21.desc = Specify the base frame id of the camera.
     22.name = depth_frame_id
     22.type = string
     22.default = camera_depth_frame
     22.desc = Specify the depth frame id of the camera.
     23.name = depth_optical_frame_id
     23.type = string
     23.default = camera_depth_optical_frame
     23.desc = Specify the depth optical frame id of the camera.
     24.name = color_frame_id
     24.type = string
     24.default = camera_rgb_frame
     24.desc = Specify the color frame id of the camera.
     25.name = color_optical_frame_id
     25.type = string
     25.default = camera_rgb_optical_frame
     25.desc = Specify the color optical frame id of the camera.
     26.name = ir_frame_id
     26.type = string
     26.default = camera_ir_frame
     26.desc = Specify the IR frame id of the camera.
     27.name = ir_optical_frame_id
     27.type = string
     27.default = camera_ir_optical_frame
     27.desc = Specify the IR optical frame id of the camera.
     28.name = ir2_frame_id
     28.type = string
     28.default = camera_ir2_frame
     28.desc = Available only for '''R200''' and '''ZR300''' cameras. Specify the IR2 frame id of the camera.
     29.name = ir2_optical_frame_id
     29.type = string
     29.default = camera_ir2_optical_frame
     29.desc = Available only for '''R200''' and '''ZR300''' cameras. Specify the IR2 optical frame id of the camera.
     30.name = fisheye_frame_id
     30.type = string
     30.default = camera_fisheye_frame
     30.desc = Available only for '''ZR300''' camera. Specify the fisheye frame id of the camera.
     31.name = fisheye_optical_frame_id
     31.type = string
     31.default = camera_fisheye_optical_frame
     31.desc = Available only for '''ZR300''' camera. Specify the fisheye optical frame id of the camera.
     32.name = imu_frame_id
     32.type = string
     32.default = camera_imu_frame
     32.desc = Available only for '''ZR300''' camera. Specify the IMU frame id of the camera.
     33.name = imu_optical_frame_id
     33.type = string
     33.default = camera_imu_optical_frame
     33.desc = Available only for '''ZR300''' camera. Specify the IMU optical frame id of the camera.
    }
# Since the one node realsense_camera support multiple cameras, the documenter will need to manually change the group number for each camera and add text to identify the dynamic options for the camera; '''XXX camera'''
# cat devel/share/realsense_camera/docs/r200_paramsConfig.wikidoc
# Autogenerated param section. Do not hand edit.
group.1 {
name=R200 Dynamically Reconfigurable Parameters
desc='''R200 camera''' See the [[dynamic_reconfigure]] package for details on dynamically reconfigurable parameters.
0.name= ~enable_depth
0.default= True
0.type= bool
0.desc=Enable Depth 
1.name= ~color_backlight_compensation
1.default= 1
1.type= int
1.desc=Backlight Compensation Range: 0 to 4
2.name= ~color_brightness
2.default= 56
2.type= int
2.desc=Brightness Range: 0 to 255
3.name= ~color_contrast
3.default= 32
3.type= int
3.desc=Contrast Range: 16 to 64
4.name= ~color_gain
4.default= 32
4.type= int
4.desc=Gain Range: 0 to 256
5.name= ~color_gamma
5.default= 220
5.type= int
5.desc=Gamma Range: 100 to 280
6.name= ~color_hue
6.default= 0
6.type= int
6.desc=Hue Range: -2200 to 2200
7.name= ~color_saturation
7.default= 128
7.type= int
7.desc=Saturation Range: 0 to 255
8.name= ~color_sharpness
8.default= 0
8.type= int
8.desc=Sharpness Range: 0 to 7
9.name= ~color_white_balance
9.default= 6500
9.type= int
9.desc=White Balance Range: 2000 to 8000
10.name= ~color_exposure
10.default= 156
10.type= int
10.desc=Exposure Range: 39 to 10000
11.name= ~r200_lr_gain
11.default= 400
11.type= int
11.desc=LR Gain Range: 100 to 6399
12.name= ~r200_lr_exposure
12.default= 164
12.type= int
12.desc=LR Exposure Range: 1 to 164
13.name= ~color_enable_auto_white_balance
13.default= 1
13.type= int
13.desc=Enable Auto White Balance Range: 0 to 1
14.name= ~color_enable_auto_exposure
14.default= 1
14.type= int
14.desc=Enable Auto Exposure Range: 0 to 1
15.name= ~r200_lr_auto_exposure_enabled
15.default= 0
15.type= int
15.desc=Enable LR Auto Exposure Range: 0 to 1
16.name= ~r200_auto_exposure_top_edge
16.default= 0
16.type= int
16.desc=Auto Exposure Top Edge Range: 0 to 479
17.name= ~r200_auto_exposure_bottom_edge
17.default= 479
17.type= int
17.desc=Auto Exposure Bottom Edge Range: 0 to 479
18.name= ~r200_auto_exposure_left_edge
18.default= 0
18.type= int
18.desc=Auto Exposure Left Edge Range: 0 to 639
19.name= ~r200_auto_exposure_right_edge
19.default= 639
19.type= int
19.desc=Auto Exposure Right Edge Range: 0 to 639
20.name= ~r200_emitter_enabled
20.default= 1
20.type= int
20.desc=Emitter Enabled Range: 0 to 1
21.name= ~r200_dc_preset
21.default= 5
21.type= int
21.desc=R200 Depth Control Preset Possible values are: UNUSED (-1): Individual Depth Control was changed, Default (0): Default settings on chip. Similar to Medium. Best for Outdoors., Off (1): Disable almost all hardware-based outlier removal., Low (2): Lower number of outliers removed. Minimal false negatives., Medium (3): Medium number of outliers removed. Balanced approach., Optimized (4): Medium-High number of outliers removed. Derived optimization function., High (5): Higher number of outliers removed. Minimal false positives.
22.name= ~r200_dc_estimate_median_decrement
22.default= 5
22.type= int
22.desc=Estimate Median Decrement Range: 0 to 255
23.name= ~r200_dc_estimate_median_increment
23.default= 5
23.type= int
23.desc=Estimate Median Increment Range: 0 to 255
24.name= ~r200_dc_median_threshold
24.default= 235
24.type= int
24.desc=Median Threshold Range: 0 to 1023
25.name= ~r200_dc_score_minimum_threshold
25.default= 27
25.type= int
25.desc=Score Minimum Threshold Range: 0 to 1023
26.name= ~r200_dc_score_maximum_threshold
26.default= 420
26.type= int
26.desc=Score Maximum Threshold Range: 0 to 1023
27.name= ~r200_dc_texture_count_threshold
27.default= 8
27.type= int
27.desc=Texture Count Threshold Range: 0 to 31
28.name= ~r200_dc_texture_difference_threshold
28.default= 80
28.type= int
28.desc=Texture Difference Threshold Range: 0 to 1023
29.name= ~r200_dc_second_peak_threshold
29.default= 70
29.type= int
29.desc=Second Peak Threshold Range: 0 to 1023
30.name= ~r200_dc_neighbor_threshold
30.default= 90
30.type= int
30.desc=Neighbor Threshold Range: 0 to 1023
31.name= ~r200_dc_lr_threshold
31.default= 12
31.type= int
31.desc=LR Threshold Range: 0 to 2047
}
# End of autogenerated section. You may edit below.

# cat devel/share/realsense_camera/docs/f200_paramsConfig.wikidoc
# Autogenerated param section. Do not hand edit.
group.2 {
name=F200 Dynamically Reconfigurable Parameters
desc='''F200 camera''' See the [[dynamic_reconfigure]] package for details on dynamically reconfigurable parameters.
0.name= ~enable_depth
0.default= True
0.type= bool
0.desc=Enable Depth 
1.name= ~color_backlight_compensation
1.default= 1
1.type= int
1.desc=Backlight Compensation Range: 0 to 4
2.name= ~color_brightness
2.default= 55
2.type= int
2.desc=Brightness Range: 0 to 255
3.name= ~color_contrast
3.default= 32
3.type= int
3.desc=Contrast Range: 16 to 64
4.name= ~color_gain
4.default= 64
4.type= int
4.desc=Gain Range: 64 to 2540
5.name= ~color_gamma
5.default= 220
5.type= int
5.desc=Gamma Range: 100 to 280
6.name= ~color_hue
6.default= 0
6.type= int
6.desc=Hue Range: -22 to 22
7.name= ~color_saturation
7.default= 128
7.type= int
7.desc=Saturation Range: 0 to 255
8.name= ~color_sharpness
8.default= 0
8.type= int
8.desc=Sharpness Range: 0 to 7
9.name= ~color_white_balance
9.default= 3200
9.type= int
9.desc=White Balance Range: 2500 to 6500
10.name= ~color_exposure
10.default= 156
10.type= int
10.desc=Exposure Range: 39 to 10000
11.name= ~color_enable_auto_white_balance
11.default= 1
11.type= int
11.desc=Enable Auto White Balance Range: 0 to 1
12.name= ~color_enable_auto_exposure
12.default= 1
12.type= int
12.desc=Enable Auto Exposure Range: 0 to 1
13.name= ~f200_laser_power
13.default= 16
13.type= int
13.desc=Laser Power Range: 0 to 16
14.name= ~f200_accuracy
14.default= 2
14.type= int
14.desc=Accuracy Range: 1 to 3
15.name= ~f200_motion_range
15.default= 1
15.type= int
15.desc=Motion Range Range: 0 to 100
16.name= ~f200_filter_option
16.default= 5
16.type= int
16.desc=Filter Option Range: 0 to 7
17.name= ~f200_confidence_threshold
17.default= 6
17.type= int
17.desc=Confidence Threshold Range: 0 to 15
}
# End of autogenerated section. You may edit below.

# cat devel/share/realsense_camera/docs/sr300_paramsConfig.wikidoc 
# Autogenerated param section. Do not hand edit.
group.3 {
name=SR300 Dynamically Reconfigurable Parameters
desc='''SR300 camera''' See the [[dynamic_reconfigure]] package for details on dynamically reconfigurable parameters.
0.name= ~enable_depth
0.default= True
0.type= bool
0.desc=Enable Depth 
1.name= ~color_backlight_compensation
1.default= 0
1.type= int
1.desc=Backlight Compensation Range: 0 to 4
2.name= ~color_brightness
2.default= 0
2.type= int
2.desc=Brightness Range: -64 to 64
3.name= ~color_contrast
3.default= 50
3.type= int
3.desc=Contrast Range: 0 to 100
4.name= ~color_gain
4.default= 64
4.type= int
4.desc=Gain Range: 0 to 128
5.name= ~color_gamma
5.default= 300
5.type= int
5.desc=Gamma Range: 100 to 500
6.name= ~color_hue
6.default= 0
6.type= int
6.desc=Hue Range: -180 to 180
7.name= ~color_saturation
7.default= 64
7.type= int
7.desc=Saturation Range: 0 to 100
8.name= ~color_sharpness
8.default= 50
8.type= int
8.desc=Sharpness Range: 0 to 100
9.name= ~color_white_balance
9.default= 4600
9.type= int
9.desc=White Balance Range: 2800 to 6500
10.name= ~color_enable_auto_white_balance
10.default= 1
10.type= int
10.desc=Enable Auto White Balance Range: 0 to 1
11.name= ~color_exposure
11.default= 156
11.type= int
11.desc=Exposure Range: 39 to 10000
12.name= ~color_enable_auto_exposure
12.default= 1
12.type= int
12.desc=Enable Auto Exposure Range: 0 to 1
13.name= ~f200_laser_power
13.default= 16
13.type= int
13.desc=Laser Power Range: 0 to 16
14.name= ~f200_accuracy
14.default= 1
14.type= int
14.desc=Accuracy Range: 1 to 3
15.name= ~f200_motion_range
15.default= 9
15.type= int
15.desc=Motion Range Range: 0 to 100
16.name= ~f200_filter_option
16.default= 5
16.type= int
16.desc=Filter Option Range: 0 to 7
17.name= ~f200_confidence_threshold
17.default= 3
17.type= int
17.desc=Confidence Threshold Range: 0 to 15
18.name= ~sr300_auto_range_enable_motion_versus_range
18.default= 1
18.type= int
18.desc=Enable Motion Versus Range Range: 0 to 2
19.name= ~sr300_auto_range_enable_laser
19.default= 1
19.type= int
19.desc=Enable Laser Range: 0 to 1
20.name= ~sr300_auto_range_min_motion_versus_range
20.default= 180
20.type= int
20.desc=Min Motion Versus Range Range: -32767 to 32767
21.name= ~sr300_auto_range_max_motion_versus_range
21.default= 605
21.type= int
21.desc=Max Motion Versus Range Range: -32767 to 32767
22.name= ~sr300_auto_range_start_motion_versus_range
22.default= 303
22.type= int
22.desc=Start Motion Versus Range Range: -32767 to 32767
23.name= ~sr300_auto_range_min_laser
23.default= 2
23.type= int
23.desc=Min Laser Range: -32767 to 32767
24.name= ~sr300_auto_range_max_laser
24.default= 16
24.type= int
24.desc=Max Laser Range: -32767 to 32767
25.name= ~sr300_auto_range_start_laser
25.default= -1
25.type= int
25.desc=Start Laser Range: -32767 to 32767
26.name= ~sr300_auto_range_upper_threshold
26.default= 1250
26.type= int
26.desc=Upper Threshold Range: 0 to 65535
27.name= ~sr300_auto_range_lower_threshold
27.default= 650
27.type= int
27.desc=Lower Threshold Range: 0 to 65535
}
# End of autogenerated section. You may edit below.

# cat devel/share/realsense_camera/docs/zr300_paramsConfig.wikidoc 
# Autogenerated param section. Do not hand edit.
group.4 {
name=ZR300 Dynamically Reconfigurable Parameters
desc='''ZR300 camera''' See the [[dynamic_reconfigure]] package for details on dynamically reconfigurable parameters.
0.name= ~enable_depth
0.default= True
0.type= bool
0.desc=Enable Depth 
1.name= ~color_backlight_compensation
1.default= 0
1.type= int
1.desc=Backlight Compensation Range: 0 to 4
2.name= ~color_brightness
2.default= 0
2.type= int
2.desc=Brightness Range: 0 to 255
3.name= ~color_contrast
3.default= 50
3.type= int
3.desc=Contrast Range: 16 to 64
4.name= ~color_exposure
4.default= 166
4.type= int
4.desc=Exposure Range: 50 to 666
5.name= ~color_gain
5.default= 64
5.type= int
5.desc=Gain Range: 0 to 256
6.name= ~color_gamma
6.default= 300
6.type= int
6.desc=Gamma Range: 100 to 280
7.name= ~color_hue
7.default= 0
7.type= int
7.desc=Hue Range: -2200 to 2200
8.name= ~color_saturation
8.default= 64
8.type= int
8.desc=Saturation Range: 0 to 255
9.name= ~color_sharpness
9.default= 50
9.type= int
9.desc=Sharpness Range: 0 to 7
10.name= ~color_white_balance
10.default= 4600
10.type= int
10.desc=White Balance Range: 2000 to 8000
11.name= ~r200_lr_gain
11.default= 400
11.type= int
11.desc=LR Gain Range: 100 to 6399
12.name= ~r200_lr_exposure
12.default= 164
12.type= int
12.desc=LR Exposure Range: 1 to 164
13.name= ~color_enable_auto_exposure
13.default= 1
13.type= int
13.desc=Enable Auto Exposure Range: 0 to 1
14.name= ~color_enable_auto_white_balance
14.default= 1
14.type= int
14.desc=Enable Auto White Balance Range: 0 to 1
15.name= ~r200_lr_auto_exposure_enabled
15.default= 0
15.type= int
15.desc=Enable LR Auto Exposure Range: 0 to 1
16.name= ~r200_emitter_enabled
16.default= 1
16.type= int
16.desc=Emitter Enabled Range: 0 to 1
17.name= ~r200_depth_clamp_min
17.default= 0
17.type= int
17.desc=Depth Clamp Min Range: 0 to 65535
18.name= ~r200_depth_clamp_max
18.default= 65535
18.type= int
18.desc=Depth Clamp Max Range: 0 to 65535
19.name= ~fisheye_exposure
19.default= 40
19.type= int
19.desc=Fisheye Exposure Range: 40 to 331
20.name= ~fisheye_gain
20.default= 0
20.type= int
20.desc=Fisheye Gain Range: 0 to 2047
21.name= ~fisheye_enable_auto_exposure
21.default= 1
21.type= int
21.desc=Fisheye Enable Auto Exposure Range: 0 to 1
22.name= ~fisheye_auto_exposure_mode
22.default= 0
22.type= int
22.desc=Fisheye Auto Exposure Mode Range: 0 to 2
23.name= ~fisheye_auto_exposure_antiflicker_rate
23.default= 60
23.type= int
23.desc=Fisheye Auto Exposure Antiflicker Rate Range: 50 to 60
24.name= ~fisheye_auto_exposure_pixel_sample_rate
24.default= 1
24.type= int
24.desc=Fisheye Auto Exposure Pixel Sample Rate Range: 1 to 3
25.name= ~fisheye_auto_exposure_skip_frames
25.default= 2
25.type= int
25.desc=Fisheye Auto Exposure Skip Frames Range: 0 to 3
26.name= ~frames_queue_size
26.default= 20
26.type= int
26.desc=Frames Queue Size Range: 1 to 20
27.name= ~hardware_logger_enabled
27.default= 0
27.type= int
27.desc=Hardware Logger Enabled Range: 0 to 1
28.name= ~r200_dc_preset
28.default= 5
28.type= int
28.desc=R200 Depth Control Preset Possible values are: UNUSED (-1): Individual Depth Control was changed, Default (0): Default settings on chip. Similar to Medium. Best for Outdoors., Off (1): Disable almost all hardware-based outlier removal., Low (2): Lower number of outliers removed. Minimal false negatives., Medium (3): Medium number of outliers removed. Balanced approach., Optimized (4): Medium-High number of outliers removed. Derived optimization function., High (5): Higher number of outliers removed. Minimal false positives.
29.name= ~r200_dc_estimate_median_decrement
29.default= 5
29.type= int
29.desc=Estimate Median Decrement Range: 0 to 255
30.name= ~r200_dc_estimate_median_increment
30.default= 5
30.type= int
30.desc=Estimate Median Increment Range: 0 to 255
31.name= ~r200_dc_median_threshold
31.default= 235
31.type= int
31.desc=Median Threshold Range: 0 to 1023
32.name= ~r200_dc_score_minimum_threshold
32.default= 27
32.type= int
32.desc=Score Minimum Threshold Range: 0 to 1023
33.name= ~r200_dc_score_maximum_threshold
33.default= 420
33.type= int
33.desc=Score Maximum Threshold Range: 0 to 1023
34.name= ~r200_dc_texture_count_threshold
34.default= 8
34.type= int
34.desc=Texture Count Threshold Range: 0 to 31
35.name= ~r200_dc_texture_difference_threshold
35.default= 80
35.type= int
35.desc=Texture Difference Threshold Range: 0 to 1023
36.name= ~r200_dc_second_peak_threshold
36.default= 70
36.type= int
36.desc=Second Peak Threshold Range: 0 to 1023
37.name= ~r200_dc_neighbor_threshold
37.default= 90
37.type= int
37.desc=Neighbor Threshold Range: 0 to 1023
38.name= ~r200_dc_lr_threshold
38.default= 12
38.type= int
38.desc=LR Threshold Range: 0 to 2047
}
# End of autogenerated section. You may edit below.
    }
  }
  srv {
    0.name = get_settings
    0.type = std_srvs/Empty
    0.desc = Gets the current value of the supported camera options in "options:value" format separated by semicolon returned as <<MsgLink(std_msgs/String)>>.
    1.name = set_power
    1.type = std_srvs/Empty
    1.desc = Set to `true` power on the camera, `false` to power off the camera. It turns off the camera only if camera has no subscribers and returns 'true'; otherwise it returns `false`.
    2.name = force_power
    2.type = realsense_camera/ForcePower
    2.desc = Set to `true` power on the camera, `false` to forcefully power off the camera. It turns off the camera regardless of number of subscribers. Returns 'true' if the service call is successfully; otherwise it returns `false`.
    3.name = is_powered
    3.type = std_srvs/Empty
    3.desc = Gets current state of camera power returned as <<MsgLink(std_msgs/Bool)>>. It checks whether camera is on or off and returns true or false respectively.
    4.name = get_imu_info
    4.type = std_srvs/Empty
    4.desc = Available only for '''ZR300''' cameras. Gets the IMU intrinsic data. Returns  <<MsgLink(realsense_camera/IMUInfo)>> with the header.frame_id set to either "imu_accel" or "imu_gyro" to distinguish between "accel" and "gyro" info.
  }

  prov_tf {
    group.0 {
    name = Transform Restrictions
    desc = By default, transforms will be published as static as the camera transform data does not change. Due to a [[https://github.com/ros/ros_comm/issues/146|ROS bug]] which prevents publishing more than one static transform in separate processes, the same data can be published as a dynamic transform by setting enable_tf_dynamic=true. If two (or more) cameras will be run under the same Nodelet manager, then Dynamic Transforms should be used. Due to a [[https://github.com/intel-ros/realsense/issues/92|bug in the driver for the F200/SR300 cameras]], multiple F200/SR300 '''must''' be run under the same Nodelet manager implying the need for dynamic transforms to be used.
    0.from = camera_link
    0.to = camera_rgb_frame
    0.desc = '''Static''' Transform base frame to color frame.
    1.from = camera_rgb_frame
    1.to = camera_rgb_optical_frame
    1.desc = '''Static''' Transform color frame to color optical frame.
    2.from = camera_link
    2.to = camera_depth_frame
    2.desc = '''Static''' Transform base frame to depth frame.
    3.from = camera_depth_frame
    3.to = camera_depth_optical_frame
    3.desc = '''Static''' Transform depth frame to depth optical frame.
    4.from = camera_link
    4.to = camera_ir_frame
    4.desc = '''Static''' Transform base frame to infrared frame.
    5.from = camera_ir_frame
    5.to = camera_ir_optical_frame
    5.desc = '''Static''' Transform infrared frame to infrared optical frame.

    6.from = camera_link
    6.to = camera_ir2_frame
    6.desc = Available only for '''R200/ZR300''' cameras. '''Static''' Transform base frame to infrared2 frame.
    7.from = camera_ir2_frame
    7.to = camera_ir2_optical_frame
    7.desc = Available only for '''R200/ZR300''' cameras. '''Static''' Transform infrared frame to infrared2 optical frame.

    8.from = camera_link
    8.to = camera_fisheye_frame
    8.desc = Available only for '''ZR300''' camera. '''Static''' Transform base frame to fisheye frame.
    9.from = camera_fisheye_frame
    9.to = camera_fisheye_optical_frame
    9.desc = Available only for '''ZR300''' camera. '''Static''' Transform fisheye frame to fisheye optical frame.
   10.from = camera_link
   10.to = camera_imu_frame
   10.desc = Available only for '''ZR300''' camera. '''Static''' Transform base frame to imu frame. '''''NOTE: The transform has been hardcoded until fully calibrated cameras are available to the public.'''''
   11.from = camera_imu_frame
   11.to = camera_imu_optical_frame
   11.desc = Available only for '''ZR300''' camera. '''Static''' Transform imu frame to imu optical frame.
   }
  }
}
```



### Running the Nodelet

#### R200 Cameras



```
$ roslaunch realsense_camera r200_nodelet_default.launch
```



#### F200 Cameras



```
$ roslaunch realsense_camera f200_nodelet_default.launch
```



#### SR300 Cameras



```
$ roslaunch realsense_camera sr300_nodelet_default.launch
```



#### ZR300 Cameras



```
$ roslaunch realsense_camera zr300_nodelet_default.launch
```



Sample launch files are available in launch directory. Make sure the
correct "camera_type" is specified to launch the desired camera.

### Launching Multiple Cameras

Note: The following example is based on R200 cameras. Similar options
are applicable to F200, SR300 and ZR300 cameras too, just by updating
the "camera_type".

For running multiple cameras simultaneously: Option 1: Using single
nodelet manager for all the cameras

Use "r200_nodelet_multiple_cameras.launch". Option 2: Using separate
nodelet manager for each camera

Create ".launch" files similar to "r200_nodelet_rgbd.launch" for
each camera. You may choose to include (or not) the
"processing.launch.xml" based on your requirement. Launch the
".launch" files for each camera in separate terminals. For either
option you must:

Update the "camera" and either the "serial_no" or "usb_port_id"
argument with unique values for each camera. "camera" should be a user
friendly string that follows the ROS Names convention. (E.g.
"camera1") "serial_no" is the camera serial number and can be found
by running the nodelet and viewing the terminal output "usb_port_id"
is Bus Number-Port Number in "Bus#-Port#" format, and can be found by
using lsusb -t if both "serial_no" and "usb_port_id" are set, both
much match the same camera

### Limitations

-   Currently, the camera nodelet only supports the following formats:
-   Color stream: "RGB8"
-   Depth stream: "Z16"
-   Infrared stream(s): "Y8" for R200, F200 and ZR300. "Y16" for
    SR300.
-   Fisheye stream: "RAW8"

```{=html}
<!-- -->
```
-   Generating a Depth Registered Point Cloud is very memory intensive.
    E.g. The topic /camera/depth_registered/points, generated by launch
    file "r200_nodelet_rgbd.launch", works best at 30 fps using
    640x480 resolution on a system with 16GB of RAM.

```{=html}
<!-- -->
```
-   The camera does not provide hardware based depth
    registration/projector data. Hence the launch file
    "r200_nodelet_rgbd.launch" will not generate data for the
    following topics: 

```
/camera/depth_registered/hw_registered/image_rect_raw
/camera/depth_registered/hw_registered/image_rect
/camera/depth_registered/image
/camera/depth/disparity
/camera/depth_registered/disparity
```



```{=html}
<!-- -->
```
-   The performance benchmark for multiple cameras launched at the same
    time has not been defined yet.

```{=html}
<!-- -->
```
-   For ZR300 cameras, the transform between base frame and IMU frame
    has been hardcoded until librealsense supports fetching this data
    during runtime.

### Errata

See the
[GitHub Issues Bugs](https://github.com/intel-ros/realsense/labels/bug)
for a complete list.

-   F200/SR300 cameras:
    [Multiple cameras can only be started from a single launch file for F200 and SR300 camera types.](https://github.com/intel-ros/realsense/issues/92)

```{=html}
<!-- -->
```
-   F200/SR300 cameras:
    [Native pointcloud is not generated even after enabling pointcloud.](https://github.com/intel-ros/realsense/issues/89)
    This is unlikely to be fixed as current plan is to
    [remove native point cloud generation](https://github.com/intel-ros/realsense/issues/47)
    from the node.
