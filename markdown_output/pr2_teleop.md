Note: before moving the robot base, you may want to
[tuck the arms out of the way](pr2_tuckarm).

## Bring up the robot

As with all applications, you must first
[bring up your robot](pr2_apps#bringup).

## Joystick teleoperation

The PR2 is equipped with a Playstation3 (PS3) controller.

### Pairing

Before use, the PS3 controller must be \"paired\" with the robot. If
your controller is not already paired, you can pair it by pressing the
center button, shown in the image. If you need to pair a new PS3
controller to the PR2 (i.e. not the controller that came with it), see
[the tutorials](pr2_teleop/Tutorials).

There is currently no feedback from the controller or the robot during
or after pairing. The best way to tell if they have been paired
correctly is to try issuing commands to the robot via the joystick as
described below.

[ {{attachment:pairing.png}}](attachment:pairing.png )

### Launching

Launch joystick teleop: ```
roslaunch pr2_teleop teleop_joystick.launch
```

Now you should be able to control the robot\'s base and spine with its
PS3 controller.

### Controlling

![](attachment:ps3joy_buttons.png)
![ps3 joystick diagram\|width=700](attachment:ps3diagram.png)

#### Moving the Base

To drive the robot around (i.e., drive the base), hold down L1 and use
the two joysticks to control its direction of movement (right joystick)
and rotation (left joystick). To drive the robot around at faster
speeds, also hold down R1.

#### Moving the Head

To move the robot head, hold down L1 and L2 and use the two joysticks to
control the head movements.

#### Moving the Torso

To move the robot torso, hold down L1 and press the triangle button to
move the torso up or the X button to move the torso down. The torso
moves slowly.

#### Controller Buttons

Control is configured as follows:

  -- ----------------- -- ------------------------------------------------------------------------------------------------------------------------------------------------------ --
     **Button**           **Control Action**                                                                                                                                     
     **L1**               The \"deadman\" control allows the joystick to send commands to the robot; the robot will only respond to the joystick when this button is held down   
     **L2**               The \"head\" button allows the sticks to control the head instead of the base                                                                          
     **Left stick**       Rotate (yaw) the base                                                                                                                                  
     **Right stick**      Move (translate) the base                                                                                                                              
     **Triangle**         Move the torso up                                                                                                                                      
     **X**                Move the torso down                                                                                                                                    
     **R1**               The \"run\" button commands the base to drive faster                                                                                                   
     **Circle**           Open right gripper                                                                                                                                     
     **Square**           Close right gripper                                                                                                                                    
     **D-pad right**      Open left gripper                                                                                                                                      
     **D-pad left**       Close left gripper                                                                                                                                     
  -- ----------------- -- ------------------------------------------------------------------------------------------------------------------------------------------------------ --

Note: The **L1**, **L2**, **R1**, and **R2** buttons are all labeled on
the controller.

### Unpairing the Joystick

The joystick should unpair from the PR2 automatically after 15 minutes
of inactivity, to save battery life. If you ever need to unpair the
joystick explicitly, simply press the pairing button for 10 seconds,
after which the joystick lights should stop blinking.

## Keyboard teleoperation

The robot base can be controlled via keyboard commands.

### Launching

Launch keyboard teleop: ```
roslaunch pr2_teleop teleop_keyboard.launch
``` Now you should be able
to control the robot base with keyboard commands in the shell where you
ran the above [roslaunch](roslaunch) command.

### Control

The keys that you can use, and what they do, are displayed to the
screen.
