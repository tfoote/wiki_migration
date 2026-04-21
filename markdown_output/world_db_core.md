## Overview

`world_db_core` provides the basic functionality for creating and
maintaining a persistent belief state. It uses an interface to rosbag to
record low-level sensor data and creates an index in an SQLite database.
Plugins have access to the database through
[model_database](model_database) and can store their state for later
calls. Further, plugins have access to the recorded bag files. They can
either directly play back sensor data or get instances of type
`rosbag::MessageInstance` to publish or process them on their own.

## Configuration

The basic configuration is done via ros parameters. Plugin parameters
normally live in sub-namespaces of `world_db_core`.



```clearsilver

param {
  0.name=~base_directory
  0.type= string
  0.desc= The directory in which the database is created/read and where bag files are put.

  1.name=~plugins
  1.type= list
  1.desc= The plugins to load on startup. This parameter contains a list of lists. Every sublist has length 2 with the plugin name as the first element and the namespace of the plugin as the second element.

  2.name=~topics
  2.type= list
  2.desc= The list of topics to record. `world_db_core` supports throttled recording, i.e. it records messages at most at the specified rate. This parameter is a list of lists with every sublist containing exactly two parameters. The topic to record is the first element and the minimum time difference between two messages as the second parameter.
```



## Example Configuration

This yaml snippet configures `world_db_core` to record the tilting
laser, tf and the narrow stereo. It loads four plugins and parameterizes
them. For the parameters of the plugins, please read the documentation
on [world_db_detector_lib](world_db_detector_lib) and
[tf_recorder_plugin](tf_recorder_plugin).



```
base_directory: /removable/lorenz/planes
      topics:
        - ["/tf", 0.05]
        - ["/narrow_stereo_textured/points2", 2.0]
        - ["/tilt_scan", 0.0]
      plugins:
        - ["world_db_plane_detector/PlaneDetector", "plane_detector"]
        - ["world_db_plane_detector/TableDetector", "table_detector"]
        - ["world_db_table_highlevel/TableHighlevel", "table_highlevel"]
        - ["tf_recorder_plugin/TFRecorder", "tf_recorder"]
      tf_recorder:
        record_frequency: 20.0
      plane_detector:
        detector_action: "/plane_detector/detect"
        detector_input_topic: "/plane_detector/input"
        detector_name: "/plane_detector"
        robot_base_frame: "/base_link"
        recorded_input_topic: "/narrow_stereo_textured/points2"
      table_detector:
        source_plugin_name: "plane_detector"
      table_highlevel:
        detector_action: "/highlevel_detector/highlevel_detection"
        detector_input_topic: "/highlevel_detector/input"
        detector_name: "/highlevel_detector"
        robot_base_frame: "/base_link"
        source_plugin_name: "table_detector"
        playback_rate: 10
```


