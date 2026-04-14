This paper describes an object segmentation approach for autonomous
(humanoid) service robots acting in human living environments. The
proposed system allows a robot to effectively segment textureless
objects in cluttered scenes by leveraging its manipulation capabilities.
In this approach, the cluttered scenes are first statically segmented
using part-graphbased hashing and then the interactive perception is
deployed in order to resolve possibly ambiguous static segmentation. In
the second step the RGBD (RGB + Depth) features, estimated on the RGBD
point cloud from the Kinect sensor, are extracted and tracked while
motion is induced into a scene. The resulting tracked feature
trajectories are then assigned to their corresponding object by using a
graph-based clustering algorithm, in which the graph edges can be used
to measure the distance dissimilarity between the tracked RGBD features.
In the final step, dense model reconstruction based on region growing
algorithm is applied. We evaluated the approach on a set of scenes which
consist of various textureless flat (e.g. box-like) and round (e.g.
cylinder-like) objects and the combination thereof.

![](attachment:textureless.png)

## Installation Instruction

```
svn co http://svn.code.sf.net/p/bosch-ros-pkg/code/trunk/stacks/bosch_interactive_segmentation/interactive_segmentation_textureless
```

## Video

[Youtube](https://www.youtube.com/watch?v=Bu4LayrGC1s)

## Usage

Tutorials are still work in progress.
