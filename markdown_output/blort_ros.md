![](attachment:pal_logo.png) ![](attachment:elte_logo.jpg)

![](attachment:acin-logo.png) ![](attachment:TU-Logo.png)

## Overview

BLORT - The Blocks World Robotic Vision Toolbox

The vision and robotics communities have developed a large number of
increasingly successful methods for tracking, recognizing and online
learning of objects, all of which have their particular strengths and
weaknesses. A researcher aiming to provide a robot with the ability to
handle objects will typically have to pick amongst these and engineer a
system that works for her particular setting. The toolbox is aimed at
robotics research and as such we have in mind objects typically of
interest for robotic manipulation scenarios, e.g. mugs, boxes and
packaging of various sorts. We are not aiming to cover articulated
objects (such as walking humans), highly irregular objects (such as
potted plants) or deformable objects (such as cables). The system does
not require specialized hardware and simply uses a single camera
allowing usage on about any robot. The toolbox integrates state-of-the
art methods for detection and learning of novel objects, and recognition
and tracking of learned models.

A typical situation where one would need the exact pose of an object is
when a robot needs to manipulate an object. BLORT doesn\'t need any
markers but in exchange it has to be trained for the specific object to
detect and estimate the pose of. The speed of the system is defined by
the two modules. The feature-based detector is sufficiently slower than
the edge-based tracker. The detector module typically works at 3Hz and
depending on the situation it typically needs two seconds to initialize
the tracker. The tracker module can achieve a 30-70Hz speed depending on
the hardware.

![](attachment:reem_at_desk.jpg)

An example application of pre-grasping with the help of visual servoing
techniques. BLORT is providing object detection and pose estimation for
the grasping pipeline of the REEM robot.

## Install

Execute

```
sudo apt-get install ros-hydro-perception-blort
``` A commonly used package with blort_ros is
pal_vision_segmentation which you can also get from the ROS repositories
by executing

```
sudo apt-get install ros-hydro-pal-vision-segmentation
```

## Techniques

The system works with a CAD model of the object provided. The current
implementation of the BLORT detector module uses SIFT feature
descriptors to provide an approximate estimation of the object\'s pose
for the tracker module which will track the object using edge-based
methods.

More information: \[**Mörwald, T.; Prankl, J.; Richtsfeld, A.; Zillich,
M.; Vincze, M. BLORT - The Blocks World Robotic Vision Toolbox Best
Practice in 3D Perception and Modeling for Mobile Manipulation (in
conjunction with ICRA 2010), 2010.**\] or you can also visit the
[BLORT Homepage](http://www.acin.tuwien.ac.at/?id=290).

## Usage

Please see the tutorials on the right in order to learn about how to use
and tune BLORT to your needs.

## ROS API

```clearsilver
name=blort_learnsifts
node {
  0.name=learnsifts
  0.desc=Training node. See the [[http://www.ros.org/wiki/blort_ros/Tutorials/Training|Training tutorials]] for further info.
}
sub {
  0.name = blort_image
  0.type = sensor_msgs/Image
  0.desc = Input image from camera.
  1.name = blort_camera_info
  1.type = sensor_msgs/CameraInfo
  1.desc = Camera parameters associated with the input image. '''If you input a rectified image, do provide the according camera_info as well.'''
}
``` ```clearsilver
name=blort_tracker
node {
  0.name=gltracker_node
  0.desc=Tracker node. See the [[http://www.ros.org/wiki/blort_ros/Tutorials/TrackAndDetect|Tracker/detector tutorials]] tutorials for further info.
}
sub {
  0.name = blort_image
  0.type = sensor_msgs/Image
  0.desc = Input image from camera.
  1.name = blort_camera_info
  1.type = sensor_msgs/CameraInfo
  1.desc = Camera parameters '''associated''' with the input image. '''If you input a rectified image, do provide a modified camera_info as well.'''
}
srv {
  0.name = tracker_control
  0.type = blort_ros/TrackerCommand
  0.desc = A service which uses the same things as the learnsifts button commands but mapped to integers and through a service interface.
  1.name = singleshot_service
  1.type = blort_ros/EstimatePose
  1.desc = This service can be called when BLORT is launched in '''singleshot''' mode. For more on this topic, see the [[http://www.ros.org/wiki/blort_ros/Tutorials/LaunchModes|Launch modes tutorial]].
}
srv_called {
  0.name = blort_detector/pose_service
  0.type = blort_ros/RecoveryCall
  0.desc = The tracker calles the detector to get it's next initial pose to start tracking.
  1.name = blort_detector/set_camera_info
  1.type = blort_ros/SetCameraInfo
  1.desc = A service which transfers a single CameraInfo instance to the blort_detector node.
}
param {
  0.name = ~launch_mode
  0.type = string
  0.desc = Set the mode to run BLORT in. It can be "tracking" or "singleshot". See the tutorial explaining the [[http://www.ros.org/wiki/blort_ros/Tutorials/LaunchModes|launch modes]].
  0.default = "tracking"
}
```
```clearsilver
name=blort_detector
node {
  0.name=gldetector_node
  0.desc=Detector node. See the [[http://www.ros.org/wiki/blort_ros/Tutorials/TrackAndDetect|Tracker/detector tutorials]]  for further info.
}
sub {
  0.name = camera_info
  0.type = sensor_msgs/CameraInfo
  0.desc = Camera parameters associated with the input image. '''If you input a rectified image, do provide a modified camera_info as well.''' The camerainfo is only used when launched in tracking mode.
}
srv {
  0.name = pose_service
  0.type = blort_ros/RecoveryCall
  0.desc = A service which triggers the detector to take over and try to return a pose estimate.
}
srv {
  0.name = set_camera_info
  0.type = blort_ros/SetCameraInfo
  0.desc = A service which triggers the detector to take over and try to return a pose estimate.
}
param {
  0.name = ~nn_match_threshold
  0.type = double
  0.desc = See [[http://www.ros.org/wiki/blort_ros/Tutorials/Tune#Detector_tuning|Detector tuning]].
  0.default = 0.55
  1.name = ~ransac_n_points_to_match
  1.type = int
  1.desc = See [[http://www.ros.org/wiki/blort_ros/Tutorials/Tune#Detector_tuning|Detector tuning]].
  1.default = 4
}
``` ```clearsilver
name=pose2Tf
node {
  0.name=pose2Tf
  0.desc=This node converts geometry_msgs::Pose messages to tf transforms and publishes them. Has two command line arguments for parent_name and child_name, feel free to remap "pose".
}
sub {
  0.name = pose
  0.type = geometry_msgs/Pose
  0.desc = Pose message published by someone.
}
prov_tf {
  0.from = parent_name
  0.to   = child_name
  0.desc = Transformation defined by the pose message compiled to tf transformation.
}
```
```clearsilver
name=pose2Tf_repeat
node {
  0.name=pose2Tf_repeat
  0.desc=This node converts geometry_msgs::Pose messages to tf transforms and publishes them. Has two command line arguments for parent_name and child_name, feel free to remap "pose". '''It does the same as pose2Tf with the difference that it will keep publishing the last pose forever.'''
}
sub {
  0.name = pose
  0.type = geometry_msgs/Pose
  0.desc = Pose message published by someone.
}
prov_tf {
  0.from = parent_name
  0.to   = child_name
  0.desc = Transformation defined by the pose message compiled to tf transformation.
}
```
