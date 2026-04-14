/!\\ Under construction\...

## Nodes

There are several nodes (actually implemented as nodelets) that together
perform the task of high-level control. \'High level\' in this context
means that input is generally a state estimate, plus (optionally) user
inputs from a joystick, and the output is commanded pitch, roll, yaw or
yaw rate, and altitude. Other nodes, which will differ depending on the
particular vehicle in use, process these outputs according to the needs
of the specific hardware in question (see, e.g.,
[starmac_robots_asctec](starmac_robots_asctec)).

ROS API documentation for nodes in this package:

-   [controller](flyer_controller/controller) Controller manager
-   [teleop_flyer](flyer_controller/teleop_flyer)
-   [Control Modes](flyer_controller/control_modes) Individual control
    modes
