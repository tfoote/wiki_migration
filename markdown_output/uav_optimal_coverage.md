## Dependencies

This package depends on the following message definitions:

-   [cpswarm_msgs](cpswarm_msgs)

The following library packages of the swarm behaviors library are
required:

-   [swarm_behaviors_position](swarm_behaviors_position)

The following packages of the swarm functions library are required:

-   [area_division](area_division)
-   [coverage_path](coverage_path)
-   [target_monitor](target_monitor) (only if `single_target=true`)

Further required packages are:

-   [actionlib](actionlib)

## Execution

Run the launch file ```
roslaunch uav_optimal_coverage uav_optimal_coverage.launch
``` to launch the
`uav_optimal_coverage` node.

The launch file can be configured with following parameters:

`id` (`integer`, default: 1) The identifier (ID) of the CPS used for
name spacing in simulation. `output` (`string`, default: `screen`)
Whether to show the program output (`screen`) or to write it to a log
file (`log`).

In the `param` subdirectory there is the parameter file
`uav_optimal_coverage.yaml` that allows to configure the behavior of the
`uav_optimal_coverage` node.

## Nodes

```clearsilver

node.0 {
name=uav_optimal_coverage
desc=The `uav_optimal_coverage` performs coverage with a swarm of UAVs. The coverage is optimal in a sense that the area to be covered is divided among the UAVs to avoid overlapping regions to be covered multiple times. Within each region, the assigned UAV sweeps the area using simple back and forth (boustrophedon) motion. Once the region has been sweeped completely, it aborts the coverage. When the parameter `single_target` is set to `true`, it succeeds once a target has been found and returns the target ID and position. The area division and coverage path generation are provided by the [[swarm_functions]] library.

goal{
0.name=uav_coverage/goal
0.type=cpswarm_msgs/CoverageGoal
0.desc=A goal that starts the optimal coverage behavior. It contains the altitude at which to operate.
}

result{
0.name=uav_coverage/result
0.type=cpswarm_msgs/CoverageResult
0.desc=ID and position of the target that has been found.
}

sub{
0.name=target_found
0.type=cpswarm_msgs/TargetPositionEvent
0.desc=Position and ID of a target detected by the target monitor. Only subscribed when `single_target` is set to `true`.
}

srv_called{
0.name=coverage_path/waypoint
0.type=cpswarm_msgs/GetWaypoint
0.desc=Get the current waypoint to navigate to.
}

param{
0.name=~loop_rate
0.type=real
0.default=5
0.desc=The frequency in Hz at which to run the control loops.
1.name=~queue_size
1.type=integer
1.default=1
1.desc=The size of the message queue used for publishing and subscribing to topics.
2.name=~single_target
2.type=boolean
2.default=true
2.desc=Whether the algorithm will succeed / terminate once a target has been found.
}
}
```

## Acknowledgements

This work is supported by the European Commission through the
[CPSwarm H2020 project](https://cpswarm.eu) under grant no. 731946.
