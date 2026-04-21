If you are a new user of the ROS OpenNI drivers (on Electric or later),
see [openni_launch](openni_launch) and [openni_camera](openni_camera).
This page is provided to help users of the old driver
[migrate their code](openni_camera_deprecated#Migration_guide), and for
historical interest.

`openni_camera_deprecated` is unmaintained and likely to be removed in
Groovy.

## History

ROS has long had two distinct OpenNI camera drivers:

-   The older, monolithic node.
-   The new, minimal driver nodelet, with 2D & 3D processing split off
    into separate nodelets. Launch files tie it all together.

The question of which to use has caused plenty of confusion. There are
slight differences in the ROS APIs for the two drivers. Finally, the
APIs have tended to move around to various packages across ROS releases.

### Diamondback

Microsoft released the Kinect in November 2010. Almost immediately the
open-source libfreenect community deciphered the USB protocol and
provided basic access to the depth and RGB image streams. We in the ROS
community participated in the early development of libfreenect and wrote
an experimental ROS driver for the Kinect.

In December 2010, !PrimeSense (the company behind the Kinect's
depth-sensing technology) released the OpenNI natural interaction
framework. It provided fuller access to the Kinect's hardware as well
as software depth registration and skeleton tracking. We quickly ported
our ROS driver to OpenNI.

The [openni_kinect](openni_kinect) stack, including the
[openni_camera](openni_camera) driver package, was first released in ROS
Diamondback in March 2011 following months of feverish development.

#### Old API

[openni_camera](openni_camera) provides:

-   `bin/openni_node`
-   Nodelet `openni_camera/OpenNINodelet`
-   Example launch file `launch/openni_node.launch`

#### New API

The new driver (discussed below) was backported to the Diamondback-only
package [openni_camera_unstable](openni_camera_unstable). It provides:

-   `bin/openni_node`
-   Nodelet `openni_camera/driver`
-   The nodelets from Electric's [depth_image_proc](depth_image_proc)
-   Launch file `launch/openni.launch` from Electric's
    [openni_launch](openni_launch)

### Electric

The original [openni_camera](openni_camera) driver was developed rapidly
and organically, as multiple developers hacked new features onto the
same monolithic node. Over time we discovered drawbacks of the original
ROS API, regretted its lack of flexibility, and found the codebase more
and more difficult to extend.

In Electric, we introduced a new "unstable" version of the driver,
intended to eventually replace the old monolithic one. It greatly
slimmed down the driver node(let), splitting most of the
device-independent data processing into separate nodelets in
[depth_image_proc](depth_image_proc). At the same time it added features
such as calibration, support for Asus Xtion devices, access to the IR
image stream, and registration of the depth stream with any (even
external) RGB camera.

#### Old API

Accessed as in Diamondback.

#### New API

[openni_camera](openni_camera) also provides the new, minimal driver:

-   `bin/openni_node_unstable`
-   Nodelet `openni_camera/driver`

[depth_image_proc](depth_image_proc) provides various nodelets for 2D/3D
processing.

[openni_launch](openni_launch) provides `launch/openni.launch`, which
composes the driver and processing nodelets into a unified system.

### Fuerte

In Fuerte the new API has officially reached a stable state. There
should not be any breaking ROS API changes from Electric. However the
[openni_kinect](openni_kinect) stack has been reorganized, resulting in
a couple of name changes.

#### Old API

No longer lives in [openni_camera](openni_camera). It has been split off
into [openni_camera_deprecated](openni_camera_deprecated), which still
provides:

-   `bin/openni_node`
-   Nodelet `openni_camera/OpenNINodelet`
-   Example launch file `launch/openni_node.launch`

#### New API

[openni_camera](openni_camera) (now a unary stack) provides only the
new, minimal driver:

-   `bin/openni_node` (note the renaming)
-   Nodelet `openni_camera/driver`

[depth_image_proc](depth_image_proc) has been moved to
[image_pipeline](image_pipeline).

[openni_launch](openni_launch) (also a unary stack) still provides
`launch/openni.launch`. It has gained some flexibility since Electric.

## Migration guide

### Updating from deprecated to stable API

In the stable API, the driver node(let) is minimal, publishing only the
device outputs. Instead, the deprecated node(let) API corresponds
closely to the launch file API of [openni_launch](openni_launch). If you
need processed outputs such as point clouds, replace use of
`openni_camera\[_deprecated\]/openni_node` and
`openni_camera/OpenNINodelet` with `openni_launch`.

Note the following ROS API changes between `openni_camera_deprecated`
and `openni_launch`:

-   Namespace `camera/depth/` now contains only unregistered (in the
    original depth/IR camera frame) outputs. Outputs registered to the
    RGB camera frame (including the XYZRGB point cloud) are published in
    namespace `camera/depth_registered/`.
-   Topic `camera/rgb/points` is replaced by
    `camera/depth_registered/points`.
-   There is no longer a mechanism for publishing an indexed subset of
    points. As far as we are aware, the only use case in practice was
    selecting some (possibly down-sampled) region(s)-of-interest in the
    depth image. One or more
    [image_proc/crop_decimate](image_proc#image_proc.2BAC8-electric.image_proc.2BAC8-crop_decimate)
    nodelets is a superior solution for that.

### Diamondback/Electric to Fuerte (deprecated API)

For users of the deprecated API, the only change is the package name.
Instead of: ```
# Diamondback, Electric
rosrun openni_camera openni_node
roslaunch openni_camera openni_node.launch
```

do ```
# Fuerte
rosrun openni_camera_deprecated openni_node
roslaunch openni_camera_deprecated openni_node.launch
```

The node(let) ROS API remains unchanged. The nodelet can still be loaded
by the same name, `openni_camera/OpenNINodelet`.

This package is scheduled for removal in Groovy. Please update your
packages to use the stable [openni_camera](openni_camera) and
[openni_launch](openni_launch) APIs.

## ROS API

```clearsilver
node.0 {
  name = openni_node
  desc = Deprecated OpenNI camera driver.
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
      4.name = camera/rgb/points
      4.type = sensor_msgs/PointCloud2
      4.desc = Registered XYZRGB point cloud. If using [[pcl_ros|PCL]], subscribe as `PointCloud<PointXYZRGB>`. Published only if `~depth_registration` is on.
    }
    group.1 {
      name = Depth camera
      desc = If `~depth_registration` is off, all images are in the original IR camera frame. If on, all images are registered to the RGB camera frame.
      0.name = camera/depth/camera_info
      0.type = sensor_msgs/CameraInfo
      0.desc = Camera calibration and metadata.
      1.name = camera/depth/image_raw
      1.type = sensor_msgs/Image
      1.desc = Raw image from device. Contains `uint16` depths in mm.
      2.name = camera/depth/image
      2.type = sensor_msgs/Image
      2.desc = Unrectified depth image. Contains `float` depths in m.
      3.name = camera/depth/disparity
      3.type = stereo_msgs/DisparityImage
      3.desc = Disparity image (inversely related to depth), for interop with stereo processing nodes.
      4.name = camera/depth/points
      4.type = sensor_msgs/PointCloud2
      4.desc = Unregistered XYZ point cloud. If using [[pcl_ros|PCL]], subscribe as `PointCloud<PointXYZ>`. Published only if `~depth_registration` is off.
    }
  }
  sub {
    0.name = camera/depth/indices
    0.type = pcl/PointIndices
    0.desc = If `~use_indices` is set, the subset of points to include when publishing a point cloud.
  }
  param {
    group.0 {
      0.name = ~device_id
      0.type = string
      0.desc << EOM
Specifies which device to open. The following formats are recognized:
    ||#1              ||Use first device found             ||
    ||2@3             ||Use device on USB bus 2, address 3 ||
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
      3.name = ~use_indices
      3.type = bool
      3.default = false
      3.desc = If true, listen on `camera/depth/indices` and publish point clouds containing only the requested points.
    }
    group.1 {
# Autogenerated param section. Do not hand edit.
name=Dynamically Reconfigurable Parameters
desc=See the [[dynamic_reconfigure]] package for details on dynamically reconfigurable parameters.
0.name= ~image_mode
0.default= 2
0.type= int
0.desc=Image output mode for the color/grayscale image Possible values are: SXGA_15Hz (1): 1280x1024@15Hz, VGA_30Hz (2): 640x480@30Hz, VGA_25Hz (3): 640x480@25Hz, QVGA_25Hz (4): 320x240@25Hz, QVGA_30Hz (5): 320x240@30Hz, QVGA_60Hz (6): 320x240@60Hz, QQVGA_25Hz (7): 160x120@25Hz, QQVGA_30Hz (8): 160x120@30Hz, QQVGA_60Hz (9): 160x120@60Hz
1.name= ~debayering
1.default= 0
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
}
node.1 {
  name = openni_camera/OpenNINodelet nodelet
  desc = Nodelet version of the deprecated OpenNI driver. Has the same ROS API as `openni_node` above.
}
```

## Launch files

### openni_node.launch

A simple example launch file. It opens the first enumerated device with
OpenNI depth registration enabled. The ROS API is as described above.

### kinect_frames.launch

Publishes default transforms relating the IR and RGB cameras to
[tf](tf). Included by `openni_node.launch`.
