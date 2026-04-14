## The Basics

This Lua package provides an implementation of [actionlib](actionlib) in
[Lua](http://www.lua.org). It uses [roslua](roslua) to use and provide
actions by and to other ROS nodes.

You can find the newest version at
<http://github.com/timn/ros-actionlib_lua>.

## How to use

Clone the repository in your ROS package path. Afterwards, you can
simply use the module. You can find examples in the src/test directory.
To run these examples, make sure that the actionlib_tutorial directory
from the ros_pkg_tutorials repository is in your package path. Then run
the client and the server connecting to the same ROS master.
