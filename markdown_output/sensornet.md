## Supported Hardware

The sensornet package was designed specifically for the !SensorNet
sensor and actuator nodes developed at LSE. The !SensorNet nodes
communicate over RS485, all the nodes included in this package assume a
Devantech USB-RS485 converter is being used to make the bridge between a
computer running ROS and the !SensorNet.

## ROS API

```clearsilver
node.0 {
name=sensornet_node
desc=`sensornet_node` is the node responsible for publishing the data recovered from the !SensorNet nodes.
pub{
0.name= sensornet_odor
0.type= lse_sensor_msgs/Nostril
0.desc= Chemical data from the MOX sensor(s).
}
param {
0.name= sensornet/port
0.default= /dev/ttyUSB0
0.type= string
0.desc= The port where the USB-RS485 device can be found.
}
}
node.1 {
name=scan_nodes
desc=Node discover tool.
param {
0.name= sensornet/port
0.default= /dev/ttyUSB0
0.type= string
0.desc= The port where the USB-RS485 device can be found.
}
}
node.2 {
name=set_address
desc=Tool that allows changing the address of a node. Very handy for newly built nodes.
param {
0.name= sensornet/port
0.default= /dev/ttyUSB0
0.type= string
0.desc= The port where the USB-RS485 device can be found.
}
}
node.3 {
name=set_sensors
desc=Tools that allows to change the sensors connected to a node. Very handy for newly built nodes.
param {
0.name= sensornet/port
0.default= /dev/ttyUSB0
0.type= string
0.desc= The port where the USB-RS485 device can be found.
}
}
```

## SensorNet Node Source Code and Schematics

Coming soon\...

## Communication Protocol Documentation

The !SensorNet protocol is described in
<attachment:sensornet_protocol.pdf>.
