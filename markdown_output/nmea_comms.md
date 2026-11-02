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



```clearsilver
node.0 {
 name = serial_node
 desc = Connects to a serial port, passing sentences between ROS and the port.
 sub {
  0.name = nmea_sentence_out
  0.type = nmea_msgs/Sentence
  0.desc = Sentences published here will be written to the serial port if a device is connected.
 }
 pub {
  0.name = nmea_sentence
  0.type = nmea_msgs/Sentence
  0.desc = Sentences received on the serial port.
  }
 param {
  1.name = ~frame_id
  1.default = navsat
  1.type = string
  1.desc = The value to use as the header's frame_id on published messages.
  2.name = ~port
  2.default = /dev/ttyUSB0
  2.type = string
  2.desc = Name of serial port to connect to.
  3.name = ~baud
  3.default = 115200
  3.type = int
  3.desc = Baud rate to connect at.
  }
 }
node.1 {
 name = socket_node
 desc = Open a socket server, to pass NMEA sentences to and from connected clients.
 sub {
  0.name = nmea_sentence_out
  0.type = nmea_msgs/Sentence
  0.desc = Sentences published here will be written to connected socket clients
 }
 pub {
  0.name = nmea_sentence
  0.type = nmea_msgs/Sentence
  0.desc = Sentences received from connected clients will be published here
  }
 param {
  1.name = ~frame_id
  1.default = navsat
  1.type = string
  1.desc = The value to use as the header's frame_id on published messages.
  2.name = ~port
  2.default = 29500
  2.type = int
  2.desc = Port number to open socket server on.
  }
 }
```
