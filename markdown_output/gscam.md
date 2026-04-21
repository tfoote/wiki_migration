## Overview

\`gscam\` is meant as a simple approach to using a webcam in ROS that
maximizes compatibility. \`gscam\` leverages
[Gstreamer](http://www.gstreamer.net/), a multimedia framework similar
to !DirectShow. Specifically: Gstreamer can be used to build up
multimedia \"pipelines\" consisting of sources, sinks, and filters. For
example: a v4l webcam *source* might be *filtered* by an upscaler before
being sent to the screen (a *sink*). Alternately, a mp4 file might act
as a source and be filtered into an avi file as a sink. There are many
possibilities. For an overview see:
[Using Gstreamer](http://gstreamer.freedesktop.org/data/doc/gstreamer/head/faq/html/chapter-using.html).

\`gscam\` can attach itself to a specially formatted pipeline. Provided
this pipeline is processing RGB video, \`gscam\` will rebroadcast the
video over as *both* a standard ROS image transport *and* a ROS Camera.
Since Gstreamer is compatibile with almost every video capture standard
under Linux (and many on OSX), \`gscam\` makes ROS defacto compatible
with almost every Linux webcam or video system available. Moreover,
because there are a number of Gstreamer filters for processing video
(e.g. white-balancing, cropping, etc.) gscam allows for a more advanced
video processing even with cheaper webcams.

Gstreamer is an extremely rich framework, but basic usage is fairly
simple. Please see the \"Basic Usage\" section to get started. You may
also find the Gstreamer documentation on their website to be helpful.

## Running

\`gscam\` expects an environmental variable, \`GSCAM_CONFIG\`, to
contain a gstreamer pipeline definition for it to launch. There is one
important restriction:

-   At the end of the pipeline where \`gscam\` will attach itself, the
    pipeline *must* be carrying RGB formatted video.

Here\'s an example launch that should work on almost any machine where
Gstreamer is installed and a camera of some kind is available attached
to \`/dev/video2\`. Note that \`gscam\` expects to start *within* the
bin directory:

```
roscd gscam
cd bin
export GSCAM_CONFIG="v4l2src device=/dev/video2 ! video/x-raw-rgb,framerate=30/1 ! ffmpegcolorspace"
rosrun gscam gscam
```

If you see a message about a \"failure to PAUSE\" or something similar,
the most likely cause is a permission issue with the available video
devices.

If you see a \"Processing\...\" message, it means \`gscam\` is happily
publishing.

You can graphically explore many of the available video devices with the
gstreamer-properties utility. \`gst-inspect-0.10\` (or .09 or whatever
is your Gstreamer version number) will list all of the available
plugins. For more help on specifying the \`GSCAM_CONFIG\`, see
[this cheatsheet](http://wiki.oz9aec.net/index.php/Gstreamer_cheat_sheet).

## Advanced Usage

\`gscam\` is fully compatible with the ROS Camera interface and can be
calibrated to provided rectified images. For details, see the
appropriate ROS documentation on the [image_pipeline](image_pipeline)
wiki page.

An example launch file which includes loading calibration data is

```
<launch>
  <!-- Set this to your camera's name -->
  <arg name="cam_name" value="creative_cam" />

  <!-- Start the GSCAM node -->
  <env name="GSCAM_CONFIG" value="v4l2src device=/dev/video0 ! video/x-raw-yuv,framerate=30/1,width=640,height=480 ! ffmpegcolorspace " />
  <node pkg="gscam" type="gscam" name="$(arg cam_name)">
    <param name="camera_name" value="$(arg cam_name)" />
    <param name="camera_info_url" value="package://localcam/calibrations/${NAME}.yaml" />
    <remap from="camera/image_raw" to="$(arg cam_name)/image_raw" />
  </node>

  <!-- Provide rectification -->
  <node pkg="image_proc" type="image_proc" name="creative_image_proc"
        ns="$(arg cam_name)" />

  <!-- View the raw and rectified output -->
  <node pkg="image_view" type="image_view" name="creative_view" >
    <remap from="image" to="/$(arg cam_name)/image_raw" />
  </node>
    
  <node pkg="image_view" type="image_view" name="creative_view_rect" >
    <remap from="image" to="/$(arg cam_name)/image_rect_color" />
  </node>
</launch>
```

Note it assumes calibration data is stored in a subdirectory of the ROS
package \'localcam\'.

## ROS API

```clearsilver
name=gscam
node {
  no_header=True
  0.name=gscam_publisher 
  0.desc=Sets up a ROS camera interface for a gstreamer-based camera.
}
pub {
  0.name = image_raw
  0.type = sensor_msgs/Image
  0.desc = The unprocessed image data.
  1.name = camera_info
  1.type = sensor_msgs/CameraInfo
  1.desc = Contains the camera calibration (if calibrated) and extra data about the camera configuration.
}
srv {
  0.name= set_camera_info
  0.type= sensor_msgs/SetCameraInfo
  0.desc= Set the appropriate camera info (TF frame, calibration parameters, ROI etc.)
}
```

## Troubleshooting

### Bad Camera Info

```
MessageFilter [target=/map ]: Discarding message from [/gscam_publisher] due to empty frame_id.  This message will only print once.
``` You need to set the TF frame via the
\`set_camera_info\` service described above.
