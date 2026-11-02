## Overview

Provides detections of faces in stereo camera data. The face detector
employs the OpenCV face detector (based on a cascade of Haar-like
features) to obtain an initial set of detections. It then prunes false
positives using stereo depth information. The depth information is used
to predict the real-world size of the detected face, which is then
preserved as a true face detection only if the size is realistic for a
human face. This removes the majority of false positives given by the
OpenCV detector.

In the two images below, all of the bounding boxes are detections from
the OpenCV frontal face detector. The blue detection does not have
sufficient depth information (due to low illumination) and hence will be
considered a false positive by the face_detector node. The red detection
has an unrealistic real-world size, and will be considered a false
positive. Only the green detections are returned as true face
detections.

![Raw images](doc/face2.png) ![Raw images](doc/face1.png)

## Node

### face_detector

The face_detector node can be used in two ways, continuously or as an
action. Continuous mode: detect faces in the entire image stream. Action
mode: an action is used to start face detection and the detector
processes images until it has found at least one face.

#### Action Result

- `face_positions`
  ([people_msgs/msg/PositionMeasurement](https://docs.ros.org/en/rolling/p/people_msgs/msg/PositionMeasurement.html)):
  A list of found faces.

#### Subscribed Topics

- `<camera>/left/<image>`
  ([sensor_msgs/msg/Image](https://docs.ros.org/en/rolling/p/sensor_msgs/msg/Image.html)):
  The image from the left camera in the stereo pair. Should be
  de-bayered and rectified. Can be color or grayscale.
- `<camera>/disparity`
  ([stereo_msgs/msg/DisparityImage](https://docs.ros.org/en/rolling/p/stereo_msgs/msg/DisparityImage.html)):
  The disparity image.
- `<camera>/left/camera_info`
  ([sensor_msgs/msg/CameraInfo](https://docs.ros.org/en/rolling/p/sensor_msgs/msg/CameraInfo.html)):
  The camera parameters from the left camera.
- `<camera>/right/camera_info`
  ([sensor_msgs/msg/CameraInfo](https://docs.ros.org/en/rolling/p/sensor_msgs/msg/CameraInfo.html)):
  The camera parameters from the right camera.
- `<camera>/rgb/<image>`
  ([sensor_msgs/msg/Image](https://docs.ros.org/en/rolling/p/sensor_msgs/msg/Image.html)):
  The image from the color camera. Should be de-bayered and rectified.
  Can be color or grayscale.
- `<camera>/depth_registered/<image>`
  ([sensor_msgs/msg/Image](https://docs.ros.org/en/rolling/p/sensor_msgs/msg/Image.html)):
  The registered depth image. 'image' should be image_rect.
- `<camera>/rgb/camera_info`
  ([sensor_msgs/msg/CameraInfo](https://docs.ros.org/en/rolling/p/sensor_msgs/msg/CameraInfo.html)):
  The camera parameters from the color camera.
- `<camera>/depth_registered/camera_info`
  ([sensor_msgs/msg/CameraInfo](https://docs.ros.org/en/rolling/p/sensor_msgs/msg/CameraInfo.html)):
  The camera parameters from the depth camera.

#### Published Topics

- `face_detector/people_tracker_measurements`
  ([people_msgs/msg/PositionMeasurement](https://docs.ros.org/en/rolling/p/people_msgs/msg/PositionMeasurement.html)):
  The 3D position of the center of the face. Fields are available for
  reliability and covariance measurements if desired. Axis of `pos`
  aligns to that of `fixed_frame` argument passed in the launch file.
- `face_detector/faces_cloud`
  ([sensor_msgs/msg/PointCloud](https://docs.ros.org/en/rolling/p/sensor_msgs/msg/PointCloud.html)):
  A point cloud of face centers, intended for visualization.

#### Parameters

- `~classifier_name` (`string`): A readable string for the classifier.
  Will be published with the result.
- `~classifier_filename` (`string`): Full path to the trained haar
  cascade. Provided classifiers are in opencv2. We recommend using the
  haar_frontalface_alt.xml
- `~classifier_reliability` (`double (0-1)`): Some notion of the
  classifier's reliability for use in a larger system.
- `~do_continuous` (`bool`): true=run continuously, false=wait for
  action call
- `~do_publish_faces_of_unknown_size` (`bool`): true = If depth info is
  not available, just make pos.x and pos.y in the resulting
  people_msgs/PositionMeasurement messaging the 2D image center of the
  face. false = Don't publish faces if stereo information isn't
  available.
- `~do_display` (`bool`): false = don't display anything, true =
  display detections in an OpenCV window.
- `~face_size_min_m` (`double`): The minimum width of a face, in meters.
  Defaults to 0.1m.
- `~face_size_max_m` (`double`): The maximum width of a face, in meters.
  Defaults to 0.5m.
- `~max_face_z_m` (`double`): The maximum distance of a face from the
  camera, in meters. (In the camera frame, depth is along the z-axis.)
  Defaults to 8.0m.
- `~face_separation_dist_m` (`double`): Only used for tracking. The
  maximum distance between two face detections before they are
  considered different faces. Defaults to 1.0m.
- `~use_rgbd` (`bool`): true = use data from an RGBD camera (Kinect),
  false = use stereo data
- `~approx_sync` (`bool`): true = use data from unsynchronized cameras
  (the Kinect or the stereo cameras in Gazebo), false = use data from
  synchronized cameras

## Example Usage

See `face_detector/launch/face_detector.<camera>.launch` to see how to
run the face detector continuously, or
`face_detector/launch/face_detector_action.<camera>.launch` to run it as
an action. `launch` files above are stored
[in the repository](https://github.com/wg-perception/people/tree/indigo-devel/face_detector/launch).

Possible pitfall may be the argument names (in
[face_detector.rgbd.launch](https://github.com/wg-perception/people/blob/9d99dbd8d9fa4124f270742eac2a5f12e829eeda/face_detector/launch/face_detector.rgbd.launch)
for example):



```
<arg name="camera" default="camera" />
  <arg name="depth_ns" default="depth_registered" />
  <arg name="image_topic" default="image_rect_color" />
  <arg name="depth_topic" default="image_rect_raw" />
  <arg name="fixed_frame" default="camera_rgb_optical_frame" />
```



`camera` and `depth_ns` together consists the namespace prefix, and
`\*_topic` makes the body of the topic to subscribe. In the example
above, you're looking for:

- /camera/rgb/image_rect_color
- /camera/depth_ns/image_rect_raw

See
[this answer](http://answers.ros.org/question/210751/face_detector-not-detecting-with-rgbd-camera/?answer=210752#post-id-210752)
for the name of the topics you need to correct.

### Config example with Xtion



```
<launch>
  <arg name="camera" default="camera" />
  <arg name="image_topic" default="image_raw" />
  <arg name="depth_topic" default="image_raw" />
  <arg name="fixed_frame" default="camera_rgb_optical_frame" />
  <arg name="depth_ns" default="depth_registered" />
:
</launch>
```



### Example with robots

No doubt `face_detector` works on the robots on simulator. Examples
below show how you can run this package using stereo camera on
[PR2](https://index.ros.org/p/pr2) and
[Turtlebot](https://index.ros.org/p/turtlebot). Additionally, using some
other useful packages, you can visualize face detection result on
[RViz](https://index.ros.org/p/rviz).

1\. Install some useful packages
([jsk_pr2_startup](https://index.ros.org/p/jsk_pr2_startup) that depends
on [jsk_rviz_plugins](https://index.ros.org/p/jsk_rviz_plugins), which
provides a feature to show the result of `face_detector` on `RViz`)
: 

```
apt-get install jsk_pr2_startup
```



2\. Run the robot's launch files:

For `PR2`: 

```
roslaunch pr2_gazebo pr2_empty_world.launch
roslaunch face_detector facedetector_rgb_pr2.launch  (*a)
```



For `Turtlebot`: 

```
roslaunch turtlebot_gazebo turtlebot_world.launch
roslaunch turtlebot_miscsample_cpp facedetector_rgb.launch (*b)
```



3\. Then run RViz using
[jsk_pr2_startup](https://index.ros.org/p/jsk_pr2_startup) package:


```
roslaunch jsk_pr2_startup rviz.launch
```



4\. (Simulation only) Add a `standing person` model on Gazebo; On
Gazebo, `Insert` -> `Standing person` then place him at certain
location.

5\. You may want to open `Image` plugin on `RViz` then specify
`/head_mount_kinect/rgb/image_raw` on `Image Topic` row, to make
sure that the robot is seeing the person's face.

6\. You may want to move the robot` so that the human is in the sight.

(\*a)\...Requires
[this pull request](https://github.com/wg-perception/people/pull/31)
merged and released.

(\*b)\...Requires (pull request TBA)

PR2:

![Gazebo and RViz img sample\|width=75%](https://cloud.githubusercontent.com/assets/1840401/10435680/482ca8aa-70d6-11e5-90b5-67c508c1674d.png)

Turtlebot:

![Tutelebot](doc/facedetect_turtlebot_gazebo_jsk-rviz_axis.png)
