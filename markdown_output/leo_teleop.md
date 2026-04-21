## Overview

This package can be used to control a real or simulated
[Leo Rover](Robots/Leo Rover) with a keyboard or a joystick.

## Usage

To control the robot with a keyboard, simply type on the terminal (on
your computer or on the robot via SSH): ```
rosrun leo_teleop key_teleop
``` This
will run the [teleop_twist_keyboard](teleop_twist_keyboard) node (with
some parameters set) which will print the key mapping at the start. For
best performance, set the keyboard repeat delay on your system below
300ms.

To control the robot with a joystick, use: ```
roslaunch leo_teleop joy_teleop.launch
``` If
your joystick device is available on a path other than
`/dev/input/js0`, you can specify it using the `joy_dev` argument,
for example: ```
roslaunch leo_teleop joy_teleop.launch joy_dev:=/dev/input/js1
``` The default joy button and axis
mapping was created for Xbox 360 Controller and it looks as follows:

  -- ----------------------------- -- --------------------------------------------------- --
     RB button                        Hold it to publish velocity commands to the robot   
     Up/Down Axis stick left          Control linear speed of the robot                   
     Left/Right Axis stick right      Control angular speed of the robot                  
  -- ----------------------------- -- --------------------------------------------------- --

If you would like to use custom mapping, set the `joy_config_file`
argument to a path of a YAML file containing parameters for
[teleop_twist_joy](teleop_twist_joy) node.
