The *explorer package* utilizes frontier based exploration to discover
environments autonomously operating a distributed multi-robot system.
Beside frontier detection, coordinated and uncoordinated exploration
strategies are available to select goal points. Coordinated exploration
enhances robot distribution and reduces redundancy in exploration which
result in improvement of efficiency in terms of exploration time.

## Overview

The *explorer package* comprises multiple functionalities to perform
frontier based exploration. Frontier detection is utilized on local and
global costmaps to further select navigation goals in the environment to
proceed with exploration. The assignment of robots to goals is
accomplished according to coordinated and uncoordinated exploration
strategies being applied for the distributed multi-robot system.

Auctioning thereby ensures negotiation among available goals to
coordinate efficiently, distributing robots among the environment by
minimizing the overall travel path. Additionally to frontier detection
and selection, the *explorer package* is concerned with navigation to
goal points by incorporating a simple action client utilizing
*move_base*.

## Exploration

Frontier based exploration is available for single and multi-robot
systems. The exploration package is capable to operate in Simulation,
e.g. Stage, but also to be deployed on a real robot system, e.g.
Turtlebots and Pioneers. Additionally, coordinated robots comprise
multiple frontiers as clusters to spatially interrelate groups of
frontiers. Hence, multi-robot distribution is improved and number of
participating goals, e.g. clusters, is narrowed. As a consequence,
robots auction among clusters, implying less effort to negotiate a
narrowed subset of elements.

### Single Robot Exploration

As a single robot explores, communicational capabilities are irrelevant
and exploration strategy is uncoordinated. Frontiers are therefore
detected and selected according to \"Nearest Frontier\" strategy. The
following video depicts single robot exploration utilizing Stage and
\"Nearest Frontier\" strategy. Robots detect frontiers and represent
them accordingly as red spheres in RVIZ, indicating selected frontiers
as pink sphere.

\<\<Youtube(5mU1wE69z3I?rel=0)\>\>

### Multi Robot Exploration

As a multi-robot exploration is assumed, robots maintaining a
communication link to each other are capable to coordinate on cluster
level. Thus, efficiency of exploration is increased as multiple robots
distribute among the environment to explore different areas. Such a
coordinated approach is depicted in the following video, utilizing two
robots to decrease exploration time. Further, available clusters are
represented by underlying frontiers with different colors. In the video,
two robots explore an environment emulated by Stage, where one robot is
depicted in RVIZ visualizing clusters, frontiers and selected goal
points.

\<\<Youtube(md29t2Xbdug?rel=0)\>\>

## Related Documentation

Please refer to the following paper to retrieve more information on the
node: ```
{
@InProceedings{Andre2014,
  Title                    = {Coordinated Multi-Robot Exploration: Out of the Box Packages for {ROS}},
  Author                   = {Andre, T. and Neuhold, D. and Bettstetter, C.},
  Booktitle                = {Proc. of IEEE GLOBECOM WiUAV Workshop},
  Year                     = {2014},
  Month                    = dec,
}
```} You may obtain the paper from
[IEEEXplore](http://ieeexplore.ieee.org/) or search in
[Google Scholar](http://scholar.google.at/scholar?q=Coordinated+Multi-Robot+Exploration%3A+Out+of+the+Box+Packages+for+ROS&hl=de&btnG=Suche&lr=).

## ROS API

```clearsilver
name = Exploration Package
desc = The explorer package publishes multiple topics to depict frontiers, clusters and goal points in RVIZ and to coordinate among multiple other robots participating in exploration. Further, required topics to be subscribed are listed.
sub {
  0.name = ~<name>/map_merger/global_map
  0.type = nav_msgs/OccupancyGrid
  0.desc = Global map is utilized to detect frontiers at the entire environment. As multiple robots are operated, a global map is published by the map_merger node, incorporating explored areas from all robots.
  1.name = ~<name>/base_scan
  1.type = sensor_msgs/LaserScan
  1.desc = Data being send on this topic, are required to create a map and published by the laser scanner.
  2.name = ~<name>/frontiers
  2.type = adhoc_communication/ExpFrontier
  2.desc = Topic to exchange frontiers being detected by multiple robots.
  3.name = ~<name>/visited_frontiers
  3.type = adhoc_communication/ExpFrontier
  3.desc = Topic to exchange frontiers being previously selected by a robot as navigation goal.
  4.name = ~<name>/negotiation_list
  4.type = adhoc_communication/ExpFrontier
  4.desc = Negotiation list might be used to negotiate among frontiers in the environment to avoid multiple robots selecting an identical frontier.
  5.name = ~<name>/auction
  5.type = adhoc_communication/ExpAuction
  5.desc = Topic to auction frontiers. Auction messages are exchanged on this topic.
  6.name = ~<name>/all_positions
  6.type = adhoc_communication/MmListOfPoints
  6.desc = Topic used to exchange positions of all robots in the environment.
}
pub {
  0.name = ~<name>/visitedfrontierPoints
  0.type = visualization_msgs/MarkerArray
  0.desc = Visited frontier points are published on this topic to visualize them in RVIZ.
  1.name = ~<name>/goalPoint
  1.type = geometry_msgs/PointStamped
  1.desc = Goal points are published on this topic to visualize them in RVIZ.
  2.name = ~<name>/frontierPoints
  2.type = visualization_msgs/MarkerArray
  2.desc = Frontiers points are published on this topic to visualize them in RVIZ.
  3.name = ~<name>/cluster_grid_~
  3.type = nav_msgs/GridCells
  3.desc = Topic to publish GridCells, indicating which cluster a frontier belongs.
}
srv {
  0.name = ~<name>/adhoc_communication/send_frontier
  0.type = adhoc_communication/SendExpFrontier
  0.desc = Service to disseminate frontiers among all robots operating.
  1.name = ~<name>/adhoc_communication/send_auction
  1.type = adhoc_communication/SendExpAuction
  1.desc = Service to disseminate auctioning messages among all robots operating.
}
param {
  0.name = ~<name>/frontier_selection
  0.type = int
  0.desc = Select exploration strategy. 0 indicates uncoordinated exploration, where 1 indicates coordinated exploration. As coordinated exploration is chosen, operating a single robot, communicational capabilities are unused and strategy is identical to uncoordinated exploration.
  0.default = 1
  1.name = ~<name>/local_costmap/width
  1.type = int
  1.desc = Set the size of the local costmap to detect frontiers. The local costmap is centered at the robot and detects frontiers within its range.
  1.default = 8
  2.name = ~<name>/number_unreachable_for_cluster
  2.type = int
  2.desc = Number of selected frontiers within a cluster, which are unreachable before neglecting the cluster as further navigation goal.
  2.default = 3
}
```
