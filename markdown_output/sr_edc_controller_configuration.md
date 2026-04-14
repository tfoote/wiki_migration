## Overview

This package contains the parameters for the different types of
controllers and the launch files for the controllers as well.

By default , you\'ll load the different controllers from this package,
using the provided launch files and configurations. You\'ll also save
your parameters to those yaml files.

See [sr_edc_mechanism_controllers](sr_edc_mechanism_controllers) for
more details on the actual implementation of the controllers.

## Controllers Parameters

The Parameters are saved in the different \'\'\'.yaml\'\'\' file:

-   \'\'\'motor_board_effort_controllers.yaml\'\'\': PIDs for the force
    controller running on the motor board. They are loaded by the
    calibration controllers.
-   \'\'\'motor_board_effort_controllers_stopped.yaml\'\'\': PIDs for
    the force controller running on the motor board, all parameters are
    set to 0, so the motors are stopped (useful for testing).
-   \'\'\'sr_edc_calibration_controllers.yaml\'\'\': just contains the
    joint names and the calibration controller used for Shadow Robot\'s
    hand. Our calibration controller are not doing any calibration.
-   \'\'\'sr_edc_effort_controllers.yaml\'\'\': the parameters for the
    effort controllers running on the hostside. Those controllers are
    dummy controllers as the real force control is done on the motor
    side.
-   \'\'\'sr_edc_joint_position_controllers.yaml\'\'\': the parameters
    for the joint positions controllers.
-   \'\'\'sr_edc_joint_velocity_controllers.yaml\'\'\': the parameters
    for the velocity controllers.
-   \'\'\'sr_edc_mixed_position_velocity_joint_controllers.yaml\'\'\':
    the parameters for the mixed position and velocity controllers.

## Launch files

The package also contains one launch file per controller type. You can
change which controller is started by default by editing
\'\'\'sr_edc_default_controllers.launch\'\'\'. Just make sure you only
have one type of controllers started (otherwise one of them is going to
be ignored by the controller manager).

The controller manager is started by the
\'\'\'sr_edc_controller_manager.launch\'\'\' file (which is called from
[sr_edc_launch](sr_edc_launch)/sr_edc.launch file).
