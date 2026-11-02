## Overview

This package provides global map for multiple robots. It can merge maps
from arbitrary number of robots. It expects maps from individual robots
as ROS topics. If your run multiple robots under the same ROS master
then `multirobot_map_merge` will probably work for you out-of-the-box.
It is also very easy to setup an simulation experiment.

![width="755px"](doc/screenshot.jpg)

If your run your robots under multiple ROS masters you need to run your
own way of communication between robots and provide maps from robots on
local topics (under the same master). Also if you want to distribute
merged map back to robots your communication must take care of it.

[Youtube](https://www.youtube.com/watch?v=8Adrn29BVbM&rel=0)

`multirobot_map_merge` does not depend on any particular communication
between robots.

## Architecture

`multirobot_map_merge` finds robot maps dynamically and new robots can
be added to system at any time.

![width="755px"](doc/architecture.svg)

To make this dynamic behaviour possible there are some constrains placed
on robots. First all robots must publish map under
`<robot_namespace>/map`, where topic name (`map`) is configurable,
but must be same for all robots. For each robot `<robot_namespace>`
will be of cause different.

This node support merging maps with known initial positions of the
robots or without. See below for details.

## Merging modes

Two merging modes are currently supported as orthogonal options. If you
know initial positions of robots you may preferably use the first mode
and get exact results (rigid transformation will be computed according
to initial positions). If you don't know robot's starting points you
are still able to use the second mode where transformation between grids
will be determined using heuristic algorithm. You can choose between
these two modes using the `known_init_poses` parameter.

### merging with known initial positions

This is preferred mode whenever you are able to determine exact starting
point for each robot. You need to provide initial position for each
robot. You need to provide set of
`<robot_namespace>/map_merge/init_pose` parameters. These positions
should be in `world_frame`. See
[ROS API](#ros-api).

In this merging these parameters are mandatory. If any of the required
parameters is missing robot won't be considered for merging (you will
get warning with name of affected robot).

### merging without known initial positions

If you can't provide initial poses for robots this mode has minimal
configuration requirements. You need to provide only map topic for each
robot. Transformation between grids is estimated by feature-matching
algorithm and therefore requires grids to have sufficient amount of
overlapping space to make a high-probability match. If grids don't have
enough overlapping space to make a solid match, merged map can differ
greatly from physical situation.

Estimating transforms between grids is cpu-intesive so you might want to
tune `estimation_rate` parameter to run re-estimation less often if it
causes any troubles.

## ROS API

### map_merge

Provides map merging services offered by this package. Dynamically looks
for new robots in the system and merges their maps.

#### Subscribed Topics

- `<robot_namespace>/map`
  ([nav_msgs/msg/OccupancyGrid](https://docs.ros.org/en/rolling/p/nav_msgs/msg/OccupancyGrid.html)):
  Local map for specific robot.
- `<robot_namespace>/map_updates`
  ([map_msgs/msg/OccupancyGridUpdate](https://docs.ros.org/en/rolling/p/map_msgs/msg/OccupancyGridUpdate.html)):
  Local map updates for specific robot. Most of the
  [nav_msgs/msg/OccupancyGrid](https://docs.ros.org/en/rolling/p/nav_msgs/msg/OccupancyGrid.html)
  sources (mapping algorithms) provides incremental map updates via this
  topic so they don't need to send always full map. This topic is
  optional. If your mapping algorithm does not provide this topic it is
  safe to ignore this topic. However if your mapping algorithm does
  provide this topic, it is preferable to subscribe to this topic.
  Otherwise map updates will be slow as all partial updates will be
  missed and map will be able to update only on full map updates.

#### Published Topics

- `map`
  ([nav_msgs/msg/OccupancyGrid](https://docs.ros.org/en/rolling/p/nav_msgs/msg/OccupancyGrid.html)):
  Merged map from all robots in the system.

#### Parameters

##### ROBOT PARAMETERS

Parameters that should be defined in the namespace of each robot if you
want to use merging with known initial poses of robots
(`known_init_poses` is `true`). Without these parameters robots
won't be considered for merging. If you can't provide these parameters
use merging without known initial poses. See
[Merging modes](#merging-modes)

- `<robot_namespace>/map_merge/init_pose_x` (`double`, default:
  `<no_default>`): `x` coordinate of robot initial position in
  `world_frame`. Should be in meters. It does not matter which frame
  you will consider global (preferably it should be different from all
  robots frames), but relative positions of robots in this frame must be
  correct.
- `<robot_namespace>/map_merge/init_pose_y` (`double`, default:
  `<no_default>`): `y` coordinate of robot initial position in
  `world_frame`.
- `<robot_namespace>/map_merge/init_pose_z` (`double`, default:
  `<no_default>`): `z` coordinate of robot initial position in
  `world_frame`.
- `<robot_namespace>/map_merge/init_pose_yaw` (`double`, default:
  `<no_default>`): `yaw` component of robot initial position in
  `world_frame`. Represents robot rotation in radians.

##### NODE PARAMETERS

Parameters that should be defined in the namespace of this node.

- `~robot_map_topic` (`string`, default: `map`): Name of robot map
  topic without namespaces (last component of topic name). Only topics
  with this name will be considered when looking for new maps to merge.
  This topics may be subject to further filtering (see below).
- `~robot_map_updates_topic` (`string`, default: `map_updates`): Name
  of robot map updates topic of
  [map_msgs/msg/OccupancyGridUpdate](https://docs.ros.org/en/rolling/p/map_msgs/msg/OccupancyGridUpdate.html)
  without namespaces (last component of topic name). This topic will be
  always subscribed in the same namespace as `robot_map_topic`.
  You'll likely need to change this only when you changed
  `robot_map_topic`. These topics are never considered when searching
  for new robots.
- `~robot_namespace` (`string`, default: `<empty string>`): Fixed
  part of robot map topic. You can employ this parameter to further
  limit which topics will be considered during dynamic lookup for
  robots. Only topics which contain (anywhere) this string will be
  considered for lookup. Unlike `robot_map_topic` you are not limited
  by namespace logic. Topics will be filtered using text-based search.
  Therefore `robot_namespace` does not need to be ROS namespace, but
  can contain slashes etc. This must be common part of all robots map
  topics name (all robots for which you want to merge map).
- `~known_init_poses` (`bool`, default: `true`): Selects between
  merging modes. `true` if merging with known initial positions. See
  [Merging modes](#merging-modes)
- `~merged_map_topic` (`string`, default: `map`): Topic name where
  merged map will be published.
- `~world_frame` (`string`, default: `world`): Frame id (in
  [tf](https://index.ros.org/p/tf) tree) which will be assigned to
  published merged map. This should be frame where you specified robot
  initial positions.
- `~merging_rate` (`double`, default: `4.0`): Rate in Hz. Basic
  frequency on which this node discovers merges robots maps and publish
  merged map. Increase this value if you want faster updates.
- `~discovery_rate` (`double`, default: `0.05`): Rate in Hz. Frequency
  on which this node discovers new robots. Increase this value if you
  need more agile behaviour when adding new robots. Robots will be
  discovered sooner.
- `~estimation_rate` (`double`, default: `0.5`): Rate in Hz. This
  parameter is relevant only when merging without known positions, see
  [Merging modes](#merging-modes).
  Frequency on which this node re-estimates transformation between
  grids. Estimation is cpu-intensive, so you may wish to lower this
  value.
- `~estimation_confidence` (`double`, default: `1.0`): This parameter
  is relevant only when merging without known positions, see
  [Merging modes](#merging-modes).
  Confidence according to probabilistic model for initial positions
  estimation. Default value 1.0 is suitable for most applications,
  increase this value for more confident estimations. Number of maps
  included in the merge may decrease with increasing confidence.
  Generally larger overlaps between maps will be required for map to be
  included in merge. Good range for tuning is \[1.0, 2.0\].

## Acknowledgements

This package was developed as part of my bachelor thesis at
[Charles University](http://www.mff.cuni.cz/to.en/) in Prague.



```
@masterthesis{Hörner2016,
  author = {Jiří Hörner},
  title = {Map-merging for multi-robot system},
  address = {Prague},
  year = {2016},
  school = {Charles University in Prague, Faculty of Mathematics and Physics},
  type = {Bachelor's thesis},
  URL = {https://is.cuni.cz/webapps/zzp/detail/174125/},
}
```



Idea for dynamic robot discovery is from [map_merging](map_merging)
package from Zhi Yan. Merging algorithm and configuration are different.
