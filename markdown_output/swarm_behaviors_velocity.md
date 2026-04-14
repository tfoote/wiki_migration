## Dependencies

This package depends on the following message definitions:

-   [geometry_msgs](geometry_msgs)
-   [cpswarm_msgs](cpswarm_msgs)

The following library packages of the swarm behaviors library are
required:

-   [swarm_behaviors_position](swarm_behaviors_position)

The following packages of the
[sensing and actuation library](https://github.com/cpswarm/sensing_actuation)
are required:

-   \*\_vel_provider
-   \*\_vel_controller

## Libraries

```clearsilver

node.0 {
name=velocity
desc=The `velocity` library provides velocity related functionalities. These include retrieval of current velocity, computation of relative velocity, computation of velocity to reach a certain waypoint, and setting the actuators velocity.

sub{
0.name=vel_provider/velocity
0.type=geometry_msgs/TwistStamped
0.desc=Current velocity of the CPS.
}

pub{
0.name=vel_controller/target_velocity
0.type=geometry_msgs/Twist
0.desc=The target velocity at which the CPS shall move.
}

param{
0.name=~loop_rate
0.type=real
0.default=5.0
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
