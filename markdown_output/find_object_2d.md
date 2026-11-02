## Overview

Simple Qt interface to try OpenCV implementations of SIFT, SURF, FAST,
BRIEF and other feature detectors and descriptors. Using a webcam,
objects can be detected and published on a ROS topic with ID and
position (pixels in the image). This package is a ROS integration of the
[Find-Object](http://introlab.github.io/find-object) application.

![this\|width=100%](https://raw.githubusercontent.com/wiki/introlab/find-object/doc/tutorial1/13.png)

### Citing



```
@misc{labbe11findobject,
   Author = {{Labb\'{e}, M.}},
   Howpublished = {\url{http://introlab.github.io/find-object}},
   Note = {accessed YYYY-MM-DD},
   Title = {{Find-Object}},
   Year = 2011
}
```



## Quick start



```
$ roscore &
 # Launch your preferred usb camera driver
 $ rosrun uvc_camera uvc_camera_node &
 $ rosrun find_object_2d find_object_2d image:=image_raw
```

 Visit
[Find-Object on GitHub](http://introlab.github.io/find-object) for some
tutorials.

## Description

- Subscribe to an image topic **/image**
  ([sensor_msgs/Image](http://docs.ros.org/api/sensor_msgs/html/msg/Image.html)
  )
- **Publish detected objects** (with **position**, **rotation**,
  **scale** and **shear**) as topic "objects":
  

```
$ rosrun find_object_2d print_objects_detected
  (...)
  ---
  Object 6 detected at (271.389282,138.113373)
  Object 7 detected at (115.537971,151.215271)
  ---
  Object 6 detected at (271.389862,138.345398)
  Object 7 detected at (115.422760,163.439835)
  (...)
```


- Note that parameter **Homography/homographyComputed** must be true
  (default true) in order to publish the topic.
- Parameter **General/mirrorView** would be false in order to visualize
  correctly the homography values returned.
- Take a look at the sample launch file
  [find_object_2d.launch](https://github.com/introlab/find-object/blob/master/launch/ros1/find_object_2d.launch)
  to know how to start the node without the GUI and with pre-loaded
  objects (from previously saved objects using the gui File->"save
  objects").

## 3D position of the objects

When using Kinect-like sensors, 3D position of the objects can be
computed in Find-Object ros-pkg.

![this\|width=100%](https://raw.githubusercontent.com/wiki/introlab/find-object/doc/ros_find_object_3d.png)



```
$ roslaunch openni_launch openni.launch depth_registration:=true
$ roslaunch find_object_2d find_object_3d.launch
$ rosrun rviz rviz  (for visualisation purpose: set "fixed_frame" to "/camera_link" and add TF display)
```

 Kinect v2 example (you will need
[iai_kinect2](https://github.com/code-iai/iai_kinect2) package and
[find_object_3d_kinect2.launch](https://github.com/introlab/find-object/blob/master/launch/ros1/find_object_3d_kinect2.launch)):


```
$ roslaunch kinect2_bridge kinect2_bridge.launch publish_tf:=true
$ roslaunch find_object_2d find_object_3d_kinect2.launch
```



- Take a look at the sample launch file
  [find_object_3d.launch](https://github.com/introlab/find-object/blob/master/launch/ros1/find_object_3d.launch)
  to know how to start 3D mode. Kinect-like sensors required! ROS
  parameter **subscribe_depth** must be also set to **true**.
  Subscriptions:
- /rgb/image_rect_color
  ([sensor_msgs/Image](http://docs.ros.org/api/sensor_msgs/html/msg/Image.html)
  )
- /depth_registered/image_raw
  ([sensor_msgs/Image](http://docs.ros.org/api/sensor_msgs/html/msg/Image.html)
  )
- /depth_registered/camera_info
  ([sensor_msgs/CameraInfo](http://docs.ros.org/api/sensor_msgs/html/msg/CameraInfo.html)
  )
- Position of the objects are published over TF (center of the object
  with rotation). You can set ROS parameter **object_prefix** to change
  the prefix used on TF (default is "object" which gives "/object_1"
  and "/object_2" for objects 1 and 2 respectively).
- If you are on a robot, you may want to have the pose of the objects in
  the **/map** frame. Take a look at this
  [example](https://github.com/introlab/find-object/blob/master/src/ros1/tf_example_node.cpp).
- Example on a robot:
  [Youtube](https://www.youtube.com/watch?v=o1GSQanY-Do)

## Nodes

### find_object_2d

#### Subscribed Topics

- `image`
  ([sensor_msgs/msg/Image](https://docs.ros.org/en/rolling/p/sensor_msgs/msg/Image.html)):
  RGB/Mono image. Used only if `subscribe_depth` is false.
- `rgb/image_rect_color`
  ([sensor_msgs/msg/Image](https://docs.ros.org/en/rolling/p/sensor_msgs/msg/Image.html)):
  RGB/Mono image. Required if `subscribe_depth` is true.
- `rgb/camera_info`
  ([sensor_msgs/msg/CameraInfo](https://docs.ros.org/en/rolling/p/sensor_msgs/msg/CameraInfo.html)):
  RGB camera metadata. Required if `subscribe_depth` is true.
- `registered_depth/image_raw`
  ([sensor_msgs/msg/Image](https://docs.ros.org/en/rolling/p/sensor_msgs/msg/Image.html)):
  Registered depth image. Required if `subscribe_depth` is true.

#### Published Topics

- `objects`
  ([std_msgs/msg/Float32MultiArray](https://docs.ros.org/en/rolling/p/std_msgs/msg/Float32MultiArray.html)):
  Objects detected formatted as \[objectId1, objectWidth, objectHeight,
  h11, h12, h13, h21, h22, h23, h31, h32, h33, objectId2\...\] where h##
  is a 3x3 homography matrix (h31 = dx and h32 = dy, see QTransform).
  Example handling the message (source
  [here](https://github.com/introlab/find-object/blob/master/src/ros/print_objects_detected_node.cpp))
- `objectsStamped`
  ([find_object_2d/msg/ObjectsStamped](https://docs.ros.org/en/rolling/p/find_object_2d/msg/ObjectsStamped.html)):
  Objects detected with stamp (useful to sync with corresponding TF).

#### Parameters

- `~subscribe_depth` (`bool`, default: `"true"`): Subscribe to depth
  image. [tf](https://index.ros.org/p/tf) will be published for each
  object detected (if the depth values are valid inside the object's
  region of the color image).
- `~gui` (`bool`, default: `"true"`): Launch the GUI
- `~objects_path` (`string`, default: `""`): Path to folder
  containing objects to detect.
- `~session_path` (`string`, default: `""`): Path to a session file
  to load. `objects_path` ignored if set.
- `~settings_path` (`string`, default: `""`): Path to settings file
  (\*.ini).
- `~object_prefix` (`string`, default: `"object"`): Object's prefix
  for [tf](https://index.ros.org/p/tf).
