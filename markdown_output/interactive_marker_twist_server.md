## Overview

The purpose of this package is to provide a basic generic marker server
for teleoperation of twist-based robots, particularly simple
differential drive bases. Examples of such platforms include
[TurtleBot](Robots/TurtleBot), [Husky](Robots/Husky), and
[Kingfisher](Robots/Kingfisher).

## API

{ }}}}



```
{#!wiki version indigo_and_newer
{{{
#!clearsilver CS/NodeAPI
name=marker_server
desc=Serve interactive markers for control of a robot drive base.
pub {
  0.name = cmd_vel
  0.type = geometry_msgs/Twist
  0.desc = Command velocity messages arising from markers usage. Messages are not published when the markers are idle.
}
param {
  0.name = ~link_name
  0.type = str
  0.desc = Name of frame to attach the markers to; typically will be `base_link` or `base_footprint`.
  0.default = /base_link
  1.name = ~robot_name
  1.type = str
  1.desc = Single-word name for the robot, to use in labelling the controller.
  1.default = robot
  2.name = ~marker_size_scale
  2.type = double
  2.desc = Scale the size of the markers, for platforms especially large or small.
  2.default = 1.0
}
```

 }}}}

## Roadmap

Package is **experimental**. Please see the feature tracker for planned
enhancements.
