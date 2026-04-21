![](attachment:mini_max.png)

## Package Organization

This package contains robot description and configuration files for the
Mini Maxwell platform, organized into subdirectories as follows:

-   *docs*/ contains harwdare documentation.
-   *urdf*/ contains ([xacro](xacro) representations of) [urdf](urdf)
    descriptions of various parts of Mini Maxwell (arm, head, etc.), and
    the full robot.
-   *meshes*/ contains mesh files (.stl) for visualization and collision
    properties
-   *params*/ contains yaml specification files for the ArbotiX driver
    and diagnostics.
-   *launch*/ contains [roslaunch](roslaunch) files for starting up Mini
    Max, on real hardware, or in simulation:
-   *bringup.launch* - starts the real hardware.
-   *fake-mini.launch* - brings up a simulated version (not in
    Gazebo/Stage).
-   *simple_arm_server.launch* - brings up the arm controllers.
-   *nodes*/ contains several python-based nodes, which currently have
    no home.

## Starting Up Mini Maxwell

Please see the
[Bringup Tutorial](mini_max/Tutorials/Starting up Mini Max)
