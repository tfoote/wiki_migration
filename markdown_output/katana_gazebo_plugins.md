## Available Plugins

Currently, there is only one plugin available that simulates the
gripper. See packages [katana_description](katana_description) and
[katana_arm_gazebo](katana_arm_gazebo) for usage examples and for
information on the Gazebo parameters (not documented here).

```clearsilver
node.0 {
  name = gazebo_ros_katana_gripper
  pub {
    0.name = gripper_controller_state
    0.type = katana_msgs/GripperControllerState
    0.desc = The actual position, desired position and error in position of each gripper joint.
  }
  param {
    0.name = ~gripper_object_presence_threshold
    0.type = double
    0.desc = A joint angle below this value indicates there is nothing inside the gripper.
    0.default = -0.43
  }
  srv {
    0.name = grasp_query_name
    0.type = object_manipulation_msgs/GraspStatus
    0.desc = Asks if a grasp is currently active. Used to query if the object is still detected as present in the hand, using joint angles.
  }
  goal {
    0.name = posture_action_name/goal
    0.type = object_manipulation_msgs/GraspHandPostureExecutionActionGoal
    0.desc = Enables one to open or close the gripper via the GRASP or RELEASE command or to move the gripper to a arbitrary position choosing the PRE-GRASP option.
  }
  result {
    0.name = posture_action_name/result
    0.type = object_manipulation_msgs/GraspHandPostureExecutionActionResult
    0.desc = Result of the manipulation task.
  }
}
```
