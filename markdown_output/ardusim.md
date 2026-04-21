## Documentation

This package was design to work as a bridge between a wide range of
sensors (analog, i2c, spi) and ROS using the
[arduino](http://www.arduino.cc/).

## Supported Hardware

The following sensors are currently supported by [ardusim](ardusim):

-   Devantech SRF08 Ranger
-   Devantech TPA81 Thermal Array
-   LSE MOX Nose
-   LSE Thermistor Anemometer

![](attachment:srf08_tpa81.jpg) ![](attachment:nose_anemometer.jpg)

## ROS API



```clearsilver
node.0 {
name=gp_node
desc=`gp_node` or general purpose node, is a general implementation of the ardusim protocol. This node will ask the arduino which sensors are currently connected and start publishing all available sensors.
pub{
0.name= range
0.type= lse_sensor_msgs/Range
0.desc= Range data from the sonar(s).
1.name= nose
1.type= lse_sensor_msgs/Nostril
1.desc= Chemical data from the MOX sensor(s).
2.name= tpa
2.type= lse_sensor_msgs/TPA
2.desc= Temperature data from the TPA(s).
3.name= wind
3.type= lse_sensor_msgs/Anemometer
3.desc= Wind speed and direction.
}
param {
0.name= ~port
0.default= /dev/ttyUSB1
0.type= string
0.desc= The port where the arduino can be found.
1.name= ~sonar_frame_id
1.default= /base_sonar
1.type= string
1.desc= The frame in which ranger scans will be returned.
2.name= ~nose_frame_id
2.default= /base_nose
2.type= string
2.desc= The frame in which nose readings will be returned.
3.name= ~tpa_frame_id
3.default= /base_tpa
3.type= string
3.desc= The frame in which tpa readings will be returned.
4.name= ~anemometer_frame_id
4.default= /base_anemometer
4.type= string
4.desc= The frame in which anemometer readings will be returned.
}
}
node.1 {
name=nose_node
desc=The `nose_node` was designed for the LSE MOX nose equipped with the Figaro 2620 and 2600 MOX sensors. This is the setup used on the LSE Roomba.
pub{
0.name= nose
0.type= lse_sensor_msgs/Nostril
0.desc= Chemical data from the MOX sensors.
}
param {
0.name= ~port
0.default= /dev/ttyUSB1
0.type= string
0.desc= The port where the arduino can be found.
1.name= ~frame_id
1.default= /base_nose
1.type= string
1.desc= The frame in which nose readings will be returned.
}
}
node.2 {
name=roomba_sonar_node
desc=The `roomba_sonar_node` was created for the LSE Roombas equipped with an array of 5 Devantech SRF08 rangers.
pub{
0.name= sonars
0.type= lse_sensor_msgs/Range
0.desc= Range data from the sonars.
}
param {
0.name= ~port
0.default= /dev/ttyUSB1
0.type= string
0.desc= The port where the arduino can be found.
1.name= ~frame_id
1.default= /base_sonar
1.type= string
1.desc= Base name for the frame in which sonar ranges will be returned.
}
}
node.3 {
name=thermistor_node
desc=The `thermistor_node` was created for facilitating the thermistor based anemometer calibration.
pub{
0.name= thermistors
0.type= lse_sensor_msgs/Thermistor
0.desc= Raw data from the anemometer thermistors.
}
param {
0.name= ~port
0.default= /dev/ttyUSB1
0.type= string
0.desc= The port where the arduino can be found.
1.name= ~frame_id
1.default= /base_thermistor
1.type= string
1.desc= Base name for the frame in which thermistor values will be returned.
}
}
```



## Custom Nodes

Ardusim is also available as a library on the [ardusim](ardusim)
package. This can be used to make custom nodes with any desired
combination of sensors. To start your own node check the
[Code API](http://www.ros.org/doc/api/ardusim/html/) page.

## Arduino Source Code

The Ardusim source code for the arduino can be downloaded from the
[isr-uc-ros](http://code.google.com/p/isr-uc-ros-pkg/) repository from
the [downloads](http://code.google.com/p/isr-uc-ros-pkg/downloads/list)
section.

## Communication Protocol Documentation

The Ardusim protocol is described in <attachment:ardusim_protocol.pdf>.
