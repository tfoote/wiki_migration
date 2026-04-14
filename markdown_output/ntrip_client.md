## Overview

ROS node that will communicate with an NTRP server to receive RTCM
connections and publish them on a ROS topic. Also works with virtual
NTRIP servers by subscribing to NMEA messages and sending them to the
NTRIP server

This node runs on ROS noetic and uses python3.

```clearsilver
node.0 {
 name = ntrip_client
 desc = ROS node that will communicate with an NTRIP server to receive RTCM connections and publish them on a ROS topic.
 pub {
  0.name= rtcm
  0.type= mavros_msgs/RTCM
  0.desc= RTCM corrections received from NTRIP server. Only messages whose checksums have passed validation are sent. The messages contain the raw RTCM bytes including the checksum
 }
 sub {
  0.name = nmea
  0.type = nmea_msgs/Sentence
  0.desc = Receives NMEA sentences which are sent to the NTRIP server. This is required for virtual/network mountpoints to find the best basestation to provide corrections. For specific mountpoints this is likely not needed, although it will be sent to the server anyway.
 }
 param {
  0.name = host
  0.type = string
  0.desc = Hostname of the NTRIP server that the client will receive corrections from.
  0.default = 127.0.0.1
  1.name = port
  1.type = int
  1.desc = Port that the NTRIP server is listening on.
  1.default = 2101
  2.name = authenticate
  2.type = bool
  2.desc = Whether or not to authenticate with the NTRIP server when creating the connection.
  2.default = false
  3.name = username
  3.type = string
  3.desc = The username to use when authenticating with the NTRIP server. Only used if `authenticate` is set to true
  4.name = password
  4.type = string
  4.desc = The password to use when authenticating with the NTRIP server. Only used if `authenticate` is set to true
  5.name = rtcm_frame_id
  5.type = string
  5.desc = The [[https://www.ros.org/reps/rep-0105.html|frame ID]] to set the `frame_id` variable of the RTCM message to.
  5.default = odom
 }
}
```

## Quickstart Tutorials

The github repo for this package is
[here](https://github.com/LORD-MicroStrain/ntrip_client). The README.md
file at <https://github.com/LORD-MicroStrain/ntrip_client> provides
instructions for installing and running this package.

Clone the repo into your workspace src directory and follow the
instructions in the \"Build Instructions\" section of the README.
```
git clone https://github.com/LORD-MicroStrain/ntrip_client
```
