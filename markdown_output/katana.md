## ROS API

This package provides the `katana` ROS node, which provides four sets
of functionality at once: the `joint_state_publisher`, the
`joint_movement_controller`, the
`joint_trajectory_action_controller` and the
`gripper_grasp_controller`. They are combined into one single node for
technical reasons (only one single process can access the Katana), but
documented separately below for clarity.

Also there is a second node in this package, called
`katana_arm_kinematics`, documented at the end.



```clearsilver
node.0 {
  name = katana node: general parameters
  param {
    0.name = ~simulation
    0.type = bool
    0.desc = Poor man's simulation for debugging purposes. If set to true, the node will not try to contact the real Katana arm, but instead "simulate" the effects of sending trajectories and so on. For real simulation, see the [[katana_arm_gazebo]] package.
    0.default = `false`
    1.name = katana_joints
    1.type = Array of strings
    1.desc = List of joints that this node will be commanding.
    1.default = Required
    2.name = katana_gripper_joints
    2.type = Array of strings
    2.desc = List of commanded joints belonging to the gripper.
    2.default = Required
    3.name = robot_description
    3.type = String
    3.desc = The URDF description of the Katana arm.
    3.default = Required

    4.name = ~use_serial
    4.type = bool
    4.desc = If set to `true`, use a serial port to connect to the Katana arm, otherwise use a TCP/IP connection.
    4.default = `false`

    5.name = ~ip
    5.type = String
    5.desc = If using TCP/IP: The IP on which the Katana arm is listening.
    5.default = "192.168.1.1"
    6.name = ~port
    6.type = int
    6.desc = If using TCP/IP: The port on which the Katana arm is listening.
    6.default = 5566

    7.name = ~serial_port
    7.type = int
    7.desc = If using serial: The serial port number on which the Katana arm is listening (e.g., if the Katana listens on `/dev/ttyUSB3`, set `~serial_port` = 3). Allowed values: 0-9.
    7.default = 0

    8.name = ~config_file_path
    8.type = String
    8.desc = The path to the correct config file for the Katana arm. '''Warning! Make sure to use the correct config file for your arm, otherwise you risk breaking your hardware!'''
    8.default = Required

    9.name = katana_type
    9.type = string
    9.desc = Currently one of `katana_300_6m180`, `katana_400_6m180`, `katana_450_6m90a`, `katana_450_6m90b`.
    9.default = Required
  }
  srv {
    0.name = switch_motors_off
    0.type = std_srvs/Empty
    0.desc = Switch all motors off. WARNING: If the arm is unsupported, it will fall down!
    1.name = switch_motors_on
    1.type = std_srvs/Empty
    1.desc = Switch all motors back on (motors are on by default).
    2.name = test_speed
    2.type = std_srvs/Empty
    2.desc = Service to test the maximum speed of all joints. Only needed when porting the stack to a new Katana arm.
  }
}
node.1 {
  name = joint_state_publisher
  pub {
    0.name = joint_states
    0.type = sensor_msgs/JointState
    0.desc = The measured position, velocity and effort of each joint.
  }
}
node.2 {
  name=joint_movement_action_controller
  desc = This module provides the functionality of adressing a single joint or multiple joints at once via an action interface.
  goal {
    0.name=katana_arm_controller/joint_movement_action/goal
    0.type=katana_msgs/JointMovementActionGoal
    0.desc=The goal specifies which joints shall be moved to which positions.
  }
  feedback {
    0.name=katana_arm_controller/joint_movement_action/feedback
    0.type=katana_msgs/JointMovementActionGoal
    0.desc=empty
  }
  result {
    0.name=katana_arm_controller/joint_movement_action/result
    0.type=katana_msgs/JointMovementActionResult
    0.desc=empty
  }
}

node.3 {
  name=joint_trajectory_action_controller
  desc = This module provides the functionality of both the [[joint_trajectory_action]] (via the action interface) and the [[robot_mechanism_controllers/JointSplineTrajectoryController|JointSplineTrajectoryController]] (via the `command` and `state` topics and the `query_state` service).
  param {
    0.name=joint_trajectory_action_node/constraints/<joint>/goal
    0.type=double
    0.default=0.02
    0.desc=The maximum final error for <joint> for the trajectory goal to be considered successful.  Negative numbers indicate that there is no constraint.  Given in radians. If this constraint is violated, the goal is aborted.
    1.name=joint_trajectory_action_node/constraints/stopped_velocity_tolerance
    1.type=double
    1.default=1e-6
    1.desc=The maximum velocity at the end of the trajectory for the joint to be considered stopped, given in radians. If this constraint is satisfied, the goal is successful.
  }
  goal {
    0.name=katana_arm_controller/joint_trajectory_action/goal
    0.type=pr2_controllers_msgs/JointTrajectoryActionGoal
    0.desc=The goal describes the trajectory for the robot to follow.
  }
  feedback {
    0.name=katana_arm_controller/joint_trajectory_action/feedback
    0.type=pr2_controllers_msgs/JointTrajectoryActionFeedback
    0.desc=empty
  }
  result {
    0.name=katana_arm_controller/joint_trajectory_action/result
    0.type=pr2_controllers_msgs/JointTrajectoryActionResult
    0.desc=empty
  }
  sub{
    0.name=katana_arm_controller/command
    0.type=trajectory_msgs/JointTrajectory
    0.desc=The trajectory to follow.  The absolute start time of the trajectory is given in header.stamp. The behavior differs from that of the [[robot_mechanism_controllers/JointSplineTrajectoryController|JointSplineTrajectoryController]]: Accelerations are always ignored. If positions and velocities are specified, then the controller will interpolate using cubic splines, keeping the desired velocities. If only positions are specified, it will also interpolate using cubic splines, computing the necessary velocities.
  }
  pub{
    0.name=katana_arm_controller/state
    0.type=pr2_controllers_msgs/JointTrajectoryControllerState
    0.desc=Current state of the controller, including the current and desired positions, velocities, and accelerations.
  }
  srv{
    0.name=query_state
    0.type=pr2_controllers_msgs/QueryTrajectoryState
    0.desc=The query_state service allows the user to inquire where the controller setpoint will be at a desired time.
  }
}
node.4 {
  name = gripper_grasp_controller
  desc = This module is the very similar to the [[pr2_gripper_grasp_controller]].
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
node.5 {
  name = katana_arm_kinematics
  desc = This node implements forward and inverse kinematics services. They are implemented using the [[kni]] library.
  param {
    0.name = ~config_file_path
    0.type = String
    0.desc = The path to the correct config file for the Katana arm.
    0.default = ros::package::getPath("kni") + "/KNI_4.3.0/configfiles450/katana6M90A_G.cfg"
    1.name = robot_description
    1.type = String
    1.desc = The URDF description of the Katana arm.
    1.default = Required
    2.name = katana_joints
    2.type = Array of strings
    2.desc = List of joints that this node will compute kinematics for.
    2.default = Required
  }
  srv {
    0.name = get_kinematic_solver_info
    0.type = kinematics_msgs/GetKinematicSolverInfo
    0.desc = Kinematic solver info.
    1.name = get_fk
    1.type = kinematics_msgs/GetPositionFK
    1.desc = Forward kinematics service.
    2.name = get_ik
    2.type = kinematics_msgs/GetPositionIK
    2.desc = Inverse kinematics service.
  }
}
```


