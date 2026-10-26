

```wiki
'''''[[rtabmap_ros]]:''' [[rtabmap]] | [[rtabmap_conversions]] | [[rtabmap_costmap_plugins]] | [[rtabmap_demos]] | [[rtabmap_examples]] | [[rtabmap_launch]] | [[rtabmap_legacy]] | [[rtabmap_msgs]] | [[rtabmap_odom]] | [[rtabmap_python]] | [[rtabmap_rviz_plugins]] | [[rtabmap_slam]] | [[rtabmap_sync]] | [[rtabmap_util]] | [[rtabmap_viz]]''
```



## Overview

RTAB-Map (Real-Time Appearance-Based Mapping) is a RGB-D Graph SLAM
approach based on a global Bayesian loop closure detector. The loop
closure detector uses a bag-of-words approach to determinate how likely
a new image comes from a previous location or a new location. When a
loop closure hypothesis is accepted, a new constraint is added to the
map's graph, then a graph optimizer minimizes the errors in the map. A
memory management approach is used to limit the number of locations used
for loop closure detection and graph optimization, so that real-time
constraints on large-scale environnements are always respected. RTAB-Map
can be used alone with a handheld Kinect or stereo camera for 6DoF RGB-D
mapping, and/or on a robot equipped with a laser rangefinder for 3DoF
mapping (2D LiDAR) and 6DoF mapping (3D LiDAR).

[Youtube](https://www.youtube.com/watch?v=o1GSQanY-Do)

Visit [rtabmap_ros](rtabmap_ros) to know how to use RTAB-Map under ROS.
The [rtabmap](rtabmap) package is only for convenient release of the
RTAB-Map libraries and standalone application. Visit
[RTAB-Map's wiki](https://github.com/introlab/rtabmap/wiki) to know how
to use the standalone application and
[tools](https://github.com/introlab/rtabmap/wiki/Tools) that come with
this package: 

```
$ rtabmap
```



## Citing

If you use [rtabmap](rtabmap) in academic context, please cite the
appropriate publication from <http://introlab.github.io/rtabmap>
