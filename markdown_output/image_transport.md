## Overview

When working with images we often want specialized transport strategies,
such as using image compression or streaming video codecs.
`image_transport` provides classes and nodes for transporting images
in arbitrary over-the-wire representations, while abstracting this
complexity so that the developer only sees
[sensor_msgs/msg/Image](https://docs.ros.org/en/rolling/p/sensor_msgs/msg/Image.html)
messages.

Specialized transports are provided by plugins. `image_transport`
itself provides only `"raw"` transport so as not to impose
unnecessary dependencies on client packages. Other transports will only
be available if they are built on your system. On Ubuntu, the
`ros-<distro>-base` debians include the `"compressed"` and
`"theora"` transports provided by the
[image_transport_plugins](https://index.ros.org/p/image_transport_plugins)
stack.

## Quickstart Guide

`image_transport` should always be used to publish and subscribe to
images. At this basic level of usage, it is very similar to using ROS
Publishers and Subscribers. Using `image_transport` instead of the ROS
primitives, however, gives you great flexibility in how images are
communicated between nodes.

For complete examples of publishing and subscribing to images using
`image_transport`, see the
[Tutorials](#tutorials).

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
[Roadmap](https://index.ros.org/p/image_common). If you need to
interface a Python node with some compressed image transport, try
interposing a [republish](#republish) node.

## Known Transport Packages

If you have implemented a new transport option in a public repository
and would like to see it added to this list, please email our
[mailing list](Mailing Lists).

- ros-pkg
- image_transport (`"raw"`) - The
  default transport, sending
  [sensor_msgs/msg/Image](https://docs.ros.org/en/rolling/p/sensor_msgs/msg/Image.html)
  through ROS.
- [compressed_image_transport](https://index.ros.org/p/compressed_image_transport)
  (`"compressed"`) - JPEG or PNG image compression.
- [theora_image_transport](https://index.ros.org/p/theora_image_transport)
  (`"theora"`) - Streaming video using the Theora codec.

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

The raw
[sensor_msgs/msg/Image](https://docs.ros.org/en/rolling/p/sensor_msgs/msg/Image.html)
is published on the base topic, just as with using a normal
[roscpp](https://index.ros.org/p/roscpp) `ros::Publisher`. If
additional plugins are available, they advertise subtopics of the base
topic, conventionally of the form `<base topic>/<transport name>`.
For example, using plugins for `"compressed"` and `"theora"`
transports, with a base topic of `/stereo/left/image`, the topics
would be:

- `stereo/left/image`
  ([sensor_msgs/msg/Image](https://docs.ros.org/en/rolling/p/sensor_msgs/msg/Image.html)):
  Base topic, used for `"raw"` transport. Advertised just as if we
  used `ros::Publisher`.
- `stereo/left/image/compressed` (`<transport-specific type>`): Topic
  for `"compressed"` transport.
- `stereo/left/image/theora` (`<transport-specific type>`): Topic for
  `"theora"` transport.
- `stereo/left/camera_info`
  ([sensor_msgs/msg/CameraInfo](https://docs.ros.org/en/rolling/p/sensor_msgs/msg/CameraInfo.html)):
  (*`image_transport::CameraPublisher`-only*) Camera info topic.

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
[dynamic_reconfigure](https://index.ros.org/p/dynamic_reconfigure) for
plugin parameters. }}}} 

```
{#!wiki version diamondback_and_newer
Publisher plugin parameters should be exposed through [[dynamic_reconfigure]] for best visibility and ease of use. Conventionally, they take the following form:

===== Reconfigurable parameters =====

 * {{{<base topic>/<transport name>/<parameter name>
```

 (`type`, default: `?`):
Transport-specific publisher parameter.

- `/camera/image/compressed/jpeg_quality` (`int`, default: `80`): An
  example transport-specific parameter which sets the JPEG quality for
  `"compressed"` transport for image topic `/camera/image`.

}}}}

### image_transport Subscribers

`image_transport` subscribers are used much like
[roscpp](https://index.ros.org/p/roscpp)'s `ros::Subscriber`, but may
use a specialized transport to receive images.

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

- `stereo/left/image`
  ([sensor_msgs/msg/Image](https://docs.ros.org/en/rolling/p/sensor_msgs/msg/Image.html)):
  Base topic, used for the default `"raw"` transport. Subscribed
  just as if we used `ros::Subscriber`.
- `stereo/left/image/compressed` (`<transport-specific type>`): Topic
  for `"compressed"` transport.
- `stereo/left/camera_info`
  ([sensor_msgs/msg/CameraInfo](https://docs.ros.org/en/rolling/p/sensor_msgs/msg/CameraInfo.html)):
  (*`image_transport::CameraSubscriber`-only*) Camera info topic.

#### Parameters

- `~image_transport` (`string`, default: `"raw"`): Name of the transport
  to use.

If this parameter is not set, the transport from the
`image_transport::TransportHints` argument of
`image_transport::ImageTransport::subscribe()` is used.

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
[dynamic_reconfigure](https://index.ros.org/p/dynamic_reconfigure) for
plugin parameters. }}}} 

```
{#!wiki version diamondback_and_newer

Subscriber plugin parameters should be exposed through [[dynamic_reconfigure]] for best visibility and ease of use. Conventionally, they take the following form:


===== Reconfigurable parameters =====

 * {{{~<transport name>/<parameter name>
```

 (`type`, default: `?`):
Transport-specific subscriber parameter.

- `~theora/post_processing_level` (`int`, default: `0`): An example
  transport-specific parameter which sets the post-processing level when
  subscribed using `"theora"` transport.

}}}}

## Nodes

### republish

`republish` listens on one base image topic (using any transport type,
`"raw"` by default) and republishes the images to another base
topic. By default it uses all available publishing plugins; you may
optionally specify a single out transport type. `"raw"` is the name
of the default transport, publishing
[sensor_msgs/msg/Image](https://docs.ros.org/en/rolling/p/sensor_msgs/msg/Image.html)
messages. What other transports are available depends on which plugins
are built.

#### Usage



```
$ rosrun image_transport republish [in_transport] in:=<in_base_topic> [out_transport] out:=<out_base_topic>
```



#### Examples

- Suppose we are publishing images from a robot using the streaming
  video transport `"theora"`. On an offboard computer we have
  several nodes listening to the image topic. This setup wastes
  bandwidth and computation, as each node processes the compressed video
  into still images independently. Instead we can start a republish node
  on the offboard computer, streaming the video only to that node for
  processing into
  [sensor_msgs/msg/Image](https://docs.ros.org/en/rolling/p/sensor_msgs/msg/Image.html)
  messages republished to the other nodes: 

```
$ rosrun image_transport republish theora in:=camera/image raw out:=camera/image_decompressed
```


- The above command is also useful simply to pipe a compressed image
  topic into a node that can only listen to
  [sensor_msgs/msg/Image](https://docs.ros.org/en/rolling/p/sensor_msgs/msg/Image.html)
  (because it uses `ros::Subscriber` or is written in a language other
  than C++).
- If a node publishes images only as
  [sensor_msgs/msg/Image](https://docs.ros.org/en/rolling/p/sensor_msgs/msg/Image.html),
  we can republish it using the full range of transports. Note however
  that the base topic must be different from the original topic, and
  this approach entails a slight overhead over using
  `image_transport::Publisher` in the original node.
  

```
$ rosrun image_transport republish raw in:=camera/image out:=camera/image_repub
```



#### Subscribed Topics

- `in` (`<transport-specific type>`): The image base topic to listen on
  (may actually subscribe to a subtopic).

#### Published Topics

- `out` (`<transport-specific type>`): The image base topic to publish
  to (may also publish subtopics).

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



```
$ rosrun image_transport list_transports
```

## Tutorials

To learn how to use the existing `republish` node to change an image
transport type (ie compress and decompress image streams), scroll down
the image_transport package page to the
**Nodes** section.

Otherwise, continue reading this page.

Before starting any of the `image_transport` tutorials below, take the
time to create a scratch package to work in and manipulate the example
code. Create a sandbox package with the following dependencies:


```
{#!wiki buildsystem rosbuild
{{{
$ roscreate-pkg learning_image_transport image_transport cv_bridge
```

 Make sure that the `learning_image_transport`
directory is included in your `ROS_PACKAGE_PATH` and build it:


```
$ rosmake learning_image_transport
```

 }}}} 

```
{#!wiki buildsystem catkin
{{{
$ mkdir -p ~/image_transport_ws/src
$ cd ~/image_transport_ws/src
$ source /opt/ros/indigo/setup.bash
$ catkin_create_pkg learning_image_transport image_transport cv_bridge
```

 Make sure to
include the correct `setup` file, in the above example it is for ROS
Indigo on Ubuntu and for `bash`. Once you have created the empty
package, build it: 

```
$ cd ~/image_transport_ws
$ rosdep install --from-paths src -i -y --rosdistro indigo
$ catkin_make
$ source devel/setup.bash
```

 }}}}

### Beginner Tutorials

- [\## multi-line description to be displayed in search](#-multi-line-description-to-be-displayed-in-search):
  \## the next tutorial description (optional)
- [Running the Simple Image Publisher and Subscriber with Different Transports](#running-the-simple-image-publisher-and-subscriber-with-different-transports):
  This tutorial discusses running the simple image publisher and
  subscriber using multiple transports.
- [Managing Transport Plugins](#managing-transport-plugins):
  This tutorial covers how to discover which transport plugins are
  included in your system and make them available for use. No
  programming required!
- [Writing a Simple Image Publisher (C++)](#writing-a-simple-image-publisher-c):
  This tutorial shows how to publish images using all available
  transports.
- [Writing a Simple Image Subscriber (C++)](#writing-a-simple-image-subscriber-c):
  This tutorial shows how to subscribe to images using any available
  transport. By using the `image_transport` subscriber to subscribe to
  images, any image transport can be used at run-time. To learn how to
  actually use a specific image transport, see the next tutorial.

### Intermediate Tutorials

- [\## multi-line description to be displayed in search](#-multi-line-description-to-be-displayed-in-search):
  \## the next tutorial description (optional)
- [Writing a New Transport](#writing-a-new-transport):
  This tutorials covers how to write publisher and subscriber plugins
  for a new image transport option.

### Create a new tutorial

## Troubleshooting

### Errors when using package

#### Error: I want to use transport "foo", but it's not advertised

**Example:** 

```
$ rostopic list
/camera/image
/camera/image/compressed

# No listing for /camera/image/foo
```



**Solution:**

- Does transport `"foo"` exist? Is the package providing it built?
  See the
  [Managing Transport Plugins](#managing-transport-plugins)
  tutorial, which will show you how to find out which transports are
  available and enabled on your system.

## ## multi-line description to be displayed in search

## Running the Simple Image Publisher and Subscriber with Different Transports

- **Note:** This tutorial assumes that you have completed the previous
  tutorials:
  [Writing a Simple Image Publisher](#writing-a-simple-image-publisher-c),
  [Writing a Simple Image Subscriber](#writing-a-simple-image-subscriber-c).
- **Description:** This tutorial discusses running the simple image
  publisher and subscriber using multiple transports.
- **Tutorial Level:** BEGINNER
- **Next Tutorial:**
  [Managing Transport Plugins](#managing-transport-plugins)

### Running the Publisher

Make sure that a roscore is up and running:



```
$ roscore
```

 In a previous tutorial we made a publisher node
called "my_publisher"; now run the node with an image file as the
command-line argument:



```
$ rosrun image_transport_tutorial my_publisher path/to/some/image.jpg
```

 To check that your node is running properly,
list the topics being published:



```
$ rostopic list -v
```

 Look for `/camera/image` in the output, which
should look something like:



```
Published topics:
 * /rosout [roslib/Log] 1 publisher
 * /camera/image [sensor_msgs/Image] 1 publisher
 * /rosout_agg [roslib/Log] 1 publisher

Subscribed topics:
 * /rosout [roslib/Log] 1 subscriber
```

 If you have non-default transport plugins
built, you may see additional published topics in the `/camera/image/`
namespace.

### Running the Subscriber

In the last tutorial, we made a subscriber node called
"my_subscriber"; now run it:



```
$ rosrun image_transport_tutorial my_subscriber
```

 You should see a window pop up with the image
you gave to the publisher.

Let's look at the node graph:



```
$ rosrun rqt_graph rqt_graph
```


![attachment:transport_graph.png](doc/transport_graph.png)

### Changing the Transport Used

Currently our nodes are communicating raw
[sensor_msgs/msg/Image](https://docs.ros.org/en/rolling/p/sensor_msgs/msg/Image.html)
messages, so we are not gaining anything over using `ros::Publisher`
and `ros::Subscriber`. Let's change that by introducing a new
transport.

The `compressed_image_transport` package provides plugins for the
"compressed" transport, which sends images over the wire in either
JPEG- or PNG-compressed form. Notice that `compressed_image_transport`
is not a dependency of your package; `image_transport` will
automatically discover all transport plugins built in your ROS system.

Shut down your publisher node and restart it. If you list the published
topics again, you should see a new one:



```
* /camera/image/compressed [sensor_msgs/CompressedImage] 1 publisher
```



Now let's start up a new subscriber, this one using compressed
transport. The key is that `image_transport` subscribers check the
parameter `image_transport` for the name of a transport to use in
place of "raw". Let's set this parameter and start a subscriber node
with name "compressed_listener":



```
$ rosparam set /compressed_listener/image_transport compressed
$ rosrun image_transport_tutorial my_subscriber __name:=compressed_listener
```



You should see an identical image window pop up. Let's check the node
graph again:



```
$ rosrun rqt_graph rqt_graph
```


![attachment:transport_graph_with_compressed.png](doc/transport_graph_with_compressed.png)

`compressed_listener` is listening to a separate topic carrying
JPEG-compressed versions of the same images published on
`/camera/image`.

Note that if you just want the compressed image, you can change the
parameter globally in-line: 

```
$ rosrun image_transport_tutorial my_subscriber _image_transport:=compressed
```



### Changing Transport-Specific Behavior

For a particular transport, we may want to tweak settings such as
compression level, bit rate, etc. Transport plugins can expose such
settings through
[rqt_reconfigure](https://index.ros.org/p/rqt_reconfigure). For example,
`/camera/image/compressed` allows you to change the compression format
and quality on the fly; see the
[package documentation](https://index.ros.org/p/compressed_image_transport)
for full details.

For now let's adjust the JPEG quality. By default, "compressed"
transport uses JPEG compression at 80% quality; let's change it to 15%:



```
$ rosrun rqt_reconfigure rqt_reconfigure
```



Now pick /camera/image/compressed in the drop-down menu and move the
jpeg_quality slider down to 15%. Do you see the compression artifacts in
your second view window?

Dynamic Reconfigure has updated the dynamically reconfigurable parameter
/camera/image/compressed/jpeg_quality. You can verify this by running:



```
$ rosparam get /camera/image/compressed/jpeg_quality
```



This should display 15.

## Managing Transport Plugins

- **Note:** This tutorial assumes that you have completed the previous
  tutorials: [ROS tutorials](ROS/Tutorials).
- **Description:** This tutorial covers how to discover which transport
  plugins are included in your system and make them available for use.
  No programming required!
- **Tutorial Level:** BEGINNER

### Finding available transports

`image_transport` searches your ROS installation for transport plugins
at runtime and dynamically loads all that are built. This affords you
great flexibility in adding additional transports, but makes it unclear
which are available on your system. `image_transport` provides a
`list_transports` executable for this purpose:



```
$ rosrun image_transport list_transports
Declared transports:
image_transport/compressed (*): Not available. Try 'rosmake compressed_image_transport'.
image_transport/compressedDepth (*): Not available. Try 'rosmake compressed_depth_image_transport'.
image_transport/raw
image_transport/theora (*): Not available. Try 'rosmake theora_image_transport'.

Details:
----------
"image_transport/compressed"
*** Plugins are not built. ***
 - Provided by package: compressed_image_transport
 - Publisher: This plugin publishes a CompressedImage using either JPEG or PNG compression.
 - Subscriber: This plugin decompresses a CompressedImage topic.
----------
"image_transport/compressedDepth"
*** Plugins are not built. ***
 - Provided by package: compressed_depth_image_transport
 - Publisher: This plugin publishes a compressed depth images using PNG compression.
 - Subscriber: This plugin decodes a compressed depth images.
----------
"image_transport/raw"
 - Provided by package: image_transport
 - Publisher: This is the default publisher. It publishes the Image as-is on the base topic.
 - Subscriber: This is the default pass-through subscriber for topics of type sensor_msgs/Image.
----------
"image_transport/theora"
*** Plugins are not built. ***
 - Provided by package: theora_image_transport
 - Publisher: This plugin publishes a video packet stream encoded using Theora.
 - Subscriber: This plugin decodes a video packet stream encoded using Theora.
```



This the expected output for an otherwise new ROS installation after
completing the previous tutorials. Depending on your setup, you may
already have "theora" or other transports available.

The first lines of output list "Declared transports" in your ROS
system. "compressed" and "raw" we have seen in the previous
tutorials. "theora" is new, and the asterisk next to its name
indicates that `list_transports` was unable to load the corresponding
plugins.

In the "Details" section, we can see what packages provide the various
transports, short descriptions of the plugins, whether a plugin failed
to load (and why), and (if applicable) suggestions for troubleshooting.

### Adding new transports

Let's add "theora" streaming video support to all ROS applications
using `image_transport` to send images. The easiest is to isntall
packages:



```
$ sudo apt-get install ros-indigo-theora-image-transport
```



But you can also build from source.



```
{#!wiki buildsystem rosbuild
For rosbuild you need to execute:

{{{
$ rosmake theora_image_transport
```

 }}}} 

```
{#!wiki buildsystem catkin
For catkin, just follow the instructions and build the packages in the workspace in which they exist and source the resulting `setup.*sh` file.
```

}

## Writing a Simple Image Publisher (C++)

- **Note:** This tutorial assumes that you have completed the previous
  tutorials: [ROS tutorials](ROS/Tutorials),
  [Using CvBridge to Convert Between ROS Images and OpenCV Images](https://index.ros.org/p/cv_bridge).
- **Description:** This tutorial shows how to publish images using all
  available transports.
- **Tutorial Level:** BEGINNER
- **Next Tutorial:**
  [Writing a Simple Image Subscriber](#writing-a-simple-image-subscriber-c)

### Writing a Simple Image Publisher

Here we'll create the publisher node which will continually publish an
image.

Change to the directory you've created for these tutorials:



```
{#!wiki buildsystem rosbuild
{{{
$ roscd image_transport_tutorial
```

 }}}} 

```
{#!wiki buildsystem catkin
''(Assuming you have created your package in `~/image_transport_ws`)''
{{{
$ cd ~/image_transport_ws/
$ git clone https://github.com/ros-perception/image_common.git
$ mkdir src
$ ln -s `pwd`/image_common/image_transport/tutorial/ ./src/image_transport_tutorial
```

 }}}}

#### The Code



```
{#!wiki buildsystem rosbuild
{{{
First, create `src/my_publisher.cpp` in package `image_transport_tutorial` with your favorite editor, and place the following inside it:
```

 }}}} 

