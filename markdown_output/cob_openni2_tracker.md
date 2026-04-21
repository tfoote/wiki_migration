## Introduction

The cob_openni2_tracker package provides software for detecting and
tracking people using Kinect camera data. It also can be integrated in
rviz to visualize the camera frames and users' skeletons. The users can
be detected and tracked only in the current field of view of the camera.
This software is based on the OpenNI2 libraries and NiTE2 interfaces.

The OpenNI2 libraries are used to provide an access to active devices
and their related functions (e.g. reading the direct source of data from
the sensor, composing individual frames and providing information about
the video streams). The recording of camera data is specified as a
physical device event, which is set and opened in the body_tracker node
by Device::open() function. Once the device is opened, the data will be
obtained directly from it as a video stream. In order to read the camera
depth data and pass it directly to a currently opened device a simple
video stream object will be created. The extracted depth data is
represented as a two dimensional array of pixel values and is
encapsulated in one single frame object. This frame object provides
information about data size, width and height of frame in pixels and
timestamp of the active sensor.

The NiTE2 interfaces are used to start a body tracker process and
compose a user map (of detected or tracked people) out of a current
segmented scene. Each map member describes a single user (while detected
or tracked, visible or lost), assigns them a specific user id, stores
user segmentation data and provides such functions as skeleton tracking
and joint location. Once the user tracking has started, skeleton data
will be available for the visualization processes and wrapped in a
single skeleton message (see cob_perception_common
`cob_perception_msgs/Skeleton.h`). All actively tracked users
(Skeletons) are stored at lifetime in an array of people (see
cob_perception_common `cob_perception_msgs/People.h`) and will be
published on the `/body_tracker/people` topic.

## Quick Start

### OpenNI2

Please install the OpenNI2 libraries. You don't need to start the
Openni2 driver. It will be launched in camera_openni2.launch file
automatically.

### NiTE2

The required packages for NiTE2 will be installed automatically on your
computer (via cob_people_perception/libnite2) . If you already posses
the packages for NiTE2 libraries or want to check the installation path,
please consult the CMakeLists.txt file of the cob_openni2_tracker
package.

### Launch

To use the body tracker function to detect and track people clone the
repository and required dependencies to your catkin environment and
build it according to the instructions.

If you just need the tracker without any topics of the camera driver
(image, point cloud), simply start the launch file with the
standalone_without_camera_driver option:



```
roslaunch cob_openni2_tracker body_tracker_nodelet.launch standalone_without_camera_driver:=true
```



Alternatively, if you like to use the camera driver, start the camera
driver first via



```
roslaunch openni2_launch openni2.launch depth_registration:=true
```



and then the human tracker



```
roslaunch cob_openni2_tracker body_tracker_nodelet.launch
```



After the launch process has succeeded, the launch output will be
presented in the current console window and the body tracker will be
ready to detect people. Start moving around to produce some input for
the tracker and get segmented data from the NiTE2 objects.

## Detailed Description

### Visualization

To visualize the results please start Rviz and add a Point Cloud 2 and
assign to a `/body_tracker/points_body_tracker` topic. Don't forget to
set the Color Tranformer to RGB8. This will display the point cloud data
with each detected human in a different color.

To track the results live on the camera stream, please start the camera
plug-in and assign to a `/colorimage_out` topic. Set the parameters for
a desired drawing feature in the configuration file
`/launch/body_tracker_params.yaml` to true.

### User States

According to the probability range of the segmented data, several states
can be assigned to each visible user: detected, tracked and lost.

If users become visible and are in a low probability state, they get a
unique id and will be saved at first as detected. The Point Cloud data
will be accessible to check for the detected areas. These will be
colored in three main colors to separate the detected users.

The detected users with high probability will be saved as tracked.
During this state the data will be published to a `/body_tracker/people`
topic and the colored areas of detected users will be accessible in the
Point Cloud.

If the user is lost, the user id and all assigned states will be erased
from the user map data and the user object will be deleted from the
array of tracked people.
