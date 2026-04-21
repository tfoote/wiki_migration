## Overview

This package provides basic functionality for controlling a RFID reader.

### Devices Supported

This device supports all the drivers implemented in the
[maggie_rfid_drivers](maggie_rfid_drivers) package.

## ROS Nodes



```clearsilver
node.0 {
 name = rfid_node
 desc = ROS node for controlling the rfid.

 pub {
  0.name = rfid_write
  0.type = maggie_rfid_msgs/RfidTag
  0.desc = Publish the content read in a RFID card.
 }

 srv {
  0.name = rfid_write
  0.type = maggie_rfid_msgs/WriteCard
  0.desc = Service to write content in a RFID card.
 }

 param {
  0.name = ~num_device
  0.type = int
  0.default = HEAD_READER_ID
  0.desc = Device number.
 }
}
```



## Launch File Examples

-   For the RFID reader of the head: In a terminal window, start an rfid
    node process running:



```
$ roslaunch maggie_rfid rfid_head.launch robot:=maggie
```



-   For the RFID reader of the base: In a terminal window, start an rfid
    node process running:



```
$ roslaunch maggie_rfid rfid_base.launch robot:=maggie
```



## Examples

An example to read the content of a rfid card could be:

1\. Launch the node. 2. Show the value of the topic:



```
$ rostopic echo /maggie/rfid_write
```


