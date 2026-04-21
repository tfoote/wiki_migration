# Overview

This package contains many useful states and state machines for
commanding a Care-O-bot.

# State Machine Usage and Documentation

## ApproachPoses

Approaches a pose or a list of poses and checks the accessibility for
moving to these poses beforehand with the services provided by
cob_map_accessibility_analysis. To use this state machine the map
analysis has to be started first: ```
roslaunch cob_map_accessibility_analysis map_accessibility_analysis.launch
```

### Input keys

goal_poses:: Array of geometry_msgs/Pose2D objects, each describing a
goal position of the robot. goal_pose_application:: Defines the mode of
usage of the provided goal poses: 'visit_all_in_order' (commands the
robot to all poses in the provided order),\
'visit_all_nearest' (commands the robot to all poses using the closest
next pose each time),\
'use_as_alternatives' (visits the first pose of the list that is
reachable).\
Independent of the mode, this state machine always terminates once a
goal position could be reached, so for the visit_all modes the
state_machine has to be called until 'not_reached' is returned from
'SELECT_GOAL'. Internally, the remaining, not yet visited states, are
stored in the list 'goal_poses_verified' for the visit_all modes.
new_computation_flag:: If True, the provided list of poses is examined
for accessibility, else the old list from userdata.goal_poses_verified
is used again. This variable is used by the visit_all modes, which work
on the already existing list of goal poses after the first call.

### Output_keys

new_computation_flag:: see above

## ApproachPerimeter

Approaches a pose on the perimeter of a circle and checks the
accessibility for moving to this pose beforehand with the services
provided by cob_map_accessibility_analysis. To use this state machine
the map analysis has to be started first: ```
roslaunch cob_map_accessibility_analysis map_accessibility_analysis.launch
```

### Input keys

center:: Pose2D defining the center point of the circle to be visited.
You may provide an orientation angle as well, which defines the
"viewing direction" of the target. radius:: Double value of the radius
of the circle. rotational_sampling_step:: Double value of the angular
sampling step with in \[rad\] of goal poses on the perimeter of the
circle. goal_pose_selection_strategy:: Defines which of the possible
poses on the circle shall be preferred:
'closest_to_target_gaze_direction' (commands the robot to the pose
which is closest to the target's viewing direction, useful e.g. for
living targets),\
'closest_to_robot' (commands the robot to the pose closest to the
current robot position, useful e.g. for inspecting a location).\
Independent of the mode, this state machine always terminates once a
goal position could be reached, however, to visit multiple locations on
the same circle the state_machine has to be called with
'new_computation_flag' set to False and an appropriate
'invalidate_other_poses_radius' until 'not_reached' is returned from
'SELECT_GOAL'. Internally, the remaining, not yet visited states, are
stored in the list 'goal_poses_verified'.
invalidate_other_poses_radius:: Within a circle of this radius (in
\[m\]) around the current goal pose all other valid poses become deleted
from userdata.goal_poses_verified so that the next accessible pose a a
certain minimum distance from the current goal pose.
new_computation_flag:: If True, the poses on the defined circle are
examined for accessibility, else the old list from
userdata.goal_poses_verified is used again. This variable is used to
command the robot to different perspectives on the same goal, which are
computed at the first call of this state machine.

### Output_keys

new_computation_flag:: see above

## ApproachPolygon

Approaches one or multiple poses on the perimeter of an arbitrary
polygon and checks the accessibility for moving to this pose beforehand
with the services provided by cob_map_accessibility_analysis. To use
this state machine the map analysis has to be started first:
```
roslaunch cob_map_accessibility_analysis map_accessibility_analysis.launch
```

### Input keys

polygon:: cob_3d_mapping_msgs/Shape defining the polygon whose perimeter
is to be visited by the robot. invalidate_other_poses_radius:: Within a
circle of this radius (in \[m\]) around the current goal pose all other
valid poses become deleted from userdata.goal_poses_verified so that the
next accessible pose a a certain minimum distance from the current goal
pose. new_computation_flag:: If True, the poses on the defined circle
are examined for accessibility, else the old list from
userdata.goal_poses_verified is used again. This variable is used to
command the robot to different perspectives on the same goal, which are
computed at the first call of this state machine. This state machine
always terminates once a goal position could be reached, however, to
visit multiple locations around the same polygon the state_machine has
to be called with 'new_computation_flag' set to False and an
appropriate 'invalidate_other_poses_radius' until 'not_reached' is
returned from 'SELECT_GOAL'. Internally, the remaining, not yet
visited states, are stored in the list 'goal_poses_verified'.

### Output_keys

new_computation_flag:: see above
