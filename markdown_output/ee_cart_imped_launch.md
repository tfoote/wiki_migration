## Overview

This package contains launch files for the ee_cart_imped control stack.
There are two launch files:

-   \'\'\'ee_cart_imped.launch\'\'\' inhibits the usual arm controllers
    and starts the EECartImped controller on both arms. The arm
    controllers cannot be re-started until this launch file is killed.
    To launch the controller on just one arm, use the launch files in
    [ee_cart_imped_action](ee_cart_imped_action)/launch.
-   \'\'\'load_ee_cart_imped.launch\'\'\' loads but does not start the
    EECartImped controller. The controller can be stopped and started,
    allowing it to be swapped out with other controllers, using the
    [pr2_controller_interface](http://www.ros.org/doc/electric/api/pr2_controller_manager/html/pr2__controller__manager__interface_8py.html)
    from the [pr2_controller_manager](pr2_controller_manager) package.
    For an example, see
    [this tutorial](ee_cart_imped/Tutorials/Switching Controllers at Run Time (Python)).

Launch files more specific to the action and the controller are located
in those packages. These include

-   [ee_cart_imped_action](ee_cart_imped_action)/launch/r_arm_cart_imped_action.launch:
    Launches the controller and action server for the right arm only.
-   [ee_cart_imped_action](ee_cart_imped_action)/launch/l_arm_cart_imped_action.launch:
    Launches the controller and action server for the left arm only.
-   [ee_cart_imped_control](ee_cart_imped_control)/launch/r_arm_cart_imped_controller.launch:
    Loads the controller onto the parameter server, inhibits the
    r_arm_controller and starts the force/impedance controller on the
    right arm only. Since all interaction with the controller should be
    done through the action server, this launch file should be used in
    isolation only for debugging purposes.
-   [ee_cart_imped_control](ee_cart_imped_control)/launch/l_arm_cart_imped_controller.launch:
    Loads the controller onto the parameter server, inhibits the
    l_arm_controller and starts the force/impedance controller on the
    left arm only. Since all interaction with the controller should be
    done through the action server, this launch file should be used in
    isolation only for debugging purposes.
