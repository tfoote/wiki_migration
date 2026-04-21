  -- ---------------------------------------------------------------------------------------------------------------------------------------------------------------------- --
     <style="border: 1px solid black; background-color:#FFFF00; text-align: center; vertical-align:top;" tablewidth="100%"> /!\\ Warning! This package is unstable.   
  -- ---------------------------------------------------------------------------------------------------------------------------------------------------------------------- --

## Overview

This package contains launchers, maps and world descriptions for the
TurtleBot simulation with [stdr_simulator](stdr_simulator).

![architecture_overview\|width=680](attachment:turtlebot_stdr/turtlebot_in_stdr.png)\]\]

## Tutorials

Refer to the [Tutorials](turtlebot_stdr/Tutorials) for help on how to
run.

## Differences from Stage_ros

-   TF frames used in STDR can lead to confusion due to name conflicts.
    A direct comparison of TF transforms is shown in the following
    diagram:
    [![architecture_overview\|width=680](https://raw.githubusercontent.com/mehditlili/turtlebot_simulator/indigo/turtlebot_stdr/documentation/architecture_overview.png)](https://raw.githubusercontent.com/mehditlili/turtlebot_simulator/indigo/turtlebot_stdr/documentation/architecture_overview.png)

```{=html}
<!-- -->
```
-   Currently, STDR doesn't offer an option to simulate odometry noise.
    It is only possible to simulate noise in laser or sonar sensors.
