## About

  -- -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- -- -------------------------------------------------------- --
     <tablewidth="100%" tablestyle="text-aligh:left">The `wpi_jaco` metapackage contains ROS packages and nodes that can be used to communicate with the [Kinova's](http://www.kinovarobotics.com/service-robotics/products/robot-arms/) JACO, JACO2, and MICO robot arms. The [wpi_jaco_wrapper](wpi_jaco_wrapper) package provides basic control, advanced trajectory control, and manipulation actions for both types of arm. The [jaco_interaction](jaco_interaction) package provides teleoperation via joystick, keyboard, and interactive marker control for the JACO and JACO2. The [jaco_description](jaco_description) and [mico_description](mico_description) packages contain urdf and xacro files, Collada models, and Solidworks models, as well as launch files for visualizing the robot model, and the [jaco_sdk](jaco_sdk) package contains Kinova's API for communicating with the JACO, JACO2, and MICO arms. The [jaco_moveit_config](jaco_moveit_config) and [mico_moveit_config](mico_moveit_config) packages provide example MoveIt! configurations for the JACO and MICO arms. The [wpi_jaco_msgs](wpi_jaco_msgs) package contains all of the messages, services, and actions used throughout the above packages.      ![\|height="209",width="180"](attachment:jaco.png)   
  -- -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- -- -------------------------------------------------------- --

## Notes about the JACO2

Not all of the functionality of the meta-package is implemented yet for
the JACO2. There's no jaco2_description package yet, providing a urdf
for the arm. Similarly, there is no sample MoveIt! configuration either,
which is waiting on the urdf before configuration is possible. As such,
the motion planning functionality found in the two moveit packages have
not yet been extended to the JACO2. All of the other functionality
should work as intended for the new arm.

## Installation

To install the `wpi_jaco` package, you can install from source with
the following commands:

. ```shell
cd /(your catkin workspace)/src
git clone https://github.com/RIVeR-Lab/wpi_jaco.git
cd ..
catkin_make
catkin_make install
```

## Startup

The [wpi_jaco_wrapper](wpi_jaco_wrapper) package contains a launch file,
`arm.launch`, to start all of the nodes required to communicate with
the JACO arm. Once these nodes are launched, further launch files can be
run from the other packages, all of which are documented in their
respective wiki pages.

## Support

Please send bug reports to the
[GitHub Issue Tracker](https://github.com/RIVeR-Lab/wpi_jaco/issues).
