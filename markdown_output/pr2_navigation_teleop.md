## Overview

This package provides an XML file for running [pr2_teleop](pr2_teleop)
in a configuration that allows it to run in parallel with the
[navigation](navigation) stack on the PR2 robot.

## Building Blocks

-   **\`teleop.xml\`**: Launches [pr2_teleop](pr2_teleop) in a
    [navigation](navigation) stack friendly configuration. Designed to
    be included by applications that wish to run autonomous navigation
    on the PR2, but also allow for manual teleop of the robot.
