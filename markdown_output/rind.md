![](attachment:rind.png)

## Overview

```wiki
This is a beta release to get feedback.

Currently requires Ubuntu 10.04 or having appindicator installed
```

This package provides an indicator that displays the status of ROS. It
shows the topics available and the nodes that are currently running. It
is also possible to kill and restart ROS Core using this tool.

roscore does not save it's pid to a file by default so to stop roscore
when it is manually started it must be run with the following option.

`roscore --pid ~/.ros/roscore.pid`

### Installation

This package has just been added to the ihr_tools stack and may not be
indexed yet
<http://github.com/IHeartRobotics/iheart-ros-pkg/tree/master/ihr_tools/>

Install the ihr_tools stack.

```shell
cd ~/ros/stacks
git clone git://github.com/IHeartRobotics/iheart-ros-pkg.git
cd iheart-ros-pkg/ihr_tools
rosdep install rind
rosmake rind
```

## Running

```
roscd rind
cd bin
./rind
```

## Known Bugs

-   Underscores are not shown in topic names
-   This should probably be a background process
-   Cannot kill roscore remotely
