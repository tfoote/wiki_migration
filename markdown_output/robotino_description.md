## Overview

The [robotino_description](robotino_description) package contains xacro
files and meshes required to create a urdf model of Robotino. This urdf
file is used by the [robot_state_publisher](robot_state_publisher)
package to broadcast transforms and also by [rviz](rviz) for
visualization.

### Usage

#### Generating/Updating a urdf file

If the xacro files are modified, then the \`robotino.urdf\` would have
to updated as well. This can be done by running the following command
from the \`robotino_description/urdf\` directory.

```
rosrun xacro xacro.py robotino.urdf.xacro > robotino.urdf
```
