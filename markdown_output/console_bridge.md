\'\'\'Package:\'\'\' console_bridge

\'\'\'Maintainers:\'\'\' Mirza Shah (mshah@willowgarage.com), Ioan Sucan
(isucan@willowgarage.com)

\'\'\'Author:\'\'\' Ioan Sucan (isucan@willowgarage.com)

\'\'\'Code Repository:\'\'\' <https://github.com/ros/console_bridge>

## Overview

\'\'\'console_bridge\'\'\' is a ROS-independent, pure CMake (i.e.
non-catkin and non-rosbuild package) that provides logging calls that
mirror those found in [rosconsole](rosconsole), but for applications
that are not necessarily using ROS.

Normally in ROS C++ code, developers can log data via
[rosconsole](rosconsole) using the macros ROS_DEBUG, ROS_INFO, ROS_WARN,
and ROS_ERROR. These logging messages are not only outputted to the
screen (depending on log level of course), but are also published to
`/rosout` so that other ROS nodes can subscribe to them. Applications
like [rqt_console](rqt_console) and its predecessor
[rxconsole](rxconsole) provide graphical interfaces for seeing logs
during application runtime.

The problem with this approach is that libraries that are meant to run
without ROS infrastructure and/or may not want or need the log
publishing cannot use the traditional rosconsole. This is where
console_bridge comes in.

console_bridge provides equivalent calls to the ones found in ROS
console that provide the same functionality:

```
logDebug  -- ROS_DEBUG
logInform -- ROS_INFO
logWarn   -- ROS_WARN
logError  -- ROS_ERROR
```

When these functions are used, the output is directed to stdout rather
than to both stdout and /rosout. However, here is the most interesting
feature:

\'\'\'If you want your console_bridge application to hook into /rosout,
all you have to do is switch the depedency of your package from
console_bridge to [rosconsole_bridge](rosconsole_bridge)!\'\'\'

Once you use [rosconsole_bridge](rosconsole_bridge), the implementations
of `logDebug, logInform, logWarn, and logError` will simply become
equivalent to `ROS_DEBUG, ROS_INFO, ROS_WARN, and ROS_ERROR`
respectively.

## Build Instructions

```
$ git clone git://github.com/ros/console_bridge.git
$ cd console_bridge
$ cmake .
$ make
$ sudo make install
```

## See Also

-   [rosconsole](rosconsole)
-   [rosconsole_bridge](rosconsole_bridge)
