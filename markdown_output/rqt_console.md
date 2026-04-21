![ rqt_console sample snapshot \| width=700](attachment:snap_rqt_console.png )

## Overview

`rqt_console` is a viewer in the [rqt](rqt) package that displays
messages being published to [rosout](rosout). It collects messages over
time, and lets you view them in more detail, as well as allowing you to
filter messages by various means.

Sending messages to `rqt_console` is done differently in each client
library: [C++](roscpp/Overview/Logging),
[Python](rospy/Overview/Logging)

## Usage

Assuming you have ROS installed, you can invoke `rqt_console` by just
typing: ```
rqt_console
```

## Message List

The list view shows all of the messages, updating in real time as they
arrive. The list displays all the information in the
<<MsgLink(roslib/Log)>> message broadcast on [rosout](rosout):
**Message** The message specified by the user, e.g. in the screenshot
above "hello world\..." **Severity** The severity level of the
message, e.g. Debug, Info, etc. **Node** The name of the node which
broadcast the message **Time** The time at which the message was
broadcast **Topics** The topics advertised by the node broadcasting the
message **Location** Combines the file, function and line using colons,
e.g.
`/u/jfaust/ros/base/pkgs/ros_tutorials/roscpp_tutorials/talker/talker.cpp:main:92`

There are two operations you can use on the items in the list. A *double
click* will bring up all the information about that message in a
separate box.

A *right click* will pop up a menu allowing you to filter the list based
on some aspect of the selected message

## Filtering methods

You can filter the message list in two ways, by exclude filter and
highlight filter.

!Entry Incomplete.

### Exclude

### Highlight

## Filtering types

### Severity

### Node

### Time

### Topic

### Location

### Custom

## Tutorials

See the
[rospy_tutorials/Tutorials/Logging](rospy_tutorials/Tutorials/Logging)
page. It will help you use [rosout](rosout) to publish error, info and
debug messages and view them in rqt_console.
