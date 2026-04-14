## How to run

### Running Denso\'s VS060 in a simple world

First, if you run it for the first time, install prerequisite.

```
$ rosdep install vs060
$ ros-$YOUR_ROSDISTRO$-moveit-ros-visualization  (may not be necessary)
```

You can run [VS060](vs060) manipulator on [RViz](rviz) by the following:
```
$ roslaunch denso_launch denso_vs060_moveit_demo_simulation.launch
```

Then you can plan the arm\'s pose by using
[Interactive Markers](interactive_markers‎), then actually move it to
there by hitting \`Plan & Execute\` on [MoveIt!](moveit)\'s \`RViz\`
plugin.

![\|width=75%](attachment:vs060_rviz_launch_1.png)
![\|width=75%](attachment:vs060_rviz_launch_2.png)

You can simulate object avoidance too by placing objects in \`RViz\`.
Here for example with
[tabletop](https://github.com/isucan/plannerarena/blob/master/problems/pr2_scenes/tabletop.scene).

![\|width=75%](attachment:vs060_rviz_moveit_objectAvoidance.png)

Youtube example: [Youtube](https://www.youtube.com/watch?v=ytdnVw_QEoQ)

### VS060 in iREX 2013 demo

You can run it on \`RViz\` by: ```
$ roslaunch vs060_moveit_config demo_simulation_cage.launch
```

You\'ll see \`VS060\` sitting in a bit more restricted situation.
![\|width=75%](attachment:vs060_irex_rviz.png)

The actual robot is moving in the same but real environment:
[Youtube](https://www.youtube.com/watch?v=QPEfDgPtLrQ)

### VS060 integrated with vision (xtion)

[Youtube](https://www.youtube.com/watch?v=oVQiLIBRSHw)

### Using Web Operator

Using [rwt_moveit](rwt_moveit) (package work in progress
[here](https://github.com/tork-a/visualization_rwt/pull/45/files)) you
can operate this robot via \`WebGL\`-enabled web browsers.
![\|width=85%](attachment:denso/rwt_moveit_denso_1.png)
![\|width=75%](attachment:rwt_moveit_obstacle_1.png)

### Using Cartesian Path Planner Plug-In

[Cartesian Path Planner Plug-In from ROS-Industrial](http://rosindustrial.org/news/2014/9/5/cartesian-path-planner-plug-in-for-moveit).

[Youtube](https://www.youtube.com/watch?v=rk-kPaGUL1w)
