## Description

This package provides two nodes:

- `mrpt_rawlog/rawlog_record_node`: Grabs
  [MRPT rawlogs](http://www.mrpt.org/Rawlog_Format) from ROS topics.
- `mrpt_rawlog/rawlog_play_node`: Like `rosbag play` but takes
  [MRPT rawlogs](http://www.mrpt.org/Rawlog_Format) as input.

Provided examples:



```
roslaunch mrpt_rawlog demo_play.launch
```



See
[demo_play.launch](https://github.com/mrpt-ros-pkg/mrpt_navigation/blob/master/mrpt_rawlog/launch/demo_play.launch)
online.



```
roslaunch mrpt_rawlog demo_record.launch
```



See
[demo_record.launch](https://github.com/mrpt-ros-pkg/mrpt_navigation/blob/master/mrpt_rawlog/launch/demo_record.launch)
online.

Apart from these nodes, the following non-ROS software exists for
handling rawlogs:

- [RawLogViewer](http://www.mrpt.org/list-of-mrpt-apps/rawlogviewer/): A
  powerful GUI, useful to quickly visualize the contents of any dataset,
  modify it, export and import to other formats, etc\... See
  [this video](http://www.youtube.com/watch?v=RZhMZWRplO0) on how a RGBD
  (Kinect) dataset is quickly browsed in this GUI.

<!-- -->

- [rawlog-grabber](http://www.mrpt.org/list-of-mrpt-apps/application-rawlog-grabber/):
  A command-line standalone program to grab observations from a number
  of sensors and put all together into a single timestamp-ordered
  dataset file. Works on GNU/Linux and Windows.

<!-- -->

- [rawlog-edit](http://www.mrpt.org/list-of-mrpt-apps/application-rawlog-edit/):
  A command-line equivalent of RawlogViewer for manipulating, filtering,
  etc. datasets.

<!-- -->

- [carmen2rawlog](http://www.mrpt.org/list-of-mrpt-apps/applicationcarmen2rawlog/):
  A command-line tool to import CARMEN logs as Rawlog datasets.

## Nodes



```clearsilver
 name = rawlog_play_node
 desc = The `rawlog_play_node` node parses a Rawlog file and emit its messages as `rosbag play`.
 pub {
   0{
    name = tf
    type = tf/tfMessage
    desc = Poses of the different sensors and odometry.
   }
  }

 param{
    0.name = ~base_frame
    0.type = string
    0.default = `"base_link"`
    0.desc = The frame attached to the mobile base.
  }

 prov_tf{
  0{
    from = map
    to = odom
    desc = XXX
  }
 }
```





```clearsilver
 name = rawlog_record_node
 desc = The `rawlog_record_node` node subscribes to topics and writes a Rawlog file, like `rosbag record`.
 pub {
   0{
    name = tf
    type = tf/tfMessage
    desc = Poses of the different sensors and odometry.
   }
  }

 param{
    0.name = ~raw_log_folder
    0.type = string
    0.default = `"~/"`
    0.desc = The output directory in which to store rawlogs.
  }
```
