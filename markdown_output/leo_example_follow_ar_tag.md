```wiki
'''Note:''' You can also check a detailed integration tutorial on [[https://www.leorover.tech/integrations/follow-artag|LeoRover Tech - Follow ARTag|target="_blank"]]
```

## Overview

This package contains a ROS node which enables the
[Leo Rover](Robots/Leo Rover) to follow a printed ARTag.

It is one of a couple of packages made for showing an example usage of a
stock [Leo Rover](Robots/Leo Rover).

## Usage

To run the follower simply type: ```
roslaunch leo_example_follow_ar_tag follow_ar_tag.launch
```

It will use the base configuration from the yaml files. You can run the
node with your configuration by changing the parameters (described in
[ROS API](http://wiki.ros.org/leo_example_follow_ar_tag#rosapi) section)

## ROS API

```clearsilver
name= follow_ar_tag
sub {
  group.0 {
    0.name= ar_pose_marker 
    0.type= ar_track_alvar_msgs/AlvarMarkers
    0.desc= The detected markers
    1.name= wheel_odom_with_covariance
    1.type= nav_msgs/Odometry
    1.desc= The wheel odometry used for interpolating the position between marker detections.
  }
}
pub {
  0.name= cmd_vel
  0.type= geometry_msgs/Twist
  0.desc= The velocity commands that should follow the marker.
}
param {
  group.0 {
    0.name= follow_id
    0.type= int
    0.default= 0
    0.desc= The ID of the marker to follow.
    1.name= marker_timeout
    1.type= float
    1.default= 0.5
    1.desc= The timeout after which the rover will stop moving when it loses track of the marker.
    2.name= min_ang_vel
    2.type= float
    2.default= 0.1
    2.desc= The minimum angular velocity of the rover.
    3.name= max_ang_vel
    3.type= float
    3.default= 1.0
    3.desc= The maximum angular velocity of the rover.
    4.name= angle_min
    4.type= float
    4.default= 0.1
    4.desc= The minimum angle between the rover and the marker, for which the rover will start rotating (with the min_ang_vel velocity).
    5.name= angle_max
    5.type= float
    5.default= 0.7
    5.desc= The marker angle for which the maximum angular velocity is applied. For angles between angle_min and angle_max the applied velocity linearly increases from min_ang_vel to max_ang_vel.
    6.name= min_lin_vel_forward
    6.type= float
    6.default= 0.1
    6.desc= The minimum linear velocity of the rover when driving forward.
    7.name= max_lin_vel_forward
    7.type= float
    7.default= 0.4
    7.desc= The maximum linear velocity of the rover when driving forward.
    8.name= distance_min_forward
    8.type= float
    8.default= 0.7
    8.desc= The minimum distance to the marker from the rover, for which the rover will start moving forward (with the min_lin_vel_forward).
    9.name= distance_max_forward
    9.type= float
    9.default= 1.2
    9.desc= The distance to the marker for which the maximum linear velocity is applied. For distances between distance_min_forward and distance_max_forward the applied velocity linearly increases from min_lin_vel_forward to max_lin_vel_forward.
    10.name= min_lin_vel_reverse
    10.type= float
    10.default= 0.1
    10.desc= The minimum linear velocity of the rover when going backward.
    11.name= max_lin_vel_reverse
    11.type= float
    11.default= 0.2
    11.desc= The maximum linear velocity of the rover when going backward.
    12.name= distance_max_reverse
    12.type= float
    12.default= 0.5
    12.desc= The distance to the marker below which the rover will start moving backward (with the min_lin_vel_reverse velocity).
    13.name= distance_min_reverse
    13.type= float
    13.default= 0.4
    13.desc= The distance to the marker for which the maximum linear velocity is applied. For distances between distance_max_reverse and distance_min_reverse the applied velocity linearly increases from min_lin_vel_reverse to max_lin_vel_reverse.
  }
}
```
