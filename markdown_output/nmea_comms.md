## Overview

This package provides nodes which enable bidirectional communication
between socket (server) or serial devices and the
[nmea_msgs/msg/Sentence](https://docs.ros.org/en/rolling/p/nmea_msgs/msg/Sentence.html)
message type. This may be useful for a number of scenarios, including if
you:

- want your device's raw NMEA sentences to be available to other nodes,
  or to be bagged
- have a network-connected navsat device
- are particularly sensitive to the CPU usage incurred by
  [PySerial](http://pyserial.sourceforge.net/)

Finally, the combination of a `serial_node` connected directly to a
`socket_node` can create a tee, where a device's serial data is
directly available to ROS, but also served over a socket such that a
remote machine may listen to it via netcat. This is particularly
valuable if your device has a proprietary Windows-only GUI, which you'd
like to be able to use while the device is part of a running ROS system.
An example of this usage is
[supplied in the package](https://github.com/ros-drivers/nmea_comms/blob/indigo-devel/launch/tee.launch),
which you can launch like so:



```
roslaunch nmea_comms tee.launch port:=<serial port> baud:=<baud rate>
```



Once running, you should see the output of your serial NMEA device on
the `/navsat/nmea_sentence` topic, as well as when running `nc
localhost 29500`.

## API

ROS nodes as detailed below. No code API.

## Nodes

### serial_node

Connects to a serial port, passing sentences between ROS and the port.

#### Subscribed Topics

- `nmea_sentence_out`
  ([nmea_msgs/msg/Sentence](https://docs.ros.org/en/rolling/p/nmea_msgs/msg/Sentence.html)):
  Sentences published here will be written to the serial port if a
  device is connected.

#### Published Topics

- `nmea_sentence`
  ([nmea_msgs/msg/Sentence](https://docs.ros.org/en/rolling/p/nmea_msgs/msg/Sentence.html)):
  Sentences received on the serial port.

#### Parameters

- `~frame_id` (`string`, default: `navsat`): The value to use as the
  header's frame_id on published messages.
- `~port` (`string`, default: `/dev/ttyUSB0`): Name of serial port to
  connect to.
- `~baud` (`int`, default: `115200`): Baud rate to connect at.

### socket_node

Open a socket server, to pass NMEA sentences to and from connected
clients.

#### Subscribed Topics

- `nmea_sentence_out`
  ([nmea_msgs/msg/Sentence](https://docs.ros.org/en/rolling/p/nmea_msgs/msg/Sentence.html)):
  Sentences published here will be written to connected socket clients

#### Published Topics

- `nmea_sentence`
  ([nmea_msgs/msg/Sentence](https://docs.ros.org/en/rolling/p/nmea_msgs/msg/Sentence.html)):
  Sentences received from connected clients will be published here

#### Parameters

- `~frame_id` (`string`, default: `navsat`): The value to use as the
  header's frame_id on published messages.
- `~port` (`int`, default: `29500`): Port number to open socket server
  on.
