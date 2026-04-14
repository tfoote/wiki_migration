## Overview

PPExplorer is a an odor oriented exploration algorithm that builds on
top of the odor mapping package [particle_plume](particle_plume).

The PPE algorithm is in charge of odor oriented exploration and plume
tracking. This is accomplished in four steps. (1) Initially a circle of
radius r is drawn around the robot and divided into n slices. (2) Next
the slices which overlap with obstacles are removed. (3) The slices
which contain a percentage of explored area over a certain threshold are
then also removed. (4) Finally the cost of each remaining slice is
calculated using a cost function. The slice with the lowest cost is
chosen and the goal is set. The variables used fore the cost function
are the amount of explored area, the angular distance to the odor
gradient and the angular distance to the current heading of the robot.

![\|width=100%](attachment:ppexplorer.jpg)

## ROS API

```clearsilver
node.0 {
name=pp_explorer_node
desc=`pp_explorer_node` is an odor oriented exploration and plume tracking algorithm.
pub{
0.name= debug_cells
0.type= nav_msgs/GridCells
0.desc= This allows to visually debug the slices.

1.name= pp_goal
1.type= visualization_msgs/Marker
1.desc= This allows to visually debug the goals.
}
sub{
0.name= odom
0.type= nav_msgs/Odometry
0.desc= Robot odometry.

1.name= /map
1.type= nav_msgs/OccupancyGrid
1.desc= Global map.

2.name= /map_metadata
2.type= nav_msgs/MapMetaData
2.desc= Global map metadata.

3.name= /visited_cells
3.type= nav_msgs/GridCells
3.desc= Visited cells from particle_plume.

4.name= /plume
4.type= sensor_msgs/PointCloud2
4.desc= The odor plume from particle_plume.

5.name= move_base/local_costmap/obstacles
5.type= nav_msgs/GridCells
5.desc= Obstacles from the navigation stack.

6.name= move_base/local_costmap/inflated_obstacles
6.type= nav_msgs/GridCells
6.desc= Inflated obstacles from the navigation stack.
}
param {
0.name= ~global_frame_id
0.default= map
0.type= string
0.desc= The global frame id.

1.name= ~max_visited_cells_coef
1.default= 0.35
1.type= double
1.desc= The maximum visited cells coefficient allowed for a slice to be considered. This must be a value between 0 and 1.

2.name= ~max_odor_visited_cells_coef
2.default= 0.50
2.type= double
2.desc= The maximum visited cells coefficient allowed for a slice to be considered when odor is present. This must be a value between 0 and 1.

3.name= ~pie_radius
3.default= 0.60
3.type= double
3.desc= The radius of the pie laid around the robot.

4.name= ~pie_slices
4.default= 16
4.type= int
4.desc= The number of slices inside the pie. This value cannot be lower than 4.

5.name= ~find_clearing_sim_steps
5.default= 3
5.type= int
5.desc= The number of simulations pp_explorer must be able to successfully complete to set a goal during the recovery behavior.

6.name= ~visited_cells_weight
6.default= 1.00
6.type= double
6.desc= The weight given to the visited cells in the cost function.

7.name= ~current_heading_weight
7.default= 0.01
7.type= double
7.desc= The weight given to the current heading of the robot in the cost function.

8.name= ~odor_weight
8.default= 0.10
8.type= double
8.desc= The weight given to the odor gradient in the cost function.

9.name= ~bubble_radius
9.default= 0.10
9.type= double
9.desc= The radius of the bubble used to sample the plume for calculating the odor gradient.

10.name= ~min_particle_count_difference
10.default= 5
10.type= int
10.desc= The minimum difference between the maximum and minimum particle count inside the plume to consider an odor gradient.

11.name= ~move_base/local_costmap/inflation_radius
11.default= 0.20
11.type= double
11.desc= The inflation radius used by the navigation stack.

12.name= ~debug_slices
12.default= false
12.type= bool
12.desc= If true the debug mode will be on and the topics debug_cells and pp_goal will be published to.
}
}
```

## Tutorials

Coming soon\...
