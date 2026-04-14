## Overview

This package provides a library that can be used to represent the
environment and the robot itself. It is used to generate collision
information for contacts between the robot and the world. Object
information can be added to this world either as raw point cloud
information or as 3D meshes of known objects. The
[planning_environment](planning_environment) package provides a ROS API
to the collision space and can be used to modify the collision
environment throough a set of service calls.

## API

-   C++ API is UNREVIEWED and UNSTABLE
