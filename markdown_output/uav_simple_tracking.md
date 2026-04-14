## Dependencies

This package depends on the following message definitions:

-   [cpswarm_msgs](cpswarm_msgs)

The following library packages of the swarm behaviors library are
required:

-   [swarm_behaviors_position](swarm_behaviors_position)

The following packages of the swarm functions library are required:

-   [target_monitor](target_monitor)

Further required packages are:

-   [actionlib](actionlib)

## Execution

Run the launch file ```
roslaunch uav_simple_tracking uav_simple_tracking.launch
``` to launch the
`uav_simple_tracking` node.

The launch file can be configured with following parameters:

`id` (`integer`, default: 1) The identifier (ID) of the CPS used for
name spacing in simulation. `output` (`string`, default: `screen`)
Whether to show the program output (`screen`) or to write it to a log
file (`log`).

In the `param` subdirectory there is the parameter file
`uav_simple_tracking.yaml` that allows to configure the behavior of the
`uav_simple_tracking` node.

## Nodes

```clearsilver

node.0 {
name=uav_simple_tracking
desc=The `uav_simple_tracking` tracks a target with a UAV. The UAV moves to the position straight over the target. The position of the target is updated by the target monitor from the [[swarm functions]] library. When the target is lost, i.e., the target is not in the camera field of view anymore, the tracking aborts. When the target is done, i.e., handled by another CPS, the tracking succeeds.

goal{
0.name=uav_tracking/goal
0.type=cpswarm_msgs/TrackingGoal
0.desc=A goal that starts the tracking behavior. It contains the ID of the target to track and the altitude at which to operate.
}

sub{
0.name=target_update
0.type=cpswarm_msgs/TargetPositionEvent
0.desc=Position updates of the target being tracked.
1.name=target_lost
1.type=cpswarm_msgs/TargetPositionEvent
1.desc=Whether the target being tracked has been lost.
2.name=target_done
2.type=cpswarm_msgs/TargetPositionEvent
2.desc=Whether the target being tracked has been handled by another CPS.
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
}
}
```

## Acknowledgements

This work is supported by the European Commission through the
[CPSwarm H2020 project](https://cpswarm.eu) under grant no. 731946.
