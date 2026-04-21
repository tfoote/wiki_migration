## Overview

This package provides an application that allows a PR2 robot to navigate
autonomously through a previously mapped environment.

## Prerequisites

The pr2_2dnav application requires some prerequisite steps in order to
run.

### Bring up the Robot

As with all PR2 applications, you must
[ bring up your robot](pr2_apps#bringup ).

### Provide a Map

This application assumes that a map is provided. Please see
documentation on the [map_server](map_server) for information on
providing a map over ROS.

### Tuck the Arms

Tuck the arms of the PR2 using the
[ pr2_tuckarm application](pr2_tuckarm ).

## Running the Application

The [pr2_2dnav](pr2_2dnav) application can be run with the following
command:



```
roslaunch pr2_2dnav pr2_2dnav.launch
```



## Interacting with the Application

The [navigation](navigation) stack that is the heart of the pr2_2dnav
application can be commanded via [rviz](rviz), [nav_view](nav_view), or
through code.

### rviz

-   You can bring up rviz in a pr2_2dnav friendly configuration by
    running the following launch file: 

```
roslaunch pr2_navigation_global rviz_move_base.launch
```


-   In the rviz window that pops up, you'll need to set the pose of the
    robot.
-   Take note of where the robot is in the world.
-   Right click and drag to zoom on the map.
-   Click the "2D Pose Estimate" button in the rviz GUI window.
-   Left click on the map at the location of the robot and drag to set
    orientation.
-   Verify that the scans from the base laser of the robot match up
    fairly well with the map of the environment.

```{=html}
<!-- -->
```
-   The application is now up and ready to receive goals.
-   Click the "2D Nav Goal" button in the rviz GUI window.
-   Left click on the map at the location of the goal and drag to set
    orientation.
-   If the robot is surrounded by obstacles, it may not move. Move
    obstacles or set a new goal to try again.

```{=html}
<!-- -->
```
-   [ Navigation and rviz tutorial](navigation/Tutorials/Using rviz with the Navigation Stack ):
    Provides additional information on using [rviz](rviz) with the
    [navigation](navigation) stack.

### nav_view

-   You can bring up nav_view in a pr2_2dnav friendly configuration by
    running the following launch file 

```
roslaunch pr2_navigation_global nav_view_move_base.launch
```


-   In the nav_view window that pops up, you'll need to set the pose of
    the robot.
-   Take note of where the robot is in the world.
-   Right click and drag to zoom on the map.
-   Click the "Set Pose" button in the nav_view GUI window.
-   Left click on the map at the location of the robot and drag to set
    orientation.
-   Verify that the scans from the base laser of the robot match up
    fairly well with the map of the environment.

```{=html}
<!-- -->
```
-   The application is now up and ready to receive goals.
-   Click the "Set Goal" button in the nav_view GUI window.
-   Left click on the map at the location of the goal and drag to set
    orientation.
-   If the robot is surrounded by obstacles, it may not move. Move
    obstacles or set a new goal to try again.

### Through Code

-   A tutorial on sending goals to the [navigation](navigation) stack
    with code can be found
    [ here](navigation/Tutorials/SendingSimpleGoals ).
