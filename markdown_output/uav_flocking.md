## Dependencies

This package depends on the following message definitions:

-   [geometry_msgs](geometry_msgs)
-   [cpswarm_msgs](cpswarm_msgs)

The following library packages of the swarm behaviors library are
required:

-   [position](position)
-   [velocity](velocity)

The following packages of the swarm functions library are required:

-   [coverage_path](coverage_path)
-   [target_monitor](target_monitor)

The following packages of the
[sensing and actuation library](https://github.com/cpswarm/sensing_actuation)
are required:

-   area_provider

Further required packages are:

-   [actionlib](actionlib)

## Execution

There are two launch files, one for coverage and one for tracking. Run
the launch file 

```
roslaunch uav_flocking uav_flocking_coverage.launch
```

 to launch the
`uav_flocking_coverage` node. Run the launch file


```
roslaunch uav_flocking uav_flocking_tracking.launch
```

 to launch the `uav_flocking_tracking` node.

The launch files can be configured with following parameters:

`id` (`integer`, default: 1) The identifier (ID) of the CPS used for
name spacing in simulation. `output` (`string`, default: `screen`)
Whether to show the program output (`screen`) or to write it to a log
file (`log`).

In the `param` subdirectory there is the parameter file
`uav_flocking.yaml` that allows to configure the behavior of both nodes.

## Nodes



```clearsilver

node.0 {
name=uav_flocking_coverage
desc=The `uav_flocking_coverage` performs coverage with a swarm of UAVs. The UAVs stay in a flock while sweeping the area using simple back and forth (boustrophedon) motion. Once the region has been sweeped completely, the UAVs abort the coverage. When the parameter `single_target` is set to `true`, a UAV succeeds once a target has been found and returns the target ID and position. The coverage path generation is provided by the [[swarm_functions]] library.

goal{
0.name=uav_coverage/goal
0.type=cpswarm_msgs/CoverageGoal
0.desc=An empty goal that starts the optimal coverage behavior.
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
1.name=swarm_position_rel
1.type=cpswarm_msgs/ArrayOfVectors
1.desc=Relative positions of the other swarm members.
2.name=swarm_velocity_rel
2.type=cpswarm_msgs/ArrayOfVectors
2.desc=Relative velocities of the other swarm members.
}

srv_called{
0.name=coverage_path/waypoint
0.type=cpswarm_msgs/GetWaypoint
0.desc=Get the current waypoint to navigate to.
1.name=area/get_area
1.type=cpswarm_msgs/GetPoints
1.desc=Get the area boundaries.
2.name=area/get_center
2.type=cpswarm_msgs/GetPoint
2.desc=Get the center of the area.
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
3.name=~equi_dist
3.type=real
3.default=10.0
3.desc=Equilibrium distance between CPSs in meter.
4.name=~flock_vel
4.type=real
4.default=0.5
4.desc=Target velocity of the flock in meter per second.
5.name=~form_vel
5.type=real
5.default=0.5
5.desc=Maximum velocity during formation flight in meter per second.
6.name=~equi_dist
6.type=real
6.default=1.0
6.desc=
7.name=~repulse_spring
7.type=real
7.default=1.0
7.desc=Repulsion spring constant of half-spring per square second.
8.name=~repulse_max
8.type=real
8.default=1.0
8.desc=Maximum repulsion between CPSs in meter in order to avoid over excitation.
9.name=~align_frict
9.type=real
9.default=20.0
9.desc=Velocity alignment viscous friction coefficient in square meter per second. Higher values result in slower but more stable flocks.
10.name=~align_slope
10.type=real
10.default=1.0
10.desc=Constant slope around equilibrium distance in meter.
11.name=~align_min
11.type=real
11.default=1.0
11.desc=Minimum alignment between CPS in meter in order to avoid over excitation.
12.name=~wall_frict
12.type=real
12.default=20.0
12.desc=Bounding area viscous friction coefficient in square meter per second.
13.name=~wall_decay
13.type=real
13.default=1.0
13.desc=Softness of wall as decay width in meter.
14.name=~form_shape
14.type=real
14.default=1.0
14.desc=Strength of the shape forming velocity component in formation flight.
15.name=~form_track
15.type=real
15.default=1.0
15.desc=Strength of the tracking velocity component in formation flight.
16.name=~accel_time
16.type=real
16.default=1.0
16.desc=Characteristic time needed by the CPS to reach the target velocity in seconds.
}
}

node.1 {
name=uav_flocking_tracking
desc=The `uav_flocking_tracking` performs tracking with a swarm of UAVs. The UAVs stay in a formation while tracking a target. The position of the target is updated by the target monitor from the [[swarm_functions]] library When the target is lost, i.e., the target is not in the camera field of view anymore, the tracking aborts. When the target is done, i.e., handled by another CPS, the tracking succeeds.

goal{
0.name=uav_tracking/goal
0.type=cpswarm_msgs/TrackingGoal
0.desc=A goal that starts the tracking behavior. It contains the ID of the target to track.
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
3.name=swarm_position_rel
3.type=cpswarm_msgs/ArrayOfVectors
3.desc=Relative positions of the other swarm members.
4.name=swarm_velocity_rel
4.type=cpswarm_msgs/ArrayOfVectors
4.desc=Relative velocities of the other swarm members.
}

srv_called{
0.name=area/get_area
0.type=cpswarm_msgs/GetPoints
0.desc=Get the area boundaries.
1.name=area/get_center
1.type=cpswarm_msgs/GetPoint
1.desc=Get the center of the area.
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
3.name=~equi_dist
3.type=real
3.default=10.0
3.desc=Equilibrium distance between CPSs in meter.
4.name=~flock_vel
4.type=real
4.default=0.5
4.desc=Target velocity of the flock in meter per second.
5.name=~form_vel
5.type=real
5.default=0.5
5.desc=Maximum velocity during formation flight in meter per second.
6.name=~equi_dist
6.type=real
6.default=1.0
6.desc=
7.name=~repulse_spring
7.type=real
7.default=1.0
7.desc=Repulsion spring constant of half-spring per square second.
8.name=~repulse_max
8.type=real
8.default=1.0
8.desc=Maximum repulsion between CPSs in meter in order to avoid over excitation.
9.name=~align_frict
9.type=real
9.default=20.0
9.desc=Velocity alignment viscous friction coefficient in square meter per second. Higher values result in slower but more stable flocks.
10.name=~align_slope
10.type=real
10.default=1.0
10.desc=Constant slope around equilibrium distance in meter.
11.name=~align_min
11.type=real
11.default=1.0
11.desc=Minimum alignment between CPS in meter in order to avoid over excitation.
12.name=~wall_frict
12.type=real
12.default=20.0
12.desc=Bounding area viscous friction coefficient in square meter per second.
13.name=~wall_decay
13.type=real
13.default=1.0
13.desc=Softness of wall as decay width in meter.
14.name=~form_shape
14.type=real
14.default=1.0
14.desc=Strength of the shape forming velocity component in formation flight.
15.name=~form_track
15.type=real
15.default=1.0
15.desc=Strength of the tracking velocity component in formation flight.
16.name=~accel_time
16.type=real
16.default=1.0
16.desc=Characteristic time needed by the CPS to reach the target velocity in seconds.
}
}
```



## Acknowledgements

This work is supported by the European Commission through the
[CPSwarm H2020 project](https://cpswarm.eu) under grant no. 731946.
