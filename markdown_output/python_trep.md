## Overview

Trep is a Python module for modeling articulated rigid body mechanical
systems in generalized coordinates. Trep supports basic simulation but
it is primarily designed to serve as a calculation engine for analysis
and optimal control algorithms that require 1st and 2nd derivatives of
the system's dynamics.

Full documentation is available at <http://nxr.northwestern.edu/trep>.

## ROS Tools

Trep currently provides two features for usage in ROS packages - A URDF
import tool and an extended MidpointVI class.

### URDF Import Tool

Trep can create a system model using certain tags from the
[URDF XML specification](http://wiki.ros.org/urdf/XML). The following
tags are supported:

-   Link - name
-   Inertial
-   origin
-   mass
-   inertia (only ixx,iyy,izz supported, off-axes should be zero)
-   Joint - name, type: fixed, continuous, prismatic (no joint limits)
-   origin
-   parent
-   child
-   dynamics (damping only)

Additionally, one extra tag is supported on the Joint tag. Specifying
kinematic=\'True\' creates a kinematic configuration variable in trep
for that joint.

An example of a system created from a URDF on the parameter server is:
```python
import rospy
import trep.ros as rostrep

system = rostrep.import_urdf(rospy.get_param('robot_description'))
```

Additionally, import_urdf can import the URDF onto an existing system
definition and can add a prefix to all of the frames and joints created
from the URDF using the following syntax: ```python
system = rostrep.import_urdf(rospy.get_param('robot_description'), 
         system=prev_system, prefix='new-prefix')
```

### ROSMidpointVI Integrator

The ROSMidpointVI class extends the MidpointVI class available in trep.
This class automatically publishes all frames imported from the URDF to
the `/tf` topic every time `ROSMidpointVI.step()` is called.

## Example Package

An example package called \`trep_urdf_demo\` is available at
<https://github.com/MurpheyLab/trep_urdf_demo>. This package has two
demos which can be called from launch files. After cloning the package
to your ROS workspace, run the following command:

-   \'\'\'RRbot simulator:\'\'\' ```
roslaunch trep_urdf_demo rrbot.launch
```

```{=html}
<!-- -->
```
-   \'\'\'Interactive marionette simulator:\'\'\'
    ```
roslaunch trep_urdf_demo puppet.launch
```
