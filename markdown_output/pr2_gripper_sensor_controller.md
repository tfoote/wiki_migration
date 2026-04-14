## Introduction

The [pr2_gripper_sensor_controller](pr2_gripper_sensor_controller)
package is a real-time controller that is intended to support the
[pr2_gripper_sensor_action](pr2_gripper_sensor_action) interface and
allow it to:

a\. Act as a fully compatible replacement for the simpler
[pr2_gripper_action](pr2_gripper_action) interface. a. Provide new
functionality to allow more complex gripper actions in real-time that
are able to delicately and sensitively control the gripper position and
force, as well as provide a wealth of sensory feedback.

\'\'\'Currently the
[pr2_gripper_sensor_controller](pr2_gripper_sensor_controller) can only
be accessed over the
[pr2_gripper_sensor_action](pr2_gripper_sensor_action) action interface.
There is no other API support at this time. Please refer to the
[pr2_gripper_sensor_action](pr2_gripper_sensor_action) wiki page for
usage and feature information.\'\'\'

![alt text\|width=780](attachment:wiki_control_flow_diagram_controller.png)

The [pr2_gripper_sensor_controller](pr2_gripper_sensor_controller)
package continuously publishes several messages defined in the
[pr2_gripper_sensor_msgs](pr2_gripper_sensor_msgs) package, which are
intended for use in the action servers of
[pr2_gripper_sensor_action](pr2_gripper_sensor_action) and not for
normal user usage, but can provide useful information for more advanced
users.

## Hardware Dependecies

The [pr2_gripper_sensor_controller](pr2_gripper_sensor_controller)
\'\'\'requires\'\'\' two important PR2 sensors to be available:

-   A
    [palm-mounted accelerometer](ethercat_hardware/Tutorials/GripperAccelerometer),
    which should exist on all modern PR2 robots.

```{=html}
<!-- -->
```
-   [Pressure-sensitive fingertips](pr2_hardware_interface), which are
    an optional hardware add-on for all modern PR2 that require a brief
    installation procedure \[installation link?\].

A simple test to check if these sensors exist is to run the command
`rostopic list` and check to make sure the `/accelerometer` and
`/pressure` fields are present.

## Running the Controller

### Compiling

If you are not using a prebuilt installation you may have to compile the
[pr2_gripper_sensor_controller](pr2_gripper_sensor_controller) package.
Since the [pr2_gripper_sensor_controller](pr2_gripper_sensor_controller)
package is a real-time controller, it is important to remember to
compile the package \'\'\'before\'\'\' launching your robot, otherwise
it will fail to register and load correctly with [pluginlib](pluginlib).
Compiling can be done simply by typing: ```
rosmake pr2_gripper_sensor_controller
```

Or by building any of the higher-level packages (such as
[pr2_gripper_sensor_action](pr2_gripper_sensor_action) which depend on
this package) \'\'\'before\'\'\' launching your robot.

### Launching

See the [pr2_gripper_sensor_action](pr2_gripper_sensor_action) launch
instructions, which will automatically launch the
[pr2_gripper_sensor_controller](pr2_gripper_sensor_controller) package
for both the left and right PR2 grippers. Specific left/right launch
files are available in the
[pr2_gripper_sensor_controller](pr2_gripper_sensor_controller) package,
but it is unecessary for the end user to launch them independently.
