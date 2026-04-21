This package contains nodes for calibrating the proximity sensor on the
arms of the PR2 robot. The code in that package is for the right arm,
but it can be easily adapted for the left arm.

Calibrating the proximity sensor can be splitted up into two tasks.

1\. Scanning the arm 1. Arranging the patches on the arm, based on the
scan data

## Scanning the arm

The goal of the calibration is to determine position and orientation of
each patch. The patches are treated as circles so the angle of their
orientation around a vector is not important. This means it is
sufficient to find out a XYZ vector for the position and another XYZ
vector for the orientation.

It is not feasible to enter these values by hand relative to the
robot\'s coordinate frame. For this problem the fact that the robot
knows the position of it\'s grippers is used. The scan node provides a
functionality to scan the right arm with a metal stick that has been put
into the gripper of the left arm. Before you start the scan node you
FIRST have to put this metal stick into the robot\'s left gripper. This
can be done with the pr2 teleop:

```
roslaunch pr2_teleop teleop_joystick.launch
``` Then open the gripper, place the metal stick in
between and close it again. A length of about 6 cm is sufficient.

Now you can CTRL+C the teleop again. After that you have to start the
arm planning environment for the scan method.

```
roslaunch pr2_calib_proximity_sensor both_arm_navigation.launch
``` If you did not configure your scan method yet,
you should do it now. Let\'s take a look into the *conf/scan.yaml*

Forearm and upper arm are scanned one after the other. So there is one
configuration for each.

dbl_stick_offset: 0.265 * The offset in m from r_wrist_roll_link to the
end of the metal stick forearm:*

. dbl_start_dist: 0.05 * The start distance of each point measured from
the robot\'s surface . dbl_end_dist: 0.005 * The end distance of each
point measured from the robot\'s surface . dbl_step_dist: 0.02 * The
step in which the robot goes from dbl_start_dist to dbl_end_dist .
dbl_start_angle: -3.1 * The start turning angle of the forearm .
dbl_end_angle: 3.1 * The end turning angle of the forearm .
dbl_step_angle: 0.15 * The step the robot goes from dbl_start_angle to
dbl_end_angle . dbl_start_x: 0.11 * The start value of the x value along
the rotation axis of the forearm . dbl_end_x: 0.35 * The end value of
the x value along the rotation axis of the forearm . dbl_step_x: 0.02 *
The step in which the robot goes from dbl_start_x to dbl_end_x*

upper_arm: * The variables after that have the same meaning as in the
section forearm but for the upperarm*

. dbl_start_dist: 0.045 . dbl_end_dist: 0.005 . dbl_step_dist: 0.0175 .
dbl_start_angle: -3.1 . dbl_end_angle: 0.0 . dbl_step_angle: 0.15 .
dbl_start_x: 0.14 . dbl_end_x: 0.49 . dbl_step_x: 0.02

The forearm has only one scan position since the forearm_roll_joint does
not have any joint limits. The upper arm needs two scan positions
because the upper_arm_roll joint is not continous. This is why the
start_angle is by default -3.1 and goes to 0.0 Because the upperarm gets
scanned once from above and once from underneath the whole arm is
surrounded. You can leave the standard configuration which should do a
good job, but you can also change it.

When you\'re ready you can launch the scan procedure with

```
roslaunch pr2_calib_proximity_sensor scan.launch
``` This will take a few hours\...

Don\'t mind if the scan cannot reach every measurement position, this is
normal behaviour and no problem.

## Arranging the patches

After the scan finished you can arrange the proximity sensor patches
based on the measurements of the scan. This is done with

```
roslaunch pr2_calib_proximity_sensor arrange_patches.launch
``` This will produce an output file for the
patches_tf node in [proximity_sensor_tf](proximity_sensor_tf) When the
scan method could not find any reasonable measure point for a patch, you
will get a warning and the patch is placed far away relative to
torso_lift_link, for that the tf node can run, either if there is no
calibration for each single patch.

## Visualize data

You might want to see the data that the scan method saved after it
completed. First run rviz.

```
rosrun rviz rviz
``` Now you can visualize the data for patch *n* by
running

```
roslaunch pr2_calib_proximity_sensor visualize_data.launch patch_id:=n
```
