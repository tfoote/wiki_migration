/!\\ camera_pose has moved to github:
<https://github.com/ros-perception/camera_pose>

## Stability

[camera_pose_toolkits](camera_pose_toolkits) is still unreviewed and
unstable.

## Overview

The package provides assistive tools for
[camera_pose_calibration](camera_pose_calibration). It gives the users a
much easier way to take advantage of the camera_pose_calibration
pipeline.

### Package Components

**transform_finder **

This is the most important component inside this package. Its function
can be illustrated using the following figure:

![\|height="442px",width="573"](attachment:transform_finder.JPG)

Say, you have a robotic system that has already been calibrated, i.e.
the tf tree of the robot is known. The tf tree has a camera frame (we
call it the urdf cam frame). Now you rigidly attach a new camera to one
of the robot links. You want to add the new camera frame to the tf tree.
In other words, you want to find out the 'question mark'
transformation in the figure.

To do that, the **transform_finder** module will first utilize the
camera_pose_calibration's results to find out the transformation
between the new cam frame and the urdf cam frame. Then it will look up
tf to get the transformation between the urdf cam frame and the mounting
frame (since both frames are already in the tf tree.). After that,
**transform_finder** will automatically figure out the fixed
transformation between the new camera frame and its mounting frame.

Here are two examples setups on PR2:

