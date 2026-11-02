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

=== marker_server ===

Serve interactive markers for control of a robot drive base.

==== Published Topics ====

 * {{{cmd_vel
```


([geometry_msgs/msg/Twist](https://docs.ros.org/en/rolling/p/geometry_msgs/msg/Twist.html)):
Command velocity messages arising from markers usage. Messages are not
published when the markers are idle.

#### Parameters

- `~link_name` (`str`, default: `/base_link`): Name of frame to attach
  the markers to; typically will be `base_link` or `base_footprint`.
- `~robot_name` (`str`, default: `robot`): Single-word name for the
  robot, to use in labelling the controller.
- `~marker_size_scale` (`double`, default: `1.0`): Scale the size of the
  markers, for platforms especially large or small.

}}}}

## Roadmap

Package is **experimental**. Please see the feature tracker for planned
enhancements.
