## Package Summary

This package contains the different controllers and launch files for the
[RB1 BASE robot](Robots/RB1 BASE) simulation.

-   Autor: Robotnik Automation
-   License: BSD
-   Source: git <https://github.com/RobotnikAutomation/rb1_base_sim.git>

![RB1 BASE Gazebo\|width=\"600px\"](attachment:rb1_base_gazebo.png)

## List of packages

### rb1_base_control

This package contains the launch and configuration files to spawn the
joint controllers with the ROS controller_manager. It allows to launch
the joint controllers for the RB1 BASE.

### rb1_base_gazebo

This package contains the configuration files to launch the Gazebo
environment along with the simulated robot.

### rb1_base_control

Control the robot joints in all kinematic configurations, publishes odom
topic and, if configured, also tf odom to base_link. Usually takes as
input joystick commands and generates as outputs references for the
gazebo controllers defined in rb1_base_control.

### rb1_base_2dnav

This package configures the move base stack and makes use of the
gmapping and amcl algorithms to move the rb1_base robot.

### rb1_base_purepursuit

This package contains the implemented pure pursuit algorithm for RB1
base.

## Simulating RB1 BASE

1\. Install the following dependencies:

-   [ rb1_base_common]( rb1_base_common )
-   [ robotnik_msgs]( robotnik_msgs)
-   [ robotnik_sensors]( robotnik_sensors)

2\. Launch RB1 BASE simulation with:

-   roslaunch rb1_base_sim rb1_sim.launch

3\. Enjoy! You can use the topic \"/rb1_base_control/cmd_vel\" to
control the RB1 BASE robot.
