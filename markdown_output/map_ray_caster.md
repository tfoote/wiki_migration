`map_ray_caster` provides a cached ray casting on a map, such as those
provided by `local_map` of the Large Maps Framework
([LaMa](Large Maps Framework)).

## Overview

`map_ray_caster` provides a cached ray casting on a map, such as those
provided by `local_map`. The origin of all rays is fixed relative to
the map, it is the map center. It takes as input a costmap
(<<SrvLink(nav_msgs/OccupancyGrid)>>) and returns a laser scan
(<<SrvLink(sensor_msgs/LaserScan)>>). The ray casting will be from
`scan.angle_min` to `scan.angle_max`. Moreover, other value of the
input scan are used so that the scan message must be initialized with
non-default values.

## Usage

To use the `map_ray_caster::MapRayCaster` class to compute a fake
<<SrvLink(sensor_msgs/LaserScan)>> from an occupancy grid in C++:


```cplusplus
#include <map_ray_caster/map_ray_caster.h>

map_ray_caster::MapRayCaster ray_caster;  //!> Ray casting with cache to compute a fake LaserScan.

nav_msgs::OccupancyGrid map;
map.frame_id = "map_frame";

sensor_msgs::LaserScan scan;
scan.angle_min = -M_PI_2;
scan.angle_max = M_PI_2;
scan.angle_increment = (scan.angle_max - scan.angle_min) / (720 - 1);
scan.range_max = 10;
scan.header = map.header;
scan.header.frame_id = "laser_frame";
ray_caster.laserScanCast(map, scan);
```


