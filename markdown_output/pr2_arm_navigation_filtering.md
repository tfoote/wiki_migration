## Overview

This package contains launch files and configuration files to launch
trajectory filters for the PR2 robot arms. The filters themselves can be
found in the [trajectory filters stack](trajectory_filters). This
package contains the following files:

-   config/filters.yaml - This particular file configures a trajectory
    filter chain with two filters:
-   a joint unnormalization filter that uses information about the
    current positions of the joints to unwrap continuous joints that are
    wrapped on the unit circle.
-   a \'\'short cutter\'\' that takes joint paths output by planning
    algorithms, connects random points in the path together using cubic
    splines and \'\'short cuts\'\' the path if the cubic spline
    trajectories are collision free.
-   launch/\*.launch - These files configure the filters for the right
    and left arms and also for both arms of the PR2 robot.

More information on configuring the filters can be found on the
[ filter configuration](trajectory_filter_server/YAML configuration)
page.

## Stability

1\. ROS API is REVIEWED but UNSTABLE - We will make our best effort to
keep the ROS API stable.
