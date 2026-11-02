## Overview

This library is a replacement for the ROS
[message_filters](https://index.ros.org/p/message_filters) package. It
is written in modern C++ and more type-safe than the original version.

The data flow is modeled with a pipeline metaphor, where data always
flows from a source to a sink. A filter is both source and sink for
data, possibly with different data types. For integration with ROS, the
library provides a number of subscribers and publishers which act as
sources or sinks of the data flow.

## Language Requirements

The library requires C++14 or better. Starting with Ubuntu 18.04 (ROS
Melodic), GCC uses C++14 as default dialect. For older versions, you may
or may not succeed by passing the command line option `-std=gnu++1y`
to the compiler.

## Design

The filters are written to be as data agnostic as possible. Therefore,
many filters can process arbitrary data types and are not restricted to
ROS messages. A few filters need access to ROS header information, such
as time stamp or TF frame identifier.

Sources and sinks are strongly typed, i.e., each source will only pass
on data of a particular type, and each sink will only accept data of a
particular type. The compiler will error out if you try to connect
incompatible filters. As the strong typing relies on the C++ template
mechanism, the error messages can be quite verbose and difficult to
parse sometimes (looking at you, GCC).

The library filters support arbitrary arities, i.e., the grouping of
multiple data types, where items of different types are combined and
passed on as a unit. This is particularly useful to process messages
from distinct topics which belong together conceptually, e.g., the
[sensor_msgs::Image](http://docs.ros.org/api/sensor_msgs/html/msg/Image.html)
and
[sensor_msgs::CameraInfo](http://docs.ros.org/api/sensor_msgs/html/msg/CameraInfo.html)
messages from a calibrated camera.

## Getting Started

While you are free to derive your own classes from the one of the base
classes, most programs will want to register a custom callback function
for their application logic.

The
[SimpleUserFilter](https://fkie.github.io/message_filters/classfkie__message__filters_1_1SimpleUserFilter.html)
works almost like a regular ROS callback, but it expects a boolean
return value that determines if the data is passed on to subsequent
filters in the pipeline (if any), or if processing terminates. You can
use this type of filter to consume data at the end of the pipeline, or
if you want to remove invalid inputs before further processing occurs.

The
[UserFilter](https://fkie.github.io/message_filters/classfkie__message__filters_1_1UserFilter.html)
is more generic and can be used if your filter outputs differ from its
inputs. You can implement pretty much any kind of transforming filter.

The
[UserSource](https://fkie.github.io/message_filters/classfkie__message__filters_1_1UserSource.html)
is a simple data source which can be used as callback in third-party
code.

As a simple "Hello World" example, consider:



```cplusplus
#include <ros/ros.h>
#include <std_msgs/String.h>
#include <fkie_message_filters/fkie_message_filters.h>

namespace mf = fkie_message_filters;

using StringSubscriber = mf::Subscriber<std_msgs::String, mf::RosMessage>;
using StringPublisher = mf::Publisher<std_msgs::String, mf::RosMessage>;
using GreetingFilter = mf::UserFilter<
                              StringSubscriber::Output,
                              StringPublisher::Input
                       >;

int main(int argc, char** argv)
{
    ros::init(argc, argv, "hello");
    ros::NodeHandle nh;
    StringSubscriber sub(nh, "name", 1);
    StringPublisher pub(nh, "greeting", 1);
    GreetingFilter flt;
    flt.set_processing_function(
        [](const std_msgs::String& input,
           const GreetingFilter::CallbackFunction& output)
        {
            std_msgs::String greeting;
            greeting.data = "Hello, " + input.data + "!";
            output(greeting);
        }
    );
    mf::chain(sub, flt, pub);
    ros::spin();
    return 0;
}
```



The user-defined filter accepts a
[std_msgs::String](http://docs.ros.org/api/std_msgs/html/msg/String.html)
message with a name as input and composes a new
[std_msgs::String](http://docs.ros.org/api/std_msgs/html/msg/String.html)
message with a personalized greeting as output. Note that each source
can have arbitrarily many sinks connected to it, and vice versa, so the
simplicity of the three-link chain in this example is by no means a
limitation of the library.

## Available Filters

See the [API documentation](https://fkie.github.io/message_filters) for
more details.

- `Buffer`: Store and forward data
- `CameraPublisher`: Publish consumed data to a ROS camera topic
- `CameraSubscriber`: Subscribe to a ROS camera topic as data provider
- `Combiner`: Combine multiple sinks into a single source with one of
  the following policies:
- `Fifo`: First-In-First-Out
- `ExactTime`: Exactly matching time stamp
- [ApproximateTime](#approximatetime):
  Approximately matching time stamp
- `Divider`: Split source with multiple inputs into independent output
  sinks
- `ImagePublisher`: Publish consumed data to a ROS image topic
- `ImageSubscriber`: Subscribe to a ROS image topic as data provider
- `Publisher`: Publish consumed data on a ROS topic
- `Selector`: Choose an arbitrary set of inputs to be forwarded
- `Sequencer`: Enforce correct temporal order
- `SimpleUserFilter`: Simplified filter with user-defined callback
  function
- `Subscriber`: Subscribe to a ROS topic as data provider
- `TfFilter`: Wait for TF transformations for incoming messages
- `UserFilter`: Generic filter with user-defined callback function
- `UserSource`: Manually operated data source

## Implementation Details

The pipeline processing is executed by nested calls to receive and send
functions. The library is thread-safe and guarantees basic exception
safety, but you are expected to handle your own exceptions in your
callbacks. Exceptions which propagate through library code will abort
processing for the offending message immediately, even if not all
downstream sinks have received the message yet. If there is no upstream
user-defined filter that catches the exception, the uncaught exception
will eventually terminate the program. The library will detect cycles in
the pipeline and abort with a `std::logic_error` exception.

Certain filters, such as the `Buffer` or the `TfFilter`, can
interoperate with ROS callback queues for convenient workload
scheduling.

## ApproximateTime

### ApproximateTime policy

#### Overview

This is a policy used by `fkie_message_filters::Combiner` to match
messages coming on a set of topics, even if their time stamps do not
match perfectly. It uses a modified version of the
[ApproximateTime](https://index.ros.org/p/message_filters) algorithm.
Like its predecessor, the algorithm is not merely applying an epsilon to
account for time differences, but tries to find the best possible match.
Each set of grouped messages which are output by the policy, satisfies
the following criteria:

- **Each message is used only once.** Two sets will never share the same
  message, but some messages can be dropped.
- **Messages are used in order.** Unlike the original algorithm, we do
  not guarantee that sets as a whole do not overlap, but we guarantee
  that for each topic, messages will be used in time stamp order. We
  found that revising this criterion improves match quality for
  high-frequency topics, such as stereo vision systems with depth
  images, in the presence of transient jitter.
- **Sets are contiguous.** This means that you cannot form a valid set
  from the dropped messages.
- **Sets have minimal timespan.** This means that the time stamp
  difference among messages in a set cannot be smaller without violating
  the previous property.
- **The output only depends on the time stamps,** not on the arrival
  time of messages. The messages have to arrive in order on each topic,
  but not necessarily across topics, as long as the queue size is large
  enough to accommodate for the differences.

Optional parameters:

- **Set timespan**: the time difference of two messages in the same set
  will never exceed this value. By default, the policy does not
  constrain the timespan. If you set this value, the policy will avoid
  "wasting" messages in sets which are ultimately rejected anyway.
  Oftentimes, this will give you more valid sets in total.
- **Message distance**: if messages of a particular topic cannot be
  closer together than a known interval, providing this lower bound will
  not change the output but will allow the algorithm to conclude earlier
  that a given set is optimal, thereby reducing output lag. The default
  lower bound is zero. An incorrect lower bound will result in
  suboptimal sets being selected. A typical bound is, say, half the
  frame rate of a camera.

#### Algorithm

The algorithm works as follows:

- Wait until each input queue has at least one message available.
- Pick the latest message among the heads of all queues, which is going
  to be the *pivot*. The pivot belongs to every set that is contiguous
  to the previous set, so it must belong to the newly formed set.
- For all other input queues except the pivot, advance to the next
  message until the time difference to the pivot message is minimal.
  Proving optimality depends on the minimum message distance and the
  fact that on every topic, messages will arrive in time stamp order. If
  any queue is exhausted and, at least theoretically, the next message
  could still be closer to the pivot, wait for the next message to
  arrive.
- Once all input queues have reached their optimum, send the resulting
  set. If the set violates the user-specified timespan constraint, drop
  the pivot element instead, and restart from scratch with the remaining
  messages.
- If messages arrive out of order (i.e. a message on a topic has a time
  stamp that is earlier than the previously received one), all queues
  are flushed and the policy restarts from scratch.
- If messages need to be dropped because the maximum queue size or the
  message age limit is exceeded, the pivot element is chosen again from
  the new queue heads. By default, the policy will buffer arbitrary many
  messages for at most one second.
