## Hardware Requirements

To use this package you need a schunk dexterous hand
[www.schunk-modular-robotics.com](http://www.schunk-modular-robotics.com)
with \'\'\'firmware version 0.0.2.18\'\'\'. Other firmware versions may
work, but are not officially supported. Alternatively you can use a
simulated version without any hardware, see [cob_gazebo](cob_gazebo).

## Software Requirements

The installation is tested for Ubuntu 10.04, 10.10, 11.04 and 11.10
using ROS [electric](electric). If you discover problems installing them
on other platforms, please
[tell us](http://www.care-o-bot-research.org/contributing/mailing-lists).

## ROS API

The [schunk_sdh](schunk_sdh) package provides a configurable node for
operating a schunk dexterous hand. ```clearsilver
 name = sdh_only
 desc = The `schunk_sdh` node takes in <<MsgLink(trajectory_msgs/JointTrajectory)>> messages and send this directly to the hardware. The joint states can be received by [[Topics|topics]] and the sdh can be initialized, stopped or recovered via [[Services|services]].

goal{
 0.name=follow_joint_trajectory_action/goal
 0.type=control_msgs/FollowJointTrajectoryActionGoal
 0.desc=The goal describes the target trajectory for the sdh (at the moment only the position value of the last trajectory point is used).
}

result{
 2.name=follow_joint_trajectory_action/result
 2.type=control_msgs/FollowJointTrajectoryActionResult
 2.desc=empty
}

feedback{
 0.name=follow_joint_trajectory_action/feedback
 0.type=control_msgs/FollowJointTrajectoryActionFeedback
 0.desc=empty
}

sub{
 0.name = command
 0.type = trajectory_msgs/JointTrajectory
 0.desc = Receives direct commands.
}

pub{
 0.name = /joint_states
 0.type = sensor_msgs/JointState
 0.desc = Publishes the joint states of all joints.
}

srv{
 0.name = init
 0.type = cob_srvs/Trigger
 0.desc = Initializes the node and connects to the hardware.
 1.name = stop
 1.type = cob_srvs/Trigger
 1.desc = Stops immediately all hardware movements.
 2.name = recover
 2.type = cob_srvs/Trigger
 2.desc = Recovers the hardware after an emergency stop.
 3.name = set_operation_mode
 3.type = cob_srvs/Trigger
 3.desc = Sets the operation mode for the node.
}

param{
 0.name = ~sdhdevicetype
 0.type = string
 0.default = PCAN
 0.desc = Device type for can dongle hand
 1.name = ~sdhdevicestring
 1.type = string
 1.default = /dev/pcan0
 1.desc = Device identifier for hand, e.g. /dev/pcan32
 2.name = ~dsadevicestring
 2.type = string
 2.default = Required
 2.desc = Device identifier for tactile sensors, e.g. /dev/ttyUSB0
 3.name = ~baudrate
 3.type = int
 3.default = 1000000
 3.desc = Baudrate of can module, e.g. 1000, 500,...
 4.name = ~joint_names
 4.type = list of strings
 4.default = Required
 4.desc = List of joint names corresponding to urdf description, e.g. [sdh_thumb_3_joint, sdh_finger_11_joint,...]
 5.name = /robot_description
 5.type = urdf model
 5.default = Required
 5.desc = Urdf model of the robot, including the joints and links describing the sdh
}

req_tf{
}

prov_tf{
}
```
```clearsilver
 name = dsa_only
 desc = The `dsa_only` node publishes data from the tactile sensors in form of <<MsgLink(schunk_sdh/TactileSensor)>> messages.
pub{
 0.name = tactile_data
 0.type = schunk_sdh/TactileSensor
 0.desc = Publishes data from the tactile sensors.
}

param{
 0.name = ~dsadevicestring
 0.type = string
 0.default = Required
 0.desc = Device identifier for dsa, e.g. /dev/ttyS0
 1.name = ~polling
 1.type = bool
 1.defaut = false
 1.desc = Use polling mode for getting sensor data
 2.name = ~publish_frequency
 2.type = float
 2.defaut = 0.0
 2.desc = Frequency for publishing sensor data
}
```

## Usage/Examples

This package is not intended to be used directly, but with the
corresponding launch and yaml files from e.g.
[schunk_bringup](schunk_bringup) in the [schunk_robots](schunk_robots)
stack. For using only the sdh use ```
roslaunch schunk_bringup sdh_solo.launch
``` For including
the sdh in your overall launch file use ```
<include file="$(find schunk_bringup)/components/sdh.launch" />
``` All
hardware configuration is done in the
[schunk_hardware_config](schunk_hardware_config) package. A sample
parameter file for the sdh in
\"schunk_hardware_config/sdh/config/sdh.yaml\" could look like this
```
sdhdevicetype: PCAN
sdhdevicestring: /dev/pcan0
baudrate: 1000000
joint_names: ['sdh_knuckle_joint', 'sdh_thumb_2_joint', 'sdh_thumb_3_joint', 'sdh_finger_12_joint', 'sdh_finger_13_joint', 'sdh_finger_22_joint', 'sdh_finger_23_joint']
OperationMode: position
``` A sample parameter file for the dsa tactile
sensors in \"schunk_hardware_config/sdh/config/dsa.yaml\" could look
like this ```
dsadevicestring: /dev/ttyS0
polling: false
use_rle: true
frequency: 30
```
