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



```clearsilver
node.0 {
  name = Publisher plugin
  desc =
  pub {
    0.name = <base topic>/theora
    0.type = theora_image_transport/Packet
    0.desc = Theora transport subtopic
  }
  param {
    group.0 {
      name = Reconfigurable parameters
      desc = All publisher parameters are dynamically reconfigurable per-topic. See [[dynamic_reconfigure]] for details on dynamically reconfigurable parameters.
      0.name = <base topic>/theora/optimize_for
      0.type = int
      0.default = `Quality` (1)
      0.desc = Controls whether to use constant bitrate (CBR) encoding, aiming for `~theora/target_bitrate`; or variable bitrate (VBR) encoding, aiming for `~theora/quality`. Values are `Bitrate` (0) and `Quality` (1).
      1.name = <base topic>/theora/target_bitrate
      1.type = int
      1.default = 800000
      1.desc = Target bitrate. Used if `optimize_for` is set to `Bitrate`.
      2.name = <base topic>/theora/quality
      2.type = int
      2.default = 31
      2.desc = Encoding quality level, in the range [0, 63]. Used if `optimize_for` is set to `Quality`.
      3.name = <base topic>/theora/keyframe_frequency
      3.type = int
      3.default = 64
      3.desc = Maximum distance between key frames. If set to 1, every frame is a keyframe.
    }
  }
}
node.1 {
  name = Subscriber plugin
  desc =
  sub {
    0.name = <base topic>/theora
    0.type = theora_image_transport/Packet
    0.desc = Theora transport subtopic
  }
  param {
    group.0 {
      name = Reconfigurable parameters
      desc = All subscriber parameters are dynamically reconfigurable per-node.
      0.name = ~theora/post_processing_level
      0.type = int
      0.default = 0
      0.desc = Post-processing level. Higher values can improve the appearance of the decoded images at the cost of more CPU.
    }
  }
}
```



## Nodes



```clearsilver
name= ogg_saver 
desc= `ogg_saver` listens to the Theora transport packets associated with an image topic and saves them out to a .ogv file for later playback with tools like VLC or mplayer. Since Theora does not currently support variable frame rate videos the saved file will have a speed of one frame per second.
sub {
  group.0 {
    0.name = <image>/theora
    0.type = theora_image_transport/Packet
    0.desc = The topic containing the Theora packet stream. Note that you remap the base topic `image`, just as with other image consumers like [[image_view]].
  }
  group.1 {
    name = DEPRECATED
    0.name = stream
    0.type = theora_image_transport/Packet
    0.desc = The topic containing the Theora packet stream.
  }
}
```



#### Usage



```
$ rosrun theora_image_transport ogg_saver image:=<base_topic> [output_file.ogv]
```
