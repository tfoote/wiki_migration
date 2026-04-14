tele_mobile provides teleoperation control of the mobile base of Cody,
the two-arm robot in the Healthcare Robotics Lab. It allows a joystick
at the master end to control pan&tilt servos, the linear actuator, and
the Segway Omni base on Cody.

## Usage

There are two ways to run the code. First, the user runs
joystick_node.py from the master PC, and run platform_node at the
Cody\'s control PC. Alternatively, the user can run tmobile.launch at
the master PC and it will launch both joystick node and platform node.
