## Supported Hardware

This driver supports all iXblue inertial sensors outputing stdbin
protocol like the
[Atlans](https://www.ixblue.com/products/atlans-series) and
[Phins Compact](https://www.ixblue.com/products/phins-compact-series)
series.

![](attachment:atlans.png)

## INS Configuration

The INS should be configured through its web interface to output:

-   Protocol: IXBLUE STD BIN (any version between 2 and 5)
-   Rate: desired frequency
-   Physical Link: Ethernet
-   Transport Layer: UDP
-   IP: IP of the ROS computer
-   Port: 8200

![](attachment:network_config_page.png)

## Nodes

```clearsilver
name = ixblue_ins_driver
desc = ROS driver for iXblue inertial sensors supporting stdbin protocol
pub {
  0.name = ix/ins
  0.type = ixblue_ins_msgs/Ins
  0.desc = Inertial and position data using a custom message

  1.name = standard/imu
  1.type = sensor_msgs/Imu
  1.desc = Standard ROS IMU message containing inertial data

  2.name = standard/navsatfix
  2.type = sensor_msgs/NavSatFix
  2.desc = GNSS Position of the system in Standard ROS message

  3.name = standard/timereference
  3.type = sensor_msgs/TimeReference
  3.desc = INS time reference
}
param {
  0.name = ~udp_port
  0.type = string
  0.desc = The UDP port from which the system will receive INS data.
  0.default = 8200

  1.name = ~ip
  1.type = string
  1.desc = The address of the network interface to listen to.
  1.default = 0.0.0.0

  2.name = ~time_source
  2.type = string
  2.desc = Determine the source of the timestamp data. "ins" for ins timestamp. "ros" for ROS timestamp.
  2.default = ins

  3.name = ~time_origin
  3.type = string
  3.desc = Determine the time origin of the timestamp. "sensor_default" for ins base time. "unix" for UNIX base time (since 1st of january 1970).
  3.default = unix
}
```
