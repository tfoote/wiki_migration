ros-arnl provides a ROS node that incorporates Adept MobileRobots' ARNL
localization and autonomous navigation system for Adept Mobile Robots
platforms, providing a basic ROS interface to ARNL.

ARNL is an optional package that may be purchased from Adept
MobileRobots with a laser rangefinder and robot. (It is, however,
included standard with the Pioneer LX robot.) See
<http://www.mobilerobots.com> for details.

ros-arnl connects directly to the robot and laser rangefinder (via ARNL
and ARIA libraries internally). It does not connect via any other nodes,
and so other nodes to be running to communicate with the mobile robot or
laser.

ros-arnl can be obtained by cloning the repository at
<http://github.com/MobileRobots/ros-arnl>.

You must have previously installed the ARNL libraries (Arnl and
ArnlBase) before building ros-arnl.

For instructions on building and notes on its API see the README file
provided with ros-arnl. ros-arnl has a similar interface to the standard
ROS navigation stack, but does not yet have all of the same features. It
has a few topics relevant to ARNL only as well.

ros-arnl is still under development, if you have any feedback, please
share via <http://github.com/MobileRobots/ros-arnl>.
