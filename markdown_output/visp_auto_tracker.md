## Overview

This package wraps an automated pattern barcode based tracker using
[ViSP](https://visp.inria.fr) library. The tracker estimates the pattern
position and orientation with respect to the camera. It requires the
pattern 3d model and a configuration file.

The algorithm allows first to detect automatically the barcode using one
of the following detectors:

-   QR-code detection
-   flashcode detection

Then from the location of the 4 barcode corners it computes an initial
pose using a PnP algorithm. This pose allows to initialize the model
based tracker that is dedicated to track the two squares defining the
black area arround the barcode. For the tracking we use an hybrid
approach that considers moving-edges and keypoint features that are
mainly located on the barcode. Finally, the tracker is also able to
detect loss of tracking and recover from it entering in a new barcode
detection and localization stage.

The package is composed of one node called `visp_auto_tracker`. This
node tries to track the object as fast as possible. The viewer coming
with [visp_tracker](visp_tracker) package can be used to monitor the
tracking result.

The next video shows how to track a specific pattern textured with a
QRcode. ViSP model-based tracker detects when it fails and recover the
object position thanks to QRcode detection.

[Youtube](https://www.youtube.com/watch?v=_dFF0_vWRcA)

## Reference

-   [A.I. Comport, E. Marchand, M. Pressigout, F. Chaumette. Real-time markerless tracking for augmented reality: the virtual visual servoing framework. IEEE Trans. on Visualization and Computer Graphics, 12(4):615-628, July 2006](http://www.irisa.fr/lagadic/publi/publi/Comport06b-eng.html)
-   [E. Marchand, H. Uchiyama, F. Spindler. Pose estimation for augmented reality: a hands-on survey. IEEE Trans. on Visualization and Computer Graphics, 2016](http://www.irisa.fr/lagadic/publi/publi/Marchand16a-eng.html)

## Calibration Requirements

Currently the [visp_auto_tracker](visp_auto_tracker) package requires
calibration information from a camera_info topic. To this end
[visp_camera_calibration](visp_camera_calibration) package can be used.

## Features

The package purpose is to provide the 3D pose of an object in a sequence
of images. The object has to be textured with a pattern on one face. The
pattern has to be included into a white box, itself included in a black
box.

This is an example of a valid QR-code pattern that can be downloaded
[here](https://github.com/lagadic/vision_visp/releases/download/vision_visp-0.5.0/template-qr-code.pdf).

![](attachment:template-qr-code-small.png)

This is an example of a valid flash-code pattern that can be downloaded
[here](https://github.com/lagadic/vision_visp/releases/download/vision_visp-0.5.0/template-flash-code.pdf).

![](attachment:template-flash-code-small.png)

## Installation

[visp_auto_tracker](visp_auto_tracker) is part of
[vision_visp](vision_visp) stack.

-   To install [visp_auto_tracker](visp_auto_tracker) package run
    ```
sudo apt-get install ros-$ROS_DISTRO-visp-auto-tracker
```

```{=html}
<!-- -->
```
-   Or to install the complete stack run ```
sudo apt-get install ros-$ROS_DISTRO-vision-visp
```

## Examples

You can run [visp_auto_tracker](visp_auto_tracker) on a pre-recorded bag
file that comes with the package, or on a live video from a camera.

### Pre-recorded example

To run [visp_auto_tracker](visp_auto_tracker) on a pre-recorded image
sequence, just run:

```
roslaunch launch/tutorial.launch
``` The pattern used in this example can be
downloaded
[here](http://cloud.github.com/downloads/lagadic/visp_auto_tracker/QRPattern.png).

### Live video examples

You have a ready-to-use roslaunch file in
`launch/tracklive_firewire.launch`. This works with a firewire (1394)
camera. If you have an usb camera (like a webcam) you can use
`launch/tracklive_usb.launch` launch file.

You can launch with the following command line:

```
roslaunch launch/tracklive_firewire.launch
```

## Config file

[visp_auto_tracker](visp_auto_tracker) centralises most of its
parameters inside a configuration file following the
[boost::program_options](http://www.boost.org/doc/libs/1_52_0/doc/html/program_options.html)
default format.

The basic configuration file would look like this:

```
#set the detector type: "zbar" to detect QR code, "dmtx" to detect flashcode
detector-type= zbar
#enable recovery mode when the tracker fails
ad-hoc-recovery= 1

#point 1
flashcode-coordinates= -0.024
flashcode-coordinates= -0.024
flashcode-coordinates= 0.000
#point 2
flashcode-coordinates= 0.024
flashcode-coordinates= -0.024
flashcode-coordinates= 0.000
#point 3
flashcode-coordinates= 0.024
flashcode-coordinates= 0.024
flashcode-coordinates= 0.000
#point 4
flashcode-coordinates= -0.024
flashcode-coordinates= 0.024
flashcode-coordinates= 0.000

#point 1
inner-coordinates= -0.038
inner-coordinates= -0.038
inner-coordinates= 0.000
#point 2
inner-coordinates= 0.038
inner-coordinates= -0.038
inner-coordinates= 0.000
#point 3
inner-coordinates= 0.038
inner-coordinates= 0.038
inner-coordinates= 0.000
#point 4
inner-coordinates= -0.038
inner-coordinates= 0.038
inner-coordinates= 0.000

#point 1
outer-coordinates= -0.0765
outer-coordinates= -0.0765
outer-coordinates= 0.000
#point 2
outer-coordinates= 0.0765
outer-coordinates= -0.0765
outer-coordinates= 0.000
#point 3
outer-coordinates= 0.0765
outer-coordinates= 0.0765
outer-coordinates= 0.000
#point 4
outer-coordinates= -0.0765
outer-coordinates= 0.0765
outer-coordinates= 0.000
```

### Common parameters

#### detector-type

The following detectors are supported

-   `detector-type= zbar`: uses libzbar to detect QRcodes
-   `detector-type= dmtx`: uses libdmtx to detect flashcodes

#### flashcode-coordinates

3D-coordinates in meters of the box delimiting the pattern (QRcode or
flashcode).

#### inner-coordinates

3D-coordinates in meters of the white box containing the pattern.

#### outer-coordinates

3D-coordinates in meters of the black box containing the pattern.

#### ad-hoc-recovery

When set (`tracker-type= 1`) this parameter activates the tracking
lost detection and recovery using `flashcode-coordinates`,
`inner-coordinates` and `outer-coordinates` point coordinates.

## Tracker states

The tracker is a state machine whose states vary during the tracking
process. The process includes tracking, loss and recovery. These are the
states used:

-   Waiting For Input (id: 0) : Not detecting any pattern, just
    recieving images

```{=html}
<!-- -->
```
-   Detect Flashcode (id: 1) : Pattern detected.

```{=html}
<!-- -->
```
-   Detect Model (id: 2) : Model successfully initialized (from wrl &
    xml files).

```{=html}
<!-- -->
```
-   Track Model (id: 3) : Tracking model.

```{=html}
<!-- -->
```
-   Re Detect Flashcode (id: 4) : Detecting pattern in a small region
    around where the pattern was last seen.

```{=html}
<!-- -->
```
-   Detect Flash code (id: 5) : Detecting pattern in a the whole frame.

## Viewer

When you track a model, you probably want a visual feedback. You can get
one by connecting rviz to the outputed `/object_position` topic.
[visp_auto_tracker](visp_auto_tracker) does not have a dedicated viewer.
It can use the viewer provided with [visp_tracker](visp_tracker)
package, specifically `visp_tracker/visp_tracker_viewer` node.

Without connecting another node, you can also open a debug graphical
output directly from the `visp_auto_tracker` node by setting the
`debug_display` parameter.

The following figure shows the debug output (left) next to the external
[visp_tracker](visp_tracker)/viewer (right) in the case of the hybrid
model-based tracker with QR-code initialisation:

![](attachment:tracker_viewer-small.png)

## Nodes

```clearsilver
name = visp_auto_tracker
desc = Subscribes to a camera and publishes pose.
sub {
  0.name = image_raw
  0.type = sensor_msgs/Image
  0.desc = The image topic. Should be remapped to the name of the real image topic.

  1.name = camera_info
  1.type = sensor_msgs/CameraInfo
  1.desc = The camera parameters.
}

param {
  0.name = model_path
  0.type = string
  0.desc = path to where the models are stored.

  1.name= model_name
  1.type = string
  1.desc = model name. Name of the cfg, wrl and xml files. If model_path is /path/ and model_name is model then /path/model.wrl, /path/model.xml and /path/model.cfg will be loaded. The content of the cfg file is described in "Config file" section.

  2.name= debug_display
  2.type = boolean
  2.desc = display debug information about tracking
}


pub {
  0.name = object_position
  0.type = geometry_msgs/PoseStamped
  0.desc = 3D pose of the model.

  1.name = object_position_covariance
  1.type = geometry_msgs/PoseWithCovarianceStamped
  1.desc = 3D pose of the model. The covariance part is unused

  2.name = status
  2.type = std_msgs/Int8
  2.desc = Status of the automatic tracker. See tracker states for more information.

  3.name = moving_edge_sites
  3.type = visp_tracker/MovingEdgeSites
  3.desc = Moving edge sites information (stamped). For debugging/monitoring purpose.

  4.name = klt_points_positions
  4.type = visp_tracker/KltPoints
  4.desc = Position and id of the keypoints (stamped). For debugging/monitoring purpose.

}
```

## Report a bug

Use !GitHub to
[report a bug or submit an enhancement](https://github.com/lagadic/vision_visp/issues).
