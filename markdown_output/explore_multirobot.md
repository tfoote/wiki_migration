# Package Summary

This is a multi-robot version of the
[explore](http://wiki.ros.org/explore) package.

-   Author: Zhi Yan
-   License: BSD
-   Source: git <https://github.com/yzrobot/explore_multirobot.git>
    (branch: master)

## About

The \`explore_multirobot\` package is a multi-robot version of the
[explore](http://wiki.ros.org/explore) package. It can additionally
subscribe to external topics such as map and goal, and publish messages
about distance traveled and estimated cost.

## Nodes

```clearsilver
node.0 {
  name = explore_multirobot
  desc = `explore_multirobot` provides support for multi-robot systems.
  sub {
    0.name = map
    0.type = nav_msgs/OccupancyGrid
    0.desc = External map.
    1.name = goal
    1.type = move_base_msgs/MoveBaseGoal
    1.desc = External goal.
  }
  pub {
    0.name = ~distance_traveled
    0.type = std_msgs/Float64
    0.desc = Distance traveled in real-time of the robot.
    1.name = ~estimated_cost
    1.type = std_msgs/Float64
    1.desc = Estimated cost for task allocation (currently using Euclidean distance).
  }
  param {
    0.name = ~inscribed_scale
    0.type = double
    0.desc =  How big is enough the frontier for the robot to fit through.
    0.default = 1.0
  }
}
```

## Related Documentation

Please refer to the following paper to retrieve more information on the
node: ```
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
