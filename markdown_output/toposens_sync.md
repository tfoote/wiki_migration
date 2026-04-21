## Overview

This package enables simultaneous use of multiple TS3 devices in a
sensor system. It administers the lifecycle and ultrasonic emission
characteristics of each sensor to coordinate incoming datastreams. Is is
designed as a thin layer handling multiple
[toposens_driver](toposens_driver)::Sensor instances that individually
encapsulate all the device communication and logic flow.

## ROS Nodes



```clearsilver
name = ts_sync_node
desc = triggers the connected sensors alternately and polls the data from them
pub {
  0.name = ts_scans
  0.type = toposens_msgs/TsScan
  0.desc = The messages are published alternately in the frames of the individual sensors.
}
param {
  0.name = ~ports
  0.type = XmlRpc::XmlRpcValue
  0.desc = array of terminal IDs that the individual sensors are connected to (e.g. ttyUSB0)
  1.name = ~frame_ids
  1.type = XmlRpc::XmlRpcValue
  1.desc = array of frame IDs in which the data is published (element [i] is mapped to element [i] of ~ports)
}
```


