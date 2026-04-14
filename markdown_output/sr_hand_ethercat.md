## Introduction

sh_hand_ethercat is high level package in the as-of-yet unreleased
shadow_robot_ethercat stack. This package has necessary launch files for
running the Shadow robot hand as a stand-alone (not mounted on a PR2)
device.

Use the tutorials for more information on getting shadow hand setup and
running.

## Installation

The srh_ethercat_hand stack is currently located in the c-turtle
sandbox. To code depends on some features that have not yet been
released. You will need:

-   ROS + PR2 package : ros-cturtle-pr2
-   shadow_hand_ethercat stack from c-turtle sandbox
-   pr2_mechanism from trunk

Below is a example rosinstall overlay that be used against a
ros-cturtle-pr2 distribution ```
- svn:
    uri: https://code.ros.org/svn/wg-ros-pkg/branches/trunk_cturtle/sandbox/shadow_robot_ethercat
    local-name: shadow_robot_ethercat
- svn:
    uri: https://code.ros.org/svn/wg-ros-pkg/stacks/pr2_mechanism/trunk
    local-name: pr2_mechanism
```
