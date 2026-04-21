## Overview

ROS drivers (interfaces) and nodes for Ainstein radars.

## Devices Supported

-   O79 (added Mar. 2020)
-   T79 with normal (ZOI) firmware (added Oct. 2019)
-   K77/T79 with 4+1 (BSD) firmware (added Mar. 2019)
-   SRD-D1 (added Mar. 2019)

## Nodes (and Nodelets)

```clearsilver
node.0 {
name = o79_udp_node
desc = Runs the O79 driver to read Ethernet (UDP) data, parse it and publish radar detections. The O79 imaging radar outputs both raw detections (point cloud) and tracked detections (objects) via an onboard multi-object tracking algorithm. The tracking algorithm can be run in either spherical or Cartesian coordinates; the published topics change accordingly. See the O-79 device manual for more information.
pub {
  0.name = ~targets/raw
  0.type = ainstein_radar_msgs/RadarTargetArray
  0.desc = Raw radar targets/detections, post-CFAR (point cloud)
  1.name = ~targets/tracked
  1.type = ainstein_radar_msgs/RadarTargetArray
  1.desc = Tracked radar targets/detections, post-CFAR and object tracking filter (objects)
  2.name = ~cloud/raw
  2.type = sensor_msgs/PointCloud2
  2.desc = Raw radar detections in PointCloud2 format
  3.name = ~cloud/tracked
  3.type = sensor_msgs/PointCloud2
  3.desc = Tracked radar detections in PointCloud2 format
  4.name = ~boxes
  4.type = ainstein_radar_msgs/BoundingBoxArray
  4.desc = 3D bounding boxes corresponding to track objects' extents
  5.name = ~poses
  5.type = geometry_msgs/PoseArray
  5.desc = Cartesian tracking filter tracked object poses (3D position + 3D orientation aligned with tracked velocity)
  6.name = ~velocities
  6.type = ainstein_radar_msgs/TwistArray
  6.desc = Cartesian tracking filter tracked object velocities (3D position + 3D orientation aligned with tracked velocity)
}
param {
  0.name = ~frame_id
  0.type = string
  0.desc = The frame attached to the radar sensor.
  0.default = "map"
  1.name = ~host_ip
  1.type = string
  1.desc = The host machine's static IP address.
  1.default = "10.0.0.75"
  2.name = ~host_port
  2.type = int
  2.desc = The host machine's Ethernet port, to which the radar sends data.
  2.default = 1024
  3.name = ~radar_ip
  3.type = string
  3.desc = The radar's IP address, configured and stored on the device.
  3.default = "10.0.0.10"
  4.name = ~radar_port
  4.type = int
  4.desc = The radar's Ethernet port from which data is sent, configured and stored on the device.
  4.default = 7
  5.name = ~publish_raw_cloud
  5.type = bool
  5.desc = Sets whether to publish the raw targets as a PointCloud2 message.
  5.default = false
  6.name = ~publish_tracked_cloud
  6.type = bool
  6.desc = Sets whether to publish the tracked targets as a PointCloud2 message.
  6.default = false
}
}
node.1 {
name = o79_can_node
desc = Runs the O79 driver to read CAN data, parse it and publish radar detections. The O79 imaging radar outputs both raw detections (point cloud) and tracked detections (objects) via an onboard multi-object tracking algorithm. The tracking algorithm can be run in either spherical or Cartesian coordinates; the published topics change accordingly. See the O-79 device manual for more information.
pub {
  0.name = ~targets/raw
  0.type = ainstein_radar_msgs/RadarTargetArray
  0.desc = Published raw radar detections (point cloud)
  1.name = ~targets/tracked
  1.type = ainstein_radar_msgs/RadarTargetArray
  1.desc = Published tracked radar detections (objects)
}
param {
  0.name = ~frame_id
  0.type = string
  0.desc = The frame attached to the radar sensor.
  0.default = "map"
  1.name = ~can_id
  1.type = string
  1.desc = The ID which CAN messages are published from on the bus.
  1.default = "0x18FFB24D"
}
}
node.2 {
name = t79_node
desc = Runs the T79 driver to read CAN data, parse it and publish radar detections.
sub {
  0.name = received_messages
  0.type = can_msgs/Frame
  0.desc = Raw CAN frames sent from radar
}
pub {
  0.name = ~targets/raw
  0.type = ainstein_radar_msgs/RadarTargetArray
  0.desc = Published raw radar detections (targets)
  1.name = ~targets/tracked
  1.type = ainstein_radar_msgs/RadarTargetArray
  1.desc = Published tracked radar detections (targets)
}
param {
  0.name = ~frame_id
  0.type = string
  0.desc = The frame attached to the radar sensor.
  0.default = "map"
  1.name = ~can_id
  1.type = int
  1.desc = The radar's CAN ID number (0-9), configured and stored on the device.
  1.default = 0
  2.name = ~min_range
  2.type = float
  2.desc = Minimum range for output detections, in meters (DYNAMICALLY RECONFIGURABLE).
  2.default = 0.0
  3.name = ~max_range
  3.type = float
  3.desc = Maximum range for output detections, in meters (DYNAMICALLY RECONFIGURABLE).
  3.default = 100.0
  4.name = ~min_angle
  4.type = float
  4.desc = Minimum azimuth angle for output detections, in positive degrees (DYNAMICALLY RECONFIGURABLE).
  4.default = 60.0
  5.name = ~max_angle
  5.type = float
  5.desc = Maximum azimuth angle for output detections, in positive degrees (DYNAMICALLY RECONFIGURABLE).
  5.default = 60.0
}
}
node.3 {
name = t79_bsd_node
desc = Runs the driver for a radar in the 4+1 configuration (corner T-79's + front-facing K-77) to read CAN data, parse it and publish radar detections and BSD-related "alarms" (in the case of rear T-79's). The same node is used for K-77 and corner T-79's by changing the "radar_type" parameter, as the intent is for all five radars to be used on a car simultaneously for collision awareness.
sub {
  0.name = received_messages
  0.type = can_msgs/Frame
  0.desc = Raw CAN frames sent from radar
}
pub {
  0.name = ~targets/raw
  0.type = ainstein_radar_msgs/RadarTargetArray
  0.desc = Published raw radar detections (targets)
  1.name = ~targets/tracked
  1.type = ainstein_radar_msgs/RadarTargetArray
  1.desc = Published tracked radar detections (targets)
}
param {
  0.name = ~frame_id
  0.type = string
  0.desc = The frame attached to the radar sensor.
  0.default = "map"
  1.name = ~radar_type
  1.type = int
  1.desc = The radar's type in the 4+1 configuration, set in firmware. Options are 0 (K-77), 1 (front-left T-79), 2 (front-right T-79), 3 (rear-left T-79), or 4 (rear-right T-79).
  1.default = 0
}
}
node.4 {
name = srd_d1_node
desc = Runs the SRD-D1 driver to read UART data, parse it and publish radar detections.
pub {
  0.name = ~targets/raw
  0.type = ainstein_radar_msgs/RadarTargetArray
  0.desc = Published raw radar detections (targets)
}
param {
  0.name = ~frame_id
  0.type = string
  0.desc = The frame attached to the radar sensor.
  0.default = "map"
  1.name = ~device_id
  1.type = string
  1.desc = The name of the serial interface to the radar. Assumes a serial-to-USB converter is used by default.
  1.default = "/dev/ttyUSB0"
  2.name = ~firmware_version
  2.type = strind
  2.desc = Specifies the firmware version, either "old" or "new". This changes the baudrate and message definitions, see code for details.
  2.default = "old"
}
}
```

