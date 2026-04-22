## Overview

`std_msgs` contains wrappers for ROS primitive types, which are
documented in the [msg specification](msg). It also contains the
`Empty` type, which is useful for sending an empty signal. However,
these types do not convey semantic meaning about their contents: every
message simply has a field called "`data`". Therefore, while the
messages in this package can be useful for quick prototyping, they are
**NOT intended for "long-term" usage**. For ease of documentation and
collaboration, we recommend that existing messages be used, or new
messages created, that provide meaningful field name(s).

Note that this package also contains the "!MultiArray" types, which
can be useful for storing sensor data. **However**, the same caveat
applies: it's usually "better" (in the sense of making the code
easier to understand, etc.) when developers use or create non-generic
message types (see
[discussion in this thread](https://github.com/ros/std_msgs/issues/8)
for more detail).

## Roadmap

There are currently no plans to add new data types to the `std_msgs`
package.
