## Depreciated

Please note that this package is no longer being maintained. The same
functionality can be found in the
[rbx1_vision](https://github.com/pirobot/rbx1/tree/indigo-devel/rbx1_vision)
package in the
[ROS By Example repository](https://github.com/pirobot/rbx1) which is
actively maintained and currently available through ROS Indigo.

## Overview

The pi_face_tracker ROS package uses OpenCV's Haar face detector
together with Good Features to Track and the Lucas-Kanade Optical Flow
tracker to perform face tracking in a live video stream or recorded
video file. Works best with an RGB-D camera such as the Kinect so that
depth information can be used to reduce the number of false positive
face detections.

[Youtube](https://www.youtube.com/watch?v=Yw_zkLaZNsQ)

In the video above from the
[Honda/UCSD Video Database](http://vision.ucsd.edu/~leekc/HondaUCSDVideoDatabase/HondaUCSD.html),
the left image uses only the Haar face detector while the right image
uses the detector only on the first frame to get the initial face
region, then relies on Good Features to Track and Optical Flow to follow
the face through the rest of the video. Notice that the right video
never loses the face and runs about three times faster (CPS = "cycles
per second").

## How It Works

When running in automatic face detection mode, the video is scanned
using three of the OpenCV Haar face detectors, two frontal cascades and
one profile cascade (see
[HaarDetectObjects](http://opencv.willowgarage.com/documentation/python/objdetect_cascade_classification.html?highlight=haardetectobjects#HaarDetectObjects)).
Once a face is detected, the
[GoodFeaturesToTrack](http://opencv.willowgarage.com/documentation/python/imgproc_feature_detection.html?highlight=goodfeaturestotrack#GoodFeaturesToTrack)
filter is run over the face region to extract a collection of points to
track. These points are then fed to the Lucas-Kanade Optical Flow
Tracker
[CalcOpticalFlowPyrLK](http://opencv.willowgarage.com/documentation/python/video_motion_analysis_and_object_tracking.html?highlight=calcopticalflowpyrlk#CalcOpticalFlowPyrLK)
which follows the points from one frame to the next.

Over time, feature points will be lost due to occlusions or picked up
from the background. Therefore, two additional methods are run to
maintain the integrity of the tracked feature cluster. First, feature
points are pruned (dropped) if they lie too far outside the current
cluster in the x-y camera plane (see parameter `std_err_xy`) or in
depth (see `use_depth_for_tracking`). At the same time, new feature
points are added by expanding the current cluster ROI by a small amount
(10%) and running
[GoodFeaturesToTrack](http://opencv.willowgarage.com/documentation/python/imgproc_feature_detection.html?highlight=goodfeaturestotrack#GoodFeaturesToTrack)
over the expanded region. If the feature cluster shrinks below a
specified minimum number of points (see `abs_min_features`), the
algorithm returns to the Haar face detector and scans the video to
relocate the face.

When not using automatic face detection, the only difference from above
is that the original region to track is defined by the user by dragging
a rectangle over a part of the image.

## Installation Instructions

First install Eric Perko's uvc_cam package if you don't have it
already:



```
$ git clone https://github.com/ericperko/uvc_cam.git
$ rosdep install uvc_cam
$ rosmake uvc_cam
```

 For rosdep and rosmake to work, new packages
need to be on your ROS_PACKAGE_PATH. So clone them into your sandbox, or
use rosws (do not forget to source setup.sh), or change your
ROS_PACKAGE_PATH manually.

Next, install the pi_vision stack as follows:



```
$ svn co http://pi-robot-ros-pkg.googlecode.com/svn/trunk/pi_vision
$ rosmake pi_vision
```



## How To Use

**Note:** Best results are obtained at video resolutions of 640x480 or
higher. Lower resolutions will work OK if the face is not too far away
from the camera.

### Keyboard Commands Once Tracking Has Started

First make sure the video window is in the foreground (click on the
title bar). Then type one of the following characters:

-   'q' - quit
-   'c' - clear all current features and re-detect face
-   't' - toggle text markers off/on
-   'f' - toggle features markers off/on
-   'n' - toggle night mode on/off (displays markers only)
-   'a' - toggle auto face tracking on/off

### Tracking with the Kinect RGB-D Camera



```
$ roslaunch ros2opencv openni_node.launch
```



Then launch the Kinect face tracker launch file:



```
$ roslaunch pi_face_tracker face_tracker_kinect.launch
```



### Tracking with a UVC-Compatible Webcam

If you have only one webcam attached to your computer and it is device
/dev/video0, then simply launch: 

```
$ roslaunch ros2opencv uvc_cam.launch
```



To connect to a different device, e.g. /dev/video1, use the following
form: 

```
$ roslaunch ros2opencv uvc_cam.launch device:=/dev/video1
```



Then launch the UVC face tracker launch file:



```
$ roslaunch pi_face_tracker face_tracker_uvc_cam.launch
```



### Tracking with an AVI File



```
$ roslaunch pi_face_tracker face_tracker_uvc_cam.launch
```



Then start the video file:



```
$ roslaunch ros2opencv avi2ros.launch input:=/path/to/avi/file
```



#### Special Keyboard Commands for AVI Files

First make sure the video window is in the foreground (click on the
title bar):

-   space - pause/resume video
-   r - restart video from beginning

### Tracking a Non-Face Video Patch

To track objects other than faces, first turn off face tracking either
by typing the letter 'a' in the image window or by setting the
`auto_face_tracking` parameter to `False` in the appropriate launch
file and re-running the launch file. Then use your mouse to draw a box
around the object you want to track. You can select a different patch at
any time.

## Nodes



```clearsilver
node.0 {
name = pi_face_tracker.py
desc = A ROS node for face tracking using the OpenCV face detector together with Good Features to Track and the Lucas-Kanade Optical Flow tracker.
}

sub {
  0.name = ~input_rgb_image
  0.type = sensor_msgs/Image
  0.desc = The ROS RGB image topic on which to perform face detection and tracking
  1.name = ~input_depth_image
  1.type = sensor_msgs/Image
  1.desc = The ROS image topic containing depth information
}
pub {
  0.name = /roi
  0.type = sensor_msgs/RegionOfInterest
  0.desc = The region of interest around the tracked face
  1.name = /target_point
  1.type = geometry_msgs/PointStamped
  1.desc = The PointStamped centroid of the tracked cluster (when using a 3D camera)
}
param {
  1.name = ~auto_face_tracking
  1.type = boolean
  1.desc = Run face tracking automatically at startup
  1.default = True
  2.name = ~use_haar_only
  2.type = boolean
  2.desc = Use Haar face detection only.  (Does not use Good Features or Optical Flow)
  2.default = False
  3.name = ~use_depth_for_detection
  3.type = boolean
  3.desc = Use depth info to reduce false positive face detections.
  3.default = True
  4.name = ~use_depth_for_tracking
  4.type = boolean
  4.desc = Use depth to prune features that are outside the main cluster.
  4.default = False
  5.name = ~auto_min_features
  5.type = boolean
  5.desc = Use the number of features from the first detection to monitor addition or pruning of additional features.
  5.default = True
  6.name = ~min_features
  6.type = int
  6.desc = If auto_min_features is False, use this number.
  6.default = 50
  7.name = ~abs_min_features
  7.type = int
  7.desc = If auto_min_features is False, and number of features falls below this number, rescan the image with the Haar detector to re-detect the face region.
  7.default = 6
  8.name = ~good_feature_distance
  8.type = int
  8.desc = minimum pixel distance between features for the Good Features to Track algorithm
  8.default = 5
  9.name = ~add_feature_distance
  9.type = int
  9.desc = minimum pixel distance between features when adding new features after initial face detection
  9.default = 10
  10.name = ~std_err_xy
  10.type = float
  10.desc = How far (standard error) must a feature deviate from the cluster mean in the x-y camera plane before we drop it.
  10.default = 2.5
  10a.name = ~pct_err_z
  10a.type = float
  10a.desc = How far (percent) must a feature deviate from the cluster mean in the depth (z) direction before we drop it.
  10a.default = 0.42
  11.name = ~max_mse
  11.type = float
  11.desc = Maximum mean squared error of the feature cluster before we start over again with a new Haar detection.
  11.default = 100000
  12.name = ~show_text
  12.type = str
  12.desc = Show the text messages on the image by default.  (Can be toggled later with the "t" command.)
  12.default = True
  13.name = ~show_features
  13.type = str
  13.desc = Show the feature points on the image by default.  (Can be toggled later with the "f" command.)
  13.default = True
  14.name = ~max_face_size
  14.type = float
  14.desc = Maximum size of face in meters we will accept during initial detection.
  14.default = 0.28
  14a.name = ~expand_roi
  14a.type = float
  14a.desc = Amount to multiply the ROI around the current tracked cluster when adding new points.
  14a.default = 1.02
  15.name = ~fov_width
  15.type = float
  15.desc = Width in radians of camera's field of view. (Default is for the Kinect.)
  15.default = 1.094
  16.name = ~fov_height
  16.type = float
  16.desc = Height in radians of camera's field of view. (Default is for the Kinect.)
  16.default = 1.094
  17.name = ~flip_image
  17.type = boolean
  17.desc = Flip the image 180 vertically (some laptop cameras are upside down)
  17.default = False
  18.name = ~feature_type
  18.type = int
  18.desc = What type of feature to track: 0 = Good Features, 1 = SURF
  18.default = 0
}
srv {
  0.name = ~key_command
  0.type = pi_face_tracker/KeyCommand
  0.desc = Send a std_msgs/String command such as 'c' to clear the current features

  1.name = ~set_roi
  1.type = pi_face_tracker/SetROI
  1.desc = Set the ROI to track using message type sensor_msgs/RegionOfInterest.
}
```


