# Installation requirements

You need to install the pr2_cockpit stack which contains the impedance
controller from Willow Garage. I recommend to use the Debian packages:

```
sudo apt-get install ros-electric-pr2-cockpit
```

Get the articulation stack from Freiburg: ```
cd ~/ros
svn co https://alufr-ros-pkg.googlecode.com/svn/trunk alufr-ros-pkg
svn co https://alufr-ros-pkg.googlecode.com/svn/branches/articulation-experimental
```

Compile: ```
rosmake articulation_pr2
```

# Running the demo

```
roslaunch /etc/ros/robot.launch
roslaunch pr2_teleop teleop_joystick.launch
roslaunch articulation_pr2 articulation_service.launch
```

Before you call the articulation service, make sure that the PR2 has
firmly grasped the handle. ```
rosrun articulation_pr2 articulate_object_client
```

# Parameters

All relevant parameters are in the articulation_service.launch file.

1\. \'\'\'sigma_position (in meters), default: 0.03, good choices: 0.01
\-- 0.05.\'\'\' Assumed noise in the translational components of the
observed trajectories (in meters). When sigma_position is small, the
robot will always select the most complex model (in our case, the
rotational model). In contrast, when sigma_position is large, the
simpler models will do better, so the prismatic model (or even the rigid
model) become more likely. 1. \'\'\'sigma_orientation (in radians),
default: 1.00, good choices: 0.1 \-- 1.00. \'\'\'Similar to
sigma_position, but for the orientations: This parameter defines the
assumed noise in the rotational components of the observed trajectories
(in radians). In our case, a large sigma_orientation is reasonable
because we grasp thin handles, so the observation of the orientation of
the handle during opening is not very accurate. 1. \'\'\'force_gain
(scalar), default: 4, good choices: 1 \-- 10.\'\'\' This parameter
determines how the pulling direction scaled to the next set point
(larger values mean that the set point will be placed further away; the
actual force is still limited by the saturation values of the impedance
controller, see below the rosparam section. Note that this value works
in combination with the desired_velocity setting in the service call:
\<code\>next_set_point = current_point + normalized_pulling_direction \*
desired_velocity \* force_gain\</code\> 1. \'\'\'vel_saturation_trans,
vel_saturation_rot (motor current?), default: 6.0, good choices: 1 \--
10\'\'\'. These parameters determine the saturation of the impedance
controller (larger values mean that the PR2 will pull stronger; when the
values are too small, the PR2 might not have enough force to pull
heavier objects open, if too large, it might loose the grasp). 1.
\'\'\'min_finger_distance, default: 0.00, good choices: 0.00 -
0.05.\'\'\' The PR2 checks the distance between its finger tips. If the
distance drops below min_finger_distance, it will abort the operation.

# Typical problems and solutions

-   Motion stops too early, PR2 seems to be too weak. Solutions:
-   Increase force_gain.
-   Increase vel_saturation_trans, vel_saturation_rot
-   PR2 pulls drawers along an arc instead of a line, the estimated
    model is rotational (in the console output), or the estimated model
    looks rotational in RVIZ.
-   increase the sigma_position and/or sigma_orientation.
-   PR2 pulls doors along a line instead of an arc, the estimated model
    is prismatic (in the console output), or the estimated model is a
    line in RVIZ.
-   decrease the sigma_position and/or sigma_orientation.
-   PR2 looses grip on the handle and does not seem to notice.
-   Set min_finger_distance to a suitable value, maybe 0.01 m.
