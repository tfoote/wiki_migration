## Dependencies

This package depends on the following message definitions:

-   [geometry_msgs](geometry_msgs)
-   [nav_msgs](nav_msgs)
-   [cpswarm_msgs](cpswarm_msgs)

The communication between CPSs is based on the
[CPSwarm Communication Library](https://github.com/cpswarm/swarmio).

The following packages of the
[swarm functions library](https://github.com/cpswarm/swarm_functions)
are required:

-   area_division
-   state_exchanger

The following packages of the
[sensing and actuation library](https://github.com/cpswarm/sensing_actuation)
are required:

-   \*_pos_provider

Further required packages are:

-   [tf2](tf2)

## Execution

Run the launch file 

```
roslaunch coverage_path coverage_path.launch
```

 to launch the
`coverage_path` node.

The launch file can be configured with following parameters:

`id` (`integer`, default: 1) The identifier (ID) of the CPS used for
name spacing in simulation. `output` (`string`, default: `screen`)
Whether to show the program output (`screen`) or to write it to a log
file (`log`).

In the `param` subdirectory there is the parameter file
`coverage_path.yaml` that allows to configure the behavior of the
`coverage_path` node.

## Nodes



```clearsilver

node.0{
name=coverage_path
desc=The `coverage_path` node generates a path that allows a CPS to cover a given area. It uses the area assigned by the area_division package. The generated coverage path is based on a [[https://en.wikipedia.org/wiki/Minimum_spanning_tree|minimum spanning tree]] to optimally sweep the area. The path is regenerated when area to be covered changes. The path can be retrieved either as a whole or waypoint after waypoint. In the latter case, the current waypoint is returned, based on the current position of the CPS.

sub{
0.name=area/assigned
0.type=nav_msgs/OccupancyGrid
0.desc=The area to be covered by this CPS. Only called if `divide_area=true`.
1.name=area/map
1.type=nav_msgs/OccupancyGrid
1.desc=The area to be covered. Only called if `divide_area=false`.
}

pub{
0.name=coverage_path/path
0.type=nav_msgs/Path
0.desc=The generated path for visualization purposes. Only published if the parameter `visualize` is set to true.
1.name=coverage_path/waypoint
1.type=geometry_msgs/PointStamped
1.desc=The current waypoint of the generated path for visualization purposes. Only published if the parameter `visualize` is set to true.
2.name=coverage_path/mst
2.type=geometry_msgs/PoseArray
2.desc=The minimum spanning tree of the area for visualization purposes. Only published if the parameter `visualize` is set to true.
}

srv{
0.name=coverage_path/path
0.type=nav_msgs/GetPlan
0.desc=Provides the complete generated path.
1.name=coverage_path/waypoint
1.type=cpswarm_msgs/GetWaypoint
1.desc=Provides the current waypoint of the generated path.
}

srv_called{
0.name=area/get_area
0.type=cpswarm_msgs/GetPoints
0.desc=Get the points defining the polygon of the area to be covered.
}

param{
0.name=~loop_rate
0.type=real
0.default=1.5
0.desc=The frequency in Hz at which to run the control loops.
1.name=~queue_size
1.type=integer
1.default=1
1.desc=The size of the message queue used for publishing and subscribing to topics.
2.name=~resolution
2.type=real
2.default=1.0
2.desc=The grid map underlying the path planning will be downsampled to this resolution in meter / cell.
3.name=~visualize
3.type=boolean
3.default=false
3.desc=Whether to publish the coverage path on a topic for visualization.
4.name=~divide_area
4.type=boolean
4.default=false
4.desc=Whether to divide the area among the CPSs before generating the path or to generate the path on the complete map. If true, downsampling is not available.
5.name=~vertical
5.type=boolean
5.default=false
5.desc=Whether the sweeping pattern is vertical or horizontal.
6.name=~turning_points
6.type=boolean
6.default=false
6.desc=Whether there are only waypoints at turning points of the path or also waypoints regularly spaced on straight line segments of the path.
}
}
```



## Acknowledgements

This work is supported by the European Commission through the
[CPSwarm H2020 project](https://cpswarm.eu) under grant no. 731946.
