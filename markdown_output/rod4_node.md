* **DEPRECATED**: This node/package has been generalized to
[rotoscan_node](rotoscan_node).*

![](attachment:leuze-rod4plus.jpg)

## Supported Hardware

The rod4_node driver currently supports ROD-4 models connected via
Ethernet only, but could be extended to interface with RS422 models. The
underlying network protocol implementation has been stable for more than
a year now. All testing has been done with a \"ROD4 plus\" unit.

## Configuration and Usage

rod4_node takes only two ROS parameters, one for the hostname/IP address
of the laser range finder (\"host\") and one for the frame ID
(\"frame_id\"). Configuration of the laser rangefinder is only possible
through a separate (physical) configuration port with a vendor-provided
tool and cannot be changed at runtime.

Otherwise, rod4_node should behave like any other ROS laser rangefinder
driver, i.e., publish a \<\<MsgLink(sensor_msgs/LaserScan)\>\> on the
\"scan\" topic whenever a new scan comes in.
