## Overview

/!\\ This package is still experimental.

The move action server especially comes with a very simple test action -
rotate + move forward. This could be quite useful expanded into a suite
of standardised turtlebot motion tests - updates welcome.

## Nodes

```clearsilver
name = turtlebot_move_action_server
desc = Provides an action server for moving the TurtleBot through a certain distance and rotation.

pub {
  0.name = ~cmd_vel
  0.type = geometry_msgs/Twist
  0.desc = Topic to publish drive commands to.
}
param {
  0.name = ~base_frame
  0.type = string
  0.desc = TF frame name for the center of the base.
  0.default = base_link

  1.name = ~odom_frame
  1.type = string
  1.desc = TF frame name for the odometry frame.
  1.default = odom

  2.name = ~turn_rate
  2.type = double
  2.desc = Maximum turn rate, in rad/s.
  2.default = 0.75

  3.name = ~forward_rate
  3.type = double
  3.desc = Maximum forward rate, in m/s.
  3.default = 0.25
}
req_tf {
  0.from = odom_frame
  0.to   = base_frame
  0.desc = The transform we use to determine how far the robot has moved.
}
```

## Actions

### TurtlebotMove.action

```
#goal definition
float32 turn_distance     # in radians, ccw = +, cw = -
float32 forward_distance  # in meters, forward = +, backward = -
---
#result definition
float32 turn_distance
float32 forward_distance
---
#feedback
float32 turn_distance
float32 forward_distance
```

### FindFiducial.action

```
#goal definition
uint8   CHESSBOARD = 1
uint8   CIRCLES_GRID = 2
uint8   ASYMMETRIC_CIRCLES_GRID =3

string    camera_name       # name of the camera 
uint8     pattern_width     # number of objects across
uint8     pattern_height    # number of objects down
float32   pattern_size      # size the object pattern (square size or circle size)
uint8     pattern_type      # type of pattern (CHESSBOARD, CIRCLES_GRID, ASYMMETRIC_CIRCLES_GRID)
---
#result definition
geometry_msgs/PoseStamped pose
---
#feedback
```
