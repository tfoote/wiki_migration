## Overview

`multi_jackal_base` provides a launch file for spawning all components
of a simulated [Clearpath Jackal](http://wiki.ros.org/Robots/Jackal). It
has been extended from the single robot
[jackal_base](http://wiki.ros.org/jackal_base) to separate the robots
into unique namespaces, allowing multiple robots to be simulated at the
same time.

## Tutorials

There are tutorials on how to use this package in
[multi_jackal_tutorials](http://wiki.ros.org/multi_jackal_tutorials).

## Arguments

A number of arguments can be provided when launching
`jackal_base.launch`. 1. `ns` (string) \-- The namespace of the
robot. All nodes/topics/frames will be prefixed with this. 2. `x`
(double) \-- The starting x position of the robot in Gazebo (m). 3.
`y` (double) \-- The starting y position of the robot in Gazebo (m).
4. `z` (double) \-- The starting z position of the robot in Gazebo
(m). 5. `roll` (double) \-- The starting roll orientation of the robot
in Gazebo (rad). 6. `pitch` (double) \-- The starting pitch
orientation of the robot in Gazebo (rad). 7. `yaw` (double) \-- The
starting yaw orientation of the robot in Gazebo (rad). 8. `config`
(string) \-- The configuration file to load in
[multi_jackal_description/urdf/configs](https://github.com/NicksSimulationsROS/multi_jackal/tree/ros-kinetic/multi_jackal_description/urdf/configs).
9. `config_id` (int) \-- The configuration ID for use in the
configuration file. 10. `use_move_base` (bool) \-- Whether to load
[move_base](http://wiki.ros.org/move_base) to navigate to goals. 11.
`use_global_tf` (bool) \-- Whether to provide a static transform from
`map` to `ns/odom`. 12. `use_global_ekf` (bool) \-- Whether to use
the GPS to provide `map` to `ns/odom`.

If you only want to use local odometry for positioning, set
`use_global_tf` to `true` and `use_global_ekf` to `false`. If
you want to use the Jackals GPS, set `use_global_ekf` to `true`, and
`use_global_tf` to `false`. If you want to use your own fusion, set
them both to `false`.