```wiki
Have a look at `my_publisher.cpp`:
```




```cplusplus
#include <ros/ros.h>
#include <image_transport/image_transport.h>
#include <opencv2/highgui/highgui.hpp>
#include <cv_bridge/cv_bridge.h>

int main(int argc, char** argv)
{
  ros::init(argc, argv, "image_publisher");
  ros::NodeHandle nh;
  image_transport::ImageTransport it(nh);
  image_transport::Publisher pub = it.advertise("camera/image", 1);
  cv::Mat image = cv::imread(argv[1], CV_LOAD_IMAGE_COLOR);
  cv::waitKey(30);
  sensor_msgs::ImagePtr msg = cv_bridge::CvImage(std_msgs::Header(), "bgr8", image).toImageMsg();

  ros::Rate loop_rate(5);
  while (nh.ok()) {
    pub.publish(msg);
    ros::spinOnce();
    loop_rate.sleep();
  }
}
```



#### The Code Explained

Now, let's break down the code piece by piece. For lines not explained
here, review
[Writing a Simple Publisher and Subscriber (C++)](http://www.ros.org/wiki/ROS/Tutorials/WritingPublisherSubscriber(c++)).
`image_transport/image_transport.h` includes everything we need to
publish and subscribe to images. These headers will allow us to load an
image using OpenCV and convert it to the ROS message format. We create
an `ImageTransport` instance, initializing it with our `NodeHandle`.
We use methods of `ImageTransport` to create image publishers and
subscribers, much as we use methods of `NodeHandle` to create generic
ROS publishers and subscribers. Advertise that we are going to be
publishing images on the base topic "camera/image". Depending on
whether more plugins are built, additional (per-plugin) topics derived
from the base topic may also be advertised. The second argument is the
size of our publishing queue.

`advertise()` returns an `image_transport::Publisher` object, which
serves two purposes: 1) it contains a `publish()` method that lets you
publish images onto the base topic it was created with, and 2) when it
goes out of scope, it will automatically unadvertise.. See
[this tutorial](https://index.ros.org/p/cv_bridge) for more on
ROS-OpenCV image conversion. We broadcast the image to anyone connected
to one of our topics, exactly as we would have using a
`ros::Publisher`.

#### Adding video stream from a webcam

The example above requires a path of an image file to be added as a
command line parameter (`cv::imread(argv\[1\], CV_LOAD_IMAGE_COLOR)`).
This image will be converted and send as a message to an image
subscriber. In most cases however this is not a very practical example
since often you are required to handle streaming data (for example:
multiple webcameras mounted on a robot record the scene around it and
you have to pass the image date to some other node for further
analysis). You can modify the example quite easily to make it work with
a video device supported by `cv::VideoCapture` (in case it is not you
have to handle it accordingly):



```cplusplus
#include <ros/ros.h>
#include <image_transport/image_transport.h>
#include <opencv2/highgui/highgui.hpp>
#include <cv_bridge/cv_bridge.h>
#include <sstream> // for converting the command line parameter to integer

int main(int argc, char** argv)
{
  // Check if video source has been passed as a parameter
  if(argv[1] == NULL) return 1;

  ros::init(argc, argv, "image_publisher");
  ros::NodeHandle nh;
  image_transport::ImageTransport it(nh);
  image_transport::Publisher pub = it.advertise("camera/image", 1);

  // Convert the passed as command line parameter index for the video device to an integer
  std::istringstream video_sourceCmd(argv[1]);
  int video_source;
  // Check if it is indeed a number
  if(!(video_sourceCmd >> video_source)) return 1;

  cv::VideoCapture cap(video_source);
  // Check if video device can be opened with the given index
  if(!cap.isOpened()) return 1;
  cv::Mat frame;
  sensor_msgs::ImagePtr msg;

  ros::Rate loop_rate(5);
  while (nh.ok()) {
    cap >> frame;
    // Check if grabbed frame is actually full with some content
    if(!frame.empty()) {
      msg = cv_bridge::CvImage(std_msgs::Header(), "bgr8", frame).toImageMsg();
      pub.publish(msg);
      cv::waitKey(1);
    }

    ros::spinOnce();
    loop_rate.sleep();
  }
}
```



If you have a single device you do not need to do the whole routine with
passing a command line argument (`argv\[1\]`) and parsing it at all.
In this case you can hard-code the index/address of the device and
directly pass it to the video capturing structure in OpenCV (example:
`cv::VideoCapture(0)` if /dev/video0 is used). In addition multiple
checks are also included here to make sure that the publisher does not
brake if in case the camera is shut downs or similar issue). If the
retrieved frame from the video device is not empty it will be then
converted to a ROS message, which will be published by the publisher.

