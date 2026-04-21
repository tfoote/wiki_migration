## Overview

This package is part of the [ROS-Industrial](Industrial) program. It
currently contains nodes that support communication with Universal
Robots' industrial robot controllers.

## Deprecation

```wiki
This package has been deprecated and should not be used any longer with CB3 and e-Series controllers. Any controller with Polyscope version `v3.x` or `v5.x` should use [[ur_robot_driver]] instead.

Refer to [[https://discourse.ros.org/t/deprecation-of-ur-modern-driver/11629|Deprecation of ur_modern_driver]] on ROS Discourse for more information.
```

## Compatibility

```
{#!wiki version hydro_and_newer

=== Polyscope up to v1.8.x ===

As [[ur_robot_driver]] only supports CB3 and e-Series controllers, users with Polyscope versions `<= 1.8.x` could still consider using `ur_modern_driver`.

The package has been deprecated and will no longer be developed, but for Polyscope versions up to and including `v1.8.x`, it could still be useful.

=== Polyscope v3.x and v5.x ===

Users with CB3 or e-Series controllers must use [[ur_robot_driver]] instead.

For more information, refer to [[https://discourse.ros.org/t/deprecation-of-ur-modern-driver/11629|Deprecation of ur_modern_driver]] on ROS Discourse.
```}

## Installation

The following instructions assume that a
[Catkin workspace](http://wiki.ros.org/catkin/Tutorials/create_a_workspace)
has been created at \$HOME/catkin_ws and that the source space is at
\$HOME/catkin_ws/src. Update paths appropriately if they are different
on the build machine.

In all other cases the packages will have to be build from sources in a
Catkin workspace:

```shell
cd /path/to/catkin_ws/src

# retrieve the sources (note: "kinetic-devel" builds on Indigo, Kinetic and Melodic)
git clone -b kinetic-devel https://github.com/ros-industrial/ur_modern_driver.git

cd /path/to/catkin_ws

# checking dependencies (replace '$DISTRO' with the ROS version you are using)
rosdep update
rosdep install --from-paths src --ignore-src --rosdistro $DISTRO

# building
catkin build

# activate the workspace (careful when also using other workspaces)
source /path/to/catkin_ws/devel/setup.bash
```

The packages can now be used as regular ROS packages.

## Report a Bug

<<GitHubIssues(ros-industrial/ur_modern_driver)>>
