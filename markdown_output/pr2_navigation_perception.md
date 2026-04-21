## Overview

This package contains navigation specific sensor configurations for the
PR2 robot. Using the configuration files in this package guarantees that
the PR2 runs with the sensor profiles and filters recommended for
autonomous navigation on the robot.

## Building Blocks

-   **\`lasers_and_filters.xml\`**: Ensures that the lasers on the PR2
    and the tilt sled are in the proper configuration for autonomous
    navigation, also brings up a number of filters that are applied to
    laser scans and point clouds used while navigating.
-   **\`ground_plane.xml\`**: Brings up the ground plane detection node
    for the PR2 which filters the ground plane out of laser scans used
    to provide obstacle information to the [move_base](move_base) node.

## Configuration Files

-   **\`config/base_self_filter.yaml\`**: The configuration for the
    [pr2_navigation_self_filter](pr2_navigation_self_filter) that
    removes parts of the robot body from laser scans coming from the
    base laser of the PR2.
-   **\`config/point_cloud_footprint_filter.yaml\`**: Removes points
    that fall within the footprint of the PR2 from point clouds passed
    to the [move_base](move_base) node.
-   **\`config/tilt_self_filter.yaml\`**: The configuration for the
    [pr2_navigation_self_filter](pr2_navigation_self_filter) that
    removes parts of the robot body from laser scans coming from the
    tilt laser of the PR2.
-   **\`config/tilt_laser_filters.yaml\`**: Holds intensity, angular
    bounds, and shadow filters for the tilt laser on the PR2.
-   **\`config/shadow_filter.yaml\`**: Holds the shadow filter
    configuration for the base laser on the PR2.
