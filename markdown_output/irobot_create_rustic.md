The Create platform itself outputs state information from on-board
sensors including odometers, bump sensors, cliff sensors, and battery
statistics. It can also receive differential drive commands that move
the robot. The \`irobot_create_cu\` and \`irobot_create_rustic\` ROS
nodes are responsible for linking the create with the rest of the
system. Together, they read state information from the Create and then
periodically publish it to the rest of the system. \`irobot_create_cu\`
receives high-level drive commands and/or paths from the system, check
them for validity, and then sends the necessary low-level commands to
the robot via \`irobot_create\`.

------------------------------------------------------------------------

## API Documentation

```clearsilver
node.0 {
name = base_planner_cu
desc << EOM
`irobot_create_rustic` is a modified version of [[http://code.google.com/p/brown-ros-pkg/|Brown's iRobot Create package]]. We initially had users obtain `irobot_create` by installing version 104 of the Brown ROS package, but depreciated functionality has made it incompatible with ROS V1.0, and Brown has depreciated their old `irobot_create` in-favor of a newer and significantly different node. Therefore, we have modified version 104 of Brown's `irobot_create` to make it compatible with ROS V1.0, and explicitly included the modified version as `irobot_create_rustic` in `prairiedog`.
EOM
param {
0.name= ~serial_port
0.default= /dev/create
0.type= string
0.desc= The name of the computer port to which the iRobot create is attached.
}
}
```
