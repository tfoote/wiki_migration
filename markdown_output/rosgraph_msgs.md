## Overview

`rosgraph_msgs` contains message relating to the ROS Computation
Graph. Most users are not expected to interact with messages in this
package, and it is strongly advised against. These messages are
generally wrapped in higher level APIs.

Prior to Diamondback, these messages were in the [roslib](roslib)
package. They were migrated to this package as part of
[REP 100](http://www.ros.org/reps/rep-0100.html).

## Messages

[rosgraph_msgs/msg/Log](https://docs.ros.org/en/rolling/p/rosgraph_msgs/msg/Log.html)
is the underlying message data structure for logging to
[rosout](rosout). If you use the client API methods in [rospy](rospy)
and [roscpp](roscpp), you will be protected against any future revisions
to this message.

[rosgraph_msgs/msg/Clock](https://docs.ros.org/en/rolling/p/rosgraph_msgs/msg/Clock.html)
is used for simulated [clock](Clock) in ROS. Only nodes that provide
simulated time sources are expected to use this message.
[rosgraph_msgs/msg/TopicStatistics](https://docs.ros.org/en/rolling/p/rosgraph_msgs/msg/TopicStatistics.html)
is used by [roscpp](roscpp) and [rospy](rospy) for publishing statistics
on topic connections on /statistics. See [Topics](Topics) for more
information.
