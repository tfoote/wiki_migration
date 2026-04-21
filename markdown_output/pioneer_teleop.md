# Pioneer_teleop

A ROS package providing scripts for teleoperation using keyboard,
sockets and command line.

The package is compatible with any robot using ROS ecosystem, but is
originally implemented for Adept MobileRobots Pioneer and
Pioneer-compatible robots (Including Pioneer 2, Pioneer 3, Pioneer LX,
AmigoBot, PeopleBot, PatrolBot, PowerBot, Seekur and Seekur Jr.).

In case you have a different robot, please read
[\|What if my robot is not Pionner-compatible?](http://wiki.ros.org/pioneer_teleop#What_if_my_robot_is_not_Pionner-compatible)
section

\<\<GitHubIssues(amineHorseman/pioneer_teleop)\>\>

# Dependencies

You need first to get and install
[pioneer_bringup](http://wiki.ros.org/pioneer_bringup) package

# Installation

After installing the dependencies, download or clone this repository in
your caktin workspace:

```
cd ~/catkin_ws/src
git clone https://github.com/amineHorseman/pioneer_teleop.git
rosdep install pioneer_teleop
```

Build your workspace:

{{ cd /catkin_ws catkin_make }}}

Now, make sure that python scripts are executable:

```
cd ~/catkin_ws/src/pioneer_teleop/nodes
sudo chmod +x *.py
```

# Usage

In this package, there are 3 teleoperation modes:

## Keyboard teleoperation

```
roslaunch pioneer_teleop keyboard_teleop.launch
```

This allow you to control the robot motors using keyboard arrows, use +
and - to increase or decrease the speed, and s to stop

A different version of keyboard teleoperation is also available using
this command:

```
roslaunch pioneer_teleop discrete_keyboard_teleop.launch
```

In this case, the robot moves only for a small period of time (1.5
seconds by default) and then stops.

## Sockets teleoperation

Controls the robot remotely throught socket commands (especially if you
want to move the robot using a web interface via internet/LAN).

```
roslaunch pionner_teleop socket_teleop.launch
```

The expected commands are \"*forward*\", \"*backward*\", \"*left*\" or
\"*right*\"

By default, the script listens to port 50001, and the robot moves only
for 1.5 seconds. To change these parameters, you can use extra arguments
as mentioned bellow:

```
roslaunch pionner_teleop socket_teleop.launch _port:=12345 _speed:=0.3 _move_time:=2.0
```

## Command line teleoperation

Useful if you want to move the robot using command line throught a
terminal or ssh:

```
roslaunch pionner_teleop socket_commandline.launch _direction:=forward
```

The expected commands (*\_direction* argument) are \"*forward*\",
\"*backward*\", \"*left*\" or \"*right*\"

By default, the robot moves only for 1.5 seconds at 0.2 speed. To change
these parameters, you can use extra arguments as mentionned bellow:

```
roslaunch pionner_teleop socket_teleop.launch _direction:=backward _speed:=0.3 _move_time:=2.0
```

# What if my robot is not Pionner-compatible?

This package is compatible with any robot using ROS as long as:

The velocity commands are published in */cmd_vel* topic (see the next
section). You modify the .launch scripts to remove the pionner_bringup
call, or you execute directly the python scripts located in */nodes*
folder.

# Known issues

## Velocity command topic

By default, the scripts publish velocity commands to */cmd_vel* topic.

In case your velocity commands topic has a different name, or you are
not using Pionner-compatible robots, you will have to remap your
velocity topic to */cmd_vel* or change the topic name in the python
scripts which are located in */nodes* folder
