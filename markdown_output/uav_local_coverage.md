## Dependencies

This package depends on the following message definitions:

-   [cpswarm_msgs](cpswarm_msgs)

The following library packages of the swarm behaviors library are
required:

-   [swarm_behaviors_position](swarm_behaviors_position)

The following packages of the swarm functions library are required:

-   [target_monitor](target_monitor) (only if `single_target=true`)

Further required packages are:

-   [actionlib](actionlib)

## Execution

Run the launch file 

```
roslaunch uav_local_coverage uav_local_coverage.launch
```

 to launch the
`uav_local_coverage` node.

The launch file can be configured with following parameters:

`id` (`integer`, default: 1) The identifier (ID) of the CPS used for
name spacing in simulation. `output` (`string`, default: `screen`)
Whether to show the program output (`screen`) or to write it to a log
file (`log`).

In the `param` subdirectory there is the parameter file
`uav_local_coverage.yaml` that allows to configure the behavior of the
`uav_local_coverage` node.

## Nodes



```clearsilver

node.0 {
name=uav_local_coverage
desc=The `uav_local_coverage` performs coverage locally around the current position of the UAV. This is achieved by generating a spiral movement pattern according to the [[http://mathworld.wolfram.com/CircleInvolute.html|circle involute]]. The shape of the circle involute is computed based on the characteristics of the camera of the UAV. It is computed in such a way that a downward facing camera completely covers the area around the current position of the UAV. The UAV follows this path for a predefined number of steps and then aborts the coverage. When the parameter `single_target` is set to `true`, it succeeds once a target has been found and returns the target ID and position.

goal{
0.name=uav_local_coverage/goal
0.type=cpswarm_msgs/CoverageGoal
0.desc=A goal that starts the local coverage behavior. It contains the altitude at which to operate.
}

result{
0.name=uav_local_coverage/result
0.type=cpswarm_msgs/CoverageResult
0.desc=ID and position of the target that has been found.
}

sub{
0.name=target_found
0.type=cpswarm_msgs/TargetPositionEvent
0.desc=Position and ID of a target detected by the target monitor. Only subscribed when `single_target` is set to `true`.
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
3.name=~fov_hor
3.type=real
3.default=1.236
3.desc=Horizontal camera field of view in radian. It is used to compute the path of the UAV.
4.name=~fov_ver
4.type=real
4.default=0.970
4.desc=Vertical camera field of view in radian. It is used to compute the path of the UAV.
5.name=~local_steps
5.type=integer
5.default=20
5.desc=Number of steps to do in the local coverage behavior.
}
}
```



## Acknowledgements

This work is supported by the European Commission through the
[CPSwarm H2020 project](https://cpswarm.eu) under grant no. 731946.
