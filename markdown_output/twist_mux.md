1.  keywords twist, multiplexer

## Overview

When there are more than a single source to move a robot with a
[geometry_msgs::Twist](http://docs.ros.org/api/geometry_msgs/html/msg/Twist.html)
message, it is important to multiplex all those input sources into a
single one that goes to the controller (e.g.
[diff_drive_controller](diff_drive_controller)).

This package provides a node that subscribes to a list of topics
publishing
[geometry_msgs::Twist](http://docs.ros.org/api/geometry_msgs/html/msg/Twist.html)
messages and multiplexes them using a priority-based scheme. It also
supports timeouts for each input and locking by means of topics that
publish
[std_msgs::Bool](http://docs.ros.org/api/std_msgs/html/msg/Bool.html)
messages.

## Twist multiplexer

The main node of this package is `twist_mux`, which provides a
multiplexer for
[geometry_msgs::Twist](http://docs.ros.org/api/geometry_msgs/html/msg/Twist.html)
messages. It takes N input twist topics and outputs the messages from a
single one. For selecting the topic they are prioritized based on their
priority, the messages timeout and M input lock topics that can inhibit
one input twist topic. This is illustrated in the diagram below.

![twist_mux_diagram](attachment:twist_mux_diagram.png)

## Configuration

The N input twist topics and M input lock topics are configured using
parameters, which are read when launching the node:



```bash
roslaunch twist_mux twist_mux.launch
```



In the **config** folder there are example yaml files with configuration
parameters.

### Subscribers

The `twist_mux` subscribes to the N input twist topics and M input
lock topics specified in the parameters `topics` and `locks`
described below.

#### Twist inputs

The **topics** parameter contains a list of structs with the following
fields that specify each input twist topics:

- **name** : Human readable name, only for diagnostics purposes.
- **topic** : Input topic name. The node will subscribe to it. It must
  be of
  [geometry_msgs::Twist](http://docs.ros.org/api/geometry_msgs/html/msg/Twist.html)
  type.
- **timeout** : Messages timeout in seconds. If no message arrives after
  the timeout, other topics are selected. If `timeout == 0.0`, the
  topic never enters in timeout.
- **priority** : Priority of the topic from 0 to 255. The higher the
  more priority it has over the others.

Example configuration to multiplex the autonomous navigation from
[move_base](move_base), a joystick from [joy_teleop](joy_teleop), a
keyboard from [key_teleop](key_teleop) and a tablet:


```yaml
topics:
-
  name    : navigation
  topic   : nav_vel
  timeout : 0.5
  priority: 10
-
  name    : joystick
  topic   : joy_vel
  timeout : 0.5
  priority: 100
-
  name    : keyboard
  topic   : key_vel
  timeout : 0.5
  priority: 90
-
  name    : tablet
  topic   : tab_vel
  timeout : 0.5
  priority: 100
```



The joystick and the tablet are given the maximum priority, then the
keyboard and finally the autonomous navigation. Note that it is possible
to use the same priority for several input twist topics, although it is
not recommended.

#### Lock inputs

The **locks** parameter contains a list of structs with the following
fields that specify each input lock topics:

- **name** : Human readable name, only for diagnostics purposes.
- **topic** : Input topic name. The node will subscribe to it. It must
  be of
  [std_msgs::Bool](http://docs.ros.org/api/std_msgs/html/msg/Bool.html)
  type.
- **timeout** : Messages timeout in seconds. The lock topic is supposed
  to publish at a certain frequency, so the timeout allows to detect if
  the publisher is dead in order to enable the lock. If `timeout ==
  0.0`, it is not used.
- **priority** : Priority of the topic from `0` to `255`. The higher
  the more priority it has over the others.

Example configuration to pause the navigation and give priority to the
joystick: 

```yaml
locks:
-
  name    : pause
  topic   : pause_navigation
  timeout : 0.0
  # Same priority as joystick control, so it'll not block it.
  priority: 100
-
  name    : joystick 
  topic   : joy_priority
  timeout : 0.0
  priority: 100
```



### Publishers

A single topic is selected every time a new message arrives through the
input twist topics; this is needed in order to check for the timeouts,
locks, and priorities. The messages are published in:

- **cmd_vel** : Output
  [geometry_msgs::Twist](http://docs.ros.org/api/geometry_msgs/html/msg/Twist.html)
  topic of the twist multiplexer.

The selected input is bypassed to the output, so the behavior is
completely asynchronous. There is only a small delay introduced for the
check that selects the input topic.

## Evaluation

The twist multiplexer operates asynchronously using the input twist
topics callbacks. Every time a new message arrives, the timeout,
priority, and locks are evaluated in order to select the input topic
that must be published. Doing this, the output is exactly the same as
the input. Only a small delay is introduced. Here we analyze that
overhead for different numbers of input twist and lock topics.

The next plot shows one input twist topic vs. the output one. The delay
is usually 0, and always `< 1ms`.
![twist_mux_plot_01\|width="750"](attachment:twist_mux_plot_01.png)

WIP Plot with: delay vs. N + M

All these tests have been done with a 8-core Intel(R) Core(TM) i7 CPU
870 @ 2.93GHz and 8GB of RAM with the minimum ROS nodes running and
Gazebo simulator.

## Joystick relay

In order to make it easier to use a joystick input from
[joy_teleop](joy_teleop) with [twist_mux](twist_mux), the package comes
with a joystick relay. See
[twist_mux/joystick_relay](twist_mux/joystick_relay).
