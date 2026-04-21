# Package Summary

A package that provides a node for merging multiple maps with knowledge
of the initial relative positions of robots.

-   Author: Zhi Yan
-   License: BSD
-   Source: git <https://github.com/yzrobot/map_merging.git> (branch:
    master)

## About

The map_merging package contains a ROS node that merges multiple maps
with knowledge of the initial relative positions of robots.

## Nodes



```clearsilver
node.0 {
  name = map_merging
  desc = `map_merging` merges multiple maps with knowledge of the initial relative positions of robots.
  sub {
    0.name = map
    0.type = nav_msgs/OccupancyGrid
    0.desc = map.
    1.name = pose
    1.type = geometry_msgs/PoseStamped
    1.desc = pose.
  }
  pub {
    0.name = ~map
    0.type = nav_msgs/OccupancyGrid
    0.desc = merged map.
  }
  param {
    0.name = ~max_comm_distance
    0.type = double
    0.desc =  The maximum distance feasible for the communication between robots.
    0.default = 10.0
  }
}
```



## Related Documentation

Please refer to the following paper to retrieve more information on the
node: 

```
@inproceedings{yz14simpar,
author = {Zhi Yan and Luc Fabresse and Jannik Laval and Noury Bouraqadi},
title = {Team Size Optimization for Multi-robot Exploration},
booktitle = {In Proceedings of the 4th International Conference on Simulation, Modeling, and Programming for Autonomous Robots (SIMPAR 2014)},
pages = {438--449},
address = {Bergamo, Italy},
month = {October},
year = {2014}
}
```



## Support

Zhi Yan, Luc Fabresse, Jannik Laval, and Noury Bouraqadi

Ecole des Mines de Douai, 59508 Douai, France

<http://car.mines-douai.fr>
