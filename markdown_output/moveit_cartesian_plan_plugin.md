## Overview

[Youtube](https://www.youtube.com/watch?v=jQc3z7FQwHw)

## How to try

### Compile

You can download the plugin from the following
[github repository](https://github.com/ros-industrial-consortium/fermi/tree/hydro-devel).
After getting it from the reposotory you need to run the following
commands:

```
$ catkin_make
$ source devel/setup.bash
```

### Run for the first Time

Once the build is successful and the new setup.\*sh file is sourced, you
can load a robot configured for MoveIt, for example:

```
$ roslaunch fermi_sia20d_moveit_config moveit_planning_execution.launch
```

#### Setting up the RViz Environment

It is essential to set up the RViz enviroment and include all the
necessary visuals in order to use the plugin. To set up the RViz
enviroment you need to add the following visuals and the plugin:

1\. On the displays menu go to Add->InteractiveMarkers.

2\. To add the Plugin Widget go to: Panels->Add New Panel-> Cartesian
Path Planner MoveIt Plugin.

3\. In Displays go to InteractiveMarkers and set the Update Topic to:
/moveit_cartesian_planner/update

Once this is completed you should see the Red Interaction Marker aligned
with the end-effector of the loaded robot.

To get better animation of the Cartesian Path it is recommended to
remove the MotionPlanning visual from the RViz and add the RobotModel
visual. If you plan to use this plugin more frequently it is recommended
also to save the RViz scene so you do not have to go to adding all the
necessary components every time you run certain robot. Some already
pre-configured robots are available on the
[github repository](https://github.com/ros-industrial-consortium/fermi/tree/hydro-devel).

## How to Use

### Make Plan

The TreeView gives overview of all the Way-Points added by the user.
Furthermore, by expanding the TreeView the user can change the current
pose of a Way-Point. ![](attachment:make_plan_menu.png)

### Way-Point Colors

The colour of the Way-Point lets the user know if that certain Way-Point
is in the Inverse Kinematics Solution for the Robot. The color of the
Way-Points are updated on the fly, when the user changes their pose
during interaction.

![](attachment:different_markers.png)

### Way-Point Menu

Each Way-Point has a Menu where the user can either delete the selected
Way-Point or enable the 6DOF Pose Control for the Way-Point.

![](attachment:way_point_menu.png)

### Cartesian Path

The user can set the MoveIt and Cartesian Path parameters before
Execution of the Cartesian Path from the Way-Points.

![](attachment:cartesian_planner_parameters.png)

## Further Examples

The repository contains further examples that demonstrate Cartesian path
planning capability. These can be ran with the following:
```
roslaunch fermi_blending_cell_moveit_config moveit_planning_execution.launch
``` ```
roslaunch fermi_sia20d_moveit_config moveit_planning_execution.launch
```
```
roslaunch fermi_irb2400_moveit_config moveit_planning_execution.launch
```
