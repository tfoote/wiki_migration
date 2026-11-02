

```wiki
'''Note:''' You can also check a detailed integration tutorial on [[https://www.leorover.tech/integrations/follow-artag|LeoRover Tech - Follow ARTag|target="_blank"]]
```



## Overview

This package contains a ROS node which enables the
[Leo Rover](Robots/Leo Rover) to follow a printed ARTag.

It is one of a couple of packages made for showing an example usage of a
stock [Leo Rover](Robots/Leo Rover).

## Usage

To run the follower simply type: 

```
roslaunch leo_example_follow_ar_tag follow_ar_tag.launch
```



It will use the base configuration from the yaml files. You can run the
node with your configuration by changing the parameters (described in
[ROS API](http://wiki.ros.org/leo_example_follow_ar_tag#rosapi) section)

## ROS API

<a id="rosapi"></a>

### follow_ar_tag

#### Subscribed Topics

- `ar_pose_marker`
  ([ar_track_alvar_msgs/msg/AlvarMarkers](https://docs.ros.org/en/rolling/p/ar_track_alvar_msgs/msg/AlvarMarkers.html)):
  The detected markers
- `wheel_odom_with_covariance`
  ([nav_msgs/msg/Odometry](https://docs.ros.org/en/rolling/p/nav_msgs/msg/Odometry.html)):
  The wheel odometry used for interpolating the position between marker
  detections.

#### Published Topics

- `cmd_vel`
  ([geometry_msgs/msg/Twist](https://docs.ros.org/en/rolling/p/geometry_msgs/msg/Twist.html)):
  The velocity commands that should follow the marker.

#### Parameters

- `follow_id` (`int`, default: `0`): The ID of the marker to follow.
- `marker_timeout` (`float`, default: `0.5`): The timeout after which
  the rover will stop moving when it loses track of the marker.
- `min_ang_vel` (`float`, default: `0.1`): The minimum angular velocity
  of the rover.
- `max_ang_vel` (`float`, default: `1.0`): The maximum angular velocity
  of the rover.
- `angle_min` (`float`, default: `0.1`): The minimum angle between the
  rover and the marker, for which the rover will start rotating (with
  the min_ang_vel velocity).
- `angle_max` (`float`, default: `0.7`): The marker angle for which the
  maximum angular velocity is applied. For angles between angle_min and
  angle_max the applied velocity linearly increases from min_ang_vel to
  max_ang_vel.
- `min_lin_vel_forward` (`float`, default: `0.1`): The minimum linear
  velocity of the rover when driving forward.
- `max_lin_vel_forward` (`float`, default: `0.4`): The maximum linear
  velocity of the rover when driving forward.
- `distance_min_forward` (`float`, default: `0.7`): The minimum distance
  to the marker from the rover, for which the rover will start moving
  forward (with the min_lin_vel_forward).
- `distance_max_forward` (`float`, default: `1.2`): The distance to the
  marker for which the maximum linear velocity is applied. For distances
  between distance_min_forward and distance_max_forward the applied
  velocity linearly increases from min_lin_vel_forward to
  max_lin_vel_forward.
- `min_lin_vel_reverse` (`float`, default: `0.1`): The minimum linear
  velocity of the rover when going backward.
- `max_lin_vel_reverse` (`float`, default: `0.2`): The maximum linear
  velocity of the rover when going backward.
- `distance_max_reverse` (`float`, default: `0.5`): The distance to the
  marker below which the rover will start moving backward (with the
  min_lin_vel_reverse velocity).
- `distance_min_reverse` (`float`, default: `0.4`): The distance to the
  marker for which the maximum linear velocity is applied. For distances
  between distance_max_reverse and distance_min_reverse the applied
  velocity linearly increases from min_lin_vel_reverse to
  max_lin_vel_reverse.
