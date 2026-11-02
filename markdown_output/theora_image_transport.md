## Overview

`theora_image_transport` is a plugin package for
[image_transport](https://index.ros.org/p/image_transport). It enables
any node using `image_transport` classes to publish and subscribe to
image topics compressed over the wire using the Theora video codec.

`theora_image_transport` only works with 8-bit color or grayscale
images.

**`'Before reading this page, make sure you understand the [[https://index.ros.org/p/image_transport|image_transport]] package`**'

## Tutorials

See [Tutorials](https://index.ros.org/p/image_transport) for general
instruction on using `image_transport`.

## ROS API

### Publisher plugin

#### Published Topics

- `<base topic>/theora`
  ([theora_image_transport/msg/Packet](https://docs.ros.org/en/rolling/p/theora_image_transport/msg/Packet.html)):
  Theora transport subtopic

#### Parameters

##### Reconfigurable parameters

All publisher parameters are dynamically reconfigurable per-topic. See
[dynamic_reconfigure](https://index.ros.org/p/dynamic_reconfigure) for
details on dynamically reconfigurable parameters.

- `<base topic>/theora/optimize_for` (`int`, default: `Quality` (1)):
  Controls whether to use constant bitrate (CBR) encoding, aiming for
  `theora/target_bitrate`; or variable bitrate (VBR) encoding, aiming
  for `theora/quality`. Values are `Bitrate` (0) and `Quality`
  (1).
- `<base topic>/theora/target_bitrate` (`int`, default: `800000`):
  Target bitrate. Used if `optimize_for` is set to `Bitrate`.
- `<base topic>/theora/quality` (`int`, default: `31`): Encoding quality
  level, in the range \[0, 63\]. Used if `optimize_for` is set to
  `Quality`.
- `<base topic>/theora/keyframe_frequency` (`int`, default: `64`):
  Maximum distance between key frames. If set to 1, every frame is a
  keyframe.

### Subscriber plugin

#### Subscribed Topics

- `<base topic>/theora`
  ([theora_image_transport/msg/Packet](https://docs.ros.org/en/rolling/p/theora_image_transport/msg/Packet.html)):
  Theora transport subtopic

#### Parameters

##### Reconfigurable parameters

All subscriber parameters are dynamically reconfigurable per-node.

- `~theora/post_processing_level` (`int`, default: `0`): Post-processing
  level. Higher values can improve the appearance of the decoded images
  at the cost of more CPU.

## Nodes

### ogg_saver

`ogg_saver` listens to the Theora transport packets associated with an
image topic and saves them out to a .ogv file for later playback with
tools like VLC or mplayer. Since Theora does not currently support
variable frame rate videos the saved file will have a speed of one frame
per second.

#### Subscribed Topics

- `<image>/theora`
  ([theora_image_transport/msg/Packet](https://docs.ros.org/en/rolling/p/theora_image_transport/msg/Packet.html)):
  The topic containing the Theora packet stream. Note that you remap the
  base topic `image`, just as with other image consumers like
  [image_view](https://index.ros.org/p/image_view).

##### DEPRECATED

- `stream`
  ([theora_image_transport/msg/Packet](https://docs.ros.org/en/rolling/p/theora_image_transport/msg/Packet.html)):
  The topic containing the Theora packet stream.

#### Usage



```
$ rosrun theora_image_transport ogg_saver image:=<base_topic> [output_file.ogv]
```
