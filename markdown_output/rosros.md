## Overview

Simple unified interface to ROS1 / ROS2 Python API

Auto-detects ROS version from run-time environment, and provides
equivalent functionality in either ROS version.

Main use-cases: - helper library for working with ROS messages and data
types - replacement for ROS1 / ROS2 Python API - drop-in replacement for
`rospy` to convert a ROS1 package to a ROS1/ROS2 package - drop-in
replacement for `rclpy` to convert a ROS2 package to a ROS1/ROS2
package

Requires the corresponding ROS Python libraries: `rospy` family for
ROS1, `rclpy` for ROS2.

Full API documentation available at <https://suurjaak.github.io/rosros>.
