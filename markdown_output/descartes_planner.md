## Concepts

This package contains implementations of Descartes *planners*. For more
information on the architecture of Descartes, see
[this page](descartes). A Descartes planner is responsible for
intelligently searching the valid robot configurations for a given
trajectory (with tolerances) and generating a solution in the form of a
sequence of joint configurations.

## Reference Implementations

Descartes currently offers two reference implementations of trajectory
planners. Both accept a sequence of arbitrary trajectory points for
input and output a sequence of joint trajectory points. See more details
at the [descartes_trajectory](descartes_trajectory) package page.

### Dense Planner

The first and most straightforward planner is *DensePlanner*. It takes
dense trajectories and attempts to find a path through the points that
minimizes total joint motion.

Conceptually, it performs the following operations: 1. For every
trajectory point, calculate all of the inverse kinematic solutions for
that point. These are calculated using the sampling logic implemented by
the trajectory point, and the robot model\'s knowledge of
statics/dynamics. 2. For every pair of contiguous points, calculate the
movement cost and feasibility between each joint solution for the
starting point and each joint solution for the ending point. 3. Build a
graph from the data where vertexes represent kinematic solutions and
edges represent movement costs. 4. Search this graph for the lowest cost
route from any starting configuration to any ending configuration using
Dijkstra\'s algorithm.

### Sparse Planner

*Sparse Planner* builds on top of the working principles of dense
planner, but attempts to save computational time by \'sampling\' a given
trajectory. Sparse planner runs inverse kinematics on a subset of the
original points and then attempts to solve the rest of the trajectory
using joint space interpolation and forward kinematics.

For example, if the planner must solve for points A, B, and C. It might
run inverse kinematics on A and C, and then try to infer the joint
solution for B from those. It would check its inference by running
forward kinematics and comparing it to the desired pose.

## Limitations and Failure Modes

Currently neither planner makes any effort to resolve discontinuities in
the joint space graphs generated from user trajectories and will fail if
any of the following occur: 1. A point in your trajectory is not
reachable by the robot model. 2. A point is reachable but involves a
configuration flip exceeding some threshold.
