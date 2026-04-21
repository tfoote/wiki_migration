This package contains the interface definitions (in header files) for
the [robot_controllers](robot_controllers) framework. ROS message
definitions are contained in the
[robot_controllers_msgs](robot_controllers_msgs) package. This is a
robot control infrastructure, developed initially for Fetch and Freight,
but designed to be robot-agnostic.

In comparison to ros_control, robot_controllers offers the ability to
"stack" controllers and avoids template-based hardware interfaces.
[robot_controllers](robot_controllers) has not be designed with
real-time constraints in mind, and is intended primarily for robots
where the real-time joint-level controllers are run in hardware, as is
the case for Fetch and Freight.

Documentation is primarily
[Doxygen-generated](http://docs.ros.org/indigo/api/robot_controllers_interface/html)
at this time.
