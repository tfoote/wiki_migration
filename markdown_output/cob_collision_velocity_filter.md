The `cob_collision_velocity_filter` reads the obstacles from a
rolling-window costmap and the velocity commands published by a teleop
device. It then computes relevant obstacles in driving direction and
slows down if it gets closer to them. It then stops the robot at a
specific threshold.

**Note:** The `cob_collision_velocity_filter` only works with
rectangular footprints at the moment.

## Hardware Requirements

To use this package you need either need a real or a simulated
Care-O-Bot (see [cob_bringup](cob_bringup) and
[cob_bringup_sim](cob_bringup_sim) respectively).

## ROS API

The [cob_collision_velocity_filter](cob_collision_velocity_filter)
package provides a configurable node for collision avoidance using
teleoperation devices 

```clearsilver
 name = cob_collision_velocity_filter
 desc = The `cob_collision_velocity_filter` node takes in [[http://ros.org/doc/api/geometry_msgs/html/msg/Twist.html|geometry_msgs/Twist]] messages from the teleop device as well as [[http://ros.org/doc/api/nav_msgs/html/msg/GridCells.html|nav_msgs/GridCells]] messages specifying the obstacles on the costmap. The safe movement commands are published as a [[Topics|topic]], as well as the extracted relevant obstacles in driving direction. It further periodically tries to call the `/get_footprint` service of [[cob_footprint_observer]] to check for changed footprints and adjusts the used one accordingly.

goal{
}

result{
}

feedback{
}

sub{
 0.name = teleop_twist
 0.type = geometry_msgs/Twist
 0.desc = unsafe movement command of the teleop device

 1.name = obstacles
 1.type = nav_msgs/GridCells
 1.desc = obstacles on a rolling-window costmap
}

pub{
 0.name = command
 0.type = geometry_msgs/Twist
 0.desc = safe movement command

 1.name = relevant_obstacles
 1.type = nav_msgs/GridCells
 1.desc = obstacles in driving direction
}

srv{
}

param{
 0.name = ~costmap_parameter_source
 0.type = string
 0.default = "/local_costmap_node/costmap"
 0.desc = Specifies which node to search for the initial footprint, footprint_padding, etc., e.g. /local_costmap_node/costmap.

 1.name = ~footprint_update_frequency
 1.type = double
 1.default = 1.0 [Hz]
 1.desc = Frequency at which footprint is adjusted using the `/get_footprint` service from `cob_footprint_observer`.

 2.name = ~pot_ctrl_vmax
 2.type = double
 2.default = 0.6
 2.desc = Maximum allowed velocity for safe movements.

 3.name = ~pot_ctrl_vtheta_max
 3.type = double
 3.default = 0.8
 3.desc = Maximum allowed rotational velocity for safe movements.

 4.name = ~pot_ctrl_kv
 4.type = double
 4.default = 1.0
 4.desc = Damping term for potential field like controller for slow down behaviour.

 5.name = ~pot_ctrl_kp
 5.type = double
 5.default = 2.0
 5.desc = Stiffness term for potential field like controller for slow down behaviour.

 6.name = ~pot_ctrl_virt_mass
 6.type = double
 6.default = 0.8
 6.desc = Virtual mass term for potential field like controller for slow down behaviour.

 7.name = ~influence_radius
 7.type = double
 7.default = 1.5 [m]
 7.desc = max distance of obstacles from robot center that are used for computing relevant obstacles.

 8.name = ~obstacle_damping_dist
 8.type = double
 8.default = 5.0 [m]
 8.desc = Distance in driving direction at which potential field like slow down controller starts to work.

 9.name = ~stop_threshold
 9.type = double
 9.default = 0.1 [m]
 9.desc = Distance to `relevant_obstacle` at which robot stops to move completely.

 10.name = ~use_circumscribed_threshold
 10.type = double
 10.default = 0.2 [rad/s]
 10.desc = Minimal rotational velocity at which circumscribed_radius should be used for collision avoidance while translational velocities are present. Has no influence when robot is only moving rotationally because then it is the rotational movement is the only critical one and thus is taken into account nonetheless. 

}

req_tf{
}

prov_tf{
}
```



## Usage/Examples

For starting the `cob_collision_velocity_filter` use


```
roslaunch cob_bringup base_collision_observer.launch
```

 This launches the required rolling window
[costmap_2d](costmap_2d) as well as the optional
[cob_footprint_observer](cob_footprint_observer). If you don't want to
use the [cob_footprint_observer](cob_footprint_observer) simply comment
or delete the respective lines in the launch file. For including the
`collision_velocity_filter` in your overall launch file use


```
<include file=$(find cob_bringup/tools/base_collision_observer.launch />
```

 A sample parameter file for the
[cob_collision_velocity_filter](cob_collision_velocity_filter) can look
like this: 

```
#where to look for costmap parameters
costmap_parameter_source: "/local_costmap_node/costmap" #default "/local_costmap_node/costmap"

#frequency at which the get_footprint service should be called
footprint_update_frequency: 0.5

#Parameters specifying slow down behaviour
pot_ctrl_vmax: 0.6 #default: 0.6
pot_ctrl_vtheta_max: 0.6 #default: 0.8
pot_ctrl_kv: 2.5 #damping default: 1.0
pot_ctrl_kp: 3.0 #stiffness default: 2.0
pot_ctrl_virt_mass: 0.5 #default: 0.8

#Parameters specifying collision velocity filter 
influence_radius: 2.0 #[m] distance from robot_center
obstacle_damping_dist: 1.0 # used as slow-down dist
stop_threshold: 0.1 #[m]
use_circumscribed_threshold: 0.2 #[rad/s]
```


