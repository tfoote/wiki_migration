## Build and Launch

```
rosmake nxt_teleop
```

For keyboard teleop: ```
roslaunch nxt_teleop teleop_keyboard.launch
```

For joystick teleop: ```
roslaunch nxt_teleop teleop_joy.launch
```

## ROS API

```clearsilver
node.0 {
name=nxt_teleop_joy
desc=`nxt_teleop_joy` provides a joystick interface for any nxt_robot using the [[nxt_controllers|nxt_base_controller]]. 
pub{
0.name= ~cmd_vel
0.type= geometry/Twist
0.desc= The desired linear and angular x,y,z of the base.
}
sub{
0.name= ~joy
0.type= joy/Joy
0.desc= The current state of the joystick buttons.
}
param{
1.name= ~axis_linear
1.default=1
1.type= int
1.desc= The joystick axis that will control the linear velocity.
2.name= ~axis_angular
2.default=2
2.type= int
2.desc= he joystick axis that will control the angular velocity.
3.name= ~axis_deadman
3.default=0
3.type= int
3.desc= The button for the deadman switch (this button must be pressed to drive).
4.name= ~scale_linear
4.default=50.0
4.type= double
4.desc= The scaling factor from the joystick input to the linear velocity.
5.name= ~scale_angular
5.default=2.0
5.type= double
5.desc= The scaling factor from the joystick input to the angular velocity.
}
}
node.1 {
name=nxt_teleop_key
desc=`nxt_teleop_key` provides an arrow key interface for any nxt_robot using the [[nxt_controllers|nxt_base_controller]]. 
pub{
0.name= ~cmd_vel
0.type= geometry/Twist
0.desc= The desired linear and angular x,y,z of the base.
}
param{
1.name= ~scale_linear
1.default=1.0
1.type= double
1.desc= The scaling factor from the joystick input to the linear velocity.
2.name= ~scale_angular
2.default=1.0
2.type= double
2.desc= The scaling factor from the joystick input to the angular velocity.
}
}
```
