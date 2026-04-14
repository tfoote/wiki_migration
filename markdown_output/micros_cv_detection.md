## Overview

The package aims to detect the UAV during UAV automonous take-off and
landing. In another word, it is to locate the the center of the UAV in
each frame. An initial closed curve is set according to previous
detection results, and then Chan-Vese model-based segmentation algorithm
is employed to detect object region. Finally, with the segmented object
region, the UAV center is located.

## Quick Start

### Parameters

Setup initial parameters in launch/CV_detection.launch
```
<param name="initial_x" type="int" value="320" />
<param name="initial_y" type="int" value="270" />
<param name="initial_r" type="int" value="20" />
``` The coordinate (initial_x, initial_y) is the
center of the initial curve (circle) and the initial_r is the radius

### Usage

#### Installation

```
cd ~/catkin_ws/src
git clone https://github.com/micros-uav/micros_cv_detection
cd ..
catkin_make
```

#### Running

Open a new consol and run a video node

\'\'\'Note:\'\'\'run this video node under /catkin_ws directory Run
detection node also in /catkin_ws directory ```
source devel/setup.bash
roslaunch cv_detection cv_detection.launch
```

#### Result demo

![](https://cloud.githubusercontent.com/assets/11674154/9218708/384ea87e-4107-11e5-9685-ef04869a1113.png)

-   The image is a single frame of the UAV autonomous landing video

```{=html}
<!-- -->
```
-   The red circle represents initial curve

```{=html}
<!-- -->
```
-   The green point is the UAV detection result

\'\'\'Note:\'\'\'the package is inspired by and adapted from
[\[1](http://ieeexplore.ieee.org/document/7288942/)\]. The details about
the Chan-Vese model can be found in
[\[2](https://webdocs.cs.ualberta.ca/~nray1/CMPUT615/LevelSet/ChanVese2001.pdf/)\].

## Reference

\[1\] D. Tang, T. Hu, L. Shen, D. Zhang and D. Zhou. Chan-Vese model
based binocular visual object extraction for UAV autonomous take-off and
landing. International Conference on Information Science and Technology,
2015, 67-73.

\[2\] T. F. Chan and L. A. Vese. Active contours without edges. IEEE
Transactions on Image Processing, 2001, 10: 266-277.
