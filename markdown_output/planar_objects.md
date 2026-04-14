## Overview

Experimental research code for the detection of planar objects and
articulation models using stereo data.

\'\'\'This package is deprecated. Please look at the
[articulation](articulation) stack for the replacing packages. Tutorials
are available in [articulation_tutorials](articulation_tutorials) and a
demo using Microsoft Kinect is available in
[articulation_perception](articulation_perception).\'\'\'

## Video

[Youtube](https://www.youtube.com/watch?v=bNtm6_FBJp8)

## Project: 6D poses of planar surfaces from point clouds

Jürgen Sturm

\'\'Autonomous Intelligent Systems Lab, University of Freiburg,
Germany\'\'

### Description:

During my stay at Willow Garage this summer, I am focusing on object
pose registration from point clouds. In particular, I want to be able to
detect, register and track rectangular surfaces that are common in
indoor (kitchen) environments, such as cabinet drawers and doors. These
pose and shape estimates could then be used to learn articulation models
for the interior of a kitchen, as shown in my previous work.

While 6D pose registration is a challenging problem for machine
perception in the general case, it becomes (more) feasible when
additional assumptions are being made. The stereo cameras of PR2 use
structured light to improve the matching process. As a result, they
produce highly accurate and dense depth maps. In contrast to 3D laser
scanners, the point clouds can be obtained at a normal video frame
rates.

We first apply a RANSAC-based approach for segmenting out individual
planes in the depth image. Then, for each individual plane, we start at
a random start pixel with a rectangle of an initial size, and optimize
iteratively its pose and size using a greedy search.

[More information](http://www.informatik.uni-freiburg.de/~sturm/projectposeestimationfrompointclouds.html)
(including data sets and videos)

[Willow Garage Blog](http://www.willowgarage.com/blog/2009/08/10/detecting-planar-objects-and-articulation-models)

[Video on YouTube](http://www.youtube.com/watch?v=bNtm6_FBJp8&eurl=http://www.willowgarage.com/blog/2009/08/10/detecting-planar-objects-and-articulation-models&feature=player_embedded)
