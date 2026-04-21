## Overview

\`message_filters\` is a utility library for use with [roscpp](roscpp)
and [rospy](rospy). It collects commonly used message \"filtering\"
algorithms into a common space. A message filter is defined as something
which a message arrives into and may or may not be spit back out of at a
later point in time.

An example is the time synchronizer, which takes in messages of
different types from multiple sources, and outputs them only if it has
received a message on each of those sources with the same timestamp.

## Filter Pattern

All message filters follow the same pattern for connecting inputs and
outputs. Inputs are connected either through the filter\'s constructor
or through the \`connectInput()\` method. Outputs are connected through
the \`registerCallback()\` method.

Note that the input and output types are defined per-filter, so not all
filters are directly interconnectable.

For example, given two filters \`FooFilter\` and \`BarFilter\` where
\`FooFilter\`\'s output is compatible with \`BarFilter\`\'s input,
connecting foo to bar could be (in C++):

```cplusplus
FooFilter foo;
BarFilter bar(foo);
``` or:

```cplusplus
FooFilter foo;
BarFilter bar;
bar.connectInput(foo);
``` in Python:

```python
bar(foo)
``` ```python
bar.connectInput(foo)
``` To then connect bar\'s
output to your own callback function:

```cplusplus
bar.registerCallback(myCallback);
``` The signature of \`myCallback\` is dependent on
the definition of \`BarFilter\`.

### registerCallback()

You can register multiple callbacks with the \`registerCallbacks()\`
method. They will get called in the order they are registered.

**C++**

. In C++ \`registerCallback()\` returns a
[message_filters::Connection](http://www.ros.org/doc/api/message_filters/html/c++/classmessage__filters_1_1Connection.html)
object that allows you to disconnect the callback by calling its
\`disconnect()\` method. You do not need to store this connection object
if you do not need to manually disconnect the callback.

## Subscriber

See also:
[C++ message_filters::Subscriber API docs](http://www.ros.org/doc/api/message_filters/html/c++/classmessage__filters_1_1Subscriber.html)
[Python message_filters.Subscriber](http://www.ros.org/doc/api/message_filters/html/python/#message_filters.Subscriber)

The \`Subscriber\` filter is simply a wrapper around a ROS subscription
that provides a source for other filters. The \`Subscriber\` filter
cannot connect to another filter\'s output, instead it uses a ROS topic
as its input.

### Connections

*Input*

. No input connections

*Output*

. **C++**: \`void callback(const boost::shared_ptr\<M const\>&)\`
**Python**: \`callback(msg)\`

### Example (C++)

```cplusplus
message_filters::Subscriber<std_msgs::UInt32> sub(nh, "my_topic", 1);
sub.registerCallback(myCallback);
``` is the equivalent of:

```cplusplus
ros::Subscriber sub = nh.subscribe("my_topic", 1, myCallback);
```

### Example (Python)

```python
sub = message_filters.Subscriber("pose_topic", robot_msgs.msg.Pose)
sub.registerCallback(myCallback)
```

## Time Synchronizer

See also:
[C++ message_filters::TimeSynchronizer API docs](http://www.ros.org/doc/api/message_filters/html/c++/classmessage__filters_1_1TimeSynchronizer.html),
[Python message_filters.TimeSynchronizer](http://www.ros.org/doc/api/message_filters/html/python/#message_filters.TimeSynchronizer)

The \`TimeSynchronizer\` filter synchronizes incoming channels by the
timestamps contained in their headers, and outputs them in the form of a
single callback that takes the same number of channels. The C++
implementation can synchronize up to 9 channels.

### Connections

*Input*

. **C++**: Up to 9 separate filters, each of which is of the form \`void
callback(const boost::shared_ptr\<M const\>&)\`. The number of filters
supported is determined by the number of template arguments the class
was created with. **Python**: N separate filters, each of which has
signature \`callback(msg)\`.

*Output*

. **C++**: For message types \`M0\`..\`M8\`, \`void callback(const
boost::shared_ptr\<M0 const\>&, \..., const boost::shared_ptr\<M8
const\>&)\`. The number of parameters is determined by the number of
template arguments the class was created with. **Python**:
\`callback(msg0.. msgN)\`. The number of parameters is determined by the
number of template arguments the class was created with.

### Example (C++)

Suppose you are writing a ROS node that needs to process data from two
time synchronized topics. Your program will probably look something like
this:

```cplusplus
#include <message_filters/subscriber.h>
#include <message_filters/time_synchronizer.h>
#include <sensor_msgs/Image.h>
#include <sensor_msgs/CameraInfo.h>

