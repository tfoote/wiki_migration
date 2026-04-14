## Description

For mobile manipulators, this package calculates a robot base location
where the end-effector (EE) can reach a desired pose (a.k.a. inverse
reachability). The method is computationally fast (since it depends on a
MoveIt Cartesian motion plan), simple (300 lines), and easy to use
(requiring just a service to provide the desired pose).

Below, the first image shows a mobile manipulator which is too far to
grasp the object of interest. The desired EE pose is shown in green. The
second image shows the freshly-calculated base position (red cube) which
will allow the robot to reach that pose. \<\<Please ignore the bad
camera calibration\>\>

![alt text\|width=700](attachment:1.png)

![alt text\|width=400](attachment:2.png)

This package uses \'\'move_base\'\' for base commands and
\'\'MoveIt!\'\' for manipulator motion planning.

## Installing the package

```
$ sudo apt-get install ros-indigo-move-base-to-manip
```

## Run the demo

```
$ rosrun move_base_to_manip provide_target
```

\^This launches a ROS service that will make a desired pose available to
the move_base_to_manip node. It also displays this desired pose in Rviz.
When the client sends \'\'true\'\' on the service request, this node
will shut down after providing the pose.

```
$ roslaunch move_base_to_manip move_base_to_manip.launch
```

\^This node requests the desired pose from the other node. It then moves
the end-effector to the desired height and orientation. From there, it
plans a Cartesian move to the desired pose. The % completion of the
Cartesian move informs the base on how far it must move. If the
Cartesian move is able to complete 100%, the arm moves and the program
exits. Otherwise, there is a call to \'\'move_base\'\' to get closer to
the object:

```
ac.sendGoal(goal);
```

At this point, your robot base should move.

## Parameters

The planner reads optional parameters on the
[ ROS parameter server]( http://wiki.ros.org/Parameter%20Server ). They
can be adjusted from the command line, programmatically, or left as
their default values. They are:

-   \'\'/move_base_to_manip/motion_buffer\'\': A fraction between 0
    and 1. A value of 1 means the EE will barely be able to reach the
    desired pose when fully extended. A value of 0 means the base motion
    will bring the EE to the desired pose without additional arm motion.
    Default: 0.15.

```{=html}
<!-- -->
```
-   \'\'/move_base_to_manip/move_cartesian\'\': Use a Cartesian motion
    for the final arm approach, or a regular MoveIt motion? The
    Cartesian motion may be useful if your task requires the gripper to
    maintain a constant orientation (like grasping often does). Default:
    false, i.e. do a regular motion.

```{=html}
<!-- -->
```
-   \'\'/move_base_to_manip/clear_octomap\'\': Clear the octomap
    collision scene before the final arm approach? This is often
    necessary for grasping \-- otherwise sensor noise/resolution may
    lead the robot to expect a collision. Default: true, i.e. the
    collision scene will be cleared.

```{=html}
<!-- -->
```
-   \'\'/move_base_to_manip/clear_costmaps\'\': Clear the move_base
    costmaps before base motion? Default: true.

```{=html}
<!-- -->
```
-   \'\'/move_base_to_manip/prompt_before_motion\'\': Ask the user
    before making any motion? This is useful if you\'re just starting to
    use the package and aren\'t sure what to expect. Default: true.

```{=html}
<!-- -->
```
-   \'\'/move_base_to_manip/shutdown\'\': This is the \"request\" part
    of the service call. Can be used as a signal that the server can
    shutdown. Default: true (which I use to signal the pose provider
    node to shut down).

```{=html}
<!-- -->
```
-   \'\'/move_base_to_manip/cartesian_plan_res\'\': A smaller number
    results in a more accurate prediction of the distance to the pose of
    interest. Default: 0.005m

```{=html}
<!-- -->
```
-   \'\'/move_base_to_manip/move_group_name\'\': Default \"right_ur5\"

```{=html}
<!-- -->
```
-   \'\'/move_base_to_manip/move_group_planner\'\': Default
    \"RRTConnectkConfigDefault\"

```{=html}
<!-- -->
```
-   \'\'/move_base_to_manip/velocity_scale\'\': % of maximum robot speed
    for all arm motions. Default: 0.1

```{=html}
<!-- -->
```
-   \'\'/move_base_to_manip/base_frame_name\'\': Default \"base_link\"

```{=html}
<!-- -->
```
-   \'\'/move_base_to_manip/position_tolerance\'\': Position tolerance
    for arm motions. It may be useful to bump this up if you are having
    trouble finding plans. Default: 0.01 m

```{=html}
<!-- -->
```
-   \'\'/move_base_to_manip/orientation_tolerance\'\': Orientation
    tolerance for arm motions. Default: 0.0001 rad

```{=html}
<!-- -->
```
-   \'\'/move_base_to_manip/ok_to_flip\'\': If true, the planner will
    try to flip the EE +/-180 deg about Z (i.e. \'\'yaw\'\') when it
    cannot reach a desired pose. Then it will attempt to plan again.
    Useful for 2-finger grippers. Default: true

## Tuning move_base

Here are some hints to get more suitable trajectories from
\'\'move_base\'\':

-   Make sure the resolutions of your costmap and \'\'move_base\'\'
    planners are fine enough to get the accuracy you require.

```{=html}
<!-- -->
```
-   If you see excessive spinning, make sure oscillation_timeout is set
    to a nonzero value..

```{=html}
<!-- -->
```
-   Remember, there are two controllers to tune: local and global.

```{=html}
<!-- -->
```
-   Make sure the inflation_radius is the same for both local and global
    planners.

Here are
[ more hints]( http://wiki.ros.org/navigation/Tutorials/Navigation%20Tuning%20Guide )
from the creator of \'\'move_base\'\'.

## Limitations

This package only calculates one base position which can reach the
desired pose. If the base is not able to move there, it fails. However,
\'\'move_base\'\' has some built-in obstacle avoidance capabilities and
if it fails, it will generally be close to the goal.

## See Also

Some potential ROS alternatives for mobile manipulation planning:

-   (untested) Use the [ Reuleaux]( http://wiki.ros.org/reuleaux )
    package to calculate a good location for the manipulator\'s base.
    From the manipulator\'s position, calculate a mobile base location.
    This is the \"inverse reachability database\" approach.

```{=html}
<!-- -->
```
-   (untested) It might be possible to model a robot base as 3 joints of
    a manipulator (x,y,theta) and add it to the kinematic model of the
    robot. Then an inverse kinematics solver could be used to plan the
    base and arm motion all at once.

```{=html}
<!-- -->
```
-   (outdated) DARRT - seems more feature-rich but also more
    computationally intensive.
