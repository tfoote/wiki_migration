This package implements the motion planner interface that the move_arm
package requires. This interface is described in detail in the
[arm navigation tutorials](move_arm/Tutorials). To use CHOMP, simply
launch the pr2_arm_navigation_planning/launch/chomp_planning.launch file
instead of any of the other planners.

## Video

[Youtube](https://www.youtube.com/watch?v=6aZThRpmr58)

## ROS API

-   ROS API is UNREVIEWED and UNSTABLE
-   C++ API is UNREVIEWED and UNSTABLE
-   This planner has currently been configured and tested only for the
    PR2 right arm. Testing and release for other robots is on the
    roadmap.
-   This planner cannot deal with path constraints

## Tutorials

To check out tutorials for this package, just follow the general set of
Tutorials on the [arm navigation tutorials](arm_navigation/Tutorials)
page. Replace the launch file for OMPL with the launch file for CHOMP
(the launch file for CHOMP can be found in
pr2_arm_navigation_planning/launch).
