## Overview

This package wraps an object tracker provided by the ViSP library. The
tracker provides the tracked object position with respect to the camera.
It requires the object 3d model and the object initial pose.

![ViSP box tracking\|width=400](attachment:visp-box-tracking.png)

The package is composed of one node called \`tracker\` that does the
tracking and two additional nodes \`client\` (that allows to set the
initial pose by user mouse click) and \`viewer\` that allows to
visualize the result of the tracking.

The \`tracker\` node tries to track the object as fast as possible but
needs to be initialized using the client. The viewer can be used to
monitor the tracking result.

### Use cases

-   [Optical Localization for Robot Arms, Initial Experiments (Edinburgh Hacklab)](http://edinburghhacklab.com/2012/04/optical-localization-for-robot-arms-initial-experiments/)
-   [Augmented reality, object grasping by Romeo humanoid robot, satellite tracking moving on a geosynchronous orbit, \...](https://visp.inria.fr/mbt/)

## Reference

-   [A.I. Comport, E. Marchand, M. Pressigout, F. Chaumette. Real-time markerless tracking for augmented reality: the virtual visual servoing framework. IEEE Trans. on Visualization and Computer Graphics, 12(4):615-628, July 2006](http://www.irisa.fr/lagadic/publi/publi/Comport06b-eng.html)

## Roadmap

The package implementation is finished. Minor changes in the API may
happen in the future but impact should be limited.

These features would be valuable contribution to this package:

-   Rely on !AssImp to support COLLADA models (instead of ViSP based
    VRML loader).
-   Use RViz markers and API to support display directly in RViz.

## Installation

[visp_tracker](visp_tracker) is part of [vision_visp](vision_visp)
stack.

-   To install [visp_tracker](visp_tracker) package run
    ```
sudo apt-get install ros-$ROS_DISTRO-visp-tracker
```

```{=html}
<!-- -->
```
-   Or to install the complete stack run ```
sudo apt-get install ros-$ROS_DISTRO-vision-visp
```

## Features

This package objective is to provide the pose of an object (i.e.
position and orientation) in a sequence of images knowing its 3d model
and its initial pose. It also provides the pose covariance.

## ROS API

Note: data is only published if there is at least one listener.

```clearsilver
name = tracker
desc = Main tracking node.

sub {
  0.name = ~camera_prefix/camera_info
  0.type = sensor_msgs/CameraInfo
  0.desc = Camera calibration information, see the camera_calibration package for more details.

  1.name = ~camera_prefix/image_rect
  1.type = sensor_msgs/Image
  1.desc = Rectified image, see the camera_calibration package for more details.

  2.name = object_position_hint
  2.type = geometry_msgs/TransformStamped
  2.desc = Estimation of the tracked object position. This is optional and allows automatic tracker restart if the tracking fails.
}

pub {
  0.name = object_position
  0.type = geometry_msgs/PoseStamped
  0.desc = Tracking object pose (stamped).

  1.name = object_position_covariance
  1.type = geometry_msgs/PoseWithCovarianceStamped
  1.desc = Tracking object pose with its associated covariance (stamped). You may want to use [[rviz_plugin_covariance]] to display this datatype in rviz (Fuerte+).

  2.name = moving_edge_sites
  2.type = visp_tracker/MovingEdgeSites
  2.desc = Moving edge sites information (stamped). For debugging/monitoring purpose.

  3.name = klt_points_positions
  3.type = visp_tracker/KltPoints
  3.desc = Position and id of the keypoints (stamped). For debugging/monitoring purpose.
}

