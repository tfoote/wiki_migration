This package provides new hardware interfaces to implement Cartesian ROS
control for robot manipulators.

## Rationale

Several OEMs provide native Cartesian interfaces in their robot drivers.
By offering new according hardware interfaces, implementers of ROS
controllers get direct access to Cartesian buffers for reading and
writing. Whether this provides advantages over the classic joint-based
interfaces of course depends on personal use cases. The main difference
is that in the Cartesian case the robot takes care of Inverse
Kinematics.

## Further information

For further information, especially how to integrate this into a RobotHW
interface, see the
[Documentation on GitHub](https://github.com/UniversalRobots/Universal_Robots_ROS_controllers_cartesian/blob/main/cartesian_interface/README.md)
