# Package Summary

A package that provides current position and orientation of the robot in
the map.

-   Author: Zhi Yan
-   License: BSD
-   Source: git <https://github.com/yzrobot/pose_publisher.git> (branch:
    master)

## About

The `pose_publisher` package contains a ROS node that provides current
position and orientation of the robot in the map. This package can be
used in multi-robot systems.

## Nodes



```clearsilver
node.0 {
  name = pose_publisher
  desc = `pose_publisher` provides the current position and orientation of the robot in the map.
  pub {
    0.name = /pose
    0.type = geometry_msgs/PoseStamped
    0.desc = Current robot pose.
  }
  param {
    0.name = ~publish_frequency
    0.type = double
    0.desc = Frequency (hz) at which to publish the robot pose.
    0.default = 10.0
    1.name = ~map_frame
    1.type = std::string
    1.desc = The frame attached to the map.
    1.default = map
    2.name = ~base_frame
    2.type = std::string
    2.desc = The frame attached to the mobile base.
    2.default = base_link
  }
}
```



## Usage



```
rosrun pose_publisher pose_publisher
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
