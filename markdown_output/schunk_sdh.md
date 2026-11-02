## Hardware Requirements

To use this package you need a schunk dexterous hand
[www.schunk-modular-robotics.com](http://www.schunk-modular-robotics.com)
with **firmware version 0.0.2.18**. Other firmware versions may work,
but are not officially supported. Alternatively you can use a simulated
version without any hardware, see
[cob_gazebo](https://index.ros.org/p/cob_gazebo).

## Software Requirements

The installation is tested for Ubuntu 10.04, 10.10, 11.04 and 11.10
using ROS [electric](electric). If you discover problems installing them
on other platforms, please
[tell us](http://www.care-o-bot-research.org/contributing/mailing-lists).

## ROS API

The schunk_sdh package provides a
configurable node for operating a schunk dexterous hand.

### sdh_only

The `schunk_sdh` node takes in
[trajectory_msgs/msg/JointTrajectory](https://docs.ros.org/en/rolling/p/trajectory_msgs/msg/JointTrajectory.html)
messages and send this directly to the hardware. The joint states can be
received by [topics](Topics) and the sdh can be initialized, stopped or
recovered via [services](Services).

#### Action Goal

- `follow_joint_trajectory_action/goal`
  ([control_msgs/msg/FollowJointTrajectoryActionGoal](https://docs.ros.org/en/rolling/p/control_msgs/msg/FollowJointTrajectoryActionGoal.html)):
  The goal describes the target trajectory for the sdh (at the moment
  only the position value of the last trajectory point is used).

#### Action Result

- `follow_joint_trajectory_action/result`
  ([control_msgs/msg/FollowJointTrajectoryActionResult](https://docs.ros.org/en/rolling/p/control_msgs/msg/FollowJointTrajectoryActionResult.html)):
  empty

#### Action Feedback

- `follow_joint_trajectory_action/feedback`
  ([control_msgs/msg/FollowJointTrajectoryActionFeedback](https://docs.ros.org/en/rolling/p/control_msgs/msg/FollowJointTrajectoryActionFeedback.html)):
  empty

#### Subscribed Topics

- `command`
  ([trajectory_msgs/msg/JointTrajectory](https://docs.ros.org/en/rolling/p/trajectory_msgs/msg/JointTrajectory.html)):
  Receives direct commands.

#### Published Topics

- `/joint_states`
  ([sensor_msgs/msg/JointState](https://docs.ros.org/en/rolling/p/sensor_msgs/msg/JointState.html)):
  Publishes the joint states of all joints.

#### Services

- `init`
  ([cob_srvs/srv/Trigger](https://docs.ros.org/en/rolling/p/cob_srvs/srv/Trigger.html)):
  Initializes the node and connects to the hardware.
- `stop`
  ([cob_srvs/srv/Trigger](https://docs.ros.org/en/rolling/p/cob_srvs/srv/Trigger.html)):
  Stops immediately all hardware movements.
- `recover`
  ([cob_srvs/srv/Trigger](https://docs.ros.org/en/rolling/p/cob_srvs/srv/Trigger.html)):
  Recovers the hardware after an emergency stop.
- `set_operation_mode`
  ([cob_srvs/srv/Trigger](https://docs.ros.org/en/rolling/p/cob_srvs/srv/Trigger.html)):
  Sets the operation mode for the node.

#### Parameters

- `~sdhdevicetype` (`string`, default: `PCAN`): Device type for can
  dongle hand
- `~sdhdevicestring` (`string`, default: `/dev/pcan0`): Device
  identifier for hand, e.g. /dev/pcan32
- `~dsadevicestring` (`string`, default: `Required`): Device identifier
  for tactile sensors, e.g. /dev/ttyUSB0
- `~baudrate` (`int`, default: `1000000`): Baudrate of can module, e.g.
  1000, 500,\...
- `~joint_names` (`list of strings`, default: `Required`): List of joint
  names corresponding to urdf description, e.g. \[sdh_thumb_3_joint,
  sdh_finger_11_joint,\...\]
- `/robot_description` (`urdf model`, default: `Required`): Urdf model
  of the robot, including the joints and links describing the sdh

### dsa_only

The `dsa_only` node publishes data from the tactile sensors in form of
[schunk_sdh/msg/TactileSensor](https://docs.ros.org/en/rolling/p/schunk_sdh/msg/TactileSensor.html)
messages.

#### Published Topics

- `tactile_data`
  ([schunk_sdh/msg/TactileSensor](https://docs.ros.org/en/rolling/p/schunk_sdh/msg/TactileSensor.html)):
  Publishes data from the tactile sensors.

#### Parameters

- `~dsadevicestring` (`string`, default: `Required`): Device identifier
  for dsa, e.g. /dev/ttyS0
- `~polling` (`bool`, default: `false`): Use polling mode for getting
  sensor data
- `~publish_frequency` (`float`, default: `0.0`): Frequency for
  publishing sensor data

## Usage/Examples

This package is not intended to be used directly, but with the
corresponding launch and yaml files from e.g.
[schunk_bringup](schunk_bringup) in the [schunk_robots](schunk_robots)
stack. For using only the sdh use 

```
roslaunch schunk_bringup sdh_solo.launch
```

 For including
the sdh in your overall launch file use 

```
<include file="$(find schunk_bringup)/components/sdh.launch" />
```

 All
hardware configuration is done in the
[schunk_hardware_config](schunk_hardware_config) package. A sample
parameter file for the sdh in
"schunk_hardware_config/sdh/config/sdh.yaml" could look like this


```
sdhdevicetype: PCAN
sdhdevicestring: /dev/pcan0
baudrate: 1000000
joint_names: ['sdh_knuckle_joint', 'sdh_thumb_2_joint', 'sdh_thumb_3_joint', 'sdh_finger_12_joint', 'sdh_finger_13_joint', 'sdh_finger_22_joint', 'sdh_finger_23_joint']
OperationMode: position
```

 A sample parameter file for the dsa tactile
sensors in "schunk_hardware_config/sdh/config/dsa.yaml" could look
like this 

```
dsadevicestring: /dev/ttyS0
polling: false
use_rle: true
frequency: 30
```
