## Overview

The \`robotino_safety\` package implements the \`robotino_safety_node\`
which listens for linear and angular velocities published for Robotino
on the \`robotino_cmd_vel\` topic and based on the laser scan readings,
looks out for potential obstacles and publishes velocities accordingly
on the \`cmd_vel\` topic.

![](attachment:robotino_safety_ros.png)

\'\'\'Note:\'\'\' The obstacle above is visualized in red. The yellow
cylinder is the next heading point on the global path and not the
obstacle.

The laser scans received are converted to pointclouds. The points from
the cloud are checked if they lie in the outer ellipse (as seen in the
image above). If any points do lie in the outer ellipse, it means
Robotino is approaching an obstacle and it is decelarated. If the
obstacle doesn\'t move away (in case it is not a human or a cat walking
by) and approaches the inner ellipse, Robotino continues to decelerate
and finally stop if the obstacle touches the inner ellipse.

The radii of the inner and outer ellipses can be varied in the params
below.

## ROS Nodes

```clearsilver
node.0 {
 name = robotino_safety_node
 desc = 
 pub {
  0.name = cmd_vel
  0.type = geometry_msgs/Twist
  0.desc = Linear and angular velocities for Robotino
  1.name = ~inner_ellipse_marker
  1.type = visualization_msgs/Marker
  1.desc = Visualization marker for the inner ellipse
  2.name = ~outer_ellipse_marker
  2.type = visualization_msgs/Marker
  2.desc = Visualization marker for the outer ellipse
 }
 sub {
  0.name = robotino_cmd_vel
  0.type = geometry_msgs/Twist 
  0.desc = A unique cmd_vel topic for Robotino. The velocities published on this topic are monitored by this node so to as to avoid potential collisions.
  1.name = bumper
  1.type = std_msgs/Bool
  1.desc = Bumper values from Robotino. In case of a bumper collision, the node shutsdown.
  2.name = scan
  2.type = sensor_msgs/LaserScan
  2.desc = Laser scans from Robotino. The scans are used to detect obstacles ahead.
 }

 param {
  0.name = ~outer_major_radius
  0.default = 0.70
  0.type= double
  0.desc = The major radius of the outer ellipse.
  1.name = ~outer_minor_radius
  1.default = 0.30
  1.type = double
  1.desc = The minor radius of the outer ellipse.
  2.name = ~inner_major_radius
  2.default = 0.40
  2.type = double
  2.desc = The major radius of the inner ellipse.
  3.name = ~inner_minor_radius
  3.default = 0.25  
  3.type = double
  3.desc = The minor radius of the inner ellipse.
  4.name = ~node_loop_rate
  4.default = 20
  4.type = int
  4.desc = The loop rate of this node.
 }
```

#### Usage

The \`robotino_safety_node\` can be launched as follows.
```
roslaunch robotino_safety robotino_safety_node.launch
```
