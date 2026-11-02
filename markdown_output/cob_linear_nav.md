The cob_linear_nav package provides a
configurable node for simple navigation. It drives the robot on a linear
path from its current position to its goal position **without any
obstacle avoidance**. This should be carried out in another package. If
the robot doesn't move anymore (e.g. due to an obstacle that stays on
the robot path), the robot stops trying to reach the goal after a
certain period of time (to be specified over a parameter).

## ROS API



```clearsilver
 name = cob_linear_nav
 desc = The `cob_linear_nav` node takes in [[http://ros.org/doc/api/geometry_msgs/html/msg/PoseStamped.html|geometry_msgs/PoseStamped]] messages as a new goal, as well as [[http://ros.org/doc/api/nav_msgs/html/msg/Odometry.html|nav_msgs/Odometry]] messages specifying the odometry of the robot. The movement commands are published as a [[http://ros.org/doc/api/geometry_msgs/html/msg/Twist.html|geometry_msgs/Twist]] [[Topics|topic]]. It also provides the ability to send a goal using [[rviz]] on the ''/move_base_linear_simple/goal'' topic.

goal{
}

result{
}

feedback{
}

sub{
 0.name = /move_baser_linear_simple/goal
 0.type = geometry_msgs/PoseStamped
 0.desc = new goal for the robot

 1.name = odom
 1.type = nav_msgs/Odometry
 1.desc = odometry of the robot
}

pub{
 0.name = cmd_vel
 0.type = geometry_msgs/Twist
 0.desc = movement command to robot base
}

srv{
}

param{
 1.name = ~kv
 1.type = double
 1.default = 2.5
 1.desc = Damping term for potential field like controller for translational movement.

 2.name = ~kp
 2.type = double
 2.default = 3.0
 2.desc = Stiffness term for potential field like controller for translational movement.

 3.name = ~virt_mass
 3.type = double
 3.default = 0.5
 3.desc = Virtual mass term for potential field like controller for translational movement.

 4.name = ~vmax
 4.type = double
 4.default = 0.3
 4.desc = Maximum allowed velocity for translational movement.

 5.name = ~goal_threshold
 5.type = double
 5.default = 0.03 [m]
 5.desc = Distance to goal at which robot considers to have reached the goal (translational movement only).

 6.name = ~speed_threshold
 6.type = double
 6.default = 0.08
 6.desc = Speed at which the robot considers to have stopped (translational movement only).

 7.name = ~kv_rot
 7.type = double
 7.default = 2.5
 7.desc = Damping term for potential field like controller for rotational movement.

 8.name = ~kp_rot
 8.type = double
 8.default = 3.0
 8.desc = Stiffness term for potential field like controller for rotational movement.

 9.name = ~virt_mass_rot
 9.type = double
 9.default = 0.5
 9.desc = Virtual mass term for potential field like controller for rotational movement.

 10.name = ~vtheta_max
 10.type = double
 10.default = 0.3
 10.desc = Maximum allowed rotational velocity for movement.

 11.name = ~goal_threshold_rot
 11.type = double
 11.default = 0.08
 11.desc = Distance to goal at which robot considers to have reached the goal (rotational movement only).

 12.name = ~speed_threshold_rot
 12.type = double
 12.default = 0.08
 12.desc = Speed at which the robot considers to have stopped (rotational movement only).

 13.name = ~global_frame
 13.type = string
 13.default = "/map"
 13.desc = Map frame.

 14.name = ~robot_frame
 14.type = string
 14.default = "/base_link"
 14.desc = Frame of robot which is considered to be the frame that should reach the goal position.

 15.name = ~slow_down_distance
 15.type = double
 15.default = 0.5 [m]
 15.desc = Distance to goal at which the robot starts slowing down.

 16.name = ~goal_abortion_time
 16.type = double
 16.default = 5.0 [s]
 16.desc = Time after which the robot stops trying to reach the goal, if it does not move anymore (as indicated by the odometry). This happens when the movement is stopped by an external collision avoidance function due to e.g. obstacles on the linear path.
}

req_tf{
}

prov_tf{
}
```



## Usage/Examples

For the usage of cob_linear_nav, have a
look at
[cob_navigation_global](https://index.ros.org/p/cob_navigation_global)
and the `2dnav_linear.launch` and `2dnav_linear.xml` files therein.

A sample parameter file (currently in
[cob_navigation_config](https://index.ros.org/p/cob_navigation_config)`/common/linear/ctrl_params.yaml`)
can look like this: 

```
#Parameters designing the potential field controller
#Translational part
kv: 2.50 #damping 2.50
kp: 3.00 #stiffness 3.0
virt_mass: 0.50 #0.50
vmax: 0.3 #0.3
goal_threshold: 0.03 #0.03
speed_threshold: 0.08 #0.08

#Rotational part
kv_rot: 2.0 #damping 2.0
kp_rot: 2.0 #stiffness 2.0
virt_mass_rot: 0.50 #0.5
vtheta_max: 0.3 # 0.3
goal_threshold_rot: 0.08 #0.08
speed_threshold_rot: 0.08 #0.08

#tf parameters
global_frame: /map #/map
robot_frame: /base_link #/base_link

slow_down_distance: 0.5 #0.5[m] distance from robot_center to goal at which robot starts slowing down
goal_abortion_time: 5.0 #5.0[s] time until robot aborts goal due to obstacle
```
