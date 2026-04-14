## Dependencies

This package depends on the following message definitions:

-   [smach_msgs](smach_msgs)
-   [cpswarm_msgs](cpswarm_msgs)

The communication between CPSs is based on the
[CPSwarm Communication Library](https://github.com/cpswarm/swarmio).

The state that is exchanged is read from a [SMACH](SMACH) state machine.

## Execution

Run the launch file ```
roslaunch state_exchanger state_exchanger.launch
``` to launch the
`state_exchanger` node.

The launch file can be configured with following parameters:

`id` (`integer`, default: 1) The identifier (ID) of the CPS used for
name spacing in simulation. `output` (`string`, default: `screen`)
Whether to show the program output (`screen`) or to write it to a log
file (`log`).

In the `param` subdirectory there is the parameter file
`state_exchanger.yaml` that allows to configure the behavior of the
`state_exchanger` node.

## Nodes

```clearsilver

node.0 {
name=state_exchanger
desc=The `state_exchanger` node publishes behavioral states of this CPS to the rest of the swarm and publishes the state received from the other swarm members locally. The state is taken from a locally running SMACH state machine. If the CPS is in multiple states, only the first one is considered.

sub{
0.name=smach_server/smach/container_status
0.type=smach_msgs/SmachContainerStatus
0.desc=The current state of this CPS.
1.name=bridge/events/state
1.type=cpswarm_msgs/StateEvent
1.desc=The current state of another CPS. Messages are exchanged between CPSs using the [[https://github.com/cpswarm/swarmio|CPSwarm Communication Library]].
}

pub{
0.name=state
0.type=cpswarm_msgs/StateEvent
0.desc=The current state of this CPS that is forwarded by the [[https://github.com/cpswarm/swarmio|CPSwarm Communication Library]] to the other swarm members.
1.name=swarm_state
1.type=cpswarm_msgs/ArrayOfStates
1.desc=The states of the other swarm members received through the [[https://github.com/cpswarm/swarmio|CPSwarm Communication Library]].
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
2.name=~timeout
2.type=real
2.default=20.0
2.desc=The time in seconds after which another CPS is considered to have left the swarm.
3.name=~sm_path
3.type=string
3.default=/SM_TOP
3.desc=The path of the smach state machine whose state shall be exchanged.
}
}
```

## Acknowledgements

This work is supported by the European Commission through the
[CPSwarm H2020 project](https://cpswarm.eu) under grant no. 731946.
