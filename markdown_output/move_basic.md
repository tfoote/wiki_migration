## Nodes

This package provides the `move_basic` ROS Node a very basic
navigation node.

### move_basic

The `move_basic` node performs basic navigation tasks. Path planning
consists of rotating in place to face the goal and then driving straight
towards it. It is designed to provide the same software interfaces as
[move_base](https://index.ros.org/p/move_base), that is, it implements a
`QueuedActionServer` (similar to `SimpleActionServer`, see
[actionlib documentation](https://index.ros.org/p/actionlib)), that
queues up to two goals containing `geometry_msgs/PoseStamped`
messages.

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
[rviz](https://index.ros.org/p/rviz). In the screen shot below, the
portion of the laser scan data (in white) which is currently in the path
of the robot is depicted as a red line. The light purple line shows the
path planned by the robot. A navigation goal can be sent to
`move_basic` by `rviz` by pressing the `2D nav goal` button and
clicking on the map.

![width="350px"](doc/move_basic.png)

During rotation, the footprint of the robot is shown as a blue
rectangle. The red box, if shown shows the rotation that can be
performed without collision. If no obstacles are detected that obstruct
a rotation, the red box is not shown.

![width="150px"](doc/rotation.png)

#### Subscribed Topics

- `/move_base/goal`
  ([move_base_msgs/msg/MoveBaseActionGoal](https://docs.ros.org/en/rolling/p/move_base_msgs/msg/MoveBaseActionGoal.html)):
  A goal for `move_basic` to pursue in the world via the actionlib
  interface.
- `/move_base/cancel`
  ([actionlib_msgs/msg/GoalID](https://docs.ros.org/en/rolling/p/actionlib_msgs/msg/GoalID.html)):
  A request to cancel a specific goal.
- `/move_base_simple/goal`
  ([geometry_msgs/msg/PoseStamped](https://docs.ros.org/en/rolling/p/geometry_msgs/msg/PoseStamped.html)):
  A goal for `move_basic` to pursue via the simple interface.
- `/scan`
  ([sensor_msgs/msg/LaserScan](https://docs.ros.org/en/rolling/p/sensor_msgs/msg/LaserScan.html)):
  Laser scanner data for obstacle detection.
- `/sonars`
  ([sensor_msgs/msg/Range](https://docs.ros.org/en/rolling/p/sensor_msgs/msg/Range.html)):
  Sonar data for obstacle detection
- `/tf`
  ([tf2_msgs/msg/TFMessage](https://docs.ros.org/en/rolling/p/tf2_msgs/msg/TFMessage.html)):
  The `tf` between `map` and `base_link` is used for planning if
  it is available. Otherwise, the `tf` between `odom` and
  `base_link` is used. The `tf` between `odom` and `base_link`
  is always used for execution. If laser scan data is available, it is
  assumed to be in the `laser` frame. Hence, the `tf` between
  `base_link` and `laser` must be published. If sonar sensors are
  available, their frame is determined from the messages they publish.

#### Published Topics

- `/move_base/feedback`
  ([move_base_msgs/msg/MoveBaseActionFeedback](https://docs.ros.org/en/rolling/p/move_base_msgs/msg/MoveBaseActionFeedback.html)):
  Feedback contains the current position of the base in the world.
- `/move_base/status`
  ([actionlib_msgs/msg/GoalStatusArray](https://docs.ros.org/en/rolling/p/actionlib_msgs/msg/GoalStatusArray.html)):
  Provides status information on the goals that are sent to the
  `move_base` action.
- `/move_base/result`
  ([move_base_msgs/msg/MoveBaseActionResult](https://docs.ros.org/en/rolling/p/move_base_msgs/msg/MoveBaseActionResult.html)):
  Result is empty for the `move_base` action.
- `/cmd_vel`
  ([geometry_msgs/msg/Twist](https://docs.ros.org/en/rolling/p/geometry_msgs/msg/Twist.html)):
  Velocity commands meant for execution by a mobile base.
- `/plan`
  ([nav_msgs/msg/Path](https://docs.ros.org/en/rolling/p/nav_msgs/msg/Path.html)):
  A visualization of the planned path (this is a straight line).
- `/obstacle_distance`
  ([std_msgs/msg/Float32](https://docs.ros.org/en/rolling/p/std_msgs/msg/Float32.html)):
  Distance to the nearest obstacle in the forward direction, in meters.
- `/obstacle_viz`
  ([visualization_msgs/msg/Marker](https://docs.ros.org/en/rolling/p/visualization_msgs/msg/Marker.html)):
  A visualization of detected obstacles.
- `/lateral_error`
  ([geometry_msgs/msg/Vector3](https://docs.ros.org/en/rolling/p/geometry_msgs/msg/Vector3.html)):
  Lateral error to planned straight line to the goal.

#### Services

- `~stop`
  ([std_msgs/srv/Bool](https://docs.ros.org/en/rolling/p/std_msgs/srv/Bool.html)):
  Allows a user to stop the robot, without cancelling the goal.

#### Parameters

- `~min_turning_velocity` (`double`, default: `0.18`): The minimum
  turning velocity for rotation on spot in radians/sec.
- `~max_turning_velocity` (`double`, default: `1.0`): The maximum
  turning velocity for rotation on spot in radians/sec.
- `~max_lateral_velocity` (`double`, default: `0.5`): The maximum
  lateral speed during linear movement in radians/sec.
- `~turning_acceleration` (`double`, default: `0.3`): The rate to ramp
  between `min_angular_velocity` and `max_angular_velocity` when
  starting and stopping rotation.
- `~max_linear_velocity` (`double`, default: `0.5`): The maximum speed
  for linear movement in meters/sec.
- `~linear_acceleration` (`double`, default: `0.1`): The rate to ramp
  between `min_linear_velocity` and `max_linear_velocity` when
  starting and stopping linear movement.
- `~angular_tolerance` (`double`, default: `0.01`): The maximum angular
  error that will be deemed successful.
- `~linear_tolerance` (`double`, default: `0.1`): The maximum linear
  error that will be deemed successful.
- `~localization_latency` (`double`, default: `0.5`): How long (in
  seconds) to pause between each movement step to ensure localization is
  accurate.
- `~lateral_kp` (`double`, default: `2.0`): Proportional lateral gain
  during linear movement
- `~lateral_ki` (`double`, default: `0.0`): Integral lateral gain during
  linear movement
- `~lateral_kd` (`double`, default: `20.0`): Differential lateral gain
  during linear movement
- `~velocity_threshold` (`double`, default: `0.01`): The minimum linear
  velocity close to goal that will be deemed successful.
- `~linear_gain` (`double`, default: `1.0`): Adds a gain to the linear
  velocity
- `~rotational_gain` (`double`, default: `2.5`): Adds a gain to the
  angular velocity
- `~abort_timeout` (`double`, default: `5.0`): Duration robot can drive
  away from goal before abortion in seconds
- `~obstacle_wait_threshold` (`double`, default: `10.0`): How long to
  pause for a detected obstacle before deciding it is not transient, in
  seconds.
- `~forward_obstacle_threshold` (`double`, default: `1.0`): Minimum
  distance to obstacle before stopping in meters.
- `~reverse_without_turning_threshold` (`double`, default: `0.5`): An
  upper threshold in meters for moving backwards without turning to face
  the goal.
- `~map_frame` (`string`, default: `map`): Name of the global frame.
- `~robot_width` (`double`, default: `0.35`): Distance from
  `base_link` to the side of the robot, ie half the width.
- `~robot_front_length` (`double`, default: `0.11`): Distance from
  `base_link` the front-most part of the robot.
- `~robot_back_length` (`double`, default: `0.21`): Distance from
  `base_link` the rear-most part of the robot.

#### Installation



```
sudo apt install ros-kinetic-move-basic
```



#### Example

To move forward one meter using
[rostopic](https://index.ros.org/p/rostopic) (note that
[bash](https://www.gnu.org/software/bash/) completion will provide an
empty message that can be filled out):



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
