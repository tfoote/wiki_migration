## Overview

The \`industrial_robot_client\` package provides a standardized
interface for controlling industrial robots, based on the ROS-Industrial
[Specification](Industrial/Industrial_Robot_Driver_Spec). This package
includes a C++ reference implementation of the specification, using the
[simple_message](simple_message) protocol to communicate with a
compatible server running on a standalone industrial robot controller.

Primarily, this package provides the industrial_robot_client library.
The intent is for robot-specific implementations to reuse code from this
library using standard C++ derived-class mechanisms, to avoid much of
the copy/paste duplication in current industrial-robot driver
implementations. \'\'Modification to adapt the library to new robot
needs is discussed in more detail [below](#modification).\'\'

This package also provides generic nodes exposing the base
industrial_robot_client functionality. If a robot does not require any
specific client-side code, then it may be sufficient to run these
standard nodes. [This page](/generic_implementation) describes this
usage in more detail.

## Protocol documentation

The Simple Message (!SimpleMessage) protocol defines the message
structure between the ROS driver layer and the robot controller itself.

Refer to
[REP-I0006: Message Structures of the ROS-Industrial Simple Message Protocol](https://github.com/ros-industrial/rep/blob/master/rep-I0006.rst)
for a description of the protocol.

## Modification for Robot-Specific Needs

Often, differences between manufacturer interfaces and robot designs
will require changes to the basic reference implementation provided in
the industrial_robot_client library. Joint-coupling, velocity scaling,
and communications protocols are all potential reasons for
robot-specific control code.

Rather than make a new copy of the entire ROS client codebase, it is
recommended that the integrator use a derived-class approach to only
re-implement the minimal functionality required. Wherever possible, the
new code should call the base class reference-implementation functions
to avoid code duplication and maintain consistent operations. It may be
helpful to review the library\'s [design](/design) to determine which
functionality may need replacing. Simple joint reordering and renaming
can be handled through existing capabilities, as described
[here](/joint_naming).

### Example

The following example shows how to replace the reference velocity
calculation (0-100% of max-velocity) with an absolute velocity
algorithm.

1\. Create a new derived class, based on JointTrajectoryDownloader (or
JointTrajectoryStreamer) ```cplusplus
class myRobot_JointTrajectoryDownloader : JointTrajectoryDownloader
{
...
}
```

1\. Override specific functionality. In this case, the velocity
calculation. ```cplusplus
class myRobot_JointTrajectoryDownloader : JointTrajectoryDownloader
{

public:
  bool calc_velocity(const trajectory_msgs::JointTrajectoryPoint& pt, double* rbt_velocity)
  {
    if (pt.velocities.empty())
      *rbt_velocity = SAFE_SPEED;
    else
      *rbt_velocity = std::min(pt.velocities.begin(), pt.velocities.end());

    return true;
  }
}
```

1\. Implement a new node, using an instance of the appropriate
derived-class. ```cplusplus
int main(int argc, char** argv)
{
  // initialize node
  ros::init(argc, argv, "motion_interface");

  myRobot_JointTrajectoryDownloader motionInterface;
  motionInterface.init();
  motionInterface.run();

  return 0;
}
```

### Further examples

Further examples of creating robot-specific interfaces may be found in
the following code samples:

-   [ABB driver client](https://github.com/ros-industrial/abb/blob/kinetic-devel/abb_driver/src/abb_joint_downloader_node.cpp)

## Nodes

Besides the reusable libraries, this package also provides default
implementations of a set of generic nodes. The following is the ROS API
of those generic nodes.

```clearsilver

node.0 {
  name=robot_state
  desc=Connects to a robot state server program on a controller and publishes joint states.

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
    1.desc = TCP port the robot state server program is listening on.
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
  desc=Connects to a motion relay server program on the controller and uploads trajectories. Note: this is the ''download'' version of the interface, which means the entire trajectory is uploaded to the motion relay server program before motion is started.

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
    1.desc = TCP port the motion relay server program is listening on.
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

node.2 {
  name=motion_streaming_interface
  desc=Connects to a motion relay server program on the controller and streams trajectories. Note: this is the ''streaming'' version of the interface, which means trajectories are relayed piecewise to the motion relay server program and motion is expected to start immediately (or: as soon as possible).

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
    1.desc = TCP port the motion relay server program is listening on.
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

## Reporting bugs

\<\<GitHubIssues(ros-industrial/industrial_core)\>\>
