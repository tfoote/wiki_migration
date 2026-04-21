## Overview

When working with images we often want specialized transport strategies,
such as using image compression or streaming video codecs.
`image_transport` provides classes and nodes for transporting images
in arbitrary over-the-wire representations, while abstracting this
complexity so that the developer only sees
<<MsgLink(sensor_msgs/Image)>> messages.

Specialized transports are provided by plugins. `image_transport`
itself provides only `"raw"` transport so as not to impose
unnecessary dependencies on client packages. Other transports will only
be available if they are built on your system. On Ubuntu, the
`ros-<distro>-base` debians include the `"compressed"` and
`"theora"` transports provided by the
[image_transport_plugins](image_transport_plugins) stack.

## Quickstart Guide

`image_transport` should always be used to publish and subscribe to
images. At this basic level of usage, it is very similar to using ROS
Publishers and Subscribers. Using `image_transport` instead of the ROS
primitives, however, gives you great flexibility in how images are
communicated between nodes.

For complete examples of publishing and subscribing to images using
`image_transport`, see the [Tutorials](image_transport/Tutorials).

### C++ Usage

Instead of:



```cplusplus
// Do not communicate images this way!
#include <ros/ros.h>

void imageCallback(const sensor_msgs::ImageConstPtr& msg)
{
  // ...
}

ros::NodeHandle nh;
ros::Subscriber sub = nh.subscribe("in_image_topic", 1, imageCallback);
ros::Publisher pub = nh.advertise<sensor_msgs::Image>("out_image_topic", 1);
```

 Do:



```cplusplus
// Use the image_transport classes instead.
#include <ros/ros.h>
#include <image_transport/image_transport.h>

void imageCallback(const sensor_msgs::ImageConstPtr& msg)
{
  // ...
}

ros::NodeHandle nh;
image_transport::ImageTransport it(nh);
image_transport::Subscriber sub = it.subscribe("in_image_base_topic", 1, imageCallback);
image_transport::Publisher pub = it.advertise("out_image_base_topic", 1);
```

 `image_transport` publishers advertise
individual ROS [Topics](Topics) for each available transport - unlike
ROS Publishers, which advertise a single topic. The topic names follow a
standard naming convention, outlined below. Note, however, that all code
interfaces take only a "base topic" name (to which the transport type
is automatically appended); typically you should not directly reference
the transport-specific topic used by a particular plugin.

### Python Usage

