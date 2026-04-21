## Documentation

This package provides a single node rtai_ros_bridge to interface with an
RTAI task. Before running this node one should adopt the sample time and
the mailbox names used by the node to the own needs (hardcoded in
source).

## Nodes



```clearsilver
name = wheeled_robin_node
desc = Node receives data from a mailbox and publishes this data to ROS. Data subscribed from ros is sent into an other mailbox.
sub {
  0.name = data_to_rtai
  0.type = std_msgs/UInt8MultiArray
  0.desc = This data is directly sent to the mailbox and can then be read by the RTAI task.
}
pub {
  0.name = data_from_rtai
  0.type = std_msgs/UInt8MultiArray
  0.desc = Any data sent into the mailbox by the RTAI task is publised on this topic.
}
```


