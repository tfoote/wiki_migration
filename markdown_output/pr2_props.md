Our PR2_Props based demo was accepted to IROS 2011. We hope to see
everyone there! [Youtube](https://www.youtube.com/watch?v=0K_0vSAzA3w)

![](attachment:props_pound.jpg)

## Overview

The goal of pr2_props, aside from just generally being awesome and
making you feel good, is to demonstrate the PR2's ability to do dynamic
human interaction. It has been designed to use low-latency real-time
controller packages like
[joint_trajectory_action](joint_trajectory_action) and
[pr2_gripper_sensor_action](pr2_gripper_sensor_action) so that PR2 is
capable of quickly and sensitively responding to a human slapping the
robot's hand.

Currently [pr2_props](pr2_props) supports 3 main behaviors:

-   High Five (with the left/right or both hands)
-   Low Five (with the left or right hand)
-   Pound (with the left/right or both hands) (with the ability to
    explode on impact)

## Getting pr2_props

The first step is getting the code from the upenn repository, or
installing the prebuilt binaries.

### Installing from binary

You can install pr2_props from the prebuilt binaries (diamondback,
electric, fuerte and unstable) with: ```
sudo apt-get install ros-<version>-pr2-props-stack
```

### Installing from source

Alternatively, you can checkout a local copy of the code and built it
yourself. To checkout the code using svn you should use the command
below: ```
svn co https://mediabox.grasp.upenn.edu/svn/penn-ros-pkgs/pr2_props_stack/trunk/pr2_props ~/ros/pr2_props
```

#### Compiling

Before using pr2_props you must compile it and it's dependencies. This
can be done simply by running: ```
rosmake pr2_props
``` If you have not
previously built the real-time controller libraries associated with the
[pr2_gripper_sensor_action](pr2_gripper_sensor_action) package
dependency it is important you build pr2_props prior to launching the
robot.

Above we assume /ros is part of your ROS_PACKAGE_PATH

## Running

Once you have compiled pr2_props there is one simple step you must do
before you can celebrate with your robot. First you need to launch the
real-time controllers that allow the robot to sense dynamic hand
contact. This can be done simply by: ```
roslaunch pr2_props pr2_props.launch
```

After this you are free to party with your robot in any of the following
ways: ```
for continuous repeating of different props:
rosrun  pr2_props run_all_props.sh 
or individually one-by-one:
rosrun pr2_props high_five (left/right/double)
rosrun pr2_props low_five (left/right)
rosrun pr2_props pound (left/right/double) (explode/explosion)
rosrun pr2_props repeat_high_five
rosrun pr2_props hug
``` In the above commands the values inside
() are optional. The robot is naturally right-handed if no hand is
specified. `explode` and `explosion` have the same effect.
