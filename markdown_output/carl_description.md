## About

`carl_description` contains urdf and xacro files for CARL, as well as
Collada models for all of the components. It also includes a launch file
for reading the robot model and setting up a joint_state_publisher and
robot_state_publisher for visualization in tools such as rviz.

## Organization

This package contains robot description files for CARL, organized into
subdirectories as follows:

-   `urdf/` contains xacro representations of urdf descriptions of the
    various robot components
-   `meshes/` contains mesh files for visualization
-   `robots/` contains a standalone model of the robot in both xacro
    and compiled urdf form

## Startup

The carl_description package includes a launch file that can be used to
load the robot model and setup joint state and robot state publishing
used to populate a tf tree and visualize the robot. Once launched, CARL
can be visualized in tools such as rviz. It can be launched with the
following command: ```
roslaunch carl_description view.launch
```
