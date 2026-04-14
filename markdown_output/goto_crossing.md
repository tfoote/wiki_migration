The goto_crossing provides a Go-To-Goal behavior to reach the center of
a crossing (\<\<SrvLink(lama_msgs/Crossing)\>\> message) for the Large
Maps Framework ([LaMa](Large Maps Framework)).

## Overview

The goto_crossing provides a Go-To-Goal behavior to reach the center of
a crossing (\<\<SrvLink(lama_msgs/Crossing)\>\> message).

Can be used as a ROS node or as a class instance, as documented below.

## Usage

### As ROS Node

Launch the node with \`rosrun goto_crossing goto_crossing\`.

### As Class Instance

To use the \`goto_crossing::CrossingGoer\` as class instance, one uses
\`goto_crossing::CrossingGoer::goto_crossing\` to compute the twist
necessary to reach the crossing center: ```cplusplus
#include <geometry_msgs/Twist.h>
#include <goto_crossing/crossing_goer.h>
#include <lama_msgs/Crossing.h>

goto_crossing::CrossingGoer crossing_goer;

lama_msgs::Crossing crossing;
geometry_msgs::Twist twist;
crossing.center.x = 0.56;
crossing.center.y = 0.24;
const bool goal_reached = crossing_goer.goto_crossing(crossing, twist);
```

To reset the integral parts of the PI-controller, use
```cplusplus
crossing_goer.resetIntegrals();
```

## ROS API

```clearsilver
sub { 
   0.name=~<name>/crossing
   0.type= lama_msgs/Crossing
   0.desc= Crossing which `center` attribute is the goal relative to the robot. 
}
pub {
  0.name= ~<name>/cmd_vel
  0.type= geometry_msgs/Twist
  0.desc= The set velocities to reach the goal
  1.name= ~<name>/goal_reached
  1.type= std_msgs/Bool
  1.desc= True if the goal is within `reach_distance`
}
srv {
  0.name= ~<name>/reset_integrals
  0.type= std_srvs/Empty
  0.desc= Reset the integrated sum of errors
}
param {
  0.name= ~<name>/kp_v
  0.type= float
  0.desc= Proportional gain for the linear velocity (s^-1)

  1.name= ~<name>/kp_w
  1.type= float
  1.desc= Proportional gain for the angular velocity (s^-1)

  2.name= ~<name>/ki_v
  2.type= float
  2.desc= Integral gain for the linear velocity (s^-2)

  3.name= ~<name>/ki_w
  3.type= float
  3.desc= Integral gain for the angular velocity (s^-2)

  4.name= ~<name>/min_linear_velocity
  4.type= float
  4.desc= Minimum linear set velocity (m.s^-1), used if the integral gain is 0

  5.name= ~<name>/max_linear_velocity
  5.type= float
  5.desc= Maximum linear set velocity (m.s^-1). If set to 0, the linear velocity is not throttled.

  6.name= ~<name>/min_angular_velocity
  6.type= float
  6.desc= Minimum angular set velocity (m.s^-1), used if the integral gain is 0

  7.name= ~<name>/max_angular_velocity
  7.type= float
  7.desc= Maximum angular set velocity (rad.s^-1). If set to 0, the angular velocity is not throttled.

  8.name= ~<name>/reach_distance
  8.type= float
  8.desc= Goal is reached if closer than this (m)

  9.name= ~<name>/dtheta_force_lef
  9.type= float
  9.desc= If the goal is behind the robot, force the robot to turn left if the goal angle is within [pi - dtheta_force_left_, pi], even if the angle difference would tell that we should turn right. This is to avoid instability in the case that the angle would oscillate around pi. (rad)

  10.name= ~<name>/threshold_w_only
  10.type= float
  10.desc= If dtheta is greater than this, only turn, do not go forward (rad)

  11.name= ~<name>/max_sum_v
  11.type= float
  11.desc= Anti wind-up for sum_v (m.s)

  12.name= ~<name>/max_sum_w
  12.type= float
  12.desc= Anti wind-up for sum_w_ (rad.s)}
```
