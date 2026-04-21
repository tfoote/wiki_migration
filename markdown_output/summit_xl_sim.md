## Package Summary

This package contains the different controllers and launch files for the
[SummitXL robot](Robots/SummitXL) simulation.

-   Autor: Robotnik Automation
-   License: BSD
-   Source: git
    <https://github.com/RobotnikAutomation/summit_xl_sim.git>

![SummitXL Gazebo\|width="600px"](attachment:summit_xl_gazebo.png)

## List of packages

### summit_xl_control

This package contains the launch and configuration files to spawn the
joint controllers with the ROS controller_manager. It allows to launch
the joint controllers for the Summit XL (4 axes skid steering + 2 axes
ptz), Summit XL OMNI (4 axes skid steering, 4 axes swerve drive), Summit
X-WAM (4 axes skid steering, 4 axes swerve drive, 1 linear axis for
scissor mechanism). The Summit XL simulation stack follows the
gazebo_ros controller manager scheme described in
<http://gazebosim.org/wiki/Tutorials/1.9/ROS_Control_with_Gazebo>

### summit_xl_gazebo

Launch files and world files to start the models in gazebo

### summit_xl_robot_control

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

### summit_xl_sim_bringup

Launch files that launch the complete simulation of the robot

## Simulating Summit XL

1\. Install the following dependencies:

-   [ summit_xl_common]( summit_xl_common )
-   [ robotnik_msgs]( robotnik_msgs)
-   [ robotnik_sensors]( robotnik_sensors)

2\. Launch Summit XL simulation with:

-   roslaunch summit_xl_sim_bringup summit_xl_complete.launch

3\. Enjoy! You can use the topic "/summit_xl_control/cmd_vel" to
control the Summit XL robot.
