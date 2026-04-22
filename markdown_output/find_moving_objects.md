## Overview

This package provides two main nodes; one for finding moving objects in
a stream of
[sensor_msgs/msg/LaserScan](https://docs.ros.org/en/rolling/p/sensor_msgs/msg/LaserScan.html)
messages, and one for finding moving objects in a stream of
[sensor_msgs/msg/PointCloud2](https://docs.ros.org/en/rolling/p/sensor_msgs/msg/PointCloud2.html)
messages. Two corresponding nodelets are also provided.

There are also two nodes and two nodelets for handling two special
message types:
[find_moving_objects/LaserScanArray](http://docs.ros.org/kinetic/api/find_moving_objects/html/msg/LaserScanArray.html)
and
[find_moving_objects/PointCloud2Array](http://docs.ros.org/kinetic/api/find_moving_objects/html/msg/PointCloud2Array.html).
These message types contain a header and, respectively, an array of
[sensor_msgs/msg/LaserScan](https://docs.ros.org/en/rolling/p/sensor_msgs/msg/LaserScan.html)
and
[sensor_msgs/msg/PointCloud2](https://docs.ros.org/en/rolling/p/sensor_msgs/msg/PointCloud2.html).
The intended use for these message types is for multi-diode Lidars and
similar sensors.



```wiki
'''Note that a moving-object-finding node/nodelet should take input from a single sensor only!'''
```



### Finding Moving Objects

The above-mentioned nodes and nodelets output a stream of messages (see
[Defined Message Types](#messagetypes)) containing an array of found
moving objects. For each found object, the provided information includes
details about its position and velocity in the given sensor frame, as
well as in a map, fixed, and base frame. Typically, the latter frames
should be set to `map`, `odom` and `base_link`, respectively (see
[REP 105](http://www.ros.org/reps/rep-0105.html)). A confidence value
and information about each object's distance, closest point and width
(relative the sensor) are also provided.

Note that the nodes rely on
[message filtering](http://wiki.ros.org/tf2/Tutorials/Using%20stamped%20datatypes%20with%20tf2%3A%3AMessageFilter)
from [tf2](../tf2) so the map, fixed and base frames must be specified.
For testing purposes, these could of course all be set to the frame of
the sensor itself.

The nodes/nodelets store a history of received range scans in an
internal data structure referred to as the bank. The velocity of an
object is calculated based on how it has moved from the oldest range
scan stored in the bank to the newest - so the size of the bank (that
is, the number of range scans it stores) is a critical property to set
for the system. The size of the bank can be automatically calculated
based on (measuring the publish rate of the sensor and) a desired time
period which it should cover.

There is also a confidence-enhancing node that can be used for cases
where several sensors are used. This node can take the output of the
moving-object-finding nodes connected to the sensor data streams and
increase the confidence of objects that it believes are seen by several
sensors.

The overall structure of using the provided nodes is given in
<attachment:overall_structure.pdf>.

### Visualization Using RViz

All the nodes and nodelets can be told to publish visualization messages
so that the properties of the found objects can be presented using
[RViz](http://wiki.ros.org/rviz). Each node/nodelet can publish a subset
of the following message types.

-   Arrows (using
    [visualization_msgs/msg/MarkerArray](https://docs.ros.org/en/rolling/p/visualization_msgs/msg/MarkerArray.html)
    and
    [visualization_msgs/msg/Marker](https://docs.ros.org/en/rolling/p/visualization_msgs/msg/Marker.html))
    can be used to display each object's position (base of the arrow),
    velocity (length and direction of the arrow) and confidence value
    (grayness of the arrow; by default, 0.0 is black and 1.0 is white).
-   Green lines (using
    [visualization_msgs/msg/MarkerArray](https://docs.ros.org/en/rolling/p/visualization_msgs/msg/MarkerArray.html)
    and
    [visualization_msgs/msg/Marker](https://docs.ros.org/en/rolling/p/visualization_msgs/msg/Marker.html))
    can be used to display each object's estimated width.
-   Blue lines (using
    [visualization_msgs/msg/MarkerArray](https://docs.ros.org/en/rolling/p/visualization_msgs/msg/MarkerArray.html)
    and
    [visualization_msgs/msg/Marker](https://docs.ros.org/en/rolling/p/visualization_msgs/msg/Marker.html))
    can be used to display how each object has moved from the oldest
    range scan stored in the bank to the newest.
-   The point of each object which is closest to the sensor can be
    visualized by a point (using
    [sensor_msgs/msg/LaserScan](https://docs.ros.org/en/rolling/p/sensor_msgs/msg/LaserScan.html)).
-   Points (using
    [sensor_msgs/msg/LaserScan](https://docs.ros.org/en/rolling/p/sensor_msgs/msg/LaserScan.html))
    can be used to display the newest stored range scan, adapted using
    EMA (Exponential Moving Average), in the bank.

Please refer to the "Parameters" section for each node [below](#nodes)
for more details.

## Paper

A [paper](https://doi.org/10.1007/978-3-030-17798-0_25) explaining the
algorithm and data structure used by `find_moving_objects` was
presented at CVC 2019 and published by Springer. This is a
[pre-print fulltext](attachment:pre-print.pdf) version of the above
paper.

## Example

The nodelet for interpreting
[sensor_msgs/msg/PointCloud2](https://docs.ros.org/en/rolling/p/sensor_msgs/msg/PointCloud2.html)
data streams and the node for interpreting
[sensor_msgs/msg/LaserScan](https://docs.ros.org/en/rolling/p/sensor_msgs/msg/LaserScan.html)
data streams are used in the provided
[launch file](https://github.com/andreasgustavsson/find_moving_objects/blob/kinetic-devel/launch/intel_realsense_d435_and_slamtec_rplidar_a2_w_enhancer.launch).
This launch file can be used to run the interpreters on live or recorded
sensor data (an example
[bag](https://github.com/andreasgustavsson/find_moving_objects/blob/kinetic-devel/bags)
file is provided, but it must be extracted before use). The sensors
supported by the launch file are the following (however, note that other
ROS packages and software libraries are needed to run these live).

-   Intel Realsense D435 depth camera (for
    [sensor_msgs/msg/PointCloud2](https://docs.ros.org/en/rolling/p/sensor_msgs/msg/PointCloud2.html)
    data at about 15-30Hz)
-   Slamtec rplidar A2 (for
    [sensor_msgs/msg/LaserScan](https://docs.ros.org/en/rolling/p/sensor_msgs/msg/LaserScan.html)
    data at about 12Hz)

For the nodelets, there is a launch argument `manager` which is used
to specify which manager the nodelet should connect to. For more
information about the available arguments for launching nodes and
nodelets, please refer to the respective
[launch/includes](https://github.com/andreasgustavsson/find_moving_objects/tree/master/launch/includes)
files.

[Youtube](https://www.youtube.com/watch?v=uV-eyRbe7_8&rel=0)

## Defined Message Types

The following are the message types defined by this package:

-   [find_moving_objects/MovingObject](http://docs.ros.org/kinetic/api/find_moving_objects/html/msg/MovingObject.html)
-   [find_moving_objects/MovingObjectArray](http://docs.ros.org/kinetic/api/find_moving_objects/html/msg/MovingObjectArray.html)
-   [find_moving_objects/LaserScanArray](http://docs.ros.org/kinetic/api/find_moving_objects/html/msg/LaserScanArray.html)
-   [find_moving_objects/PointCloud2Array](http://docs.ros.org/kinetic/api/find_moving_objects/html/msg/PointCloud2Array.html)

Please refer to the message type sources for their documentation.

## Nodes and Nodelets

The node and nodelet used for finding objects in
[sensor_msgs/msg/LaserScan](https://docs.ros.org/en/rolling/p/sensor_msgs/msg/LaserScan.html)
message streams have the same parameters and publish/subscribe to the
same topics. The same is true for the other node and nodelet pairs.



```clearsilver
name = laserscan_interpreter_node and LaserScanInterpreterNodelet
desc << EOM 
The node/nodelet which finds moving objects in a <<MsgLink(sensor_msgs/LaserScan)>> message stream.
There are many parameters which can be specified but the most needed ones are probably:
 * `subscribe_topic` 
 * `topic_objects`
 * `optimize_nr_scans_in_bank`
 * `object_threshold_*`
EOM
param {
  0.name=subscribe_topic
  0.type=string
  0.default="laserscan"
  0.desc=The topic subscribed to.
  1.name=subscribe_buffer_size
  1.type=int
  1.default=1
  1.desc=The size of the subscription buffer.
  2.name=ema_alpha
  2.type=double
  2.default=1.0
  2.desc=Exponential Moving Average (EMA) weighting decrease factor. (If set to 1.0, then there is no EMA.)
  3.name=map_frame
  3.type=string
  3.default="map"
  3.desc=The map frame.
  4.name=fixed_frame
  4.type=string
  4.default="odom"
  4.desc=The fixed frame.
  5.name=base_frame
  5.type=string
  5.default="base_link"
  5.desc=The base frame.
  6.name=nr_scans_in_bank
  6.type=int
  6.default=0
  6.desc=The size of the bank. For this size to take effect, `optimize_nr_scans_in_bank` must be set with the value 0.0.
  7.name=optimize_nr_scans_in_bank
  7.type=double
  7.default=0.5
  7.desc=If not 0.0, then the bank size is optimized to cover the specified time period (in seconds) and `nr_scans_in_bank` is ignored.
  8.name=publish_objects
  8.type=bool
  8.default=`true`
  8.desc=Whether to publish the found moving objects in [[http://docs.ros.org/kinetic/api/find_moving_objects/html/msg/MovingObjectArray.html|find_moving_objects/MovingObjectArray]] messages.
  9.name=publish_ema
  9.type=bool
  9.default=`true`
  9.desc=Whether to publish the newest sensor data (EMA:ed) stored in the bank in a <<MsgLink(sensor_msgs/LaserScan)>> message.
  10.name=publish_objects_closest_points_markers
  10.type=bool
  10.default=`true`
  10.desc=Whether to publish the closest points (relative the sensor) of the found objects in a <<MsgLink(sensor_msgs/LaserScan)>> message.
  11.name=publish_objects_velocity_arrows
  11.type=bool
  11.default=`true`
  11.desc=Whether to publish a <<MsgLink(visualization_msgs/MarkerArray)>> message with an arrow describing the velocity and confidence of each found object.
  12.name=publish_objects_delta_position_lines
  12.type=bool
  12.default=`true`
  12.desc=Whether to publish a <<MsgLink(visualization_msgs/MarkerArray)>> message with a a line describing the change in position of each found object as seen be the bank.
  13.name=publish_objects_width_lines
  13.type=bool
  13.default=`true`
  13.desc=Whether to publish a <<MsgLink(visualization_msgs/MarkerArray)>> message with a a line describing the width of each found object.
  14.name=publish_buffer_size
  14.type=int
  14.default=1
  14.desc=The size of each publish buffer.
  15.name=topic_objects
  15.type=string
  15.default="moving_objects"
  15.desc=The topic name on which to publish the found moving objects.
  16.name=topic_ema
  16.type=string
  16.default="ema"
  16.desc=The topic name on which to publish the newest sensor data stored in the bank.
  17.name=topic_objects_closest_points_markers
  17.type=string
  17.default="objects_closest_point_markers"
  17.desc=The topic name on which to publish the closest points of the found objects.
  18.name=topic_objects_velocity_arrows
  18.type=string
  18.default="objects_velocity_arrows"
  18.desc=The topic name on which to publish the velocity arrows of the found objects.
  19.name=topic_objects_delta_position_lines
  19.type=string
  19.default="objects_delta_position_lines"
  19.desc=The topic name on which to publish the delta position lines of the found objects.
  20.name=topic_objects_width_lines
  20.type=string
  20.default="objects_width_lines"
  20.desc=The topic name on which to publish the width lines of the found objects.
  21.name=ns_velocity_arrows
  21.type=string
  21.default="velocity_arrows"
  21.desc=The namespace of the velocity arrows.
  22.name=ns_delta_position_lines
  22.type=string
  22.default="delta_position_lines"
  22.desc=The namespace of the delta position lines.
  23.name=ns_width_lines
  23.type=string
  23.default="width_lines"
  23.desc=The namespace of the width lines.
  24.name=velocity_arrows_use_full_gray_scale
  24.type=bool
  24.default=`false`
  24.desc=Whether the gray-scale of the velocity arrows should be adapted so that the value of `object_threshold_min_confidence` corresponds to black (the default is that 0.0 corresponds to black and 1.0 to white).
  25.name=velocity_arrows_use_sensor_frame
  25.type=bool
  25.default=`false`
  25.desc=Whether velocity arrows should be displayed in the sensor frame (the default is to display them in the map frame).
  26.name=velocity_arrows_use_base_frame
  26.type=bool
  26.default=`false`
  26.desc=Whether velocity arrows should be displayed in the base frame (the default is to display them in the map frame).
  27.name=velocity_arrows_use_fixed_frame
  27.type=bool
  27.default=`false`
  27.desc=Whether velocity arrows should be displayed in the fixed frame (the default is to display them in the map frame).
  28.name=object_threshold_edge_max_delta_range
  28.type=double
  28.default=0.15
  28.desc=Maximum range difference for two consecutive scan points to belong to the same object.
  29.name=object_threshold_min_nr_points
  29.type=int
  29.default=3
  29.desc=The minimum number of points an object must consist of.
  30.name=object_threshold_max_distance
  30.type=double
  30.default=6.5
  30.desc=The maximum distance of the object.
  31.name=object_threshold_min_speed
  31.type=double
  31.default=0.1
  31.desc=The minimum speed of the object.
  32.name=object_threshold_max_delta_width_in_points
  32.type=int
  32.default=15
  32.desc=The maximum difference in width of the object between two consecutive sensor scans.
  33.name=object_threshold_bank_tracking_max_delta_distance
  33.type=double
  33.default=0.4
  33.desc=The maximum distance the object is allowed to move between two consecutive sensor scans.
  34.name=object_threshold_min_confidence
  34.type=double
  34.default=0.7
  34.desc=The minimum confidence needed in order to publish the given object.
  35.name=base_confidence
  35.type=double
  35.default=0.3
  35.desc=A value corresponding to how well the sensor as such is trusted.
}
```





```clearsilver
name = laserscanarray_interpreter_node and LaserScanArrayInterpreterNodelet
desc << EOM
The node/nodelet which finds moving objects in a [[http://docs.ros.org/kinetic/api/find_moving_objects/html/msg/LaserScanArray.html|find_moving_objects/LaserScanArray]] message stream. 
The same parameters as specified for the `laserscan_interpreter_node` and `Laser``Scan``Interpreter``Nodelet` above are valid here as well.
```





```clearsilver
name = pointcloud2_interpreter_node and PointCloud2InterpreterNodelet
desc << EOM
The node/nodelet which finds moving objects in a <<MsgLink(sensor_msgs/PointCloud2)>> message stream. 
The same parameters as specified for the `laserscan_interpreter_node` and `Laser``Scan``Interpreter``Nodelet` above are valid here as well, with the addition of some `Point``Cloud2`-specific ones listed below.
There are many parameters which can be specified but the most needed ones are probably:
 * `subscribe_topic` 
 * `topic_objects`
 * `optimize_nr_scans_in_bank`
 * `sensor_frame_has_z_axis_forward`
 * `object_threshold_*`
 * `threshold_z_min`
 * `threshold_z_max`
EOM
param {
  0.name=subscribe_topic
  0.type=string
  0.default="pointcloud"
  0.desc=The topic subscribed to.
  1.name=sensor_frame_has_z_axis_forward
  1.type=bool
  1.default=`true`
  1.desc=Whether the sensor frame is an optical frame (see [[http://www.ros.org/reps/rep-0103.html|REP 103]]).
  2.name=bank_view_angle
  2.type=double
  2.default=3.141592654
  2.desc=The Field of View (FoV) of the internal bank representation. (This should preferably be larger than the sensor FoV.)
  3.name=nr_points_per_scan_in_bank
  3.type=int
  3.default=360
  3.desc=The number of scan points in the internal bank representation.
  4.name=message_x_coordinate_field_name
  4.type=string
  4.default="x"
  4.desc=The name of the field in the <<MsgLink(sensor_msgs/PointCloud2)>> message containing the x-coordinate of a point.
  5.name=message_y_coordinate_field_name
  5.type=string
  5.default="y"
  5.desc=The name of the field in the <<MsgLink(sensor_msgs/PointCloud2)>> message containing the y-coordinate of a point.
  6.name=message_z_coordinate_field_name
  6.type=string
  6.default="z"
  6.desc=The name of the field in the <<MsgLink(sensor_msgs/PointCloud2)>> message containing the z-coordinate of a point.
  7.name=voxel_leaf_size
  7.type=double
  7.default=0.01
  7.desc=Defines how many bank points a given cloud point should map onto.
  8.name=threshold_z_min
  8.type=double
  8.default=0.0
  8.desc=Cloud points with a z-coordinate (negative y-coordinate if `sensor_frame_has_z_axis_forward` is set to `true`) smaller than this are discarded.
  9.name=threshold_z_max
  9.type=double
  9.default=1.0
  9.desc=Cloud points with a z-coordinate (negative y-coordinate if `sensor_frame_has_z_axis_forward` is set to `true`) larger than this are discarded.
}
```





```clearsilver
name = pointcloud2array_interpreter_node and PointCloud2ArrayInterpreterNodelet
desc << EOM
The node/nodelet which finds moving objects in a [[http://docs.ros.org/kinetic/api/find_moving_objects/html/msg/PointCloud2Array.html|find_moving_objects/PointCloud2Array]] message stream. 
The same parameters as specified for the `pointcloud2_interpreter_node` and `Point``Cloud2``Interpreter``Nodelet` above are valid here as well.
```





```clearsilver
name = moving_objects_confidence_enhancer_node
desc << EOM
The node which can take information about moving objects as found by several sensors and increase the confidence for those objects which it believes are seen by several sensors.
There are many parameters which can be specified but the most needed ones are probably:
 * `subscribe_topic` 
 * `topic_moving_objects_enhanced`
 * `threshold_max_delta_time_for_different_sources`
 * `threshold_max_delta_position`
 * `threshold_max_delta_velocity`
 * `ignore_z_map_coordinate_for_position`
EOM
param {
0.name=subscribe_topic
0.type=string
0.default="moving_objects"
0.desc=The topic to subscribe to.
1.name=subscribe_buffer_size
1.type=int
1.default=10
1.desc=The size of the subscription buffer.
2.name=verbose
2.type=bool
2.default=`false`
2.desc=Verbose output.
3.name=print_received_objects
3.type=bool
3.default=`false`
3.desc=Whether to print the objects received from each sensor.
4.name=publish_objects
4.type=bool
4.default=`true`
4.desc=Whether to publish/forward the received objects in [[http://docs.ros.org/kinetic/api/find_moving_objects/html/msg/MovingObjectArray.html|find_moving_objects/MovingObjectArray]] messages.
5.name=publish_objects_velocity_arrows
5.type=bool
5.default=`true`
5.desc=Whether to publish a <<MsgLink(visualization_msgs/MarkerArray)>> message with an arrow describing the velocity and confidence of each found object.
6.name=publish_objects_closest_points_markers
6.type=bool
6.default=`true`
6.desc=Whether to publish the closest points (relative the sensor) of the found objects in a <<MsgLink(sensor_msgs/LaserScan)>> message.
7.name=publish_buffer_size
7.type=int
7.default=2
7.desc=The size of each publish buffer.
8.name=topic_moving_objects_enhanced
8.type=string
8.default="moving_objects_enhanced"
8.desc=The topic name on which to publish the moving objects with possibly increased confidence values.
9.name=topic_objects_velocity_arrows
9.type=string
9.default="objects_velocity_arrows"
9.desc=The topic name on which to publish the velocity arrows of the found objects.
10.name=topic_objects_closest_points_markers
10.type=string
10.default="objects_closest_points_markers"
10.desc=The topic name on which to publish the closest points of the found objects.
11.name=velocity_arrows_use_full_gray_scale
11.type=bool
11.default=`false`
11.desc=Whether the gray-scale of the velocity arrows should be adapted so that the value of `threshold_min_confidence` corresponds to black (the default is that 0.0 corresponds to black and 1.0 to white).
12.name=velocity_arrows_use_sensor_frame
12.type=bool
12.default=`false`
12.desc=Whether velocity arrows should be displayed in the sensor frame (the default is to display them in the map frame).
13.name=velocity_arrows_use_base_frame
13.type=bool
13.default=`false`
13.desc=Whether velocity arrows should be displayed in the base frame (the default is to display them in the map frame).
14.name=velocity_arrows_use_fixed_frame
14.type=bool
14.default=`false`
14.desc=Whether velocity arrows should be displayed in the fixed frame (the default is to display them in the map frame).
15.name=threshold_min_confidence
15.type=double
15.default=0.0
15.desc=The minimum confidence needed in order to publish the given object.
16.name=threshold_max_delta_time_for_different_sources
16.type=double
16.default=0.2
16.desc=The maximum difference between the timestamps of messages received from different sensors in order to compare the objects contained in the respective messages.
17.name=threshold_max_delta_position
17.type=double
17.default=0.1
17.desc=The maximum difference in the derived positions of two objects seen by different sensors in order to consider the objects to actually be the same physical object.
18.name=threshold_max_delta_velocity
18.type=double
18.default=0.1
18.desc=The maximum difference in the derived velocities of two objects seen by different sensors in order to consider the objects to actually be the same physical object.
19.name=ignore_z_map_coordinate_for_position
19.type=bool
19.default=`true`
19.desc=Whether to ignore the difference in vertical position (in the map frame) when comparing the position of two objects seen by different sensors.
}
```



## Bug Reports and Feature Requests
