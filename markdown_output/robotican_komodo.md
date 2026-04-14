# User manual

The Komodo Robot manual have all the information needed in order to use
and maintain your robot hardware. For software and ROS related
information use use this page and the [Tutorials](robotican/Tutorials)
page.

[Komodo Robot Manual](attachment:Komodo_Manual_v2.2.pdf)

# Inerfaces

## All joints

Hardware interfaces:

-   [hardware_interface::JointStateInterface](hardware_interface)

Controllers:

-   [joint_state_controller/JointStateController](joint_state_controller)

## Mobile base

Hardware interfaces:

-   [hardware_interface::VelocityJointInterface](hardware_interface)

Controllers:

-   [joint_state_controller/JointStateController](joint_state_controller)
-   [diff_drive_controller::DiffDriveController](diff_drive_controller)

## Arm

Hardware interfaces:

-   [hardwareInterface::PosVelJointInterface](hardware_interface)

Controllers:

-   [position_velocity_controllers/JointTrajectoryController](https://github.com/robotican/robotican/blob/master/robotican_controllers/include/robotican_controllers/joint_trajectory_controller.h)

## Gripper

Hardware interfaces:

-   [hardwareInterface::PositionJointInterface](hardware_interface)

Controllers:

-   [position_controllers/GripperActionControllerTwo](position_controllers)

# Available sensors

-   HD Camera
-   RGBD Camera
-   SR300 RGBD camera (Above gripper)
-   GPS
-   9-DoF IMU
-   3 x Ultrasonic Range Finders (left, rear, right)
-   Emergency button
-   Battery monitor
