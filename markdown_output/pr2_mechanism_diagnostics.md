## Overview

The `pr2_mechanism_diagnostics` package publishes data from the
`mechanism_statistics` topic onto diagnostics. This data is published
by
[pr2_controller_manager](https://index.ros.org/p/pr2_controller_manager).
The joints and controllers diagnostics come from this package.

The `mechanism_statistics` topic contains statistics and information
from the joints, actuators and controllers.

## ROS API

### pr2_mechanism_diagnostics

Publishes joint and controller diagnostics

#### Subscribed Topics

- `mechanism_statistics`
  ([pr2_mechanism_msgs/msg/MechanismStatistics](https://docs.ros.org/en/rolling/p/pr2_mechanism_msgs/msg/MechanismStatistics.html)):
  Data from pr2_controller_manager

#### Published Topics

- `/diagnostics`
  ([diagnostic_msgs/msg/DiagnosticArray](https://docs.ros.org/en/rolling/p/diagnostic_msgs/msg/DiagnosticArray.html)):
  Joints and controllers diagnostics output at 1Hz

#### Parameters

- `~disable_controller_warnings` (`bool`, default: `false`): Disable
  warnings from controller overruns.
- `/use_sim_time` (`bool`, default: `false`): Warnings from controller
  overruns are disabled if running in simulation
