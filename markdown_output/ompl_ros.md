This package contains a ROS interface to [ompl](ompl). Since the
\'\'\'ompl\'\'\' planning library itself does not contain collision
checking or robot modeling code (it has abstract implementations of
these), we need a layer on top of this, that uses the
[planning_environment](planning_environment) package to provide an
implementation for the abstract interfaces \'\'\'ompl\'\'\' needs
satisfied.

More documentation on the content of this library is available
[here](http://www.ros.org/doc/api/ompl_ros/html/index.html).

## ROS API

-   The ROS API is UNREVIEWED and UNSTABLE
-   The C++ API is UNREVIEWED and UNSTABLE
