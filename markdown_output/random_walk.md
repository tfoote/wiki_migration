## Overview

This package contains an implementation of a random walk algorithm based
on the navigation stack. The algorithm generates a random cell inside
the map, checks if the cell is not an obstacle or too close to one, and
sends the robot there.

## ROS API

```clearsilver
node.0 {
name=random_walk
desc=`random_walk` is navigation stack based random walk algorithm.
sub{
0.name= map
0.type= nav_msgs/OccupancyGrid
0.desc= The global map.
1.name= move_base/local_costmap/obstacles
1.type= nav_msgs/GridCells
1.desc= Obstacles.
2.name= move_base/local_costmap/inflated_obstacles
2.type= nav_msgs/GridCells
2.desc= Inflated obstacles.
2.name= /visited_cells
2.type= nav_msgs/GridCells
2.desc= Visited cells from particle_plume.
}
param {
0.name= move_base/local_costmap/inflation_radius
0.default= 0.20
0.type= double
0.desc= The inflation radius used by the navigation stack.
}
}
```
