## Example

See the [Operator Tutorial](nav2d/Tutorials/RobotOperator) for an
example how to setup the Operator in Stage and use a Joystick to
simulate commands from a higher level node.

## ROS Interface

```clearsilver
node.0 {
  name=operator
  desc=The `operator` takes motion commands from a path planner and outputs control commands to the robot hardware avoiding obstacles in front of the robot.
  sub{
    0.name= scan
    0.type= sensor_msgs/LaserScan
    0.desc= Laser scans to update local costmap.
    1.name= tf
    1.type= tf/tfMessage
    1.desc= Transforms.
    2.name= cmd
    2.type= nav2d_operator/cmd
    2.desc= Motion command comming from a higher level node, e.g. a path planner. `Velocity` ranges from full speed backward (-1.0) over stop (0.0) to full speed forward (1.0). `Turn` ranges from maximum left (-1.0, turn in place ccw) over straight (0) to maximum right (1.0, turn in place cw). The parameter `Mode` defines how to handle obstacles, either by avoiding them (0) or stopping in front of them (1).
  }
  pub{
    0.name= cmd_vel
    0.type= geometry_msgs/Twist
    0.desc= Control command to robot platform.
    1.name= ~desired
    1.type= nav_msgs/GridCells
    1.desc= Visualizes the received input command.
    2.name= ~route
    2.type= nav_msgs/GridCells
    2.desc= Visualizes the control command send to the robot.
    3.name= ~local_map/costmap
    3.type= nav_msgs/OccupancyGrid
    3.desc= Visualizes the internal Costmap2D.
  }

  param {
    0.name= ~max_free_space
    0.default=5.0
    0.type= double
    0.desc= Maximum considered trajectory length. All turn directions with longer trajectories will have an equal distance-value of 1.0.
    1.name= ~safety_decay
    1.default=0.95
    1.type= double
    1.desc=Obstacles will be discounted by this value for every cell distance in the costmap. A lower value (<1.0) causes the robot to avoid obstacles later and ignore obstacles that are far away.
    2.name= ~max_velocity
    2.default=1.0
    2.type= double
    2.desc=Maximum velocity command to be send to the robot when no obstacles present. A value of 1.0 means 100% of the platforms own max speed.
    3.name= ~safety_weight
    3.default=1
    3.type= int
    3.desc=Relative influence of a trajectories distance to obstacles.
    4.name= ~distance_weight
    4.default=1
    4.type=int
    4.desc=Relative influence of free space in front of the robot.
    5.name= ~conformance_weight
    5.default=1
    5.type=int
    5.desc=Relative influence of the conformance with the desired turn direction from path planner etc.
    6.name= ~continue_weight
    6.default=1
    6.type=int
    6.desc=Relative influence of the continuity of control commands.
    7.name= ~publish_route
    7.default=false
    7.type=bool
    7.desc=Whether to publish the `desired` and `route` topics.
```
