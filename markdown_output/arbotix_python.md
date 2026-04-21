## Overview

The arbotix_python package provides a basic ROS interface to an
[ArbotiX RoboController](http://www.trossenrobotics.com/p/arbotix-robot-controller.aspx)
over a USB serial connection, or XBEE wireless radios.

This package consists of three tools: the driver, a GUI for interacting
with the driver, and a terminal tool for setting up your servos.

## Driver Node

```clearsilver
name=driver.py
desc=Interface to an ArbotiX !RoboController. 
pub {
  0.name=/joint_states
  0.type = sensor_msgs/JointState
  0.desc = Servo position feedback. Servo meta-information must be configured via parameters. 
}
sub {
  0.name=<servo>/command
  0.type = std_msgs/Float64
  0.desc = Commanded position to move servo to, in radians.
}
srv {
  3.name = <servo>/relax
  3.type = arbotix_msgs/Relax
  3.desc = Relax servo (turn off torque) until next command is sent. 
}
param {
  0.name = ~port
  0.type = str
  0.desc = Name of port to use.
  0.default = /dev/ttyUSB0
  1.name = ~baud
  1.type = int
  1.desc = Baud rate, in bps.
  1.default = 115200
  2.name = ~rate
  2.type = int
  2.desc = Rate at which to run main loop. 
  2.default = 100
  3.name = ~read_rate
  3.type = float
  3.desc = Rate at which to read servos and publish joint_states topic. 
  3.default = 10
  4.name = ~write_rate
  4.type = float
  4.desc = Rate at which to write command updates to servo. 
  4.default = 10
  5.name = ~sync_read
  5.type = boolean
  5.desc = Whether to use sync_read or not. Must be disabled when using hardware such as a USB2Dynamixel.
  5.default = True
  6.name = ~sync_write
  6.type = boolean
  6.desc = Whether to use sync_write or not. 
  6.default = True
  7.name = ~dynamixels/<servo>/id
  7.type = str
  7.desc = Dynamixel ID for servo.
  8.name = ~dynamixels/<servo>/neutral
  8.type = int
  8.desc = Neutral position for servo.
  8.default = 512
  9.name = ~dynamixels/<servo>/range
  9.type = float
  9.desc = Range of servo, in degrees. 
  9.default = 300.0
  10.name = ~dynamixels/<servo>/ticks
  10.type = int
  10.desc = Number of ticks, for EX-106s, you would pass in 4096, other servos likely won't need this altered.
  10.default = 1024
  11.name = ~dynamixels/<servo>/min_angle
  11.type = float
  11.desc = Minimum angle in degrees.
  11.default = -150.0
  12.name = ~dynamixels/<servo>/max_angle
  12.type = float
  12.desc = Maximum angle in degrees.
  12.default = 150.0
  13.name = ~dynamixels/<servo>/max_speed
  13.type = float
  13.desc = Maximum speed in degrees/sec.
  13.default = 684.0
  14.name = ~dynamixels/<servo>/invert
  14.type = boolean
  14.desc = Whether to invert servo rotation or not.
  14.default = false
  15.name = ~dynamixels/<servo>/readable
  15.type = boolean
  15.value = Whether servo should be queried for position when doing joint_state update. If false, last commanded position is used for joint_state publications.
  15.default = true
}
```

### Submodules

The \`arbotix_python\` package also offers several controllers which add
higher-level interfaces to common hardware. These include:

-   [diff_controller](arbotix_python/diff_controller) - A controller for
    a differential drive base.
-   [follow_controller](arbotix_python/follow_controller) - A controller
    offering a \`control_msgs/FollowJointTrajectoryAction\` input.

This package also offers complete access to the digital and analog IO on
the ArbotiX:

-   [io channels](arbotix_python/io) - for streaming digital and analog
    inputs and outputs.

### Configuration

Because of the complexity of the parameters, the easiest way to
configure the ArbotiX node is via a YAML file. For example, a simple
robot with a differential drive base and a pan and tilt head (with a
follow_controller) might look like:

```
port: /dev/ttyUSB1
rate: 15
dynamixels: {
    head_pan_joint: {id: 1, invert: true},
    head_tilt_joint: {id: 2, max_angle: 100, min_angle: -100}
}
controllers: {
  head_controller: {type: follow_controller, joints: [head_pan_joint, head_tilt_joint], action_name: head_controller/follow_joint_trajectory },
  base_controller: {type: diff_controller, base_width: 0.140, ticks_meter: 26145 }
}
```

If you saved such a YAML file in a package you have created, you could
then start the ArbotiX node using a launch file such as:

```
<launch>
  <node name="arbotix" pkg="arbotix_python" type="driver.py" output="screen">
    <rosparam file="$(find your_package)/default.yaml" command="load" />
  </node>
</launch>
```

## ControllerGUI

The ControllerGUI is a test/teleop node that allows you to control a
mobile base and/or your Dynamixel servos. The ControllerGUI publishes
geometry_msgs/Twist commands to the *cmd_vel* topic, and commands to
individual servos. It will automatically determine the names and limits
of your servos from your YAML specification file. Launching the
ControllerGUI is as easy as: ```
rosrun arbotix_python controllerGUI.py
``` You should then
see a window like:

![](attachment:controllerGUI.png)

Moving the red dot up drives the robot forward, moving left/right turns
in place, etc. The slider bars move servos, but must be checked to be
enabled. When not enabled, they will be updated with the values of the
last joint_states message, so that when enabled they will not *snap* to
a position, but just torque-on in place. In the above image, only
head_pan and head_tilt are enabled.

## Terminal

Working with Dynamixel servos often requires some setup of the servos
themselves. This is made easy with the ArbotiX terminal tool. The
terminal works like a typical Linux terminal, you can type \`ls\` to
query which servos are attached, \`mv 1 2\` will \`move\` the servo with
ID 1 to an ID of 2, etc:

```
$ rosrun arbotix_python terminal.py 
ArbotiX Terminal --- Version 0.1
Copyright 2011 Vanadium Labs LLC
>>  ls
   1 .... .... .... .... .... .... .... .... 
.... .... .... .... .... .... .... .... .... 
>>  mv 1 2
OK
>>  ls
....    2 .... .... .... .... .... .... .... 
.... .... .... .... .... .... .... .... ....
```

The terminal has several other commands. Typing \`help\` will list all
commands: ```
>>  help
ArbotiX Terminal V0.1

valid commands:
 ls - list the servos found on the bus. 
 mv id id2 - rename any servo with ID=id, to id2
 baud b - set baud rate of bus to b
 get param id - get a parameter value from a servo
 set param id val - set parameter on servo ID=id to val

valid parameters
 pos - current position of a servo, 0-1023
 baud - baud rate
 temp - current temperature, degrees C, READ ONLY
```
