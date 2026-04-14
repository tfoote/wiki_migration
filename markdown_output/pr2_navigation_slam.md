## Overview

This package contains configuration files for the [move_base](move_base)
and [gmapping](gmapping) nodes meant to be run in an application that
requires SLAM-based global navigation. This package also includes launch
files that bring up [rviz](rviz) and [nav_view](nav_view) with global
navigation specific configuration options.

## Applications

-   \'\'\'\`rviz/rviz_move_base_slam.launch\`\'\'\': Starts [rviz](rviz)
    with a SLAM friendly navigation setup.
-   \'\'\'\`nav_view/nav_view_move_base_slam.launch\`\'\'\': Starts
    [nav_view](nav_view) with a SLAM friendly navigation setup.

## Building Blocks

-   \'\'\'\`move_base.xml\`\'\'\': Holds a PR2 specific configuration of
    the [move_base](move_base) node designed fow navigation with a SLAM
    system. Should be run in conjunction with [gmapping](gmapping) or
    another SLAM system with a similar interface.
-   \'\'\'\`slam_gmapping.xml\`\'\'\': Holds a PR2 specific
    configuration of the [gmapping](gmapping) node. Designed to be
    included by applications that wish to run [gmapping](gmapping) on
    the PR2.

## Configuration Files

-   \'\'\'\`config/base_local_planner_params.yaml\`\'\'\': Holds
    parameters for the [base_local_planner](base_local_planner) specific
    to SLAM-based navigation on the PR2.
-   \'\'\'\`config/global_costmap_params.yaml\`\'\'\': Holds parameters
    for the global [ costmap](costmap_2d ) used in thee
    \`move_base.xml\` configuration file. This is the costmap used by
    the [navfn](navfn) planner, and in this case, receives periodic
    updates from a SLAM system such as [gmapping](gmapping).
-   \'\'\'\`config/local_costmap_params.yaml\`\'\'\': Holds parameters
    for the local [ costmap](costmap_2d ) used in the \`move_base.xml\`
    configuration file. This is the costmap used by the
    [base_local_planner](base_local_planner) planner, which operates in
    an odometric frame.
-   \'\'\'\`config/move_base_params.yaml\`\'\'\': Holds SLAM-based
    navigation specific parameters for the [move_base](move_base) node.
