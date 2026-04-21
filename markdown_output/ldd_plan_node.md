## Description

[ldd_plan_node](ldd_plan_node) performs kinematic planning for the PR2
arm using the LDD algorithm, documented here:



```
Paul Vernaza and Daniel D. Lee. Learning dimensional descent planning for a highly-articulated robot arm. In Proceedings of the International Conference on Intelligent Robots and Systems, 2011.
```



## Usage

The planner runs as a ROS node that serves `GetMotionPlan` requests.
It may be launched by executing `roslaunch ldd_plan_node
ldd_plan_node.launch`.

Various environment variables can be set that affect the performance of
the algorithm. A convenient way to experiment with different parameters
is to prepend them to the launch command as so:



```
option1=true option2=100 roslaunch ldd_plan_node ldd_plan_node.launch
```



### Parameters

The following parameters may be set via environment variables:

-   `bboxMargin` (float > 0, default 1.0) In each iteration, LDD
    searches for variations of the current path in some direction. The
    larger this parameter, the further LDD searches along each
    direction. If LDD cannot find a feasible path for your problem,
    increasing this parameter may help. Visualizing the paths with
    `plotting=true` may help to determine whether this parameter needs
    to be increased.

```{=html}
<!-- -->
```
-   `nPath0` (int > 0, default 100) LDD discretizes the initial path
    (a straight line) by choosing `nPath0` samples along its length.
    Suppose that the samples chosen in this way are a distance L apart.
    In subsequent iterations, the path is resampled so that the distance
    between samples is exactly L. Increasing this parameter therefore
    increases the resolution of the search.

```{=html}
<!-- -->
```
-   `nGradSamp` (int > 0, default 10000) LDD will draw this many
    random samples of the cost gradient in order to learn a basis for
    dimensional descent. Increasing this parameter will decrease the
    variance in the paths found by LDD, at the expense of increased
    runtime.

```{=html}
<!-- -->
```
-   `nCostThreads` (int > 0, default 1) LDD will spawn this many
    threads in parallel to compute the cost function and cost gradients.

```{=html}
<!-- -->
```
-   `minPlanTime` (float > 0, default 0.)

```{=html}
<!-- -->
```
-   `maxPlanTime` (float > 0, default infinity) LDD will optimize the
    path for at least `minPlanTime` seconds. It will then return the
    best path found so far, if a feasible path has been found, or
    continue planning until a feasible path is found or `maxPlanTime`
    is reached (whichever comes first).

```{=html}
<!-- -->
```
-   `minIt` (int > 0, default 0)

```{=html}
<!-- -->
```
-   `maxIt` (int > 0) The minimum and maximum number of iterations to
    perform before termination.

```{=html}
<!-- -->
```
-   `dimMaxOpt` (int >= 0, default -1) LDD cycles through a set of
    variation directions, optimizing the path sequentially in each of
    these directions, in order of "decreasing importance" before
    looping around. `dimMaxOpt` is the index of the maximum dimension
    to be optimized before looping around. If set to -1, LDD will
    optimize all dimensions.

```{=html}
<!-- -->
```
-   `fCheckSampRate` (float > 0, default 20.) At each iteration, the
    current path is resampled at a rate given by `fCheckSampRate`
    samples per radian and then checked for feasibility. The lower this
    parameter, the more likely it is that [ldd_plan_node](ldd_plan_node)
    will consider feasible a path that [move_arm](move_arm) considers
    infeasible (and will hence abort). Setting this parameter too high,
    however, will adversely affect performance.

```{=html}
<!-- -->
```
-   `plotting` (boolean, default false) If set to true, a 2D
    visualization will be shown illustrating the cost restricted to the
    currently-optimized submanifold and the optimal path found
    restricted to this sub manifold.

## Known issues

-   Important parameters in ldd_plan_node.launch are currently
    undocumented

```{=html}
<!-- -->
```
-   `right_arm` is currently hard-coded in LDDPlan.hh
