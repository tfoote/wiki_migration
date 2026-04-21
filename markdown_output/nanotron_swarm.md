## Overview

![](http://wiki.ros.org/nanotron_swarm?action=AttachFile&do=get&target=nanoPAN_DK)



```wiki
This package is part of the ROS stack [[rangeonly_driver]]. It provides a driver for [[http://nanotron.com/|Nanotron]] range-only sensors based on Swarm API firmware. The ROS driver has been developed at the University of Seville in the [[http://grvc.us.es|Robotics, Vision and Control research group (GRVC)]]. This driver also provides a custom ROS message for range-only sensors (see message [[http://docs.ros.org/indigo/api/rangeonly_msgs/html/msg/P2PRange.html|rangeonly_msgs/P2PRange]] on package [[rangeonly_msgs]]).
```

 

```wiki
This package is part of the ROS stack [[rangeonly_driver]]. It provides a driver for [[http://nanotron.com/|Nanotron]] range-only sensors based on Swarm API firmware. The ROS driver has been developed at the University of Seville in the [[http://grvc.us.es|Robotics, Vision and Control research group (GRVC)]]. This driver also provides a custom ROS message for range-only sensors (see message nanotron_swarm/P2PRange of this rosbuild package).
```

 In the case of
Nanotron devices, these devices are based on the Time of Flight of radio
signals to measure the distance between a pair of devices.

## Applications

Examples of usage of this driver can be found in:

-   Aerial robot [dataset](http://grvc.us.es/staff/caba/roslam) for
    indoor and outdoor applications such as localization or Range-Only
    Simultaneous Localization And Mapping (RO-SLAM).

![Range-only sensors in structures - ARCAS project\|width="480"](http://grvc.us.es/staff/felramfab/roslam_datasets/img/manipulation.jpg)

-   RTLS application from Nanotron company (sensor manufacturer):
    <http://nanotron.com/EN/index.php>

## Nodes



```
{#!wiki buildsystem catkin
{{{
#!clearsilver CS/NodeAPI
node.0 {
  name=nanotron_swarm
  desc=`nanotron_swarm` takes the ranging data from usb-serial interface and transforms it in P2PRange ROS messages. The node uses the swarm API firmware which consist on a serial port API.
  pub{
    0.name= range
    0.type= rangeonly_msgs/P2PRange
    0.desc= The range-only mesaurements.
  }
```

 }}}} 

```
{#!wiki buildsystem rosbuild
{{{
#!clearsilver CS/NodeAPI
node.0 {
  name=nanotron_swarm
  desc=`nanotron_swarm` takes the ranging data from usb-serial interface and transforms it in P2PRange ROS messages. The node uses the swarm API firmware which consist on a serial port API.
  pub{
    0.name= range
    0.type= nanotron_swarm/P2PRange or nanotron_swarm/P2PRange (in rosbuild)
    0.desc= The range-only mesaurements.
  }
```

 }}}}

#### Parameters



```clearsilver
param {
  no_header=True
  0.name= ~device
  0.default=/dev/ttyUSB0
  0.type= string
  0.desc= The device USB serial port in which the sensor is connected.
  1.name= ~frame_id
  1.default=/base_nanotron
  1.type= string
  1.desc= The frame ID of the range-only sensor.
}
```



## Report a Bug
