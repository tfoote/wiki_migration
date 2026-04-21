## Overview

A ROS node for using libsensors to provide diagnostics information about
the sensors (CPU temp, GPU temp, fan speed, voltage, etc) on a computer
system.

## Nodes



```clearsilver
node.0 {
  name = libsensors_monitor
  desc = Node to publish sensor information from a computer
  sub {
  }
  pub {
    0.name = /diagnostics
    0.type = diagnostic_msgs/DiagnosticArray
    0.desc = Diagnostic information about the computer.
  }
  param {
    0.name = ~ignore_sensors
    0.type = string[]
    0.default = 
    0.desc = An array of sensors to ignore (the names of the sensors)
  }
}
```


