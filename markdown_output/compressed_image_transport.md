## Overview

`compressed_image_transport` is a plugin package for
[image_transport](https://index.ros.org/p/image_transport). It enables
any node using `image_transport` classes to publish and subscribe to
compressed image topics. Compression format (JPEG or PNG) and quality
can be changed on the fly.

**`'Before reading this page, make sure you understand the [[https://index.ros.org/p/image_transport|image_transport]] package`**'

## Tutorials

See [Tutorials](https://index.ros.org/p/image_transport) for general
instruction on using `image_transport`. `compressed_image_transport`
is featured in the `image_transport` tutorial
[Examining the Simple Image Publisher and Subscriber](https://index.ros.org/p/image_transport).

## ROS API

### Publisher plugin

#### Published Topics

- `<base_topic>/compressed`
  ([sensor_msgs/msg/CompressedImage](https://docs.ros.org/en/rolling/p/sensor_msgs/msg/CompressedImage.html)):
  Compressed transport subtopic.

{

}}}}



```wiki

{
```

}



```
{#!wiki version noetic_and_newer

==== Parameters ====

===== Reconfigurable parameters =====

Starting in Diamondback, all publisher parameters are dynamically reconfigurable per-topic. See [[dynamic_reconfigure]] for details on dynamically reconfigurable parameters.

 * {{{<base_topic>/compressed/format
```

 (`string`, default: `jpeg`): Compression format
to use, "jpeg" or "png".

- `<base_topic>/compressed/jpeg_quality` (`int`, default: `80`): JPEG
  quality percentile, in the range \[1, 100\]. Lower values trade image
  quality for space savings.
- `<base_topic>/compressed/jpeg_progressive` (`bool`, default: `False`):
  Enable compression to progressive JPEG.
- `<base_topic>/compressed/jpeg_optimize` (`bool`, default: `False`):
  Enable JPEG compress optimization.
- `<base_topic>/compressed/jpeg_restart_interval` (`int`, default: `0`):
  JPEG restart interval in the range of \[0, 65535\].
- `<base_topic>/compressed/png_level` (`int`, default: `9`): PNG
  compression level, in the range \[1, 9\]. Higher values trade
  computation time for space savings.

}}}}

}}}

### Subscriber plugin

#### Subscribed Topics

- `<base_topic>/compressed`
  ([sensor_msgs/msg/CompressedImage](https://docs.ros.org/en/rolling/p/sensor_msgs/msg/CompressedImage.html)):
  Compressed transport subtopic.

## Publishing compressed images directly

Some cameras (particularly webcams) output their image data already in
JPEG format. When writing a driver for such a camera, a quick and dirty
approach is to simply copy the JPEG data into a
[sensor_msgs/msg/CompressedImage](https://docs.ros.org/en/rolling/p/sensor_msgs/msg/CompressedImage.html)
message and publish it on a topic of the form `image_raw/compressed`.
Then any ROS node using
[image_transport](https://index.ros.org/p/image_transport) can subscribe
to `image_raw` with transport `compressed`, just as if
`image_transport` were used on the publisher side. Of course, the
other transport topics (including `image_raw` itself) will not be
available.

## Tutorials

See [Tutorials](https://index.ros.org/p/image_transport) for general
instruction on using `image_transport`. `compressed_image_transport`
is specifically featured in the `image_transport` tutorial
[Examining the Simple Image Publisher and Subscriber](https://index.ros.org/p/image_transport).
