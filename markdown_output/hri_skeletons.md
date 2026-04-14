![\|height=\"400px\"](attachment:rviz_human.jpg)

## Overview

`hri_skeletons` detects and tracks human bodies in both 2D (2D keypoints
of the body, in the image space) and 3D (generating on the fly URDF
models for each detected humans, alongside their
\<\<MsgLink(sensor_msgs/JointState)\>\> and [TF](tf) trees).

The detection relies on the open-source
[Intel OpenVINO toolkit](https://docs.openvinotoolkit.org/), requires
only a RGB stream, and runs at 15FPS on an Intel 10th gen CPU.

## Installation

-   Follow first the general
    [ ROS4HRI installation instructions](https://git.brl.ac.uk/ROS4HRI/main/blob/master/README.md ).

```{=html}
<!-- -->
```
-   Install the
    [ {{hri_msgs}}} package](https://git.brl.ac.uk/ROS4HRI/hri_msgs/blob/master/README.md )

```{=html}
<!-- -->
```
-   then:

```
$ cd ~/src
$ git clone https://git.brl.ac.uk/ROS4HRI/hri_skeletons.git
$ cd hri_skeletons
$ mkdir build && cd build
$ cmake -DCMAKE_BUILD_TYPE=Release -DCMAKE_INSTALL_PREFIX=~/dev .. && make && make install
```

You can test this node by running:

```
$ rosrun usb_cam usb_cam
$ rosrun hri_skeletons run image:=/usb_cam/image_raw _debug:=true _model:=$HOME/openvino_models/public/human-pose-estimation-3d-0001/FP16/human-pose-estimation-3d-0001.xml
```

which should display something like that (debug mode = true):

![\|width=\"500px\"](attachment:debug_screnshot.jpg)

## ROS API

### Subscribed topics

\`image\` (\<\<MsgLink(sensor_msgs/Image)\>\>)

. input RGB stream

### Published topics

For each detected body, an unique id is created, and a corresponding
topic namespace \`humans/bodies/\<id\>\` is created. Within that
namespace, the following topics are published:

\`humans/bodies/\<id\>/joint_states\`
(\<\<MsgLink(sensor_msgs/JointState)\>\>)

. the human body joint state

\`humans/bodies/\<id\>/skeleton2d\`
(\<\<MsgLink(hri_msgs/Skeleton2D)\>\>)

. the 2D coordinates of the skeleton\'s bones, with respect to the
source image.

### Parameters

\`model\` (\`string\`)

. The full path to the OpenVINO model for human 3D pose estimation

\`debug\` (\`bool\`)

. If true, will open 2 debug windows, one with the 2D skeleton overlaid
onto the input image, one with a 3D view of the skeletons.
