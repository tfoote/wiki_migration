## Documentation

This
[Tutorial](turtlebot_interactive_markers/Tutorials/UsingTurtlebotInteractiveMarkers)
will walk you through using interactive markers to control the
TurtleBot.

## Video

[Youtube](https://www.youtube.com/watch?v=MQ6fNrehMNI)

## Nodes

```clearsilver
name = turtlebot_marker_server
desc = Creates an interactive marker server to allow the user to control the TurtleBot base through rviz

pub {
  0.name = /turtlebot_node/cmd_vel
  0.type = geometry_msgs/Twist
  0.desc = TurtleBot commanded velocity topic
}
param {
  1.name = ~link_name
  1.type = string
  1.desc = tf frame to center the interactive markers around
  1.default = /base_link

  2.name = ~linear_scale
  2.type = double
  2.desc = Value to scale translation input by to convert to velocity
  2.default = 1.0

  3.name = ~angular_scale
  3.type = double
  3.desc = Value to scale rotational input by to convert to angular velocity
  3.default = 2.2
}
```
