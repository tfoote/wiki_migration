## Overview

This package is part of the [ROS-Industrial](Industrial) program.

## Status

The package is usable as-is, but is not feature complete. However, no
significant development is planned, as development focus has shifted to
[abb_robot_driver](https://github.com/ros-industrial/abb_robot_driver)
(with [abb_libegm](https://github.com/ros-industrial/abb_libegm) and
[abb_librws](https://github.com/ros-industrial/abb_librws)).

Community contributed usability enhancements and new features will
however be accepted and merged.

## YuMi

While it is possible to use this driver with !YuMi, for now this is not
recommended.

Users who have the EGM option available, consider using
[abb_robot_driver](https://github.com/ros-industrial/abb_robot_driver),
as it will offer the best possible motion quality.

The driver does not include any robot models (ie: \`\_description\`
packages) however. Various sources for those exist, one of which could
be [kth-ros-pkg/yumi](https://github.com/kth-ros-pkg/yumi).

## Features

This package currently supports the following:

-   IRC5 controllers with !RobotWare 5.13 and up
-   Single mechanical units (ie: a basic 6 axis robot)
-   Up to 4 integrated external \'\'linear\'\' axes (in a single
    mechanical unit)
-   Joint state reporting for all axes (in a single mechanical unit)
-   Trajectory downloading for all axes (in a single mechanical unit)

The driver is largely manipulator agnostic, meaning that it will work
with just about any ABB robot an IRC5 controller is compatible with.

### Multi-group robots

There is no special support for robot controllers configured with
multiple mechanical units, but this can be worked-around by setting up
multiple instances of the RAPID programs and assigning them to specific
units. Paired with multiple instances of the ROS nodes (appropriately
namespaced) this supports asynchronous motion execution and state
reporting in multi-group robot setups.

## Requirements

The ABB ROS Server code is written in RAPID, using a socket interface
and multiple parallel tasks. The code was originally tested on an IRC5
controller, with an IRB-2400 robot, but other combinations should also
work. The following controller options are required:

-   \`623-1\`: \'\'Multitasking\'\'
-   \`672-1\`: \'\'Socket Messaging\'\' (in recent !RobotWare versions,
    this option is included with \`616-1\`: \'\'PC Interface\'\')

!RobotWare OS version 5.13 or later is required due to the use of
certain socket options. Earlier versions may work, but will require
modifications to the RAPID code.

## Tutorials

Use the links on the [Tutorials](abb/Tutorials) page for access to the
tutorials. These explain how to install and set up the RAPID programs on
the controller, as well as how to use them in conjunction with the ROS
nodes in this package.

## Nodes

```clearsilver

node.0 {
  name=robot_state
  desc=Connects to the !StateServer RAPID task on the controller and publishes joint states.

  pub {
    0.name = joint_states
    0.type = sensor_msgs/JointState
    0.desc = Joint state for all joints of the connected robot.
  }

  pub {
    1.name = robot_status
    1.type = industrial_msgs/RobotStatus
    1.desc = Aggregate controller/robot status (ie: drives enabled, motion possible, etc)
  }

  feedback {
    0.name = feedback_states
    0.type = control_msgs/FollowJointTrajectory
    0.desc = Provide feedback of current vs. desired joint position (and velocity/acceleration).
  }

  param {
    0.name = robot_ip_address
    0.type = str
    0.desc = IP address of the controller to connect to. If this is not set the node will exit.
    0.default = none
    1.name = ~port
    1.type = integer
    1.desc = TCP port the !StateServer RAPID task is listening on.
    1.default = 11002
    2.name = robot_description
    2.type = str
    2.desc = The urdf xml robot description.
    2.default = none
    3.name = controller_joint_names
    3.type = [str, str, str, ..]
    3.desc = (optional) A list containing all joints the driver should assume control over. If this parameter is not found, the driver will try to extract this from the `robot_description` parameter, but this will result in all joints in the urdf to be included. If the driver should only publish joint states for a subset of the joints in the urdf, the `controller_joint_names` parameter must be set.
  }
}

node.1 {
  name=motion_download_interface
  desc=Connects to the !MotionServer RAPID task on the controller and uploads trajectories.

  sub {
    0.name = joint_states
    0.type = sensor_msgs/JointState
    0.desc = Joint state for all joints of the connected robot.
    1.name = joint_path_command
    1.type = trajectory_msgs/JointTrajectory
    1.desc = Execute a pre-calculated joint trajectory on the robot.
  }

  srv {
    0.name = joint_path_command
    0.type = industrial_msgs/CmdJointTrajectory
    0.desc = Execute a new motion trajectory on the robot.
    1.name = stop_motion
    1.type = industrial_msgs/StopMotion
    1.desc = Stop execution of the current motion at the earliest time possible.
  }

  param {
    0.name = robot_ip_address
    0.type = str
    0.desc = IP address of the controller to connect to. If this is not set the node will exit.
    0.default = none
    1.name = ~port
    1.type = integer
    1.desc = TCP port the !MotionServer RAPID program is listening on.
    1.default = 11000
    2.name = robot_description
    2.type = str
    2.desc = The urdf xml robot description.
    2.default = none
    3.name = controller_joint_names
    3.type = [str, str, str, ..]
    3.desc = (optional) A list containing all joints the driver should assume control over. If this parameter is not found, the driver will try to extract this from the `robot_description` parameter, but this will result in all joints in the urdf to be included. If the driver should only control a subset of the joints in the urdf, the `controller_joint_names` parameter must be set.
    3.default = none
  }
}
```

[Included page industrial/contact_us_tech_support not found](Included page industrial/contact_us_tech_support not found)
