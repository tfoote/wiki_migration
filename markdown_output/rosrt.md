## Overview

rosrt is a package that contains realtime-safe tools for interacting
with ROS. It is currently **experimental** and **not API stable**, so
use at your own risk. Used together with a Xenomai Kernel the ROS
processes get guaranteed CPU time and are not affected by other
processes. rosrt can also slightly improve performance by avoiding
memory allocations by preallocating. Those speed-ups should probably be
helpful even if not running a real time system if small margins are
important.

## Initialization

Before using any of rosrt you must call:

```cplusplus
rosrt::init();
```

There is an optional
[InitOptions](http://www.ros.org/doc/api/rosrt/html/structros_1_1rt_1_1InitOptions.html)
argument to `rosrt::init()`.

`rosrt::init()` starts three threads, one for publishing, one for
subscribing and one for garbage collection. The publisher thread uses a
lock-free multi-writer single-reader queue with a fixed limit on the \#
of messages specified by `InitOptions::pubmanager_queue_size`.

## Publisher

See also:
[rosrt::Publisher API docs](http://www.ros.org/doc/api/rosrt/html/classros_1_1rt_1_1Publisher.html)

Using the `rosrt::Publisher` is very similar to the standard
`ros::Publisher` but with some realtime-specific requirements. First,
it provides you with a fixed-size buffer of messages (10 in the example
below). To be realtime safe you must allocate your messages out of this
`rosrt::Publisher` you're publishing it with. Second, you must
initialize each of those messages with a template message when you
initialize the `rosrt::Publisher`. Anything that needs to be
preallocated should be preallocated in this template.

```cplusplus
rosrt::Publisher<std_msgs::UInt32> pub(nh.advertise<std_msgs::String>("topic", 1), 10, std_msgs::UInt32());
std_msgs::UInt32Ptr msg = pub.allocate();
if (msg)
{
  msg->data = 10;
  pub.publish(msg);
}
```

Deallocation of the `Publisher`'s pool of memory is done by a
separate garbage collection thread, and will not happen until all
messages allocated out of the `Publisher` have been freed (or on
program exit).

## Subscriber

See also:
[rosrt::Subscriber API docs](http://www.ros.org/doc/api/rosrt/html/classros_1_1rt_1_1Subscriber.html)

Using the `rosrt::Subscriber` is a bit different from the standard
`ros::Subscriber`, mainly because it's polling based instead of
callback based:

```cplusplus
rosrt::Subscriber<std_msgs::UInt32> sub(3, nh, "test");
std_msgs::UInt32ConstPtr msg = sub.poll();
if (msg)
{
  ...
}
```

As with the `rosrt::Publisher`, you must specify a message pool size.
If you are not going to be storing off received messages the optimal
size for this is 3 (1 for the ROS-side subscription queue, 1 waiting in
the Subscriber, 1 in use by realtime).

`poll()` will never return the same message twice. This means:
```
<message received>
sub.poll()  <---  returns a message
sub.poll()  <---  returns NULL
<message received>
sub.poll()  <---  returns a message
...
```

Deallocation of the `Subscriber`'s pool of memory is done by a
separate garbage collection thread, and will not happen until all
messages allocated out of the `Subscriber` have been freed (or on
program exit).

## Allocation Tracking

rosrt also provides a way of tracking allocations and frees per thread.
See the `getThreadAllocInfo()`, `resetThreadAllocInfo()`,
`setThreadBreakOnAllocOrFree()` functions in
[the rosrt namespace](http://www.ros.org/doc/api/rosrt/html/namespaceros_1_1rt.html),
as well as the
[AllocInfo struct](http://www.ros.org/doc/api/rosrt/html/structros_1_1rt_1_1AllocInfo.html).
