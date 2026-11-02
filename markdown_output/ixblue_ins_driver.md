## Supported Hardware

This driver supports all iXblue inertial sensors outputing stdbin
protocol like the
[Atlans](https://www.ixblue.com/products/atlans-series) and
[Phins Compact](https://www.ixblue.com/products/phins-compact-series)
series.

![attachment:atlans.png](doc/atlans.png)

## INS Configuration

The INS should be configured through its web interface to output:

- Protocol: IXBLUE STD BIN (any version between 2 and 5)
- Rate: desired frequency
- Physical Link: Ethernet
- Transport Layer: UDP
- IP: IP of the ROS computer
- Port: 8200

![attachment:network_config_page.png](doc/network_config_page.png)

## Nodes

### ixblue_ins_driver

ROS driver for iXblue inertial sensors supporting stdbin protocol

#### Published Topics

- `ix/ins`
  ([ixblue_ins_msgs/msg/Ins](https://docs.ros.org/en/rolling/p/ixblue_ins_msgs/msg/Ins.html)):
  Inertial and position data using a custom message
- `standard/imu`
  ([sensor_msgs/msg/Imu](https://docs.ros.org/en/rolling/p/sensor_msgs/msg/Imu.html)):
  Standard ROS IMU message containing inertial data
- `standard/navsatfix`
  ([sensor_msgs/msg/NavSatFix](https://docs.ros.org/en/rolling/p/sensor_msgs/msg/NavSatFix.html)):
  GNSS Position of the system in Standard ROS message
- `standard/timereference`
  ([sensor_msgs/msg/TimeReference](https://docs.ros.org/en/rolling/p/sensor_msgs/msg/TimeReference.html)):
  INS time reference

#### Parameters

- `~udp_port` (`string`, default: `8200`): The UDP port from which the
  system will receive INS data.
- `~ip` (`string`, default: `0.0.0.0`): The address of the network
  interface to listen to.
- `~time_source` (`string`, default: `ins`): Determine the source of the
  timestamp data. "ins" for ins timestamp. "ros" for ROS timestamp.
- `~time_origin` (`string`, default: `unix`): Determine the time origin
  of the timestamp. "sensor_default" for ins base time. "unix" for
  UNIX base time (since 1st of january 1970).
