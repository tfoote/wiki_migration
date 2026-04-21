This package provides generic nodes for monitoring a linux host.

## Nodes



```clearsilver
node.0 {
name = hd_monitor.py
desc = Monitor hard drive status through the hddtemp daemon. This checks each drive's temperature using SMART, and checks that drives have not been removed or unplugged.
pub {
0.name = diagnostics
0.type = diagnostic_msgs/DiagnosticArray
0.desc = Hard drive diagnostic information
}
}
node.1 {
name = ntp_monitor.py
desc = Monitor NTP sync status between computers. The hostname to connect is specified as the first command-line argument, and the offset tolerances can be set with additional command-line arguments. See `rosrun diagnostic_common_diagnostics ntp_monitor.py -h` for more options.
pub {
0.name = diagnostics
0.type = diagnostic_msgs/DiagnosticArray
0.desc = NTP diagnostic information
}
}
node.2 {
name = sensors_monitor.py
desc = Monitor system sensors using the `sensors` command. This checks the system's built-in temperature, voltage, and fan speed status, using the system's default thresholds.
param {
0.name = ~ignore_fans
0.type = bool
0.desc = Ignore fan speed warnings
0.default = False
}
pub {
0.name = diagnostics
0.type = diagnostic_msgs/DiagnosticArray
0.desc = Sensor diagnostic information
}
}
node.3 {
name = tf_monitor.py
desc = Monitor TF status. Checks are made that TF messages are being published, that transforms are up-to-date, that no cycles are present in the TF status, that there is a single authority publishing each transform, and that frames have a consistent parent.
sub {
0.name = tf
0.type = tf/tfMessage
0.desc = TF topic
}
pub {
0.name = diagnostics
0.type = diagnostic_msgs/DiagnosticArray
0.desc = TF diagnostic information
}
}
```


