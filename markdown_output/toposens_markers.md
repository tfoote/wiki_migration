## Overview

This package enables the visualization of data from a Toposens 3D
ultrasonic sensor Marker Arrays.

## ROS Nodes



```clearsilver
name = ts_markers_node
desc = translates messages of type <<MsgLink(toposens_msgs/TsScan)>> into messages of type <<MsgLink(visualization_msgs/MarkerArray)>>
sub {
  0.name = ts_scans
  0.type = toposens_msgs/TsScan
  0.desc = the scans that are published by the [[toposens_driver]]
}
pub {
  0.name = ts_markers
  0.type = visualization_msgs/MarkerArray
  0.desc = an array of markers for visualizing the sensor data
}
param {
  0.name = ~frame_id
  0.type = std_msgs/String
  0.desc = frame ID in which the data is published
  1.name = ~lifetime
  1.type = double
  1.desc = duration for which a marker should remain visible
  2.name = ~scale
  2.type = double
  2.desc = magnitude for resizing markers equally and simultaneously
}
```


