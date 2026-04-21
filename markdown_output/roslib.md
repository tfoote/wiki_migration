## Overview

`roslib` is the base dependency of all ROS
[Client Libraries](Client Libraries) and tools. It contains common tools
like the generators for [Messages](Messages) and [Services](Services) as
well as common message definitions like `Header` and `Log`. It also
contains the common path-bootstrapping code for ROS Python nodes and
tools.

## roslib for C++ Developers

roslib contains the definition of the `ros::Time` and
`ros::Duration` objects used in [roscpp](roscpp) and other ROS C++
libraries. It also contains functions for querying the ROS package
system. Please see the [Code API](http://ros.org/doc/api/roslib/html/)
and the [roscpp Time overview](roscpp/Overview/Time) for more details.

## roslib for Python Developers

If you are a Python developer, you might be confused that there are both
the [roslib](roslib) and [rospy](rospy) packages that support Python
development in ROS. In fact, some of the functionality they provide is
very similar.

There is only one line of `roslib` you need to know, which exists for
bootstrapping reasons:```
import roslib; roslib.load_manifest('YOUR_PACKAGE_NAME')
```

Otherwise, the simple answer is **use [rospy](rospy)**. Unless you're
more familiar with ROS Python development, `rospy` should provide you
with all the APIs you need to run a node, call services, access the
Parameter Server, etc\... roslib is primarily an internal library used
by ROS core developers to write tools.

## Developer tools for client library authors

`roslib` contains command-line tools for message generation necessary
for ROS [client library](Client Libraries) authors. These tools are
[documented here](roslib/gentools).

## Roadmap

Currently no new features are planned for `roslib`. But as new, common
functionality is added to the ROS platform, it will likely be supported
by libraries here.
