![width=400](doc/ROSaic_noborder.png)

## Overview

This Wiki page facilitates the installation, configuration and usage of
ROSaic for people in the robotics and autonomous vehicle communities.
The C++ driver can be used with the Septentrio family of mosaic
receivers (e.g.
[mosaic-x5](https://www.septentrio.com/en/products/gnss-receivers/rover-base-receivers/receivers-module/mosaic),
[mosaic-H](https://www.septentrio.com/en/products/gnss-receivers/gnss-modules/mosaic-h))
and is also usable with other Septentrio GNSS or event GNSS/INS
receivers (e.g.
\[\[<https://www.septentrio.com/en/products/gnss-receivers/oem-receiver-boards/asterx-m3-pro-plus%7CAsteRx-m3>
\],
<https://www.septentrio.com/en/products/gnss-receivers/rover-base-receivers/integrated-gnss-receivers/asterxsb>,
\[\[<https://www.septentrio.com/en/products/gnss-receivers/gnss-ins-ruggedized-boxes/asterx-sbi3-pro-plus>
\|AsteRx-SBi3\] and others).

## About Septentrio

![](https://www.septentrio.com/themes/custom/septentrio/logo.png)

Septentrio designs, manufactures and sells high-precision,
multi-frequency, multi-constellation GPS/GNSS equipment for use in
demanding applications. Septentrio products are used in a wide variety
of industries including marine, construction, precision agriculture,
logistics, machine control, rail, automotive, survey and mapping,
geographic information systems (GIS), unmanned aerial vehicles (UAVs)
and scientific. Septentrio receivers deliver consistently accurate and
precise GNSS positioning scalable to centimeter-level and designed to
perform solidly in the most challenging environments. Septentrio
receivers are available as OEM boards, housed receivers and smart
antennas.

The technology offers high accuracy and reliability thanks to GNSS+
algorithms as well as
[Septentrio's Advanced Interference Monitoring and Mitigation (AIM+)](https://www.septentrio.com/en/advanced-interference-monitoring-mitigation-aim)
which protects against RF interference (jamming) and spoofing.

For more information about Septentrio products go to
[http:\\\\www.septentrio.com](http:\\www.septentrio.com)

## ROSaic = ROS + mosaic

ROSaic is a C++ driver for Septentrio's mosaic receivers and beyond.
This ROS package publishes
[sensor_msgs/NavSatFix](https://docs.ros.org/melodic/api/sensor_msgs/html/msg/NavSatFix.html),
[gps_common/GPSFix](https://docs.ros.org/melodic/api/gps_common/html/msg/GPSFix.html)
and
[geometry_msgs/PoseWithCovarianceStamped.msg](https://docs.ros.org/melodic/api/geometry_msgs/html/msg/PoseWithCovarianceStamped.html)
messages. The same ROSaic node also allows subscription to a set of
common NMEA sentences - conforming to the NMEA standard NMEA 0183 - as
well as to a range of proprietary Septentrio Binary Format (SBF)
messages. User-specific ROSaic parameters enable the configuration of
differential correction services via NTRIP for a variety of hardware
setups.

## Additional Support for ROSaic Users

- Go to [Septentrio Support page](https://www.septentrio.com/en/support)
  for further documentation of Septentrio GNSS receivers.
