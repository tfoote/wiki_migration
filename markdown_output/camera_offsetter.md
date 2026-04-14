## Stability

This is still an experimental application that has not been reviewed
yet. Its interface quite possibly will be changing.

## Overview

The package creates a virtual camera, allows the user to move it and
republishes raw sensor (stereo) data in the virtual camera. You can use
it to fix calibration problems locally by eliminating obvious
disparities between the 3D laser or robot data and stereo/image data.

![](attachment:offsetter_high_level.png)

The package contains 3 main nodes:

-   \`mono_offsetter\` - Creates a virtual monocular camera and
    republishes \`camera_info\` and various image topics
-   \`stereo_offsetter\` - Creates a virtual stereo camera and
    republishes \`camera_info\` and image_raw topics
-   \`keyboard_interface\` - Sends simple twist and baseline offsets
    using the keyboard.

### Limitations

The calibration is done manually and is only as good as you hand tune
it. Also keep in mind that a perfect calibration in one part of the
workspace will not necessarily result in a perfect calibration in
another part of the workspace.

It is possible that the calibration problem is caused by something else,
so keep your eyes open.

## Creating a Virtual Camera (Node API)

```clearsilver
node.0{
  name= mono_offsetter
  desc= Offset a monocular camera, such as the PR2's Hi-Res Prosilica cam or its forearm cameras
  sub {
    0.name=virtual_pose
    0.type=geometry_msgs/Pose
    0.desc=Set the offset to be the incoming pose
    1.name=virtual_twist
    1.type=geometry_msgs/Twist
    1.desc=Change the offset by the specified twist
    2.name=[camera]/camera_info
    2.type=sensor_msgs/CameraInfo
    2.desc=Used to offset camera info. Always enabled
    3.name=[camera]/image_raw,image_rect,image_rect_color
    3.type=sensor_msgs/Image
    3.desc=Used to offset images. Respectively enabled by the `~use_raw`, `~use_rect`, and `~use_rect_color` parameters.
  }
  pub {
    0.name=[camera]_offset/camera_info
    0.type=sensor_msgs/CameraInfo
    0.desc=Used to offset camera info. Always enabled
    1.name=[camera]_offset/image_raw,image_rect,image_rect_color
    1.type=sensor_msgs/Image
    1.desc=Used to publish offset images. Respectively enabled by the `~use_raw`, `~use_rect`, and `~use_rect_color` parameters.
  }
  param {
    0.name= ~config_file
    0.type=string
    0.desc=Filename to for reading/writing the most recent offset
    0.default= False
    1.name= ~use_raw
    1.type= bool
    1.desc= If ''True'', then offsetter republishes `image_raw`
    1.default= False
    2.name= ~use_rect
    2.type= bool
    2.desc= If ''True'', then offsetter republishes `image_rect`
    2.default= False
    3.name= ~use_rect_color
    3.type= bool
    3.desc= If ''True'', then offsetter republishes `image_rect_color`
    3.default= False
  }
}
```

#### Example

Suppose that you want to offset a camera in the \`/prosilica\`
namespace. You could use the following launch file:
```
<launch>
  <node type="mono_offsetter" pkg="camera_offsetter" name="prosilica_offsetter">
    <remap from="camera" to="/prosilica" />
    <param name="config_file" type="string" value="[HOME_DIR]/prosilica.offset" />
    <param name="use_rect_color" type="bool" value="True" />
  </node>
</launch>
```

This launches a camera_offsetter that subscribes to
\`/prosilica/image_rect_color\` and \`/prosilica/camera_info\`. It
copies the data from these messages, appends \`\_offset\` to the
frame_ids, and republishes on \`prosilica_offset/image_rect_color\` and
\`/prosilica/camera_info\`.

```clearsilver
node.0{
  name= stereo_offsetter
  desc= Offset a stereo camera
  sub {
    0.name=virtual_pose
    0.type=geometry_msgs/Pose
    0.desc=Set the offset to be the incoming pose
    1.name=virtual_twist
    1.type=geometry_msgs/Twist
    1.desc=Change the offset by the specified twist
    2.name=baseline_factor
    2.type=std_msgs/Float64
    2.desc=Change the stereocamera baseline by the specified factor
    3.name=[stereo]/left/camera_info, [stereo]/right/camera_info
    3.type=sensor_msgs/CameraInfo
    3.desc=Used to offset left & right camera info
    4.name=[stereo]/left/image_raw, [stereo]/right/image_raw
    4.type=sensor_msgs/Image
    4.desc=Used to offset left & right raw images
  }
  pub {
    0.name=[stereo]_offset/left/camera_info, [stereo]_offset/right/camera_info
    0.type=sensor_msgs/CameraInfo
    0.desc=Used to offset left & right camera info
    1.name=[stereo]_offset/left/image_raw, [stereo]_offset/right/image_raw
    1.type=sensor_msgs/Image
    1.desc=Used to publish offset left & right images
  }
  param {
    0.name= ~config_file
    0.type=string
    0.desc=Filename to for reading/writing the most recent offset
    0.default= False
  }
}
```

Suppose that you want to offset a stereocamera in the \`/narrow_stereo\`
namespace. You could use the following launch file:
```
<launch>
  <node type="stereo_offsetter" pkg="camera_offsetter" name="stereo_offsetter">
    <remap from="stereo" to="/narrow_stereo" />
    <param name="config_file" type="string" value="[HOME_DIR]/narrow.offset" />
  </node>

  <group ns="narrow_stereo_offset">
    <node type="stereo_image_proc" name="proc" pkg="stereo_image_proc"/>
  </group>
</launch>
``` This will create a virtual stereocamera in the
\`/narrow_stereo_offset\` namespace. This file also launches the
\`stereo_image_proc\` node on the offset camera.

## Use the keyboard to move a virtual camera (Node API)

```clearsilver
node.2{
  name=keyboard_interface
  desc= Sends incremental pose offsets as twists. Can also send baseline updates for virtual stereocameras
  pub {
    0.name=virtual_pose
    0.type=geometry_msgs/Pose
    0.desc=Set the offset to be the incoming pose
    1.name=virtual_twist
    1.type=geometry_msgs/Twist
    1.desc=Change the offset by the specified twist
    2.name=baseline_factor
    2.type=std_msgs/Float64
    2.desc=Change the stereocamera baseline by the specified factor
  }
}
```

#### Command Line Usage

-   In translation mode, keys x/X, y/Y, z/Z move the virtual camera in
    fixed increments (e.g. x=-0.001, X=+0.001).
-   In rotation mode, keys x/X, y/Y, z/Z rotate the virtual camera
    around respective axis
-   In baseline mode, keys b/B increase or decrease the stereocamera
    baseline

#### Example

To start the keyboard interface, all you need to do is start the node in
the same namespace as the offsetter. If the offsetter is in the global
namespace, then a simple \`rosrun\` is sufficient:
```
rosrun camera_offsetter keyboard_interface
```