`image_transport` does not yet support Python, though it is on the
[Roadmap](image_common/Roadmap). If you need to interface a Python node
with some compressed image transport, try interposing a
[republish](#republish) node.

## Known Transport Packages

If you have implemented a new transport option in a public repository
and would like to see it added to this list, please email our
[mailing list](Mailing Lists).

-   ros-pkg
-   [image_transport](image_transport) (`"raw"`) - The default
    transport, sending <<MsgLink(sensor_msgs/Image)>> through ROS.
-   [compressed_image_transport](compressed_image_transport)
    (`"compressed"`) - JPEG or PNG image compression.
-   [theora_image_transport](theora_image_transport) (`"theora"`) -
    Streaming video using the Theora codec.

## Library ROS API

ROS Publishers and Subscribers are used to transport messages of any
type. `image_transport` offers publishers and subscribers specialized
for images. Because they encapsulate complicated communication behavior,
`image_transport` publishers and subscribers have a public ROS API as
well as a C++ code API. Please see the separate
[code API](http://www.ros.org/doc/api/image_transport/html/)
documentation for C++ usage. The ROS API is documented below.

### image_transport Publishers

`image_transport` publishers are used much like ROS Publishers, but
may offer a variety of specialized transport options (JPEG compression,
streaming video, etc.). Different subscribers may request images from
the same publisher using different transports.

C++: `image_transport::Publisher`
([API](http://www.ros.org/doc/api/image_transport/html/classimage__transport_1_1Publisher.html)),
`image_transport::CameraPublisher`
([API](http://www.ros.org/doc/api/image_transport/html/classimage__transport_1_1CameraPublisher.html))

#### Published topics

`image_transport` publishers advertise individual ROS [Topics](Topics)
for each available transport - unlike ROS Publishers, which advertise a
single topic. The topic names follow a standard naming convention,
outlined below. Note, however, that all code interfaces take only a
"base topic" name; typically you should not directly reference the
transport-specific topic used by a particular plugin.

The raw <<MsgLink(sensor_msgs/Image)>> is published on the base
topic, just as with using a normal [roscpp](roscpp) `ros::Publisher`.
If additional plugins are available, they advertise subtopics of the
base topic, conventionally of the form `<base topic>/<transport
name>`. For example, using plugins for `"compressed"` and
`"theora"` transports, with a base topic of `/stereo/left/image`,
the topics would be:



```clearsilver
  pub {
  no_header=True
  0.name= stereo/left/image
  0.type= sensor_msgs/Image
  0.desc= Base topic, used for `"raw"` transport. Advertised just as if we used `ros::Publisher`.
  1.name= stereo/left/image/compressed
  1.type= <transport-specific type>
  1.desc= Topic for `"compressed"` transport.
  2.name= stereo/left/image/theora
  2.type= <transport-specific type>
  2.desc= Topic for `"theora"` transport.
  3.name= stereo/left/camera_info
  3.type= sensor_msgs/CameraInfo
  3.desc= (''`image_transport::CameraPublisher`-only'') Camera info topic.
}
```



#### Parameters

`image_transport` publishers have no independent parameters, but
plugins are permitted to make use of the
[Parameter Server](Parameter Server) for configuration options, e.g. bit
rate, compression level, etc. See the plugin package documentation.

Publisher plugin parameters give subscribers hooks to configure the
publisher-side encoding to suit the needs on the client side. Lookup
therefore occurs in the public namespace defined by `<base_topic>`,
rather than the private namespace of the publishing node. Note that
these parameters are a shared resource, controlling the behavior
observed by all subscribers to the image topic.

{

NOTE: This convention was changed in Diamondback, to support using
[dynamic_reconfigure](dynamic_reconfigure) for plugin parameters. }}}}


```
{#!wiki version diamondback_and_newer
Publisher plugin parameters should be exposed through [[dynamic_reconfigure]] for best visibility and ease of use. Conventionally, they take the following form:
{{{
#!clearsilver CS/NodeAPI
param {
  no_header= True
  group.0 {
    name=Reconfigurable parameters
    desc=
    0.name= <base topic>/<transport name>/<parameter name>
    0.type= type
    0.default= ?
    0.desc= Transport-specific publisher parameter.
    1.name= /camera/image/compressed/jpeg_quality
    1.type= int
    1.default= 80
    1.desc= An example transport-specific parameter which sets the JPEG quality for `"compressed"` transport for image topic `/camera/image`.
  }
}
```

 }}}}

### image_transport Subscribers

`image_transport` subscribers are used much like [roscpp](roscpp)'s
`ros::Subscriber`, but may use a specialized transport to receive
images.

C++: `image_transport::Subscriber`
([API](http://www.ros.org/doc/api/image_transport/html/classimage__transport_1_1Subscriber.html)),
`image_transport::CameraSubscriber`
([API](http://www.ros.org/doc/api/image_transport/html/classimage__transport_1_1CameraSubscriber.html))

#### Subscribed topics

A `Subscriber` instance is created with a "base topic" name and the
name of the transport to use. It subscribes to the transport-specific
ROS topic associated with the base topic. For example, if the base topic
is `/stereo/left/image`, the subscribed topics for transports
`"raw"` and `"compressed"` are respectively:



```clearsilver
sub {
  no_header=True
  0.name= stereo/left/image
  0.type= sensor_msgs/Image
  0.desc= Base topic, used for the default `"raw"` transport. Subscribed just as if we used `ros::Subscriber`.
  1.name= stereo/left/image/compressed
  1.type= <transport-specific type>
  1.desc= Topic for `"compressed"` transport.
  2.name= stereo/left/camera_info
  2.type= sensor_msgs/CameraInfo
  2.desc= (''`image_transport::CameraSubscriber`-only'') Camera info topic.
}
```

 

```clearsilver
param {
  0.name= ~image_transport
  0.default= "raw"
  0.type= string
  0.desc= Name of the transport to use.
}
```

 If this parameter is
not set, the transport from the `image_transport::TransportHints`
argument of `image_transport::ImageTransport::subscribe()` is used.

`image_transport::TransportHints` may be used to specify a different
namespace for parameter lookup. This is useful to remap
`image_transport` into a separate namespace to allow different
transports for different image subscriptions. The node writer may even
specify a parameter name other than `image_transport`, although this
is discouraged for the sake of consistency. Nodes that subscribe to
image topics should document what parameter(s) control transport,
especially if different from `image_transport`.

Subscriber plugins are permitted to make use of the
[Parameter Server](Parameter Server) for configuration options, e.g.
video post-processing level. See the plugin package documentation.

Subscriber plugin parameters configure the behavior of one particular
subscriber. They affect how the data received is interpreted (decoded).
This differs from publisher plugin parameters, which are a shared
resource affecting the data sent to all subscribers. The namespace used
for parameter lookup is again specified through
`image_transport::TransportHints`, defaulting to the private namespace
of the subscribing node.

{

NOTE: This convention was changed in Diamondback, to support using
[dynamic_reconfigure](dynamic_reconfigure) for plugin parameters. }}}}


```
{#!wiki version diamondback_and_newer

Subscriber plugin parameters should be exposed through [[dynamic_reconfigure]] for best visibility and ease of use. Conventionally, they take the following form:

{{{
#!clearsilver CS/NodeAPI
param {
  no_header= True
  group.0 {
    name=Reconfigurable parameters
    desc=
    0.name= ~<transport name>/<parameter name>
    0.type= type
    0.default= ?
    0.desc= Transport-specific subscriber parameter.
    1.name= ~theora/post_processing_level
    1.type= int
    1.default= 0
    1.desc= An example transport-specific parameter which sets the post-processing level when subscribed using `"theora"` transport.
  }
}
```

 }}}}

