## Concept

`mqtt_bridge` provides a functionality to bridge between ROS and MQTT
in bidirectional.

`mqtt_bridge` uses ROS message as its protocol. Messages from ROS are
serialized by json (or messagepack) for MQTT, and messages from MQTT are
deserialized for ROS topic. So MQTT messages should be ROS message
compatible. (We use `rosbridge_library.internal.message_conversion`
for message conversion.)

This limitation can be overcome by defining custom bridge class.

## Nodes

```clearsilver
node.0{
name=mqtt_bridge_node
desc= The `mqtt_bridge_node` provides a functionality to bridge between ROS and MQTT in bidirectional.
```
