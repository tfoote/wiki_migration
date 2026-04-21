[Included page bowpmap_ros/menu not found](Included page bowpmap_ros/menu not found)

# Package Summary

BoWP-Map is a RGB image based topological mapping algorithm.

-   Author : Nishant Kejriwal

```{=html}
<!-- -->
```
-   Email id: kejriwalnishant1990@gmail.com

```{=html}
<!-- -->
```
-   License : BSD

```{=html}
<!-- -->
```
-   Bug/ feature tracker:
    <https://gitlab.com/nishant1990/bowpmap_ros/issues>

```{=html}
<!-- -->
```
-   Source: git <https://gitlab.com/nishant1990/bowpmap_ros.git>
    (branch: master)

## Overview

## Tutorials

## Demos

### Appearance-based loop closure detection-only

[Youtube](https://www.youtube.com/watch?v=eme6JX9pINU)

This video is a result of BoWP-Map on New College Dataset.

### Real Time implementation of BoWP-Map

[Youtube](https://www.youtube.com/watch?v=0qLjV-vrwZA)

## Nodes

### bowpmap_ros

It is a wrapper of the BoWP-Map Core library for topological mapping .
The graph of the map is incrementally built and the output is shown
using ros topics where loop closure information is published.


```clearsilver

sub {
  0.name = rgb/image
  0.type = sensor_msgs/Image
  0.desc = Kinect RGB Images or Any monocular camera image for topological mapping. This topic is mapped to RGB image topic of either kinect or any web camera(By default, it is set to kinect rgb image topic).
  1.name = odom
  1.type = nav_msgs/Odometry
  1.desc = Odometry data is used to visualise the map built using bowpMap algorithm. Visualisation is not a part of the algorithm. You can download the bowpMap code with visualisation from here : https://gitlab.com/nishant1990/bowpmap_ros.git (branch: prasun).
    }
 pub {
  0.name = loopClosure
  0.type = std_msgs/Bool
  0.desc = BoWP-Map based loop closure detection.
  1.name = loopClosureImage
  1.type = sensors_msgs/Image
  1.desc = Loop Closure Image and Query Image combined together.
    }
  param {
    0.name = ~matching_threshold
    0.type = double  
    0.default = 15
    0.desc = Matching Threshold for geometrical verification. It is varied with environment.
    1.name = ~distance
  1.type = double  
  1.default = 0.8
  1.desc = Nearest neighbor distance ratio. Generally this ratio is fixed and should not   be varied. However to get more matching features in the K-D tree, you can increase the distance threshold. 
  2.name = ~hessian
  2.type = int
  2.default = 100
  2.desc = Hessian threshold, This threshold varies the number of descriptor per image. If threshold is lowered, number of keypoint detected are increased and vice-versa.
  3.name = ~noOfDescriptors
  3.type = int
  3.default = 1000
  3.desc = Number of descriptors which you want to keep in each image.  
  4.name = ~candidates
  4.type = int
  4.default = 1
  4.desc = Number of candidates for geometrical verification step using RANSAC.
  5.name = ~loopProbability
  5.type = double
  5.default = 0.1
  5.desc = Minimum probability for each loop closure candidate.
  }
}
```


