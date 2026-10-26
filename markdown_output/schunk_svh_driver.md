# Deprecated

This is the documentation for the deprecated, unsupported version of the
Schunk SVH driver. For the currently maintained version, please see the
[schunk_svh_ros_driver](http://wiki.ros.org/schunk_svh_ros_driver).

  -- ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- --
     [Youtube](https://www.youtube.com/watch?v=hPtSbPzROrs)                                                                                                                                      
     -The demonstration in the video was developed for the Schunk Expert Days and uses the reflexxxes library for interpolation. The SVH driver used is an early version of this repository-\|   
  -- ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- --

  -- --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- --
     <style="background-color: lightgrey;"> Info: The newest Version of this driver (v0.2.0 and above) will support the new hardware versions of the Schunk SVH (2.0 and above).   
  -- --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- --

## Overview

This package provides a way of controlling the
[Schunk Five Finger Hand](http://mobile.schunk-microsite.com/en/produkte/produkte/servoelektrische-5-finger-greifhand-svh.html).
It provides the driver for the low level interface and enables an easy
control of the hand via ROS [messages](Messages).

## Installation

If you just want to use the driver it is recommended to install it via
repository. All the required libraries are contained within the package.
The core driver for the SVH is independent of ros and can also be used
in other frameworks if you desire.

### Hardware Requirements

To use this package you will need a
[Schunk Five Finger Hand](http://mobile.schunk-microsite.com/de/produkte/produkte/servoelektrische-5-finger-greifhand-svh.html).
It communicates via RS485 protocol. Brainbox USB to Serial converter
have proven to work well with the hand and are usually delivered in
combination with the hand.

### Software Requirements

All required (non ROS) libraries are contained in the package and the
package is tested to work under Ubuntu Linux 12.04, 14.04 and 16.04 but
should have no problem to work in any Linux environment.

### From Repository

Install the package by calling: { }}}} { }}}} { }}}} { }}}} { }}}} the
package comes with udev rules that allow for an easy discovery of the
brainbox adapters. Install them by calling: 

```
rosrun schunk_svh_driver create_udev_rules
```


this will copy the udev rules to `/etc/udev/rules.d` and restart your
udev service.

### From Source

You will need to checkout the following packages into your workspace's
src directory:

- <https://github.com/fzi-forschungszentrum-informatik/fzi_icl_core>
- <https://github.com/fzi-forschungszentrum-informatik/fzi_icl_comm>
- <https://github.com/fzi-forschungszentrum-informatik/schunk_svh_driver>

then just call 

```
catkin_make_isolated
   source devel_isolated/setup.bash
```



