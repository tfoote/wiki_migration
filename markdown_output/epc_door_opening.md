## Hardware Requirements

To run this code, the PR2 must grasp a hook. At the Healthcare Robotics
Lab, we 3D print a hook end effector and a tool adapter for the PR2 to
grasp it. These can be downloaded from:

-   [Hook End Effector](http://www.hsi.gatech.edu/hrl-wiki/index.php/Hook_End_Effector)
-   [ Tool Adapter](http://www.hsi.gatech.edu/hrl-wiki/index.php/PR2_Tool_Adapter)

## Running the Code

Steps to run the door opening code on a PR2: 1. Launch the Cartesian
controller, node to estimate mechanism kinematics, and end effector
forces. ```
$ roslaunch epc_door_opening pr2_door_opening.launch
``` 1. Run the door opening equilibrium
point controller ```
$ roscd epc_door_opening/src/epc_door_opening/
$ python door_epc.py
``` and follow the on screen
instructions.

## Limitations

The code released within this package is identical in spirit to our
previous implementation of door opening on the robot Cody, which we
released in [2010_icra_epc_pull](2010_icra_epc_pull).

However, this package implements a subset of the functionality of
[2010_icra_epc_pull](2010_icra_epc_pull), and has poorer performance in
its current implementation. In particular:

-   This package contains code to open a cabinet door or drawer once the
    robot is positioned in front of the mechanism. It does not address
    navigating up to the mechanism.
-   The mobile base of the robot is kept stationary.
-   The code has not been tested extensively as
    [2010_icra_epc_pull](2010_icra_epc_pull). For example, we do not
    know what the performance will be for different positions of the
    robot relative to the mechanism handle.
-   We are using estimates of the force at the end effector (via the
    joint torques), instead of directly measuring the force using a
    force-torque sensor.
-   The robot will fail to open mechanisms that require a large force to
    open (such as most refrigerators, spring loaded doors). We have
    tested it on two different cabinets.
