## Overview

ROS node that will communicate with an NTRP server to receive RTCM
connections and publish them on a ROS topic. Also works with virtual
NTRIP servers by subscribing to NMEA messages and sending them to the
NTRIP server

This node runs on ROS noetic and uses python3.

### ntrip_client

ROS node that will communicate with an NTRIP server to receive RTCM
connections and publish them on a ROS topic.

#### Subscribed Topics

- `nmea`
  ([nmea_msgs/msg/Sentence](https://docs.ros.org/en/rolling/p/nmea_msgs/msg/Sentence.html)):
  Receives NMEA sentences which are sent to the NTRIP server. This is
  required for virtual/network mountpoints to find the best basestation
  to provide corrections. For specific mountpoints this is likely not
  needed, although it will be sent to the server anyway.

#### Published Topics

- `rtcm`
  ([mavros_msgs/msg/RTCM](https://docs.ros.org/en/rolling/p/mavros_msgs/msg/RTCM.html)):
  RTCM corrections received from NTRIP server. Only messages whose
  checksums have passed validation are sent. The messages contain the
  raw RTCM bytes including the checksum

#### Parameters

- `host` (`string`, default: `127.0.0.1`): Hostname of the NTRIP server
  that the client will receive corrections from.
- `port` (`int`, default: `2101`): Port that the NTRIP server is
  listening on.
- `authenticate` (`bool`, default: `false`): Whether or not to
  authenticate with the NTRIP server when creating the connection.
- `username` (`string`): The username to use when authenticating with
  the NTRIP server. Only used if `authenticate` is set to true
- `password` (`string`): The password to use when authenticating with
  the NTRIP server. Only used if `authenticate` is set to true
- `rtcm_frame_id` (`string`, default: `odom`): The
  [frame ID](https://www.ros.org/reps/rep-0105.html) to set the
  `frame_id` variable of the RTCM message to.

## Quickstart Tutorials

The github repo for this package is
[here](https://github.com/LORD-MicroStrain/ntrip_client). The README.md
file at <https://github.com/LORD-MicroStrain/ntrip_client> provides
instructions for installing and running this package.

Clone the repo into your workspace src directory and follow the
instructions in the "Build Instructions" section of the README.


```
git clone https://github.com/LORD-MicroStrain/ntrip_client
```
