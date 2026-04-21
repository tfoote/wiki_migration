## Dependencies

This package depends on the following message definitions:

-   [geometry_msgs](geometry_msgs)
-   [cpswarm_msgs](cpswarm_msgs)

The communication between CPSs is based on the
[CPSwarm Communication Library](https://github.com/cpswarm/swarmio).

The following packages of the
[swarm functions library](https://github.com/cpswarm/swarm_functions)
are required:

-   task_allocation

The following packages of the
[sensing and actuation library](https://github.com/cpswarm/sensing_actuation)
are required:

-   \*_pos_provider

Further required packages are:

-   [tf2](tf2)

## Execution

Run the launch file 

```
roslaunch target_monitor target_monitor.launch
```

 to launch the
`target_monitor` node.

The launch file can be configured with following parameters:

`id` (`integer`, default: 1) The identifier (ID) of the CPS used for
name spacing in simulation. `output` (`string`, default: `screen`)
Whether to show the program output (`screen`) or to write it to a log
file (`log`).

In the `param` subdirectory there are two parameter files
`target_monitor.yaml` and `targets.yaml` that allows to configure the
behavior of the `target_monitor` node. The `targets.yaml` contains the
coordinates of the simulated targets. It is only used when the parameter
`simulation` is set to `true`. They are given as two list parameters
where the list index is the ID of the target.

## Nodes



```clearsilver

node.0 {
name=target_monitor
desc=The `target_monitor` node keeps track of targets and their positions that are being detected by CPSs in the swarm. They are typically detected by a camera. Each target has a unique numeric ID assigned to it which should be a positive integer. Targets that are detected locally by this CPS are reported through the `target_tracking` topic. It contains the offset between the current position and the target position in form of a transform. This information can either originate from another node or, if `simulation` is set to `true`, from this node. In the latter case, the target detection is triggered according to the current position of the CPS and the coordinates given in the `targets.yaml` parameter file. Targets that are being managed have a certain state associated to them. This is depicted by the following diagram where the transitions are labled with incoming event / outgoing event: {{attachment:target_fsm.png}} The state of the target changes depending on local and remote events that are exchanged between CPSs through the [[https://github.com/cpswarm/swarmio|CPSwarm Communication Library]].

sub{
0.name=pos_provider/pose
0.type=geometry_msgs/PoseStamped
0.desc=The current position of this CPS.
1.name=target_tracking
1.type=cpswarm_msgs/TargetTracking
1.desc=The offset of the target as reported by the camera.
2.name=cps_selected
2.type=cpswarm_msgs/TaskAllocatedEvent
2.desc=The event of a target being assigned by this CPS.
3.name=target_done
3.type=cpswarm_msgs/TargetPositionEvent
3.desc=The event of a target being completed by this CPS.
4.name=bridge/events/target_found
4.type=cpswarm_msgs/TargetPositionEvent
4.desc=The event of a target being found by another CPS. Messages are exchanged between CPSs using the [[https://github.com/cpswarm/swarmio|CPSwarm Communication Library]].
5.name=bridge/events/target_update
5.type=cpswarm_msgs/TargetPositionEvent
5.desc=Target updates from other CPSs. Messages are exchanged between CPSs using the [[https://github.com/cpswarm/swarmio|CPSwarm Communication Library]].
6.name=bridge/events/cps_selected
6.type=cpswarm_msgs/TaskAllocatedEvent
6.desc=The event of a target being assigned by another CPS. Messages are exchanged between CPSs using the [[https://github.com/cpswarm/swarmio|CPSwarm Communication Library]].
7.name=bridge/events/target_lost
7.type=cpswarm_msgs/TargetPositionEvent
7.desc=The event of a target being lost by another CPS. Messages are exchanged between CPSs using the [[https://github.com/cpswarm/swarmio|CPSwarm Communication Library]].
8.name=bridge/events/target_done
8.type=cpswarm_msgs/TargetPositionEvent
8.desc=The event of a target being completed by another CPS. Messages are exchanged between CPSs using the [[https://github.com/cpswarm/swarmio|CPSwarm Communication Library]].
9.name=bridge/uuid
9.type=cpswarm_msgs/TargetPositionEvent
9.desc=The UUID of this CPS.
}

pub{
0.name=target_tracking
0.type=cpswarm_msgs/TargetTracking
0.desc=The offset of the target that is simulated by this node. Messages are published if `simulation` is set to `true` and the distance between the CPS and a simulated target is less than or equal to `fov`.
1.name=target_found
1.type=cpswarm_msgs/TargetPositionEvent
1.desc=The event of a target being found by this CPS. The event is forwarded by the [[https://github.com/cpswarm/swarmio|CPSwarm Communication Library]] to the other swarm members.
2.name=target_update
2.type=cpswarm_msgs/TargetPositionEvent
2.desc=Target updates from this CPS. The event is forwarded by the [[https://github.com/cpswarm/swarmio|CPSwarm Communication Library]] to the other swarm members.
3.name=target_lost
3.type=cpswarm_msgs/TargetPositionEvent
3.desc=The event of a target being lost by this CPS. The event is forwarded by the [[https://github.com/cpswarm/swarmio|CPSwarm Communication Library]] to the other swarm members.
4.name=target_done
4.type=cpswarm_msgs/TargetPositionEvent
4.desc=The event of a target being completed by this CPS. The event is forwarded by the [[https://github.com/cpswarm/swarmio|CPSwarm Communication Library]] to the other swarm members.
}

goal{
0.name=cmd/target_done/goal
0.type=cpswarm_msgs/TargetGoal
0.desc=Sets the state of a target to done. This invokes the target_done event to be published.
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
2.name=~tracking_timeout
2.type=real
2.default=5.0
2.desc=The time in seconds after which a target transitions into the state lost when no target information is received.
3.name=~target_tolerance
3.type=real
3.default=0.1
3.desc=The path of the smach state machine whose state shall be exchanged.
4.name=~fov
4.type=real
4.default=0.5
4.desc=Range of the target tracking camera in meter. It is used to simulate target detection. Targets within this distance are detected by the CPS.
5.name=~simulation
5.type=boolean
5.default=false
5.desc=Whether the targets are detected virtually by position or actually by the camera tracking topic.
6.name=~targets_x
6.type=real list
6.default=[]
6.desc=The x-coordinates of the simulated targets.
7.name=~targets_y
7.type=real list
7.default=[]
7.desc=The y-coordinates of the simulated targets.
}
}
```



## Acknowledgements

This work is supported by the European Commission through the
[CPSwarm H2020 project](https://cpswarm.eu) under grant no. 731946.