## Nodes



```clearsilver
node {
  0.name= republish
  0.desc= `republish` listens on one base image topic (using any transport type, `"raw"` by default) and republishes the images to another base topic. By default it uses all available publishing plugins; you may optionally specify a single out transport type. `"raw"` is the name of the default transport, publishing <<MsgLink(sensor_msgs/Image)>> messages. What other transports are available depends on which plugins are built.
}
```



#### Usage



```
$ rosrun image_transport republish [in_transport] in:=<in_base_topic> [out_transport] out:=<out_base_topic>
```



#### Examples

-   Suppose we are publishing images from a robot using the streaming
    video transport `"theora"`. On an offboard computer we have
    several nodes listening to the image topic. This setup wastes
    bandwidth and computation, as each node processes the compressed
    video into still images independently. Instead we can start a
    republish node on the offboard computer, streaming the video only to
    that node for processing into <<MsgLink(sensor_msgs/Image)>>
    messages republished to the other nodes: 

```
$ rosrun image_transport republish theora in:=camera/image raw out:=camera/image_decompressed
```


-   The above command is also useful simply to pipe a compressed image
    topic into a node that can only listen to
    <<MsgLink(sensor_msgs/Image)>> (because it uses
    `ros::Subscriber` or is written in a language other than C++).
-   If a node publishes images only as
    <<MsgLink(sensor_msgs/Image)>>, we can republish it using the
    full range of transports. Note however that the base topic must be
    different from the original topic, and this approach entails a
    slight overhead over using `image_transport::Publisher` in the
    original node. 

```cplusplus
// Use the image_transport classes instead.
#include <ros/ros.h>
#include <image_transport/image_transport.h>

void imageCallback(const sensor_msgs::ImageConstPtr& msg)
{
  // ...
}

ros::NodeHandle nh;
image_transport::ImageTransport it(nh);
image_transport::Subscriber sub = it.subscribe("in_image_base_topic", 1, imageCallback);
image_transport::Publisher pub = it.advertise("out_image_base_topic", 1);
```

0



```cplusplus
// Use the image_transport classes instead.
#include <ros/ros.h>
#include <image_transport/image_transport.h>

void imageCallback(const sensor_msgs::ImageConstPtr& msg)
{
  // ...
}

ros::NodeHandle nh;
image_transport::ImageTransport it(nh);
image_transport::Subscriber sub = it.subscribe("in_image_base_topic", 1, imageCallback);
image_transport::Publisher pub = it.advertise("out_image_base_topic", 1);
```

1

#### Parameters

`republish` itself does not make use of the
[Parameter Server](Parameter Server). Plugins may read or set
plugin-specific parameters, however.

## Command-line tools

### list_transports

`list_transports` lists the declared image transport options across
all ROS packages and attempts to determine whether they are currently
available for use (packages built, plugins able to be loaded properly,
etc.).

#### Usage



```cplusplus
// Use the image_transport classes instead.
#include <ros/ros.h>
#include <image_transport/image_transport.h>

void imageCallback(const sensor_msgs::ImageConstPtr& msg)
{
  // ...
}

ros::NodeHandle nh;
image_transport::ImageTransport it(nh);
image_transport::Subscriber sub = it.subscribe("in_image_base_topic", 1, imageCallback);
image_transport::Publisher pub = it.advertise("out_image_base_topic", 1);
```

2
