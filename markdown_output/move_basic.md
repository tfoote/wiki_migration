## Nodes

This package provides the `move_basic` ROS Node a very basic
navigation node.

### move_basic

The `move_basic` node performs basic navigation tasks. Path planning
consists of rotating in place to face the goal and then driving straight
towards it. It is designed to provide the same software interfaces as
[move_base](move_base), that is, it implements a `QueuedActionServer`
(similar to `SimpleActionServer`, see
[ actionlib documentation](actionlib )), that queues up to two goals
containing `geometry_msgs/PoseStamped` messages.

It is assumed that we are dealing with imperfect localization data:
`map`->`base_link` is accurate but may be delayed and is at a slow
rate and `odom`->`base_link` is more frequent, but drifts,
particularly after rotating. To counter these issues, `move_basic`
plans in the `map` frame, and waits a short time after each step, and
executes movement in the `odom` frame. If goals in the `base_link`
frame are received, they are interpreted as relative to the robot's
current position. This behavior is different to that of `move_base`,
which will not accept goals in the `base_link` frame.

#### Collision Avoidance

If data from a laser scanner or sonars is available, collision avoidance
can be performed. If an obstacle is detected, it will slow or stop in an
attempt to avoid a collision.

#### Visualization

Some of the data produced by `move_basic` can be visualized with
[ rviz](rviz ). In the screen shot below, the portion of the laser scan
data (in white) which is currently in the path of the robot is depicted
as a red line. The light purple line shows the path planned by the
robot. A navigation goal can be sent to `move_basic` by `rviz` by
pressing the `2D nav goal` button and clicking on the map.

![\|width="350px"](attachment:move_basic.png)

During rotation, the footprint of the robot is shown as a blue
rectangle. The red box, if shown shows the rotation that can be
performed without collision. If no obstacles are detected that obstruct
a rotation, the red box is not shown.

![\|width="150px"](attachment:rotation.png)

