This package provides services which make object detection more
convenient.

The main service provided by this package performs the following:

-   Grabs a recent point could from a sensor_msgs/PointCloud2 source
-   Transforms the received cloud into the base_link frame
-   Extracts objects and surfaces using
    [rail_pcl_object_segmentation](rail_pcl_object_segmentation)
-   Names each object and surface, publishes them to various topics, and
    informs
    [ MoveIt\'s Planning Scene](http://moveit.ros.org/wiki/Environment_Representation/Overview )
    of the results
-   Returns the named objects

## Services

### Object Discovery - provided by discover_objects_server

This is the highest-level service which provides the most convenience
for discovering objects. This service implements the entire workflow
listed above. The discover_objects_server service processes messages of
the type !DiscoverObjects.srv.

### Updating the Planning Scene - provided by update_environment_service

This service encapsulates the process of naming object and surface point
clouds, publishing them to various ros topics, clearing the state of
[MoveIt\'s Planning Scene](http://moveit.ros.org/wiki/Environment_Representation/Overview),
and adding all discovered objects and surfaces to the Planning Scene.

## Launch Files

### object_discovery.launch

This launch file is the recommended way to start the object discovery
service.

The following nodes are always started:

-   discover_objects_server
-   extract_objects from
    [rail_pcl_object_segmentation](rail_pcl_object_segmentation)
-   cluster_bounding_box_finder_server.py from
    [object_manipulator](object_manipulator)

The following nodes are only started when updating the environment is
enabled:

-   update_environment_service

#### Arguments

` update_state_cloud_timestamps ` (boolean, default=true) Point clouds
may be received which are too old to compute a tf transformation for. If
this flag is true, the latest available transformation will be used when
this occurs; otherwise, a service call will fail.

` update_environment ` (boolean, default=true) When true, the discovered
objects will be given string names and be published such that
[planning_environment](planning_environment) is made aware of them. Note
that any/all objects tracked by
[planning_environment](planning_environment) will be cleared during a
discover_objects service request.

` sensor_topic ` (string, default=/xtion/depth_registered/points) The
topic on which the discover_objects service will wait for a
sensor_msgs/PointCloud2 message when a service request is received.

` target_frame_id ` (string, default=/odom) The tf frame which the
received sensor_msgs/PointCloud2 should be transformed into before
extracting objects.

## Nodes

### discover_objects_server

This node provides an implementation of the !DiscoverObjects.srv
service.

#### Parameters

` ~/sensor_topic ` (string) The topic on which to wait for a
sensor_msgs/PointCloud2 to arrive from when a service request is
received.

` ~/target_frame_id ` (string) The tf frame to transform a received
sensor_msgs/PointCloud2 message in to before extracting objects from it.

` ~/service_name ` (string, default=\"discover_objects\") The name under
which this service should appear in ROS.

` ~/extract_objects_service_name ` (string, default=\"extract_objects\")
The name of the service to use for extracting objects from a point
cloud. This service must conform to !ExtractObjects.srv as defined in
[rail_pcl_object_segmentation](rail_pcl_object_segmentation).

` ~/update_environment ` (boolean, default=true) If true, an
!UpdateEnvironment.srv request will be delivered to the service at the
name specified by /update_environment_service_name.

` ~/update_environment_service_name ` (string,
default=\"update_environment\") Defines the name at which to send
requests to update
[MoveIt\'s Planning Scene](http://moveit.ros.org/wiki/Environment_Representation/Overview)
with object information, if enabled.

` ~/update_old_cloud_timestamps ` (boolean, default=false) In the event
that a point cloud is received which is too old to process a tf
transformation for, this flag determines whether to use the latest
available transformation or throw an error. If true, the latest
available transform is used; otherwise, the affected service request
fails with an error.

### update_environment_service

This node provides an implementation of the !UpdateEnvironment.srv
service.

#### Parameters

` ~/service_name ` (string, default=\"update_environment\") The name
under which this service should appear in ROS.

` ~/bounding_box_service_name ` (string,
default=\"find_cluster_bounding_box2\") The name at which a bounding box
service which fulfills the
[object_manipulation_msgs](object_manipulation_msgs)
!FindClusterBoundingBox2.srv interface can be called.

` ~/output/collision_object_topic_name ` (string,
default=\"collision_object\") The name of the topic to publish collision
object messages suitable for consumption by
[ MoveIt\'s Planning Scene](http://moveit.ros.org/wiki/Environment_Representation/Overview ).

## Using This Package

Make sure a depth camera is generating point clouds. Determine if you
need to change any of the default parameters of the object detection,
then launch it with those arguments: ```
roslaunch rail_object_discovery object_detection.launch
```

When you wish to extract objects, call the \`/discover_objects\` service
with the desired constraints. Here are some example ones:
```
rosservice call /discover_objects "constraints:
object_min_sensor_range: 0.2
  object_max_sensor_range: 4.0
  object_min_spherical_radius: 0.01
  object_max_spherical_radius: 0.1
plane_slope_tolerance: 2.0"
``` Alternately, you can run the
\`extract_objects.sh\` script included in the package, which uses the
constraints in the above example. ```
rosrun rail_object_detection extract_objects.sh
```

If you wish to view the extracted objects in rviz without using !MoveIt,
you can view each extracted object and plane cloud separately by making
a !PointCloud2 display for each of them. The objects are published to
\`/extract_objects/object\_#\` and the planes are published to
\`/extract_objects/plane\_#\`, where \# is 0-9.

Furthermore, a file called \`vision.rviz\` is included in the \`extra/\`
folder. If you paste its contents into an rviz configuration file, it
will add a group of displays for vision-related topics, including Images
for the rgb and depth images of the camera, !PointCloud2s for the camera
and each extracted object and plane, and a !MarkerArray which displays
the name of each object above its center.
