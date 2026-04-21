Please contact aleeper\<at\>stanford.edu with questions/feedback. If you
find something unclear in the documentation, feel free to ask, or if you
figure it out, contribute!

TODO: Most of this stuff should be moved into a tutorial\...

## Video

[Youtube](https://www.youtube.com/watch?v=xY3cnMdjbow)

## Bring up the robot

As with all applications, you must first
[bring up your robot](pr2_apps#bringup).

## Joystick Configuration

The package currently supports two interfaces: a Sony PS3 \"Sixaxis\"
Controller, and a 3Dconnexion \"Spacenav\" device.

To configure a Sixaxis device, follow the steps in
[ps3joy](ps3joy/Tutorials/PairingJoystickAndBluetoothDongle#Pairing) to
pair it with your computer.

To configure a Spacenav device, follow the instructions in
[spacenav_node](spacenav_node/Tutorials/UsingTheSpacenavNode)

## Launching

There are two launch files: one which should be run on the robot, and
one which should be run locally.

On the robot:

```
roslaunch pr2_remote_teleop launch_on_robot.launch
``` On a local computer:

```
roslaunch pr2_remote_teleop sixaxis_teleop.launch
*** or ***
roslaunch pr2_remote_teleop spacenav_teleop.launch
```

## Controlling with a PS3 Joystick

The pr2_remote_teleop package supports the ps3 sixaxis controller. The
control scheme below is the default one; any of these controls can be
easily modified by editing the config file in config/sixaxis.yaml.

NOTE that the \"select\" and \"start\" buttons act as a controller
suppress, that is, to change between controllers or camera views, hold
down start or select FIRST, then press the accompanying button
selection, then release start/select.

### Selecting camera views and robot controllers

To select the active a camera view (the affects which frame is used when
controlling the arms):

  -- ----------------------- -- ----------------------------------- --
     **Select + Triangle**      View the wide-angle head camera     
     **Select + X **            View the narrow-angle head camera   
     **Select + Square**        View the left forearm camera        
     **Select + Circle**        View the right forearm camera       
  -- ----------------------- -- ----------------------------------- --

To start controlling a part of the robot:

  -- ----------------------- -- ------------------------------------- --
     **Start + Pad-Up**         Start the head controller             
     **Start + Pad-Down **      Start the base and torso controller   
     **Start + Pad-Left**       Start the left arm controller         
     **Start + Pad-Right**      Start the right arm controller        
  -- ----------------------- -- ------------------------------------- --

### Head Controller

With the head controller active, the controls are as follows:

  -- -------------------- -- ------------------------------------------------------------- --
     **Left Joystick**       Pan the head left and right                                   
     **Right Joystick**      Tilt head forward and backward                                
     **Square**              Have the head look at and follow the left gripper position    
     **Circle**              Have the head look at and follow the right gripper position   
     **Triangle**            Center the head                                               
     **X**                   Toggle the red texture projector on/off                       
  -- -------------------- -- ------------------------------------------------------------- --

### Base Controller

With the base controller active, the controls are as follows:
\|\|**L1**\|\| \"Deadman switch,\" you must hold this down to issue any
commands to the base.

  -- -------------------- -- -------------------------------------------------- --
     **Left Joystick**       Translate the robot forward-backward, left-right   
     **Right Joystick**      Change the robot\'s orientation left-right         
     **Triangle**            Move the torso up                                  
     **X**                   Move the torso down                                
  -- -------------------- -- -------------------------------------------------- --

### Arm Controller

The arms are controlled using a cartesian controller to command position
and orientation of the gripper, specifically, the gripper finger tips.
It is useful to understand the frames used to control the gripper:

-   Translation is controlled in a frame parallel to the ground, but
    aligned so that \"forward\" aligns with the current camera view (but
    parallel to the ground).
-   Rotation is controlled in the gripper\'s local frame; roll, pitch,
    and yaw have the same local effect no matter the current position of
    the arm.

With the (left or right) arm controller active, the controls are as
follows:

  -- -------------------- -- ------------------------------------------------------------------------------------------------------------------- --
     **Left Joystick**       Moves the gripper forward-backward, left-right in the plane parallel to the ground.                                 
     **L1, L2**              Moves the gripper up (L1) and down (L2) vertically.                                                                 
     **Right Joystick**      Pivots the gripper about the finger tips. Up-down control the pitch, and left-right control the yaw (or heading).   
     **R1, R2**              Rolls the gripper wrist clockwise (R2) and counter-clockwise (R1).                                                  
     **Circle**              Opens the gripper while the button is held.                                                                         
     **Square**              Closes the gripper while the button is held.                                                                        
  -- -------------------- -- ------------------------------------------------------------------------------------------------------------------- --

### Unpairing the Joystick

The joystick should unpair from the PR2 automatically after 15 minutes
of inactivity, to save battery life. If you ever need to unpair the
joystick explicitly, simply press the pairing button for 10 seconds,
after which the joystick lights should stop blinking.

## Controlling with a Spacenav

  -- ------------------ -- ------------------------------------------------------------------------------------ --
     \<#FFFF00\> TODO      This will be generalized so that the keyboard keys can be re-assigned by the user.   
  -- ------------------ -- ------------------------------------------------------------------------------------ --

The spacenav has 6 axes of proportional control, and two buttons. These
are mapped to the various functions depending on the active control
mode, which is selected using the keyboard according to the table below.

  -- -------------------------------- -- ----------------------------------------------------------------- --
     **General**                                                                                           
     h                                   Prints help to the terminal                                       
     **Set Active Controller**                                                                             
     , (comma)                           left arm                                                          
     . (period)                          right arm                                                         
     a                                   base/torso                                                        
     q                                   head manual control                                               
     e                                   head follows active gripper                                       
     V                                   rviz camera control (the frame is /rviz_viewpoint )               
     **Arm Control Mode**                                                                                  
     space                               position control                                                  
     m                                   rotation control                                                  
     c                                   6-dof control, best for \"flying\" the gripper like an airplane   
     **Frame Control Policy**            The frame of reference for input commands.                        
     z                                   Active camera frame                                               
     x                                   Torso lift frame                                                  
     v                                   Active camera frame projected to be parallel to the ground        
     **Select active camera frame**                                                                        
     1                                   left forearm camera                                               
     2                                   wide stereo camera                                                
     3                                   right forearm camera                                              
     w                                   narrow stereo camera                                              
     \(4\)                               r_gripper_stereo camera, if available                             
  -- -------------------------------- -- ----------------------------------------------------------------- --

## Keyboard teleoperation

TODO :)
