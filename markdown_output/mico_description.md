## About

`mico_description` contains urdf and xacro files for the MICO arm. It
also includes a launch file for reading the robot model and setting up a
[joint_state_publisher](joint_state_publisher) and
[robot_state_publisher](robot_state_publisher) for visualization in
tools such as rviz.

## Organization

This package contains robot description files for the MICO arm,
organized into subdirectories as follows:

-   `urdf/` contains xacro representations of urdf descriptions of the
    arm and its parts, as well as a generated urdf file for the
    standalone arm.
-   `robots/` contains urdf descriptions for the arms as standalone
    robots.
-   `meshes/` contains mesh files for visualization and collision
    properties.

## Installation

To install the `wpi_jaco` package, you can install from source with
the following commands: . 

```shell
cd /(your catkin workspace)/src
git clone https://github.com/RIVeR-Lab/wpi_jaco.git
cd ..
catkin_make
catkin_make install
```



## Startup

The `mico_description` package includes a launch file that can be used
to load the robot model and setup joint state and robot state publishing
used to populate a tf tree and visualize the robot. Once launched, the
MICO model can be visualized in tools such as rviz. It can be launched
with the following command:

. 

```
roslaunch mico_description display.launch
```



The launch file also includes a parameter (`gui`) to launch a GUI
which can control each joint to test the model's behavior, which can be
launched as follows:

. 

```
roslaunch mico_description display.launch gui:=true
```


