## Overview

This package contains CIR-KIT-Unit03 control configuration, for
interfacing with [ros_control](ros_control)
([steer_drive_controller](steer_drive_controller)),
[ira_laser_tools](https://github.com/iralabdisco/ira_laser_tools),
[laser_filters](laser_filters), and
[lower_step_detector](lower_step_detector). All file paths are relative
to the base package.

### Sensor Input

Scaned data from 2 LRFs on CIR-KIT-Unit03 is merged with
[ira_laser_tools](https://github.com/iralabdisco/ira_laser_tools) and
filtered via [laser_filters](laser_filters).

[lower_step_detector](lower_step_detector) can be used as and downstairs
detection by installing a LRF with a lower angle.

### Velocity Input

CIR-KIT-Unit03 velocity input is directly received from
[steer_drive_controller](steer_drive_controller).
