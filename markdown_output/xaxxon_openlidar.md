## Overview

**Xaxxon OpenLIDAR **is an open hardware rotational laser scanner, using
the Garmin LIDAR-!LiteV3 sensor. Full specs and complete documentation
can be found at
[xaxxon.com/xaxxon/openlidar](http://www.xaxxon.com/xaxxon/openlidar)

![](http://www.xaxxon.com/images/xaxxon/openlidar/xaxxon_openlidar_sensor.jpg)
![](http://www.xaxxon.com/images/xaxxon/openlidar/xaxxon_openlidar_rear_iso.jpg)
![](http://www.xaxxon.com/images/xaxxon/openlidar/rvizopenlidar.jpg)

## Node

### lidarbroadcast.py

. Python driver for OpenLIDAR. Searches USB ports for connected sensor,
automatically starts the motor and range broadcast, converting the data
stream into a <<MsgLink(sensor_msgs/LaserScan)>> message. Each
message contains data from a single full revolution.

#### Published Topic

. `/scan` (<<MsgLink(sensor_msgs/LaserScan)>>) . using TF frame ID
"laser_frame"

#### Subscribed Topic

. `/odom` (<<MsgLink(nav_msgs/Odometry)>>) . OPTIONAL - used by
`dropscan_turnrate` parameter

#### Parameters

. `minimum_range` (double, default 0.5) . minimum output for laser
sensor, meters

. `maximum_range` (double, default 40.0) . maximum output for laser
sensor, meters

. `rpm` (integer, default 180) . revolution speed for lidar motor,
revs per minute

. `masks` (string) . frame masks CW/RHR+ start-mask/stop-mask pairs,
degrees 0-360, space separated

. `dropscan_turnrate` (integer, default 0) . blank scans when
exceeding mobile base odom yaw rate, deg per sec, 0 to disable . Ignored
if `/odom` topic unavailable

. `park_offset` (double, default 180.0) . sensor park (stop-position)
offset from photo sensor, degrees

. `forward_offset` (double, default 189.0) . scan header offset from
photo sensor, degrees

. `read_frequency` (double, default 715.0) . sensor read frequency, Hz

## More Info

Full specs and complete documentation can be found at
[xaxxon.com/xaxxon/openlidar](http://www.xaxxon.com/xaxxon/openlidar)
