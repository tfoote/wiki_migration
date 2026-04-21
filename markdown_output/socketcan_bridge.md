## Overview

The packages provides functionality to expose CAN frames from
[SocketCAN](http://en.wikipedia.org/wiki/SocketCAN) to a ROS Topic.
Internally it uses the [socketcan_interface](socketcan_interface) from
the [ros_canopen](ros_canopen) package, as such it is capable of dealing
with both normal and extended CAN frames. For more information and
hardware related information see
[socketcan_interface](socketcan_interface).

## Nodes

The functionality is offered in the form of three nodes:
`socketcan_bridge_node`, `socketcan_to_topic_node` and
`topic_to_socketcan_node`. To receive frames from and sent frames to the
same CAN device, the `socketcan_bridge_node` needs to be used to prevent
every sent message from being echoed to the receiving topic.



```clearsilver
name = socketcan_bridge_node
desc = Receives frames from SocketCAN devices and publishes these on the topic, at the same time it listens to CAN messages and sends these to SocketCAN. The frames that are sent to the CAN device are not published as received messages.
pub {
  0.name = received_messages
  0.type = can_msgs/Frame
  0.desc = Frames received on the SocketCAN device are published in this topic.
}
sub {
  0.name = sent_messages
  0.type = can_msgs/Frame
  0.desc = Messages received here will be sent to the SocketCAN device.
}
param {
  0.name = ~can_device
  0.type = string
  0.desc = Name of the SocketCAN device, by default these devices are named ''can0'' and upwards.
  0.default = can0
}
```





```clearsilver
name = socketcan_to_topic_node
desc = Publishes the frames received on the SocketCAN device to a topic.
pub {
  0.name = received_messages
  0.type = can_msgs/Frame
  0.desc = Frames received on the SocketCAN device are published in this topic.
}
param {
  0.name = ~can_device
  0.type = string
  0.desc = Name of the SocketCAN device, by default these devices are named ''can0'' and upwards.
  0.default = can0
}
```





```clearsilver
name = topic_to_socketcan_node
desc = Sends CAN messages received on the topic to the SocketCAN device.
sub {
  0.name = sent_messages
  0.type = can_msgs/Frame
  0.desc = Messages received here will be sent to the SocketCAN device.
}
param {
  0.name = ~can_device
  0.type = string
  0.desc = Name of the SocketCAN device, by default these devices are named ''can0'' and upwards.
  0.default = can0
}
```



### Remarks

Several aspects to take into account:

-   Error frames from the device are also converted to a message and
    published on the topic. A warning is displayed for every error
    frame.
-   The timestamp of the messages is based on `ros::Time::now()` at
    the moment the frame is read from SocketCAN.
