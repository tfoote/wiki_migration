## Overview

Package contains RVIZ plugin which serves as user interface for
[srs_assisted_arm_navigation](srs_assisted_arm_navigation), plugin for
assisted detection (bounding box estimation) and arm navigation state
visualizer.

## Assisted arm navigation user interface

![RVIZ plugin.\|width=200px](attachment:arm-nav-ui.png)

```clearsilver

sub {
  0.name= /but_arm_manip/state
  0.type=srs_assisted_arm_navigation_msgs/AssistedArmNavigationState
  0.desc= A state of arm navigation. 
}

srv{

  0.name= /but_arm_manip/arm_nav_start
  0.type= srs_assisted_arm_navigation_msgs/ArmNavStart
  0.desc= Called from assisted arm nav. node to enable controls and inform user about requested action.
}

param {
  0.name=~wait_for_start 
  0.default=`"true"`
  0.type= bool
  0.desc= If true, controls in plugin are disabled by default so, user can't start planning anytime.
}
```

Presets for goal positions can be defined in yaml file. Here is the
example with two presets, where first preset is relative position and
second absolute. Orientation can be specified as RPY (three values) or
as quaternion (four values). Presets are displayed in the user
interface.

```
arm_nav_presets:
 -
  name: Lift object
  position: [0.0, 0.0, 0.15]
  orientation: [0.0, 0.0, 0.0]
  relative: true
 -
  name: Hold position
  position: [-0.223, 0.046, 0.920]
  orientation: [0.020, 0.707, -0.706, 0.033]
  relative: false
```

## Assisted arm navigation state visualizer

Node for publishing text marker indicating state of arm planning - tells
user if the arm is in collision or the requested position is not
reachable etc. It needs *rviz_cam_add* TF frame published by assisted
arm navigation node to visualize text marker near the end effector when
planning.

![Text marker tells user if there is some problem.\|width=600px](attachment:statevis.png)

```clearsilver
pub {
  0.name= /but_arm_manip/state_vis
  0.type=visualization_msgs/MarkerArray
  0.desc= Marker with text informing user about state of current motion request. 
}
sub {
  0.name= /but_arm_manip/state
  0.type= srs_assisted_arm_navigation_msgs/AssistedArmNavigationState
  0.desc=  Current state of planning.
}
```

## Assisted detection (bounding box estimation)

RVIZ plugin for assisted object detection. Actionlib interface can be
called to get ROI of object in image stream. This ROI can be then
converted to 3D bounding box using [BB estimator](bb_estimator).

![Assisted detection pop-up window.\|width=600px](attachment:assist-det.png)

```clearsilver

sub {
  0.name= bb_video_in
  0.type= sensor_msgs/Image
  0.desc=  Video stream.
}

param {
  0.name=~is_video_flipped 
  0.default=`"true"`
  0.type= bool
  0.desc= If true, plugin will flip video horizontally.
}
```

##### Action Subscribed Topics

```clearsilver
sub {
  no_header= True
  0.name= /manual_bb_estimation_action/goal
  0.type= srs_assisted_arm_navigation_msgs/ManualBBEstimationGoal
  0.desc=Ask user to select ROI of object.
  1.name= /manual_bb_estimation_action/cancel
  1.type= actionlib_msgs/GoalID
  1.desc= A request to cancel given task.
}
```

##### Action Published Topics

```clearsilver
pub {
  no_header= True
  0.name= /manual_bb_estimation_action/feedback
  0.type= srs_assisted_arm_navigation_msgs/ManualBBEstimationFeedback
  0.desc= Feedback contains the current selected ROI.

  1.name= /manual_bb_estimation_action/status
  1.type= actionlib_msgs/GoalStatusArray
  1.desc= Provides status information on the goal.

  2.name= /manual_bb_estimation_action/result
  2.type= srs_assisted_arm_navigation_msgs/ManualBBEstimationResult
  2.desc= Result contains final ROI.
}
```

Example of action client for assisted detection plugin can be found in
*detect_unknown_object_assisted* SMACH generic state implemented in
[srs_arm_navigation_tests](srs_arm_navigation_tests).
