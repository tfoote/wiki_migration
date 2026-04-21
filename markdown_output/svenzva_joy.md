## Nodes



```clearsilver
node.0 {
name = svenzva_joy_node
desc = This is a standard/common implementation of joystick mgmnt through the `joy` package.
pub {
0.name = /joy
0.type = sensor_msgs/Joy
0.desc = `joy` node standard output of joystick information.
}
}
node.1 {
name = svenzva_2axis_manager
desc = The ROS joystick manager for the Svenzva Arm. This node has separate versions depending on the joystick connected. Supported joysticks are: `Xbox 360` and `Svenzva 6-Axis Joystick`
pub {
0.name = /joy
0.type = sensor_msgs/Joy
0.desc = `joy` node standard output of joystick information.
1.name = /revel/eef_velocity
1.type = geometry_msgs/Twist
1.desc = Target end effector velocity as interpreted by the connected joystick (either Xbox 360 controller or Svenzva 6-Axis controller)
}
sub {
0.name =  /joy
0.type = sensor_msgs/Joy
0.desc = `joy` node standard output of joystick information.
1.name = /revel/gripper_action
1.type = svenzva_msgs/GripperAction
1.desc = An actionlib action commanding the open/closing of the gripper.
}
```


