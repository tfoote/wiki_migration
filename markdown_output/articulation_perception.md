Please see the tutorials for a demo of this package using Microsoft's
Kinect sensor.

## Introduction

This package provides a module that detects rectangles in depth images
and estimates their pose. Further, the module can track these rectangles
over time and publish them as ArticulatedTrack messages. From these
tracks, the articulation_models/model_learner_msg can learn the
kinematic model underlying the observed motion.

A demo launch file is available that runs the detector, model learner,
and visualization using RVIZ (see package tutorials). This
implementation is very efficient: it runs on a Intel Core2 Duo with more
than 10fps.

## Approach

The detector itself works as follows:

-   Input: a stream of dense depth images
-   Segment the depth image using RANSAC
-   Initialize a rectangle candidate in each plane
-   Iteratively optimize the pose of the candidate by maximizing an
    objective function (see paper) until convergence
-   Accept or reject the sample based on the pixel precision and recall
-   Assign the detected rectangle to an existing track or initialize a
    new track
-   Output: a stream of ArticulatedTrack messages

## Screen shots

The following images demonstrate how the detector, tracker, and model
learning works.

### Motivating example

Here, the lid of a laptop is opened and closed. By tracking the pose of
the laptop lid, the kinematic model of the lid is estimated from its
motion and visualized using RVIZ.

  -- -------------------------------------------- -- -------------------------------------------------------------------- -- ------------------------------------------------------------------- --
     ![\|height=160](attachment:laptop-rgb.png)      ![\|height=160](attachment:laptop-segmentation.png)                     ![\|height=160](attachment:laptop-rviz.png)                         
     The lid of a laptop is opened and closed        Visualization of the plane segmentation and the detected rectangle      Resulting kinematic model learned from a sequence of observations   
  -- -------------------------------------------- -- -------------------------------------------------------------------- -- ------------------------------------------------------------------- --

### Robustness against occlusions

Our approach also allows that parts of the tracked object are occluded:

  -- ------------------------------------------------------- -- --------------------------------------------------------------- --
     ![\|height=160](attachment:laptop-rgb-occlussion.png)      ![\|height=160](attachment:laptop-segmentation-occlusion.png)   
  -- ------------------------------------------------------- -- --------------------------------------------------------------- --

### Iterative pose fitting

Our approach segments the depth image into planes, and iteratively fits
a rectangle to each plane. During pose fitting, our approach minimizes a
cost function that is based on the number of true positive, false
positive, and true negative pixels.

  -- ------------------------------------------ -- ------------------------------------------ -- ------------------------------------------ --
     ![\|width=200](attachment:fitting-1.png)      ![\|width=200](attachment:fitting-2.png)      ![\|width=200](attachment:fitting-3.png)   
  -- ------------------------------------------ -- ------------------------------------------ -- ------------------------------------------ --

### Segmentation and Detection

After fitting rectangles to all detected planes, our approach filters
the candidates based on the pixel precision and recall. In these images,
the detected planes are colored in blue/green/red and the detected
rectangular objects are indicated using thick white borders.

  -- ----------------------------------------------- -- ----------------------------------------------- --
     ![\|width=200](attachment:segmentation-1.png)      ![\|width=200](attachment:segmentation-2.png)   
  -- ----------------------------------------------- -- ----------------------------------------------- --

### Examples of learned kinematic models

  -- ---------------------------------------------- --
     ![\|width=600](attachment:rviz-cabinet1.png)   
     ![\|width=600](attachment:rviz-cabinet2.png)   
     ![\|width=600](attachment:rviz-cabinet3.png)   
     ![\|width=600](attachment:rviz-cabinet4.png)   
  -- ---------------------------------------------- --

## More Information

More information (including videos, papers, presentations) can be found
on the homepage of
[Juergen Sturm](http://vision.in.tum.de/members/sturmju).

## Report a Bug

If you run into any problems, please feel free to contact Juergen Sturm
<juergen.sturm@in.tum.de>.

## References

Jürgen Sturm, Kurt Konolige, Cyrill Stachniss, Wolfram Burgard.
Vision-based Detection for Learning Articulation Models of Cabinet Doors
and Drawers in Household Environments. In Proc. of the IEEE
International Conference on Robotics and Automation (ICRA), Anchorage,
USA, 2010.
[pdf](http://www.informatik.uni-freiburg.de/~sturm/media/sturm10icra.pdf)
