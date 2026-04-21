## Description

This package provides several launch files for [rviz](rviz) to visualize
WheeledRobin.

## Use

### Visualizing the Robot

First launch the robot either in real or faked mode and start the Kinect
drivers (see Getting Started section in WheeledRobin).

Then run 

```
roslaunch wheeled_robin_rviz_launchers view_robot.launch
```

 and a new rviz window will open and
show the robot in fixed odom frame.

## Launch Files

-   view_robot.launch - fairly generic, preconfigured to show both robot
    and 3d views.
