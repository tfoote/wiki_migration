## Dependencies

This package depends on the following message definitions:

-   [geometry_msgs](geometry_msgs)
-   [nav_msgs](nav_msgs)
-   [cpswarm_msgs](cpswarm_msgs)

The communication between CPSs is based on the
[CPSwarm Communication Library](https://github.com/cpswarm/swarmio).

The following packages of the
[sensing and actuation library](https://github.com/cpswarm/sensing_actuation)
are required:

-   area_provider
-   \*_pos_provider
-   \*_pos_controller

## Execution

Run the launch file ```
roslaunch area_division area_division.launch
``` to launch the
`area_division` node.

The launch file can be configured with following parameters:

`id` (`integer`, default: 1) The identifier (ID) of the CPS used for
name spacing in simulation. `output` (`string`, default: `screen`)
Whether to show the program output (`screen`) or to write it to a log
file (`log`).

In the `param` subdirectory there is the parameter file
`area_division.yaml` that allows to configure the behavior of the
`area_division` node.

## Nodes

```clearsilver

node.0 {
name=area_division
desc=The `area_division` divides the environment area among multiple CPSs. When this node is running, it listens to area division requests by other CPSs to perform the area division. The division is also triggered when CPS join or leave the swarm or the behavior state of this CPS changes. Once the area division starts, all CPSs that participate in the area division, stop moving, and synchronize in order to achieve the same area division result. The division algorithm is based on the [[https://github.com/athakapo/DARP|DARP algorithm]] which tries to divide the area optimally. Each CPS is assigned an equal share of the environment that includes its current position.

sub{
0.name=state
0.type=cpswarm_msgs/StateEvent
0.desc=The behavior state of this CPS.
1.name=swarm_state
1.type=cpswarm_msgs/ArrayOfStates
1.desc=The behaior states of the other CPSs.
2.name=pos_provider/pose
2.type=geometry_msgs/PoseStamped
2.desc=The current position of this CPS.
3.name=area/map
3.type=nav_msgs/OccupancyGrid
3.desc=The map to be divided.
4.name=bridge/uuid
4.type=swarmros/String
4.desc=The UUID of this CPS as provided by the [[https://cpswarm.github.io/swarmio/swarmros/msg/String.html|CPSwarm Communication Library]].
5.name=bridge/events/area_division
5.type=cpswarm_msgs/AreaDivisionEvent
5.desc=The area division requests from other CPSs. Messages are exchanged between CPSs using the [[https://github.com/cpswarm/swarmio|CPSwarm Communication Library]].
}

pub{
0.name=pos_controller/goal_position
0.type=geometry_msgs/PoseStamped
0.desc=The topic for stoping the CPS.
1.name=area_division
1.type=cpswarm_msgs/AreaDivisionEvent
1.desc=The topic for requesting area division among the available CPSs in the swarm. The request is forwarded by the [[https://github.com/cpswarm/swarmio|CPSwarm Communication Library]] to the other swarm members.
2.name=area/assigned
2.type=nav_msgs/OccupancyGrid
2.desc=The area assigned to this CPS.
3.name=area/rotated
3.type=nav_msgs/OccupancyGrid
3.desc=The area to be divided, rotated so the lower boundary is horizontal. For visualization purposes, only published if the parameter `visualize` is set to true.
4.name=area/downsampled
4.type=nav_msgs/OccupancyGrid
4.desc=The area to be divided, downsampled to a lower resolution. For visualization purposes, only published if the parameter `visualize` is set to true.
}

srv_called{
0.name=area/get_rotation
0.type=cpswarm_msgs/GetDouble
0.desc=Get the rotation required to align the lower boundary of the area horizontally.
}

param{
0.name=~loop_rate
0.type=real
0.default=1.5
0.desc=The frequency in Hz at which to run the control loops.
1.name=~queue_size
1.type=integer
1.default=10
1.desc=The size of the message queue used for publishing and subscribing to topics.
2.name=~resolution
2.type=real
2.default=1.0
2.desc=The grid map underlying the area division will be downsampled to this resolution in meter / cell.
3.name=~swarm_timeout
3.type=real
3.default=5.0
3.desc=The time in seconds communication in the swarm can be delayed at most. Used to wait after an area division event before starting the area division or time after which it is assumed that a swarm member has left the swarm if no position update has been received.
4.name=~visualize
4.type=boolean
4.default=false
4.desc=Whether to publish the area division on a topic for visualization.
5.name=~states
5.type=string list
5.default=[]
5.desc=Only CPSs in these states divide the area among each other.
6.name=~/optimizer/iterations
6.type=integer
6.default=10
6.desc=Maximum number of iterations of the optimization algorithm.
7.name=~/optimizer/variate_weight
7.type=real
7.default=0.01
7.desc=Maximum variate weight of connected components.
8.name=~/optimizer/discrepancy
8.type=integer
8.default=30
8.desc=Maximum difference between number of assigned grid cells to each CPS.
}
}
```

## Acknowledgements

This work is supported by the European Commission through the
[CPSwarm H2020 project](https://cpswarm.eu) under grant no. 731946.
