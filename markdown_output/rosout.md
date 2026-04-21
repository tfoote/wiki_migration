## Overview

rosout is the name of the console log reporting mechanism in ROS. It can
be thought as comprising several components:

-   The [`rosout`](#rosapi) node for subscribing, logging, and
    republishing the messages.
-   The [/rosout](#rosout_topic) topic
-   The [/rosout_agg](#rosout_agg) topic for subscribing to an
    aggregated feed
-   <<MsgLink(rosgraph_msgs/Log)>> message type, which defines
    standard fields as well as [verbosity levels](Verbosity Levels).
-   [client APIs](#client_apis) to facilitate easy use of the rosout
    reporting mechanism
-   GUI tools, like [rqt_console](rqt_console), for viewing the console
    log messages.

The `rosout` *package* only provides the `rosout` node.

## Client APIs

Individual client APIs provide different ways of broadcasting to rosout:

-   [roscpp](roscpp) uses [rosconsole](rosconsole), which is described
    in the [roscpp logging overview](roscpp/Overview/Logging).
-   [rospy](rospy)'s implementation is detailed in the
    [rospy logging overview](rospy/Overview/Logging).

## Verbosity Levels

Please see [Verbosity Level Best Practices](Verbosity Levels).

## ROS API/Nodes

The `/rosout` node is part of [roscore](roscore) and has preferential
startup order.



```clearsilver
name = rosout 
desc = rosout subscribes to the standard `/rosout` topic, records these messages in a textual log file, and rebroadcasts the messages on `/rosout_agg`. 
sub {
  0.name = /rosout
  0.type = rosgraph_msgs/Log
  0.desc = Standard ROS topic for publishing logging messages.
}
pub {
  0.name = /rosout_agg
  0.type = rosgraph_msgs/Log
  0.desc = Aggregated feed of messages published to `/rosout`.
}
```



### /rosout

ROS [client libraries](Client Libraries) are required to publish console
logging messages to the `/rosout` topic as a standard interface.

### /rosout_agg

`/rosout_agg` is an aggregated feed for subscribing to console logging
messages. This aggregated topic is offered as a performance improvement:
instead of connecting to individual ROS nodes to receive their console
messages, the aggregated message feed can instead be received directly
from the `rosout` node.

### rosout.log

`rosout` node by default logs all messages into `rosout.log` in the
ROS log directory. This can be disabled by setting environment variable
`ROSOUT_DISABLE_FILE_LOGGING` to `True` when launching
[roscore](roscore).

By default, `rosout.log` prints `topic` name for every message. This
behavior can be changed by setting boolean ROS parameter
`/rosout/omit_topics` at any time.

## Roadmap/Stability

No future development on `rosout` is currently planned.
