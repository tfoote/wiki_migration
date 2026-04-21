## Overview

This simple library extracts information from a ROS Message, even when
its type is unknown at compilation time.

Have you ever wanted to build an app that can subscribe to any topic and
extract its content, or can read data from any rosbag? What if the topic
and/or the bag contains user defined ROS types ignored at compilation
time?

The common solution in the ROS ecosystem is to use Python, that provides
the needed introspection. Tools, for instance, like rqt_plot and rqt_bag
took this approach. This library implements a C++ alternative.

# Some background

The ROS Message Types can be described as a
[Interface Description Language](https://en.wikipedia.org/wiki/Interface_description_language).
This approach is very well known and commonly used on the web and in
distributed systems in general.

A [rosmsg](rosmsg) is defined by the user; an "IDL compiler", i.e.
[gencpp](gencpp), reads this schema and generates a header file that
contains the source code that the user shall include in his/her
applications. The inclusion of this header file is needed on both the
publisher *and* the subscriber sides.

This approach provides strong and type-safe contracts between the
producer and the consumer of the message and, additionally, is needed to
implements a fast serialization / deserialization mechanism.

The only "problem" is that in very few use cases (for instance if you
want to build a plugin to
[load ROS bags in MATLAB](https://github.com/bcharrow/matlab_rosbag))
you don't know in advance which ROS Messages you will need to read.
Therefore, you won't be able to include the necessary header files.

## Ros Type Introspection

The library is composed of three main modules:

-   **Parser**: it performs introspection of a Ros Message using the
    schema stored in `ros::message_traits::Definition`.

```{=html}
<!-- -->
```
-   **Deserializer**: using the schema built by the parsed, it can
    extract the actual values from a raw message.

```{=html}
<!-- -->
```
-   **Renamer**: last but not least, the library offers as well an easy
    way to remap/rename the data using a simple set of rules. This can
    be very handy in multiple scenarios that are very common in ROS.

This library is particularly useful to extract data from two
type-erasing classes provided by ROS itself:

1\.
[topic_tools::ShapeShifter](http://docs.ros.org/indigo/api/topic_tools/html/classtopic__tools_1_1ShapeShifter.html):
a type used to subscribe to any topic, regardless of the original type.

2\.
[rosbag::MessageInstance](http://docs.ros.org/indigo/api/rosbag_storage/html/c++/classrosbag_1_1MessageInstance.html):
the generic type commonly used to read data from a ROS bag.

## Usage

Please refer to
<https://github.com/facontidavide/type_introspection_tests/tree/master/example>.

Contact the author if you have any question.
