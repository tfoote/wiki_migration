## Description

This package contains a launch file for the \`turtlebot_teleop_joy
\`node in [turtlebot_teleop](turtlebot_teleop) to teleoperate a robot
with a Thrustmaster T-Wireless gamepad. The launch file also includes
the \`turtlebot_teleop/launch/includes/velocity_smoother.launch.xml\`
file. A `joy_node `node from [joy](joy) is also loaded.

## Use

Just run

```
roslaunch wheeled_robin_teleop thrustmaster_teleop.launch
``` and use a Thrustmaster T-Wireless gamepad to
teleoperate the robot. Key 5 is used as Deadman Key. Left joystick is
used to drive the robot forward and backward, right joystick is used for
rotating the robot.
