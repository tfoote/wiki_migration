![\|width="333",height="200"](attachment:Logo-white-medium.jpg)

## Description

This package offer visualizations for [asr_psm](asr_psm) learner and
inference results using RViz and gnuplot.

**Learned** gaussian mixture models (GMMs) representing the relations
between scene objects are drawn as ellipsoids representing their kernels
(in position), connected by arrows:

![\|width="490",height="370"](attachment:1.png)

*Figure 1: Learning of a relation based on an example. Arrows indicate
the relative positions in the coordinate frame of the parent node,
depicted to the right. A single Gaussian kernel was learned.*

![\|width="680",height="300"](attachment:2.png)

*Figure 2: Visualization of another learned model. The covariance
ellipsoids describe the relative position of an object in the frame of
the superior (parent) object. The trajectory relative to it is marked by
the arrows. Here, a more complex trajectory was more precisely described
by two kernels.*

![\|width="420",height="350"](attachment:3.png)

*Figure 3.1: An office scenario consisting of two screens with
adjustable height, a keyboard and a cup placed reative to them. The
trajectories of all objects are projected onto a camera image here.*

![\|width="440",height="270"](attachment:4.png)

*Figure 3.2: The Probabilistic Scene Model of the relative object poses
for the same scene.*

In **inference**, the relation graph is drawn as arrows, colours based
on the probability calculated for the relation. Probability of the
complete scene is shown as a gnuplot bar chart (gnuplot screen terminal
required).

![\|width="840",height="500"](attachment:5.png)

*Figure 4: Inference result for a scene consisting of 4 objects. The
vertical arrow in the upper left indicates the selected reference
object, its colour the likelihood of the scene.*

For a description of how the package is used in context, see the
documentation for [asr_psm](asr_psm).

## Functionality

Creates markers to depict the structures described above and publishes
them.

Uses gnuplot-io to send gnuplot commands to a live window.

## Usage

### Needed packages

-   [asr_resources_for_psm](asr_resources_for_psm)

### Needed software

-   RViz
-   A gnuplot screen terminal like gnuplot-io.
-   Eigen
-   Boost

### Start system

Started from [asr_psm](asr_psm).

Otherwise, use functions in your code:

*asr_psm_visualizations* mirrors the hierarchical model structure of
[asr_psm](asr_psm) in its hierarchical structure of *RViz*-Visualizers:

1\. !ProbabilisticSceneModelVisualization 1.
!ProbabilisticSceneVisualization 1.
!ProbabilisticPrimarySceneObjectVisualization 1.
!ProbabilitsicSecondarySceneObjectVisualization

Build trees of visualizers with
superiorVisualizer->appendVisualizer(inferiorVisualizer)

The visualizers take the following input:

1\. PSMVis *.: scale*, *sigma multiplier* (to scale Gaussian
ellipsoids),* frame id*: through setDrawingParameters() (see
*Parameters*) 1. PSVis: * description*-string: constructor 1. Primary:*
description*. *AsrResourcesForPSM Pose:* setPose(). Visualize wiht
drawInLearningMode(), drawInInferenceMode() or drawInTargettingMode()
(in inference: shows the model kernels). 1. Secondary: In *learner*,
append Gaussian kernels to visualize with appendKernel(mean,
covariance).

*!GnuplotVisualization* takes *bar labels*, *chart title*,* y axis
label* and *range*: initAnimatedBarChart(). Also pairs of *description*
and *likelihood*: updateBarChartValues().

*GMMGnuplotVisualization *uses gnuplot to visualize Gaussian Kernels as
histograms (given as *data* to plotOrientationHistogram()) for a given
rotation axis *rotaxis*.

![\|width="650",height="410"](attachment:6.png)

*Figure 5: Kernel in orientation for pitch-axis.*

## ROS Nodes

### Published Topics

-   /psm

### Parameters

Parameters *scaleFactor*, *sigmaMultiplier* and *frame_id* set by
[asr_psm](asr_psm)'s launch files:

-   *base_frame_id*: The name of the frame the objects should be
    transformed to. default: "/PTU".
-   *scale_factor*: to enlarge the visualization. default: "1.0".
-   *sigma_multiplier*: multiplier to the sigma of the standard
    deviation. default: "3.0" in learner, "2.0" in inference.

## Tutorials

The tutorial for the [asr_psm](asr_psm) package describes the output of
asr_psm_visualizations in context of [asr_psm](asr_psm).
