## State Documentation

### Manipulation states

#### move_arm_to_given_positions_assisted

Description: Allows remote operator to navigate arm to calculated
pregrasp positions for known object.

Source File: `arm_manip_states.py`

input_keys:
`['list_of_target_positions','list_of_id_for_target_positions','name_of_the_target_object','pose_of_the_target_object','bb_of_the_target_object']`

output_keys: `['id_of_the_reached_position']`

outcomes: `['completed','not_completed','failed','pre-empted','repeat']`

#### move_arm_from_a_given_position_assisted

Description: Allows remote operator to navigate arm to safe position.

Source File: `arm_manip_states.py`

input_keys: none

output_keys: none

outcomes: `['completed','not_completed','failed','pre-empted']`

#### grasp_unknown_object_assisted

Description: Allows remote operator to grasp unknown object.

Source File: `arm_manip_states.py`

input_keys: tbd

output_keys: tbd

outcomes: `['completed','not_completed','failed','pre-empted']`

#### select_srs_grasp

Description: Selects a grasp for a given object.

Source File: `srs_grasp_states.py`

input_keys: `['object', 'target_object_id']`

output_keys: `['grasp_configuration', 'poses']`

outcomes: `['succeeded', 'not_possible', 'failed', 'preempted']`

#### srs_grasp

Description: Grasp the object.

Source File: `srs_grasp_states.py`

input_keys: `['grasp_configuration','grasp_configuration_id']`

output_keys: `['grasp_categorisation']`

outcomes: `['succeeded','not_completed','failed', 'preempted']`

#### grasp_base_pose_estimation

Description: Estimate the best grasp position.

Source File: `srs_grasp_states.py`

input_keys: `['object','target_workspace_name']`

output_keys: `['base_pose']`

outcomes: `['retry', 'not_retry', 'failed', 'preempted']`

### Navigation states

tbd

### Perception states

tbd
