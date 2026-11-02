

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



To visualize in [rviz](https://index.ros.org/p/rviz):


```
rosrun rviz rviz
```

 Set the Fixed Frame (top left of rviz window)
to `/camera_depth_optical_frame`.

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
[rgbd_launch](https://index.ros.org/p/rgbd_launch).



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





```clearsilver
param {
  no_header=True
  group.2 {
    name = tf frames
    0.name = rgb_frame_id
    0.type = string
    0.default = `/<camera>_rgb_optical_frame`
    0.desc = The tf frame id of the RGB camera.
    1.name = depth_frame_id
    1.type = string
    1.default = `/<camera>_depth_optical_frame`
    1.desc = The tf frame id of the IR camera.
  }
```





```clearsilver
param {
  no_header=True
  2.name = publish_tf
  2.type = bool
  2.default = true
  2.desc = If true, publish the default (uncalibrated) tf tree. Set to false if extrinsics are provided by another source, e.g. calibration or bag file playback.
}
```





```clearsilver
param {
  no_header=True
  3.name = tf_prefix
  3.type = string
  3.default = ""
  3.desc = If set, this tf_prefix is prefixed to all frame ids used/generated by `openni.launch`
}
```





```clearsilver
param {
  no_header=True
  group.3 {
    name = Remapping
    0.name = rgb
    0.type = string
    0.default = rgb
    0.desc = Remap the `rgb` namespace.
    1.name = ir
    1.type = string
    1.default = ir
    1.desc = Remap the `ir` namespace.
    2.name = depth
    2.type = string
    2.default = depth
    2.desc = Remap the `depth` namespace.
    3.name = depth_registered
    3.type = string
    3.default = depth_registered
    3.desc = Remap the `depth_registered` namespace.
    4.name = projector
    4.type = string
    4.default = projector
    4.desc = Remap the `projector` namespace.
  }
  group.4 {
    name = Launch configuration
    0.name = debug
    0.type = bool
    0.default = false
    0.desc = If true, launches nodelet manager in GDB for debugging.
}
```





```clearsilver
param {
  no_header=True
  1.name = respawn
  1.type = bool
  1.default = false
  1.desc = If true, enables bond topics between nodelet loaders and the managers and respawns any nodes (manager or loader) that die. This makes the system robust to any node dying, but the proliferation of bond topics can overwhelm introspection tools like rxgraph.
}
```

 

```clearsilver
param {
  no_header=True
  1.name = num_worker_threads
  1.type = int
  1.default = 4
  1.desc = Sets the number of worker threads in the nodelet manager
}
```



This section only covers arguments that are specific to
`openni_launch`. There are also some common arguments that can be
supplied to `openni.launch` that are documented with
[rgbd_launch](https://index.ros.org/p/rgbd_launch).

#### Published Topics

Please consult the documentation at
[rgbd_launch](https://index.ros.org/p/rgbd_launch).

}}}

## Tutorials

- [Recording and playing back Kinect data](#recording-and-playing-back-kinect-data):
  This tutorial shows how to efficiently record Kinect data into the ROS
  bag file format, and play it back into the same ROS processing graph.
- [Calibrating the Kinect depth camera to the built-in RGB camera](#calibrating-the-kinect-depth-camera-to-the-built-in-rgb-camera):
  This tutorial demonstrates an alternative to OpenNI for registering
  the depth and RGB cameras based on a user calibration instead of the
  factory one. It requires an extrinsic calibration, calculating the
  relative transform between the two cameras.
- [Calibrating the Kinect depth camera to an external RGB camera](#calibrating-the-kinect-depth-camera-to-an-external-rgb-camera):
  This tutorial demonstrates how to register the Kinect depth image to
  an external RGB camera instead of the built-in one. This requires an
  extrinsic calibration, calculating the relative transform between the
  two cameras.
- [Intrinsic calibration of the Kinect cameras](#intrinsic-calibration-of-the-kinect-cameras):
  This tutorial shows how to calibrate the intrinsic parameters of the
  IR (depth) and RGB cameras, including focal length and the distortion
  model. For applications requiring high accuracy, calibration can
  improve on the default camera models used by
  [openni_camera](https://index.ros.org/p/openni_camera). **This
  calibration does not necessary fully calibrate the depth.** Especially
  the ASUS Xtion is prone to depth errors and needs further calibration
  (see also [here](http://www.roboticsproceedings.org/rss09/p27.pdf) and
  [here](http://alexteichman.com/octo/clams/)). There is no official
  module in ROS yet to calibrate this (as of 6th February 2015).
- [Quick start guide](#quick-start-guide):
  Begin here. This tutorial demonstrates how to open a Kinect (or other
  OpenNI device) in ROS, introduces ROS tools for visualization and
  configuration, and explains how to get registered (depth + RGB)
  outputs like color point clouds.

## Recording and playing back Kinect data

Motivating use case: We are writing algorithms that process point
clouds, and wish to record some benchmark datasets for testing. We can
use [rosbag](https://index.ros.org/p/rosbag) to record and play back ROS
topics, but how can we best use it to capture the firehose of Kinect
data?

(The approach in this tutorial works for any Kinect data, not only point
clouds.)

### Recording data

#### Which topics do I need?

Since our end goal is to process point clouds, the obvious solution is
to record either the `camera/depth/points` (XYZ) or
`camera/depth_registered/points` (XYZRGB) topic. Unfortunately the
point cloud messages (especially XYZRGB) are *extremely*
memory-inefficent. Let's compare the size of the point cloud and raw
image (from which point clouds are produced) topics:

  -- ------------------------------------ -- ----------------- -- ---------------------------------------------- --
     Topic                                   Bytes per pixel      Notes                                          
     `camera/depth/image_raw`              2                    `uint16` in mm                               
     `camera/rgb/image_raw`                1                    `uint8` Bayer format                         
     `camera/depth/points`                 16                   `3\*sizeof(float)` + 4 bytes padding         
     `camera/depth_registered/points`      32                   Additional 16 bytes (mostly padding) for RGB   
  -- ------------------------------------ -- ----------------- -- ---------------------------------------------- --

For XYZRGB, the point cloud (32 Bpp) is more than ten times the size of
the raw data (3 Bpp). Not only will this waste disk space, it impairs
our ability to record point clouds at all. Given an XYZRGB point cloud
topic streaming 30fps at size 640x480, and a typical hard disk (data
transfer rate 1030 Mbits/s), we can record an upper bound of 13 point
clouds per second to disk.

To save both bandwidth and disk space, and for flexibility in later
processing, we will save the raw topics (and their associated camera
parameters).

If you do not need color (XYZ-only point clouds), record:

- `camera/depth/image_raw`
- `camera/depth/camera_info`

If you want XYZRGB point clouds, make sure that OpenNI registration is
enabled and record:

- `camera/depth_registered/image_raw`
- `camera/depth_registered/camera_info`
- `camera/rgb/image_raw`
- `camera/rgb/camera_info`

The point clouds will be reconstructed on-the-fly in playback.

##### Registered or unregistered

If you have fully calibrated your Kinect
([intrinsics](#intrinsic-calibration-of-the-kinect-cameras)
and
[extrinsics](#calibrating-the-kinect-depth-camera-to-the-built-in-rgb-camera)),
you may instead record:

- `camera/depth/image_raw`
- `camera/depth/camera_info`
- `camera/rgb/image_raw`
- `camera/rgb/camera_info`
- `/tf`

This is more flexible, as you retain the original (unregistered) depth
images. The depth-to-RGB registration performed by
openni_launch can do as well or better
than OpenNI, but does require extra calibration effort from the user.

`/tf` is needed for the relative transform between the depth and RGB
cameras, queried through [tf](https://index.ros.org/p/tf). If you record
this, use the `publish_tf:=false` argument (new in Fuerte) to
openni_launch during playback.

#### Start the device

First, start your device using
openni_launch. For this tutorial we'll
enable OpenNI registration and record XYZRGB data:


```
roslaunch openni_launch openni.launch depth_registration:=true
```



Since we will record only the raw topics, you could alternatively start
only the [openni_camera](https://index.ros.org/p/openni_camera) driver
(configured to use the `camera` namespace): 

```
ROS_NAMESPACE=camera rosrun openni_camera openni_node_unstable _depth_registration:=true _rgb_frame_id:=/camera_rgb_optical_frame _depth_frame_id:=/camera_rgb_optical_frame

ROS_NAMESPACE=camera rosrun openni_camera openni_node _depth_registration:=true _rgb_frame_id:=/camera_rgb_optical_frame _depth_frame_id:=/camera_rgb_optical_frame
```



This is ideal for low-resource systems. For recording purposes, you need
not have the relatively heavyweight
openni_launch stack installed at all!

#### Record the bag

Record the XYZRGB topics listed earlier: 

```
rosbag record camera/depth_registered/image_raw camera/depth_registered/camera_info camera/rgb/image_raw camera/rgb/camera_info --limit=60 -O kinect
```



This records 2s of Kinect data to `kinect.bag`. See
[rosbag](https://index.ros.org/p/rosbag) for all command-line options.

Checking the contents of your bag, you should see something like:


```
$ rosbag info kinect.bag 
path:        kinect.bag
version:     2.0
duration:    2.0s
start:       Apr 25 2012 16:36:43.05 (1335397003.05)
end:         Apr 25 2012 16:36:45.01 (1335397005.01)
size:        52.9 MB
messages:    240
compression: none [60/60 chunks]
types:       sensor_msgs/CameraInfo [c9a58c1b0b154e0e6da7578cb991d214]
             sensor_msgs/Image      [060021388200f6f0f447d0fcd9c64743]
topics:      camera/depth_registered/camera_info   60 msgs    : sensor_msgs/CameraInfo
             camera/depth_registered/image_raw     60 msgs    : sensor_msgs/Image     
             camera/rgb/camera_info                60 msgs    : sensor_msgs/CameraInfo
             camera/rgb/image_raw                  60 msgs    : sensor_msgs/Image
```



### Playing back data

Close (Ctrl-C) the ROS OpenNI driver you started earlier. We will bring
up openni_launch again, but without the
device driver. The bag will provide the raw data streams instead.

First, make sure that the Master (and Parameter server) is already
running. If not, use the following command: 

```
roscore
```



Before starting any nodes, do the magic invocation:


```
rosparam set /use_sim_time true
```



See [Clock](Clock) for the gory details. This basically tells nodes on
startup to use simulated time (ticked here by `rosbag`) instead of
wall-clock time (as in a live system). It avoids confusing
time-dependent components like [tf](https://index.ros.org/p/tf), which
otherwise would wonder why messages are arriving with timestamps far in
the past. Bring up the openni_launch
processing graph, using the `load_driver` launch file argument to
suppress loading the driver nodelet: 

```
roslaunch openni_launch openni.launch load_driver:=false
```



In Electric, you can instead feed the driver an invalid device ID. This
is a hack, and the driver will complain (a lot), but it works:


```
roslaunch openni_launch openni.launch device_id:=invalid
```



Open [rviz](https://index.ros.org/p/rviz) and create a `PointCloud2`
display of `/camera/depth_registered/points`, with fixed frame
`/camera_link`. Or, if you don't need visuals, just monitor the
topic: 

```
rostopic hz /camera/depth_registered/points
```



Finally, play back the recorded data through
[rosbag](https://index.ros.org/p/rosbag): 

```
rosbag play --clock kinect.bag
```

## Calibrating the Kinect depth camera to the built-in RGB camera

### Should I calibrate?

As we saw in the
[Quick Start guide](#registration-matching-depth-to-color),
OpenNI provides a good registration of the depth and RGB images
out-of-the-box, using the factory calibration. This easy solution should
be sufficient for most use cases.

Just as we can
[calibrate the depth camera to an external RGB camera](#calibrating-the-kinect-depth-camera-to-an-external-rgb-camera),
we can calibrate it to the built-in one. This has certain advantages:

- Registering the depth image compresses it into the narrower field of
  view of the RGB image, losing some information. For pure 3D processing
  (color not required), it is better to use the original depth image.
  Calibrating gives you the flexibility to use both registered and
  unregistered depth streams simultaneously.
- As a corollary: if you have (intentionally or by mistake)
  [recorded a bag](#recording-and-playing-back-kinect-data)
  containing RGB and unregistered depth data, you can recover registered
  depth data.
- Registration based on a user calibration may achieve slightly better
  accuracy, but this is limited by noise in the detected depths.

Disadvantages include:

- The extra effort required.
- Some sensors (e.g. the ASUS Xtion PRO Live, but not the Kinect) have
  hardware support for registration, saving CPU cycles.

### Intrinsic calibration

Make sure you have
[calibrated the depth and RGB camera intrinsics](#intrinsic-calibration-of-the-kinect-cameras).

### Extrinsic calibration

First read through the tutorial for
[calibrating to an external RGB camera](#calibrating-the-kinect-depth-camera-to-an-external-rgb-camera).
The approach here is the same, but there is a significant complication:
the Kinect cannot stream from its RGB and IR cameras simultaneously.
This is likely a firmware limitation.

Unfortunately, this breaks
[camera_pose_calibration](https://index.ros.org/p/camera_pose_calibration),
which achieves its robustness by looking for time intervals where the
checkerboard is stable and visible in all cameras. We will coerce it
into working, through a series of hacks to create the illusion of
simultaneous RGB and IR streams.

Create and bring up a launch file that opens the Kinect and starts the
extrinsic [tf](https://index.ros.org/p/tf) publisher:


```
<launch>

  <!-- Bring up Kinect and processing nodelets -->
  <include file="$(find openni_launch)/launch/openni.launch">
    <!-- Set cam info URLs, if not in the default location -->

    <!-- Suppress the default tf transforms (Fuerte only) -->
    <arg name="publish_tf" value="false" />
  </include>

  <!-- Extrinsic transform publisher -->
  <include file="$(find camera_pose_calibration)/blocks/calibration_tf_publisher.launch">
    <arg name="cache_file" value="/some/path/kinect_extrinsics_cache.bag" />
  </include>

</launch>
```



Make sure to set `cache_file` to a real path.

`openni.launch` publishes a default set of `tf` transforms linking
the IR and RGB cameras. We must suppress these defaults, as
`camera_pose_calibration` will provide that transform instead. In
Fuerte we can use the `publish_tf` argument. In Electric, copy
`openni.launch` and remove the lines at the bottom that include
`kinect_frames.launch`.

Rigidly place your checkerboard target in view of the Kinect. Since we
are hacking away the robustness guarantees of
`camera_pose_calibration`, it is crucial that neither the Kinect nor
the checkerboard move through the rest of the process. Provide diffuse
IR illumination (place a Post-it over the projector) and verify that the
checkerboard is clearly visible to both cameras:


```
rosrun image_view image_view image:=/camera/ir/image_raw

rosrun image_view image_view image:=/camera/rgb/image_color
```



Use [rosbag](https://index.ros.org/p/rosbag) to record 10 seconds of RGB
data to `rgb.bag`: 

```
rosbag record --limit=300 -O rgb.bag /camera/rgb/image_rect /camera/rgb/camera_info
```



Later we will play this back while streaming live from the IR camera.
But first, we must enter the realm of [simulated time](Clock):


```
rosparam set /use_sim_time true
```



Bring down (Ctrl-C) your launch file and bring it back up again. The
`/use_sim_time` tells all nodes to listen on the `/clock` topic for
the current ROS time, instead of using the system wall-clock time. The
OpenNI driver will not fully initialize at this point, because it is
waiting for a clock server. Play your recorded bag once to nudge it
along: 

```
rosbag play rgb.bag --clock
```



The `\--clock` option tells `rosbag` to act as the clock server, and
publish simulated time ticks on `/clock` in synch with the recorded
messages it's playing back.

Start the calibrator, substituting your checkerboard dimensions:


```
roslaunch camera_pose_calibration calibrate_2_camera.launch camera1_ns:=/camera/rgb_bag camera2_ns:=/camera/ir checker_rows:=4 checker_cols:=5 checker_size:=0.0249
```



Now play the bag again: 

```
rosbag play rgb.bag --clock /camera/rgb/camera_info:=/camera/rgb_bag/camera_info /camera/rgb/image_rect:=/camera/rgb_bag/image_rect
```



This time we remap the RGB topics so as not to conflict with the real,
live RGB topics. The calibrator listens on the live IR topics and the
recorded RGB topics.

The calibrator should find the checkerboard and successfully run the
optimization. For simplicity we'll only use one checkerboard view; this
is not ideal but should be adequate. The tf publisher caches the
transform to whatever path you gave it with the `cache_file` argument.

Now bring everything down and disable simulated time:


```
rosparam set /use_sim_time false
```



### Color point clouds

Bring your Kinect launch file up once more. `openni.launch` already
loads all the
[depth_image_proc](https://index.ros.org/p/depth_image_proc) nodelets
required to register the depth camera to the built-in RGB camera. Make
sure you have unblocked the IR projector - the Kinect won't see depth
at all without it!

Start [rviz](https://index.ros.org/p/rviz) and open a `PointCloud2`
display for topic `/camera/depth_registered/points`. Set the Fixed
Frame to `/camera_depth_optical_frame`. You should see a lovely color
point cloud.

![Registered point cloud](doc/RvizRegistered.png)

You can compare with OpenNI registration by enabling it as shown in the
[Quick Start guide](#registration-matching-depth-to-color).

## Calibrating the Kinect depth camera to an external RGB camera

### Attaching an external RGB camera

The Kinect's built-in RGB camera is more than adequate for many
purposes, but sometimes we want more. Higher-end cameras can offer
better image quality. OpenNI offers little control over important camera
features like exposure, gain, and white balance. If necessary, it is
possible to register the Kinect's depth camera to an external RGB
camera and build color point clouds using it instead of the built-in RGB
camera.

See [camera_drivers](camera_drivers) for a listing of cameras with
existing ROS drivers.

![Mounted external camera](doc/KinectProsilicaLabeled.jpg)

First you must rigidly mount your chosen RGB camera to the Kinect,
preferably as close as possible to the IR camera. The greater the
distance between the two, the more problems you will have with occlusion
(one camera sees things the other can't). Not surprisingly, the
built-in RGB camera occupies the sweet spot between the IR camera and IR
projector, where occlusion issues are minimized. You can get fairly
close mounting directly above or below the IR camera, however.

Registration has two requirements:

- Intrinsic calibration - the internal parameters of both cameras (focal
  length, distortion, etc.).
- Extrinsic calibration - the locations of the cameras with respect to
  each other in space.

### Intrinsic calibration

You should have calibrated the depth camera intrinsics in the
[previous tutorial](#intrinsic-calibration-of-the-kinect-cameras).

Perform the
[monocular calibration](https://index.ros.org/p/camera_calibration) of
the external RGB camera as well.

### Extrinsic calibration

We will use the
[camera_pose_calibration](https://index.ros.org/p/camera_pose_calibration)
package to determine the relative poses of the two cameras based on
mutual views of a checkerboard target. The transform will then be
broadcast over [tf](https://index.ros.org/p/tf). Make sure its stack is
installed: 

```
# Electric
sudo apt-get install ros-electric-camera-pose

# Fuerte
sudo apt-get install ros-fuerte-camera-pose
```



See the
[camera_pose_calibration Getting Started guide](https://index.ros.org/p/camera_pose_calibration)
for more information on the following steps, presented briefly here.

Create and bring up a launch file which:

- Opens the Kinect (and its various processing nodelets)
- Opens your external camera
- Starts [image_proc](https://index.ros.org/p/image_proc) for the
  external camera
- Starts the extrinsic [tf](https://index.ros.org/p/tf) publisher
  

```
<launch>

  <!-- Bring up Kinect -->
  <include file="$(find openni_launch)/launch/openni.launch">
    <!-- Set cam info URLs, if not in the default location -->
  </include>

  <!-- BRING UP EXTERNAL CAMERA HERE -->

  <!-- Also bring up image_proc for it, to get image_rect topic.
       In Electric, assuming camera namespace /my_camera: -->
  <node ns="my_camera" name="external_proc" pkg="image_proc" type="image_proc" />

  <!-- In Fuerte, you can instead load image_proc as nodelets into the
       OpenNI nodelet manager: -->
  <include ns="my_camera" file="$(find image_proc)/launch/image_proc.launch">
    <arg name="manager" value="/camera_nodelet_manager" />
  </include>

  <!-- Extrinsic transform publisher -->
  <include file="$(find camera_pose_calibration)/blocks/calibration_tf_publisher.launch">
    <arg name="cache_file" value="/some/path/kinect_extrinsics_cache.bag" />
  </include>

</launch>
```



The extrinsic publisher listens for the output of the optimization
routine we're about to run, publishes the results to `tf`, and saves
them to disk to be automatically loaded in the future.

As with the intrinsic calibration, make sure you get a clean
(unspeckled) IR image. E.g. cover the IR projector with a Post-it.

Now follow the
[Running calibration](https://index.ros.org/p/camera_pose_calibration)
instructions. The command will look something like:


```
# Replace the checkerboard dimensions and the /my_camera namespace

roslaunch camera_pose_calibration calibrate_2_camera.launch camera1_ns:=/my_camera camera2_ns:=/camera/ir checker_rows:=4 checker_cols:=5 checker_size:=0.0249
```



Capture as many checkerboard poses as you like, but three is likely
enough.

### Creating color point clouds

`openni.launch` loads all of the
[depth_image_proc](https://index.ros.org/p/depth_image_proc) nodelets
required to register the depth camera to the built-in RGB camera, if not
using
[OpenNI's registration](#registration-matching-depth-to-color)
capability. Since we are adding a new camera to the system, we need to
do a bit more work.

Fortunately we can reuse some of the machinery from
openni_launch, which splits off the
registration-related processing into its own launch file. Append the
following to your launch file from before: 

```
<launch>
  ...

  <!-- Register depth to external RGB camera and create point clouds -->
  <!-- Replace 'my_camera' with the correct namespace -->
  <include file="$(find openni_launch)/launch/includes/depth_registered.launch">
    <arg name="manager" value="/camera_nodelet_manager" />
    <arg name="rgb" value="my_camera" />
    <arg name="depth" value="camera/depth" />
    <!-- New namespace 'my_camera_depth' contains the outputs -->
    <arg name="depth_registered" value="my_camera_depth" />
    <arg name="suffix" value="my_camera_depth" />
  </include>

</launch>
```



Make sure that OpenNI registration is disabled - uncheck the
`depth_registration` box for `/camera/driver` using
[dynamic_reconfigure](https://index.ros.org/p/dynamic_reconfigure). Also
make sure you have unblocked the IR projector - the Kinect won't see
depth at all without it!

Now start [rviz](https://index.ros.org/p/rviz) and open a
`PointCloud2` display for topic `/my_camera_depth/points`. Set the
Fixed Frame to `/camera_depth_optical_frame`. You should see a lovely
color point cloud. Cover the Kinect RGB camera with your thumb to verify
it is not being used.

![Registered point cloud](doc/RvizExternalRegistered.png)

This screenshot was generated using the rig pictured at the top of the
page, with the external camera mounted below the IR camera.

An unfortunate but instructive artifact is visible: the top of the hand
is projected onto the back of the chair. This is because:

- That chair section is visible to the IR camera, but not to the
  external RGB camera. The hand blocks the RGB camera's view.
- The chair points are projected to where they would have appeared in
  the RGB image, which overlaps with the hand.
- The
  [depth_image_proc/register](https://index.ros.org/p/depth_image_proc)
  nodelet performs Z-buffering (prefers a nearer depth to a further one
  for the same RGB pixel), but\...
- It fails here because the external camera is much higher resolution
  (5Mp) than the IR camera, allowing the further away chair points to
  "slip through the cracks" in the Z-buffering.

A nice project would be modifying `depth_image_proc/register` to
densely interpolate the higher-resolution registered depth image.

## Intrinsic calibration of the Kinect cameras

### Should I calibrate?

Not necessarily. The
[openni_camera](https://index.ros.org/p/openni_camera) driver provides
default camera models out-of-the-box with reasonably accurate focal
lengths (relating 3D points to 2D image coordinates). They do not model
lens distortion, but fortunately the Kinect uses low-distortion lenses
(`\|k1\| = 0.1`), so even the edges of the image are not displaced by
more than a few pixels.

If your application requires maximum accuracy from the Kinect's 3D
data, however, performing a rigorous calibration is helpful.

### RGB camera

Bring up the OpenNI driver: 

```
roslaunch openni_launch openni.launch
```



Now follow the standard
[monocular camera calibration](https://index.ros.org/p/camera_calibration)
instructions. Use the following command (substituting the correct
dimensions of your checkerboard): 

```
rosrun camera_calibration cameracalibrator.py image:=/camera/rgb/image_raw camera:=/camera/rgb --size 5x4 --square 0.0245
```



Don't forget to Commit your successful calibration.

### IR (depth) camera

The Kinect detects depth by using an IR camera and IR speckle projector
as a pseudo-stereo pair. We will calibrate the "depth" camera by
detecting checkerboards in the IR image, just as we calibrated the RGB
camera.

The speckle pattern makes it impossible to detect the checkerboard
corners accurately in the IR image. The simplest solution is to cover
the projector (lone opening on the far left) with one or two Post-it
notes, mostly diffusing the speckles. An ideal solution is to block the
projector completely and provide a separate IR light source. Good
illumination sources include sunlight, halogen lamps, or incandescent
lamps.

  -- ------------------------------- -- ------------------------------------------------- --
     ![IR](doc/ir.jpg)                  ![IR covered](doc/ir_covered.jpg)                 
     <:> IR with speckle pattern      <:> IR with projector covered by Post-it note   
  -- ------------------------------- -- ------------------------------------------------- --

As before, follow the
[monocular camera calibration](https://index.ros.org/p/camera_calibration)
instructions: 

```
rosrun camera_calibration cameracalibrator.py image:=/camera/ir/image_raw camera:=/camera/ir --size 5x4 --square 0.0245
```



The Kinect camera driver cannot stream both IR and RGB images. It will
decide which of the two to stream based on the amount of subscribers, so
kill nodes that subscribe to RGB images before doing the IR calibration.

Don't forget to Commit your successful calibration.

### Where are the intrinsics saved?

When you click Commit, `cameracalibrator.py` sends the new calibration
to the camera driver as a service call. The driver immediately begins
publishing the updated calibration on its `camera_info` topic.

[openni_camera](https://index.ros.org/p/openni_camera) uses
[camera_info_manager](https://index.ros.org/p/camera_info_manager) to
manage calibration parameters. By default, it saves intrinsics to
`\$HOME/.ros/camera_info/NAME.yaml` and identifies them by the device
serial number: 

```
$ ls ~/.ros/camera_info/
depth_B00362708888047B.yaml  rgb_B00362708888047B.yaml
```



Whenever you bring up the OpenNI driver, it will look for a previously
saved calibration. If you want to share the intrinsics among multiple
users, move them somewhere public (e.g. `/public/path/`) and use a
launch file which configures the camera info URLs:


```
<launch>

 <!-- Include official launch file and specify camera_info urls -->
 <include file="$(find openni_launch)/launch/openni.launch">
   <!-- provide arguments to that launch file -->
   <arg name="rgb_camera_info_url"
        value="file:///public/path/rgb_B00362708888047B.yaml" />
   <arg name="depth_camera_info_url"
        value="file:///public/path/depth_B00362708888047B.yaml" />
 </include>

</launch>
```

## Quick start guide

### Opening the device

Open a command line and launch the OpenNI driver like this:


```
roslaunch openni_launch openni.launch
```



That's it! `openni.launch` opens your Kinect and processes the raw
data into convenient outputs like [point clouds](pcl). See the
reference documentation for
all topics published by `openni.launch`. We'll explore some of them
below.

### Visualizing the data

#### rviz

We'll use the [rviz](https://index.ros.org/p/rviz) 3D visualization
environment to view point clouds: 

```
rosrun rviz rviz
```



Set the Fixed Frame (top of the Display panel under Global Options) to
`/camera_link`.

In the Displays panel, click Add and choose the
[PointCloud2 display](https://index.ros.org/p/rviz). Set its topic to
`/camera/depth/points`. Turning the background color to light gray can
help with viewing.

This is the *unregistered* point cloud in the frame of the depth (IR)
camera. It is not matched with the RGB camera images. We'll get to
color point clouds below. For now, set Color Transformer to
`AxisColor` to colormap the points by distance.

![rviz](doc/RvizWithDisplaysPanel.png)

Also try opening an
[image display](http://www.ros.org/wiki/rviz/DisplayTypes/Image) and
check out the various image topics.

#### Image viewers

Alternatively you can use
[image_view](https://index.ros.org/p/image_view) to view both the RGB
image: 

```
rosrun image_view image_view image:=/camera/rgb/image_color
```



and the depth image: 

```
rosrun image_view image_view image:=/camera/depth/image
```



  -- --------------------- -- ------------------------- --
     ![RGB](doc/rgb.jpg)      ![Depth](doc/depth.png)   
  -- --------------------- -- ------------------------- --

[image_view](https://index.ros.org/p/image_view) also contains the
`disparity_view` viewer for
[sensor_msgs/msg/DisparityImage](https://docs.ros.org/en/rolling/p/sensor_msgs/msg/DisparityImage.html)
messages: 

```
rosrun image_view disparity_view image:=/camera/depth/disparity
```



![Disparity](doc/disparity.png)

Although useful for visualization, for general 3D processing you are
encouraged to use the point cloud or depth image topics rather than
disparity images, which are particular to stereo. See
[REP 118](http://www.ros.org/reps/rep-0118.html) for technical details
about depth images.

### Registration: matching depth to color

The depth and color images come from two separate, slightly offset,
cameras, so they do not perfectly overlap. However, for each pixel in
the depth image, we can calculate its position in 3D space and reproject
it into the image plane of the RGB camera. In this way we build up a
*registered* depth image, where each pixel is aligned with its
counterpart in the RGB image.

OpenNI has a builtin registration capability, which uses the Kinect
factory calibration. We can use
[dynamic_reconfigure](https://index.ros.org/p/dynamic_reconfigure) to
change the ROS OpenNI driver's settings at runtime. Open the dynamic
reconfigure GUI: 

```
rosrun rqt_reconfigure rqt_reconfigure
```



Select `/camera/driver` from the drop-down menu. Enable the
`depth_registration` checkbox.

![Reconfigure GUI](doc/ReconfigureGui.png)

Note that the ROS driver is now receiving registered depth images from
the underlying OpenNI framework; it does not have access to the
unregistered data. The ROS driver no longer publishes in the
unregistered `/camera/depth/` namespace, but instead in
/`camera/depth_registered/`.

For example, to view the registered disparity image:


```
rosrun image_view disparity_view image:=/camera/depth_registered/disparity
```



![Disparity registered](doc/disparity_reg.png)

Now let's look at the registered point cloud. Go back to `rviz`, and
change the topic of your !PointCloud2 display to
`/camera/depth_registered/points`. Set Color Transformer to `RGB8`.
You should see a color, 3D point cloud of your scene.

![rviz](doc/RvizColor.png)
