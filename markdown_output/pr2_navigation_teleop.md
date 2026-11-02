## Overview

This package provides an XML file for running
[pr2_teleop](https://index.ros.org/p/pr2_teleop) in a configuration that
allows it to run in parallel with the
[navigation](https://index.ros.org/p/navigation) stack on the PR2 robot.

## Building Blocks

- **`teleop.xml`**: Launches
  [pr2_teleop](https://index.ros.org/p/pr2_teleop) in a
  [navigation](https://index.ros.org/p/navigation) stack friendly
  configuration. Designed to be included by applications that wish to
  run autonomous navigation on the PR2, but also allow for manual teleop
  of the robot.
