See [Robots/CIR-KIT-Unit03](Robots/CIR-KIT-Unit03) for instructions and
tutorials.

## Overview

The `cirkit_unit03_gazebo` package contains launch and configuration
files for using the CIR-KIT-Unit03 robot in a simulated environment
(i.e. [Gazebo](http://gazebosim.org/)).

### Launch Simulation

The `husky_empty_world.launch` file pulls in
[ros_control](ros_control)
([steer_drive_controller](steer_drive_controller)) configuration from
[cirkit_unit03_control](cirkit_unit03_control), starts a
[Gazebo](http://gazebosim.org/) instance with a world where a couple of
obstacles are set, and loads the simulated Husky description via
`cirkit_unit03_world.launch`.

The `cirkit_unit03_clearpath_playpen.launch` file demonstrates how to
select an alternative world for the simulation. The world file called
from the launch is slightly modified from one used in
[husky_gazebo](husky_gazebo).

### Simulation Configuration

The `description_gazebo.launch` file loads the standard Husky URDF
from [cirkit_unit03_description](cirkit_unit03_description), along with
the requisite Gazebo plugins for simulation. T
