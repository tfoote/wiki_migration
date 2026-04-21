## Introduction

This node implements generation of stereoscopic 3D image from a stereo
camera. This is done by superimposing red filtered left and cyan
filtered right image. When viewed with appropriate glasses, illusion
depth is created. More about anaglyph images on
WikiPedia:Anaglyph_image.

Implementation is based on an older version of `stereo_view` node in
[image_view](image_view).

## Video

This video was taken in Fever dance studio (<http://www.fever.hr>),
using a Videre STOC 9cm baseline stereo camera.

[Youtube](https://www.youtube.com/watch?v=95sBvSfKtZw)

## ROS API

```clearsilver
name = anaglyph
desc = Generates red/cyan anaglyph image
sub {
  0.name = <stereo>/left/<image>
  0.type = sensor_msgs/Image
  0.desc = Stereo camera left image. Namespaces (parameters) `stereo` and `image` should be remapped appropriately.
  1.name = <stereo>/right/<image>
  1.type = sensor_msgs/Image
  1.desc = Stereo camera right image. Namespaces (parameters) `stereo` and `image` should be remapped appropriately.
}
pub {
  0.name = <stereo>/anaglyph3D
  0.type = sensor_msgs/Image
  0.desc = Red/cyan anaglyph image.
}
```
