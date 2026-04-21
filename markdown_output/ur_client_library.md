## Overview

This package contains the C++ library for accessing Universal Robots
robotic arms from the CB3- or e-Series. It is the base of the
[ur_robot_driver](http://wiki.ros.org/ur_robot_driver).

## Compatibility

### Polyscope up to v1.8.x

This package does not support CB2 controllers.

For robots with Polyscope `v1.8.x` or older, please see whether
[ur_modern_driver](ur_modern_driver) is sufficient.

### Polyscope v3.x and v5.x

Make sure the controller runs `v3.7` or newer for CB3, or `v5.1` or
newer for e-Series controllers.

## Library Contents

Currently, this library contains the following components:

-   **Basic primary interface**: The primary interface isn't fully
    implemented at the current state and provides only basic
    functionality. See A word on the primary / secondary interface for
    further information about the primary interface.
-   **RTDE interface**: The RTDE interface is fully supported by this
    library. See RTDEClient for further information on how to use this
    library as an RTDE client.
-   **Dashboard interface**: The Dashboard server can be accessed
    directly from C++ through helper functions using this library.
-   **Custom motion streaming**: This library was initially developed as
    part of the Universal Robots ROS driver. Therefore, it also contains
    a mechanism to do data streaming through a custom socket, e.g. to
    perform motion command streaming.

## Additional information

Most documentation is handled inside the Githhub
[README](https://github.com/UniversalRobots/Universal_Robots_Client_Library/blob/master/README.md)
files.

## Contributing

<<GitHubIssues(UniversalRobots/Universal_Robots_Client_Library)>>