In the first one: the left wide stereo camera is chosen as the urdf
camera (from the many cameras on the PR2 head); the Kinect is the new
camera that we want in, and it is mounted on the left side plate. There
are multiple joints between the stereo camera and the side plate, but
it's OK, since they are in the same tf tree. The transform_finder will
output the static transformation between the kinect rgb frame and the
side plate frame. Please see
[this tutorial](http://www.ros.org/wiki/camera_pose_toolkits/Tutorials/Add_Kinect_to_PR2)
for more details.

  -- -------------------------------------------------------------------- --
     side-plate mounted                                                   
     ![\|height="512px",width="682"](attachment:pr2-side-mount.jpg)   
  -- -------------------------------------------------------------------- --

In the second example, the mounting frame and urdf cam frame happen to
be the same. The transform_finder module can still handle this
situation. Actually, this situation is simpler, since tf information is
not needed.

  -- -------------------------------------------------------------------- --
     head mounted                                                         
     ![\|height="512px",width="682"](attachment:pr2-head-mount.jpg)   
  -- -------------------------------------------------------------------- --

**urdf_updater**

This module converts transform_finder's output into
[XML Robot Description Format (URDF)](http://www.ros.org/wiki/urdf/XML)
snippet and then inserts it into your robot description file.

**static_transform_tf_broadcaster**

This module collects transform_finder's outputs and publishes them to
tf. transform_finder can send transforms between different frame pairs.
The broadcaster keeps track of the frame pairs and only save the most
recent transform for each frame pair. Right before this module
terminates, it saves all the transform messages into a bag.

**transform_message_saver**

Every time transform_finder publishes a message to
'camera_pose_static_transform_update' topic, this module saves it to a
bag file. Upon start-up, if this node detects that there are previously
saved messages in the bag, it will first try to re-publish them to tf.
Since there is no 'append' operation for rosbag, this node has to keep
an internal list of frame pairs (it only saves the most updated
transform message for each frame pair) and then overwrite the rosbag
file with the updated list every time. This module saves the message to
disk on the fly, so if the program crashes somehow, you will not lose
your previous calibration work.

There is a similar node in camera_pose_calibration package. That one
works with any topic type, but it can only saves the most recent message
for each topic; this module only works with the
'camera_pose_static_transform_update' topic (of type
geometry_msgs::TransformStamped), but it can save multiple messages for
this topic.

**transform_replay**

This module extracts the transform messages from previously generated
bag (either by tf broadcaster or transform_message_saver) and
re-publishes them to tf. This allows users to easily reuse their
calibration results at a later time. All they need to do is to type in
the following line:



```
rosrun camera_pose_toolkits transform_playback_node [your_bag_name]
```



And all the transform messages in the bag are published to tf.

**camera_dispatcher & dispatcher_gui**

These two modules together allow the user to dynamically switch the
camera frames they want to calibrate (without restarting the
transform_finder module). User can select the name space of the camera
to be calibrated from a drop-down list. This is particularly helpful
when you need to calibrate the poses of multiple cameras.

### A Simplified Workflow

![\|height="1077px",width="696"](attachment:components2.jpg)

In the workflow chart: black circles are nodes, red rectangles are
topics, the black solid arrows indicate the message flows between nodes
and topics; green dotted arrows indicate service calls; clouds are
launch files, or a group of nodes; dashed arrows indicate file IO
operations (read/write). If the color of the arrow is blue, it means the
flow is a one time deal.

Note 1: this chart shows all the nodes in camera_pose_toolkits package,
but you don't have to use all of them at the same time. You can use
launch files to assemble them based on your need. ( But your launch file
should always include transform_finder node.)

Note 2: the cal_optimzer node is a component of the
[camera_pose_calibration](camera_pose_calibration) package.

## Getting Started

### Requirements

-   You have two cameras. One is the urdf camera (whose frame has
    already been calibrated relative to the other frames in your robot).
    Another is a new camera, rigidly attached to one link of your robot.
    Both cameras publishes image_rect and camera_info messages under
    their own namespace.
-   The transformation between the urdf camera frame and the new
    camera's mounting frame is published to tf. (**Not needed** *if the
    mounting frame happens to be the urdf camera frame*)
-   All the requirements mentioned in the
    [camera_pose_calibration](camera_pose_calibration) page.

### Operation

Launching camera_pose_urdf_updater with arguments could look like this:



```
roslaunch camera_pose_toolkits urdf_updater.launch new_cam_ns:=MS_Kinect/rgb urdf_cam_ns:=/wide_stereo/left mounting_frame:=torso_lift_link urdf_input_file:=/etc/ros/diamondback/urdf/robot.xml urdf_output_file:=/u/yiping/new.xml checker_rows:=4 checker_cols:=5 checker_size:=0.0249 headless:=1
```

 The **urdf_updater.launch** includes
**calibrate_2_camera.launch**, which is located in the
**launch_extrinsics** directory in the camera_pose_calibration package
path.

The arguments:

-   **new_cam_ns**: the name space of the newly added camera.
-   **urdf_cam_ns**: the name space of the calibrated camera (a.k.a.
    urdf camera).

```{=html}
<!-- -->
```
-   **checker_rows**: the number of checker corners horizontally.
-   **checker_cols**: the number of checker corners vertically.
-   **checker_size**: the size of one checker (in meters).
-   **urdf_input_file**: original urdf file (no information of the new
    camera frame).
-   **urdf_output_file**: updated urdf file (with information of the new
    camera frame).
-   **mounting_frame**: the id of the frame on which the new camera is
    mounted
-   **headless**: suppress the aggregated image view. (as you can see,
    some of the arguments are prepared for *calibrate_2_camera.launch*)

As soon as you see the "successfully ran optimization" image (i.e.
calibration finished), transform_finder will output an updated
transformation between the new camera and its mounting frame.

By default, the cal_optimizer doesn't monitor the transformation
between the urdf camera frame and the mounting frame, however,if during
the calibration, the **urdf camera frame** moves relative to the
mounting frame, you would want the cal_optimizer node to know it and
reset the cache for the previous measurements before running the
optimization again.

To activate cal_optimizer's tf monitoring and conditional cache reset
function, you need to set up a parameter
'optimizer_conditional_resetter_enable' on the parameter server. In
most cases, if the urdf camera frame and the mounting frame are
different frames, you will always want to include the following line



```
<param name="optimizer_conditional_resetter_enable" value ="True" />
```



in your launch file.

Usually, to get better calibration results, you can do 3-4 checkerboard
measurements with one urdf camera pose and then change the urdf camera
pose (relative to the mounting frame) and so the checkerboard
measurements again. You can choose 3-5 different urdf camera poses.

If you use urdf_writer node, the urdf description of the new camera
frame will be inserted right before the </robot> tag. However, if the
designated input urdf file is not found in the directory, urdf_writer
will generate an empty file with the same name and then put the urdf
snippet in it, and you will receive a warning complaining about missing
parent.
