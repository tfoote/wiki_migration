Note that these launch files do not include sensor data processing, an
implementation of which can be found in
[tabletop_object_perception](tabletop_object_perception). Launch files
combining manipulation (as contained here) and perception can be found
in [pr2_tabletop_manipulation_launch](pr2_tabletop_manipulation_launch).
Once started, the manipulation pipeline is ready to serve requests for
tasks such as object pickup and placing.

## PR2 Gripper Hand Description

This package also contains configuration files with the description of a
PR2 arm equipped with a gripper as needed by the manipulation pipeline.
The format of an arm/hand description is documented in the
[object_manipulator](object_manipulator) page. Here is an example of
such a configuration file:



```
hand_description:
  right_arm:
    hand_frame: r_wrist_roll_link
    robot_frame: base_link
    attached_objects_name: attached
    attach_link: r_gripper_r_finger_tip_link
    hand_group_name: r_end_effector
    arm_group_name: right_arm
    hand_database_name: WILLOW_GRIPPER_2010
    hand_joints: [r_gripper_l_finger_joint,r_gripper_r_finger_joint,r_gripper_r_finger_tip_joint,r_gripper_l_finger_tip_joint]
    hand_touch_links: [r_gripper_palm_link,r_gripper_r_finger_tip_link,r_gripper_l_finger_tip_link,r_gripper_l_finger_link,r_gripper_r_finger_link]
    hand_fingertip_links: [r_gripper_r_finger_tip_link,r_gripper_l_finger_tip_link]
    hand_approach_direction: [1.0,0.0,0.0]
  left_arm:
    hand_frame: l_wrist_roll_link
    robot_frame: base_link
    attached_objects_name: attached
    attach_link: l_gripper_r_finger_tip_link
    hand_group_name: l_end_effector
    arm_group_name: left_arm
    hand_database_name: WILLOW_GRIPPER_2010
    hand_joints: [l_gripper_l_finger_joint,l_gripper_r_finger_joint,l_gripper_r_finger_tip_joint,l_gripper_l_finger_tip_joint]
    hand_touch_links: [l_gripper_palm_link,l_gripper_r_finger_tip_link,l_gripper_l_finger_tip_link,l_gripper_l_finger_link,l_gripper_r_finger_link]
    hand_fingertip_links: [l_gripper_r_finger_tip_link,l_gripper_l_finger_tip_link]
    hand_approach_direction: [1.0,0.0,0.0]
```



## Running the Manipulation Pipeline

To launch the manipulation pipeline and execute pickup and place tasks
using the PR2 robot, tutorials and launch files are provided in
[pr2_tabletop_manipulation_apps](pr2_tabletop_manipulation_apps).
