# Package Summary

This package contains the parameter files that are used by the package
[amigo_gazebo](amigo_gazebo) to set up the controllers for the gazebo
simulation. These parameter files are formatted as
[YAML-files](http://en.wikipedia.org/wiki/YAML) and are located in the
\'\'parameters\'\' directory of the package. This directory contains the
following files which contain the controller parameters:

-   \'\'\'arm_controllers.yaml\'\'\': Parameter file for the left and
    right arm controller
-   type (pr2_controller manager type)
-   joints/mechanisms (corresponding joints and mechanisms)
-   gains (controller parameters: p,i,d,i_clamp of the
    [control_toolbox](control_toolbox))
-   limits (limits on position, velocity and acceleration)
-   init_positions (initial reference position of the controller)
-   \'\'\'base_controller.yaml\'\'\': Parameter file for the setup of
    the base controller
-   type (pr2_controller manager type)
-   joints/mechanisms (corresponding joints and mechanisms)
-   \'\'\'base_pid.yaml\'\'\': Parameter file that contains the
    controller parameters of the base controller
-   limits (limits on position, velocity and acceleration)
-   gains (controller parameters: p,i,d,i_clamp of the
    [control_toolbox](control_toolbox))
-   Intertia properties
-   \'\'\'filter.yaml\'\'\': Parameter file that contains the parameters
    for the lowpass-filter
-   \'\'\'gripper_controllers.yaml\'\'\': Parameter file that contains
    the parameters of the gripper controller
-   type (pr2_controller manager type)
-   joints/mechanisms (corresponding joints and mechanisms)
-   gains (controller parameters: p,i,d,i_clamp of the
    [control_toolbox](control_toolbox))
-   limits (limits on position, velocity and acceleration)
-   init_positions (initial reference position of the controller)
-   \'\'\'head_controller.yaml\'\'\': Parameter file that contains the
    parameters of the head controller
-   type (pr2_controller manager type)
-   joints/mechanisms (corresponding joints and mechanisms)
-   gains (controller parameters: p,i,d,i_clamp of the
    [control_toolbox](control_toolbox))
-   limits (limits on position, velocity and acceleration)
-   init_positions (initial reference position of the controller)
-   \'\'\'odom_publisher.yaml\'\'\': Parameter file that contains the
    parameters of the odometry publisher
-   type (pr2_controller manager type)
-   joints/mechanisms (corresponding joints and mechanisms)
-   publish_tf (boolean that describes if the tf needs to be published)
-   \'\'\'spindle_controller.yaml\'\'\': Parameter file that contains
    the parameters of the spindle controller
-   type (pr2_controller manager type)
-   joints/mechanisms (corresponding joints and mechanisms)
-   gains (controller parameters: p,i,d,i_clamp of the
    [control_toolbox](control_toolbox))
-   feedforward (controller parameters feedforward)
-   limits (limits on position, velocity and acceleration)
-   init_positions (initial reference position of the controller)
