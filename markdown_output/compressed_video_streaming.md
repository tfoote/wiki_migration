# DEPRECATED

## Warnings

-   The recommended way to stream theora video is now:
    <http://www.ros.org/wiki/theora_image_transport>. The only case
    where this package remains preferable is if you already have a node
    publishing images which you cannot modify.

## Usage

This mini-usage tutorial is assuming you are trying to stream camera
data off the wide stereo camera on a robot to a local machine.

On the robot:

```
roscd compressed_video_streaming
rosmake compressed_video_streaming
rosrun compressed_video_streaming image_compression_node image:=/wide_stereo/right/image_rect_color
``` (note, in the third command above replace
\"/wide_stereo/right/image_rect_color\" with whatever the name of the
topic your images are being published on is.

Off the robot:

```
roscd compressed_video_streaming
rosmake compressed_video_streaming
rosrun compressed_video_streaming image_decompression_node
``` A sample bag is also available
[HERE](attachment:theora_stream.bag). Rosrecord appears to have dropped
some packets, so there is a little bit of corruption, but it\'s not too
bad. Thanks go to Priyanka for modeling in the video. To use it just do
the \"Off the robot\" portion of the setup and then rosplay the bag
(make sure you run the decompression node before starting bag playback,
it will not work otherwise).

## Under the Hood

The compression and decompression node talk to each other over the
\"image_stream\" topic. To use multiple instances of these nodes in the
system image_stream must be remapped to some new topic for each
compression/decompression node pair.

The decompression node always creates an openCV window (this may be
problematic in some setups where viewing the decompressed imagery isn\'t
the desired final step, and at some point a parameter will be added to
disable this window). The decompression node also publishes the
decompressed images to a new topic: \"streamed_video\".

Right now the node is using a fixed bitrate of 800k bits per second.
This has been exposed as a parameter in
<http://www.ros.org/wiki/theora_image_transport>.
