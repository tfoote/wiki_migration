## Overview

The rosserial_python package contains a
Python implementation of the host-side rosserial connection. It
automatically handles setup, publishing, and subscribing for a connected
rosserial-enabled device.

Note that you need to install pyserial for this to work (try pip install
pyserial).

## Nodes

### serial_node.py

Interface to a rosserial-enabled device. This node automatically spins
up subscribers and publishers based on the configuration information
stored in the device.

#### Parameters

- `~port` (`str`, default: `/dev/ttyUSB0`): Name of port to use.
- `~baud` (`int`, default: `57600`): Baud rate, in bps.

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
