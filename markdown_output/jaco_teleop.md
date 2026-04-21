## About

The `jaco_teleop` package provides various methods for human control
of the JACO and JACO2 arm via keyboard teleoperation and
joystick/gamepad teleoperation. This may work for the MICO as well, but
it has not yet been tested.

## Nodes

```clearsilver
node.0 {
  name = jaco_joy_teleop
  desc = 'jaco_joy_teleop' allows for simultaneous 6-DoF control of the arm and individual finger control using a joystick or gamepad.
  sub {
    0.name = joy
    0.type = sensor_msgs/Joy
    0.desc = Reads input from a joystick or gamepad.
  }
  pub {
    0.name = jaco_arm/angular_cmd
    0.type = wpi_jaco_msgs/AngularCommand
    0.desc = Send angular commands (finger control) to the arm.
    1.name = jaco_arm/cartesian_cmd
    1.type = wpi_jaco_msgs/CartesianCommand
    1.desc = Send Cartesian commands to the JACO arm.
  }
  srv_called {
    0.name = jaco_arm/software_estop
    0.type = wpi_jaco_msgs/EStop
    0.desc = Arm software emergency stop and restart.
  }
  param {
    0.name = linear_throttle_factor
    0.type = double
    0.desc = Velocity throttle for arm linear motion.
    0.default = 1.0
    1.name = angular_throttle_factor
    1.type = double
    1.desc = Velocity throttle for arm angular motion.
    1.default = 1.0
    2.name = finger_throttle_factor
    2.type = double
    2.desc = Velocity throttle for finger movement.
    2.default = 1.0
    3.name = controller_type
    3.type = string
    3.desc = Type of controller being used (currently either "analog" or "digital" for triggers, more to be added as necessary).
    3.default = "digital"
    4.name = wpi_jaco/arm_name
    4.type = string
    4.desc = Name of the arm, either "jaco" or "jaco2"
    4.default = jaco
  }
}
node.1 {
  name = jaco_key_teleop
  desc = 'jaco_key_teleop' allows for keyboard teleop of the arm and finger joints.
  pub {
    0.name = jaco_arm/angular_cmd
    0.type = wpi_jaco_msgs/AngularCommand
    0.desc = Send angular commands (finger control) to the arm.
    1.name = jaco_arm/cartesian_cmd
    1.type = wpi_jaco_msgs/CartesianCommand
    1.desc = Send Cartesian commands to the arm.
  }
  param {
    0.name = linear_throttle_factor
    0.type = double
    0.desc = Velocity throttle for arm linear motion.
    0.default = 1.0
    1.name = angular_throttle_factor
    1.type = double
    1.desc = Velocity throttle for arm angular motion.
    1.default = 1.0
    2.name = finger_throttle_factor
    2.type = double
    2.desc = Velocity throttle for finger movement.
    2.default = 1.0
    3.name = wpi_jaco/arm_name
    3.type = string
    3.desc = Name of the arm, either "jaco" or "jaco2"
    3.default = jaco
  }
}
```

## Controls

Controls for the joystick and keyboard teleop nodes are listed below.

### Joystick Teleop

The joystick teleop node currently supports both gamepads with analog
triggers and gamepads with digital triggers. The gamepad type can be set
on launch with the `controller_type` parameter. Currently, the node
has been tested with the Logitech Dual Action wired controller (digital
triggers), the Logitech Wireless Gamepad (analog triggers), and the
Microsoft XBOX 360 wired controller (analog triggers). If your gamepad
does not work with this node, you can remap the axes and buttons using
[joystick_remapper](joystick_remapper) package, or open an issue in the
code repository and support for the new controller may be added.

The arm has two control modes, Arm Control and Finger Control, which can
be switched to by pressing buttons 2(A) and 1(X), respectively.

Arm Control Mode:

-   left thumbstick - arm x and y translation
-   right thumbstick - arm pitch and yaw
-   left and right bumper - arm roll
-   left and right triggers - arm down/up translation
-   back button - enable arm estop
-   start button - disable arm estop
-   d-pad - display help

Finger Control Mode:

-   left thumbstick up/down - open/close all fingers
-   right thumbstick up/down - open/close thumb
-   left bumper and trigger - open/close first finger
-   right bumper and trigger - open/close second finger
-   back button - enable arm estop
-   start button - disable arm estop
-   d-pad - display help

### Keyboard Teleop

The keyboard teleop operates by reading input from the command line, and
as such it can only recognize one key press at a time.

The arm has two control modes, Arm Control and Finger Control, which can
be switched to by pressing the 1 and 2 keys, respectively.

Arm Control Mode:

-   w/s - arm forward/backward translation
-   a/d - arm left/right translation
-   r/f - arm up/down translation
-   q/e - arm roll
-   up/down - arm pitch
-   left/right - arm yaw
-   h - display help

Finger Control Mode:

-   q/a - open/close thumb
-   w/s - open/close top finger
-   e/d - open/close bottom finger
-   r/f - open/close all fingers
-   h - display help

## Installation

To install the `wpi_jaco` package, you can install from source with
the following commands: . ```shell
cd /(your catkin workspace)/src
git clone https://github.com/RIVeR-Lab/wpi_jaco.git
cd ..
catkin_make
catkin_make install
```

## Startup

Joystick or keyboard teleop can be started with the launch files
`jaco_joy_teleop.launch` and `jaco_key_teleop.launch`, respectively.
Both files have parameters for velocity limits, which can be set on
launch to limit the velocities of the arm's translation, rotation, and
finger movement. Furthermore, `jaco_joy_teleop.launch` includes a
parameter for the controller type, which can currently be set to either
"analog" or "digital", representing controllers with analog triggers
and digital triggers, respectively. Example launch syntax is given
below.

With default parameters: . ```
roslaunch jaco_teleop jaco_joy_teleop.launch
``` .
```
roslaunch jaco_teleop jaco_key_teleop.launch
```

Example with parameters: . ```
roslaunch jaco_teleop jaco_joy_teleop.launch linear_throttle_factor:=0.5 angular_throttle_factor:=0.5 finger_throttle_factor:=0.75 controller_type:="analog"
``` .
```
roslaunch jaco_teleop jaco_key_teleop.launch linear_throttle_factor:=0.5 angular_throttle_factor:=0.5 finger_throttle_factor:=0.75
```
