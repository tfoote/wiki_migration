## Nodes

```clearsilver
node.0 {
 name = artstage
 desc = Modified version of stage/stageros customized to the needs of the ART vehicle.  Provides a 2D simulation of the vehicle using a model of the vehicle's response to simulated actuator settings.
 pub {
  0.name = odom
  0.type = nav_msgs/Odometry
  0.desc = three-dimensional odometry of simulated vehicle
  1.name = ground_truth
  1.type = nav_msgs/Odometry
  1.desc = true pose of simulated vehicle
  2.name = clock
  2.type = roslib/Clock
  2.desc = simulated time (if use_sim_time)
  3.name = laser/front
  3.type = sensor_msgs/LaserScan
  3.desc = simulated front Sick laser scans
 }
prov_tf {
  0.from = /odom
  0.to   = /vehicle
  0.desc = pose of simulated vehicle in the odometry frame of reference
 }
sub {
  0.name = brake/state
  0.type = art_msgs/BrakeState
  0.desc = simulated brake position
  1.name = shifter/state
  1.type = art_msgs/Shifter
  1.desc = transmission gear currently selected
  2.name = steering/state
  2.type = art_msgs/SteeringState
  2.desc = simulated steering wheel position
  3.name = throttle/state
  3.type = art_msgs/ThrottleState
  3.desc = simulated throttle position
 }
param {
  0.name = ~latitude
  0.type = double
  0.desc = latitude of map center
  0.default = 29.446018
  1.name = ~longitude
  1.type = double
  1.desc = longitude of map center
  1.default = -98.607024
  4.name = ~use_sim_time
  4.type = bool
  4.desc = publish simulated clock topic, if true
  4.default = true
  6.name = ~world_file
  6.type = str
  6.desc = Stage world file name
  6.default = command line argument
 }
}
```

#### Usage

```
rosrun simulator_art artstage <world>
```

Where \`\<world\>\` is the full path name of the stage world file to
load. To run one of the world files included in this package, resolve it
like this (all on one line):

```
rosrun simulator_art artstage $(rospack find simulator_art)/world/swri_site_visit.world
```

## To Do

-   Improve vehicle model.
-   Simulate additional lasers.
-   Handle multiple vehicles.
