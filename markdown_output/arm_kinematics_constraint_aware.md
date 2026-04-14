This package provides a generic implementation of constraint aware
kinematics for any serial manipulator. It is based on a combination of
the ROS collision checking tools with KDL forward and inverse kinematics
solvers. This package exposes this functionality in three ways:

1\. C++ class: A C++ interface through a class that inherits from the
base class provided in the [kinematics_base](kinematics_base)
package. 1. ROS plugin interface: This interface allows other programs
to configure and use this implementation of kinematics at runtime. The
configuration is done through yaml and is described in more detail in
the [tutorials](arm_kinematics_constraint_aware/Tutorials) for setting
up a node. 1. A ROS node: This node has the same ROS API as the node
provided by the
[pr2_arm_kinematics_constraint_aware](pr2_arm_kinematics_constraint_aware)
package. It can use the plugin from this package or a custom plugin
created for a specific robot.

## Configuration for your own arm

Follow the [tutorials](arm_kinematics_constraint_aware/Tutorials) for
configuring this node for your own arm.
