```wiki
/!\ '''Under Development'''

Please be patient, this ROS package and the related wiki page are still under development!
```

## Documentation

See the [project homepage](ros4link) for installation instructions.

The page [KIPR Link Robot Controller](Robots/KIPR_Link) provides more
information about the hardware.

## Nodes

```clearsilver
node.0 {
  name = create_node
  desc = The create node is an ROS interface which allows to drive the iRobot Create from the KIPR Link.
}
node.1 {
  name = camera_node
  desc = The camera node enables access to the ''KIPR Link Robot Control Software'' camera features.
}
node.2 {
  name = driver_node
  desc = This node is a ROS interface to remaining ''KIPR Link Robot Control Software'' features.
}
node.3 {
  name = shell_cmd_node 
  desc = This node provides shell commands for every API function of the ''KIPR Link Robot Control Software''.
}
```

## Report a Bug

Please use
[Google Code Issues](https://code.google.com/p/ros4link/issues/list) to
report bugs or request features.

------------------------------------------------------------------------
