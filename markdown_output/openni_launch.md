

```wiki
<<TOC(4)>>

== Overview ==
This package contains launch files for using OpenNI-compliant devices such as the Microsoft Kinect in ROS. It creates a [[nodelet]] graph to transform raw data from the device driver into point clouds, disparity images, and other products suitable for processing and visualization.

Starting with ROS Hydro, all the functionality of `openni_launch` has been moved to [[rgbd_launch]], in order to allow other drivers such as libfreenect ([[freenect_launch]]) to use the same code. `openni_launch` itself contains 1 launch file:
 * `launch/openni.launch` - Launch RGB-D processing through [[rgbd_launch]] with the OpenNI driver.

== Quick start ==
Launch the OpenNI driver. This will launch the full constellation of nodelets:
{{{
roslaunch openni_launch openni.launch
```



To visualize in [rviz](rviz): 

```
rosrun rviz rviz
```

 Set the Fixed
Frame (top left of rviz window) to `/camera_depth_optical_frame`.

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
rosrun rqt_reconfigure rqt_reconfigure
```



And select `/camera/driver` from the drop-down menu. Enable the
`depth_registration` checkbox.

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



## Launch files



```clearsilver
node.0 {
  name = openni.launch
  desc << EOM
Launches in one process the device driver and many processing nodelets for turning the raw RGB and depth images into useful products, such as point clouds. Provides default tf tree linking the RGB and depth cameras.
EOM
}
```



#### Arguments

This section only covers arguments that are specific to
`openni_launch`. There are also some common arguments that can be
supplied to `openni.launch` that are documented with
[rgbd_launch](rgbd_launch).



```clearsilver
param {
  no_header=True
  group.0 {
    0.name = camera
    0.type = string
    0.default = camera
    0.desc << EOM
Descriptive name for your device. All published topics are ''pushed down'' into the `<camera>` namespace, and this also affects tf frame ids and some node names. If you are using multiple cameras, use this argument to disambiguate them.
EOM
  }
  group.1 {
    name = Device driver
    0.name = device_id
    0.type = string
    0.default = #1
    0.desc << EOM
Specifies which device to open. The following formats are recognized:
    ||#1 ||Use first device found ||
    ||2@3 ||Use device on USB bus 2, address 3 ||
    ||B00367707227042B||Use device with given serial number||
EOM
    1.name = rgb_camera_info_url
    1.type = string
    1.default = `file://${ROS_HOME}/camera_info/${NAME}.yaml`
    1.desc << EOM
[[camera_info_manager#URL_Names|Calibration URL]] for the RGB camera. By default, looks in your ROS home directory for calibration identified by the device serial number, e.g. `$HOME/.ros/camera_info/rgb_B00367707227042B`. If no calibration is found, uses a default camera model with a typical focal length and distortion unmodeled.
EOM
    2.name = depth_camera_info_url
    2.type = string
    2.default = `file://${ROS_HOME}/camera_info/${NAME}.yaml`
    2.desc << EOM
[[camera_info_manager#URL_Names|Calibration URL]] for the IR/depth camera. By default, looks in your ROS home directory for calibration identified by the device serial number, e.g. `$HOME/.ros/camera_info/depth_B00367707227042B`. If no calibration is found, uses a default camera model with the focal length reported by OpenNI and distortion unmodeled.
EOM
  }
```





```clearsilver
param {
  no_header=True
  3.name = depth_registration
  3.type = bool
  3.default = false
  3.desc = If true, use OpenNI's factory-calibrated depth->RGB registration.
  4.name = load_driver
  4.type = bool
  4.default = true
  4.desc = If true, load the OpenNI device driver. Set to false if raw data is provided by another source, e.g. bag file playback.
}
```





```
rosrun rviz rviz
```

0



```
rosrun rviz rviz
```

1



```
rosrun rviz rviz
```

2



```
rosrun rviz rviz
```

3



```
rosrun rviz rviz
```

4 

```
rosrun rviz rviz
```

5

This section only covers arguments that are specific to
`openni_launch`. There are also some common arguments that can be
supplied to `openni.launch` that are documented with
[rgbd_launch](rgbd_launch).

#### Published Topics

Please consult the documentation at [rgbd_launch](rgbd_launch).

}}}
