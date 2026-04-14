## Description

This package contains a recognition system for square, binary 2D-markers
using either a mono or a stereo camera setup.

\'\'Examples of used (printed) markers:\'\'
![\|width=\"600\",height=\"337\"](attachment:aruco_markers.jpg)

\'\'Close-up of a marker with its orientation:\'\'
![\|width=\"600\",height=\"355\"](attachment:aruco_marker_orientation_2.jpg)

## Functionality

### Overview

The objects are detected in the image(s) using the
[ArUco](https://www.uco.es/investiga/grupos/ava/node/26)-library.
Depending on the used camera system (mono or stereo), the found markers
are further processed. If a mono system is used, the found poses of the
[ArUco](https://www.uco.es/investiga/grupos/ava/node/26)-library are
published, if on the other hand a stereo system is used, the final
marker pose is calculated based on the positions of the markers in the
left and right image: If a marker with the same id was found in each of
them, the 3D corner points are calculated using triangulation of the 2D
corner points in each image. The final pose is then calculated using ICP
and then published.

Marker images can be created by using the marker creator tool this
package contains. They need to be printed and then they can be attached
to corresponding objects in the scene. This correspondance can be
specified by adding mesh-models to the
[asr_object_database](asr_object_database) and naming the object
depending on the used marker id (compare already created objects in the
database for more information).

### Example

In this example 4 markers are in the scene, two of which have a
corresponding object stored in the
[asr_object_database](asr_object_database) (monitor and mouse). The
markers each have the size of 1.5x1.5mm and the used cameras have a
resolution of 1292x964.

\'\'Camera image of the stereo setup:\'\'
![\|width=\"700\",height=\"232\"](attachment:aruco_results_3.png)

\'\'Resulting rviz-visualization of the found markers:\'\'
![\|width=\"700\",height=\"232\"](attachment:aruco_results.png)

\'\'Resulting 3D-rviz-visualization of the found markers (as two of the
markers don\'t have a corresponding object only their marker orientation
is shown):\'\'
![\|width=\"600\",height=\"405\"](attachment:aruco_results_2.png)

## Usage

### Needed packages

-   [asr_ivt](asr_ivt)
-   [asr_ivt_bridge](asr_ivt_bridge)
-   [asr_msgs](asr_msgs)
-   [asr_object_database](asr_object_database)

### Needed hardware

A calibrated mono or stereo camera system.

## Start system

### Marker Recognition

Start the process with

```
roslaunch asr_aruco_marker_recognition aruco_marker_recognition.launch
```

------------------------------------------------------------------------

To start the (paused) recognition call the following service:

```
rosservice call /asr_aruco_marker_recognition/get_recognizer
``` To pause the (running) recognition call:

```
rosservice call /asr_aruco_marker_recognition/release_recognizer
```

### Marker Creator

First edit the parameters for the marker creator as you need them to be
(see configuration) and then start the process with

```
roslaunch asr_aruco_marker_recognition marker_creator.launch
``` The created marker images can be found in the
directory specified in the configuration-yaml-file.

## ROS Nodes

### Subscribed Topics

The image and camera information of the left camera (or the camera in a
mono setup):

-   \'\'sensor_msgs/Image\'\' (default: /stereo/left/image_color)
-   \'\'sensor_msgs/CameraInfo\'\' (default: /stereo/left/camera_info)

The topic names can be set in a .yaml file (see configuration). If a
stereo setup is used, the topics above need to be available for both,
the left and the right camera (by default the topic names are the same
with right instead of left)

### Published Topics

-   \'\'sensor_msgs/Image\'\': A visualization of the found markers in
    the left image (default: markers_left)
-   \'\'sensor_msgs/Image\'\': A visualization of the found markers in
    the right image (default: markers_right)
-   \'\'visualization_msgs/Marker\'\': A visualization of the objects
    corresponding to the found markers (stored in the
    asr_object_database) (default: /stereo/visualization_marker)
-   \'\'asr_msgs/AsrObject\'\': A message containing information about
    the found markers and their corresponding objects (name, pose etc.)
    (default: /stereo/objects)

As the subscribed topics, the output topics can be defined in a .yaml
file.

### Parameters

The following parameters can be changed in the
\'\'aruco_marker_recognition_params.yaml\'\' file in the param folder:

-   \'\'use_stereo\'\': If this is true a stereo camera system is used
    for the recognition, in that case the topics for the left and right
    camera have to be set (if this is false the topics of the left
    camera are used for the recognition)
-   \'\'image_left_topic\'\': The topic of the left camera image
-   \'\'image_right_topic\'\': The topic of the right camera image (only
    used if \'\'use_stereo\'\' is true)
-   i\'\'mage_left_cam_info_topic\'\': The topic of the left camera\'s
    parameters
-   \'\'image_right_cam_info_topic\'\': The topic of the right camera\'s
    parameters (only used if \'\'use_stereo\'\' is true)
-   \'\'vis_markers_topic\'\': The topic name of the visualization
    markers used in rviz
-   \'\'left_markers_img_topic\'\': The topic name of the overlay image
    of the left camera
-   \'\'right_markers_img_topic\'\': The topic name of the overlay image
    of the right camera (only used if \'\'use_stereo\'\' ist true)
-   \'\'asr_objects_topic\'\': The name of the topic the
    !AsrObject-messages are published on
-   \'\'marker_size\'\': The size of the used markers in meters
-   \'\'recognizer_name\'\': The name of this recognizer specified in
    [asr_object_database](asr_object_database)

The marker creator has the following parameters specified in
\'\'marker_creator_params.yaml\'\' in the param folder:

-   \'\'marker_ids\'\': A list containing the ids of the markers images
    are created for (valid ids: 0 - 1023)
-   \'\'output_rel_path\'\': The path of the directory the marker images
    are saved to (relative to the package root)
-   \'\'marker_pixel_size\'\': The size of the output markers in pixels

### Needed Services

This package calls a service provided by the
[asr_object_database](asr_object_database) to get information about the
objects corresponding to the used markers:

-   \'\'/asr_object_database/object_meta_data\'\'

### Provided Services

-   \'\'get_recognizer: \'\'Starts the recognition if it is currently
    paused
-   Parameter: -
-   Returns: -
-   \'\'release_recognizer: \'\'Pauses the recognition if it is
    currently running.
-   Parameter: -
-   Returns: -
