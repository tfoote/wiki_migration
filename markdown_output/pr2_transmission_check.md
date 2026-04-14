## Overview

Checks transmissions status of PR2 transmissions.

To do this, it loads the URDF from the \`robot_description\` param, and
checks that each actuator calibration flag corresponds to the correct
joint position. It works for all joints with simple transmissions, and
wrist transmissions.

Once a transmission reports invalid data, the
\"pr2_etherCAT/halt_motors\" service will be called. Users must reset
motors using the pr2_dashboard.

## Nodes

```clearsilver
name = pr2_transmission_check
desc = Publishes joint and controller diagnostics, checks transmissions
pub {
  0.name = ~transmission_status
  0.type = std_msgs/Bool
  0.desc = True if transmissions are OK
  1.name = /diagnostics
  1.type = diagnostic_msgs/DiagnosticArray
  1.desc = Publishes output for each transmission
}
srv {
  0.name= ~reset_trans_check
  0.type= pr2_power_board/PowerBoardCommand2
  0.desc= Reset the transmission status to True
}
```

All transmissions will publish diagnostics on last observed position,
the joints and actuators, and the number of errors. Joints that have
transmission errors will be in error state until reset.
