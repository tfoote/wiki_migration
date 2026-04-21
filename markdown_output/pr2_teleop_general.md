Note: This package originated as \`pr2_teleop_booth\` and wasn\'t
released before [ROS Hydro](hydro).

## Overview

This package offers two executables for general control of the PR2
robot - a joystick-based control program using the PS3 joystick and a
keyboard control program. Each of these programs allows a user to
control the sensor head, tilting laser, arms, base, and torso of the PR2
robot as well as enabling some useful modes for demonstration.

### Handy Cheat Sheet

<attachment:teleop_cheat_sheet.png>

## Joystick control

This section will focus on the executable pr2_teleop_general_joystick,
which allows control through a PS3 joystick controller.

### Launch files

There are several launch files offered for convenience. The first can be
accessed using

```
roslaunch pr2_teleop_general pr2_teleop_general_joystick.launch
``` This launch file enables body control, head
control, and arm control but disables prosilica control. It also starts
pr2_kinematics nodes for the left and right arms, which are necessary
for joystick control of the arms and enabling walk_along_mode.

```
roslaunch pr2_teleop_general pr2_teleop_general_joystick_noik.launch
```

implements the same functionality but does not launch arm ik nodes,
assuming that they are already running from another launch file.

```
roslaunch pr2_teleop_general pr2_teleop_general_joystick_bodyhead_only.launch
```

disables arm control altogether and starts no processes associated with
the arms.

### Pairing

Before use, the PS3 controller must be \"paired\" with the robot. If
your controller is not already paired, you can pair it by pressing the
center button, shown in the image.

There is currently no feedback from the controller or the robot during
or after pairing. The best way to tell if they have been paired
correctly is to try issuing commands to the robot via the joystick as
described below.

![](http://www.ros.org/wiki/pr2_teleop?action=AttachFile&do=get&target=pairing.png)

### Joystick layout overview

This program implements four different mapping modes for the face
buttons of the ps3 joystick depending on which of the front buttons are
depressed. If none of the front buttons are pressed then no commands are
relayed to the robot.

![ps3 joy mapping controls\|width=800](attachment:joy_ps3_front_annotated.jpg)

#### Base control mapping

In base control mode the operator can move the base or raise and lower
the torso.

#### Sensor/Head/Follow mapping

This mode permits the operator to control the head, control the tilt of
the laser, turn the projected light display on or off, and to set the
\"follow me\" mode.

#### Arm control mappings

The final mappings allow the operator to control either arm
independently or to control both simultaneously.

![ top annotated \| width=800](attachment:joy_ps3_top_annotated.jpg)

### Sensor/Head/Follow mapping

Accessing this mapping requires that the upper right front button be
depressed - see the above image.

  -- --------------------------- -- -------------------------------------------------------------------------------------------------------- --
     **Button**                     **Control Action**                                                                                       
     **1**                          Cycles the head mode (see below)                                                                         
     **2**                          Cycles the laser between Off, Slow Scan, and Fast Scan                                                   
     **3**                          Toggles the projected light between off and on                                                           
     **5 (Select) double-tap**      Moves the arms to follow mode position (see below)                                                       
     **5 (Select)**                 Exits follow mode (see below)                                                                            
     **6 (Start)**                  Initiates follow mode if the arms are in proper position and select has been double-tapped (see below)   
     **ly+/-**                      Pans the head right/left if in position control mode                                                     
     **rx+/-**                      Tilts the head up/down if in position control mode                                                       
  -- --------------------------- -- -------------------------------------------------------------------------------------------------------- --

#### Head control modes

There are four control modes for the head. The first is position
control, which allows the head to be tilted and panned using the analog
sticks. The second and third modes point the head at the right hand hand
and the left hand respectively. The final mode places the head in
mannequin mode.

#### Follow me mode

All of this assumes that the top right front button is depressed. In
order to get into follow me mode you must double-tap Select. This will
move the arms into a position in front of the robot. Do not interfere
with the arms as they are moving, and make sure they have clear paths.
Once in position press Start in order to initiate follow me mode. The
robot will nod its head if everything was successful. Otherwise it will
shake its head. To exit follow me mode press Select once.

### Base control mapping

The base control is accessible by pushing the top left front button.
Base and torso controls are essentially the same as that described in
[pr2_teleop](pr2_teleop).

  -- ------------------ -- --------------------------------------- --
     **Button**            **Control Action**                      
     **7 (Triangle)**      Raises torso                            
     **10 (X)**            Lowers torso                            
     **rx+/-**             Translates the robot forward/backward   
     **rx+/-**             Translates the robot right/left         
     **ry+/-**             Rotates the robot right/left            
  -- ------------------ -- --------------------------------------- --

### Arm control mappings

The lower front buttons control the arms. The arms may be controlled
individually by pressing only one of the front two buttons. If both arm
buttons are held any commands will be issued to both arms.

  -- ------------------ -- ----------------------------------------------------------------------------------------------------------- --
     **Button**            **Control Action**                                                                                          
     **1**                 Cycles are in between controller modes. Modes are no controllers, position control, and mannequin control   
     **2**                 When in both arm control mode untucks the arms. Does nothing in single arm control mode.                    
     **3**                 When in both arm control mode tucks the arms. Does nothing in single arm control mode.                      
     **7 (Triangle)**      Rotates the wrist or wrists counter-clockwise                                                               
     **10 (X)**            Rotates the wrist or wrists clockwise                                                                       
     **8 (Square)**        Closes the gripper or grippers                                                                              
     **9 (Circle)**        Opens the gripper or grippers                                                                               
     **rx+/-**             When arm or arms are in position control mode, move wrist forward/back                                      
     **ry+/-**             When arm or arms are in position control mode, move wrist right/left                                        
     **lx+/-**             When arm or arms are in position control mode, move wrist up/down                                           
  -- ------------------ -- ----------------------------------------------------------------------------------------------------------- --

## Keyboard control

This section will focus on the executable pr2_teleop_general_keyboard,
which allows robot control using the keyboard.

### Launching

There are three launch files which largely mirror the functionality
described for the joystick:

```
roslaunch pr2_teleop_general pr2_teleop_general_keyboard.launch
```

brings up arm ik and allows control of all modes

```
roslaunch pr2_teleop_general pr2_teleop_general_keyboard_noik.launch
```

does not bring up ik nodes, assuming they are running elsewhere.

```
roslaunch pr2_teleop_general pr2_teleop_general_keyboard_bodyhead_only.launch
```

allows control of only the body and the head.

### Interacting with the program

The program brings up text guides that describe the function of the
keys.

## ROS parameters for joystick and keyboard

As a convenience the joystick and keyboard programs implement largely
the same set of ROS parameters:

### Basic parameters

```clearsilver
param {
 no_header = True
  0.name=control_body
  0.default=`true`
  0.type= Boolean
  0.desc= Whether or not to permit control of the body
  1.name=control_head
  1.default=`true`
  1.type= Boolean
  1.desc= Whether or not to permit control of the head and sensors
  2.name=control_rarm
  2.default=`true`
  2.type= Boolean
  2.desc= Whether or not to permit control of the right arm 
  3.name=control_larm 
  3.default=`true`
  3.type= Boolean
  3.desc= Whether or not to permit control of the left arm
  4.name=control_prosilica
  4.default=`true`
  4.type= Boolean
  4.desc= Whether or not to permit control of the prosilica (in order to poll frames)
  5.name=arm_controller_name
  5.default=`"arm_controller"`
  5.type= string
  5.desc= The arm controller suffix that is used for arm position mode ("r_" or "l_" will prepend the suffix)
}
```

### Advanced parameters

There are many parameters offered by the modules that will generally not
need to be changed by the users. Here we list two of the most important.

```clearsilver
param {
 no_header = True 
  1.name=arm_controller_name
  1.default=`"arm_controller"`
  1.type= string
  1.desc= The arm controller suffix that is used for arm position mode ("r_" or "l_" will prepend the suffix)
  2.name=prosilica_namespace
  2.default=`"prosilica_polled"`
  2.type= string
  2.desc=The namespace to connect to the prosilica for the polling topic
}
```
