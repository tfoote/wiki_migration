1.  repository
    <https://github.com/ElettraSciComp/DStar-Trajectory-Planner>

## Overview

![](https://upload.wikimedia.org/wikipedia/commons/8/8f/D%2A-Algorithmus_Blockade_Two_running_two.png)

(the picture is taken from
[en.wikipedia.org/D\*](https://en.wikipedia.org/wiki/D*))

------------------------------------------------------------------------

`dstar_trajectory_planner` is a [move_base](move_base) plugin
implementing global trajectory planning with
[D\* informed incremental search algorithm](https://citeseerx.ist.psu.edu/viewdoc/summary?doi=10.1.1.15.3683)
with external optimizers. It strives to simplify the development of
robotic systems operating in dense industrial environments.

-   **Package** URL:
    <https://github.com/ElettraSciComp/DStar-Trajectory-Planner>

### Package Contents

The package contains two plugins:

-   **D-star trajectory planner** that maintains generation of the
    global trajectory on the provided costmap, and dynamic replanning by
    request coming from move_base.
-   **Virtual Walls module** processing JSON objects to generate the
    non-passable and explicitly passable zones as OpenCV polygons added
    over the existing map.

## Configuration

### Example Configuration



```YAML
DStarGlobalPlanner:
    goal_distance_threshold: 0.3
    neighbor_distance_threshold: 0.12
    occupancy_threshold: 64
    cutoff_distance: 16
    trajectory_optimizer:
        repulsion_gain: 70.0
        potential_field_radius: 12
    erosion:
        enable: true
        erosion_gap: 2
    paths:
        enable: true
        from: map.json # OPTIONAL PASSABLE ZONES FILE
```



### Parameters Explained

\
Here `cells` should be considered as elements of
<<MsgLink(nav_msgs/OccupancyGrid)>>.

## Development and Roadmap

The package was developed under the Remotization and Robotization
Initiative at [Elettra Sincrotrone Trieste](https://www.elettra.eu) by
the members of the ICT Group. It is part of an innovative flexible
control system for mobile robots that the group leaders presented in
Tokyo during
[16th IFToMM World Congress 2023](https://wc2023.jc-iftomm.org/). The
interested ones can find the published papers here:

-   [Universal Configurable Navigation and Control System for Industrial Unmanned Ground Vehicles with Differential Chassis](https://doi.org/10.1007/978-3-031-45770-8_29)
-   [D-Star-Based Optimized Trajectory Planner for Mobile Robots Operating in Dense Environments](https://link.springer.com/chapter/10.1007/978-3-031-67295-8_33)

### Roadmap

0\. Improve the initial documentation. 1. Implement the custom "magic"
linked list that keeps the sorted state. 2. Avoid map copying during the
initialization. 3. Separate area parsers completely from the kernel
library.
