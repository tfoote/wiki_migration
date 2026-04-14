## Dependencies

This package depends on the following message definitions:

-   [geometry_msgs](geometry_msgs)
-   [cpswarm_msgs](cpswarm_msgs)

The communication between CPSs is based on the
[CPSwarm Communication Library](https://github.com/cpswarm/swarmio).

The following packages of the
[sensing and actuation library](https://github.com/cpswarm/sensing_actuation)
are required:

-   \*\_pos_provider
-   \*\_vel_provider

Further required packages are:

-   [tf2](tf2)

## Execution

Run the launch file ```
roslaunch kinematics_exchanger kinematics_exchanger.launch
``` to launch the
`kinematics_exchanger` node.

The launch file can be configured with following parameters:

`id` (`integer`, default: 1) The identifier (ID) of the CPS used for
name spacing in simulation. `output` (`string`, default: `screen`)
Whether to show the program output (`screen`) or to write it to a log
file (`log`).

In the `param` subdirectory there is the parameter file
`kinematics_exchanger.yaml` that allows to configure the behavior of the
`kinematics_exchanger` node.

## Nodes

```clearsilver

node.0 {
name=kinematics_exchanger
desc=The `kinematics_exchanger` node publishes position and velocity of this CPS to the rest of the swarm and publishes the position and velocity received from the other swarm members locally. It publishes the swarm position both as relative and absolute coordinates. The swarm velocity is published only as relative coordinates.

sub{
0.name=pos_provider/pose
0.type=geometry_msgs/PoseStamped
0.desc=The current position of this CPS.
1.name=vel_provider/velocity
1.type=geometry_msgs/TwistStamped
1.desc=The current velocity of this CPS.
2.name=bridge/events/position
2.type=cpswarm_msgs/Position
2.desc=The current position of another CPS. Messages are exchanged between CPSs using the [[https://github.com/cpswarm/swarmio|CPSwarm Communication Library]].
3.name=bridge/events/velocity
3.type=cpswarm_msgs/Velocity
3.desc=The current velocity of another CPS. Messages are exchanged between CPSs using the [[https://github.com/cpswarm/swarmio|CPSwarm Communication Library]].
}

pub{
0.name=position
0.type=cpswarm_msgs/Position
0.desc=The current position of this CPS that is forwarded by the [[https://github.com/cpswarm/swarmio|CPSwarm Communication Library]] to the other swarm members.
1.name=velocity
1.type=cpswarm_msgs/Velocity
1.desc=The current velocity of this CPS that is forwarded by the [[https://github.com/cpswarm/swarmio|CPSwarm Communication Library]] to the other swarm members.
2.name=swarm_position
2.type=cpswarm_msgs/ArrayOfPositions
2.desc=The positions of the other swarm members received through the [[https://github.com/cpswarm/swarmio|CPSwarm Communication Library]].
3.name=swarm_position_rel
3.type=cpswarm_msgs/ArrayOfVectors
3.desc=The positions of the other swarm members received through the [[https://github.com/cpswarm/swarmio|CPSwarm Communication Library]] relative to the position of this CPS.
4.name=swarm_velocity_rel
4.type=cpswarm_msgs/ArrayOfVectors
4.desc=The velocities of the other swarm members received through the [[https://github.com/cpswarm/swarmio|CPSwarm Communication Library]] relative to the velocity of this CPS.
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
3.name=~sample_size
3.type=integer
3.default=5
3.desc=The number of data samples to average over for reliable results.
4.name=~init
4.type=integer
4.default=30
4.desc=The number of messages to ignore during initialization. This is because the first messages are inaccurate.
}
}
```

## Acknowledgements

This work is supported by the European Commission through the
[CPSwarm H2020 project](https://cpswarm.eu) under grant no. 731946.
