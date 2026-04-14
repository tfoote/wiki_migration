## Usage

These ROS nodes are designed to detect and track faces in images coming
from a ROS image topic. The nodes display or publish an image with the
resulting detections drawn on top of the image. The coordinates of the
detections can also be published to a separate topic. The settings of
the detection system can be easily adapted using ROS rqt_reconfigure
(rosrun rqt_reconfigure rqt_reconfigure). The nodes also publish the
coordinates of the faces for the use with other nodes. To work for a
wide variaty of scenarios, the following features are included:

-   OpenCV Face Detection
-   Dlib Face Detection
-   OpenCV CUDA support
-   OpenCV tracking (Optical flow)
-   OpenCV 2.4 & 3.0 supporte

An example of some of the nodes can be found
[here](http://www.phil.lu/?page_id=328). The code is available on
[GitHub](https://github.com/phil333/face_detection).

## Nodes

### face_detection

Node uses OpenCV (HAAR Cascade detector) to detect faces only.

```
roslaunch face_detection face_detection.launch
```

### face_tracking

Node uses OpenCV (HAAR Cascade detector) to detect faces. Detected faces
are tracked using Opencv (Optical flow LK). Both the detected and the
tracked faces are then merged into one list.

### face_detection_cuda

Node uses OpenCV (HAAR Cascade detector) and CUDA to detect faces only.

```
roslaunch face_detection face_detection_cuda.launch
```

### face_detection_dlib

Node uses Dlib (HOG Cascade detector) to detect faces only.

```
roslaunch face_detection face_detection_dlib.launch
```

### face_listener

Example node reading the published face coordinates

```
rosrun face_detection face_listener
```

### Changing Node settings

All setting can be adjusted dynamicaly using the ROS rqt reconfigure
setup.

```
rosrun rqt_reconfigure rqt_reconfigure
``` Once you have the rqt_reconfigure open, change
the input image default (/camera/image_raw) to your desired input.
Additional information about the different settings are annotated in the
dynamic reconfigure setup (hover over the desired setting in the
rqt_reconfigure for additional information)

## Additional Setup Information

### Multi-threading:

In order to get the best performance out of the detection, you should
compile your OpenCV package with Multi-threading support. OpenCV makes
use of TBB (WITH_TBB=ON) to to enable Multi-threading, for both versions
2.4 and 3.0. Here is a tutorial on how to install OpenCV with
Multi-threading for version 3.0
(<http://rodrigoberriel.com/2014/10/installing-opencv-3-0-0-on-ubuntu-14-04/>).

WARNING: Reinstalling OpenCV might break some of you other ROS packages,
so you might want to stick to your current version. This node will also
run without Multi-threading support, but especially the Face_Tracking
node will run considerably slower.

### OpenCV CUDA:

To enable faster detection, CUDA support has been enabled for the
detection process. Keep in mind that the CUDA detection is slightly
different to the original OpenCV detection and will deliver different,
slightly less accurate results. Currently only the detection process has
been implemented for CUDA. The tracking part is still under development.

### Dlib

The Dlib face detection system has a higher accuracy to detect faces
which are closer to the camera, especially faces which are tilted
sideways. The system is a bit slower than OpenCV, mainly because of the
lack of additional configuration settings (min max searchwindow_scale
\...). It also has a lower accuracy with smaller faces. The detection is
using a HOG cascade.

Since it is uncommon to have Dlib installed, the face_detection_dlib
node is disabled by default. If you want to use this node, you need to
enable it in the CMakeLists file under the section \"DLIB\". You will
also need to link the installation directory in the CMakeLists
(include(../dlib/cmake)). The Dlib library can be found on their website
(<http://dlib.net/>). If your CPU does not support the AVX instruction
set, you might have to change the line \"#set(USE_AVX_INSTRUCTIONS 1)\"
