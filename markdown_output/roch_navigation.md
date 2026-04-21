  -- ---------------------------- -- -- -- -------------------------------- --
     [English](roch_navigation)            [简体中文](cn/roch_navigation)   
  -- ---------------------------- -- -- -- -------------------------------- --

## Tutorial

There have a simple tutorial for running
[roch_navigation](roch/Tutorials/Using package of roch_navigation).

roch_navigation reference to
[turtlebot_navigation](turtlebot_navigation), and both laser and camera
can using SLAM and [navigation](navigation).

## Launch Files

-   **gmapping_demo.launch** - The map building launch file for Roch.
    Starts the *sensor.launch* in [roch_bringup](roch_bringup),
    [map_server](map_server) and [gmapping](gmapping).
-   **amcl_demo.launch** - The navigation base on map launch file for
    Roch. Starts the **sensor.launch** in [roch_bringup](roch_bringup)
    and [move_base](move_base).
