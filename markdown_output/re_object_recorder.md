## What does re_object_recorder do?

The [re_object_recorder](re_object_recorder) package aims at the
creation of object detection models using the Kinect sensor. It allows
the user to control the recording process and improve the results by
manually removing incorrect clouds. By default, 2 types of models with
the following names are created for each object:

-   `kinectmodel.zip`: Contains all the data collected during the
    scanning process. This model files can be used by
    [re_kinect_object_detector](re_kinect_object_detector).
-   `2dcammodel.zip`: A more space efficient object model. These files
    can be used by [re_vision](re_vision). If a !RoboEarth connection is
    established, you can also upload the object model files to the
    database.

See the tutorial
[roboearth_stack/Tutorials/Record an object model](roboearth_stack/Tutorials/Record an object model)
on how to use it.

The object under investigation has to be placed on a marker table, that
holds the following pattern <attachment:marker_template.pdf>. It is
important to print it out the same size (marker edge length of 80.0 mm).
These AR (Augmented Reality) markers are used to register the point
cloud for the model from different views without any expensive
computations. All packages are located in the object_scanning
subdirectory under the [roboearth_stack](roboearth_stack).

This package relies on [ar_bounding_box](ar_bounding_box) to create a
bounding box fixed to the marker pattern. The bounding box is used to
filter the points belonging to the model from background points.

## Common Problems and Solutions

### General Hints

If re_object_recorder is unable to receive object recordings, please
consider the following hints:

-   Make sure that the Kinect camera is not too close to the marker
    pattern. A distance of around 60 cm from the Kinect to the marker
    pattern should be enough.
-   Check that the black boxes on the marker template are squares with a
    side length of 80 mm. You may need to disable printing margins on
    your printer settings to achieve this.
-   Make sure that the marker template is lit uniformly.
-   Glossy and poorly textured objects will probably give poor detection
    results.
-   If none of the hints listed here is helpful to you, consider writing
    a mail to our mailing list:
    <https://lists.roboearth.org/mailman/listinfo/roboearth-users_roboearth.org>

### 'detected X markers in the image; at least 3 markers are necessary to estimate a coordinate system. please check your camera setup.'

ar_bounding_box tries to detect the 3 markers closest to the Kinect and
create a coordinate system; this warning gets displayed whenever there
are less than 3 markers detected.

-   Make sure the marker template is lit uniformly. E.g. turn on the
    artificial light and try to remove light sources that could
    interfere with the recording process.
-   Make sure that the camera has 3 markers completely in its field of
    view. You can check this with e.g. the rviz tool.
-   Check that the point cloud produced by the Kinect contains the
    marker template (using the rviz tool). If not, try moving the camera
    a bit away from the marker template. The Kinect can only provide
    reliable depth information from a distance of around 60cm from the
    object under consideration (see also
    [openni_kinect/kinect_accuracy](openni_kinect/kinect_accuracy)).

### 'distance X/X too large: XXXX'

This message indicates that the ar_bounding_box node was unable to
calculate a coordinate frame from the detected markers.

In order to eliminate implausible scans, we check the distances between
the estimated marker positions. If they differ from the distances given
by the marker template by more than a small threshold, ar_bounding_box
outputs the above warning. In this case, you should check the estimated
marker positions with rivz.

There are multiple ways to address this problem:

-   Check that your camera setup allows the Kinect to always have at
    least three markers fully in its view. You can check this with e.g.
    the rviz tool.
-   Remove objects that look similar to markers from the Kinect's field
    of view.
-   Try to improve the lighting conditions (see above).
-   Make sure the marker template has the right size (each marker must
    have an edge length of exactly 80 mm), is assembled precisely (the
    !RoboEarth logo should form a perfect circle) and is completely
    planar.
-   As a last resort you can increase the 'marker_dist_threshold'
    parameter in ar_bounding_box/launch/ar_kinect.launch'. Increasing
    this parameter will however imply that the maximum allowable error
    on the pattern_base coordinate frame increases, hereby allowing
    larger deviations between measured scans.

### Bad alignment of point clouds

If the point clouds do not seem to be aligned at all, make sure that
depth registration is enabled for the openni driver. See
[openni_launch#Quick_start](openni_launch#Quick_start) on how to do
that.

## Subscribed Topics

. `/resulting_pcl`
([sensor_msgs/msg/PointCloud2](https://docs.ros.org/en/rolling/p/sensor_msgs/msg/PointCloud2.html))
. The object's pointcloud (from [ar_bounding_box](ar_bounding_box)).
