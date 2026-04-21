## Overview

This package contains the development version of
[openni_camera](openni_camera), so that Diamondback users can easily
access new features. Note that [openni_camera](openni_camera) is locked
for Diamondback and will be updated only with bug fixes.
[openni_camera_unstable](openni_camera_unstable) makes no guarantees of
API stability across releases, use at your own risk!

Major new features include:

-   Support for ASUS Xtion Pro devices, which have the depth sensor but
    no RGB camera.
-   Access to IR image stream.
-   Support for calibrating the IR and RGB cameras for higher accuracy.
    The default camera models (if uncalibrated) do not model lens
    distortion, and make possibly inaccurate assumptions about focal
    length and image center.
-   Support for registering the depth images with any RGB camera,
    including one external to the device.
-   The driver has been subdivided into several nodelets for greater
    flexibility.

API breakages from [openni_camera](openni_camera):

-   The "camera/depth" namespace became too overloaded. It has been
    broken in two:
-   "camera/depth" - Contains unregistered depth outputs, including
    XYZ point cloud.
-   "camera/depth_registered" - Contains registered (aligned with RGB
    image) outputs, including XYZRGB point cloud.
-   openni_node now publishes only the raw images from the device, not
    the processed outputs (point clouds, etc.). Use the provided launch
    files instead.

In E-turtle [openni_camera_unstable](openni_camera_unstable) has become
[openni_camera](openni_camera).

See [openni_kinect/Roadmap](openni_kinect/Roadmap) for planned future
features.

## Tutorials

### Quick start

Don't forget to build the driver if you've installed from source:


```
rosmake openni_camera_unstable
```



Launch the OpenNI driver: 

```
roslaunch openni_camera_unstable openni.launch
```



To visualize in [rviz](rviz): 

```
rosrun rviz rviz
```



Set the Fixed Frame (top left of rviz window) to
`/camera_depth_optical_frame`.

Add a !PointCloud2 display, and set the topic to
`/camera/depth/points`. Turning the background to light gray can help
with viewing. This is the *unregistered* point cloud in the frame of the
depth (IR) camera. It is not matched with the RGB camera images.

Alternatively you can view the disparity image: 

```
rosrun image_view disparity_view image:=/camera/depth/disparity
```



Now let's look at a *registered* point cloud, aligned with the RGB
data. Open the dynamic reconfigure GUI: 

```
rosrun dynamic_reconfigure reconfigure_gui
```



And select `/camera/driver` from the drop-down menu. Enable
`depth_registration`: ![](attachment:openni_reconfigure.png)

Now go back to rviz, and change your !PointCloud2 topic to
`/camera/depth_registered/points`. Set Color Transformer to `RGB8`.
You should see a color, 3D point cloud of your scene.

Again, you can view the registered disparity image:


```
rosrun image_view disparity_view image:=/camera/depth_registered/disparity
```



To view the color image from the RGB camera outside of rviz:


```
rosrun image_view image_view image:=/camera/rgb/image_color
```



or to view the grayscale image: 

```
rosrun image_view image_view image:=/camera/rgb/image_mono
```



### Camera calibration

For instructions on calibrating camera intrinsics, see
[openni_camera/calibration](openni_camera/calibration).

## Known issues

## Launch files

This package provides launch files to load the driver nodelet and
various data processing nodelets as a coordinated system.