using namespace sensor_msgs;
using namespace message_filters;

void callback(const ImageConstPtr& image, const CameraInfoConstPtr& cam_info)
{
  // Solve all of perception here...
}

int main(int argc, char** argv)
{
  ros::init(argc, argv, "vision_node");

  ros::NodeHandle nh;

  message_filters::Subscriber<Image> image_sub(nh, "image", 1);
  message_filters::Subscriber<CameraInfo> info_sub(nh, "camera_info", 1);
  TimeSynchronizer<Image, CameraInfo> sync(image_sub, info_sub, 10);
  sync.registerCallback(boost::bind(&callback, _1, _2));

  ros::spin();

  return 0;
}
``` (Note: In this particular case you could use
the
[CameraSubscriber](http://www.ros.org/doc/api/image_transport/html/classimage__transport_1_1CameraSubscriber.html)
class from [image_transport](image_transport), which essentially wraps
the filtering code above.)

### Example (Python)

```python
import message_filters
from sensor_msgs.msg import Image, CameraInfo

def callback(image, camera_info):
  # Solve all of perception here...

image_sub = message_filters.Subscriber('image', Image)
info_sub = message_filters.Subscriber('camera_info', CameraInfo)

ts = message_filters.TimeSynchronizer([image_sub, info_sub], 10)
ts.registerCallback(callback)
rospy.spin()
```

## Time Sequencer

See also:
[C++ message_filters::TimeSequencer API docs](http://www.ros.org/doc/api/message_filters/html/c++/classmessage__filters_1_1TimeSequencer.html)

**Python: the \`TimeSequencer\` filter is not yet implemented.**

The \`TimeSequencer\` filter guarantees that messages will be called in
temporal order according to their header\'s timestamp. The
\`TimeSequencer\` is constructed with a specific delay which specifies
how long to queue up messages before passing them through. A callback
for a message is never invoked until the messages\' time stamp is out of
date by at least delay. However, for all messages which are out of date
by at least the delay, their callback are invoked and guaranteed to be
in temporal order. If a message arrives from a time prior to a message
which has already had its callback invoked, it is thrown away.

### Connections

*Input*

. **C++**: \`void callback(const boost::shared_ptr\<M const\>&)\`

*Output*

. **C++**: \`void callback(const boost::shared_ptr\<M const\>&)\`

### Example (C++)

The C++ version takes both a delay an an update rate. The update rate
determines how often the sequencer will check its queue for messages
that are ready to be pass through. The last argument is the number of
messages to queue up before beginning to throw some away.

```cplusplus
FooFilter foo;
BarFilter bar;
bar.connectInput(foo);
```0

## Cache

See also:
[C++ message_filters::Cache API docs](http://www.ros.org/doc/api/message_filters/html/c++/classmessage__filters_1_1Cache.html)
[Python message_filters.Cache](http://www.ros.org/doc/api/message_filters/html/python/#message_filters.Cache)

Stores a time history of messages.

Given a stream of messages, the most recent N messages are cached in a
ring buffer, from which time intervals of the cache can then be
retrieved by the client. The timestamp of a message is determined from
its \`header\` field.

```cplusplus
FooFilter foo;
BarFilter bar;
bar.connectInput(foo);
```1 The Cache immediately passes messages through
to its output connections.

### Connections

*Input*

. **C++**: \`void callback(const boost::shared_ptr\<M const\>&)\`
**Python**: \`callback(msg)\`

*Output*

. **C++**: \`void callback(const boost::shared_ptr\<M const\>&)\`
**Python**: \`callback(msg)\`

In C++:

```cplusplus
FooFilter foo;
BarFilter bar;
bar.connectInput(foo);
```2 In Python:

```cplusplus
FooFilter foo;
BarFilter bar;
bar.connectInput(foo);
```3 In this example, the \`Cache\` stores the last
100 messages received on \`my_topic\`, and \`myCallback\` is called on
the addition of every new message. The user can then make calls like
\`cache.getInterval(start, end)\` to extract part of the cache.

```cplusplus
FooFilter foo;
BarFilter bar;
bar.connectInput(foo);
```4 }}}}

## Policy-Based Synchronizer \[ROS 1.1+\]

The \`Synchronizer\` filter synchronizes incoming channels by the
timestamps contained in their headers, and outputs them in the form of a
single callback that takes the same number of channels. The C++
implementation can synchronize up to 9 channels.

The \`Synchronizer\` filter is templated on a policy that determines how
to synchronize the channels. There are currently two policies:
\`ExactTime\` and \`ApproximateTime\`.

**C++ Header:** \`message_filters/synchronizer.h\`

### Connections

*Input*

. **C++**: Up to 9 separate filters, each of which is of the form \`void
callback(const boost::shared_ptr\<M const\>&)\`. The number of filters
supported is determined by the number of template arguments the class
was created with. **Python**: N separate filters, each of which has
signature \`callback(msg)\`.

*Output*

. **C++**: For message types \`M0\`..\`M8\`, \`void callback(const
boost::shared_ptr\<M0 const\>&, \..., const boost::shared_ptr\<M8
const\>&)\`. The number of parameters is determined by the number of
template arguments the class was created with. **Python**:
\`callback(msg0.. msgN)\`. The number of parameters is determined by the
number of template arguments the class was created with.

### ExactTime Policy

The \`message_filters::sync_policies::ExactTime\` policy requires
messages to have exactly the same timestamp in order to match. Your
callback is only called if a message has been received on all specified
channels with the same exact timestamp. The timestamp is read from the
\`header\` field of all messages (which is required for this policy).

**C++ Header:** \`message_filters/sync_policies/exact_time.h\`

**Example (C++)**

```cplusplus
FooFilter foo;
BarFilter bar;
bar.connectInput(foo);
```5

### ApproximateTime Policy

The \`message_filters::sync_policies::ApproximateTime\` policy uses
[an adaptive algorithm](message_filters/ApproximateTime) to match
messages based on their timestamp.

```cplusplus
FooFilter foo;
BarFilter bar;
bar.connectInput(foo);
```6 **C++ Header:**
\`message_filters/sync_policies/approximate_time.h\`

**Example (C++)**

```cplusplus
FooFilter foo;
BarFilter bar;
bar.connectInput(foo);
```7 ```cplusplus
FooFilter foo;
BarFilter bar;
bar.connectInput(foo);
```8 }}}}

## Chain \[ROS 1.1+\]

See also:
[C++ API Docs](http://www.ros.org/doc/api/message_filters/html/c++/classmessage__filters_1_1Chain.html)

The \`Chain\` filter allows you to dynamically chain together multiple
single-input/single-output (simple) filters. As filters are added to it
they are automatically connected together in the order they were added.
It also allows you to retrieve added filters by index.

\`Chain\` is most useful for cases where you want to determine which
filters to apply at runtime rather than compile-time.

### Connections

*Input*

. **C++**: \`void callback(const boost::shared_ptr\<M const\>&)\`

*Output*

. **C++**: \`void callback(const boost::shared_ptr\<M const\>&)\`

### Examples (C++)

**Simple Example**

```cplusplus
FooFilter foo;
BarFilter bar;
bar.connectInput(foo);
```9 **Bare Pointers**

It is possible to pass bare pointers in. These will **not** be
automatically deleted when Chain is destructed.

```python
bar(foo)
```0 **Retrieving a Filter**

```python
bar(foo)
```1