### Building your node



```
{#!wiki buildsystem rosbuild
Add the following line to your `CMakeLists.txt` file:
{{{
rosbuild_add_executable(my_publisher src/my_publisher.cpp)
```



and do



```
$ make
```

 }}}} 

```
{#!wiki buildsystem catkin
Just run:
{{{
catkin_make
```

 }}}} Now let's
[write a simple image subscriber](#writing-a-simple-image-subscriber-c).

## Writing a Simple Image Subscriber (C++)

- **Note:** This tutorial assumes that you have completed the previous
  tutorials: [ROS tutorials](ROS/Tutorials),
  [Using CvBridge to Convert Between ROS Images and OpenCV Images](https://index.ros.org/p/cv_bridge).
- **Description:** This tutorial shows how to subscribe to images using
  any available transport. By using the `image_transport` subscriber
  to subscribe to images, any image transport can be used at run-time.
  To learn how to actually use a specific image transport, see the next
  tutorial.
- **Tutorial Level:** BEGINNER
- **Next Tutorial:**
  [Running the Simple Image Publisher and Subscriber with Different Transports](#running-the-simple-image-publisher-and-subscriber-with-different-transports)

### Writing a Simple Image Subscriber

Here we'll create the subscriber node which will display an image topic
on screen.



```
{#!wiki buildsystem rosbuild
Change to the directory you've created for these tutorials:
{{{
$ roscd image_transport_tutorial
```

 }}}} 

