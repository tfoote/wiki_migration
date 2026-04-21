## Overview

This package provides reactive grasp, reactive lift, and reactive
approach actions, and compliant close and grasp adjustment services for
the PR2 gripper. All of the above use the pressure sensors on the
fingertips to improve object grasping. Details on this module can be
found in the following paper:
[\*\*Contact-Reactive Grasping of Objects with Partial Shape Information\*\*](http://www.willowgarage.com/sites/default/files/contactreactive.pdf).

In order to use these actions and services, you probably want to launch
either

-   pr2_tabletop_manipulation_launch/launch/pr2_tabletop_manipulation.launch
    (no slip detection) or
-   pr2_tabletop_manipulation_launch/launch/pr2_tabletop_manipulation_slip.launch
    (with slip detection) NOTE: with trunk of c-turtle/d-turtle you must
    manually edit pr2_tabletop_manipulation.launch and set \<arg
    name=\"use_slip_controllers\" default=\"true\"/\>

## ROS API

-   The reactive approach action moves the gripper from a pre-grasp
    position to a grasp position while monitoring the fingertip sensors;
    unexpected tip contacts cause the gripper to back up and try to move
    around the object.

```{=html}
<!-- -->
```
-   The compliant close service closes the gripper while watching the
    fingertip sensors, so that seeing one contact early causes the arm
    to counter-move such that the finger that contacted first holds its
    position.

```{=html}
<!-- -->
```
-   The grasp adjustment service tries to adjust the position of the
    gripper relative to a grasp such that the contacts do not look
    unstable (contact only at the edge or only at the tip of the front
    of a fingertip sensor).

```{=html}
<!-- -->
```
-   The reactive grasp action executes reactive approach, followed by
    compliant close, followed by grasp adjustment, doing each step
    multiple times as necessary.

```{=html}
<!-- -->
```
-   The reactive lift action tries to lift an object while using the
    slip-avoidance controller in package slipgrip_controller to avoid
    crushing deformable objects more than is necessary to grasp them. It
    also leaves the slip-avoidance controller in slip-servo mode after
    it returns, so the controller can continue to adjust the grasp force
    as needed until the object is released.

### API Stability

The ROS API is UNREVIEWED and UNSTABLE

### ROS Parameters

```clearsilver
param {
  1.name= side_step
  1.default= .015 m
  1.type= double
  1.desc= How far to move to the side (in the direction of the tip that contacted) during reactive approach.
  2.name= back_step
  2.default= .03 m
  2.type= double
  2.desc= How far to back up when a tip contact is detected during reactive approach.
  3.name= approach_num_tries
  3.default= 5
  3.type= int
  3.desc= How many times to attempt to back up and move around upon detecting unexpected contacts during reactive approach.
  4.name= goal_pos_thres
  4.default= .01 m
  4.type= double
  4.desc= How close you have to be to the goal before reactive approach will ignore tip contacts (and assume it's at a goal that may have desired tip contact).
  5.name= min_contact_row
  5.default= 1
  5.type= int (between 0 and 5)
  5.desc= How far in contact has to be seen on the 5x3 front array of each fingertip pressure sensor (0=none/disable grasp adjustment in the gripper x-direction, 1=the row nearest to the tip,... 5=the row farthest in) for a grasp to be considered stable
  6.name= min_gripper_opening
  6.default= .0011 m
  6.type= double
  6.desc= If the gripper closes to a value lower than this, it will assume that it is empty.
  7.name= max_gripper_opening
  7.default= .1 m
  7.type= double
  7.desc= If the gripper closes and has a value higher than this, it will assume that the grasp failed (useful if you know the width of the desired grasp).
  8.name= grasp_adjust_x_step
  8.default= .02 m
  8.type= double
  8.desc= How far to move the gripper along the gripper x-axis during grasp adjustment when only tip contacts are seen
  9.name= grasp_adjust_z_step
  9.default= .015 m
  9.type= double
  9.desc= How far to move the gripper along the gripper +-z-axis during grasp adjustment when only edge contacts are seen
  10.name= grasp_num_tries
  10.default= 2
  10.type= int
  10.desc= Number of times to attempt the reactive approach (upon failure, if this param is more than 1, the gripper will move the goal forward by forward_step and perform reactive approach again).
  11.name= forward_step
  11.default= 0
  11.type= double
  11.desc= If non-zero, how far to move the goal forward before attempting reactive approach again.  If set to zero, defaults to 3 cm for grasps from the top and 6 cm for grasps from any other direction.
  12.name= close_force
  12.default= 100
  12.type= double
  12.desc= The gripper force to use when closing hard (used every time if use_slip_controller is false; used only if the grasp still looks unstable after adjustment if use_slip_controller is true) 
  13.name= use_slip_controller
  13.default= False
  13.type= bool
  13.desc= If True, uses the pr2_gripper_fingersensor_action; if False, uses the default pr2_gripper_action.  If this is False, reactive lift becomes just a Cartesian move up, and reactive grasp will always use close_force when closing on the object.
}
```

### Action APIs

The reactive_grasp_server node provides implementations of
\`SimpleActionServer\` (see [ actionlib documentation](actionlib )). The
action servers for reactive grasp and reactive approach take in goals
containing \`object_manipulation_msgs/ReactiveGraspGoal\` messages, and
the action server for reactive lift takes in goals containing
\`object_manipulation_msgs/ReactiveLiftGoal\` messages. You can
communicate with these nodes over ROS directly, but the recommended way
to send goals is by using the \`SimpleActionClient\`. Please see
[ actionlib documentation](actionlib ) for more information.

#### Reactive Grasp Action Subscribed Topics

```clearsilver
sub {
  no_header= True
  0.name= reactive_grasp/right/goal (or reactive_grasp/left/goal)
  0.type= object_manipulation_msgs/ReactiveGraspGoal
  0.desc= A goal for executing a reactive grasp.
  1.name= reactive_grasp/right/cancel (or reactive_grasp/left/cancel)
  1.type= actionlib_msgs/GoalID
  1.desc= A request to cancel a specific goal.
}
```

#### Reactive Grasp Action Published Topics

```clearsilver
pub {
  no_header= True
  0.name= reactive_grasp/right/status (or reactive_grasp/left/status)
  0.type= actionlib_msgs/GoalStatusArray
  0.desc= Provides status information on the goals that are sent to the reactive grasp action. 
  1.name= reactive_grasp/right/result (or reactive_grasp/left/result)
  1.type= object_manipulation_msgs/ReactiveGraspResult
  1.desc= Contains a result code of type object_manipulation_msgs/ManipulationResult, that indicates the final result of the reactive grasp.
}
```

#### Reactive Approach Action Subscribed Topics

```clearsilver
sub {
  no_header= True
  0.name= reactive_approach/right/goal (or reactive_approach/left/goal)
  0.type= object_manipulation_msgs/ReactiveGraspGoal
  0.desc= A goal for executing a reactive approach.
  1.name= reactive_approach/right/cancel (or reactive_approach/left/cancel)
  1.type= actionlib_msgs/GoalID
  1.desc= A request to cancel a specific goal.
}
```

#### Reactive Approach Action Published Topics

```clearsilver
pub {
  no_header= True
  0.name= reactive_approach/right/status (or reactive_approach/left/status)
  0.type= actionlib_msgs/GoalStatusArray
  0.desc= Provides status information on the goals that are sent to the reactive approach action. 
  1.name= reactive_approach/right/result (or reactive_approach/left/result)
  1.type= object_manipulation_msgs/ReactiveGraspResult
  1.desc= Contains a result code of type object_manipulation_msgs/ManipulationResult, that indicates the final result of the reactive approach.
}
```

#### Reactive Lift Action Subscribed Topics

```clearsilver
sub {
  no_header= True
  0.name= reactive_lift/right/goal (or reactive_lift/left/goal)
  0.type= object_manipulation_msgs/ReactiveLiftGoal
  0.desc= A goal for executing a reactive lift.
  1.name= reactive_lift/right/cancel (or reactive_lift/left/cancel)
  1.type= actionlib_msgs/GoalID
  1.desc= A request to cancel a specific goal.
}
```

#### Reactive Lift Action Published Topics

```clearsilver
pub {
  no_header= True
  0.name= reactive_lift/right/status (or reactive_lift/left/status)
  0.type= actionlib_msgs/GoalStatusArray
  0.desc= Provides status information on the goals that are sent to the reactive lift action. 
  1.name= reactive_lift/right/result (or reactive_lift/left/result)
  1.type= object_manipulation_msgs/ReactiveLiftResult
  1.desc= Contains a result code of type object_manipulation_msgs/ManipulationResult, that indicates the final result of the reactive lift.
}
```

### Services

Both the compliant close and grasp adjustment services use the
std_srvs/Empty service. (If you use these services and would prefer that
they be actions, or that they provide feedback of some sort, email
hsiao@willowgarage.com with your suggestions, and they\'re likely to be
implemented in a later release.)

The compliant close service is called
\`/l_reactive_grasp/compliant_close\` (or
\`/r_reactive_grasp/compliant_close\`) and the grasp adjustment service
is called \`/l_reactive_grasp/grasp_adjustment\` (or
\`r_reactive_grasp/grasp_adjustment\`).
