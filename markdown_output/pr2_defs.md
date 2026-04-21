## Package Organization

This package contains robot description files for PR2, organized into
subdirectories as follows:

-   *calibration*/ contains calibration parameters included by urdf
    files
-   *defs*/ contains ([xacro](xacro) representations of) [urdf](urdf)
    descriptions of various parts of the PR2 (arm, torso, etc.)
-   *robots*/ contains ([xacro](xacro) representations of) [urdf](urdf)
    descriptions of the full robot, that refer to the macros in *defs*/
-   *meshes*/ contains mesh files (.stl) for visualization and collision
    properties
-   *launch*/ contains [roslaunch](roslaunch) files that upload the
    robot urdf descriptions to the parameter server

## Status and Roadmap (Oct 2009)

Note that this package evolved organically, together the the prototype
hardware at Willow Garage, and currently includes definitions for a
large number of legacy pieces of hardware, as well as specific
configurations that currently exist at Willow Garage. This package is
being replaced by a version which properly represents the production
hardware before the 1.0 release of this stack: see the
[pr2_description](pr2_description) package.

## Tutorials

No tutorials for this exist right now. Several of the
[URDF tutorials](urdf/Tutorials) explain the files in this package in
detail. See also [robot_model](robot_model) and
[simulator_gazebo](simulator_gazebo).
