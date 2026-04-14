This package contains YAML files that are used to configure the default
controllers controllers on the Care-O-bot. The package also contains a
[roslaunch](roslaunch) file that configures, loads and starts the
default controllers via
[pr2_controller_manager](pr2_controller_manager). The default
controllers are:

-   for each wheel of the
    [base_controller](robot_mechanism_controllers/JointVelocityController)
-   arm
    [arm_controller](robot_mechanism_controllers/JointSplineTrajectoryController)
-   hand
    [sdh_controller](robot_mechanism_controllers/JointSplineTrajectoryController)
-   torso
    [torso_controller](robot_mechanism_controllers/JointSplineTrajectoryController)
-   head
    [head_controller](robot_mechanism_controllers/JointSplineTrajectoryController)
