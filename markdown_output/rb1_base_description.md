## Overview

This package contains the the urdf, meshes and other files needed to
create the rb1_base description. The package has the following folders:

\- **launch:** In this folder you will find the launch files ready to be
executed

\- **meshes:** In this folder you will find the STL files of the
different parts of the robots

\- **robots:** In this folder you will find the final description of the
robot, where all the parts are integrated

\- **urdf:** Here you will find the different possible parts of the
robot. Each one is a xacro file that will be included in the final
description

## Usage

To view and manipulate the non-fixed joints in [rviz](rviz), install the
package and execute the following command: ```
roslaunch rb1_base_description rb1_base_rviz.launch
```

On the other hand, if you are using either the simulation or the real
robot you will have to execute the following command:
```
roslaunch rb1_base_description rb1_base_state.launch
```

In case you want to change the robot's urdf, this can be found inside
the **robots** folder.
