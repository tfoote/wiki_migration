## Overview

This package contains launch and configuration files for the
[move_base](move_base) and [amcl](amcl) nodes meant to be run in an
application that requires global navigation with a pre-specified static
map.

## Applications

-   **`launch/2dnav_linear.launch`**: Starts global navigation using
    the simple linear navigation of [cob_linear_nav](cob_linear_nav).
-   **`launch/2dnav_ros_dwa.launch`**: Starts global navigation using
    the [move_base](move_base) node of the [navigation](navigation)
    stack with the
    [Dynamic Window local path planning](dwa_local_planner).
-   **`launch/2dnav_ros_tr.launch`**: Starts global navigation using
    the [move_base](move_base) node of the [navigation](navigation)
    stack with the
    [Trajectory Rollout local path planning](base_local_planner).

Furthermore it holds two launch files for internal navigation packages
of Fraunhofer IPA.

-   **`launch/2dnav_ipa.launch`**: Starts global navigation using the
    IPA Navigation.
-   **`launch/2dnav_ipa_extloc.launch`**: Starts global navigation
    using the IPA Navigation with external localization.

## Building Blocks

-   **`launch/2dnav_linear.xml`**: Holds a Care-O-bot specific
    configuration of the [cob_linear_nav](cob_linear_nav) node. Designed
    to be included by applications that wish to run linear navigation on
    the Care-O-bot.
-   **`launch/2dnav_ros_dwa.xml`**: Holds a Care-O-bot specific
    configuration of the [move_base](move_base) node with the dynamic
    window approach. Designed to be included by applications that wish
    to run global navigation with DWA on the Care-O-bot.
-   **`launch/2dnav_ros_tr.xml`**: Holds a Care-O-bot specific
    configuration of the [move_base](move_base) node with the trajectory
    rollout approach. Designed to be included by applications that wish
    to run global navigation with TR on the Care-O-bot.
-   **`launch/amcl_node.xml`**: Holds a Care-O-bot specific
    configuration of the [amcl](amcl) node. Designed to be included by
    applications that wish to run [amcl](amcl) on the Care-O-bot.
    Assumes a map is available from an instance of the
    [map_server](map_server) node.

## Configuration Files

-   **`config/global_costmap_params.yaml`**: Holds parameters for the
    global [ costmap](costmap_2d ) used in the `2dnav_ros_dwa.xml` and
    `2dnav_ros_tr.xml` building blocks. This is the costmap used by
    the [navfn](navfn) planner, and in this case, is initialized by a
    static map offered by an instance of the [map_server](map_server)
    node.
-   **`config/local_costmap_params.yaml`**: Holds parameters for the
    local [ costmap](costmap_2d ) used in the `2dnav_ros_dwa.xml` and
    `2dnav_ros_tr.xml` building blocks. This is the costmap used by
    the specific local planner, which operates in an odometric frame.
