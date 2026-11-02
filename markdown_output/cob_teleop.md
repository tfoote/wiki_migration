## Hardware Requirements

This package uses a joystick or keyboard for teleoperation of
Care-O-bot. To use this package you need either a real Care-O-bot or a
simulated one (see [cob_gazebo](https://index.ros.org/p/cob_gazebo)).

## ROS API

The cob_teleop package provides both, a
configurable node for teleoperation by joystick or by keyboard.


```clearsilver
 name = cob_teleop
 desc = The `cob_teleop` node takes in <<MsgLink(sensor_msgs/Joy)>> messages and send direct commands to the hardware.

goal{
}

result{
}

feedback{
}

sub{
 0.name = joy
 0.type = sensor_msgs/Joy
 0.desc = Receives joystick commands.
 1.name = /joint_states
 1.type = sensor_msgs/JointState
 1.desc = Receives the joint states of all joints for initialization.
}

pub{
 0.name = arm_controller/command
 0.type = trajectory_msgs/JointTrajectory
 0.desc = Publishes commands to the arm.
 1.name = torso_controller/command
 1.type = trajectory_msgs/JointTrajectory
 1.desc = Publishes commands to the torso.
 2.name = tray_controller/command
 2.type = trajectory_msgs/JointTrajectory
 2.desc = Publishes commands to the tray.
 3.name = base_controller/command
 3.type = geometry_msgs/Twist
 3.desc = Publishes commands to the base.
}

srv{
}

param{
 0.name = ~run_factor
 0.type = float
 0.default = 1.5
 0.desc = Defines the factor to multiply velocities when run button is pressed.

 1.name = ~lower_neck_button
 1.type = int
 1.default = 6
 1.desc = Joystick button for lower neck.
 2.name = ~upper_neck_button
 2.type = int
 2.default = 4
 2.desc = Joystick button for upper neck.
 3.name = ~tray_button
 3.type = int
 3.default = 3
 3.desc = Joystick button for tray.
 4.name = ~arm_joint12_button
 4.type = int
 4.default = 0
 4.desc = Joystick button for joint 1 and 2 of arm.
 5.name = ~arm_joint34_button
 5.type = int
 5.default = 1
 5.desc = Joystick button for joint 3 and 4 of arm.
 6.name = ~arm_joint56_button
 6.type = int
 6.default = 2
 6.desc = Joystick button for joint 5 and 6 of arm.
 7.name = ~arm_joint7_button
 7.type = int
 7.default = 3
 7.desc = Joystick button for joint 7 of arm.
 8.name = ~deadman_button
 8.type = int
 8.default = 5
 8.desc = Joystick button for deadman functionality.
 9.name = ~run_button
 9.type = int
 9.default = 7
 9.desc = Joystick button run functionality.

 10.name = ~axis_vx
 10.type = int
 10.default = 1
 10.desc = Joystick axis for base movements along x-axis.
 11.name = ~axis_vy
 11.type = int
 11.default = 0
 11.desc = Joystick axis for base movements along y-axis.
 12.name = ~axis_vth
 12.type = int
 12.default = 2
 12.desc = Joystick axis for base movements around tetha-axis.
 13.name = ~up_down
 13.type = int
 13.default = 5
 13.desc = Joystick axis for up and down movements.
 14.name = ~left_right
 14.type = int
 14.default = 4
 14.desc = Joystick axis for left and right movements.

 13.name = ~lower_tilt_step
 13.type = float
 13.default = 0.05
 13.desc = Step for lower tilt movements in rad/sec.
 14.name = ~lower_pan_step
 14.type = float
 14.default = 0.05
 14.desc = Step for lower pan movements in rad/sec.
 15.name = ~upper_tilt_step
 15.type = float
 15.default = 0.075
 15.desc = Step for upper tilt movements in rad/sec.
 16.name = ~upper_pan_step
 16.type = float
 16.default = 0.075
 16.desc = Step for upper pan movements in rad/sec.
 17.name = ~tray_step
 17.type = float
 17.default = 0.1
 17.desc = Step for tray movements in rad/sec.
 18.name = ~arm_left_right_step
 18.type = float
 18.default = 0.1
 18.desc = Step for left and right arm movements in rad/sec.
 19.name = ~arm_up_down_step
 19.type = float
 19.default = 0.1
 19.desc = Step for up and down arm movements in rad/sec.

 20.name = ~max_vx
 20.type = float
 20.default = 0.3
 20.desc = Maximum velocity for base movements along x-axis in m/sec.
 21.name = ~max_vy
 21.type = float
 21.default = 0.2
 21.desc = Maximum velocity for base movements along y-axis in m/sec.
 22.name = ~max_vth
 22.type = float
 22.default = 0.3
 22.desc = Maximum velocity for base movements around tetha-axis in rad/sec.
 23.name = ~max_ax
 23.type = float
 23.default = 0.5
 23.desc = Maximum acceleration for base movements along x-axis in m/sec^2.
 24.name = ~max_ay
 24.type = float
 24.default = 0.5
 24.desc = Maximum acceleration for base movements along y-axis in m/sec^2.
 25.name = ~max_ath
 25.type = float
 25.default = 0.5
 25.desc = Maximum acceleration for base movements around tetha-axis in rad/sec^2.
}

req_tf{
}

prov_tf{
}
```



## Usage/Examples

### Starting teleoperation node

For starting the teleoperation with joystick 

```
roslaunch cob_bringup teleop.launch
```


For including the teleoperation in your overall launch file use


```
<include file="$(find cob_bringup)/tools/teleop.launch" />
```

 If you haven't got joystick you can move the
base of the robot using the keyboard: 

```
roslaunch cob_teleop teleop_keyboard.launch
```



### Move components

To be able to use the joystick the `deadman_button` has to be pressed
all the time, as soon as the button is released a stop will be send to
all hardware components. Have a look at the following image to see which
buttons command which components. ![width=100%](doc/teleop.png)

For **moving the base**: Hold the `deadman` button and use the base
`rotation` and `translation` axis to move the base.

For **moving the torso**: Hold the `deadman` button and the `upper`
or `lower` neck button, then use the `up_down` or `left_right`
axis to move the torso.

For **moving the tray**: Hold the `deadman` button and the `tray`
button, then use the `up_down` axis to move the tray.

For **moving the arm**: Hold the `deadman` button and one of the
`arm` buttons, then use the `up_down` or `left_right` axis to move
the selected arm joints.

### Parameter file

A sample parameter file could look like this 

```
# common params
run_factor: 2.0

# buttons
lower_neck_button: 6
upper_neck_button: 4
tray_button: 3
arm_joint12_button: 0
arm_joint34_button: 1
arm_joint56_button: 2
arm_joint7_button: 3
deadman_button: 5
run_button: 7

# axes
axis_vx: 1
axis_vy: 0
axis_vth: 2
up_down: 5 #tray--up/down; tilt--front/back, here we just name up_down
left_right: 4 #pan--left/right

# velocities in rad/sec, m/sec
lower_tilt_step: 0.05
lower_pan_step: 0.05
upper_tilt_step: 0.075
upper_pan_step: 0.075
tray_step: 0.15
arm_left_right_step: 0.1
arm_up_down_step: 0.1
max_vx: 0.3
max_ax: 0.5
max_vy: 0.2
max_ay: 0.5
max_vth: 0.3
max_ath: 0.7
```