```clearsilver
node.0 {
  name = openni.launch
  desc  << EOM
Launches in one process the device driver and many processing nodelets for turning the raw RGB and depth images into useful products, such as point clouds. Provides default tf tree linking the RGB and depth cameras.

==== Arguments ====
`camera` (`string`, default: camera)

    Descriptive name for your device. All published topics are ''pushed down'' into the `<camera>` namespace, and this also affects tf frame ids and some node names. If you are using multiple cameras, use this argument to disambiguate them.

`device_id` (`string`, default: #1)

    Specifies which device to open. The following formats are recognized:
    ||#1              ||Use first device found             ||
    ||2@3             ||Use device on USB bus 2, address 3 ||
    ||B00367707227042B||Use device with given serial number||

`rgb_frame_id` (`string`, default: `/<camera>_rgb_optical_frame`)

    The tf frame id of the RGB camera.

`depth_frame_id` (`string`, default: `/<camera>_depth_optical_frame`)

    The tf frame id of the IR camera.

`calibration_dir` (`string`, default: `/tmp`)

    Directory containing calibration parameter files.

`rgb_calibration` (`string`, default: `<calibration_dir>/calibration_%s.yaml`)

    File name of the RGB camera calibration. `%s` is expanded by the driver to the unique camera name `rgb_[serial#]`. For example, by default `rgb_calibration` could expand to `/tmp/calibration_rgb_B00367707227042B.yaml`.

`depth_calibration` (`string`, default: `<calibration_dir>/calibration_%s.yaml`)

    File name of the depth camera calibration. `%s` is expanded by the driver to the unique camera name `depth_[serial#]`. For example, by default `depth_calibration` could expand to `/tmp/calibration_depth_B00367707227042B.yaml`.

`rgb` (`string`, default: rgb)

    Remap the `rgb` namespace.

`ir` (`string`, default: ir)

    Remap the `ir` namespace.

`depth` (`string`, default: depth)

    Remap the `depth` namespace.

`depth_registered` (`string`, default: depth_registered)

    Remap the `depth_registered` namespace.

EOM
  pub {
    group.0 {
      name = RGB camera
      0.name = camera/rgb/camera_info
      0.type = sensor_msgs/CameraInfo
      0.desc = Camera calibration and metadata.
      1.name = camera/rgb/image_raw
      1.type = sensor_msgs/Image
      1.desc = Raw image from device. Format is Bayer GRBG for Kinect, YUV422 for PSDK.
      2.name = camera/rgb/image_mono
      2.type = sensor_msgs/Image
      2.desc = Monochrome unrectified image.
      3.name = camera/rgb/image_color
      3.type = sensor_msgs/Image
      3.desc = Color unrectified image.
      4.name = camera/rgb/image_rect
      4.type = sensor_msgs/Image
      4.desc = Monochrome rectified image.
      5.name = camera/rgb/image_rect_color
      5.type = sensor_msgs/Image
      5.desc = Color rectified image.
    }
    group.1 {
      name = Depth camera
      0.name = camera/depth/camera_info
      0.type = sensor_msgs/CameraInfo
      0.desc = Camera calibration and metadata.
      1.name = camera/depth/image_raw
      1.type = sensor_msgs/Image
      1.desc = Raw image from device. Contains `uint16` depths in mm.
      2.name = camera/depth/image
      2.type = sensor_msgs/Image
      2.desc = Unrectified depth image. Contains `float` depths in m.
      3.name = camera/depth/image_rect
      3.type = sensor_msgs/Image
      3.desc = Rectified depth image. Contains `float` depths in m.
      4.name = camera/depth/disparity
      4.type = stereo_msgs/DisparityImage
      4.desc = Disparity image (inversely related to depth), for interop with stereo processing nodes.
      5.name = camera/depth/points
      5.type = sensor_msgs/PointCloud2
      5.desc = XYZ point cloud. If using [[pcl_ros|PCL]], subscribe as `PointCloud<PointXYZ>`.
    }
    group.2 {
      name = Registered depth camera (aligned with RGB camera)
      desc << EOM
These topics can be produced in two ways.

If OpenNI registration is enabled:
 * The unregistered `camera/depth/*` topics are not published.
 * The raw depth image from OpenNI is published in `camera/depth_registered` instead.
If OpenNI registration is disabled ''and'' you have calibrated the cameras to each other:
 * `camera/depth_registered/image_raw` is computed from `camera/depth/image_raw` using the camera instrinsics and transform between them.
 * Both registered and unregistered depth outputs are published.
EOM
      0.name = camera/depth_registered/camera_info
      0.type = sensor_msgs/CameraInfo
      0.desc = Camera calibration and metadata. Same as `camera/rgb/camera_info` but time-synced to depth images.
      1.name = camera/depth_registered/image_raw
      1.type = sensor_msgs/Image
      1.desc = Raw image from device. Contains `uint16` depths in mm.
      2.name = camera/depth_registered/image
      2.type = sensor_msgs/Image
      2.desc = Unrectified depth image. Contains `float` depths in m.
      3.name = camera/depth_registered/image_rect
      3.type = sensor_msgs/Image
      3.desc = Rectified depth image. Contains `float` depths in m.
      4.name = camera/depth_registered/disparity
      4.type = stereo_msgs/DisparityImage
      4.desc = Disparity image (inversely related to depth), for interop with stereo processing nodes.
      5.name = camera/depth_registered/points
      5.type = sensor_msgs/PointCloud2
      5.desc = XYZRGB point cloud. If using [[pcl_ros|PCL]], subscribe as `PointCloud<PointXYZRGB>`.
    }
    group.3 {
      name = IR camera
      0.name = camera/ir/camera_info
      0.type = sensor_msgs/CameraInfo
      0.desc = Camera calibration and metadata.
      1.name = camera/ir/image_raw
      1.type = sensor_msgs/Image
      1.desc = Raw `uint16` IR image.
      2.name = camera/ir/image_rect
      2.type = sensor_msgs/Image
      2.desc = Rectified IR image.
    }
  }
# Autogenerated param section. Do not hand edit.
param {
group.0 {
name=Dynamically Reconfigurable Parameters
desc=See the [[dynamic_reconfigure]] package for details on dynamically reconfigurable parameters.
0.name= ~image_mode
0.default= 2
0.type= int
0.desc=Image output mode for the color/grayscale image Possible values are: SXGA_15Hz (1): 1280x1024@15Hz, VGA_30Hz (2): 640x480@30Hz, VGA_25Hz (3): 640x480@25Hz, QVGA_25Hz (4): 320x240@25Hz, QVGA_30Hz (5): 320x240@30Hz, QVGA_60Hz (6): 320x240@60Hz, QQVGA_25Hz (7): 160x120@25Hz, QQVGA_30Hz (8): 160x120@30Hz, QQVGA_60Hz (9): 160x120@60Hz
1.name= ~debayering
1.default= 1
1.type= int
1.desc=Bayer to RGB algorithm Possible values are: Bilinear (0): Fast debayering algorithm using bilinear interpolation, EdgeAware (1): debayering algorithm using an edge-aware algorithm, EdgeAwareWeighted (2): debayering algorithm using a weighted edge-aware algorithm
2.name= ~depth_mode
2.default= 2
2.type= int
2.desc=depth output mode Possible values are: SXGA_15Hz (1): 1280x1024@15Hz, VGA_30Hz (2): 640x480@30Hz, VGA_25Hz (3): 640x480@25Hz, QVGA_25Hz (4): 320x240@25Hz, QVGA_30Hz (5): 320x240@30Hz, QVGA_60Hz (6): 320x240@60Hz, QQVGA_25Hz (7): 160x120@25Hz, QQVGA_30Hz (8): 160x120@30Hz, QQVGA_60Hz (9): 160x120@60Hz
3.name= ~depth_registration
3.default= False
3.type= bool
3.desc=Depth data registration 
4.name= ~depth_time_offset
4.default= 0.0
4.type= double
4.desc=depth image time offset in seconds Range: -1.0 to 1.0
5.name= ~image_time_offset
5.default= 0.0
5.type= double
5.desc=image time offset in seconds Range: -1.0 to 1.0
}
}
# End of autogenerated section. You may edit below.
  srv {
    0.name = camera/rgb/set_camera_info
    0.type = sensor_msgs/SetCameraInfo
    0.desc = Set the RGB camera calibration.
    1.name = camera/ir/set_camera_info
    1.type = sensor_msgs/SetCameraInfo
    1.desc = Set the IR camera calibration.
  }
  prov_tf {
    0.from = /<camera>_rgb_optical_frame
    0.to =  /<camera>_depth_optical_frame
    0.desc = Default estimate for the transform between the RGB and IR cameras. If OpenNI registration is disabled, this is used with the calibrated camera intrinsics to perform registration.
  }
}
```



## Nodelets

Reference documentation coming.

## Nodes

Reference documentation coming.
