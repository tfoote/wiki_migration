This package contains an implementation of a "remote" watchdog. There
exists one watchdog monitor that monitors all watchdogs and many
watchdogs.

## Implementing a Watchdog in your node

To implement a watchdog timer into your code, you should first add the
watchdog_timer package as a dependency to your package.

Then you should include the



```
#include "watchdog_timer/Watchdog.h"
```



in your code.

In addition, at the CMakeLists.txt file you should link your executable
to the Watchdog library



```
rosbuild_add_link_flags(executable_name -lWatchdog)
```



### Creating a Watchdog

To create a watchdog object (and register it at the watchdog monitor),
create a watchdog object



```
Watchdog theWatchdogName("nameOfWatchdog",ros::Duration(10));
```



Where the first argument of the constructor is the unique name of the
watchdog and the second argument is the amount of time that the timer
will countdown, until it resets.

### Starting, Stopping and Reseting a Watchdog

Having your watchdog timer you can start/ stop/ reset the timer by using
the objects methods.

By calling the 

```
theWatchdogName.start();
```

 you can start the watchdog.

Similarly:



```
theWatchdogName.stop();
```





```
theWatchdogName.reset();
```



### When a watchdog times out

When a watchdog times-out the watchdog monitor will emit a ROS_ERROR and
will publish a message at the /robot/watchdogResets topic.

## Starting the Watchdog monitor

To start the watchdog monitor you can run



```
rosrun watchdog_timer wdtMonitor
```



or you could include it in a .launch file

## Technical Information

This watchdog implementation does not try to reset any nodes or perform
any other action. It's sole purpose is to notify that a node has failed
to reset in time a watchdog.

The watchdog implementation has a couple of services and topics. At the
/robot/watchdogRegistry service a watchdog can register/ start/ stop
itself. This is taken care by the client watchdog implementation. The
/robot/watchdog topic is used for the watchdog client to publish their
resets, to be heard by the watchdog monitor.
