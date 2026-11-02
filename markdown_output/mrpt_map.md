## Nodes

### mrpt_map

The `mrpt_map` node publishes (static, prebuilt) metric maps stored in
MRPT formats: [.simplemap](http://www.mrpt.org/robotics_file_formats/)
or [.gridmap](http://www.mrpt.org/robotics_file_formats/).

Most ROS packages expect the map to be a unique occupancy grid map. This
node supports those simple maps, plus all other
[map kinds defined in MRPT](http://www.mrpt.org/tutorials/programming/maps-for-localization-slam-map-building/the_hierarchical_model_of_metric_maps/).

#### Published Topics

- `map`
  ([nav_msgs/msg/OccupancyGrid](https://docs.ros.org/en/rolling/p/nav_msgs/msg/OccupancyGrid.html)):
  Only if param `map_file` is NOT empty, the loaded map will be
  published here (Latched)
- `map_metadata` (`nav_msgs::MapMetaData`): Only if param `map_file`
  is NOT empty, the loaded map will be published here (Latched)

#### Services

- `static_map`
  ([nav_msgs/srv/GetMap](https://docs.ros.org/en/rolling/p/nav_msgs/srv/GetMap.html)):
  You can retrieve the loaded map here

#### Parameters

- `~ini_file` (`string`, default: `"map.ini"`): Path to a
  configuration file containing all the required MRPT map parameters.
  See
  [TSetOfMetricMapInitializers::loadFromConfigFile](http://reference.mrpt.org/svn/classmrpt_1_1slam_1_1_t_set_of_metric_map_initializers.html#a48e5c339561ec695921aa7db6291c0e1)
  for format specifications.
- `~map_file` (`string`, default: `(none)`): Path to an MRPT map file in
  either `.simplemap` or `.gridmap` formats. "Simple maps" are
  sequences of observation-pose pairs, so the physical metric map(s) are
  actually generated at load-time.
- `~debug` (`bool`, default: `true`): Verbose debug output
- `~frequency` (`double`, default: `0.1`): Map publication rate (Hz)
- `~frame_id` (`string`, default: `"map"`): TF frame name for published
  map messages
