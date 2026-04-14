# User manual

The Lizi Robot manual have all the information needed in order to use
and maintain your robot hardware. For software and ROS related
information use use this page and the [Tutorials](robotican/Tutorials)
page.

[Lizi Robot Manual](attachment:LiziManual_V1.0.pdf)

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

# Available sensors

-   HD Camera
-   SR300 RGBD camera
-   GPS
-   9-DoF IMU
-   3 x Ultrasonic Range Finders (left, rear, right)
-   Battery monitor
