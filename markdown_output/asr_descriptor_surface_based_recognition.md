![\|width=\"333\",height=\"200\"](attachment:Logo-white-medium.jpg)

## Description

This package contains an object localization system that returns 6-DoF
poses for textured objects in RGBD-data.
![\|width=\"600\",height=\"248\"](attachment:descriptor_overview_eng.png)

## Functionality

This package uses a combination of 2D and 3D recognition algorithms to
detect objects in a textured point cloud. This task is achieved by using
a 5-step process:

1\. At first a 2D-recognition on the input-image is done. This
recognition is based on the descriptor-matching functions the
[HALCON](http://www.mvtec.com/products/halcon/) library offers (see
[here](http://www.mvtec.com/doc/halcon/11/en/create_uncalib_descriptor_model.html)
and
[here](http://www.mvtec.com/doc/halcon/11/en/find_uncalib_descriptor_model.html)
for more information on the used matching algorithms and the used
parameters) and it uses images of the object, taken from different
orientations (we call them views), as references for the matching with
the scene image (therefore a coarse orientation of the object can
already be computed.\
![\|width=\"600\",height=\"241\"](attachment:descriptor_2d_search_eng.png)\

1\. Once a texture (view) of the searched object is found in the image,
the point cloud is reduced with the diameter of the object at the
corresponding location (this correspondence exists because of the
registration of the camera image to the depth image). In the training
phase the object\'s diameter was set and so was the location of the
found view\'s center. As the matching returns a homography as a result
which describes the transformation of the trained view into the scene
image, it is possible to transform the set center point with this
homography into the image. For the pixel which results from this
transformation, the corresponding 3D-point in the cloud can be obtained.
To reduce errors which can occur because of noise in the point cloud
data, the median of multiple points in the area of this corresponding
pixel is used. To get those other points, an offset is added to the
pixel location and the corresponding 3D-points are taken into account
for the calculation of the median. Now the point cloud is reduced with
the diameter of the object around this median point.\
\
*Transformation into the scene image (abstracted; view\'s center
depicted as cross; descriptor points depicted as red dots):*\
![\|width=\"600\",height=\"187\"](attachment:descriptor_cloud_reduction.png)\
\
\
*Cloud reduction:\
*
![\|width=\"600\",height=\"241\"](attachment:descriptor_2d_search_eng.png) 1.
The reduced point cloud, which should only contain the object, now is
used for a 3D matching with the trained object model (see
[here](http://www.mvtec.com/doc/halcon/11/en/create_surface_model.html)
and
[here](http://www.mvtec.com/doc/halcon/11/en/find_surface_model.html)
for more information). 1. In case of a rotation-variant object, the
resulting pose from the last step can now be returned; as we want to be
able to recognize objects without this feature as well though (e.g.
cylindrical objects or spherical ones), more steps are necessary to
ensure that the found pose is correct. That is because the last step
only uses the geometrical attributes of the object to find it in the
point cloud but not the texture/color information. To ensure that the
found pose is also valid for those informations, the 2D and 3D matching
results are compared and the pose is adjusted (as we know which view was
found and how it is transformed into the image we can approximate the
orientation of the object).\
\
*Rotation-invariance (from left: no rotation, cylindrical, spherical):*\
![\|width=\"600\",height=\"255\"](attachment:descriptor_rot_invariance.png)\
\
*Geometrical view problem (both views on the left appear as the cloud on
the right):*\
![\|width=\"600\",height=\"417\"](attachment:descriptor_geom_view.png)\
1. The last step is optional and is used to add another validation layer
to the recognition process. The textured mesh of the found object is
rendered to an artificial image with the found pose. Now the 2D matching
from step 2 is done again on this new image. Based on a metric comparing
the resulting homographies of the matching on both the real and the
artificial image, it can be checked whether the found pose is valid and
can be returned.\
\
*Real scene image left, artificial one right:*\
![\|width=\"600\",height=\"243\"](attachment:descriptor_pose_val.png)\

In addition to the object recognizer, the package offers a graphical
training application which is used to add new objects to the list of
recognizable entities.

## Usage

### Needed packages

-   [asr_halcon_bridge](asr_halcon_bridge)
-   [asr_msgs](asr_msgs)
-   [asr_ros_uri](asr_ros_uri)
-   [asr_rapidxml](asr_rapidxml)
-   [asr_object_database](asr_object_database)

### Needed software

-   wxWidgets
-   Eigen
-   Boost

### Needed hardware

A depth sensor with a registered RGB camera is needed to get textured
point clouds as an input for this package. In our scenario we used a
Microsoft Kinect and an additional AVT Guppy camera for the RGB images
because of the low resolution of the internal RGB-camera of the Kinect.

As this package makes use of the HALCON library provided by the
asr_halcon_bridge package, you need to make sure that a valid license is
available on your machine. If this license is obtained by using a
USB-dongle, make sure that it is plugged in when you use this software
or you will get an exception at startup.

### Start system

To start the process, call:

```
roslaunch asr_descriptor_surface_based_recognition descriptor_surface_based_recognition.launch
``` Now you can call one of the provided services
to add or remove objects to/from the list of recognizable ones.

## ROS Nodes

### Subscribed Topics

-   *sensor_msgs/Image*: The RGB-camera image (default:
    /stereo/left/image_rect_color)
-   *sensor_msgs/Image*: The same as the camera image above but as a
    greyscale image (default: /stereo/left/image_rect)
-   *sensor_msgs/PointCloud2*: The point cloud the images above are
    registered to (default: /kinect/depth_registered_with_guppy/points)

### Published Topics

-   *visualization_msgs/MarkerArray*: A visualization of the volume in
    the point cloud the recognizer uses for each object after it was
    found in 2D (default:
    /asr_descriptor_surface_based_recognition/object_boxes)\
    ![\|width=\"600\",height=\"243\"](attachment:descriptor_vis_boxes.png)
-   *sensor_msgs/PointCloud2*: A visualization of the reduced point
    clouds the recognizer uses for the 3D recognition (one color for
    each object) (default:
    /asr_descriptor_surface_based_recognition/object_clouds)\
    ![\|width=\"600\",height=\"246\"](attachment:descriptor_vis_cloud.png)
-   *sensor_msgs/Image*: A visualization of the 2D recognition results\
    ![\|width=\"600\",height=\"242\"](attachment:descriptor_vis_2d.png)
-   *asr_msgs/AsrObject*: The found objects as an !AsrObject-message
    which can be used by other packages and contains information like
    the name, pose etc. (default: /stereo/objects)
-   *visualization_msgs/Marker*: A visualization of the found objects as
    meshes (default: /stereo/visualization_marker)\
    ![\|width=\"600\",height=\"244\"](attachment:descriptor_results.png)

### Parameters

There are two types of parameters which can be set, static and dynamic
ones. The static ones can be found in the .yaml file in the
param-directory and the dynamic ones in the launch-file (or during
runtime by using [dynamic_reconfigure](dynamic_reconfigure)).

Static parameters:

-   image_color_topic (string): The name of the topic the colored
    scene-image is published on (default: /stereo/left/image_rect_color)
-   image_mono_topic (string): The name of the topic the greyscale
    scene-image is published on (default: /stereo/left/image_rect)
-   point_cloud_topic (string): The name of the topic the point cloud is
    published on (default: /kinect/depth_registered_with_guppy/points)
-   output_objects_topic (string): The name of the topic the found
    objects are published on as !AsrObject -messages (default:
    /stereo/objects)
-   output_marker_topic (string): The name of the topic the found
    objects are published on as visualizable meshes (default:
    /stereo/visualization_marker)
-   output_marker_bounding_box_topic (string): The name of the topic the
    bounding boxes of the reduced point clouds are published on for
    visualization (default: object_boxes)
-   output_cloud_topic (string): The name of the topic the reduced point
    clouds are published on for visualization (default: object_clouds)
-   output_image_topic (string): The name of the topic the 2D
    recognition results are published on for visualization (default:
    objects_2D)
-   pose_val_image_width (double): The width of the pose validation
    image (should be the same as the width of the original camera image)
    (default: 1292.0)
-   pose_val_image_height (double): The height of the pose validation
    image (should be the same as the height of the original camera
    image) (default: 964.0)
-   pose_val_render_image_width (integer): The width of the render image
    used for visualizing the pose validation (default: 800)
-   pose_val_render_image_height (integer): The height of the render
    image used for visualizing the pose validation (default: 600)
-   pose_val_far_plane (double): The far clip plane distance of the
    virtual camera used for pose validation (default: 100)
-   pose_val_near_plane (double): The near clip plane distance of the
    virtual camera used for pose validation (default: 0.01)
-   pose_val_cx (double): The x-value of the optical center of the
    virtual camera used for pose validation (should be the same as the
    one of the original camera) (default: 648.95153)
-   pose_val_cy (double): The y-value of the optical center of the
    virtual camera used for pose validation (should be the same as the
    one of the original camera) (default: 468.29311)
-   pose_val_fx (double): The focal length in x-direction of the virtual
    camera used for pose validation (should be the same as the one of
    the original camera) (default: 1689.204742)
-   pose_val_fy (double): The focal length in y-direction of the virtual
    camera used for pose validation (should be the same as the one of
    the original camera) (default: 1689.204742)

Dynamic parameters:

-   medianPointsOffset (integer): Offset of the points used for
    calculating the median point the point cloud reduction relies on
    (see step 2 in functionality).
-   samplingDistance (double): Scene sampling distance relative to the
    diameter of the surface model used in the 3D recognition (the HALCON
    matching algorithms reduces the scene point cloud by sampling it
    with this distance, see
    [here](http://www.mvtec.com/doc/halcon/11/en/find_surface_model.html))
-   keypointFraction (double): Fraction of sampled scene points used as
    key points in 3D recognition (see the page mentioned at the
    samplingDistance parameter)
-   useVisualisationColor (boolean): Use a colorized image for the
    visualisation of the 2D recognition
-   visualisationColorPointsRed (integer): Red component of the
    visualized points\' color
-   visualisationColorPointsGreen (integer): Green component of the
    visualized points\' color
-   visualisationColorPointsBlue (integer): Blue component of the
    visualized points\' color
-   visualisationColorBoxRed (integer): Red component of the visualized
    bounding box color
-   visualisationColorBoxGreen (integer): Green component of the
    visualized bounding box color
-   visualisationColorBoxBlue (integer): Blue component of the
    visualized bounding box color
-   boundingBoxBorderSize (integer): Thickness of the visualized
    bounding box in the 2D visualization
-   orientationTriangleSize (integer): Size of the triangle visualizing
    the orientation of the bounding box in the 2D visualization
-   featurePointsRadius (integer): Radius of the visualized feature
    points in the 2D visualization
-   drawCloudBoxes (boolean): Draw bounding boxes, each containing the
    3D search domain for a found object instance
-   drawCompleteCloudBoxes (boolean): Draw a complete bounding box (only
    the front side if false)
-   usePoseValidation (boolean): Validate found poses by comparing the
    input RGB-image to a rendered one with the found objects
-   poseValidationDistanceError (integer): Maximum distance between two
    points which were projected with the found projection matrix in the
    original image and the one in the rendered image
-   aggressivePoseValidation (boolean): Discard a pose if the searched
    view can\'t be found in the rendered image during pose validation
    (e.g. because of the bad resolution of the rendered mesh model). If
    disabled, a pose is always set as valid when no view was found,
    otherwise it is set as invalid in that case
-   evaluation (boolean): Output evaluation files (runtimes and found
    poses)

### Needed Services

The process calls services from the asr_object_database to get
information about the objects which are recognizable:

-   */asr_object_database/object_meta_data*: Is called to get basic
    information about recognizable objects
-   */asr_object_database/recognizer_list_meshes*: Is called to get all
    available object meshes. This information is needed due to internal
    implementation details of the pose validation step.

### Provided Services

-   get_recognizer: Adds an object to the list of recognizable ones
-   Parameters:
-   object_name (string): The name of the object
-   count (integer): The maximum amount of instances this object can
    have in the scene
-   use_pose_val (boolean): If true, pose validation is used to reduce
    the amount of recognition failures
-   Returns:
-   success (boolean): Indicates whether the object was added correctly
-   object_name (string): The name of the added object
-   release_recognizer: Removes a single object from the list of
    recognizable ones
-   Parameters:
-   object_name (string): The name of the object to remove
-   Returns: -
-   get_object_list: Returns the list of objects the system currently
    tries to recognize
-   Parameters: -
-   Returns:
-   objects (string\[\]): A list of names of the objects currently
    recognized
-   clear_all_recognizers: Clears the list of recognizable objects
-   Parameters: -
-   Returns: -

## Tutorials

-   [Training a new object](asr_descriptor_surface_based_recognition/trainer_tutorial)