```clearsilver
sub {
  0.name= /move_base/goal
  0.type= move_base_msgs/MoveBaseActionGoal
  0.desc= A goal for `move_basic` to pursue in the world via the actionlib interface.
  1.name= /move_base/cancel
  1.type= actionlib_msgs/GoalID
  1.desc= A request to cancel a specific goal.
  2.name= /move_base_simple/goal
  2.type= geometry_msgs/PoseStamped
  2.desc= A goal for `move_basic` to pursue via the simple interface.
  3.name= /scan
  3.type= sensor_msgs/LaserScan
  3.desc= Laser scanner data for obstacle detection.
  4.name= /sonars
  4.type= sensor_msgs/Range
  4.desc= Sonar data for obstacle detection
  5.name= /tf
  5.type= tf2_msgs/TFMessage
  5.desc= The `tf` between `map` and `base_link` is used for planning if it is available.  Otherwise, the `tf` between `odom` and `base_link` is used. The `tf` between `odom` and `base_link` is always used for execution. If laser scan data is available, it is assumed to be in the `laser` frame. Hence, the `tf` between `base_link` and `laser` must be published.  If sonar sensors are available, their frame is determined from the messages they publish.
}

pub {
  0.name= /move_base/feedback
  0.type= move_base_msgs/MoveBaseActionFeedback
  0.desc= Feedback contains the current position of the base in the world.
  1.name= /move_base/status
  1.type= actionlib_msgs/GoalStatusArray
  1.desc= Provides status information on the goals that are sent to the `move_base` action.
  2.name= /move_base/result
  2.type= move_base_msgs/MoveBaseActionResult
  2.desc= Result is empty for the `move_base` action.
  3.name= /cmd_vel
  3.type=geometry_msgs/Twist 
  3.desc= Velocity commands meant for execution by a mobile base. 
  4.name= /plan
  4.type= nav_msgs/Path
  4.desc= A visualization of the planned path (this is a straight line).
  5.name= /obstacle_distance
  5.type= std_msgs/Float32
  5.desc= Distance to the nearest obstacle in the forward direction, in meters.
  6.name= /obstacle_viz
  6.type= visualization_msgs/Marker
  6.desc= A visualization of detected obstacles.
  7.name= /lateral_error
  7.type= geometry_msgs/Vector3
  7.desc= Lateral error to planned straight line to the goal.
}
srv{
  0.name= ~stop
  0.type= std_msgs/Bool
  0.desc= Allows a user to stop the robot, without cancelling the goal.
}
param {
  0.name= ~min_turning_velocity
  0.type= double
  0.desc= The minimum turning velocity for rotation on spot in radians/sec.
  0.default= 0.18
  1.name= ~max_turning_velocity
  1.type= double
  1.desc= The maximum turning velocity for rotation on spot in radians/sec.
  1.default= 1.0
  2.name= ~max_lateral_velocity
  2.type= double
  2.desc= The maximum lateral speed during linear movement in radians/sec.
  2.default= 0.5
  3.name= ~turning_acceleration
  3.type= double
  3.desc= The rate to ramp between `min_angular_velocity` and `max_angular_velocity` when starting and stopping rotation.
  3.default= 0.3
  4.name= ~max_linear_velocity
  4.type= double
  4.desc= The maximum speed for linear movement in meters/sec.
  4.default= 0.5
  5.name= ~linear_acceleration
  5.type= double
  5.desc= The rate to ramp between `min_linear_velocity` and `max_linear_velocity` when starting and stopping linear movement.
  5.default= 0.1
  6.name= ~angular_tolerance
  6.type= double
  6.desc= The maximum angular error that will be deemed successful.
  6.default=0.01
  7.name= ~linear_tolerance
  7.type= double
  7.desc= The maximum linear error that will be deemed successful.
  7.default=0.1
  8.name= ~localization_latency
  8.type= double
  8.desc= How long (in seconds) to pause between each movement step to ensure localization is accurate.
  8.default=0.5
  9.name=~lateral_kp
  9.type=double
  9.desc= Proportional lateral gain during linear movement
  9.default=2.0
 10.name=~lateral_ki
 10.type=double
 10.desc= Integral lateral gain during linear movement
 10.default=0.0
 11.name=~lateral_kd
 11.type=double
 11.desc= Differential lateral gain during linear movement
 11.default=20.0
 12.name=~velocity_threshold
 12.type=double
 12.desc= The minimum linear velocity close to goal that will be deemed successful.
 12.default=0.01
 13.name= ~linear_gain
 13.type= double
 13.desc= Adds a gain to the linear velocity
 13.default=1.0
 14.name= ~rotational_gain
 14.type= double
 14.desc= Adds a gain to the angular velocity
 14.default=2.5
 15.name= ~abort_timeout
 15.type= double
 15.desc= Duration robot can drive away from goal before abortion in seconds
 15.default=5.0
 16.name= ~obstacle_wait_threshold
 16.type=double
 16.desc= How long to pause for a detected obstacle before deciding it is not transient, in seconds.
 16.default=10.0
 17.name= ~forward_obstacle_threshold
 17.type=double
 17.desc=Minimum distance to obstacle before stopping in meters.
 17.default=1.0
 18.name= ~reverse_without_turning_threshold
 18.type=double
 18.default=0.5
 18.desc=An upper threshold in meters for moving backwards without turning to face the goal.
 19.name= ~map_frame
 19.type=string
 19.default=map
 19.desc=Name of the global frame.
 20.name=~robot_width
 20.type=double
 20.desc= Distance from `base_link` to the side of the robot, ie half the width.
 20.default=0.35
 21.name=~robot_front_length
 21.type=double
 21.desc= Distance from `base_link` the front-most part of the robot.
 21.default=0.11
 22.name=~robot_back_length
 22.type=double
 22.desc= Distance from `base_link` the rear-most part of the robot.
 22.default=0.21
}
```

#### Installation

```
sudo apt install ros-kinetic-move-basic
```

#### Example

To move forward one meter using [ rostopic ]( rostopic ) (note that
[ bash ]( https://www.gnu.org/software/bash/ ) completion will provide
an empty message that can be filled out):

```
rostopic pub /move_base_simple/goal geometry_msgs/PoseStamped "header:
  seq: 0
  stamp:
    secs: 0
    nsecs: 0
  frame_id: 'base_link'
pose:
  position:
    x: 1.0
    y: 0.0
    z: 0.0
  orientation:
    x: 0.0
    y: 0.0
    z: 0.0
    w: 1.0"
```

This is an example of a relative goal, since the `frame_id` is set to
`base_link`. The position of the target pose is set to 1 meter in the
forward direction, and the orientation is the identity quaternion.
