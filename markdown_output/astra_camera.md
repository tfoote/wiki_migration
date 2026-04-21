astra_camera

A ROS driver for Orbbec 3D cameras.

## Install

This package supports ROS Kinetic and Melodic.

1\. Install [ROS](http://wiki.ros.org/ROS/Installation). 1. Install
dependences ```
sudo apt install ros-*-rgbd-launch ros-*-libuvc ros-*-libuvc-camera ros-*-libuvc-ros
``` 1. Create a
[ROS Workspace](http://wiki.ros.org/ROS/Tutorials/InstallingandConfiguringROSEnvironment)(if
you don't have one) ```
mkdir -p
/catkin_ws/src
/catkin_ws/
catkin_make
``` 1. Pull the repository
into your ROS workspace ```
/catkin_ws/src
git clone https://github.com/orbbec/ros_astra_camera
``` 1. Create astra udev
rule ```
roscd astra_camera
./scripts/create_udev_rules
``` 1. Go to catkin workspace and compile
astra_camera ```
/catkin_ws
catkin_make --pkg astra_camera
```

### Filter Enable (To be deprecated: recommend to try master branch at first)

Astra driver provides normal and filtering methods. With filter driver,
we can get more precise depth data but it would cost more computing
resources. If the program will be executed on embedded systems, we
suggest to use normal method. You can use -DFILTER=ON / OFF to change
the method as below.

catkin_make \--pkg astra_camera -DFILTER=OFF

## Run astra_camera

If you didn't add source \$YOUR_WORKSPACE/devel/setup.bash to your
.bashrc, remember to source it when open a new terminal :)

### Examples

#### Use Astra

roslaunch astra_camera astra.launch

#### Use Astra Stereo S (w/ UVC)

roslaunch astra_camera stereo_s.launch

You can use rviz or image_view to verify the outputs.

## Important Topics

-   \*/image_raw: depth/rgb/ir raw images
-   \*/image_rect_raw: images rectified by intrinsic/extrinsic
    parameters
-   \*/camera_info: camera intrinsic/extrinsic parameters
-   /camera/depth/points: point cloud without color information
-   /camera/depth_registered/points: xyzrgb point cloud

## Useful Services

This package provides multiple
[ros services](http://wiki.ros.org/Services) for users to get useful
information and set up devices. To know more about using these services,
please check [this tutorial](http://wiki.ros.org/rosservice).

-   /camera/get_device_type: return a string containing astra device
    type
-   /camera/get_ir_exposure: get exposure value of ir camera
-   /camera/get_ir_gain: get gain value of ir camera
-   /camera/get_serial: get serial number
-   /camera/get_uvc_exposure: get exposure value of rgb camera
-   /camera/get_uvc_gain: get gain value of rgb camera
-   /camera/get_uvc_white_balance: get white balance value of rgb camera
-   /camera/reset_ir_exposure: reset ir exposure to default value
-   /camera/reset_ir_gain: reset ir gain to default value
-   /camera/set_ir_exposure: set ir exposure to specific value
-   /camera/set_ir_gain: set ir gain to specific value
-   /camera/set_laser: turn on (true) or turn off (false) laser
-   /camera/set_uvc_exposure: set uvc exposure. (set 0 indicating auto
    mode)
-   /camera/set_uvc_gain: set uvc gain
-   /camera/set_uvc_white_balance: set uvc white balance (set 0
    indicating auto mode)
-   /camera/set_ir_flood: turn on (true) or turn off (false) ir flood
-   /camera/switch_ir_camera: while using stereo_s/stereo_s_u3, you can
    switch (left/right) ir camera

### Examples

After launching an astra camera, you can get ir exposure by the
following command

1\. ir exposure ```
rosservice call /camera/get_ir_exposure
``` Next, you can change this value
in this way ```
rosservice call /camera/set_ir_exposure
``` 1. turn on/off laser
```
rosservice call /camera/set_laser
rosservice call /camera/set_laser
``` 1. switch ir ```
rosservice call /camera/switch_ir_camera
rosservice call /camera/switch_ir_camera
```

For the other services, the usage is same as the above example.

## Multiple Cameras

To launch multiple cameras, you could modify multi_astra.launch to match
your setting. The important settings are device_x_id(serial number of
your devices), 3d_sensor(name of launch file), and has_uvc_serial(does
your camera's uvc have serial number).

If you received USB Buffer Error, you could try to increase your USBFS
buffer size by the following command.

```
echo 64 > /sys/module/usbcore/parameters/usbfs_memory_mb
```
