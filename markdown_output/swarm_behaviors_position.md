## Dependencies

This package depends on the following message definitions:

-   [geometry_msgs](geometry_msgs)
-   [cpswarm_msgs](cpswarm_msgs)

The following packages of the
[sensing and actuation library](https://github.com/cpswarm/sensing_actuation)
are required:

-   area_provider
-   \*_pos_provider
-   \*_pos_controller

Further required packages are:

-   [tf2](tf2)

## Libraries



```clearsilver

node.0 {
name=position
desc=The `position` library provides position related functionalities. These functionalities can be grouped into three categories: calculations, retrieval of sensor data, and setting of actuators. The calculations include distance measurements, checking whether a position is in the defined environment, and calculation of goal positions. The sensor data includes absolute and relative bearing as well as local position. The actuators to be controlled is locomotion by providing a goal position waypoint.

sub{
0.name=pos_provider/pose
0.type=geometry_msgs/PoseStamped
0.desc=Position and orientation of the CPS.
}

pub{
0.name=pos_controller/goal_position
0.type=geometry_msgs/PoseStamped
0.desc=The goal waypoint where the CPS shall move to.
}

srv_called{
0.name=area/out_of_bounds
0.type=cpswarm_msgs/OutOfBounds
0.desc=Check whether a coordinate is within the defined environment area.
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
2.name=~goal_tolerance
2.type=real
2.default=0.1
2.desc=The distance in meter that the CPS can be away from a goal while still being considered to have reached that goal.
3.name=~visualize
3.type=boolean
3.default=false
3.desc=Whether to publish the goal waypoint on a topic for visualization.
}
}
```



## Acknowledgements

This work is supported by the European Commission through the
[CPSwarm H2020 project](https://cpswarm.eu) under grant no. 731946.
