## Usage

To start, just execute screenrun. ```
rosrun screenrun screenrun [b]
``` If *b* is
passed, byobu is used instead of screen.

## Configuration

The programs to run will be read from a local parameter *programs* that
contains a list of programs to run. Commands will not be executed, but
inserted into the screen as if they were typed. Thus, Ctrl-C, \<up\>,
etc. should work. To actually run a command append \\015 (Enter) to a
command.

A screen session named *ros* is started and screen windows with the
program name are created, where the commands are entered. Usually the
*programs* parameter will come from a configuration or launch file. See
this example as a reference: ```
-
    name: planner
    commands:
        - roscd tidyup_grasp_actions\015
        - roslaunch tidyup_grasp_actions continual-planning-tidyup-grasp-tuck.launch 
-
    name: dashboard
    commands:
        - rosrun pr2_dashboard pr2_dashboard\015
```
