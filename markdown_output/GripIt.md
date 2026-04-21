## Description

Provided the depth map of an arbitrary scene, GripIt can extract the
geometric edges of objects in said scene and further calculate the
optimal approach vector for a 2-finger pinch-based robotic grippers.
This information is presented in an interactive 3D point cloud view.
Furthermore, GripIt provides editable parameters which governs
particular features of the 2D and 3D scene. As a high-level overview,
GripIt relies on machine vision algorithms to define the edges within a
depth map. These edges are then paired and a normal vector calculated
based on the underlying surface's depth map representation.

## Installation

GripIt has been uploaded to ROS Jenkins build system.

Running the following commands should download the package to your local
environment.

```
$ sudo apt install ros-kinetic-gripit
```

### Application Dependencies

Currently, GripIt relies on the following packages:

1\. OpenCV2 1. Matplotlib 2.1.0 1. Numpy 1.13.3 1. PyQt 1. PyQtGraph
0.10.0 1. Scipy 0.19.1 1. Scikit-image 0.13.0

## Launching GripIt

After Installation, GripIt could be launced using the following
commands:

```
$ rosrun gripit gripit
```

-   Ensure a Roscore instance already running and color and depth topic
    is being published by a separate package.

## Using Application

GripIt incorporates a set of parameters which may be used to alter the
edge detection and point-cloud representation of the scene.

**`Parameters`**

-   Auto-Canny Sigma:

Controls the sensitivity for edge detection algorithms that are used.
Lower value may exclude some edges, while a higher value may present
noise. The default value of 33% is a statistical recommendation.

-   Segmentation Tolerance:

Influences at what angle an edge may be divided.

-   Minimum Paring Length Ratio - Edge Pair Min Distance

Sets the minimum distance that an edge-pair has to be in order to be
processed

-   Edge Pair Max Distance:

Sets the maximum distance that an edge-pair has to be in order to be
processed

-   Edge Pair Angle:

The maximum angle between 2 edge pair vectors

### Processing a Scene

On loading a scene, GripIt will launch the Base view as show in
figure 1. Here the program parameters are edited, a region of interest
is established under the crop rectangle of the image, and the scene
processed by clicking the process button.

<https://user-images.githubusercontent.com/847804/47836771-dccfef80-dd7f-11e8-8450-94cba4f4ef22.png>

After a scene has been processed, a set of views will be added to the
base window as tabs. These views present the calculated edge-pairs and
approach vector as a 2D image and a 3D point-cloud. At any time the
parameters could be re-edited and the scene re-updated with leaving the
application.

Edge-Pair View:

<https://user-images.githubusercontent.com/847804/47836814-0ab53400-dd80-11e8-8d94-86517731bb55.png>

The first of these tabs, EdgePairs, displays the edge-pairs located in
the cropped scene. These edge pairs are color coded, and given numeric
names. The underlying points defining an edge could also be viewed by
selecting "Display Edge Points." By pressing the left or right keys, a
correspond 2d depth map image will be presented in the image view. To
view the approach vector of an edge-pair, an edge-pair must be selected
from the drop-down menu. Clicking "process face" generates an approach
vector for the selected edge-pair. This vector could be viewed by
switching to the Point-Cloud tab.

<https://user-images.githubusercontent.com/847804/47836838-215b8b00-dd80-11e8-8a90-a13437607edc.png>

In the point cloud tab, GripIt presents the scene in a 3D point cloud.
The edge select tool of the EdgePair tab is synchronized with the edges
that are shown in the PointCloud view. When an edge is processed the
calculated approach vector is represented by a 2-finger gripper. This
gripper dynamically resizes to grasp the selected edges. The scene
presented in the Point-Cloud View could be panned and rotated as needed.
