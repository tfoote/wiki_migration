## Overview

This package contains methods for filtering robot trajectories. These
filters are focused on the needs of industrial robots and applications.

## Filters



```clearsilver

node.0 {
  name = uniform_sample_filter
  desc = Re-samples a planned trajectory with a uniform time step in between points.  Re-sampling is done using a higher order spline smoother in joint space.  The filter expects fully defined trajectories (position, velocity, acceleration).

  param {
    0.name = sample_duration
    0.type = float
    0.desc = step size in seconds between way-points.
  }
}

node.1 {
  name = n_point_filter
  desc = Reduces trajectory to be <=N total points.  This reduction process uses existing points (re-sampling and interpolation are not done).  This filter works best with a uniformly sampled trajectory, but this is not required.  If the trajectory is less than N points, no filtering is performed.

  param {
    0.name = n_points
    0.type = float
    0.desc = maximum number of waypoints (must be >=2)
  }
```



## Applying Filters

{ }}}} {}

## Tutorials

For more detailed examples see the
[tutorials](industrial_trajectory_filters/Tutorials) page.

[Included page industrial/contact_us_tech_support not found](Included page industrial/contact_us_tech_support not found)

## Reporting bugs