## Usage

### T79+BSD and/or K77

To configure the radar type prior to testing, use the provided
[t79_bsd_config.sh](https://github.com/AinsteinAI/ainstein_radar/blob/master/ainstein_radar_drivers/scripts/t79_bsd_config.sh)
script which depends on
[can-utils](https://github.com/linux-can/can-utils). Using eg.
`candump can0` is also useful debugging tool to monitor CAN traffic on
the SocketCAN interface.

These CAN radars require a
[socketcan_bridge](http://wiki.ros.org/socketcan_bridge) node publishing
CAN frames to the `/received_messages` ROS topic (see the launch file
below for an example). This package can be installed with:

`bash sudo apt install ros-kinetic-socketcan-bridge`

### K79

The file k79_node.cpp implements a ROS node using the RadarInterfaceK79
interface class to create a UDP socket bound to the host IP address and
port (which must match the radar's configuration), launch a thread to
read and publish data to the RadarData message type.

The python script
[k79_gui.py](https://github.com/AinsteinAI/ainstein_radar/blob/master/ainstein_radar_drivers/scripts/k79_gui.py)
can be used to configure the network parameters and flash new firmware.
See the tutorials for more information.

## Launch Files

The easiest way to get started with any particular radar is to use the
corresponding
[example launch files](https://github.com/AinsteinAI/ainstein_radar/tree/master/ainstein_radar_drivers/launch).
