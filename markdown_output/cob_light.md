## Hardware Requirements

To use this package you need a Care-O-bot light modul connected via USB.

## ROS API

The [cob_light](cob_light) package provides a node that connects to the
light hardware board and offers a message interface over
[topics](Topics). The current state of the light is published as a
[visualization marker](rviz/DisplayTypes/Marker).


```clearsilver
 name = cob_light.py
 desc = The `cob_light.py` node takes in <<MsgLink(std_msgs/ColorRGBA)>> messages and send this directly to the hardware. If no hardware is present, the node runs in a simulated mode only publishing [[rviz/DisplayTypes/Marker|visualization markers]].

sub{
 0.name = command
 0.type = std_msgs/ColorRGBA
 0.desc = Receives color commands in RGBA format.
}

pub{
 0.name = marker
 0.type = visualization_msgs/Marker
 0.desc = Publishes the current state of the light.
}

param{
 0.name = ~devicestring
 0.type = string
 0.default = Required
 0.desc = Device identifier for hand, e.g. /dev/ttyUSB3
 1.name = ~baudrate
 1.type = int
 1.default = Required
 1.desc = Baudrate of serial interface, e.g. 230400
}

req_tf{
}

prov_tf{
}
```



## Usage/Examples

The package can be used via a launch file which loads all parameters and
starts the light node. For starting the light use


```
roslaunch cob_bringup light.launch
```

 For including the light in your overall launch
file use 

```
<include file="$(find cob_bringup)/components/light.launch" />
```

 A sample parameter file could look
like this 

```
devicestring: /dev/ttyUSB3
baudrate: 230400
```



For testing the light you can start a test_script which changes the LEDs
to different colors. 

```
rosrun cob_light test.py
```


