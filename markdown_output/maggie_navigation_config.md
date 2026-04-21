## Overview

This package holds a number of common configuration files for the
[move_base](move_base) and [amcl](amcl) nodes meant to be run in an
application that requires global navigation with a pre-specified static
map. It also contains navigation specific sensor configurations. In
particular, it holds parameter settings for the
[base_local_planner](base_local_planner), [costmap_2d](costmap_2d), and
[move_base](move_base) components of the [move_base](move_base) node
that are shared between many different configurations of the
[navigation](navigation) stack run on the
[Social Robot Maggie](Robots/Maggie).

## Building Blocks

-   **\`launch/real/navigation_real.launch\`**:
-   **\`launch/simulation/navigation_simulation.launch\`**:

```{=html}
<!-- -->
```
-   **\`launch/amcl.launch\`**: holds a [Maggie robot](Robots/Maggie)
    specific configuration of the [amcl](amcl) node. Designed to be
    included by applications that wish to run [amcl](amcl) on the
    [Maggie robot](Robots/Maggie). Assumes a map is available from an
    instance of the [map_server](map_server) node.
-   **\`launch/move_base.launch\`**: holds a
    [Maggie robot](Robots/Maggie) specific configuration of the
    [move_base](move_base) node designed for navigation with a
    pre-specified static map. Should be run in conjunction with the
    [amcl](amcl) and [map_server](map_server) nodes.

```{=html}
<!-- -->
```
-   **\`launch/laser/hokuyo.launch\`**: ensures that the hokuyo laser is
    in the proper configuration for autonomous navigation.
-   **\`launch/laser/sick.launch\`**: ensures that the sick laser is in
    the proper configuration for autonomous navigation, also brings up a
    number of filters that are applied to laser scans used while
    navigating.

## Configuration Files

-   **\`config/base_local_planner_params.yaml\`**: holds parameters for
    the [base_local_planner](base_local_planner) specific to global
    navigation on the [Social Robot Maggie](Robots/Maggie).
-   **\`config/costmap_common_params.yaml\`**:
-   **\`config/global_costmap_params.yaml\`**: holds parameters for the
    global [costmap](costmap_2d) used in the \`move_base.launch\`
    configuration file. This is the costmap used by the [navfn](navfn)
    planner, and in this case, is initialized by a static map offered by
    an instance of the [map_server](map_server) node.
-   **\`config/initial_pose.yaml\`**:
-   **\`config/local_costmap_params.yaml\`**: holds parameters for the
    local [costmap](costmap_2d) used in the \`move_base.launch\`
    configuration file. This is the costmap used by the
    [base_local_planner](base_local_planner) planner, which operates in
    an odometric frame.