param {
  0.name = ~camera_prefix
  0.type = std_msgs/String
  0.desc = Camera topics namespace ('image_rect' and 'camera_info' topics must be published in this namespace)

  1.name = ~first_threshold
  1.type = float64
  1.desc = What proportion of points should be valid to acccept an initial pose.

  2.name = ~lambda
  2.type = float64
  2.desc = Gain used to compute the control law.

  3.name = ~mask_size
  3.type = int64
  3.desc = Mask size (in pixel) used to compute the image gradient and determine the object contour.

  4.name = ~min_samplestep
  4.type = float64
  4.desc = Minimum allowed samplestep. Useful to specify a lower bound when the samplestep is changed.

  5.name = ~model_name
  5.type = std_msgs/String
  5.desc = Model name (without the `.wrl` filename extension)

  6.name = ~model_path
  6.type = std_msgs/String
  6.desc = Model database path. Uses the [[resource_retriever]] syntax to fetch remote models (i.e. `package://`, `http://`, etc.)

  7.name = ~mu1
  7.type = float64
  7.desc = Minimum image contrast allowed to detect a contour.

  8.name = ~mu2
  8.type = float64
  8.desc = Maximum image contrast allowed to detect a contour.

  9.name = ~n_mask
  9.type = int64
  9.desc = Number of masks applied to determine the object contour.

  10.name = ~n_total_sample
  10.type = int64
  10.desc = How many discretization points are used to track the feature.

  11.name = ~range
  11.type = int64
  11.desc = Maximum seek distance on both sides of the reference pixel.

  12.name = ~sample_step
  12.type = int64
  12.desc = Minimum distance in pixel between two discretization points.

  13.name = ~strip
  13.type = int64
  13.desc = How many pixels are ignored around the borders.

  14.name = ~threshold
  14.type = float64
  14.desc = Value used to determine if a moving edge is valid or not.

  15.name = ~aberration
  15.type = float64
  15.desc = Ignored.

  16.name = ~init_aberration
  16.type = float64
  16.desc = Ignored.

  17.name = ~compensate_robot_motion
  17.type = bool
  17.desc = If set to true, the robot movement will be used to help reliable tracking (experimental). For this feature to work, tf must provide the transformation between the world frame id and the camera.
  17.default = false

  18.name = ~world_frame_id
  18.type = string
  18.desc = World frame name (see `~compensate_robot_motion`).
  18.default = /odom
}

srv {
  0.name = init_tracker
  0.type = visp_tracker/Init
  0.desc = Initialize the tracking by providing the model name, model path, initial object pose and moving edge settings.

  1.name = tracking_meta_data
  1.type = visp_tracker/TrackingMetaData
  1.desc = Provides the current camera prefix, model name and model path.
}

prov_tf {
  0.from = <camera frame>
  0.to   = visp_tracker
  0.desc = Object position w.r.t. the camera.
}

req_tf {
  0.from = ~world_frame_id
  0.to   = <camera frame>
  0.desc = Robot movement (optional, see `~compensate_robot_motion`).
}
```

```clearsilver
name = client
desc = Command line tool used to decide which object to track and what is its initial pose.
param {
  0.name = ~camera_prefix
  0.type = std_msgs/String
  0.desc = Camera topics namespace ('image_rect' and 'camera_info' topics must be published in this namespace)

  1.name = ~tracker_prefix
  1.type = std_msgs/String
  1.desc = Namespace in which the tracker has been launched.
  1.default = tracker_mbt

  2.name = ~model_path
  2.type = std_msgs/String
  2.desc = Model location on the filesystem.
  2.default = $(find visp_tracker)/models

  3.name = ~model_name
  3.type = std_msgs/String
  3.desc = Model name. '''This parameter is mandatory when launching the client.'''
}
```

```clearsilver
name = viewer
desc = Monitoring tool.
param {
  0.name = ~tracker_prefix
  0.type = std_msgs/String
  0.desc = Namespace in which the tracker has been launched.
  0.default = /tracker_mbt

  1.name = ~image_transport
  1.type = string
  1.desc = [[image_transport]] plug-in to be used.
  1.default = raw
}
```

## Nodelets

This package provides both nodes and nodelet versions of the tracker,
client and viewer.

They are respectively named:

-   \`visp_tracker/Tracker\`
-   \`visp_tracker/TrackerClient\`
-   \`visp_tracker/TrackerViewer\`

\...and provide the same API than the equivalent nodes.

When the nodelet version is used, no-copy intraprocess publishing is
used. See the [nodelet](nodelet) documentation for more information.

An example launch file is also provided: ```
roslaunch visp_tracker tutorial-nodelet.launch
```

\'\'Note:\'\' even if a nodelet is available for the client and viewer,
one should avoid running them in the same process than the vision
pipeline to avoid crashing the whole pipeline if something goes wrong.

## Launch file example

Here is a launch file which starts the tracker and client.

{ }}}}

{ }}}}

## Report a bug

Use !GitHub to
[report a bug or submit an enhancement](https://github.com/lagadic/visp_tracker/issues).
