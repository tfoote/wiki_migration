## Overview

The \`pr2_drive_life_test\` package contains a tool to shuffle the PR2
during a [PR2 Burn In Test](life_test/PR2 Burn In). This tool should be
launched with the file
\`pr2_drive_life_test/pr2_drive_life_test.launch\`.

The script \`pr2_drive_life_test.py\` commands the PR2 base during the
PR2 burn in test. It runs a 500 Hz loop to command the base along a
sinusoidal path inside the PR2 burn-in test fixture.

The launch file contains a [map_server](map_server) and [amcl](amcl) to
localize the robot in the test fixture. The map \`life_test.pgm\` is
specific to the PR2 burn in text fixture.

### Reset / Relocalize

If the script detects that motors are halted, it will stop sending drive
commands until the service \`pr2_base/reset_drive\` is called. When the
service is called, the robot is relocalized to the center of the test
fixture by publishing on the \`initialpose\` topic.

This reset ability allows an operator to recenter a robot that has
gotten lost in the burn in test fixture.

### Listener

A special \"listener\" in
[pr2_hardware_test_monitor](pr2_hardware_test_monitor) listens to the
output from the \`pr2_drive_life_test.py\` script. It will call the
\`pr2_base/reset_drive\` service when needed.

## ROS API

```clearsilver
name = pr2_drive_life_test.py
desc = Drives the PR2 base during the PR2 burn in test.
sub {
  0.name = pr2_etherCAT/motors_halted
  0.type = std_msgs/Bool
  0.desc = Motors halted
}
pub {
  0.name = base_driving
  0.type = std_msgs/Bool
  0.desc = Whether robot is driving or not.
  1.name = visualization_markers
  1.type = visualization_msgs/Marker
  1.desc = Target/goal pose of the robot.
  2.name = cmd_vel
  2.type = geometry_msgs/Twist
  2.desc = Commanded velocity of the robot
  3.name = initialpose
  3.type = geometry_msgs/PoseWithCovarianceStamped
  3.desc = Initial pose of the robot
}
srv {
  0.name = pr2_base/halt_drive
  0.type = std_srvs/Empty
  0.desc = Stop sending drive commands
  1.name = pr2_base/reset_drive
  1.type = std_srvs/Empty
  1.desc = Restart sending drive commands
}
```
