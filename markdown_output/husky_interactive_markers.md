{

If you want to launch only the markers without an rviz instance:



```
roslaunch husky_interactive_markers interactive_markers.launch
```



Markers should appear around Husky in running rviz instances. Click and
drag them to send velocity command messages.

## Nodes



```clearsilver
node.0 {
 name = marker_server
 desc = Creates an interactive marker server to allow the user to control the Husky base through rviz
 pub {
  0.name= cmd_vel
  0.type= geometry_msgs/Twist
  0.desc= [[Robots/Husky|Husky]] commanded velocity topic.
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
}
```

 }}}}

{ }}}}
