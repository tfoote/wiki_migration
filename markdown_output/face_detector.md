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

![Raw images\|width=360 height=270](attachment:face2.png)
![Raw images\|width=360 height=270](attachment:face1.png)

## Node

```clearsilver
name = face_detector
desc = The face_detector node can be used in two ways, continuously or as an action. Continuous mode: detect faces in the entire image stream. Action mode: an action is used to start face detection and the detector processes images until it has found at least one face. 
sub {
  0.name = <camera>/left/<image>
  0.type = sensor_msgs/Image
  0.desc = The image from the left camera in the stereo pair. Should be de-bayered and rectified. Can be color or grayscale.
  1.name = <camera>/disparity
  1.type = stereo_msgs/DisparityImage
  1.desc = The disparity image.
  2.name = <camera>/left/camera_info
  2.type = sensor_msgs/CameraInfo
  2.desc = The camera parameters from the left camera.
  3.name = <camera>/right/camera_info
  3.type = sensor_msgs/CameraInfo
  3.desc = The camera parameters from the right camera.
  4.name = <camera>/rgb/<image>
  4.type = sensor_msgs/Image
  4.desc = The image from the color camera. Should be de-bayered and rectified. Can be color or grayscale.
  5.name = <camera>/depth_registered/<image>
  5.type = sensor_msgs/Image
  5.desc = The registered depth image. 'image' should be image_rect.
  6.name = <camera>/rgb/camera_info
  6.type = sensor_msgs/CameraInfo
  6.desc = The camera parameters from the color camera.
  7.name = <camera>/depth_registered/camera_info
  7.type = sensor_msgs/CameraInfo
  7.desc = The camera parameters from the depth camera.
}
pub {
  0.name = face_detector/people_tracker_measurements
  0.type = people_msgs/PositionMeasurement
  0.desc = The 3D position of the center of the face. Fields are available for reliability and covariance measurements if desired. Axis of `pos` aligns to that of `fixed_frame` argument passed in the launch file.
  1.name = face_detector/faces_cloud
  1.type = sensor_msgs/PointCloud
  1.desc = A point cloud of face centers, intended for visualization.
}
param {
  0.name = ~classifier_name
  0.type = string
  0.desc = A readable string for the classifier. Will be published with the result.
  1.name = ~classifier_filename
  1.type = string
  1.desc = Full path to the trained haar cascade. Provided classifiers are in opencv2. We recommend using the haar_frontalface_alt.xml
  2.name = ~classifier_reliability
  2.type = double (0-1)
  2.desc = Some notion of the classifier's reliability for use in a larger system.
  3.name = ~do_continuous
  3.type = bool
  3.desc = true=run continuously, false=wait for action call
  4.name = ~do_publish_faces_of_unknown_size
  4.type = bool 
  4.desc = true = If depth info is not available, just make pos.x and pos.y in the resulting people_msgs/PositionMeasurement messaging the 2D image center of the face. false = Don't publish faces if stereo information isn't available.
  5.name = ~do_display
  5.type = bool
  5.desc = false = don't display anything, true = display detections in an OpenCV window.
  6.name = ~face_size_min_m
  6.type = double
  6.desc = The minimum width of a face, in meters. Defaults to 0.1m.
  7.name = ~face_size_max_m
  7.type = double
  7.desc = The maximum width of a face, in meters. Defaults to 0.5m.
  8.name = ~max_face_z_m
  8.type = double
  8.desc = The maximum distance of a face from the camera, in meters. (In the camera frame, depth is along the z-axis.) Defaults to 8.0m.
  9.name = ~face_separation_dist_m
  9.type = double
  9.desc = Only used for tracking. The maximum distance between two face detections before they are considered different faces. Defaults to 1.0m.
  10.name = ~use_rgbd
  10.type = bool
  10.desc = true = use data from an RGBD camera (Kinect), false = use stereo data
  11.name = ~approx_sync
  11.type = bool
  11.desc = true = use data from unsynchronized cameras (the Kinect or the stereo cameras in Gazebo), false = use data from synchronized cameras
}
result {
  0.name = face_positions
  0.type = people_msgs/PositionMeasurement
  0.desc = A list of found faces.
}
```

## Example Usage

See `face_detector/launch/face_detector.<camera>.launch` to see how to
run the face detector continuously, or
`face_detector/launch/face_detector_action.<camera>.launch` to run it as
an action. \`launch\` files above are stored
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

\`camera\` and \`depth_ns\` together consists the namespace prefix, and
\`\*\_topic\` makes the body of the topic to subscribe. In the example
above, you\'re looking for:

-   /camera/rgb/image_rect_color
-   /camera/depth_ns/image_rect_raw

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

No doubt \`face_detector\` works on the robots on simulator. Examples
below show how you can run this package using stereo camera on
[PR2](pr2) and [Turtlebot](turtlebot). Additionally, using some other
useful packages, you can visualize face detection result on
[RViz](rviz).

1\. Install some useful packages ([jsk_pr2_startup](jsk_pr2_startup)
that depends on [jsk_rviz_plugins](jsk_rviz_plugins), which provides a
feature to show the result of \`face_detector\` on \`RViz\`) :
```
apt-get install jsk_pr2_startup
```

2\. Run the robot\'s launch files:

For \`PR2\`: ```
roslaunch pr2_gazebo pr2_empty_world.launch
roslaunch face_detector facedetector_rgb_pr2.launch  (*a)
```

For \`Turtlebot\`: ```
roslaunch turtlebot_gazebo turtlebot_world.launch
roslaunch turtlebot_miscsample_cpp facedetector_rgb.launch (*b)
```

3\. Then run RViz using [jsk_pr2_startup](jsk_pr2_startup) package:
```
roslaunch jsk_pr2_startup rviz.launch
```

4\. (Simulation only) Add a \`standing person\` model on Gazebo; On
Gazebo, \`Insert\` -\> \`Standing person\` then place him at certain
location.

5\. You may want to open \`Image\` plugin on \`RViz\` then specify
\`/head_mount_kinect/rgb/image_raw\` on \`Image Topic\` row, to make
sure that the robot is seeing the person\'s face.

6\. You may want to move the robot\` so that the human is in the sight.

(\*a)\...Requires
[this pull request](https://github.com/wg-perception/people/pull/31)
merged and released.

(\*b)\...Requires (pull request TBA)

PR2:

![Gazebo and RViz img sample\|width=75%](https://cloud.githubusercontent.com/assets/1840401/10435680/482ca8aa-70d6-11e5-90b5-67c508c1674d.png)

Turtlebot:

![Tutelebot\|width=\"85%\"](attachment:facedetect_turtlebot_gazebo_jsk-rviz_axis.png)
