## Overview

This package wraps an object tracker provided by the ViSP library. The
tracker provides the tracked object position with respect to the camera.
It requires the object 3d model and the object initial pose.

![ViSP box tracking](doc/visp-box-tracking.png)

The package is composed of one node called `tracker` that does the
tracking and two additional nodes `client` (that allows to set the
initial pose by user mouse click) and `viewer` that allows to
visualize the result of the tracking.

The `tracker` node tries to track the object as fast as possible but
needs to be initialized using the client. The viewer can be used to
monitor the tracking result.

### Use cases

- [Optical Localization for Robot Arms, Initial Experiments (Edinburgh Hacklab)](http://edinburghhacklab.com/2012/04/optical-localization-for-robot-arms-initial-experiments/)
- [Augmented reality, object grasping by Romeo humanoid robot, satellite tracking moving on a geosynchronous orbit, \...](https://visp.inria.fr/mbt/)

## Reference

- [A.I. Comport, E. Marchand, M. Pressigout, F. Chaumette. Real-time markerless tracking for augmented reality: the virtual visual servoing framework. IEEE Trans. on Visualization and Computer Graphics, 12(4):615-628, July 2006](http://www.irisa.fr/lagadic/publi/publi/Comport06b-eng.html)

## Roadmap

The package implementation is finished. Minor changes in the API may
happen in the future but impact should be limited.

These features would be valuable contribution to this package:

- Rely on !AssImp to support COLLADA models (instead of ViSP based VRML
  loader).
- Use RViz markers and API to support display directly in RViz.

## Installation

visp_tracker is part of
[vision_visp](https://index.ros.org/p/vision_visp) stack.

- To install visp_tracker package run
  

```
sudo apt-get install ros-$ROS_DISTRO-visp-tracker
```



<!-- -->

- Or to install the complete stack run 

```
sudo apt-get install ros-$ROS_DISTRO-vision-visp
```



## Features

This package objective is to provide the pose of an object (i.e.
position and orientation) in a sequence of images knowing its 3d model
and its initial pose. It also provides the pose covariance.

<a id="ROS_API"></a>

## ROS API

Note: data is only published if there is at least one listener.

### tracker

Main tracking node.

#### Subscribed Topics

- `~camera_prefix/camera_info`
  ([sensor_msgs/msg/CameraInfo](https://docs.ros.org/en/rolling/p/sensor_msgs/msg/CameraInfo.html)):
  Camera calibration information, see the camera_calibration package for
  more details.
- `~camera_prefix/image_rect`
  ([sensor_msgs/msg/Image](https://docs.ros.org/en/rolling/p/sensor_msgs/msg/Image.html)):
  Rectified image, see the camera_calibration package for more details.
- `object_position_hint`
  ([geometry_msgs/msg/TransformStamped](https://docs.ros.org/en/rolling/p/geometry_msgs/msg/TransformStamped.html)):
  Estimation of the tracked object position. This is optional and allows
  automatic tracker restart if the tracking fails.

#### Published Topics

- `object_position`
  ([geometry_msgs/msg/PoseStamped](https://docs.ros.org/en/rolling/p/geometry_msgs/msg/PoseStamped.html)):
  Tracking object pose (stamped).
- `object_position_covariance`
  ([geometry_msgs/msg/PoseWithCovarianceStamped](https://docs.ros.org/en/rolling/p/geometry_msgs/msg/PoseWithCovarianceStamped.html)):
  Tracking object pose with its associated covariance (stamped). You may
  want to use [rviz_plugin_covariance](rviz_plugin_covariance) to
  display this datatype in rviz (Fuerte+).
- `moving_edge_sites`
  ([visp_tracker/msg/MovingEdgeSites](https://docs.ros.org/en/rolling/p/visp_tracker/msg/MovingEdgeSites.html)):
  Moving edge sites information (stamped). For debugging/monitoring
  purpose.
- `klt_points_positions`
  ([visp_tracker/msg/KltPoints](https://docs.ros.org/en/rolling/p/visp_tracker/msg/KltPoints.html)):
  Position and id of the keypoints (stamped). For debugging/monitoring
  purpose.

#### Services

- `init_tracker`
  ([visp_tracker/srv/Init](https://docs.ros.org/en/rolling/p/visp_tracker/srv/Init.html)):
  Initialize the tracking by providing the model name, model path,
  initial object pose and moving edge settings.
- `tracking_meta_data`
  ([visp_tracker/srv/TrackingMetaData](https://docs.ros.org/en/rolling/p/visp_tracker/srv/TrackingMetaData.html)):
  Provides the current camera prefix, model name and model path.

#### Parameters

- `~camera_prefix` (`std_msgs/String`): Camera topics namespace
  ('image_rect' and 'camera_info' topics must be published in this
  namespace)
- `~first_threshold` (`float64`): What proportion of points should be
  valid to acccept an initial pose.
- `~lambda` (`float64`): Gain used to compute the control law.
- `~mask_size` (`int64`): Mask size (in pixel) used to compute the image
  gradient and determine the object contour.
- `~min_samplestep` (`float64`): Minimum allowed samplestep. Useful to
  specify a lower bound when the samplestep is changed.
- `~model_name` (`std_msgs/String`): Model name (without the `.wrl`
  filename extension)
- `~model_path` (`std_msgs/String`): Model database path. Uses the
  [resource_retriever](https://index.ros.org/p/resource_retriever)
  syntax to fetch remote models (i.e. `package:*`, `http:*`, etc.)
- `~mu1` (`float64`): Minimum image contrast allowed to detect a
  contour.
- `~mu2` (`float64`): Maximum image contrast allowed to detect a
  contour.
- `~n_mask` (`int64`): Number of masks applied to determine the object
  contour.
- `~n_total_sample` (`int64`): How many discretization points are used
  to track the feature.
- `~range` (`int64`): Maximum seek distance on both sides of the
  reference pixel.
- `~sample_step` (`int64`): Minimum distance in pixel between two
  discretization points.
- `~strip` (`int64`): How many pixels are ignored around the borders.
- `~threshold` (`float64`): Value used to determine if a moving edge is
  valid or not.
- `~aberration` (`float64`): Ignored.
- `~init_aberration` (`float64`): Ignored.
- `~compensate_robot_motion` (`bool`, default: `false`): If set to true,
  the robot movement will be used to help reliable tracking
  (experimental). For this feature to work, tf must provide the
  transformation between the world frame id and the camera.
- `~world_frame_id` (`string`, default: `/odom`): World frame name (see
  `compensate_robot_motion`).

#### Required tf Transforms

- `~world_frame_id` → `<camera frame>`: Robot movement (optional, see
  `compensate_robot_motion`).

#### Provided tf Transforms

- `<camera frame>` → `visp_tracker`: Object position w.r.t. the camera.

### client

Command line tool used to decide which object to track and what is its
initial pose.

#### Parameters

- `~camera_prefix` (`std_msgs/String`): Camera topics namespace
  ('image_rect' and 'camera_info' topics must be published in this
  namespace)
- `~tracker_prefix` (`std_msgs/String`, default: `tracker_mbt`):
  Namespace in which the tracker has been launched.
- `~model_path` (`std_msgs/String`, default:
  `$(find visp_tracker)/models`): Model location on the filesystem.
- `~model_name` (`std_msgs/String`): Model name. **This parameter is
  mandatory when launching the client.**

### viewer

Monitoring tool.

#### Parameters

- `~tracker_prefix` (`std_msgs/String`, default: `/tracker_mbt`):
  Namespace in which the tracker has been launched.
- `~image_transport` (`string`, default: `raw`):
  [image_transport](https://index.ros.org/p/image_transport) plug-in to
  be used.

## Nodelets

This package provides both nodes and nodelet versions of the tracker,
client and viewer.

They are respectively named:

- `visp_tracker/Tracker`
- `visp_tracker/TrackerClient`
- `visp_tracker/TrackerViewer`

\...and provide the same API than the equivalent nodes.

When the nodelet version is used, no-copy intraprocess publishing is
used. See the [nodelet](https://index.ros.org/p/nodelet) documentation
for more information.

An example launch file is also provided: 

```
roslaunch visp_tracker tutorial-nodelet.launch
```



*Note:* even if a nodelet is available for the client and viewer, one
should avoid running them in the same process than the vision pipeline
to avoid crashing the whole pipeline if something goes wrong.

## Launch file example

Here is a launch file which starts the tracker and client.

{ }}}}

{ }}}}

## Report a bug

Use !GitHub to
[report a bug or submit an enhancement](https://github.com/lagadic/visp_tracker/issues).

## Tutorials

- [Fine tuning of the tracking parameters](#fine-tuning-of-the-tracking-parameters):
  Modifying offline and online the tracking parameters.
- [Getting started with the ViSP moving edge tracker](#getting-started-with-the-visp-moving-edge-tracker):
  How to track an object using a recorded video sequence.
- [Tracking your own model](#tracking-your-own-model):
  How to track a custom object.

## Troubleshooting

### Reminder

- **The tracker uses CORRECTED images.** Be sure to calibrate your
  camera and subscribe to the image topic after correction (see
  [image_proc](https://index.ros.org/p/image_proc)).
- **The tracker uses an initial pose.** You will need to use either the
  GUI or an initial estimation to start the tracker.

### Tips and tricks

#### How fast is the tracking?

Each time a new pose is computed, a new pose is published. Therefore, to
see your tracking frequency you can run: 

```
$ rostopic hz /tracker_mbt/result
```



There is no ideal tracking frequency as it depends on how fast your
object moves. However, if the frequency is less than 25hz, the tracking
will probably fail.

#### The tracking initialization fails

If the initialization using the GUI fails, it is either due to the model
(bad format, failed to parse\...) or due the camera calibration
parameters.

The tracker uses the K and P matrices information as well as the camera
distorsion model. Make sure that your camera is correctly calibrated
(using [camera_calibration](https://index.ros.org/p/camera_calibration)
for instance). See also the message documentation
[sensor_msgs/msg/CameraInfo](https://docs.ros.org/en/rolling/p/sensor_msgs/msg/CameraInfo.html).

#### The tracking fails at the first iteration after initialization

Make sure the model normals are correctly set. The tracker eliminates
invisible faces. If normals are wrong, the tracker will remove all the
object faces.

#### My tracking is too slow!

Several factors can slow down your tracking.

First, you will never be able to track at a higher frequency than the
rectified image topic frequency. Tracking is only done once per image
and stops until a new image is received.

Therefore, you should take a look at your rectified image topic
frequency by running: 

```
# Topic name should be changed to match the topic you use.
$ rostopic hz /camera/image_rect
```



Once you have checked that the tracking frequency is way lower than the
rectified image topic frequency, it means that you may have problem.

- Is the grabbing and processing on different computer? This setup is
  not recommended. Make sure in the tracker node output that no warning
  appears regarding message synchronization. The node only tracks when
  receiving synchronized image and camera calibration data. If your
  network is too slow, it may happen only once in a while.
- Is your model too complex? You can try to reduce the number of lines
  in your model.
- Change the tracking parameters. Decrease the `mask_size`, the
  `sample_step` and increase the `ntotal_sample` to run the
  algorithm faster.

#### Use image_transport to use compressed video streams

If the tracker is on a remote machine, you may use the additional
`_image_transport` parameter to use compressed video streams. See
[image_transport](https://index.ros.org/p/image_transport) documentation
for more details about compressed streams.

It will reduce the amount of data passing through the network but will
induce a delay in the transmission and add CPU load on the remote
machine which has to compress the flow.

However, **do not** use it when launching the tracker node. The camera
device and tracker node should be on the same machine to avoid delays
and in this case, it is not necessary to compress the stream. On the
opposite, it will decrease the tracking quality.

On the opposite, you can used compressed streams for the client and
viewer. It is not recommended for the client as it may decrease the
click precision but is highly recommended for the viewer.

The viewer ensures that the projected object pose and camera data are
synchronized which mean that even if a delay is induced by the stream
compression, displayed information will remain consistent.

#### The camera calibration is crucial

The main idea behind the virtual visual servoing is to project lines
from a 3d model and compare them with the image lines. If the camera
rectification is bad, it will be impossible to find a pose where the
projected lines and the real one are at the same location. Therefore the
algorithm will fail.

## Fine tuning of the tracking parameters

- **Description:** Modifying offline and online the tracking parameters.
- **Tutorial Level:** INTERMEDIATE

### Parameters description

The most important parameters for the tracking are the moving edge
parameters. Moving edges are points along the object lines which are
detected during the tracking and use to update the object pose.

They have a great influence on the tracking quality and on the CPU load
induced by the tracking.

Different parameters can be tuned, their effect is documented in the
associated message
[visp_tracker/msg/MovingEdge](https://docs.ros.org/en/rolling/p/visp_tracker/msg/MovingEdge.html).

### Offline modification

You can start the tracking with specific parameters by typing the
following command while the client is running: 

```shell
rosrun dynamic_reconfigure dynparam load /tracker_mbt_client my-parameters.yaml
```



### Online modification

When the tracking is started, you can modify the parameters by typing:


```shell
rosrun dynamic_reconfigure dynparam load /tracker_mbt my-parameters.yaml
```



Or by using the graphical interface: 

```shell
rosrun dynamic_reconfigure reconfigure_gui /tracker_mbt
```



![Tracker node reconfigure GUI](doc/visp-tracker-reconfigure-gui.png)

## Getting started with the ViSP moving edge tracker

- **Note:** Start here if you want to learn how to track an object.
- **Description:** How to track an object using a recorded video
  sequence.
- **Tutorial Level:** BEGINNER
- **Next Tutorial:**
  [Tracking your own model](#tracking-your-own-model)

### Starting the video sequence

The package comes with a sample bag file in
`bag/tutorial-static-box.bag`.

It stores synchronized messages for a monocular camera and its
associated camera information.

You can launch rosbag replay, the tracker node and a client by typing:



```
# If you are using ROS Groovy or later:
roslaunch visp_tracker tutorial.launch
# If you are using ROS Fuerte or later:
roslaunch visp_tracker tutorial-fuerte.launch
# If you are using ROS Diamondback or before:
roslaunch visp_tracker tutorial.launch
```



### Setting the initial pose

The client will launch automatically and display the following image.

![ViSP box tracking](doc/visp-tracking-start.png)

\- You must first right-click to enter in the manual pose initialization
stage, then left-click on four of the box corners in the order
illustrated by the following screenshot:

![ViSP box tracking](doc/visp-tracking-init.png)

\- If the initial pose is satisfactory (ie. the green lines of the model
match the object edges) you have to validate the initial pose with a
left-click. Note that with a right-click you enter again in the previous
stage where you have to left-click on the four points.

\- Before validating the initial pose, you can tune the tracking
parameters:



```
rosrun rqt_reconfigure rqt_reconfigure /tracker_mbt_client
```



\- Finally a new left-click closes the initialization stage and start
the tracker.

### Monitoring the tracking

You can then monitor the tracker by running:



```
rosrun visp_tracker visp_tracker_viewer _camera_prefix:=/wide_left/camera
```

 The viewer should display a result similar to
this screenshot:
![ViSP box tracking](doc/visp_tracker_Tutorials_Getting%20started_visp-box-tracking.png)

To plot the object position, type:



```
rqt_plot topics /object_position/transform/translation/x:y:z
```



### Fine tuning the tracking parameters

Additionally, the tracking parameters can be changed online using
`rqt_reconfigure`:



```
rosrun rqt_reconfigure rqt_reconfigure /tracker_mbt
```

## Tracking your own model

- **Description:** How to track a custom object.
- **Tutorial Level:** BEGINNER
- **Next Tutorial:**
  [Fine tuning of the tracking parameters](#fine-tuning-of-the-tracking-parameters)

If you are not familiar with ViSP model-based tracker, follow first the
ViSP
[model-based tutorial](http://visp-doc.inria.fr/doxygen/visp-daily/tutorial-tracking-mb.html).

To use the tracker with your own object, you need to create an object
database.

The object database is located by default in the `models` directory
were tree objects are provided: `laas-box`, `floppy-box` and
`shelf`.

You can either add your own object in a new directory located in the
`models` directory or choose to put your directory else where. In this
case, you have to fill the `model_path` parameter accordingly when
starting the client (or initializing the object using the
'init_tracker' service).

### Required files

Consider that you want to track a new object called `my-box`.

Create first a folder called `my-box`, for example in the `models`
folder besides existing `laas-box`. In this new `my-box` folder you
have to introduce the following files:

- The CAD model of the object to consider, either in `.cao` or in
  `.wrl` format
- `my-box.cao`: object CAD model in `.cao` format. This home-made
  format is described in
  [here](http://visp-doc.inria.fr/doxygen/visp-daily/tutorial-tracking-mb.html#mb_advanced_cao).
- `my-box.wrl`: object CAD model in VRML format. This format is
  described
  [here](http://visp-doc.inria.fr/doxygen/visp-daily/tutorial-tracking-mb.html#mb_advanced_wrml).
- `my-box.init`: initialization file used to estimate the initial pose
  by clicking on 2D points in the image. The content of this file is
  described
  [here](http://visp-doc.inria.fr/doxygen/visp-daily/tutorial-tracking-mb.html#mb_started_src_explained).
- `tracker.yaml`: best tracking parameters for this object (optional).
  The signification of the tracker settings is given
  [here](http://visp-doc.inria.fr/doxygen/visp-daily/tutorial-tracking-mb.html#mb_settings).
- `my-box.ppm`: this file is optional and corresponds to an image that
  shows where the user has to click to initialize the tracker.
- Additionally, `my-box.0.pos` contains the last initial pose and is
  created automatically by the client.

Once created, modify `model_name` parameter to `my-box`.

### Modeling the object

Any 3D modeling software can be used as long as it can export its models
to the VRML format. But in that case, be careful since all the triangles
will be exported. In that case the model will contain all the triangle
edges even those that are not real object contours. An example of such a
model that doesn't work with moving-edges features is given
[here](http://visp-doc.inria.fr/doxygen/visp-daily/tutorial-tracking-mb.html#mb_teabox_cao_triangle).
That is why we suggest to use only a 3D modeling software to determine
the 3D coordinates of some points and create the CAD model manually.

Keep in mind that this tracker tracks **lines**. Therefore, when loading
an object, the lines are extracted from the 3D model and all the other
information are discarded.

Warning: the surface normals are used to determine if a face is visible
or not. They are taken into account and if they are not correctly
oriented (normal vector toward outside the object), the tracker will
fail.

It is also important to notice that the tracking frequency decreases as
the number of tracked lines increases. Therefore, do not give to the
tracker a full model of your object, trim all the lines which cannot be
tracked precisely (bad gradient, hardly visible\...).

Popular modeling software includes:

- [Blender](http://www.blender.org/) - open source, powerful modeling
  software
- [AC3d](http://www.inivis.com/) - proprietary/non-free simple modeling
  software
- [Modeling software list on Wikipedia](http://en.wikipedia.org/wiki/3D_computer_graphics_software)

### Writing the initialization file

The initialization file is used by the client to compute the object
initial pose.

To compute the initial pose, the client does as follow:

- grab an image
- let the user click on a predetermined object location such as a corner
- repeat for all points in the initialization file
- compute the best pose such as the 3d pose projection matches the
  clicked points.

To do so, we need to associate 2D points with particular 3D points in
the tracked object. This association is provided by the initialization
file.

Here is the initialization file for the `laas-box`:



```
4
-0.175  0.175  0.156
-0.175 -0.175  0.156
 0.175 -0.175  0.156
-0.175 -0.175 -0.156
```

 In this example, the user will click on four
points. The first point coordinates are (X = -0.175, Y = 0.175, Z =
0.156).

Using your modeling software, determine the 3D coordinates of four
particular points of your object (four corners for instance). They
**should not be on the same plane**.

It is a good idea to provide an image showing in which order and where
to click on the object. This file with extension .ppm is optional.

### Providing the recommended tracking parameters

Optionally, you can provide the `tracker.yaml` file with specific
tracking parameters:

Here is a good starting point:



```yaml
{
mask_size: 3,
mu1: 0.5,
mu2: 0.5,
n_mask: 180,
ntotal_sample: 800,
range: 10,
sample_step: 3.,
threshold: 2000.0
}
```

 This file is optional and not automatically
read.
