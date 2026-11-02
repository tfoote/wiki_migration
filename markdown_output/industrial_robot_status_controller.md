## Overview

This package provide a `ros_control` compatible controller that
publishes robot/controller state (e-stopped, in motion, etc) as
[industrial_msgs/msg/RobotStatus](https://docs.ros.org/en/rolling/p/industrial_msgs/msg/RobotStatus.html)
messages.

## Documentation

See the documentation in the repository:
[gavanderhoorn/industrial_robot_status_controller](https://github.com/gavanderhoorn/industrial_robot_status_controller).

## Controllers

Controllers provided by this package:

### IndustrialRobotStatusController

Publishes `industrial_msgs/RobotStatus` based on information coming
from the underlying `hardware_interface`.

#### Published Topics

- `robot_status`
  ([industrial_msgs/msg/RobotStatus](https://docs.ros.org/en/rolling/p/industrial_msgs/msg/RobotStatus.html)):
  Status of the robot or controller (e-stopped, in motion, motion
  possible, etc)

#### Parameters

- `publish_rate` (`float`, default: `10.0`): rate at which
  `RobotStatus` messages should be published (Hz)
- `handle_name` (`str`, default: `"industrial_robot_status_handle"`):
  name of the `IndustrialRobotStatusHandle` resource exposed by the
  `hardware_interface`

## Report a Bug
