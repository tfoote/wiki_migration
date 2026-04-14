## About

The \`carl_moveit_package\` includes configuration files for running the
[CARL robot](carl_bot) with MoveIt!. The package also includes a ros
node that acts as a wrapper for relevant MoveIt! functionality that CARL
uses, and a node that provides simple execution of common actions such
as arm readying, retracting, and lifting.

\<\<MsgSrvDoc(carl_moveit)\>\>

## Nodes

```clearsilver
node.0 {
  name = carl_moveit_wrapper
  desc = 'carl_moveit_wrapper' provides a convenient wrapper to commonly used MoveIt! functionality for CARL, such as motion planning for end-effector poses, end-effector Cartesian trajectory generation, and inverse kinematics.
  sub {
    0.name = joint_states
    0.type = sensor_msgs/JointState
    0.desc = Joint state updates for CARL.
    1.name = carl_moveit_wrapper/cartesian_control
    1.type = geometry_msgs/Twist
    1.desc = Experimental direct end-effector control using Jacobian pseudoinverse methods.
    2.name = jaco_arm/arm_homed
    2.type = std_msgs/Bool
    2.desc = Listen for the arm to complete a home action using the Kinova API.
  }
  pub {
    0.name = jaco_arm/angular_cmd
    0.type = wpi_jaco_msgs/AngularCommand
    0.desc = Send angular commands to the JACO.
  }
  pub {
    1.name = carl_moveit/computed_trajectory
    1.type = moveit_msgs/DisplayTrajectory
    1.desc = Trajectory visualization for debugging planned paths.
  }
  srv_called {
    0.name = compute_ik
    0.type = moveit_msgs/GetPositionIK
    0.desc = Get inverse kinematics from MoveIt!.
    1.name = clear_octomap
    1.type = std_srvs/Empty
    1.desc = Clear the octomap (environment collision voxel grid).
  }
  srv {
    0.name = carl_moveit_wrapper/cartesian_path
    0.type = carl_moveit/CartesianPath
    0.desc = Compute and execute a Cartesian path for CARL's end-effector.
  }
  srv {
    1.name = carl_moveit_wrapper/call_ik
    1.type = carl_moveit/CallIK
    1.desc = Compute inverse kinematics given a only a pose (automatically handles other parameters MoveIt! needs for IK).
  }
  act_called {
    0.name = jaco_arm/joint_velocity_controller/trajectory
    0.type = control_msgs/FollowJointTrajectoryGoal
    0.desc = Joint velocity control based smooth trajectory generator and follower, provides smooth trajectory execution for any valid point-to-point trajectory in the arm's workspace.
  }
  goal {
    0.name = carl_moveit_wrapper/move_to_pose
    0.type = carl_moveit/MoveToPoseGoal
    0.desc = Plan a trajectory to a pose goal, and execute the trajectory if planning was successful.  Note that the pose is for the jaco_link_hand frame.
  }
  goal {
    1.name = carl_moveit_wrapper/move_to_joint_pose
    1.type = carl_moveit/MoveToJointPoseGoal
    1.desc = Plan a trajectory to a joint configuration goal, and execute the trajectory if planning was successful.
  }
  result {
    0.name = carl_moviet_wrapper/move_to_pose
    0.type = carl_moveit/MoveToPoseResult
    0.desc = Success/failure of motion planning and trajectory execution to a given pose.
  }
  result {
    1.name = carl_moveit_wrapper/move_to_joint_pose
    1.type = carl_moveit/MoveToJointPoseResult
    1.desc = Success/failure of motion planning and trajectory execution to a given joint configuration.
  }
}
node.1 {
  name = carl_moveit_common_actions
  desc = 'carl_moveit_common_actions' provides a quick way to call preprogrammed actions that require motion planning, such as resetting the arm to its home position with obstacle avoidance.
  sub {
    0.name = jaco_arm/angular_cmd
    0.type = wpi_jaco_msgs/AngularCommand
    0.desc = Angular command publisher for the arm.
  }
  srv_called {
    0.name = jaco_arm/erase_trajectories
    0.type = std_srvs/Empty
    0.desc = Stop any currently running arm trajectory.
  }
  srv_called {
    1.name = jaco_arm/get_angular_position
    1.type = wpi_jaco_msgs/GetAngularPosition
    1.desc = Read joint positions from the arm.
  }
  goal {
    0.name = carl_moveit_wrapper/common_actions/arm_action
    0.type = carl_moveit/ArmAction
    0.desc = Perform a pre-defined arm action, such as moving the arm to the ready position or retracted position using motion planning for obstacle avoidance.
    1.name = carl_moveit_wrapper/common_actions/lift
    1.type = rail_manipulation_msgs/LiftAction
    1.desc = Raise the end-effector up by 10 cm using Cartesian path planning and execution.
    2.name = carl_moveit_wrapper/common_actions/pickup
    2.type = carl_moveit/PickupAction
    2.desc = Execute a complete pickup action on a given pickup pose.
   }
  result {
    0.name = carl_moveit_wrapper/common_actions/arm_action
    0.type = carl_moveit/ArmResult
    0.desc = Success/failure of arm action.
    1.name = carl_moveit_wrapper/common_actions/lift
    1.type = rail_manipulation_msgs/LiftResult
    1.desc = Success/failure of the lift action.
    2.name = carl_moveit_wrapper/common_actions/pickup
    2.type = carl_moveit/PickupResult
    2.desc = Success/failure of the pickup action.
  }
  act_called {
    0.name = carl_moveit_wrapper/move_to_joint_pose
    0.type = carl_moveit/MoveToJointPoseGoal
    0.desc = Call to the move arm action server that will plan and move to a joint goal.
    1.name = carl_moveit_wrapper/move_to_pose
    1.type = carl_moveit/MoveToPoseGoal
    1.desc = Call to the move arm action server that will plan and move to an end-effector goal.
    2.name = jaco_arm/manipulation/gripper
    2.type = rail_manipulation_msgs/GripperAction
    2.desc = Gripper open/close action.
    3.name = carl_moveit_wrapper/common_actions/lift
    3.type = rail_manipulation_msgs/LiftAction
    3.desc = Call to lift action.
  }
```

## Installation

To install the \`carl_moveit\` package, you can install from source with
the following commands: . ```shell
cd /(your catkin workspace)/src
git clone https://github.com/WPI-RAIL/carl_moveit.git
cd ..
catkin_make
catkin_make install
```

## Startup

The \`carl_moveit\` package contains many launch files that are used for
configuring MoveIt! for CARL. They can be used to run MoveIt! on CARL,
on a simulated robot, run benchmarks, visualize motion planning, and
adjust parameters. Primarily, the \`carl_moveit_full.launch\` file can
be used to run everything required for MoveIt! on CARL, as well as
\`carl_moveit_wrapper\` and \`carl_moveit_common_actions\`: .
```
roslaunch carl_moveit carl_moveit_full.launch
```
