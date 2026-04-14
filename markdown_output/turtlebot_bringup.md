## TurtleBot Bringup

Follow the
[bringup tutorial](turtlebot_bringup/Tutorials/TurtleBot Bringup) to
start your !TurtleBot.

## Launch Files

-   \'\'\'minimal.launch\'\'\' - The base launch file for !TurtleBot.
    Starts the basic nodes ([kobuki_node](kobuki_node) or
    [create_node](create_node)),
    [laptop_battery_monitor](http://www.ros.org/wiki/turtlebot_node#laptop_battery_monitor),
    [robot_state_publisher](robot_state_publisher),
    [diagnostic_aggregator](diagnostic_aggregator), and
    [robot_pose_ekf](robot_pose_ekf). Includes app_manager.launch.

```{=html}
<!-- -->
```
-   \'\'\'app_manager.launch\'\'\' - Starts the !TurtleBot app managers
    and loads the !TurtleBot app list.
