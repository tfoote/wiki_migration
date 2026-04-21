## Starting Teleoperation

Start all the needed remote teleoperation nodes by running


```
roslaunch nao_teleop teleop_joy.launch
```

 on the remote machine (e.g. your PC).

Then start [naoqi_driver](naoqi_driver) either on your local machine or
on the Nao (nao_walker and nao_controller are required by this node). By
default, gamepad teleoperation starts paused. Just hit the "toggle
control button" (#8 by default or #9 on PS3 controller) and start
walking Nao around by setting the velocities for the !OmniWalk engine
with the two sticks on the gamepad (see below).

## Teleoperating Nao

You can teleoperate Nao using any joystick or gamepad configured in ROS
with omnidirectional velocities, very similar to
[pr2_teleop](pr2_teleop#Controlling). The following commands are
currently implemented (tested on a Logitech Cordless Rumblepad II, where
the button numbering should be increased by one as it starts with
"1"):

-   Right analog stick: translational velocity
-   Left analog stick (left / right): rotational velocity (turning)
-   Button 0: Standing up ("Init pose")
-   Button 5: Toggle head movement: hold to control the head directly
    with the analog sticks
-   Button 8: Toggle gampad control on / off. Enabling gamepad control
    will also enable stiffness on the Nao.
-   Button 9: Go to safe "crouching" / "squatting" position and
    remove joint stiffness (Enable stiffness again by toggling control
    off and on again)

Initially, gamepad control is off and needs to be enabled with button 8.
When you're done you can either shut down all nodes or toggle gamepad
control off, Nao will remain standing in its current state.

Below is the default button placement on a Logitech Cordless Rumblepad
II. The button / behavior mapping can be changed with parameters.

![](attachment:nao_teleop.png)

## Node API



```clearsilver
node.0 {
name = teleop_nao_joy
desc = Teleoperates Nao with a Joystick / Gamepad
sub {
  0.name = joy
  0.type = joy/Joy
  0.desc = Input from joystick driver
}
pub {
  0.name = cmd_vel
  0.type = geometry_msgs/Twist
  0.desc = Omnidirectional walking velocity
  1.name = motion_command_btn
  1.type = nao_ctrl/MotionCommandBtn
  1.desc = discrete motion actions (e.g. "sit down")
  2.name = head_angles
  2.type = nao_ctrl/HeadAngles
  2.desc = desired joint angles for the head
  3.name = speech
  3.type = std_msgs/String
  3.desc = Status messages to be said over Nao's speech synthesis (e.g. "Gamepad enabled")
}

param {
  0.name = ~axis_*
  0.type = int
  0.desc = `axis_`... parameters (e.g. `axis_x`) enable you to adjust the axes used to control Nao's motion to your preference or hardware setting.

  1.name = ~btn_*
  1.type = int
  1.desc = `btn_`... parameters (e.g. `btn_enable_control) enable you to adjust the buttons used to control Nao to your preference or hardware setting.

  2.name = ~max_vx
  2.type = double
  2.desc = Maximum fraction of x velocity to be used when teleoperating (between 0 and 1). This controls Nao's step length.
  2.default = 1.0

  3.name = ~max_vy
  3.type = double
  3.desc = Maximum fraction of y velocity to be used when teleoperating (between 0 and 1). This controls Nao's step length.
  3.default = 1.0

  4.name = ~max_vw
  4.type = double
  4.desc = Maximum fraction of rotational velocity to be used when teleoperating (between 0 and 1). This controls Nao's step length when turning.
  4.default = 0.5
}
}
```


