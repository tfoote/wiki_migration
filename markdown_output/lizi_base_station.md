```wiki
'''Note:''' This stack is designed for robots purchased before June 2014. 
For new robots, see the [[robotican|robotican]] stack.
```

## Preliminary Setup

You must complete the
[Network setup for controlling the Lizi robots from a remote machine](lizi_robot/Tutorials/Network setup for controlling the Lizi robots from a remote machine)
tutorial before using this package.

The base station computer should have the entire lizi_robot meta-package
built. You should also answer \'y\' (yes) to all steps of the setup.sh
file (see the
[Lizi robot installation](lizi_robot/Tutorials/Lizi robot installation)
tutorial)

In order to use the joystick control node one should also install the
joystick-drivers package. ```
$ sudo apt-get install ros-hydro-joystick-drivers
```

## Launching the Lizi robots

For the following examples we assume we have two Lizi robots with id\'s
1 and 2 with IP addresses 192.168.0.101 and 192.168.0.102 respectively.
The base station computer IP address is 192.168.0.100. One can use any
other IP addresses.

First, we will edit the
lizi_robot/lizi_base_station/launch/base_station.launch file to match
the above Lizi robots addresses: ```shell
<machine name="lizi1" address="192.168.0.101" user="lizi" password="a" env-loader="~/catkin_ws/src/lizi_robot/lizi/config/lizi_env.sh" default="true"/>

<group ns="lizi_1">
   <include file="$(find lizi_base_station)/launch/remote_lizi.launch">
   <arg name="id" value="1" />
   </include>
</group>


<machine name="lizi2" address="192.168.0.102" user="lizi" password="a" env-loader="~/catkin_ws/src/lizi_robot/lizi/config/lizi_env.sh" default="true"/>

<group ns="lizi_2">
   <include file="$(find lizi_base_station)/launch/remote_lizi.launch">
   <arg name="id" value="2" />
   </include>
</group>
```

Make sure that the \<machine/\> parameters are all correct according to
your network setup and to the specific robot computer username and
password. Note that from the factory the default username is \"lizi\"
and password is \"a\". .

In order to select exactly what will be launched on the lizi robots, see
the lizi_robot/lizi_base_station/launch/remote_lizi.launch file.

Set the following parameters according to the base station IP address:
```
$ export ROS_MASTER_URI="http://192.168.0.100:11311"
$ export ROS_IP="192.168.0.100"
$ export ROSLAUNCH_SSH_UNKNOWN=1
```

Finally, launch the base_station.launch file: ```
$ roslaunch lizi_base_station base_station.launch
```

If you have any problems during the launch, check your network setup.

Now you can control all the Lizi robots, try printing the current topics
to check that everything is ok: ```
$ rostopic list
```

## Controlling the Lizi robots

One can use the multi_lizi_control node to control multiple Lizi robots
from a single joystick.

The lizi_robot/lizi_base_station/launch/base_station.launch is used to
launch the required parameters and start the node.

You will have to figure out your joystick port and the id numbers of
joystick axes and buttons. To do so, type: ```
$ ls /dev/input
``` and
find the joystick port name (usually /dev/input/js0).

Now run: ```
$ sudo jstest /dev/input/js0
``` Play with joystick sticks and buttons
and write down the numbers of the axes which you would like to control
the drive and the axes to control the pan-tilt system. You should also
choose a button for switching between Lizi robots.

Edit the base_station.launch to match the joystick port.

Now, edit the lizi_robot/lizi_base_station/config/base_station.yaml
file:

lizi_n: 2 \# The number of Lizi robots

joy_for: 3 \# Axis for forward motion.

joy_rot: 2 \# Axis for rotation motion.

joy_pan: 0 \# Axis for pan control.

joy_tilt: 1 \# Axis for tilt control.

joy_scroll_btn: 5 \# button for switching between Lizi robots.

joy_slow_btn: 4 \# button for switching slow mode (half of max_vel).

joy_center_btn: 6 \# button for centering pan tilt system.

max_vel: 1.0 \# Maximum forward velocity (m/s)

max_rot: 3.0 \# Maximum rotation velocity (rad/s)

max_pan: 0.6 \# Maximum pan angle (+- rad)

max_tilt: 0.5 \# Maximum tilt angle (+- rad)

The above numbers are suitable for a logitech usb joystick. Use
*joy_for: 4* and *joy_rot: 3* for Xbox 360 Controller.

Launching the base_station.launch file can be done manually:
```
$ roslaunch lizi_base_station multi_lizi_control.launch
``` or as a part of the base_station.launch:
```
<include file="$(find lizi_base_station)/launch/multi_lizi_control.launch"/>
```

Now you can manually drive and operate the pan-tilt system of all the
Lizi robots.

You can watch the robots cameras and sensors using rqt.

Have fun!
