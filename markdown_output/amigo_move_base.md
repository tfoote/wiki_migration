# Under Construction

This package has not been released yet, but will be soon.

# Package Summary

This package contains configuration files to control the base of amigo,
that is make amigo move to a certain location.

## Functional Description

The launch file base_navigation.launch starts two nodes. The first one
loads a global map of everything the robot has seen so far and a local
map based on the current sensor input. It then starts a motion planner
for both maps. The second node starts the simultanious localization and
mapping (slam) algorithm that translates the sensor input into a map and
calculates amigo\'s location based on that.
