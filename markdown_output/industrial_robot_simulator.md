## Overview

This package simulates an industrial robot controller that adheres to
the [ROS-Industrial](Industrial) driver specification. Currently the
simulator only supports the minimum
[requirements](Industrial/Industrial_Robot_Driver_Spec#Essential_Capabilities).
The purpose of this node is to provide a simulated robot controller for
development. This simulator publishes standard topics that can be fed
into [Rviz](rviz) to create a realistic visualization of an actual robot
cell. Note that the simulation is at the ROS API level, the node does
not accept Simple Message TCP/UDP connections.

## Usage

The industrial robot simulator package contains a convenience launch
file for bringing up typical low level nodes (sometimes called bringup
scripts). These nodes include the simulator and a controlling action
server. In typical applications the action server receives trajectories
from a higher level planner (not included in this launch file).

Standalone execution is through roslaunch: ```
roslaunch industrial_robot_simulator robot_interface_simulator.launch
```

## Node API

```clearsilver
name = industrial_robot_simulator
desc = Simulates an industrial robot controller as defined in ROS-Industrial.
sub {
 0.name = joint_path_command
 0.type = trajectory_msgs/JointTrajectory
 0.desc = Commanded joint trajectories.
}
pub {
 0.name = joint_states
 0.type = sensor_msgs/JointState
 0.desc = Joint State for each non-fixed joint in the robot.
 1.name = feedback_states
 1.type = control_msgs/FollowJointTrajectoryFeedback
 1.desc = Feedback information (errors) for each non-fixed joint state.
}
param {
 0.name = controller_joint_names
 0.type = str[]
 0.desc = Joint controller names (for more info see [[industrial_robot_client/generic_implementation#Parameters|here]]).
 0.default = ['joint_1', ..., 'joint_6']
 1.name = initial_joint_state
 1.type = double[]
 1.desc = Initial state of all (revolute) joints. Units: rad.
 1.default = [0, ..., 0]
 2.name = motion_update_rate
 2.type = double
 2.desc = Internal update rate of the motion interpolator. If 0, node will not interpolate between trajectory points. Units: Hz.
 2.default = 100.0
 3.name = pub_rate
 3.type = double
 3.desc = Publish rate for state publisher(s). Units: Hz.
 3.default = 10.0
}
```

\<\<Include(industrial/contact_us_tech_support)\>\>

## Reporting bugs

\<\<GitHubIssues(ros-industrial/industrial_core)\>\>
