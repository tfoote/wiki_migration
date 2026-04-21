## Installation

**Ubuntu**: We are only supporting the phidgets_ros package on Ubuntu.
This package should just work with [phidgets_py_api](phidgets_py_api)
and [foote-ros-pkg/phidgets/phidgetspp_c_api](phidgetspp_c_api) nodes.

**MacOSX**: You must do the following:

1\. Download and install the Mac version of the Phidgets, Inc. driver
library:

Mac OS X, Phidget 21 Installer <http://www.phidgets.com/drivers.php>

2\. Download and install Phidgets, Inc. python bindings
<http://www.phidgets.com/downloads/libraries/PhidgetsPython_2.1.6.20100129.zip>

3\. Make sure the python bindings are on your PYTHONPATH.

4\. Comment out the dependency on phidgets_py_api in
phidgets_ros/manifest.xml. Execute rosmake and the Phidgets code should
work on your Mac.

## Accelerometer ROS API

```clearsilver
node.0 {
name= accelerometer.py node
desc= This node is a wrapper around the Accelerometer class provided by Phidgets Inc. This node can be started with or without the accelerometer hardware plugged in. It publishes !AccelerometerEvents when the accelerometer is attached, and it stops publishing when the accelerometer is detached. The node can remaining running throughout multiple accelerometer hardware connects/disconnects.
pub{
0.name= accelerometer/<device_serial_number OR user_defined_name>
0.type= phidgets_ros/AccelerometerEvent
0.desc= Accelerometer value changed events (sensitivity default=0.0).
}
param {
group.0 {
name= Launch Parameters
desc= These parameters are used to specify the user-defined-name, serial_number, and sensitivity for the Accelerometer hardware.
0.name= name
0.default= &#39;&#39;
0.type= str
0.desc= An optional name for the device (used for topic namespace)
1.name= serial_number
1.default= -1
1.type= int
1.desc= The serial number for the Accelerometer. A value of -1 indicates that any serial number is acceptable. Use this with caution as there is no guarantee of which device gets connected if there is more than one accelerometer connected.
2.name= sensitivity
2.default= 0.0
2.type= float
2.desc= This is the amount that an acceleration value must change to trigger an event and publish new data to the topic. The default of 0.0 generates events and publishes to the topic as fast as the hardware can trigger events (our tests show ~62HZ)
3.name= x_axis_id
3.default= 0
3.type= int
3.desc= The accelerometer hardware provides values for axes that are indexed 0-2. Depending on how the device is mounted, the x,y,z mapping can change. Use this parameter to specify the x-axis.
4.name= y_axis_id
4.default= 1
4.type= int
4.desc= The accelerometer hardware provides values for axes that are indexed 0-2. Depending on how the device is mounted, the x,y,z mapping can change. Use this parameter to specify the y-axis.
5.name= z_axis_id
5.default= 2
5.type= int
5.desc= The accelerometer hardware provides values for axes that are indexed 0-2. Depending on how the device is mounted, the x,y,z mapping can change. Use this parameter to specify the z-axis.
}
}
}
```

## RFID ROS API

```clearsilver
node.0 {
name= rfid.py node
desc= This node is a wrapper around the RFID class provided by Phidgets Inc. This node can be started with or without the rfid hardware plugged in. It publishes RFIDEvents when the rfid is attached, and it stops publishing when the rfid is detached. The node can remaining running throughout multiple rfid hardware connects/disconnects.
pub{
0.name= rfid/<device_serial_number OR user_defined_name>
0.type= phidgets_ros/RFIDEvent
0.desc= RFID tag gained/lost events.
}
param {
group.0 {
name= Launch Parameters
desc= These parameters are used to specify the user-defined-name, serial_number, and sensitivity for the RFID hardware.
0.name= name
0.default= &#39;&#39;
0.type= str
0.desc= An optional name for the device (used for topic namespace)
1.name= serial_number
1.default= -1
1.type= int
1.desc= The serial number for the RFID. A value of -1 indicates that any serial number is acceptable. Use this with caution as there is no guarantee of which device gets connected if there is more than one rfid connected.
}
}
}
```

## InterfaceKit ROS API

```clearsilver
node.0 {
name= interface_kit.py node
desc= This node is a wrapper around the !InterfaceKit class provided by Phidgets Inc. This node can be started with or without the !InterfaceKit hardware plugged in. It publishes !Float64Stamped messages when the !InterfaceKit is attached, and it stops publishing when the !InterfaceKit is detached. The node can remaining running throughout multiple !InterfaceKit hardware connects/disconnects.
pub{
0.name= interface_kit/<device_serial_number OR user_defined_name>/sensor/<port_number>
0.type= phidgets_ros/Float64Stamped
0.desc= A new sensor value for a phidgets sensor value changed event.
}
param {
group.0 {
name= Launch Parameters
desc= These parameters are used to specify the user-defined-name, serial_number, and sensitivity for the InterfaceKit hardware.
0.name= name
0.default= &#39;&#39;
0.type= str
0.desc= An optional name for the device (used for topic namespace)
1.name= serial_number
1.default= -1
1.type= int
1.desc= The serial number for the InterfaceKit. A value of -1 indicates that any serial number is acceptable. Use this with caution as there is no guarantee of which device gets connected if there is more than one InterfaceKit connected.
}
}
}
```
