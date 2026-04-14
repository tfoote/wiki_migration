## Nodes

### mrpt_map

The \`mrpt_map\` node publishes (static, prebuilt) metric maps stored in
MRPT formats: [.simplemap](http://www.mrpt.org/robotics_file_formats/)
or [.gridmap](http://www.mrpt.org/robotics_file_formats/).

Most ROS packages expect the map to be a unique occupancy grid map. This
node supports those simple maps, plus all other
[map kinds defined in MRPT](http://www.mrpt.org/tutorials/programming/maps-for-localization-slam-map-building/the_hierarchical_model_of_metric_maps/).

```clearsilver
srv {
  0.name = static_map
  0.type = nav_msgs/GetMap
  0.desc = You can retrieve the loaded map here
}
pub {
  0.name= map
  0.type= nav_msgs/OccupancyGrid
  0.desc= Only if param `~map_file` is NOT empty, the loaded map will be published here  (Latched)

  1.name= map_metadata
  1.type= nav_msgs::MapMetaData
  1.desc= Only if param `~map_file` is NOT empty, the loaded map will be published here  (Latched)
}
param{
    0.name = ~ini_file
    0.type = string
    0.default = `"map.ini"`
    0.desc = Path to a configuration file containing all the required MRPT map parameters. See [[http://reference.mrpt.org/svn/classmrpt_1_1slam_1_1_t_set_of_metric_map_initializers.html#a48e5c339561ec695921aa7db6291c0e1|TSetOfMetricMapInitializers::loadFromConfigFile]] for format specifications.
   
    1.name = ~map_file
    1.type = string
    1.default = (none)
    1.desc = Path to an MRPT map file in either `.simplemap` or `.gridmap` formats. "Simple maps" are sequences of observation-pose pairs, so the physical metric map(s) are actually generated at load-time.

    2.name = ~debug
    2.type = bool
    2.default = true
    2.desc = Verbose debug output

    3.name = ~frequency
    3.type = double
    3.default = 0.1
    3.desc = Map publication rate (Hz)

    4.name = ~frame_id
    4.type = string
    4.default = "map"
    4.desc = TF frame name for published map messages
}
```
