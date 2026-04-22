## Overview

The `dfs_explorer` package implements the node `explorer.py` which
is an explorer with depth-first-search-like algorithm for finite worlds
for the Large Maps Framework ([LaMa](Large Maps Framework)). It proceeds
as follows: 0. Go to the first crossing (for example, jockey
[nj_laser](nj_laser) or [nj_costmap](nj_costmap)). 1. Get a new
[lama_msgs/msg/Crossing](https://docs.ros.org/en/rolling/p/lama_msgs/msg/Crossing.html)
descriptor (robot should be at crossing center), compare this descriptor
with descriptors saved in the map, and add a new vertex in the case that
the place is considered to be a place that was not already visited. If,
on the opposite, the vertex is an already visited one, add an edge to
the map and associate as a descriptor, the angle of the exit that was
taken to reach this node from the previous node. This implies using a
localizing jockey (for example, jockey [lj_laser](lj_laser) or
[lj_costmap](lj_costmap)). 2. Choose the next exit to visit with a
preference to visiting an exit of the vertex at which the robot
currently is. 3. Move to that vertex, if necessary (for example, with a
combination of [nj_escape_crossing](nj_escape_crossing) and either
[nj_laser](nj_laser) or [nj_costmap](nj_costmap)). 4. Let the robot
escape from the node in the chosen direction (for example with jockey
[nj_escape_crossing](nj_escape_crossing)). The edge does not exists yet,
set the direction through a topic. 5. Move to the next crossing (for
example, jockey [nj_laser](nj_laser) or [nj_costmap](nj_costmap)). 6.
Repeat from step 1. until all vertices and all exits are visited.

## Usage

A test launch file can be found in the [lama_test](lama_test) package:


```shell
roslaunch lama_test test_dfs_explorer.launch
```


