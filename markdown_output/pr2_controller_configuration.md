This package contains YAML files that are used to configure the default
controllers and the calibration controllers on the pr2. The package also
contains a [roslaunch](roslaunch) file that configures, loads and starts
the default controllers via
[pr2_controller_manager](pr2_controller_manager). The default
controllers are:

-   base:
-   [base_controller](pr2_mechanism_controllers/Pr2BaseController)
-   [base_odometry](pr2_mechanism_controllers/Pr2Odometry)
-   arms:
-   [r_arm_controller](robot_mechanism_controllers/JointSplineTrajectoryController)
-   [l_arm_controller](robot_mechanism_controllers/JointSplineTrajectoryController)
-   [r_gripper_controller](pr2_mechanism_controllers/Pr2GripperController)
-   [l_gripper_controller](pr2_mechanism_controllers/Pr2GripperController)
-   head:
-   [head_controller](robot_mechanism_controllers/JointSplineTrajectoryController)
-   [laser_tilt_controller](pr2_mechanism_controllers/LaserScannerTrajController)
-   torso
-   [torso_controller](robot_mechanism_controllers/JointSplineTrajectoryController)

These files are used in places such as [pr2_bringup](pr2_bringup) to
instantiate the default PR2 controllers.

For [pr2_simulator](pr2_simulator), a clone of this package with
separate configuration is in
[pr2_controller_configuration_gazebo](pr2_controller_configuration_gazebo).
