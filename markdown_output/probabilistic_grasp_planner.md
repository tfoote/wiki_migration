This package is currently unreleased. It will be included in the next
released major version of the manipulation pipeline, tentatively
scheduled for November 2010.

## Motivation

Please see the [motivation](probabilistic_grasp_planner/motivation)
page.

## Overview

Please see the [overview](probabilistic_grasp_planner/overview) page.

[Youtube](https://www.youtube.com/watch?v=YiLzZdYAilI)

## Usage

This planner should act as a drop-in replacement for the database-backed
planner. Trunk of the manipulation pipeline should automatically use it,
Services:

-   [GraspPlanning](http://www.ros.org/doc/api/object_manipulation_msgs/html/srv/GraspPlanning.html).
    Takes a graspable object containing all of the different
    representations for the object, and returns a sorted list of the
    grasps for that object, ordered by their estimated probability of
    success.
