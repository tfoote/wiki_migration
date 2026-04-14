This package includes the kinematic and geometric model of the robot
named \"tra1\". tra1 is an industrial robot manipulator with 6 DOFs, for
specialized to manipulate heavy weight object up to 20kg.

# Quick start

To visualize the robot model in rviz, type command as:

```
$ roslaunch tra1_description tra1.launch
``` The rviz and slider interface for joint angle
appears.

![ScreenShot\|width=\"75%\"](attachment:Screenshot from 2017-09-15 10-33-10.png)

# Package contents

The files organized into following directories.

-   urdf/ contains (xacro representations of) urdf descriptions of tra1.
-   meshes/ contains mesh files (.stl) for visualization and collision
    properties.
-   launch/ contains launch file to visualize the robot model in rviz.
