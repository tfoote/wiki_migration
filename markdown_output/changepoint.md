## Overview

This package provides a ROS service that implements CHAMP, an online
Bayesian changepoint detection algorithm. Given a set of parameterized
models, CHAMP can detect changepoints in time series data, in which the
underlying model generating the data appears to change. CHAMP can detect
changes between different models, as well as changes in generative
parameters within a given model class.

Several model types come standard with the package (1D Gaussian,
articulation models), and more can be added easily through a pluginlib
interface. When adding additional models, essentially all that is
required is a likelihood / BIC function for the model, and a way of
fitting model parameters to a given segment of data.

This [tech report](http://www.cs.umass.edu/%7Esniekum/pubs/CHAMP.pdf)
describes the technical aspects of CHAMP in detail.

## Installation

Currently, this package must be installed from source and also requires
the articulation package to build the articulation plugin. Both are easy
to build using rosmake:

```shell
svn co http://alufr-ros-pkg.googlecode.com/svn/trunk/articulation
git clone https://github.com/sniekum/changepoint.git
cd changepoint
rosmake
```

## Parameters

There are only 5 parameters of CHAMP that must be set:

-   len_mean: The expected mean length of segments.

```{=html}
<!-- -->
```
-   len_sigma: The expected variance of segment length. Make this large
    if little is known about the length of segments.

```{=html}
<!-- -->
```
-   min_seg_len: The minimum length of any segment. This is generally
    dictated by model class (i.e. 3 points needed to fit a plane). This
    can also be set higher to prevent overfitting.

```{=html}
<!-- -->
```
-   max_particles: The maximum number of particles in the particle
    filter used to keep track of the distribution over the location of
    the most recent changepoint. More particles results in better
    results, but slower performance.

```{=html}
<!-- -->
```
-   resamp_particles: The number of particles to resample down to after
    max_particles have been exceeded. Usually this will be equal to
    max_particles, but there is evidence in the literature that having
    it be significantly less than max_particles can be useful, because
    the resampling decision can be made jointly once every few time
    steps, rather than incrementally at every time step.

NOTE: Currently, the DetectChangepoints ROS service only supports
detection on batch data, despite the algorithm being online. Future
updates will expose an interface that allows online usage.

## Example 1: Gaussian 1-D model

This first example uses a single model, in which data is generated from
a zero-mean Gaussian, but where the variance of the distribution can
change between segments. Simulated data is provided in the test/data
folder that contains 5 segments of Gaussian data with changing variance.

First, run the changepoint server: ```shell
roslaunch changepoint changepoint_server.launch
```

Then:

```shell
cd test
python gaussTest.py
``` should result in: ![](attachment:ex1.png)
```
Model: Gaussian    Length: 41
Start: 0
End: 40
   mu : 0.0
   sigma : 2.38037437793
   log_likelihood : -93.7340487169
   model_evidence : -97.4476207836

Model: Gaussian    Length: 60
Start: 41
End: 100
   mu : 0.0
   sigma : 1.11776428109
   log_likelihood : -91.8161427535
   model_evidence : -95.9104873158

Model: Gaussian    Length: 31
Start: 101
End: 131
   mu : 0.0
   sigma : 3.18557109903
   log_likelihood : -79.9046735685
   model_evidence : -83.338660773

Model: Gaussian    Length: 49
Start: 132
End: 180
   mu : 0.0
   sigma : 1.58176429671
   log_likelihood : -91.9964906366
   model_evidence : -95.8883109347

Model: Gaussian    Length: 69
Start: 181
End: 249
   mu : 0.0
   sigma : 2.39939035641
   log_likelihood : -158.296572189
   model_evidence : -162.530678693
```

## Example 2: Articulation models

This second example uses 3 separate models of articulated motion from
the articulation package: rigid, prismatic, and revolute. This comes
from work described in:

J. Sturm, C. Stachniss, and W. Burgard. A probabilistic framework for
learning kinematic models of articulated objects. Journal of Artificial
Intelligence Research, 41(2):477--526, 2011.

Example data is provided in the test/data folder (in the form of a
difference trajectory of the poses of two objects) that contains 2
segments: rotational motion, followed by rigid motion between two
objects.

First, run the changepoint server: ```shell
roslaunch changepoint changepoint_server.launch
```

Then:

```shell
cd test
python articTest.py
``` should result in: ![](attachment:ex2.png)
```
Model: rotational    Length: 43
Start: 0
End: 42
   rot_radius : 0.100188846698
   rot_center.x : -0.0237696457762
   rot_center.y : -0.0232395299195
   rot_center.z : -0.00476561153689
   rot_axis.x : 0.0168210955552
   rot_axis.y : -0.0347638765967
   rot_axis.z : 0.240095357072
   rot_axis.w : 0.969980795243
   rot_orientation.x : -0.000544986444002
   rot_orientation.y : -0.0180811333546
   rot_orientation.z : 0.133017461034
   rot_orientation.w : 0.990948601425
   log_likelihood : 185.088191002
   model_evidence : 6.43118550699

Model: rigid    Length: 63
Start: 43
End: 105
   rigid_position.x : 0.0763430434138
   rigid_position.y : -0.0408163083626
   rigid_position.z : 0.00269622400637
   rigid_orientation.x : 0.0437177485907
   rigid_orientation.y : -0.019221237714
   rigid_orientation.z : 0.0095507242092
   rigid_orientation.w : 0.998813338991
   log_likelihood : 258.428841159
   model_evidence : 245.99943698
```

Unlike the Gaussian example, the articulation models have some
parameters to tune. Currently, these are hardcoded in articulation.cpp.
A brief description of each:

-   sigma_position: The expected standard deviation of position data in
    meters. It is very important for this to be approximately accurate
    based on the noise of the source of your data, as it greatly affects
    how heavily to penalize deviations from a model, which in turn
    distinguish between actual change and noise.

```{=html}
<!-- -->
```
-   sigma_orientation: The expected standard deviation of orientation
    data in radians. Also important to set correctly for the same
    reasons as sigma_position.

```{=html}
<!-- -->
```
-   optimizer_iterations: The number of iterations to run nonlinear BFGS
    optimization on each set of parameters from each SAC iteration. Even
    if this is set to 0, there will still be optimization done on the
    final parameters. It is generally fine to set this to 0, and setting
    it higher than zero will greatly impact running time.

```{=html}
<!-- -->
```
-   sac_iterations: The number of sample consensus (SAC) iterations to
    randomly try to find good model parameters for each segment fit.

```{=html}
<!-- -->
```
-   prior_outlier_ratio: The expected weighted outlier ratio from Sturm
    et al.
