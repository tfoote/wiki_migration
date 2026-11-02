## Overview

This package simulates an industrial robot controller that adheres to
the [ROS-Industrial](Industrial) driver specification. Currently the
simulator only supports the minimum
[requirements](Industrial/Industrial_Robot_Driver_Spec#Essential_Capabilities).
The purpose of this node is to provide a simulated robot controller for
development. This simulator publishes standard topics that can be fed
into [Rviz](https://index.ros.org/p/rviz) to create a realistic
visualization of an actual robot cell. Note that the simulation is at
the ROS API level, the node does not accept Simple Message TCP/UDP
connections.

## Usage

The industrial robot simulator package contains a convenience launch
file for bringing up typical low level nodes (sometimes called bringup
scripts). These nodes include the simulator and a controlling action
server. In typical applications the action server receives trajectories
from a higher level planner (not included in this launch file).

Standalone execution is through roslaunch: 

```
roslaunch industrial_robot_simulator robot_interface_simulator.launch
```



## Node API

### industrial_robot_simulator

Simulates an industrial robot controller as defined in ROS-Industrial.

#### Subscribed Topics

- `joint_path_command`
  ([trajectory_msgs/msg/JointTrajectory](https://docs.ros.org/en/rolling/p/trajectory_msgs/msg/JointTrajectory.html)):
  Commanded joint trajectories.

#### Published Topics

- `joint_states`
  ([sensor_msgs/msg/JointState](https://docs.ros.org/en/rolling/p/sensor_msgs/msg/JointState.html)):
  Joint State for each non-fixed joint in the robot.
- `feedback_states`
  ([control_msgs/msg/FollowJointTrajectoryFeedback](https://docs.ros.org/en/rolling/p/control_msgs/msg/FollowJointTrajectoryFeedback.html)):
  Feedback information (errors) for each non-fixed joint state.

#### Parameters

- `controller_joint_names` (`str[]`, default:
  `['joint_1', ..., 'joint_6']`): Joint controller names (for more info
  see [here](https://index.ros.org/p/industrial_robot_client)).
- `initial_joint_state` (`double[]`, default: `[0, ..., 0]`): Initial
  state of all (revolute) joints. Units: rad.
- `motion_update_rate` (`double`, default: `100.0`): Internal update
  rate of the motion interpolator. If 0, node will not interpolate
  between trajectory points. Units: Hz.
- `pub_rate` (`double`, default: `10.0`): Publish rate for state
  publisher(s). Units: Hz.

## Contact us/Technical support

For questions about this package or ROS-Industrial in general, please
contact the developers by posting a message in the
[ROS-Industrial category](https://discourse.ros.org/c/ros-industrial) on
ROS Discourse.

## Reporting bugs
