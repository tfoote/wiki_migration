## Dependencies

This package depends on the following message definitions:

-   [cpswarm_msgs](cpswarm_msgs)

The following library packages of the swarm behaviors library are
required:

-   [swarm_behaviors_position](swarm_behaviors_position)

The following packages of the swarm functions library are required:

-   [target_monitor](target_monitor) (only if `single_target=true`)

The following packages of the
[sensing and actuation library](https://github.com/cpswarm/sensing_actuation)
are required:

-   area_provider
-   obstacle_detection

Further required packages are:

-   [actionlib](actionlib)
-   [random_numbers](random_numbers)

## Execution

Run the launch file 

```
roslaunch uav_random_direction uav_random_direction.launch
```

 to launch the
`uav_random_direction` node.

The launch file can be configured with following parameters:

`id` (`integer`, default: 1) The identifier (ID) of the CPS used for
name spacing in simulation. `output` (`string`, default: `screen`)
Whether to show the program output (`screen`) or to write it to a log
file (`log`).

In the `param` subdirectory there is the parameter file
`uav_random_direction.yaml` that allows to configure the behavior of the
`uav_random_direction` node.

## Nodes



```clearsilver

node.0 {
name=uav_random_direction
desc=The `uav_random_direction` performs coverage using the random direction algorithm. The random direction is a mathematical movement model, where an agent moves straight forward until it reaches an obstacle or the environment boundary. There, it changes its direction randomly into a direction that is clear of obstacles. When the parameter `single_target` is set to `true`, the UAV succeeds once a target has been found and returns the target ID and position.

goal{
0.name=uav_coverage/goal
0.type=cpswarm_msgs/CoverageGoal
0.desc=A goal that starts the random direction coverage behavior. It contains the altitude at which to operate.
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
0.name=area/get_area
0.type=cpswarm_msgs/GetPoints
0.desc=Get the area polygon.
1.name=obstacle_detection/get_clear_sector
1.type=cpswarm_msgs/GetSector
1.desc=Get the circular sector that is clear of obstacles.
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
3.name=~margin
3.type=real
3.default=0.5
3.desc=The distance in meter to keep to the environment boundary.
4.name=/rng_seed
4.type=integer
4.default=0
4.desc=The seed used for random number generation. In the default case, a random seed is generated.
}
}
```



## Acknowledgements

This work is supported by the European Commission through the
[CPSwarm H2020 project](https://cpswarm.eu) under grant no. 731946.
