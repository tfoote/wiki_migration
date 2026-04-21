## Overview

The non persistent voxel layer incorporate information from the sensors
in the form of PointClouds or LaserScans. This information is converted
into 3D and populated into a temporary voxel_grid for each sensor cycle.

ROS drop in replacement to the voxel layer which does not persist
readings through iterations when ray tracing or map maintenance is
undesirable.

Created in response to need for a rolling local costmap layer to not
persist readings due to a specific sensor being used. After looking
through the community, it seems several people on ros answers have asked
for a similar tool. This is to make that possible.

Source and bug tracker:
<https://github.com/SteveMacenski/nonpersistent_voxel_layer>

Maintainer: Steve Macenski <stevenmacenski AT gmail DOT com>

Author: Steve Macenski, based on work from: Eitan Marder-Eppstein, David
V. Lu!!, Dave Hershberger, contradict@gmail.com

### Marking

The costmap automatically subscribes to sensors topics and updates
itself accordingly. Each sensor is used to mark. With the voxel layer,
obstacle information from each column is projected down into two
dimensions when put into the costmap. The non-persistent voxel layer
does not do any clearing and resets each sensor cycle.

### ROS API

Same API applies to this layer as to the voxel layer, except for the
clearing operations.



```clearsilver
sub {
  0.name= <point_cloud_topic>
  0.type= sensor_msgs/PointCloud
  0.desc= For each `"PointCloud"` source listed in the `observation_sources` parameter list, information from that source is used to update the costmap.
  1.name= <point_cloud2_topic>
  1.type= sensor_msgs/PointCloud2
  1.desc= For each `"PointCloud2"` source listed in the `observation_sources` parameter list, information from that source is used to update the costmap.
  2.name= <laser_scan_topic>
  2.type= sensor_msgs/LaserScan
  2.desc= For each `"LaserScan"` source listed in the `observation_sources` parameter list, information from that source is used to update the costmap.
  3.name= "map"
  3.type= nav_msgs/OccupancyGrid
  3.desc= The costmap has the option of being initialized from a user-generated static map (see the [[#Map_management_parameters | static_map]] parameter). If this option is selected, the costmap makes a service call to the [[map_server]] to obtain this map. 
}
```



#### Sensor management parameters



```clearsilver
param {
  no_header=True
  0.name= ~<name>/observation_sources
  0.default= `""`
  0.type= string
  0.desc=  A list of observation source names separated by spaces. This defines each of the `<source_name>` namespaces defined below.
}
```



Each *`source_name`* in `observation_sources` defines a namespace in
which parameters can be set:



```clearsilver
param {
  no_header=True
  0.name= ~<name>/<source_name>/topic
  0.default=`source_name`
  0.type= string
  0.desc= The topic on which sensor data comes in for this source. Defaults to the name of the source.
  1.name= ~<name>/<source_name>/sensor_frame
  1.default= `""`
  1.type= string
  1.desc= The frame of the origin of the sensor. Leave empty to attempt to read the frame from sensor data. The frame can be read from both `sensor_msgs/LaserScan`, `sensor_msgs/PointCloud`, and `sensor_msgs/PointCloud2` messages.
  2.name= ~<name>/<source_name>/observation_persistence
  2.default= 0.0
  2.type= double
  2.desc= How long to keep each sensor reading in seconds. A value of 0.0 will only keep the most recent reading.
  3.name= ~<name>/<source_name>/expected_update_rate
  3.default= 0.0
  3.type= double
  3.desc= How often to expect a reading from a sensor in seconds. A value of 0.0 will allow infinite time between readings. This parameter is used as a failsafe to keep the [[navigation | navigation stack]] from commanding the robot when a sensor has failed. It should be set to a value that is slightly more permissive than the actual rate of the sensor. For example, if we expect a scan from a laser every 0.05 seconds we might set this parameter to be 0.1 seconds to give a generous buffer and account for some amount of system latency.
  4.name= ~<name>/<source_name>/data_type
  4.default=`"PointCloud"`
  4.type= string
  4.desc=  The data type associated with the topic, right now only `"PointCloud"`, `"PointCloud2"`, and `"LaserScan"` are supported.
  5.name= ~<name>/<source_name>/marking
  5.default= `true`
  5.type= bool
  5.desc= Whether or not this observation should be used to mark obstacles.
  6.name= ~<name>/<source_name>/max_obstacle_height
  6.default=2.0
  6.type= double
  6.desc= The maximum height in meters of a sensor reading considered valid. This is usually set to be slightly higher than the height of the robot. Setting this parameter to a value greater than the global `max_obstacle_height` parameter has no effect. Setting this parameter to a value less than the global `max_obstacle_height`  will filter out points from this sensor above that height.
  7.name= ~<name>/<source_name>/min_obstacle_height
  7.default= 0.0
  7.type= double
  7.desc=  The minimum height in meters of a sensor reading considered valid. This is usually set to be at ground height, but can be set higher or lower based on the noise model of your sensor.
  8.name= ~<name>/<source_name>/obstacle_range
  8.default=2.5
  8.type= double
  8.desc= The maximum range in meters at which to insert obstacles into the costmap using sensor data.
  9.name= ~<name>/<source_name>/raytrace_range
  9.default=3.0
  9.type= double
  9.desc= The maximum range in meters at which to raytrace out obstacles from the map using sensor data.
  10.name= ~<name>/<source_name>/inf_is_valid
  10.default=false
  10.type= bool
  10.desc= Allows for Inf values in `"LaserScan"` observation messages. The Inf values are converted to the laser maximum range.
}
```



#### Global Filtering Parameters

These parameters apply to all sensors.



```clearsilver
param {
  no_header=True
  0.name= ~<name>/max_obstacle_height
  0.default= 2.0
  0.type= double
  0.desc= The maximum height of any obstacle to be inserted into the costmap in meters. This parameter should be set to be slightly higher than the height of your robot.
  1.name= ~<name>/obstacle_range
  1.default=2.5
  1.type= double
  1.desc= The default maximum distance from the robot at which an obstacle will be inserted into the cost map in meters. This can be over-ridden on a per-sensor basis.
}
```



#### NonPersistentVoxelCostmapPlugin

The following parameters are used by the
NonPersistentVoxelCostmapPlugin.



```clearsilver
param {
  no_header=True
  0.name= ~<name>/origin_z
  0.default= 0.0
  0.type= double
  0.desc= The z origin of the map in meters.
  1.name=~<name>/z_resolution
  1.default= 0.2
  1.type= double
  1.desc= The z resolution of the map in meters/cell.
  2.name= ~<name>/z_voxels
  2.default= 10
  2.type= int
  2.desc= The number of voxels to in each vertical column, the height of the grid is z_resolution * z_voxels.
  3.name= ~<name>/unknown_threshold
  3.default= ~<name>/z_voxels
  3.type= int
  3.desc= The number of unknown cells allowed in a column considered to be "known"
  4.name= ~<name>/mark_threshold
  4.default= 0
  4.type=  int
  4.desc=  The maximum number of marked cells allowed in a column considered to be "free".
  5.name= ~<name>/publish_voxel_map
  5.default= `false`
  5.type= bool
  5.desc= Whether or not to publish the underlying voxel grid for visualization purposes.
  6.name= ~<name>/footprint_clearing_enabled
  6.default= `true`
  6.type= bool
  6.desc= If true, the robot footprint will clear (mark as free) the space in which it travels.
}
```


