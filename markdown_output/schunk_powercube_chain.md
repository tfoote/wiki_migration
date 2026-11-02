## Hardware Requirements

To use this package you need one or more powercubes
[www.schunk-modular-robotics.com](http://www.schunk-modular-robotics.com).
Alternatively you can use a simulated version without any hardware, see
[schunk_bringup_sim](schunk_bringup_sim).

## Software Requirements

The installation is tested for Ubuntu 14.04 using ROS [indigo](indigo).
If you discover problems installing them on other platforms, please
[tell us](http://www.care-o-bot-research.org/contributing/mailing-lists).

## ROS API

The schunk_powercube_chain
package provides a configurable node for operating a chain of powercube
modules.

### schunk_powercube_chain

The `schunk_powercube_chain` node takes in
[brics_actuator/msg/JointVelocities](https://docs.ros.org/en/rolling/p/brics_actuator/msg/JointVelocities.html)
messages and sends this directly to the hardware. The chain can be
initialized, stopped or recovered via [services](Services).

#### Subscribed Topics

- `joint_group_velocity_controller/command`
  ([std_msgs/msg/Float64MultiArray](https://docs.ros.org/en/rolling/p/std_msgs/msg/Float64MultiArray.html)):
  Receives velocity commands.
- `joint_group_position_controller/command`
  ([std_msgs/msg/Float64MultiArray](https://docs.ros.org/en/rolling/p/std_msgs/msg/Float64MultiArray.html)):
  Receives position commands (Not implemented yet).

#### Published Topics

- `/joint_states`
  ([sensor_msgs/msg/JointState](https://docs.ros.org/en/rolling/p/sensor_msgs/msg/JointState.html)):
  Joint state information for all modules in chain.
- `joint_trajectory_controller/state`
  ([control_msgs/msg/JointTrajectoryControllerState](https://docs.ros.org/en/rolling/p/control_msgs/msg/JointTrajectoryControllerState.html)):
  Controller state information for all modules in chain.
- `driver/current_operationmode`
  ([std_msgs/msg/String](https://docs.ros.org/en/rolling/p/std_msgs/msg/String.html)):
  Current operation mode for chain.
- `/diagnostics`
  ([diagnostic_msgs/msg/DiagnosticArray](https://docs.ros.org/en/rolling/p/diagnostic_msgs/msg/DiagnosticArray.html)):
  Diagnostics information about chain.

#### Services

- `driver/init`
  ([std_srvs/srv/Trigger](https://docs.ros.org/en/rolling/p/std_srvs/srv/Trigger.html)):
  Initializes the node and connects to the hardware.
- `driver/stop`
  ([std_srvs/srv/Trigger](https://docs.ros.org/en/rolling/p/std_srvs/srv/Trigger.html)):
  Stops immediately all hardware movements.
- `driver/recover`
  ([std_srvs/srv/Trigger](https://docs.ros.org/en/rolling/p/std_srvs/srv/Trigger.html)):
  Recovers the hardware after an emergency stop.
- `driver/set_operation_mode`
  ([cob_srvs/srv/SetString](https://docs.ros.org/en/rolling/p/cob_srvs/srv/SetString.html)):
  Sets the operation mode for the node. Currently only "velocity" mode
  implemented.

#### Parameters

- `can_module` (`string`, default: `Required`): Can module specifier,
  e.g. PCAN, ESD
- `can_device` (`string`, default: `Required`): Device address of can
  module, e.g. /dev/can0, /dev/pcan2,\...
- `can_baudrate` (`int`, default: `Required`): Baudrate of can module,
  e.g. 1000, 500,\...
- `module_ids` (`list of ints`, default: `Required`): Modul IDs of the
  powercubes, e.g. \[10,11,12,13,\...\]
- `force_use_movevel` (`bool`, default: `false`): Forces using the M5API
  moveVel command instead of moveStep.
- `joint_names` (`list of strings`, default: `Required`): List of joint
  names corresponding to urdf description, e.g. \[arm_1_joint,
  arm_2_joint, arm_3_joint,\...\]
- `max_accelerations` (`list of doubles`, default: `Required`): List of
  maximal accelerations for the modules in rad/sec\^2, e.g.
  \[0.8,0.8,0.8,\...\]
- `horizon` (`double`, default: `0.05`): Horizon in seconds for
  commanding moveStep. E.g. 0.1 commands a step size of 0.1 seconds into
  the future.
- `frequency` (`double`, default: `10 Hz`): Controller frequency.
- `min_publish_duration` (`double`, default: `Required`): Minimum
  duration of publishing joint states if no command is received,
  otherwise for each received command one joint state message is
  published.
- `/robot_description` (`urdf model`, default: `Required`): Urdf model
  of the robot, including the joints and links describing the chain of
  powercubes

## Usage/Examples

This package is not intended to be used directly, but with the
corresponding launch and yaml files from e.g.
[schunk_bringup](schunk_bringup) in the [schunk_robots](schunk_robots)
stack. For starting only the lwa use 

```
roslaunch schunk_bringup lwa_solo.launch
```

 For
including the lwa in your overall launch file use


```
<include file="$(find schunk_bringup)/components/lwa.launch" />
```

 All hardware configuration is done in the
[schunk_hardware_config](schunk_hardware_config) package. A sample
parameter file in "schunk_hardware_config/lwa/config/lwa.yaml" could
look like this 

```
can_module: PCAN
can_device: /dev/pcan1
can_baudrate: 1000
modul_ids: [1,2,3,4,5,6,7]
joint_names: [arm_1_joint, arm_2_joint, arm_3_joint, arm_4_joint, arm_5_joint, arm_6_joint, arm_7_joint]
max_accelerations: [0.8,0.8,0.8,0.8,0.8,0.8,0.8]
frequency: 68
OperationMode: position
ptp_vel: 0.4 # rad/sec
ptp_acc: 0.1 # rad/sec^2
max_error: 0.2 # rad
```
