## Full Documentation from GitHub

## Nodelets



```clearsilver

name = mqtt_client/MqttClient
desc = Enables connected ROS-based devices or robots to exchange ROS messages via an MQTT broker using the MQTT protocol.

sub {
  0.name = <bridge/ros2mqtt[*]/ros_topic>
  0.type = topic_tools/ShapeShifter
  0.desc = ROS topic whose messages are transformed to MQTT messages and sent to the MQTT broker. May have arbitrary ROS message type.
}

pub {
  0.name = <bridge/mqtt2ros[*]/ros_topic>
  0.type = topic_tools/ShapeShifter
  0.desc = ROS topic on which MQTT messages received from the MQTT broker are published. May have arbitrary ROS message type.

  1.name = ~/latencies/<bridge/mqtt2ros[*]/ros_topic>
  1.type = std_msgs/Float64
  1.desc = Latencies measured on the message transfer to <bridge/mqtt2ros[*]/ros_topic> are published here, if the received messages have a timestamp injected.
}

srv {
  0.name = is_connected
  0.type = mqtt_client/IsConnected
  0.desc = Returns whether the client is connected to the MQTT broker.
}

param {
  0.name = ~broker/host
  0.type = str
  0.desc = IP address or hostname of the machine running the MQTT broker
  0.default = localhost

  1.name = ~broker/port
  1.type = int
  1.desc = port the MQTT broker is listening on
  1.default = 1883

  2.name = ~broker/user
  2.type = str
  2.desc = username used for authenticating to the broker (if empty, will try to connect anonymously)

  3.name = ~broker/pass
  3.type = str
  3.desc = password used for authenticating to the broker

  4.name = ~broker/tls/enabled
  4.type = bool
  4.desc = whether to connect via SSL/TLS
  4.default = false

  5.name = ~broker/tls/ca_certificate
  5.type = str
  5.desc = CA certificate file trusted by client (relative to ROS_HOME)
  5.default = /etc/ssl/certs/ca-certificates.crt

  6.name = ~client/id
  6.type = str
  6.desc = unique ID used to identify the client (broker may allow empty ID and automatically generate one)

  7.name = ~client/buffer/size
  7.type = int
  7.desc = maximum number of messages buffered by the bridge when not connected to broker (only available if client ID is not empty)
  7.default = 0

  8.name = ~client/buffer/directory
  8.type = str
  8.desc = directory used to buffer messages when not connected to broker (relative to ROS_HOME)
  8.default = buffer

  9.name = ~client/last_will/topic
  9.type = str
  9.desc = topic used for this client's last-will message (no last will, if not specified)

  11.name = ~client/last_will/message
  11.type = str
  11.desc = last-will message
  11.default = offline

  12.name = ~client/last_will/qos
  12.type = int
  12.desc = QoS value for last-will message
  12.default = 0

  13.name = ~client/last_will/retained
  13.type = bool
  13.desc = whether to retain last-will message
  13.default = false

  14.name = ~client/clean_session
  14.type = bool
  14.desc = whether to use a clean session for this client
  14.default = true

  15.name = ~client/keep_alive_interval
  15.type = float
  15.desc = keep-alive interval in seconds
  15.default = 60.0

  16.name = ~client/max_inflight
  16.type = int
  16.desc = maximum number of inflight messages
  16.default = 65535

  17.name = ~client/tls/certificate
  17.type = str
  17.desc = client certificate file (only needed if broker requires client certificates; relative to ROS_HOME)

  18.name = ~client/tls/key
  18.type = str
  18.desc = client private key file (relative to ROS_HOME)

  19.name = ~client/tls/password
  19.type = str
  19.desc = client private key password

  20.name = ~bridge/ros2mqtt/[ros_topic]
  20.type = str
  20.desc = ROS topic whose messages are transformed to MQTT messages

  21.name = ~bridge/ros2mqtt/[mqtt_topic]
  21.type = str
  21.desc = MQTT topic on which the corresponding ROS messages are sent to the broker

  22.name = ~bridge/ros2mqtt/[inject_timestamp]
  22.type = bool
  22.desc = whether to attach a timestamp to a ROS2MQTT payload (for latency computation on receiver side)
  22.default = false

  23.name = ~bridge/ros2mqtt/[advanced/ros/queue_size]
  23.type = int
  23.desc = ROS subscriber queue size
  23.default = 1

  24.name = ~bridge/ros2mqtt/[advanced/mqtt/qos]
  24.type = int
  24.desc =  MQTT QoS value
  24.default = 0

  25.name = ~bridge/ros2mqtt/[advanced/mqtt/retained]
  25.type = bool
  25.desc = whether to retain MQTT message
  25.default = false

  26.name = ~bridge/mqtt2ros/[mqtt_topic]
  26.type = str
  26.desc = MQTT topic on which messages are received from the broker

  27.name = ~bridge/mqtt2ros/[ros_topic]
  27.type = str
  27.desc = ROS topic on which corresponding MQTT messages are published

  28.name = ~bridge/mqtt2ros/[advanced/mqtt/qos]
  28.type = int
  28.desc = MQTT QoS value
  28.default = 0

  29.name = ~bridge/mqtt2ros/[advanced/ros/queue_size]
  29.type = int
  29.desc =  ROS publisher queue size
  29.default = 1

  30.name = ~bridge/mqtt2ros/[advanced/ros/latched]
  30.type = bool
  30.desc = whether to latch ROS message
  30.default = false
}
```
