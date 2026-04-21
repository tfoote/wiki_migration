## Overview

This ROS node is just a wrapper for the
[v4lctl](http://linux.die.net/man/1/v4lctl) tool. It provides two
services, to set and to get particular
[v4l](http://www.linuxtv.org/wiki/index.php/What_is_V4L_or_DVB?) video
device parameter. If a yaml file will be provided a save and restore
capability will be enabled. Parameter are then loaded and set
automatically in the capture device when starting the node. Changed
parameter are stored to a yaml file when the program ends. Additionally
a dynamic reconfigure rqt gui is available to manipulate v4l parameter.

The below v4lctl list output is based on an Osprey 440 bttv capture
card.
[This node's dynamic reconfigure GUI](http://wiki.ros.org/uavc_v4lctl?action=AttachFile&do=view&target=v4lctlgui.png)
is optimized for this card (but the services provided by this ROS node
are generic and can be used for any hardware related available v4l
parameter). Your card may output other options. To support them as well
feel free to adapt the files v4lctl_node.cpp and v4lctlNodeDyn.cfg in
the repository to your needs.



```
$ v4lctl list
  attribute  | type   | current | default | comment
  -----------+--------+---------+---------+-------------------------------------
  norm       | choice | PAL-I   | NTSC    | NTSC NTSC-M NTSC-M-JP NTSC-M-KR PAL PAL-BG PAL-H PAL-I PAL-DK PAL-M PAL-N PAL-Nc PAL-60 SECAM SECAM-B SECAM-G SECAM-H SECAM-DK SECAM-L SECAM-Lc
  input      | choice | Composi | Composi | Composite0 Composite1 Composite2 Composite3
  bright     | int    |   32768 |   32768 | range is 0 => 65280
  contrast   | int    |   32768 |   27648 | range is 0 => 65408
  color      | int    |   32768 |   32768 | range is 0 => 65408
  hue        | int    |   32768 |   32768 | range is 0 => 65280
  mute       | bool   | on      | off     |
  Chroma AGC | bool   | off     | off     |
  Color Kill | bool   | off     | off     |
  Comb Filte | bool   | off     | off     |
  Auto Mute  | bool   | on      | on      |
  Luma Decim | bool   | off     | off     |
  AGC Crush  | bool   | on      | on      |
  VCR Hack   | bool   | off     | off     |
  Whitecrush | int    |     127 |     127 | range is 0 => 255
  Whitecrush | int    |     207 |     207 | range is 0 => 255
  UV Ratio   | int    |      51 |      50 | range is 0 => 100
  Full Luma  | bool   | off     | off     |
  Coring     | int    |       0 |       0 | range is 0 => 3
```



## Nodes



```clearsilver
node.0 {
 name = v4lctl
 desc =
 param {
  7.name= ~device
  7.type= string
  7.desc= The device which v4l parameter are to be changed.
  7.default= /dev/video0
  8.name= ~yaml
  8.type= string
  8.desc= Optional - Path to a yaml file where the changed device v4l parameter are stored to and are read and restored from when starting the node.
  8.default= <empty>
 }
 srv {
  0.name = v4lctlSet
  0.type = uavc_v4lctl/v4lctlSet
  0.desc = Sets a particular v4l parameter.
  1.name = v4lctlGet
  1.type = uavc_v4lctl/v4lctlGet
  1.desc = Gets a particular v4l parameter.
 }
}
```



#### Starting the node

The package contains a launch file which can be used to start the node.



```
$ roslaunch uavc_v4lctl v4lctl.launch device:=/dev/video1
```



#### Sample service calls



```
$ rosservice call /v4lctlSet bright "77%"
$ rosservice call /v4lctlGet bright

$ rosservice call /v4lctlSet hue '!!str 40000'
$ rosservice call /v4lctlGet hue

$ rosservice call /v4lctlSet 'setattr "UV Ratio"' 30%
$ rosservice call /v4lctlGet "UV Ratio"
```



## Installation

### From source

The sources can be found here: <https://github.com/meuchel/uavc_v4lctl>

To build the package do the following:



```
cd ~/catkin_ws/src
git clone https://github.com/meuchel/uavc_v4lctl
cd ~/catkin_ws
catkin build # depending on your workspace it could also be catkin_make
```



## References

<http://linux.die.net/man/1/v4lctl>

<http://www.linuxtv.org/wiki/index.php/V4L_TV_Viewing>
