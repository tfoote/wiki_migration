## Overview

This package provide a `ros_control` compatible controller that
publishes robot/controller state (e-stopped, in motion, etc) as
<<MsgLink(industrial_msgs/RobotStatus)>> messages.

## Documentation

See the documentation in the repository:
[gavanderhoorn/industrial_robot_status_controller](https://github.com/gavanderhoorn/industrial_robot_status_controller).

## Controllers

Controllers provided by this package:

```clearsilver

node.0 {
  name=IndustrialRobotStatusController
  desc=Publishes `industrial_msgs/RobotStatus` based on information coming from the underlying `hardware_interface`.

  pub {
    0.name = robot_status
    0.type = industrial_msgs/RobotStatus
    0.desc = Status of the robot or controller (e-stopped, in motion, motion possible, etc)
  }

  param {
    0.name = publish_rate
    0.type = float
    0.desc = rate at which `RobotStatus` messages should be published (Hz)
    0.default = 10.0
    1.name = handle_name
    1.type = str
    1.desc = name of the `IndustrialRobotStatusHandle` resource exposed by the `hardware_interface`
    1.default = "industrial_robot_status_handle"
  }
}
```

## Report a Bug

<<GitHubIssues(gavanderhoorn/industrial_robot_status_controller)>>
