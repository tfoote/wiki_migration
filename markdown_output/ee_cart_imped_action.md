## Overview

The ee_cart_imped_action is a node that provides an action interface for
the [ee_cart_imped_control](ee_cart_imped_control) node. Specifically,
it allows tracking trajectories that involve force control and sending
goals and cancel signals to the controller. The action can also put
constraints on the trajectory and aborts trajectory execution when the
constraints are violated. All interaction with the
[ee_cart_imped_control](ee_cart_imped_control) package should be done
through this action interface.

![](attachment:interface.png)

The force/impedance controller is useful for many different tasks:

[Youtube](https://www.youtube.com/watch?v=1ZB383ktTWk)

For more videos, look at the
[ee_cart_imped_control documentation](ee_cart_imped_control#Videos).

## ROS API

The ROS API consists of three parts: parameters, the action server, and
an interface to the EECartImped Controller.

### Parameters



```clearsilver
param {
  0.name=constraints/goal/time
  0.type=double
  0.default=0.0
  0.desc=The amount of time (in seconds) that the controller is permitted to be late to the goal.  If goal_time has passed after the goal should have been completed and the controller still has not reached the final position, then the goal is aborted.
  2.name=constraints/goal/
  2.type=geometry_msgs/Pose
  2.default=-1.0 for all entries
  2.desc=The maximum final error in pose for the trajectory goal to be considered successful.  Negative numbers indicate that there is no constraint.  If the goal position specifies force in any Cartesian DOF, the position constraints in that DOF are ignored.  If the controller does not reach the goal point to within these constraints in the allowed time, the goal is aborted.
  3.name=constraints/goal/effort
  3.type=double
  3.default=-1.0
  3.desc=The maximum error allowed in the squared difference between the joint efforts.  A negative number indicates there is no constraint.  The PR2 does not have force sensors that allow us to close the loop so this is simply the difference between the efforts the joints are commanded to produce and the efforts they are actually able to produce.  If the goal position does not specify force in any DOF, this constraint is ignored.
  4.name=constraints/trajectory/
  4.type=geometry_msgs/Pose
  4.default=-1.0 for all entries
  4.desc=The maximum error in pose at any point during execution of the trajectory.  Negative numbers indicate that there is no constraint.  If the current trajectory point specifies force in one Cartesian DOF, the position constraints in that DOF are ignored.  If this constraint is violated at any time, the goal is aborted.  This is ''not'' a constraint on how far from a trajectory point the current point can be; rather it is a constraint on the error between the point the controller should currently be trying to reach according to the interpolation and the point at which the end effector actually is.
  5.name=constraints/trajectory/effort
  5.type=double
  5.default=-1.0
  5.desc=The maximum error allowed in the squared difference between the joint efforts during the trajectory.  A negative number indicates there is no constraint.  The PR2 does not have force sensors that allow us to close the loop so this is simply the difference between the efforts the joints are commanded to produce and the efforts they are actually able to produce.  If the current trajectory point does not specify force in any DOF, this constraint is ignored.
```



Example configuration (from
[ee_cart_imped_control](ee_cart_imped_control)/pr2_arms_cart_imped_controller.yaml):



```
r_arm_cart_imped_action_node:
    constraints:
      goal:
        time: 0.0
        position:
          x: 0.2
          y: 0.2
          z: 0.2
        orientation:
          x: 0.2
          y: 0.2
          z: 0.2
          w: 0.2
        effort: 0.002
      trajectory:
        effort: -1.0
```



### Action Interface

The EECartImpedAction provides an
[ action server](actionlib#Implementing_an_ActionServer ) that takes in
goals of the type
[ee_cart_imped_msgs/msg/EECartImpedActionGoal](https://docs.ros.org/en/rolling/p/ee_cart_imped_msgs/msg/EECartImpedActionGoal.html)
and publishes feedback of the type
[ee_cart_imped_msgs/msg/EECartImpedActionFeedback](https://docs.ros.org/en/rolling/p/ee_cart_imped_msgs/msg/EECartImpedActionFeedback.html).



```clearsilver
sub {
  0.name=ee_cart_imped_action/goal
  0.type=ee_cart_imped_msgs/EECartImpedActionGoal
  0.desc=The goal describes the trajectory with force control for the robot to follow.
  1.name=ee_cart_imped_action/cancel
  1.type=actionlib_msgs/GoalID
  1.desc=A request to cancel a specific goal.
}
pub {
  0.name=ee_cart_imped_action/feedback
  0.type=ee_cart_imped_msgs/EECartImpedActionFeedback
  0.desc=Feedback describing the progress the mechanism is making on following the trajectory with force control.  Gives both the desired trajectory and the current trajectory.
  1.name=ee_cart_imped_action/status
  1.type=actionlib_msgs/GoalStatusArray
  1.desc=Provides status information on the goals that are sent to the action.
  2.name=ee_cart_imped_action/result
  2.type=ee_cart_imped_msgs/EECartImpedActionResult
  2.desc=Publishes information about the result of the last goal.
}
```



### Controller Interface



```clearsilver
sub {
  0.name=state
  0.type=ee_cart_imped_msgs/EECartImpedFeedback
  0.desc=Listens to the state of the controller.  Uses this subscription to monitor the trajectory.
}
pub {
  0.name=command
  0.type=ee_cart_imped_msgs/EECartImpedGoal
  0.desc=Sends trajectories with force control to the controller.
}
```



## Usage

In general, interaction with the action server should take place through
an action client. To facilitate this process, we have written C++ and
python wrappers around the
[ simple action client](actionlib#C.2B-.2B-_SimpleActionClient ) and
included them in the package. To use the these clients, look at their
code APIs
[(c++)](http://www.ros.org/doc/api/ee_cart_imped_action/html/c++/classEECartImpedArm.html )
[(python)](http://www.ros.org/doc/api/ee_cart_imped_action/html/python/ee_cart_imped_action.EECartImpedClient-class.html)
or the [tutorials](ee_cart_imped/Tutorials).
