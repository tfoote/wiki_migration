## Overview

This package provides a method for construction of a 3D representation
of sensed data that we label a \'\'\'collision_map\'\'\'. A collision
map is a set of boxes whose extents and orientation is specified. It is
typically generated using point-cloud data from laser range sensors,
stereo cameras and other 3-D sensing devices.

Note: This node requires input of type PointCloud. If using an OpenNI
device that outputs only PointCloud2, you should look at
[collider](collider) or [octomap_server](octomap_server) instead.

### Collision map with self occlusions

This particular type of collision map is an implementation of an
occupancy grid for the environment of the robot which also contains
points from the previous world views, if they have become occluded by
robot links. The example in the picture shows the collision map after
part of it has been occluded by the arm (in red).

[![\|width=640](attachment:collision_map_self_occ.png)](attachment:collision_map_self_occ.png)

## ROS API

### API Stability

-   ROS API is UNREVIEWED and UNSTABLE
-   C++ API is UNREVIEWED and UNSTABLE
