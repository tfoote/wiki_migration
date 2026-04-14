## Overview

This package contains the node that subscribes to /joy messages and
publishes command messages for the robot platform including speed level
control. The joystick output is feed to a mux
(<http://wiki.ros.org/twist_mux>) so that the final command to the robot
can be set by different components (move_base, etc.)

The node allows to load different types of joysticks (PS4, PS3,
Logitech, Thrustmaster). New models can be easily added by creating new
.yaml files. If modbus_io node is available, the digital outputs
(ligths, axes, etc.) can also be controlled with the pad. If ptz camera
is available, the pan-tilt-zoom can also be commanded with the pad.
