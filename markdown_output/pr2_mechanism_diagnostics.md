## Overview

The `pr2_mechanism_diagnostics` package publishes data from the
`mechanism_statistics` topic onto diagnostics. This data is published
by [pr2_controller_manager](pr2_controller_manager). The joints and
controllers diagnostics come from this package.

The `mechanism_statistics` topic contains statistics and information
from the joints, actuators and controllers.

## ROS API



```clearsilver
name = pr2_mechanism_diagnostics
desc = Publishes joint and controller diagnostics
sub {
  0.name = mechanism_statistics
  0.type = pr2_mechanism_msgs/MechanismStatistics
  0.desc = Data from pr2_controller_manager
}
pub {
  0.name = /diagnostics
  0.type = diagnostic_msgs/DiagnosticArray
  0.desc = Joints and controllers diagnostics output at 1Hz
}
param {
  0.name = ~disable_controller_warnings
  0.type = bool
  0.desc = Disable warnings from controller overruns.
  0.default = false

  1.name = /use_sim_time
  1.type = bool
  1.desc = Warnings from controller overruns are disabled if running in simulation
  1.default = false
}
```


