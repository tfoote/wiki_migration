![\|width=\"333\",height=\"200\"](attachment:Logo-white-medium.jpg)

## Description

This package provides a \'perception algorithm\'-independent simulation
of 6-D object localization for 3D object search by a mobile robot: Based
on the poses of the searched objects with respect to the current viewing
frustum(s) of the robot, the detectability of the objects is estimated.

## Functionality

The system loads objects specified in a object-constellation-file and
recognizes them based on the current camera position (for both, left and
right camera). For a single object at first the given pose is
transformed from the world to the camera frames. For each camera frame
the transformed pose is rated based on its position in the camera
frustum (the distance to the camera and the angles to the camera\'s
visual axis (azimut and elevation) are used). If the rating is higher
than a specified threshold value the pose is valid and the object is
marked as found and returned.

------------------------------------------------------------------------

Optionally random errors which can occur in real world recognition
scenarios can be simulated in three ways:

1\. To simulate frame specific recognition errors random correctly found
objects can be dropped every couple frames 1. To simulate the
recognition accuracy in the found position of the object poses random
noise is added to slightly alter the position in all dimensions 1.
Similar to the position noise errors in the orientation can be generated
for each dimension

------------------------------------------------------------------------

The object-constellation file is using the XML-format and needs to have
a specific layout:

-   The file needs to have at least a root node called *Objects*
-   All recognizable objects are child nodes of this root node and are
    named *Object*
-   The value of each object is its pose (position in x-, y-,
    z-direction followed by its orientation as a quaternion (w,x,y,z) or
    euler angles)
-   In addition to the pose each object has 4 attributes (similar to the
    meta information of the objects in the
    [asr_object_database](asr_object_database)):
-   type: The name of the object
-   mesh: The path to the object\'s mesh file (as a package-url)
-   id: The id of the object
-   angles: Specifies how the orientation is denoted in the pose (can be
    either quaternion or euler)

An example for a valid constellation file could be the following:

```
<Objects>
    <Object type="Cup" id="011021054100" mesh="package://asr_object_database/rsc/databases/segmentable_objects/Cup/object.dae" angles="quaternion">-1.2902,0.729374,0.755761,0.721985,-0.665815,-0.13442,0.131754 </Object>
    <Object type="CoffeeBox" id="0" mesh="package://asr_object_database/rsc/databases/textured_objects/CoffeeBox/CoffeeBox.dae" angles="euler">1.5,-0.5,1.5,90,0,0 </Object>
</Objects>
```

## Usage

### Needed packages

-   [asr_msgs](asr_msgs)
-   [asr_rapidxml](asr_rapidxml)

------------------------------------------------------------------------

If the feature is not turned off there also needs to be a valid
transformation between the frames of the camera and the ones of the
objects in the configuration file (by default \\map). For more
information on the transformation check
[asr_kinematic_chain_dome](asr_kinematic_chain_dome),
[asr_kinematic_chain_mild](asr_kinematic_chain_mild) and [tf](tf).

### Needed software

-   libeigen3-dev
-   ApproxMVBB library. Last checked version 1.1.3 is available here:
    <https://github.com/gabyx/ApproxMVBB/releases/tag/v1.1.3>

### Needed hardware

No hardware is needed for this package to work but by default there has
to be a camera frame which can either be simulated or gathered by using
a real camera setup.

### Start system

At first set the configuration parameters depending on your usage
scenario (see configuration). After you have chosen the object
constellation you want to use and set the topics correctly start the
process:

```
roslaunch fake_object_recognition fake_object_recognition.launch
```

------------------------------------------------------------------------

Now call one of the offered services to add or remove objects from the
list of detectable entities.

## ROS Nodes

### Subscribed Topics

Apart from the frames mentioned above there are no input topics for this
package.

### Published Topics

-   *visualization_msgs/Marker*: A visualization of all available
    objects in the chosen constellation (default:
    /asr_fake_object_recognition/constellation_visualization)
-   *asr_msgs/AsrObject*: The found objects as an *!AsrObject* -message
    to be used by other packages which depend on the results of object
    recognizers (default: /stereo/objects)
-   *visualization_msgs/Marker*: A visualization of the found objects
    depending on the current camera pose (default:
    /stereo/visualization_marker)

### Parameters

This package offers two sets of parameters you can adjust, the static
ones which you can set by adjusting the params.yaml file located in the
param-directory of the package, and the dynamic ones which you can
either set by adjusting the launch-file or during runtime by using
[dynamic_reconfigure](dynamic_reconfigure).

Static parameters:

-   *frame_world* (string): The name of the frame the objects in your
    constellation file are relative to
-   *frame_camera_left* (string): The name of the left camera frame in
    your (simulated or real) camera setup
-   *frame_camera_right* (string): The name of the right camera frame
    (Should be the same as frame_camera_left if you are using a mono
    camera setup)
-   *config_file_path* (string): The path to the XML-file containing
    your object constellation (the path can be relative to your package
    root or absolute)
-   *output_rec_objects_topic* (string): The name of the topic the found
    objects are published on as *!AsrObject *-messages
-   *output_rec_marker_topic* (string): The name of the topic the
    visualization of the found objects is published on
-   *output_constellation_topic* (string): The name of the topic the
    visualization of all available objects in your constellation-XML is
    published on
-   *rating_theshold* (double): The threshold value for the distance
    rating (objects are found if their rating is higher than this value)
-   *rating_threshold_x* (double): The threshold value for the azimut
    angle rating (objects are found if their rating is higher than this
    value)
-   *rating threshold_y* (double): The threshold value for the elevation
    angle rating (objects are found if their rating is higher than this
    value)
-   *timer_duration* (double): The time between the recognition cycles
    (in seconds)

Dynamic parameters:

-   *frustum_mode* (integer): Specifies which camera frustum is used for
    the pose rating of the object (0=both needed, 1=only one needed,
    2=use the left one, 3=use the right one)
-   *use_camera_pose* (boolean): If false all objects in the
    constellation-config-file are published without checking their pose
    relative to the camera
-   *use_pose_invalidation* (boolean): If true randomly invalidates
    found poses based on *prob_pose_invalidation*-value
-   *prob_pose_invalidation* (double): The probability which is used to
    invalidate poses
-   *use_position_noise* (boolean): If true randomly alters the
    positions of the found objects in all dimensions depending on a
    normal distribution
-   *pos_noise_normal_dist_mean* (double): The mean value of the normal
    distribution used for the generation of position errors
-   *pos_noise_normal_dist_dev* (double): The standard deviation value
    of the normal distribution used for the generation of position
    errors
-   *use_orientation_noise* (boolean): If true randomly alters the
    orientations of the found objects depending on normal distributions
-   *or_x_noise_normal_dist_mean* (double): The mean value of the normal
    distribution used for the generation of orientation errors (x-axis)
-   *or_x_noise_normal_dist_dev* (double): The standard deviation value
    of the normal distribution used for the generation of orientation
    errors (x-axis)
-   *or_y_noise_normal_dist_mean* (double): The mean value of the normal
    distribution used for the generation of orientation errors (y-axis)
-   *or_y_noise_normal_dist_dev* (double): The standard deviation value
    of the normal distribution used for the generation of orientation
    errors (y-axis)
-   *or_z_noise_normal_dist_mean* (double): The mean value of the normal
    distribution used for the generation of orientation errors (z-axis)
-   *or_z_noise_normal_dist_dev* (double): The standard deviation value
    of the normal distribution used for the generation of orientation
    errors (z-axis)
-   *config_file_path* (string): The path to the XML-file containing
    your object constellation (the path can be relative to your package
    root or absolute; at startup the path set in the config.yaml file is
    used and can be altered with this parameter during runtime)

### Needed Services

No external services are called by this package.

### Provided Services

-   *get_all_recognizers*: Adds all objects in the used constellation
    file to the list of recognizable objects
-   Parameters: -
-   Returns: -
-   *get_recognizer*: Adds a single object in the used constellation
    file to the list of recognizable objects
-   Parameters:
-   object_type_name (string): The name of the object to add
-   Returns: -
-   *clear_all_recognizers*: Clears the list of recognizable objects
-   Parameters: -
-   Returns: -
-   *release_recognizer*: Removes a single object from the list of
    recognizable objects
-   Parameters:
-   object_type_name (string): The name of the object to remove
-   Returns: -
