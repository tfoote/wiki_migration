## Overview

This package contains scripts and launch files for testing SRS assisted
arm navigation pipeline. There is fake decision making which can be used
instead of [srs_decision_making](srs_decision_making) for testing.
Package also contains copy of assisted arm navigation generic states.

## Installation

-   install [srs_assisted_arm_navigation](srs_assisted_arm_navigation),
    [srs_assisted_arm_navigation_ui](srs_assisted_arm_navigation_ui) and
    [srs_assisted_grasping](srs_assisted_grasping)
-   build srs_arm_navigation_tests with ```
rosmake srs_arm_navigation_tests
```

## Configuration

TBD

## Usage

File arm_manip_generic_states.py implements two smach generic states
which can be used as part of state machine:

-   move_arm_to_given_positions_assisted
-   for user assisted trajectory planning i.e. for move the arm to the
    pre-grasp position
-   move_arm_from_a_given_position_assisted
-   for user assisted navigation to a safe position

```{=html}
<!-- -->
```
-   launch needed stuff:

```
roslaunch srs_arm_navigation_tests fake_dm_test.launch
```

-   spawn milk:

```
roslaunch srs_arm_navigation_tests milk_box.launch
```

-   run the fake decision making

```
roslaunch srs_arm_navigation_tests fake_dm_only.launch
```

-   It will test both generic states in this order:
-   move_arm_to_given_positions_assisted
-   move_arm_from_a_given_position_assisted
-   Fake_dm will try to use [srs_grasping](srs_grasping) services to
    obtain pregrasp position. If it's not possible fake ones will be
    used (just to test visualization).

## Tutorials

-   [Usage of assisted arm navigation](srs_arm_navigation_tests/Tutorials/Usage of assisted arm navigation)
