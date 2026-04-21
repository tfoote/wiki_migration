## Overview

The ee_cart_imped_control (for End Effector Cartesian Impedance Control)
implements a controller that executes trajectories for force/impedance
control of the end effector of a chain of joints. Each point on the
trajectory specifies a wrench or a stiffness around a Cartesian degree
of freedom as well as a Cartesian position and orientation. For a degree
of freedom, if a stiffness is specified, the controller will attempt to
reach the position given with that stiffness (mimicking a proportional
position controller). If a wrench is specified, the position information
is ignored.

The controller is an open-loop Jacobian-transpose force controller. At
every point on the trajectory the desired stiffness or desired wrench is
converted into a Cartesian force/wrench vector and ultimately into a
joint torque vector using the transpose of the arm's instantaneous
Jacobian matrix. No guarantee is made to the *magnitude* of the applied
force/wrench/impedance because this is an open-loop controller. There is
currently not adequate feedback on the arm to determine the applied
force/wrench/impedance. Joint stiction, joint position limits, motor
torque limits, and sometimes the arm configuration (at a singularity,
for example) will cause the applied force/wrench/impedance to deviate
from the desired values. Generally, unless the arm is at a singularity
or a joint is at its limit, the *direction* of the
force/wrench/impedance will be correct.

The controller takes trajectory points and linearly interpolates, in
Cartesian space, between positions and orientations. However, it does
not interpolate between force or stiffness, but simply holds the
requested force or stiffness constant for each segment.

This controller should never be used directly; rather, all interaction
with it should take place through the
[ee_cart_imped_action](ee_cart_imped_action).

## Videos

[Youtube](https://www.youtube.com/watch?v=Z9Pnj2UzPq0)

In this video, the PR2 first moves its gripper to the center of its body
and then applies a constant force in the *x* direction (towards/away
from the robot). As you can see, the force is light so the human can
easily stop the motion. However, with no intervention, the robot hand
will continue to move as far in the *x* direction as it can go. There is
no sense of trying to achieve a goal in this direction. This type of
control is useful if you wish to exert a constant force against
something.

[Youtube](https://www.youtube.com/watch?v=AfRUwsIOvqo)

In this video, the PR2 first moves its gripper to the center of its body
and then tries to extend the gripper about 25 cm farther away, but with
low stiffness in the *x* direction (towards/away from the robot). Since
the stiffness is low, it is easy for a human to move the hand away from
the center of the body in the *x* direction and it returns slowly. In
the *y* and *z* directions, however, where the stiffness is set to the
maximum, it takes a lot of strength to displace the gripper and it
returns very quickly to its set point.

[Youtube](https://www.youtube.com/watch?v=FOkAt_EMZLA)

This controller is useful for any activity in which it is necessary to
use less than the full strength of the arms. This video shows several
short clips of the PR2 using the force/impedance controller for various
tasks.

For even more videos, see the
[ CSAIL ee_cart_imped videos](http://projects.csail.mit.edu/pr2/videos/ee_cart_imped/ ).

## ROS API

### Parameters



```clearsilver
param{
  0.name=root_name
  0.type=string
  0.desc=The base frame in which the end effector motion will be specified.
  1.name=tip_name
  1.type=string
  1.desc=The frame of the tip
}
```



Example configuration (from
[ee_cart_imped_control](ee_cart_imped_control)/pr2_arms_cart_imped_controller.yaml):



```yaml
r_arm_cart_imped_controller:
  type: EECartImpedControlPlugin
  root_name: torso_lift_link
  tip_name: r_gripper_tool_frame
```



### Topics



```clearsilver
pub{
  0.name=state
  0.type=ee_cart_imped_msgs/EECartImpedFeedback
  0.desc=Current state of the controller, including the current and desired positions and orientations, the desired force or stiffness, and the force or stiffness passed to the joints (TODO: Make this the actual joint effort in Cartesian space).
}
```





```clearsilver
sub{
  0.name=command
  0.type=ee_cart_imped_msgs/EECartImpedGoal
  0.desc=The trajectory to follow.  The absolute start time of the trajectory is given in header.stamp.  If forces are specified, the controller will try to exert that force in the correct direction throughout the trajectory segment.  If stiffness is specified, the controller will try to achieve the desired segment point with that stiffness.  At the end of the trajectory, the controller holds the last point.
}
```



## Closed Loop Control

As written, the force control is open-loop because there is no force
sensor in the PR2 arm. This creates anomalous behavior when the force
being applied by the controller is not enough to overcome the static
friction in the joints. At the moment, it is up to the user to work
around this problem. For example, when the gripper is in contact with a
surface, the gripper force sensors can be used as feedback. Although the
controller itself cannot integrate this information, it can be done a
higher level using the information from the
"/pressure/r_gripper_motor" or "/pressure/l_gripper_motor" topics.
Similarly, ensuring that the end effector moves a certain distance while
constantly exerting a force in that direction (as in pushing an object)
can be done by monitoring the position of the gripper and exerting ever
greater forces until it begins to move. In the video below, the PR2 is
using the ee_cart_imped controller to exert a light force on the table
and the gripper fingertip sensors to decide whether it is currently on
the table.

[Youtube](https://www.youtube.com/watch?v=jXk0sjKJ1ho)

Video credit: Dylan Hadfield-Menell, Thomas Garver
