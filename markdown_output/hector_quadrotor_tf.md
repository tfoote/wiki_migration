## Documentation

This package provides a convenient gamepad based control option for
quadrotor UAVs and similar vehicles. By default, the provided launch
files provide a configuration similar to the \"Mode 2\" control scheme
on RC helicopters as described
[ here](http://www.rc-airplane-world.com/rc-helicopter-transmitter-modes.html ).
The node publishes
[ geometry_msgs/Twist](http://www.ros.org/doc/api/geometry_msgs/html/msg/Twist.html )
messages on the \'/cmd_vel\' topic by default, the control input on the
gamepad thus represents desired translational and angular velocities.
