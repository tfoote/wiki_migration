Note: before moving the robot base, you may want to
[tuck the arms out of the way](https://index.ros.org/p/pr2_tuckarm).

## Bring up the robot

As with all applications, you must first
[bring up your robot](https://index.ros.org/p/pr2_apps).

## Joystick teleoperation

The PR2 is equipped with a Playstation3 (PS3) controller.

### Pairing

Before use, the PS3 controller must be "paired" with the robot. If
your controller is not already paired, you can pair it by pressing the
center button, shown in the image. If you need to pair a new PS3
controller to the PR2 (i.e. not the controller that came with it), see
[the tutorials](#tutorials).

There is currently no feedback from the controller or the robot during
or after pairing. The best way to tell if they have been paired
correctly is to try issuing commands to the robot via the joystick as
described below.

[![attachment:pairing.png](doc/pairing.png)](doc/pairing.png)

### Launching

Launch joystick teleop: 

```
roslaunch pr2_teleop teleop_joystick.launch
```



Now you should be able to control the robot's base and spine with its
PS3 controller.

### Controlling

![attachment:ps3joy_buttons.png](doc/ps3joy_buttons.png)
![ps3 joystick diagram](doc/ps3diagram.png)

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
     **L1**               The "deadman" control allows the joystick to send commands to the robot; the robot will only respond to the joystick when this button is held down   
     **L2**               The "head" button allows the sticks to control the head instead of the base                                                                          
     **Left stick**       Rotate (yaw) the base                                                                                                                                  
     **Right stick**      Move (translate) the base                                                                                                                              
     **Triangle**         Move the torso up                                                                                                                                      
     **X**                Move the torso down                                                                                                                                    
     **R1**               The "run" button commands the base to drive faster                                                                                                   
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

Launch keyboard teleop: 

```
roslaunch pr2_teleop teleop_keyboard.launch
```

 Now you should be able
to control the robot base with keyboard commands in the shell where you
ran the above [roslaunch](https://index.ros.org/p/roslaunch) command.

### Control

The keys that you can use, and what they do, are displayed to the
screen.

## Tutorials

- [Pairing the PR2 with a New PS3 Joystick](#pairing-the-pr2-with-a-new-ps3-joystick):
  Instructions for pairing the PR2 to a new PS3 joystick.

## Pairing the PR2 with a New PS3 Joystick

- **Description:** Instructions for pairing the PR2 to a new PS3
  joystick.
- **Keywords:** teleop ps3
- **Tutorial Level:** ADVANCED

### Find the PR2's Bluetooth MAC Address

The first step is to find the PR2's bluetooth MAC address. The key step
here is that it is **c2** that has bluetooth:



```
ssh c2
hciconfig
```



You should see output something like:



```
$  hciconfig
hci0:	Type: USB
	BD Address: 00:1B:DC:00:06:F8 ACL MTU: 310:10 SCO MTU: 64:8
	UP RUNNING PSCAN 
	RX bytes:647476598 acl:11163343 sco:0 events:560 errors:0
	TX bytes:5862 acl:262 sco:0 commands:137 errors:0
```



The MAC address is listed after BD Address. In this example it is
00:1B:DC:00:06:F8.

If this doesn't work, you can try:



```
sudo hciconfig hci0 up
hciconfig
```



If that still does not work, doublecheck that you are running on c2 not
c1.

### Set the Joystick's Bluetooth Master

Using the microUSB cable, plug the joystick into any computer running
ROS for which you have sudo. Set the joystick's Bluetooth master to the
PR2's MAC address using:



```
roscd ps3joy
sudo ./bin/sixpair <MAC Address>
```



You should see output like:



```
Current Bluetooth master: 00:02:76:2a:20:71
Setting master bd_addr to 00:1b:dc:00:06:f8
```



### Pair the Joystick and PR2

Unplug the joystick from the computer. The PR2 automatically runs
ps3joy.py so you should not have to start that. Instead simply start the
robot: 

```
robot start
```

 And then launch pr2_teleop


```
roslaunch pr2_teleop telop_joystick.launch
```

 Press the center button of the joystick to pair
it with the PR2. You should now be able to control the PR2 using the new
joystick.

### More Information

For more information, see the [ps3joy](https://index.ros.org/p/ps3joy)
package. Pairing a new PS3 joystick with the PR2 is similar to
[pairing the joystick to a computer with one USB](https://index.ros.org/p/ps3joy).

When following any tutorials about bluetooth on the PR2, remember:

1\. Bluetooth is on c2 not c1 2. The PR2 starts ps3joy.py when it boots.
If you try the command 

```
rosrun ps3joy ps3joy.py
```

 you will see an error
about the process already running. There was apparently a problem with
Karmic that would also give this error, but make sure you have killed
any previous ps3joy process before trying those fixes:


```
ps -A|grep ps3joy
```
