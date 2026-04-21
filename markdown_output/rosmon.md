![](attachment:screenshot.svg)

## Why rosmon?

rosmon is a drop-in replacement for the venerable [roslaunch](roslaunch)
tool. It offers some interesting features both for monitoring and
debugging:

-   rosmon has a clean, modern console UI. With one glance at the status
    bar, you can see that all of your nodes are still running as they
    should. Console output from the nodes is intercepted and augmented
    with the node name - allowing you to immediately see *which* node is
    printing that message. This also works for plain output without
    rosconsole macros.
-   rosmon has a ROS interface itself. Query node status or start/stop
    nodes using service calls. This allows you to use ROS network
    transparency for remote monitoring.
-   rosmon is developer friendly. With two keystrokes, you can attach
    gdb to a running node. If a node crashes without gdb attached, you
    can run gdb against an automatically collected coredump, providing
    post-mortem analysis.
-   rosmon is *fast*. Thanks to lazy evaluation of parameters, costly
    calls to [xacro](xacro) and friends are reduced as much as possible.

## Differences to roslaunch

The [roslaunch/XML](roslaunch/XML) specification is complex and a bit
vague, so you can expect some differences. Bug reports are welcome!
Known differences include:

-   rosmon will not launch [roscore](roscore) automatically. We believe
    that it is important to make a conscious decision how and where to
    run the roscore. Often, restarting roslaunch unknowingly restarts
    the contained roscore, leading to hard-to-debug problems with other
    connected nodes.
-   The `<machine>` tag is not supported.

For additional information and rosmon extensions not supported by
roslaunch see [rosmon/XML](rosmon/XML).

rosmon was developed for the DARPA Robotics Challenge, which influenced
our decision to develop it in a statically typed language (C++) for more
runtime robustness. However, this meant that [roslaunch](roslaunch) XML
parsing code could not be used.

## Installation

Binary packages are available:

```
sudo apt install ros-${ROS_DISTRO}-rosmon

source /opt/ros/${ROS_DISTRO}/setup.bash # Needed to use the 'mon launch' shortcut
```

If you just need the rosmon CLI and don't require the `rqt_rosmon` rqt
plugin, you can install the smaller package
`ros-${ROS_DISTRO}-rosmon-core` instead.

Recommendation: To benefit from compressed core dump storage and
explicit core dump storage limits, install systemd-coredump.

## Usage

When installed, rosmon drops a handy shell wrapper into your shell
context (currently supported in bash and zsh). You may have to re-source
your workspace environment after building. Usage (similar to roslaunch):

```
mon launch <package> <launch file> [arguments]
```

or

```
mon launch <path to launch file> [arguments]
```

Full usage information:

```
Usage:
  rosmon [actions] [options] some_package test.launch [arg1:=value1 ...]
  rosmon [actions] [options] path/to/test.launch [arg1:=value1 ...]

Actions (default is to launch the launch file):
  --benchmark    Exit after loading the launch file
  --list-args    List launch file arguments

Options:
  --disable-ui   Disable fancy terminal UI
  --help         This help screen
  --log=FILE     Write log file to FILE
  --name=NAME    Use NAME as ROS node name. By default, an anonymous
                 name is chosen.

rosmon also obeys some environment variables:
  ROSMON_COLOR_MODE   Can be set to 'truecolor', '256colors', 'ansi'
                      to force a specific color mode
                      If unset, rosmon tries to detect the best
                      available color mode.
```

## Console interface

rosmon features a basic console interface. Each node is assigned a
dedicated key, which can be used to open the action menu for that node.
Available actions are:

-   Starting/stopping the node (keys 's' and 'k')
-   Starting a debugger, either attached to the running process or
    post-mortem against a collected coredump (key 'd')

## GUI interface

rosmon can also be controlled remotely using an [rqt](rqt) plugin, which
uses rosmon's ROS interface. The context menu offers starting and
stopping control. Additionally collected statistics (CPU and memory
usage) are displayed.

## Nodes

```clearsilver
name = rosmon
desc = Main rosmon node.
pub {
  0.name = ~state
  0.type = rosmon/State
  0.desc = Current state of all controlled nodes. Updated every second.
}
srv {
  0.name = ~start_stop
  0.type = rosmon/StartStop
  0.desc = Start or stop a controlled node.
}
```
