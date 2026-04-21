# Package Summary

A package that decomposes the `/tf` topic into multiple ones.

-   Author: Zhi Yan
-   License: BSD
-   Source: git <https://github.com/yzrobot/tf_splitter.git> (branch:
    master)

## About

The `tf_splitter` package contains a ROS node that decomposes the
`/tf` topic into multiple ones according to the number of robots. This
package can be used in multi-robot systems to alleviate the network
traffic load.

## Nodes

```clearsilver
node.0 {
  name = tf_splitter
  desc = `tf_splitter` decomposes the `/tf` topic into multiple ones according to the number of robots.
  sub {
    0.name = /tf
    0.type = tf/tfMessage
    0.desc = Transform tree.
  }
  pub {
    0.name = /<tf prefix according to the robots>
    0.type = tf/tfMessage
    0.desc = Splitted transform tree.
  }
}
```

## Usage

```
rosrun tf_splitter tf_splitter
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
