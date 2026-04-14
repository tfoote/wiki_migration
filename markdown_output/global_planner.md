## Overview

This package provides an implementation of a fast, interpolated global
planner for navigation. This class adheres to the
\`nav_core::BaseGlobalPlanner\` interface specified in the
[nav_core](nav_core) package. It was built as a more flexible
replacement to [navfn](navfn), which in turn is based on
[NF1](http://cs.stanford.edu/group/manips/publications/pdfs/Brock_1999_ICRA.pdf).

## Examples of Different Parameterizations

### Standard Behavior

All parameters default. ![](attachment:GlobalPlanner.png)

### Grid Path

\`use_grid_path=True\` ![](attachment:GridPath.png) Path follows the
grid boundaries.

### Simple Potential Calculation

\`use_quadratic=False\` ![](attachment:Nonquad.png) Slightly different
calculation for the potential. Note that the original potential
calculation from [navfn](navfn) is a quadratic approximation. Of what,
the maintainer of this package has no idea.

### A\* Path

\`use_dijkstra=False\` ![](attachment:AStar.png) Note that a lot less of
the potential has been calculated (indicated by the colored areas). This
is indeed faster than using Dijkstra\'s, but has the effect of not
necessarily producing the same paths. Another thing to note is that in
this implementation of A\*, the potentials are computed using
4-connected grid squares, while the path found by tracing the potential
gradient from the goal back to the start uses the same grid in an
8-connected fashion. Thus, the actual path found may not be fully
optimal in an 8-connected sense. (Also, no visited-state set is tracked
while computing potentials, as in a more typical A\* implementation,
because such is unnecessary for 4-connected grids). To see the
differences between the behavior of Dijkstra\'s and the behavior of A\*,
consider the following example.

#### Dijkstra\'s

![](attachment:Dijkstra.png)

#### A\*

![](attachment:AStar2.png)

### Old Navfn Behavior

\`old_navfn_behavior=True\` For reproducing paths just like
[NavFn](navfn) did. ![](attachment:OldNavFn.png)

Note:

-   The start of the path does not match the actual start location.
-   The very end of the path moves along grid lines.
-   All of the coordinates are slightly shifted by half a grid cell

## Orientation filter

As a post-processing step, an orientation can be added to the points on
the path. With use of the orientation_mode parameter (dynamic
reconfigure), the following orientation modes can be set:

-   \`None=0\` (No orientations added except goal orientation)
-   \`Forward=1\` (Positive x axis points along path, except for the
    goal orientation)
-   \`Interpolate=2\` (Orientations are a linear blend of start and goal
    pose)
-   \`ForwardThenInterpolate=3\` (Forward orientation until last
    straightaway, then a linear blend until the goal pose)
-   \`Backward=4\` (Negative x axis points along the path, except for
    the goal orientation)
-   \`Leftward=5\` (Positive y axis points along the path, except for
    the goal orientation)
-   \`Rightward=6\` (Negative y axis points along the path, except for
    the goal orientation)

The orientation of point i is calculated using the positions of \`i -
orientation_window_size\` and \`i + orientation_window_size\`. The
window size can be altered to smoothen the orientation calculation.

\<\<Youtube(NQ2z90i5V2I&rel=0)\>\>

## ROS API

```clearsilver
pub {
  0.name  = ~<name>/plan
  0.type = nav_msgs/Path
  0.desc = The last plan computed, published every time the planner computes a new path, and used primarily for visualization purposes.
}
param {
  0.name = ~<name>/allow_unknown
  0.default = `true`
  0.type = bool
  0.desc = Specifies whether or not to allow the planner to create plans that traverse unknown space. NOTE: if you are using a layered costmap_2d costmap with [[costmap_2d/hydro/obstacles|a voxel or obstacle layer]], you must also set the track_unknown_space param for that layer to be true, or it will convert all your unknown space to free space (which planner will then happily go right through).
  1.name = ~<name>/default_tolerance
  1.default = 0.0
  1.type = double
  1.desc = A tolerance on the goal point for the planner. The planner will attempt to create a plan that is as close to the specified goal as possible but no further than `default_tolerance` away. 
  2.name = ~<name>/visualize_potential
  2.default = `false`
  2.type = bool
  2.desc = Specifies whether or not to visualize the potential area computed via a !PointCloud2. 
  3.name = ~<name>/use_dijkstra
  3.default = `true`
  3.type = bool
  3.desc = If true, use dijkstra's algorithm. Otherwise, A*. 
  4.name = ~<name>/use_quadratic
  4.default = `true`
  4.type = bool
  4.desc = If true, use the quadratic approximation of the potential. Otherwise, use a simpler calculation. 
  5.name = ~<name>/use_grid_path
  5.default = `false`
  5.type = bool
  5.desc = If true, create a path that follows the grid boundaries. Otherwise, use a gradient descent method.
  6.name = ~<name>/old_navfn_behavior
  6.default = `false`
  6.type = bool
  6.desc = If for some reason, you want global_planner to exactly mirror the behavior of [[navfn]], set this to true (and use the defaults for the other boolean parameters)
  7.name = ~<name>/lethal_cost
  7.default = 253
  7.type = int
  7.desc = Lethal Cost (dynamic reconfigure)
  8.name = ~<name>/neutral_cost
  8.default = 50
  8.type = int
  8.desc = Neutral Cost (dynamic reconfigure)
  9.name = ~<name>/cost_factor
  9.default = 3.
  9.type =  double
  9.desc = Factor to multiply each cost from costmap by (dynamic reconfigure)
  10.name = ~<name>/publish_potential
  10.default = True
  10.type = bool
  10.desc = Publish Potential Costmap (dynamic reconfigure)
  11.name = ~<name>/orientation_mode
  11.default = 0
  11.type = int
  11.desc = How to set the orientation of each point (`None=0`, `Forward=1`, `Interpolate=2`, `ForwardThenInterpolate=3`, `Backward=4`, `Leftward=5`, `Rightward=6`) (dynamic reconfigure)
  12.name = ~<name>/orientation_window_size
  12.default = 1
  12.type = int
  12.desc = What window to use to determine the orientation based on the position derivative specified by the orientation mode (dynamic reconfigure)
  13.name = ~<name>/outline_map
  13.default = true
  13.type = bool
  13.desc = Outlines the global costmap with lethal obstacles. For the usage of a non static (rolling window) global costmap this needs to be set to false
}
```
