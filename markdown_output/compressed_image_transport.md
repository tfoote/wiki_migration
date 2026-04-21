## Overview

\`compressed_image_transport\` is a plugin package for
[image_transport](image_transport). It enables any node using
\`image_transport\` classes to publish and subscribe to compressed image
topics. Compression format (JPEG or PNG) and quality can be changed on
the fly.

\'\'\'\'\'Before reading this page, make sure you understand the
[image_transport](image_transport) package\'\'\'\'\'

## Tutorials

See [image_transport/Tutorials](image_transport/Tutorials) for general
instruction on using \`image_transport\`. \`compressed_image_transport\`
is featured in the \`image_transport\` tutorial
[Examining the Simple Image Publisher and Subscriber](image_transport/Tutorials/ExaminingImagePublisherSubscriber).

## ROS API

```clearsilver
name = Publisher plugin
desc =
pub {
  0.name = <base_topic>/compressed
  0.type = sensor_msgs/CompressedImage
  0.desc = Compressed transport subtopic.
}
```

{

}}}}

```wiki
[[Included page compressed_image_transport/diamondback_params not found]]
```

```clearsilver
name = Subscriber plugin
desc =
sub {
  0.name = <base_topic>/compressed
  0.type = sensor_msgs/CompressedImage
  0.desc = Compressed transport subtopic.
}
```

## Publishing compressed images directly

Some cameras (particularly webcams) output their image data already in
JPEG format. When writing a driver for such a camera, a quick and dirty
approach is to simply copy the JPEG data into a
\<\<MsgLink(sensor_msgs/CompressedImage)\>\> message and publish it on a
topic of the form \`image_raw/compressed\`. Then any ROS node using
[image_transport](image_transport) can subscribe to \`image_raw\` with
transport \`compressed\`, just as if \`image_transport\` were used on
the publisher side. Of course, the other transport topics (including
\`image_raw\` itself) will not be available.
