## Overview

This package provides a ROS interface for GPS devices that output
compatible NMEA sentences. See the
[GPSD documentation of NMEA sentences](http://www.catb.org/gpsd/NMEA.html)
for details on the raw format. Of the thousands of NMEA-compatible GPS
devices, we are compiling a list of
[devices known to be supported](nmea_navsat_driver/SupportedHardware).

This package is compatible with the [geographic_info](geographic_info)
project as well as any other nodes that support
[sensor_msgs/msg/NavSatFix](https://docs.ros.org/en/rolling/p/sensor_msgs/msg/NavSatFix.html)
and/or
[sensor_msgs/msg/TimeReference](https://docs.ros.org/en/rolling/p/sensor_msgs/msg/TimeReference.html).

No C++ or Python API is provided, only a ROS API.

This package replaces the [nmea_gps_driver](nmea_gps_driver) package
present in Fuerte and Groovy.

## Sample Usage

To get up and running quickly, you can use the following command to
start outputting your GPS data onto ROS topics. This assumes your GPS is
outputting GGA NMEA sentences, is connected to `/dev/ttyUSB0` and is
communicating at 38400 baud.



```
$ rosrun nmea_navsat_driver nmea_serial_driver _port:=/dev/ttyUSB0 _baud:=38400
```



## Roadmap

- Add support for additional NMEA sentences beyond GSA, RMC and GGA.
  Specific requests for support of individual sentences should be filed
  as enhancement tickets.
- Add sentence synchronization. Currently, there is little or no
  buffering, which prevents the driver from using multiple types of
  sentences to generate one cycle of topic outputs.

## Nodes



```clearsilver
node.0 {
 name = nmea_topic_driver
 desc = NMEA GPS Topic driver node. Reads NMEA sentences from a ROS topic instead of directly from e.g. a serial port.
 sub{
  0.name = nmea_sentence
  0.type = nmea_msgs/Sentence
  0.desc = NMEA sentences, 1 per message. The header.stamp should correspond to the time that the message was read from the device for accurate time_reference output. The header.frame_id on the messages on this topic will be used when setting frame_id on the output messages. These sentences do not have to be checksummed or otherwise validated before reaching the driver.
 }
 pub{
  0.name = fix
  0.type = sensor_msgs/NavSatFix
  0.desc = GPS position fix reported by the device. This will be published with whatever positional and status data was available even if the device doesn't have a valid fix. Invalid fields may contain !NaNs.
  1.name = vel
  1.type = geometry_msgs/TwistStamped
  1.desc = Velocity output from the GPS device. Only published when the device outputs valid velocity information. The driver does not calculate the velocity based on only position fixes.
  2.name = time_reference
  2.type = sensor_msgs/TimeReference
  2.desc = The timestamp from the GPS device is used as the `time_ref`.
  }
 param {
  1.name = ~time_ref_source
  1.default = <the value of ~frame_id>
  1.type = string
  1.desc = The value to use as the source in the <<MsgLink(sensor_msgs/TimeReference messages)>>.
  2.name = ~useRMC
  2.default = False
  2.type = bool
  2.desc = Whether to generate position fixes from GGA sentences or RMC sentences. If `True`, fixes will be generated from RMC. If `False`, fixes will be generated based on the GGA sentences. Using GGA sentences allows for approximated covariance output while RMC provides velocity information.
  }
 }
node.1 {
 name = nmea_serial_driver
 desc = NMEA GPS Serial driver node. Replaces nmea_gps_driver.py to reduce naming conflicts and use new common parsing+driver backend.
 pub{
  0.name = fix
  0.type = sensor_msgs/NavSatFix
  0.desc = GPS position fix reported by the device. This will be published with whatever positional and status data was available even if the device doesn't have a valid fix. Invalid fields may contain !NaNs.
  1.name = vel
  1.type = geometry_msgs/TwistStamped
  1.desc = Velocity output from the GPS device. Only published when the device outputs valid velocity information. The driver does not calculate the velocity based on only position fixes.
  2.name = time_reference
  2.type = sensor_msgs/TimeReference
  2.desc = The timestamp from the GPS device is used as the `time_ref`.
  }
 param {
  0.name = ~port
  0.default = /dev/ttyUSB0
  0.type = string
  0.desc = The device path
  1.name = ~baud
  1.default = 4800
  1.type = int
  1.desc = The baud rate to receive NMEA data.
  2.name = ~frame_id
  2.default = gps
  2.type = string
  2.desc = The `frame_id` for the header of the <<MsgLink(sensor_msgs/NavSatFix)>> and <<MsgLink(geometry_msgs/TwistStamped)>> output messages. Will be resolved with `tf_prefix` if defined.
  3.name = ~time_ref_source
  3.default = <the value of ~frame_id>
  3.type = string
  3.desc = The value to use as the source in the <<MsgLink(sensor_msgs/TimeReference messages)>>.
  4.name = ~useRMC
  4.default = False
  4.type = bool
  4.desc = Whether to generate position fixes from GGA sentences or RMC sentences. If `True`, fixes will be generated from RMC. If `False`, fixes will be generated based on the GGA sentences. Using GGA sentences allows for approximated covariance output while RMC provides velocity information.
  }
 }
node.3 {
 name = nmea_topic_serial_reader
 desc = Reads NMEA sentences from the specified serial port and publishes them to a ROS topic. This is a simple front-end for use with nmea_topic_driver.py
 pub{
  0.name = nmea_sentence
  0.type = nmea_msgs/Sentence
  0.desc = A single time-stamped NMEA sentence captured from the serial device
  }
 param {
  0.name = ~port
  0.default = /dev/ttyUSB0
  0.type = string
  0.desc = The device path
  1.name = ~baud
  1.default = 4800
  1.type = int
  1.desc = The baud rate to receive NMEA data.
  2.name = ~frame_id
  2.default = gps
  2.type = string
  2.desc = The `frame_id` for the header of the <<MsgLink(nmea_msgs/Sentence)>> and output message. Will be resolved with `tf_prefix` if defined.
  }
 }
```



## Troubleshooting

If you are using this package for the first time and encountering
problems you should first check that the package installed correctly and
in the right location. Then consult
[ROS/Troubleshooting](ROS/Troubleshooting), [FAQ](FAQ) and
<http://answers.ros.org/questions/> to see if a solution has already
been identified for your problem.

If you are having trouble with nmea_serial_driver and connecting to a
serial port, ensure that the user has permission to access the port by
checking to see if the user is part of the "dialout" group. See
[here](http://answers.ros.org/question/231957/connection-issue-using-nmea_serial_driver/?answer=231961#post-id-231961)
for more information.

## Report a Bug