```
{#!wiki buildsystem catkin
''(Assuming you have created your package in `~/image_transport_ws`)''
{{{
$ cd ~/image_transport_ws/src/image_transport_tutorial
```

 }}}}

#### The Code



```
{#!wiki buildsystem rosbuild
First, create `src/my_subscriber.cpp` in package `learning_image_transport` with your favorite editor, and place the following inside it:
```

} 

```
{#!wiki buildsystem catkin
Have a look at the `src/my_subscriber.cpp` file:
```

}



```cplusplus
#include <ros/ros.h>
#include <image_transport/image_transport.h>
#include <opencv2/highgui/highgui.hpp>
#include <cv_bridge/cv_bridge.h>

void imageCallback(const sensor_msgs::ImageConstPtr& msg)
{
  try
  {
    cv::imshow("view", cv_bridge::toCvShare(msg, "bgr8")->image);
    cv::waitKey(30);
  }
  catch (cv_bridge::Exception& e)
  {
    ROS_ERROR("Could not convert from '%s' to 'bgr8'.", msg->encoding.c_str());
  }
}

int main(int argc, char **argv)
{
  ros::init(argc, argv, "image_listener");
  ros::NodeHandle nh;
  cv::namedWindow("view");

  image_transport::ImageTransport it(nh);
  image_transport::Subscriber sub = it.subscribe("camera/image", 1, imageCallback);
  ros::spin();
  cv::destroyWindow("view");
}
```



#### The Code Explained

Now, let's break down the code piece by piece. For lines not explained
here, review
[Writing a Simple Publisher and Subscriber (C++)](http://www.ros.org/wiki/ROS/Tutorials/WritingPublisherSubscriber(c++)).
`image_transport/image_transport.h` includes everything we need to
publish and subscribe to images. These headers will allow us to display
images using OpenCV's simple GUI capabilities. type. All image
encoding/decoding is handled automagically for you. The body of the
callback. We convert the ROS image message to an OpenCV image with BGR
pixel encoding, then show it in a display window. See
[this tutorial](https://index.ros.org/p/cv_bridge) for more on
ROS-OpenCV image conversion. Create an OpenCV display window. We create
an `ImageTransport` instance, initializing it with our `NodeHandle`.
We use methods of `ImageTransport` to create image publishers and
subscribers, much as we use methods of `NodeHandle` to create generic
ROS publishers and subscribers.. ROS will call the "imageCallback"
function whenever a new image arrives. The 2nd argument is the queue
size.

`subscribe()` returns an `image_transport::Subscriber` object, that
you must hold on to until you want to unsubscribe. When the
`Subscriber` object is destructed, it will automatically unsubscribe
from the "camera/image" base topic.

There are versions of the `subscribe()` function which allow you to
specify a class member function, or even anything callable by a
Boost.Function object. Dispose of our display window.

In just a few lines of code, we have written a ROS image viewer that can
handle images in both raw and a variety of compressed forms. In fact,
this is a stripped-down version of
[image_view](https://index.ros.org/p/image_view).

### Building your node



```
{#!wiki buildsystem rosbuild
Add the following line to your `CMakeLists.txt` file:
{{{
rosbuild_add_executable(my_subscriber src/my_subscriber.cpp)
```



and do



```
$ make
```

 }}}} 

```
{#!wiki buildsystem catkin
Just run:

{{{
$ catkin_make
```

 }}}}

Next let's
[run our publisher and subscriber with different image transports](#running-the-simple-image-publisher-and-subscriber-with-different-transports).

## Writing a New Transport

- **Note:** This tutorial assumes that you have completed the previous
  tutorials:
  [image_transport Beginner Tutorials](#tutorials),
  [pluginlib](https://index.ros.org/p/pluginlib).
- **Description:** This tutorials covers how to write publisher and
  subscriber plugins for a new image transport option.
- **Tutorial Level:** INTERMEDIATE

NOTE: This tutorial is incomplete.

### Overview

The real power of `image_transport` comes from its extensibility.
Nodes using `image_transport` to publish and receive images can take
advantage of new transports without so much as a recompile. In this
tutorial we will see how to write our own transport for a very simple
kind of "compression": subsampling on the publisher side, then
supersampling back to the original dimensions on the client side.

There are four steps to writing a transport: 1. Define your
transport-specific message type. For example, a streaming video
transport would use some `Packet` type for internal communication. 2.
Write your publisher plugin. This encodes a
[sensor_msgs/msg/Image](https://docs.ros.org/en/rolling/p/sensor_msgs/msg/Image.html)
into one or more instances of the transport-specific message type and
publishes them on the dedicated transport topic. 3. Write your
subscriber plugin. This listens on the transport topic and decodes the
transport-specific messages back into
[sensor_msgs/msg/Image](https://docs.ros.org/en/rolling/p/sensor_msgs/msg/Image.html)
messages passed to the user callback. 4. Register your transport plugins
so that `image_transport` can find them.

The above outline assumes that your transport uses a single ROS topic
for all publisher-subscriber communication, which should normally be the
case. This assumption allows us to use the C++ base classes
[SimplePublisherPlugin](http://www.ros.org/doc/api/image_transport/html/classimage__transport_1_1SimplePublisherPlugin.html)
and
[SimpleSubscriberPlugin](http://www.ros.org/doc/api/image_transport/html/classimage__transport_1_1SimpleSubscriberPlugin.html).
These classes take care of all the scaffolding and bookkeeping so that
we can simply get on with writing our encoding and decoding functions.
If for some reason your transport requires a more exotic communication
structure, it is possible (but much less pleasant!) to subclass the
lower-level base classes
[PublisherPlugin](http://www.ros.org/doc/api/image_transport/html/classimage__transport_1_1PublisherPlugin.html)
and
[SubscriberPlugin](http://www.ros.org/doc/api/image_transport/html/classimage__transport_1_1SubscriberPlugin.html)
instead.

The code for that tutorial is in the tutorial folder of image_transport
at: <https://github.com/ros-perception/image_common>

### Defining the Message Type

Create `msg/ResizedImage.msg` in package `learning_image_transport`
with your favorite editor, and place the following inside it:


```
uint32 original_height
uint32 original_width
sensor_msgs/Image image
```



Our message is very simple: we store the subsampled image along with its
original dimensions, so that we can later restore it (with some loss of
information, of course).

### Writing a Simple Publisher Plugin

#### The Code

Create `include/image_transport_tutorial/resized_publisher.h` and
place the following inside it: 

```cplusplus
#include <image_transport/simple_publisher_plugin.h>
#include "learning_image_transport/ResizedImage.h"

class ResizedPublisher : public image_transport::SimplePublisherPlugin<learning_image_transport::ResizedImage>
{
public:
  virtual std::string getTransportName() const
  {
    return "resized";
  }

protected:
  virtual void publish(const sensor_msgs::Image& message,
                       const PublishFn& publish_fn) const;
};
```



Next create `src/resized_publisher.cpp` and place the following inside
it: 

```cplusplus
#include <image_transport_tutorial/resized_publisher.h>
#include <opencv2/imgproc/imgproc.hpp>
#include <cv_bridge/cv_bridge.h>

void ResizedPublisher::publish(const sensor_msgs::Image& message,
                               const PublishFn& publish_fn) const
{
  cv::Mat cv_image;
  boost::shared_ptr<void const> tracked_object;
  try
  {
    cv_image = cv_bridge::toCvShare(message, tracked_object, message.encoding)->image;
  }
  catch (cv::Exception &e)
  {
    ROS_ERROR("Could not convert from '%s' to '%s'.", message.encoding.c_str(), message.encoding.c_str());
    return;
  }

  // Retrieve subsampling factor from the parameter server
  double subsampling_factor;
  std::string param_name;
  nh().param<double>("resized_image_transport_subsampling_factor", subsampling_factor, 2.0);

  // Rescale image
  int new_width = cv_image.cols / subsampling_factor + 0.5;
  int new_height = cv_image.rows / subsampling_factor + 0.5;
  cv::Mat buffer;
  cv::resize(cv_image, buffer, cv::Size(new_width, new_height));

  // Set up ResizedImage and publish
  image_transport_tutorial::ResizedImage resized_image;
  resized_image.original_height = cv_image.rows;
  resized_image.original_width = cv_image.cols;
  resized_image.image = *(cv_bridge::CvImage(message.header, "bgr8", cv_image).toImageMsg());
  publish_fn(resized_image);
}
```



#### The Code Explained

Starting with `resized_publisher.h`: We include the headers for our
base class and transport-specific message type. We declare our publisher
plugin class, inheriting from `SimplePublisherPlugin`.
`SimplePublisherPlugin` is templated on the transport-specific message
type. `SimplePublisherPlugin` requires us to implement only two
functions, and one of them is dead simple! `getTransportName()`
returns the name of the transport; we have chosen `"resized"`. The
other required function is an internal (protected) version of
`publish()`. This is where we encode the
[sensor_msgs/msg/Image](https://docs.ros.org/en/rolling/p/sensor_msgs/msg/Image.html)
argument into a `ResizedImage` and publish it. But what is that
`PublishFn` argument? This type is defined by
`SimplePublisherPlugin`. `PublishFn` is a function object that takes
our transport-specific message type as an argument and publishes it
using some ROS primitive.

Why this indirection? It turns out that in ROS there are two distinct
ways to publish messages to a subscriber. The normal way is to broadcast
a message to all subscribers; the other way, seldom used, is to publish
a message to a single subscriber within a subscriber status callback.
`SimplePublisherPlugin` performs some tricky plumbing to use our
implementation of `publish()` in both cases.

For the details of `publish()`, the code is self-explanatory.

### Writing a Simple Subscriber Plugin

#### The Code

Create `include/learning_image_transport/resized_subscriber.h` and
place the following inside it: 

```cplusplus
#include <image_transport/simple_subscriber_plugin.h>
#include <image_transport_tutorial/ResizedImage.h>

class ResizedSubscriber : public image_transport::SimpleSubscriberPlugin<image_transport_tutorial::ResizedImage>
{
public:
  virtual ~ResizedSubscriber() {}

  virtual std::string getTransportName() const
  {
    return "resized";
  }

protected:
  virtual void internalCallback(const typename image_transport_tutorial::ResizedImage::ConstPtr& message,
                                const Callback& user_cb);
};
```



Next create `src/resized_subscriber.cpp` and place the following
inside it: 

```cplusplus
#include <image_transport_tutorial/resized_subscriber.h>
#include <cv_bridge/cv_bridge.h>
#include <opencv2/imgproc/imgproc.hpp>

void ResizedSubscriber::internalCallback(const image_transport_tutorial::ResizedImage::ConstPtr& msg,
                                         const Callback& user_cb)
{
  // This is only for optimization, not to copy the image
  boost::shared_ptr<void const> tracked_object_tmp;
  cv::Mat img_rsz = cv_bridge::toCvShare(msg->image, tracked_object_tmp)->image;
  // Resize the image to its original size
  cv::Mat img_restored;
  cv::resize(img_rsz, img_restored, cv::Size(msg->original_width, msg->original_height));

  // Call the user callback with the restored image
  cv_bridge::CvImage cv_img(msg->image.header, msg->image.encoding, img_restored);
  user_cb(cv_img.toImageMsg());
};
```



#### The Code Explained

### Registering the Transport Plugins

We have written our transport plugins, but some steps remain to register
them with ROS so that `image_transport` can find them. For details on
these steps, see [pluginlib](https://index.ros.org/p/pluginlib); below
we will note only features of special relevance to `image_transport`.

#### Adding to the Plugin List

Create `src/manifest.cpp` and place the following inside it:



```cplusplus
#include <pluginlib/class_list_macros.h>
#include <image_transport_tutorial/resized_publisher.h>
#include <image_transport_tutorial/resized_subscriber.h>

PLUGINLIB_REGISTER_CLASS(resized_pub, ResizedPublisher, image_transport::PublisherPlugin)

PLUGINLIB_REGISTER_CLASS(resized_sub, ResizedSubscriber, image_transport::SubscriberPlugin)
```



We register our plugin classes as `resized_pub` and `resized_sub`.
These names follow an important convention; `image_transport` assumes
that for a transport named `<foo>`, the publisher and subscriber
plugins have respective lookup names `<foo>_pub` and
`<foo>_sub`.

We register our plugins as instances of the low-level base classes
`PublisherPlugin` and `SubscriberPlugin`. The "simple" base
classes we used in our code subclass `PublisherPlugin` and
`SubscriberPlugin` to provide a more convenient high-level interface.

#### Writing the Plugin Description File

Now create `resized_plugins.xml` in the `learning_image_transport/`
directory and place the following inside it:



```
<library path="lib/libresized_image_transport">
  <class name="resized_pub" type="ResizedPublisher" base_class_type="image_transport::PublisherPlugin">
    <description>
      This plugin publishes a decimated version of the image.
    </description>
  </class>

  <class name="resized_sub" type="ResizedSubscriber" base_class_type="image_transport::SubscriberPlugin">
    <description>
      This plugin rescales a decimated image to its original size.
    </description>
  </class>
</library>
```



This file helps ROS to automatically discover, load and reason about our
plugins.

#### Exporting the Plugins

Finally, we must point to our plugin description file within the package
[Manifest](Manifest). Insert the following lines in your
`package.xml`:



```xml
<export>
  <image_transport plugin="${prefix}/resized_plugins.xml"/>
</export>
```



### Building Your Transport

In your `CMakeLists.txt`, uncomment `rosbuild_genmsg()` (to generate
our `ResizedImage` message) and build our plugins as a library:



```
cmake_minimum_required(VERSION 2.8)
project(image_transport_tutorial)

find_package(catkin REQUIRED cv_bridge genmsg image_transport sensor_msgs)

# add the resized image message
add_message_files(DIRECTORY msg
   FILES ResizedImage.msg
)
generate_messages(DEPENDENCIES sensor_msgs)

catkin_package()

find_package(OpenCV)

include_directories(include ${OpenCV_INCLUDE_DIRS})

# add the plugin examples
add_library(resized_publisher src/manifest.cpp src/resized_publisher.cpp src/resized_subscriber.cpp)
target_link_libraries(resized_publisher ${catkin_LIBRARIES} ${OpenCV_LIBRARIES})
```



### Using Your Transport
