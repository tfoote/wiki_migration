## Overview

The `tedusar_daf_path_follower` is a simple but efficient path
follower for skid-steered/differential drive mobile robots as part of
`tedusar_ros_pkg`` `repository. To control path follower a
`tedusar_nav_msgs`` `package is needed which define control messages.

## Dynamic Arc Fitting Path Follower

The DAF Path Follower provide control commands (linear and rotational
velocity) based on given path designated to follow. Behaviour of the DAF
path follower can be adapted to your needs with given Parameters.

### ROS Parameters

\- `base_link (string):`

. Mobile robot base link , default `/base_footprint.`

\- `pub_cmd_hz (double):`

. Frequency of veloctiy commands publishing, default 10 Hz.

\- `path_topic (nav_msgs/Path):`

. ROS subscription topic name to path waypoints, default
`/exploration_path`

\- `pose_update_topic (nav_msgs/Odometry):`

. Subscription topic name to robot current position, default `/odom.`

\- `imu_data (sensor_msgs/Imu):`

. IMU information subscription topic name, default `/imu_data.`

\- `out_cmd_vel (geometry_msgs/Twist):`

. Velocity publisher topic name, default `/cmd_vel.`

\- `max_lin_vel (double):`

. Maximum linear velocity (m/s), default `0.4.`

\- `min_lin_vel (double):`

. Minimum linear velocity (m/s), default `0.1.`

\- `max_rot_vel (double):`

. Maximum rotational velocity (rad/s), default `0.8.`

\- `min_rot_vel (double):`

. Minimum rotational velocity (rad/s), default `0.4.`

\- `executin_period (double):`

. Execution period defines distance parameter lookahead (m) which is
second, distance is calculated execution_period\*max_lin_vel, default
`1.0.`

\- `global_goal_tolerance (double):`

. DAF path follower report goal reached if tolerance is reached (m),
default `0.1.`

\- `enable_angle_compensation (bool):`

. Allows DAF to compensate angle difference while moving, based on
following params, default `true.` - `lower_al_angle (double):` .
This parameter defines lower angle treshold which defines if
compensation (rad), default `/0.2.` - `upper_al_angle (double):` .
This parameter defines lower angle treshold which defines if
compensation (rad), default `/1.0.`

\- `enable_ground_compensation (bool):`

. Allows DAF to use IMU data and compensate angle of inclination while
execution velocity commands, default `true.`

\- `enable_velocity_compensation (bool):`

. Allows DAF to increase linear and rotational veloctiy if robot does
not reach on given velocity commands, default `true.`

\- `stability_angle (double):`

. This is an angle thresholf, when it is reached the DAF path follower
reponde with failure and warn that robot is inclined too much, default
`1.0.`

\- `show``_local_path_planning (bool):`

. It publish additional topics wich are display auxilary geometry
information, additional information are need, default `false``.` . -
`map``_link (string):` . Map link, for dispaying additonal
information , default `/map.`

## Launch File Examples

Start a `tedusar_path_follower` process with default parameter
setings.

```
$ roslaunch tedusar_daf_path_follower daf_path_follower_default.launch
```

## Other Documentation

Publication:
