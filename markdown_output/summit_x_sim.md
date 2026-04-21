## Package Summary

This package contains the different controllers and launch files for the
[SummitX robot](Robots/SummitX) simulation.

-   Autor: Robotnik Automation
-   License: BSD
-   Source: git <https://github.com/RobotnikAutomation/summit_x_sim.git>

![SummitX Gazebo\|width="600px"](attachment:summit_x_gazebo.png)

## List of packages

### summit_x_control

This package contains the launch and configuration files to spawn the
joint controllers with the ROS controller_manager.

### summit_x_gazebo

Launch files and world files to start the models in gazebo

### summit_x_robot_control

Control the robot joints in all kinematic configurations, publishes odom
topic and, if configured, also tf odom to base_link. Usually takes as
input joystick commands and generates as outputs references for the
gazebo controllers defined in summit_xl_control. This package permits an
alternative way to control the robot motion (4 motorwheels) that by
default is carried on by the Gazebo plugin (skid-steer). In the default
configuration this package only controls the pan-tilt camera joints.
When used as main controller of the simulated robot, this node also
computes the odometry of the robot using the joint movements and a IMU
and publish this odometry to /odom. The node has a flag in the yaml
files that forces the publication or not of the odom->base_footprint
frames, needed by the localization and mapping algorithms.
