## About

The \`rail_segmentation\` package provides tabletop segmentation
functionality given a point cloud. It also allows for segmentation
within a robot\'s coordinate frame, so that objects stored on a robot\'s
platform can be segmented.

\<\<MsgSrvDoc(rail_segmentation)\>\>

## Object Segmentation APIs

This package exposes three APIs to perform object segmentation, with
varying inputs and outputs. Each API uses the same underlying object
segmentation pipeline, supporting all of the node\'s parameters (listed
in the next section). To call each API, simply use the appropriate ROS
service.

-   \'\'\'Broadcast API\'\'\' (\'\'/segment\'\') - segment objects from
    the most recent point cloud from the \`point_cloud_topic\` param,
    and send the result on the \`/segmented_objects\` topic. This API
    takes an empty service message, and is recommended for cases where
    multiple nodes will need to make use of the segmented object
    information.
-   \'\'\'Direct API\'\'\' (\'\'/segment_objects\'\') - segment objects
    from the most recent point cloud from \`point_cloud_topic\`, and
    return the results in the service response. This API directly
    returns results to the service client that initiated the
    segmentation call, and is recommended for directly incorporating
    object segmentation into a linear pipeline.
-   \'\'\'Static Point Cloud API\'\'\'
    (\'\'/segment_objects_from_point_cloud\'\') - segment objects from a
    given point cloud, and return the results in the service response.
    This API provides object segmentation from arbitrary point clouds,
    not limited to the \`point_cloud_topic\` param, and is recommended
    for applications that require multiple algorithms (including object
    segmentation) to run on the same point cloud, as the user has
    control over exactly which point cloud is used as input.

## Nodes

```clearsilver
node.0 {
  name = rail_segmentation
  desc = `rail_segmentation` provides tabletop object segmentation for handheld objects, as well as segmentation within a robot's coordinate frame for detecting objects stored on a robot itself.
  sub {
    0.name = <~/point_cloud_topic parameter>
    0.type = sensor_msgs/PointCloud2
    0.desc = Incoming point cloud data.
  }
  pub {
    0.name = ~/segmented_objects
    0.type = rail_manipulation_msgs/SegmentedObjectList
    0.desc = Segmented point clouds, images, markers, and calculated features for detected individual objects.
  }
  pub {
    1.name = ~/segmented_table
    1.type = rail_manipulation_msgs/SegmentedObject
    1.desc = A segmented object representing the detected surface above which object segmentation occurs.
  }
  pub {
    2.name = ~/markers
    2.type = visualization_msgs/MarkerArray
    2.desc = Visualization markers corresponding to the segmented objects.
  }
  pub {
    3.name = ~/table_marker
    3.type = visualization_msgs/Marker
    3.desc = Marker corresponding to the detected segmentation surface.
  }
  pub {
    4.name = ~/debug_pc
    4.type = sensor_msgs/PointCloud2
    4.desc = Point cloud publisher for debugging the pipeline, only used if the debug parameter is set to true.
  }
  pub {
    5.name = ~/debug_img
    5.type = sensor_msgs/Image
    5.desc = Image publisher for debugging the pipeline, only used if the debug parameter is set to true.
  }
  srv {
    0.name = ~/segment
    0.type = std_srvs/Empty
    0.desc = Perform object segmentation that will automatically determine a segmentation zone (coordinate frame and bounding volume) as defined by the zones.yaml config file.
  }
  srv {
    1.name = ~/segment_objects
    1.type = rail_manipulation_msgs/SegmentObjects
    1.desc = Alternate API to call object segmentation that returns the segmented objects list as the result in the service message (will also still publish segmented objects on the ~/segmented_objects topic).
  }
  srv {
    2.name = ~/segment_objects_from_point_cloud
    2.type = rail_manipulation_msgs/SegmentObjectsFromPointCloud
    2.desc = Alternate API to call object segmentation on a point cloud that's passed in through the service request, rather than on the most up-to-date point cloud from the `point_cloud_topic` param.
  }
  srv {
    3.name = ~/clear
    3.type = std_srvs/Empty
    3.desc = Clear all segmented objects from the segmented object list.
  }
  srv {
    4.name = ~/remove_object
    4.type = rail_segmentation/RemoveObject
    4.desc = Remove an object from the segmented object list at a given index.
  }
  srv {
    5.name = ~/calculate_features
    5.type = rail_manipulation_msgs/ProcessSegmentedObjects
    5.desc = Recalculate, or fill in uncalculated features of, a given list of segmented objects; assumes that at minimum the point cloud field is set (note that some features cannot be recalculated after segmentation, such as the 2d image).
  }
  param {
    0.name = ~/debug
    0.type = bool
    0.desc = Flag to publish debugging information.
    0.default = false
  }
  param {
    1.name = ~/point_cloud_topic
    1.type = string
    1.desc = ROS topic name for incoming point cloud data.
    1.default = "/camera/depth_registered/points"
  }
  param {
    2.name = ~/zones_config
    2.type = string
    2.desc = Location of the config file defining segmentation zones.
    2.default = "<path to rail_segmentation>/config/zones.yaml"
  }
  param {
    3.name = ~/min_cluster_size
    3.type = int
    3.desc = Minimum number of points in a segmented cluster required to be considered a segmented object.
    3.default = 200
  }
  param {
    4.name = ~/max_cluster_size
    4.type = int
    4.desc = Maximum number of points in a segmented cluster required to be considered a segmented object.
    4.default = 10000
  }
  param {
    5.name = ~/cluster_tolerance
    5.type = double
    5.desc = Maximum Euclidean distance to consider a point as belonging to a cluster, in meters.
    5.default = 0.02
  }
  param {
    6.name = ~/use_color
    6.type = bool
    6.desc = Flag to enable color-based clustering on top of Euclidean distance clustering.
    6.default = false
  }
  param {
    7.name = ~/crop_first
    7.type = bool
    7.desc = Flag to crop the workspace to the segmentation zone workspace bounds before performing table surface detection (helps performance, but may make it harder to detect large surfaces, particularly in cluttered environments).
    7.default = false
  }
  param {
    8.name = ~/label_markers
    8.type = bool
    8.desc = Flag to label the cluster visualization markers published on the `~/markers` topic with text markers showing the corresponding cluster indices from the `~/segmented_objects` topic.
    8.default = false
  }
```

## Installation

To install the \`rail_segmentation\` package, you can install from
source with the following commands: . ```shell
cd /(your catkin workspace)/src
git clone https://github.com/GT-RAIL/rail_segmentation.git
cd ..
catkin_make
catkin_make install
```

## Defining Segmentation Zones

Segmentation zones can be defined in yaml config files, an example of
which can be found in the config directory. The \`zones.yaml\` file
defines a segmentation zone that will segment objects on horizontal
surfaces anywhere above the level of the floor.

The fields for defining a zone are as follows:

Required fields:

-   name - (string) the name of the zone
-   parent_frame_id - (string) parent frame for calculating the roll,
    pitch, and yaw of the camera
-   child_frame_id - (string) child frame for calculating the roll,
    pitch, and yaw of the camera
-   bounding_frame_id - (string) the coordinate frame in which the
    segmentation bounding volume is defined
-   segmentation_frame_id - (string) the coordinate frame in which
    objects should be segmented

Optional fields:

-   remove_surface - (bool) flag for surface removal; set to true if
    segmentation surfaces should be detected and removed, false if
    segmentation should be bounded only by the bounding volume (defaults
    to false).
-   require_surface - (bool) flag for requiring a surface to be found in
    order to perform segmentation; if set to true, clustering will not
    be run if a large horizontal surface is not detected (defaults to
    false).
-   roll_min - (double) lower bound on camera roll for this zone to be
    used, calculated as the roll from the parent_frame_id to the
    child_frame_id
-   roll_max - (double) upper bound on camera roll (for zone selection)
-   pitch_min - (double) lower bound on camera pitch (for zone
    selection)
-   pitch_max - (double) upper bound on camera pitch (for zone
    selection)
-   yaw_min - (double) lower bound on camera yaw (for zone selection)
-   yaw_max - (double) upper bound on camera yaw (for zone selection)
-   x_min - lower x bound defining the bounding volume (for workspace
    cropping)
-   x_max - upper x bound defining the bounding volume (for workspace
    cropping)
-   y_min - lower y bound defining the bounding volume (for workspace
    cropping)
-   y_max - upper y bound defining the bounding volume (for workspace
    cropping)
-   z_min - lower z bound defining the bounding volume (for workspace
    cropping)
-   z_max - upper z bound defining the bounding volume (for workspace
    cropping)

## Segmentation and Results

Segmentation is performed by point cloud clustering according to
Euclidean distance (and optionally, similar color patches) within a
workspace defined by the segmentation zone yaml file.

Each resulting segmented object is represented by a
[rail_manipulation_msgs](rail_manipulation_msgs) SegmentedObject
message, with the following data calculated and filled in:

-   point_cloud: the segmented point cloud
-   image: an rgb image containing the points of the segmented point
    cloud
-   centroid: the segmented point cloud centroid
-   center: the segmented point cloud center (ignores point cloud
    density)
-   bounding_volume: a vertically-aligned, minimum volume bounding
    rectangular prism
-   width (deprecated in favor of the bounding volume): object width
    (dimension along the x-axis in the point cloud frame)
-   depth (deprecated in favor of the bounding volume): object depth
    (dimension along the y-axis in the point cloud frame)
-   height (deprecated in favor of the bounding volume): object height
    (dimension along the z-axis in the point cloud frame)
-   rgb: average color in RGB color space
-   cielab: average color in CIELAB color space (allows for Euclidean
    distance calculation in the color space)
-   marker: downsampled point cloud marker for display in rviz

## Startup

The \`rail_segmentation\` package can be launched by running the
rail_segmentation node: . ```
rosrun rail_segmentation rail_segmentation
```
