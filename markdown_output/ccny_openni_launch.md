## Details

The [ccny_openni_launch](ccny_openni_launch) package is a collection of
utility launch files for using RGB-D cameras based on the OpenNI driver.
The launch files use the `rgbd_image_proc` application from
[ccny_rgbd](ccny_rgbd) to process the raw sensor stream into rectified,
registered RGB and depth images, and (optionally) a point cloud.

The package provides three top-level launch files: for launching a live
device, for data recording, and for data playback.

The bags recorded will contain the raw RGB and Depth images at VGA
resolution, together with their CameraInfo topics.

For more information about the output topics and parameters, see
`rgbd_image_proc` in [ccny_rgbd](ccny_rgbd).

### Live operation

The
[ openni.launch](https://github.com/ccny-ros-pkg/ccny_rgbd_tools/blob/master/ccny_openni_launch/launch/openni.launch )
file will launch the driver and the processing nodelets.

```shell
roslaunch ccny_openni_launch openni.launch
```

![](attachment:openni_launch.png)

### Recording data

The
[ openni_record.launch](https://github.com/ccny-ros-pkg/ccny_rgbd_tools/blob/master/ccny_openni_launch/launch/openni_record.launch )
file will launch the device driver and record the raw data to a bag. No
processing is performed. The bag will include the raw RGB and depth
images, together with their CameraInfo topics.

```shell
roslaunch ccny_openni_launch openni_record.launch bag_name:=<path_to_ros_bag>
```

![](attachment:openni_record_launch.png)

### Playing bagged data

The
[ openni_play.launch](https://github.com/ccny-ros-pkg/ccny_rgbd_tools/blob/master/ccny_openni_launch/launch/openni_play.launch )
file will play a recorded bag and launch the processing nodelets. The
output of this launch file is the same as the output of
[ openni.launch](https://github.com/ccny-ros-pkg/ccny_rgbd_tools/blob/master/ccny_openni_launch/launch/openni.launch ).

```shell
roslaunch ccny_openni_launch openni_play.launch bag_name:=<path_to_ros_bag>
```

![](attachment:openni_play_launch.png)

## Configuration files

You can pass configuration files to `ccny_openni_launch` by setting
the `calib_path` parameter in
[device.launch](https://github.com/ccny-ros-pkg/ccny_rgbd_tools/blob/master/ccny_openni_launch/launch/include/device.launch)
and
<https://github.com/ccny-ros-pkg/ccny_rgbd_tools/blob/master/ccny_openni_launch/launch/include/proc.launch>
\|\| proc.launch\]\]

There are four configuration files of interes

-   **rgb.yml**: RGB camera intrinsics and distortion
-   **depth.yml**: Depth (or more accurately, IR) camera intrinsics and
    distortion
-   **extr.yml**: Extrinsic matrix between the RGB and Depth cameras
    (rotation and translation)
-   **warp.yml**: Per-pixel depth unwarping of the depth image,
    according to some polynomial model.

**rgb.yaml** and **depth.yml** are passed to the OpenNI driver ,which
distributes them as CameraInfo topics. They can be generated using the
[camera_calibration](camera_calibration) package.

**extr.yml**and **warp.yml** are passed to `rgbd_image_proc`. They can
be generated using [ccny_rgbd_calibrate](ccny_rgbd_calibrate) (coming
soon).

Using **warp.yml** is optional and be disabled using a flag in
`rgbd_image_proc`.

## Bug Reports & Feature Requests

We appreciate the time and effort spent submitting bug reports and
feature requests.

Please submit your tickets through
[github](https://github.com/ccny-ros-pkg/ccny_rgbd_tools/issues/)
(requires github account) or by emailing the maintainers.
