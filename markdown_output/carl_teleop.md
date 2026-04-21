## About

The `carl_teleop` package provides various methods for human control
of the CARL robot, such as teleoperation of the base, arm, and sensors
via keyboard teleoperation and joystick/gamepad teleoperation.

## Nodes



```clearsilver
node.0 {
  name = carl_joy_teleop
  desc = 'carl_joy_teleop' allows for control of the Segway base, simultaneous 6-DoF control of the JACO arm, individual finger control, and sensor position control using a joystick or gamepad.
  sub {
    0.name = joy
    0.type = sensor_msgs/Joy
    0.desc = Reads input from a joystick or gamepad.
  }
  pub {
    0.name = cmd_vel
    0.type = geometry_msgs/Twist
    0.desc = Send twist commands to the Segway base.
  }
  pub {
    1.name = jaco_arm/angular_cmd
    1.type = wpi_jaco_msgs/AngularCommand
    1.desc = Send angular commands (for fingers) to the JACO arm.
  }
  pub {
    2.name = jaco_arm/cartesian_cmd
    2.type = wpi_jaco_msgs/CartesianCommand
    2.desc = Send Cartesian commands to the JACO arm.
  }
  pub {
    3.name = asus_controller/tilt
    3.type = std_msgs/Float64
    3.desc = Send tilt commands to the asus depth sensor controller.
  }
  pub {
    4.name = creative_controller/pan
    4.type = std_msgs/Float64
    4.desc = Send pan commands to the creative depth sensor controller.
  }
  pub {
    5.name = carl_moveit_wrapper/cartesian_control
    5.type = geometry_msgs/Twist
    5.desc = Send Cartesian commands to an alternate test controller.
  }
  srv_called {
    0.name = rail_segmentation/segment
    0.type = rail_segmentation/Segment
    0.desc = Segmentation command for the asus point cloud.
  }
  srv_called {
    1.name = jaco_arm/software_estop
    1.type = wpi_jaco_msgs/EStop
    1.desc = Arm estop activation/deactivation.
  }
  act_called {
    0.name = carl_moveit_wrapper/common_actions/ready_arm
    0.type = wpi_jaco_msgs/HomeArmGoal
    0.desc = Arm home and retract actions with obstacle avoidance.
  }
  param {
    0.name = linear_throttle_factor_base
    0.type = double
    0.desc = Velocity throttle for base forward/backward motion.
    0.default = 1.0
  }
  param {
    1.name = angular_throttle_factor_base
    1.type = double
    1.desc = Velocity throttle for base left/right angular motion.
    1.default = 1.0
  }
  param {
    2.name = linear_throttle_factor_arm
    2.type = double
    2.desc = Velocity throttle for arm linear motion.
    2.default = 1.0
  }
  param {
    3.name = angular_throttle_factor_arm
    3.type = double
    3.desc = Velocity throttle for arm angular motion.
    3.default = 1.0
  }
  param {
    4.name = finger_throttle_factor
    4.type = double
    4.desc = Velocity throttle for finger movement.
    4.default = 1.0
  }
  param {
    5.name = controller_type
    5.type = string
    5.desc = Type of controller being used (currently either "analog" or "digital" for triggers, more to be added as necessary).
    5.default = "digital"
  }
  param {
    6.name = use_teleop_safety
    6.type = bool
    6.desc = Whether base commands should go through the teleop safety layer before reaching the robot.
    6.default = false
  }
}
node.1 {
  name = carl_key_teleop
  desc = 'carl_key_teleop' allows for keyboard teleop of the base, arm, and finger joints.
  pub {
    0.name = cmd_vel
    0.type = geometry_msgs/Twist
    0.desc = Send twist commands to the Segway base.
  }
  pub {
    1.name = jaco_arm/angular_cmd
    1.type = wpi_jaco_msgs/AngularCommand
    1.desc = Send angular commands to the JACO arm.
  }
  pub {
    2.name = jaco_arm/cartesian_cmd
    2.type = wpi_jaco_msgs/CartesianCommand
    2.desc = Send Cartesian commands to the JACO arm.
  }
  param {
    0.name = linear_throttle_factor_base
    0.type = double
    0.desc = Velocity throttle for base forward/backward motion.
    0.default = 1.0
  }
  param {
    1.name = angular_throttle_factor_base
    1.type = double
    1.desc = Velocity throttle for base left/right angular motion.
    1.default = 1.0
  }
  param {
    2.name = linear_throttle_factor_arm
    2.type = double
    2.desc = Velocity throttle for arm linear motion.
    2.default = 1.0
  }
  param {
    3.name = angular_throttle_factor_arm
    3.type = double
    3.desc = Velocity throttle for arm angular motion.
    3.default = 1.0
  }
  param {
    4.name = finger_throttle_factor
    4.type = double
    4.desc = Velocity throttle for finger movement.
    4.default = 1.0
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
triggers) and the Logitech Wireless Gamepad (analog triggers). If your
gamepad does not work with this node, you can remap the axes and buttons
using [joystick_remapper](joystick_remapper) package, or open an issue
in the code repository and support for the new controller may be added.

The arm has four control modes, Finger Control, Arm Control, Base
Control, and Sensor Control, which can be switched to by pressing
buttons 1(X), 2(A), 3(B), and 4(Y) respectively.

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

Base Control Mode:

-   left thumbstick up/down - base forward/backward translation
-   right thumbstick left/right - base left/right rotation
-   left bumper - deadman switch, must be held to move the base
-   right bumper - boost, increases max driving speed while held
-   back button - enable arm estop
-   start button - disable arm estop
-   d-pad - display help

Sensor Control Mode:

-   left thumbstick left/right - creative servo pan
-   right thumbstick up/down - asus servo tilt
-   right thumbstick click - asus segmentation
-   left bumper - home arm
-   right bumper - retract arm

### Keyboard Teleop

The keyboard teleop operates by reading input from the command line, and
as such it can only recognize one key press at a time.

The arm has three control modes, Arm Control, Finger Control, and Base
Control which can be switched to by pressing the 1, 2, and 3 keys,
respectively.

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

Base Control Mode:

-   up/down - base forward/backward translation
-   left/right - base left/right rotation
-   h - display help

## Installation

To install the `carl_bot` package, you can install from source with
the following commands: . 

```shell
cd /(your catkin workspace)/src
git clone https://github.com/WPI-RAIL/carl_bot.git
cd ..
catkin_make
catkin_make install
```



## Startup

Joystick or keyboard teleop can be started with the launch files
`carl_joy_teleop.launch` and `carl_key_teleop.launch`, respectively.
Both files have parameters for velocity limits, which can be set on
launch to limit the velocities of the arm's translation, rotation,
finger movement, and base movement. Furthermore,
`carl_joy_teleop.launch` includes a parameter for the controller type,
which can currently be set to either "analog" or "digital",
representing controllers with analog triggers and digital triggers,
respectively. Example launch syntax is given below.

With default parameters: . 

```
roslaunch carl_teleop carl_joy_teleop.launch
```

 .


```
roslaunch carl_teleop carl_key_teleop.launch
```



Example with parameters: . 

```
roslaunch carl_teleop carl_joy_teleop.launch linear_throttle_factor_base:=0.5 angular_throttle_factor_base:=0.5 linear_throttle_factor_arm:=0.8 angular_throttle_factor_arm:=0.8 finger_throttle_factor:=0.75 controller_type:="analog"
```

 .


```
roslaunch carl_teleop carl_key_teleop.launch linear_throttle_factor_base:=0.5 angular_throttle_factor_base:=0.5 linear_throttle_factor_arm=0.8 angular_throttle_factor_arm=0.8 finger_throttle_factor:=0.75
```