If you have the fzi_icl_core or fzi_icl_comm package in your workspace
you'll have to build it with *catkin_make_isolated*, as those packages
are plain cmake packages. See the
[REP 134](http://www.ros.org/reps/rep-0134.html) for details.

The package comes with UDEV rules for the Brainbox USB to Serial adapter
to install these source your workspace and call the following:


```
rosrun schunk_svh_driver create_udev_rules
```

 which will copy the udev rules into
`/etc/udev/rules.d` and restart your udev service.

## ROS API



```clearsilver
name = svh_controller
desc = This node is interfacing with the Schunk Five Finger Hand and provides the ability to control the fingers and read out any feedback
sub {
  0.name = connect
  0.type = std_msgs/Empty
  0.desc = Tries to connect to the hardware when triggered. The hardware will use the `serial_device` that can be reconfigured via dynamic reconfigure
}
sub {
  1.name = reset_channel
  1.type = std_msgs/Int8
  1.desc = Triggers a reset of the given channel (finger). See channel mapping below.
  2.name = enable_channel
  2.type = std_msgs/Int8
  2.desc = Enables a given channel (finger). See channel mapping below.
  3.name = channel_targets
  3.type = sensor_msgs/JointState
  3.desc = Target position the channels (fingers) shall move to. Note that it has less performance to give targets for individual channels or a subset of the available DoF than providing it for all at once. If 8 channels are given instead of 9 the driver will send 8 packets instead of 1 which might influence serial device performance. Only the names and positions will be evaluated from the JointState message.
}
pub{
 0.name = channel_feedback
 0.type = sensor_msgs/JointState
 0.desc = Current position of the channels (fingers).
 1.name = channel_currents
 1.type = std_msgs/Float64MultiArray
 1.desc = Current currents of the channels (fingers).
 2.name = parameter_descriptions
 2.type = dynamic_reconfigure/ConfigDescription
 2.desc = Names, values and description of the current parameters
 3.name = parameter_descriptions
 3.type = dynamic_reconfigure/ConfigDescription
 3.desc = Names, min/max values and description of the parameters in general
 4.name = parameter_updates
 4.type = dynamic_reconfigure/Config
 4.desc = Names, values and description of the current parameters
}
param {
  0.name = ~autostart
  0.type = bool
  0.desc = If set to true the controller will immediately try to connect to the hardware and start a reset of all the channels (fingers)
  0.default = true
  1.name = ~serial_device
  1.type = string
  1.desc = Device handle to use for the serial communication, e.g /dev/ttyUSB0
  1.default = /dev/ttyUSB0
  2.name = ~disable_flags
  2.type = vector of bool
  2.desc = Indicates if a channel (finger) should be disabled. If disabled a finger will not be activated by the hardware but behaves as if everything was fine. This can be used in case a finger has a hardware failure.
  2.default = 9 x false
  3.name = ~reset_timeout
  3.type = int
  3.desc = Time in seconds after which a reset of a channel (finger) is aborted if the reset current threshold can not be reached. If a channel (finger) needs to reach 300mA for detection of a hard stop but is stuck at 200mA the reset is aborted after reset_timeout seconds.
  3.default = 5
  4.name = ~finger_reset_speed
  4.type = double
  4.desc = Dynamic reconfigure value. Speed of fingers during reset, given as percentage of their usual speed.
  4.default = 0.2
  5.name = /robot_description
  5.type = urdf model
  5.default = URDF at description/urdf/svh-standalone.urdf.xacro
  5.desc = Urdf model of the hand, including the joints and links describing the svh
  6.name = ~logging_config
  6.type = string
  6.desc = Path to the logging.xml file configuring the internal logging of the svh_driver library. If none is specified but the internal logging is enabled the output will be lost and warnings will be given.
  6.default = /etc/logging.xml 
  7.name = ~use_internal_logging
  7.type = bool
  7.desc = Actives the log output of the svh driver library. This uses a ROS Independent logging system providing deeper insight into whats happening. By Default the log files are stored in ~/.ros/log but the files can be specified by providing a new logging.xml.
  7.default = false
}
param {
  8.name = ~CHANNEL_NAME/position_controller
  8.type = vector of floats
  8.desc = Parameters used for the hardware position controller. See additional documentation in YAML files and below.  If no values are provides the controller will use safe internal defaults.
  8.default = see yaml files

  9.name = ~CHANNEL_NAME/current_controller
  9.type = vector of floats
  9.desc = Parameters used for the hardware current controller. See additional documentation in YAML files and below. If no values are provides the current will use safe internal defaults.
  9.default = see yaml files

  10.name = ~CHANNEL_NAME/home_settings
  10.type = vector of floats
  10.desc = Parameters used for the homing of the fingers providing soft stops and reset parameterization. See additional documentation in YAML files and below. If no values are provides the controller will use safe internal defaults.
  10.default = see yaml files
  11.name = ~VERSIONS_PARAMETER
  11.type = array
  11.desc = Array of parameters for all hardware versions and all joints. The values are read from the *.yaml files in the package's ''etc'' directory.
  11.default = Filled with values from the etc/controller_default.yaml file
}
```

 

```clearsilver
name = svh_sin_test
desc = this node is meant as a very very simple test program to show how to interface with the `svh_controller` and to check if the hardware works
sub {
  0.name = toggle_run
  0.type = std_msgs/Empty
  0.desc = If toggled by a message the node will start or stop outputting joint angles based on a sin.
  1.name = speed
  1.type = std_msgs/Float32
  1.desc = Sets the execution speed. The higher the number, the slower it is. Should not be smaller than 3.0.
  2.name = loop
  2.type = std_msgs/Float32
  2.desc = Sets the loop rate for the update interval. The greater the better.
}
pub{
 0.name = channel_targets
 0.type = sensor_msgs/JointState
 0.desc = Target position of the fingers for the svh_controller
}
```



## Additional API information

### Channel Mapping

The SVH has 9 degrees of freedom which are addressed as channels. Topics
that accept channels will use the following mapping:

  -- ------------------------ -- ------------ -- ---- ------------------------------------------------- --
     **Channel Name**            **Number**                                                             
     ALL                         -1              <   10> ![](attachment:svh_finger_description.png)   
     THUMB_FLEXION               0                                                                      
     THUMB_OPPOSITION            1                                                                      
     INDEX_FINGER_DISTAL         2                                                                      
     INDEX_FINGER_PROXIMAL       3                                                                      
     MIDDLE_FINGER_DISTAL        4                                                                      
     MIDDLE_FINGER_PROXIMAL      5                                                                      
     RING_FINGER                 6                                                                      
     PINKY                       7                                                                      
     FINGER_SPREAD               8                                                                      
  -- ------------------------ -- ------------ -- ---- ------------------------------------------------- --

### Parameter sets

Each finger is controlled by a cascade of position and current
controller (see additional Information if you are interested in that)
and has a set of homing settings. The individual settings are read via
parameter server addressing them via their hardware version and
CHANNEL_NAME which is stated in the section channel mapping. For
example: The settings of the Ring Finger would be searching for the
corresponding hardware version and the entry of RING_FINGER and so
forth.

When using the launch file `svh_controller.launch` all parameters are
read from yaml files residing in the folder *etc*. If you want to give
custom parameters just edit the file *etc/controller_user.yaml* if you
are using the source installation. In case of an installation from deb
you should first copy the file under *etc/controller_user.yaml* to a
folder with user write acces, make your changes and then use it by
adding the argument `controller_config:=path_to_your/logging.xml` when
launching the node.

If you want to go back to the original values (and have edited the file,
residing in etc) you can simply delete the file and copy the
*controller_default.yaml* to the name *controller_user.yaml* and start
again. If no *controller_user.yaml* file is present the values of the
default file will be used. If both files are missing or the node use
used without the launch file hardcoded default values that are safe will
be used.



```wiki
WARNING: These settings enable control of very low level concepts. Setting wrong values here may lead to permanent damage in the hardware. Especially the maximum allowed currents should not be exceeded. Consult the [[attachment:svh_hardware_information.pdf]] before you change things.
```



## Usage

The package is ready to be used as standalone package for fast testing
or in combination with other packages providing the target points for
the fingers. To test the package or your hardware we recommend that you
run the standalone version first and get familiar with the behavior of
the Hand.

In any case **you should use the provided launch script** as it sets up
many variables, the parameter sets and some additional packages that are
needed for correct operation and visualization.

### Hardware setup

Make sure the hand is connected to an appropriate power source and via a
USB to Serial adapter to your PC. You can check which adapters are
available with a quick: 

```
ls /dev
```

 where an entry like
/ttyUSB0 should be present. In case you have multiple adapters the
easiest way to check which one you are using is to disconnect the
adapter shortly and check which of the ttyUSBx devices is gone.

You can change the device used by adding the argument `serial_device`
to the launch calls, change it via dynamic reconfigure and then do a
reconnect or change it permanently by replacing the argument in the
launch file.

If no ttyUSBx device comes up, make sure you have installed the udev
rules correctly or if you are using any other hardware installed the
drivers according to their documentation.

If the power supply is not connected probably or the it delivers not
enough power the connection to the hand may have problems. This will
lead to a package loss during communication.

### Standalone usage

If you want to check out that everything is working or just want to move
the hand into any position you can use the package as standalone with
sliders.

Make sure the hardware is powered and can move freely and launch the
controller node by calling 

```
roslaunch schunk_svh_driver svh_controller.launch standalone:=true
```

 This will
automatically connect the driver to the hardware and call the reset
routine for all fingers. Upon the message: "Driver was autostarted!
Input can now be sent. Have a safe and productive day!" the hand is
ready and fingers can be moved by using the Joint State publisher gui
that has come up.

You can disable the autostart by adding the argument autostart:


```
roslaunch schunk_svh_driver svh_controller.launch standalone:=true autostart:=false
```



By using the `standalone` argument the launchfile will start a joint
state publisher for easy input. If you do not activate this as input you
have to provide the target positions by another node or console input.
The package folder comes with a file called "quick_commands" which
gives you some examples how to controll the hand via rostopic.

### Together with other packages

By default the node will await input from another node. To use the
svh_controller with your project **it is highly recommended that you
include it via its launch file** like this: 

```
<include file="$(find schunk_svh_driver)/launch/svh_controller.launch">
        <arg name="standalone" value="False" />
        <arg name="gui" value="False" />
  </include>
```

 The
argmuments are not strictly necessary as the values default to these.
This way of including the node may however be more than you want because
the launch script already contains things like a robot state publisher
etc. if you just want the node, but do not want to care about the config
files and so on you can use the very simple include file:


```
catkin_make_isolated
   source devel_isolated/setup.bash
```

0 again, fill out the arguments you need, the
rest will default to predefined values. If you use the svh_node.launch
file you will have to provide an "output joint state publisher" for
the joint states in order to generate the joint states required for the
URDF (note below). This option is only available from version 0.1.6 and
up (deb file install is 0.1.5).

If you just want to use the node without the configuration files, etc.
the node will default to hard-coded values.

**NOTE** The urdf of the node makes use of the `mimic` tag which is
currently only resolved by the robot joint state publisher. in order to
generate TFs for the visualization and to get the angles of the coupled
joints the node is used in conjunction with a joint state publisher and
a robot state publisher. If you include the node without these nodes the
TF tree will not be complete as the joints that use mimic are not
working. See the URDF section for details on joints, their naming and
relation.

### Visualisation

The node will automatically show the input sliders if started with the
standalone argument. If you additionally provide the `gui` argument as
true an rqt gui will be opened when launching the node:


```
catkin_make_isolated
   source devel_isolated/setup.bash
```

1

The `rqt` gui opens always to its default configuration (which is
usually the last one). The SVH comes with the plugin `SVH_Reset` which
enables easy reset control of the hand. Additionally you can use
dynamic_reconfigure to change some of the values and the RVIZ plugin to
visualize the robot model of the SVH. A configuration file for rviz is
provided with the package at "urdf/svh.rviz". Your configuration
should look something like this to access all GUI functionalities:

![](attachment:svh_rqt_gui.jpg)

### Simulation

If you do not want to use the actual hand you can simply start a
simulation of the hand by using: 

```
catkin_make_isolated
   source devel_isolated/setup.bash
```

2 as with the
real hardware you can choose to use the simulation (which is not really
a simulation but just a visualisation) with convenient sliders or with
the command line/ your own packages by using the `standalone`
argument: 

```
catkin_make_isolated
   source devel_isolated/setup.bash
```

3

**Note**: The SVH uses relative encoders that need a hard stop to reset.
Especially the finger spread however also contains springs that will
lead to a slightly different pose than commanded in real execution. So
please beware when you develop poses without the hardware in the loop.

### sin test

As a test to see if the hardware is properly working the very simple
test node `svh_sin_test` is provided. Make sure the hand can move
freely and run the test with: 

```
catkin_make_isolated
   source devel_isolated/setup.bash
```

4 after all
fingers are reset all fingers except the thumb will perform a sinus like
motion. You can stop/start the motion execution by sending:


```
catkin_make_isolated
   source devel_isolated/setup.bash
```

5 During execution the driver will output
warnings like this: 

```
catkin_make_isolated
   source devel_isolated/setup.bash
```

6 this is perfectly normal
as the sin test tries to drive the fingers to positions outside of the
soft stops.

Note that the node is just intended to allow a quick function test of
the hardware or a simple example of how to interface with the controller
node.

### Additional usage information

In case you do not use the autostart feature of the controller you will
have to connect and start the controller manually. You should do this by
using the `SVH_Reset` plugin provided with the package. When the
hardware is ready press the connect button. Afterwards you can either
reset all or individual fingers by pressing reset. The fingers will be
disabled after start but are automatically enabled once a target
position is set.

If you prefer to use the command line to send topics, some predefined
test inputs are stored in the "quick_commands" file for convenience.
Just copy and paste them to the command line.

### Argument Listing

The following arguments are possible for the main launch file and can be
mixed freely (most are just passed to the parameters of the node):

*gui (default: true)* Autostarts an rqt gui if set to true *autostart
(default: true)* Immediately connect to the hardware and reset the
fingers upon start if set to true *serial_device (default:
/dev/ttyUSB0)* Sets the serial device to use for the connection
*simulation (default: false)* Only starts the visualization part of the
SVH and no driver node if set to true. *logging_config (default:
schunk_svh_driver/etc/logging.xml)* Full qualified path to the location
of the logging.xml. The file is used to configure the output of the
internal logging framework *use_internal_logging (default: false)* If
set to true the log output (DEBUG and TRACE) of the SVH driver will be
written to the location specified by the logging.xml (/.ros/log by
default) *controller_config (default:
schunk_svh_driver/etc/controller_user.yaml)* Full qualified path to a
yaml file containing the configuration for the low level controllers.
Copy the file in "schunk_svh_driver/etc/controller_user.yaml" for this
purpose *general_config (default: schunk_svh_driver/etc/svh.yaml)* Full
qualified path to a yaml file containing the basic configuration of the
ros node, mainly which finger is disabled. Copy the file in
"schunk_svh_driver/etc/svh.yaml" for this purpose *standalone
(default: false)* Indicates that the controller should be used with
direct human input when set to true

## Troubleshooting

*After an autostart (default setting) of the software the fingers do not
begin to move* The autostart tries to connect to the hand and run and
autostart immediately. Check the output of the driver. After a
successful connect it should read: 

```
catkin_make_isolated
   source devel_isolated/setup.bash
```

7 If the
driver states: 

```
catkin_make_isolated
   source devel_isolated/setup.bash
```

8 the serial device could not ne
opened. Check that you have installed the udev rules and that the device
shows up as /dev/ttyUSBx when you connect it *After an autostart of the
software it says **Send packages = 28, received packages = 20** or
something similar* In this case the device could be opened but the
connection has quality issues and loses packets. You can try to connect
again using the connect button of the plugin or the connect topic. The
problem most likely stems from a bad connection (to long cables, bad
connectors) or in rare cases from to little processing power on the
executing hardware (which is not able to keep up with the data rate of
the connection) *During reset of the fingers it states **Driving channel
5 to hard stop. Detection thresholds: Current MIN: -500.000000mA MAX:
500.000000mA** or similar and nothing is happening* During reset the
fingers need to reach a certain percentage of the maximum allowed
current to detect a hard stop. The amount is configured in the homing
settings by the "reset current factor" which you can find in the
\*.yaml files in the *etc* folder. If for example the finger is supposed
to reach 400mA but is stuck and only manages to get up to 200mA the
threshold will not be reached. In such cases the reset timeout should
abort the timeout after the amount of seconds specified. However the
timeout is only active once there is no measurable difference in
current. In case the current changes a little bit but does not reach the
threshold it will be in an infinite loop. In this (rare) case stop the
driver execution, maybe restart the hardware, and set a lower reset
current factor. *During reset the finger stops as soon as it touches any
resistance and is initialized in an odd position* In this case the value
for the reset current factor and/or the overall allowed current for the
motor controller is set to low. As state above the hard stop is based on
a current threshold. If this threshold is very low even small
disturbances can be detected as hard stop. Also if the finger is not
strong enough to overcome the disturbances the current will rise up to
the maximum allowed current. If it still can not overcome the
disturbance most likely a reset is detected. Please make sure that no
hardware fault is present in case this happens with high enough currents
*The fingers work but they "run away" when they do fast movements or
touch something and can not be controlled afterwards* This is the case
when the current peaks commanded to the current controller are to high.
The internal driver units will detect overcurrent/voltage and shut down
leaving the finger in an odd state. You can reset the finger manually
and resume operation, however this is an indication that your current
controller parameters are not right. As a general direction: Choose a
low P value and a higher I value as the current controller will try to
negate an error in the desired current. In case the error changes
suddenly a high P gain leads to a very output for the motor drivers
resulting in this case. Setting the controllers right is not easy, if
you are uncertain what to set just use the default settings *A finger is
broken, can i still use the rest of the finger?* YES! You can disable
the finger by editing the "etc/svh.yaml" file or by copying it and
then providing it via launch argument. Change the "disable_flags"
value of the finger you want to disable to true and it will not be used
during execution. However all calls to this finger will be answered in
the most positive way possible (i.e. it will register as enabled and
homed) *The plugin does not show in rqt, or a failure occurs during
loading* Try resetting the cache of `rqt` by calling `rqt
\--clear-config` and then try again *The hand gets very hot* There are
many motors and electronic circuits on a very small space. A quite high
temperature is nothing to worry about. You should however still be able
to touch everything. Otherwise you should check for a hardware fault
*RVIZ shows nothing like the screenshot when i load it* You need to
configure it yourself to show the robot model and maybe the TF tree or
use the provided config file at "etc/urdf.rviz" *When i start the node
with rosrun the URDF tree of a robot state publisher is not complete* We
used the mimic tag to model the chained kinematic of the fingers. The
mimic tag however is only evaluated by the joint state publisher. In the
launch file of the controller you can see how you can use the joint
state publisher just for the purpose of providing the values for these
mimicked joints *Where is the actual functionality within the ROS
package? It hardly seems to do anything* The actual driver was developed
as a standalone library which is then used by the SVHNode to control the
functionality. Take a look at the "driver_svh" folder which is also
contained in the src folder.

### Getting Help

If the troubleshooting did not answer your questions you can ask the
community via or contact the support offered by FZI on behalf of Schunk
at svh-support AT fzi DOT de

\-\-\-\--

## Additional information

Information provided here is meant for developers that want to use the
driver in a very specific way or extend it.

### URDF

The following illustration shows where the individual joints are located
within the kinematic model of the hand and how the connected finger
segments are scaled in respect to these joints. The mimic joints will
always have the joint angle of the joint they mimic times the scaling
factor that is stated for each joint ![](attachment:svh_joint_names.png)
The links in the URDF contain many helper and dummy links that are
needed to create the quite complex kinematic chain why the following
illustration of the links is only partially accurate. Especially the
links names "e" are mostly virtual and really in one place. Also the
base link is actually further in the back than drawn in the picture. Due
to the limitations of 2D we could not accurately illustrate this:
![](attachment:svh_link_names.png) For proper illustration of the robot
model simplified collada files where created out of the original CAD
data of the SVH. The following picture shows which part corresponds to a
file name: ![](attachment:svh_dae_filenames.png)

### Kinematic dependencies and ranges

The following indicates the maximum angles (from wich the scaling for
the svh driver was calculated): ![](attachment:svh_kinematic_ranges.jpg)
The joint names correspond to the ones seen in this kinematic
description ![](attachment:svh_kinematic_dependencies.jpg)
![](attachment:svh_overall_measurements.jpg)

### Additional Documents

- low level protocol information used to communicate with the SVH
  <attachment:svh_protocol_specification.pdf>
- Hardware specifications (i.e. max motor
  currents)<attachment:svh_hardware_information.pdf>
- Controller specifications (low level information)
  <attachment:svh_controller_description.pdf>
