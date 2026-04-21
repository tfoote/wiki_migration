## Overview

The [rosserial_python](rosserial_python) package contains a Python
implementation of the host-side rosserial connection. It automatically
handles setup, publishing, and subscribing for a connected
rosserial-enabled device.

Note that you need to install pyserial for this to work (try pip install
pyserial).

## Nodes

```clearsilver
name=serial_node.py
desc=Interface to a rosserial-enabled device. This node automatically spins up subscribers and publishers based on the configuration information stored in the device.
param {
  0.name = ~port
  0.type = str
  0.desc = Name of port to use.
  0.default = /dev/ttyUSB0
  1.name = ~baud
  1.type = int
  1.desc = Baud rate, in bps.
  1.default = 57600
}
```

## Examples

To run the node with a different port and baud rate, for example on
/dev/ttyACM1, you must specify the `port` and `baud` parameters on
the command line:

```
rosrun rosserial_python serial_node.py _port:=/dev/ttyACM1 _baud:=115200
```

You can also specify these parameters as part of your launch file:

```
<launch>
  <node pkg="rosserial_python" type="serial_node.py" name="serial_node">
    <param name="port" value="/dev/ttyACM1"/>
    <param name="baud" value="115200"/>
  </node>
</launch>
```
