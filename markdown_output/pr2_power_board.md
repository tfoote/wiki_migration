## Overview

`power_node2` controls with the PR2 power board. The API below is for
informational purposes only; it is not intended for use by anything
other than [power_monitor](power_monitor), which is where you should
look for power data.

The `power_node2` runs on the PR2 and controls the PR2 power board.
The node regulates the main fan speed of the PR2 based on battery and
power board temperature.

## Nodes



```clearsilver
name = power_node2
pub {
  0.name= /diagnostics
  0.type= diagnostics_msgs/DiagnosticArray
  0.desc= Diagnostic information
  1.name= ~state
  1.type= pr2_msgs/PowerBoardState
  1.desc= Power board state
}
sub {
  0.name = battery/server2
  0.type = pr2_msgs/BatteryServer2
  0.desc = Battery data, for temperatures
}
srv {
  0.name= ~control2
  0.type= pr2_power_board/PowerBoardCommand2
  0.desc= Send a command to the power board
  1.name= ~control
  1.type= pr2_power_board/PowerBoardCommand
  1.desc= Send a command to the power board (DEPRECATED)
}
param {
  0.name= ~sample_frequency
  0.type= float
  0.default= 10.0
  0.desc= Sampling frequency
  1.name= ~transition_frequency
  1.type= float
  1.default= 0.1
  1.desc= Transition frequency
}
```





```clearsilver
name = power_node
desc = Deprecated node for controller Rev. A and B power boards.
pub {
  0.name= /diagnostics
  0.type= diagnostics_msgs/DiagnosticArray
  0.desc= Diagnostic information
  1.name= ~state
  1.type= pr2_msgs/PowerBoardState
  1.desc= Power board state
}
srv {
  1.name= ~control
  1.type= pr2_power_board/PowerBoardCommand
  1.desc= Send a command to the power board
}
```


