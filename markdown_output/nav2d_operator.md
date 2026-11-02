## Example

See the [Operator Tutorial](https://index.ros.org/p/nav2d) for an
example how to setup the Operator in Stage and use a Joystick to
simulate commands from a higher level node.

## ROS Interface

### operator

The `operator` takes motion commands from a path planner and outputs
control commands to the robot hardware avoiding obstacles in front of
the robot.

#### Subscribed Topics

- `scan`
  ([sensor_msgs/msg/LaserScan](https://docs.ros.org/en/rolling/p/sensor_msgs/msg/LaserScan.html)):
  Laser scans to update local costmap.
- `tf`
  ([tf/msg/tfMessage](https://docs.ros.org/en/rolling/p/tf/msg/tfMessage.html)):
  Transforms.
- `cmd`
  ([nav2d_operator/msg/cmd](https://docs.ros.org/en/rolling/p/nav2d_operator/msg/cmd.html)):
  Motion command comming from a higher level node, e.g. a path planner.
  `Velocity` ranges from full speed backward (-1.0) over stop (0.0) to
  full speed forward (1.0). `Turn` ranges from maximum left (-1.0,
  turn in place ccw) over straight (0) to maximum right (1.0, turn in
  place cw). The parameter `Mode` defines how to handle obstacles,
  either by avoiding them (0) or stopping in front of them (1).

#### Published Topics

- `cmd_vel`
  ([geometry_msgs/msg/Twist](https://docs.ros.org/en/rolling/p/geometry_msgs/msg/Twist.html)):
  Control command to robot platform.
- `~desired`
  ([nav_msgs/msg/GridCells](https://docs.ros.org/en/rolling/p/nav_msgs/msg/GridCells.html)):
  Visualizes the received input command.
- `~route`
  ([nav_msgs/msg/GridCells](https://docs.ros.org/en/rolling/p/nav_msgs/msg/GridCells.html)):
  Visualizes the control command send to the robot.
- `~local_map/costmap`
  ([nav_msgs/msg/OccupancyGrid](https://docs.ros.org/en/rolling/p/nav_msgs/msg/OccupancyGrid.html)):
  Visualizes the internal Costmap2D.

#### Parameters

- `~max_free_space` (`double`, default: `5.0`): Maximum considered
  trajectory length. All turn directions with longer trajectories will
  have an equal distance-value of 1.0.
- `~safety_decay` (`double`, default: `0.95`): Obstacles will be
  discounted by this value for every cell distance in the costmap. A
  lower value (<1.0) causes the robot to avoid obstacles later and
  ignore obstacles that are far away.
- `~max_velocity` (`double`, default: `1.0`): Maximum velocity command
  to be send to the robot when no obstacles present. A value of 1.0
  means 100% of the platforms own max speed.
- `~safety_weight` (`int`, default: `1`): Relative influence of a
  trajectories distance to obstacles.
- `~distance_weight` (`int`, default: `1`): Relative influence of free
  space in front of the robot.
- `~conformance_weight` (`int`, default: `1`): Relative influence of the
  conformance with the desired turn direction from path planner etc.
- `~continue_weight` (`int`, default: `1`): Relative influence of the
  continuity of control commands.
- `~publish_route` (`bool`, default: `false`): Whether to publish the
  `desired` and `route` topics.
