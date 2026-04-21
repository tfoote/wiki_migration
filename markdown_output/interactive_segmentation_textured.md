This package implements a novel object segmentation algorithm for
autonomous service robots acting in human living environments. The
proposed system allows a robot to effectively segment textured objects
in cluttered scenes by leveraging its manipulation capabilities. In this
interactive perception approach, 2D-features are tracked while the robot
actively induces motions into a scene using its arm. Thereby, the robot
autonomously infers appropriate arm movements which can effectively
separate objects. The resulting tracked feature trajectories are
assigned to their corresponding object by using a novel randomized
clustering algorithm, which samples rigid motion hypotheses for the a
priori unknown number of scene objects. We evaluated the approach on
challenging scenes which included occluded and reflective objects, as
well as objects of varying shapes and sizes.

See also below video and the associated tutorials.

![](attachment:web.png)

## Installation Instruction



```
svn co http://sourceforge.net/p/bosch-ros-pkg/code/1591/tree/trunk/stacks/bosch_interactive_segmentation
```



## Video

[Youtube](https://www.youtube.com/watch?v=4VVov6E3iiM)

## Usage

Please see the tutorials on the right side in order to learn how to use
the package.
