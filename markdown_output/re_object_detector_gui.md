## What does re_object_detector_gui do?

[re_object_detector_gui](re_object_detector_gui) aims to be a simple
front end for downloading object models from the !RoboEarth database and
to feed these into different object detection algorithms.

See the tutorial
[roboearth_stack/Tutorials/Using recorded models for object detection](roboearth_stack/Tutorials/Using recorded models for object detection)
for a step-by-step approach.

It is written specifically for detecting models created with the
[re_object_recorder](re_object_recorder). It allows to use either the
[re_vision](re_vision) or
[re_kinect_object_detector](re_kinect_object_detector) object detection
service.

## Subscribed Topics

`/camera/rgb/image_color`
([sensor_msgs/msg/Image](https://docs.ros.org/en/rolling/p/sensor_msgs/msg/Image.html))
Color image from the Kinect camera

`/re_kinect/detection_results`
([re_kinect_object_detector/msg/DetectionResult](https://docs.ros.org/en/rolling/p/re_kinect_object_detector/msg/DetectionResult.html))
Detection results from the re_kinect object detection node

## Published Topics

`/re_vslam/new_model`
([std_msgs/msg/String](https://docs.ros.org/en/rolling/p/std_msgs/msg/String.html))
Path to new models for re_vision added or downloaded by the user

`/re_kinect/model_path`
([std_msgs/msg/String](https://docs.ros.org/en/rolling/p/std_msgs/msg/String.html))
Path to new models for the re_kinect node added or downloaded by the
user
