## Notice

  -- ---------------------------------------------------------------------------------------------------------------------------------------------- --
     \<#FFFF00\> Turtlebot Calibration is used for iRobot create base TurtleBot gyro calibration. Kobuki base does not need any gyro calibration.   
  -- ---------------------------------------------------------------------------------------------------------------------------------------------- --

## Overview

The current calibration accounts for the following two factors:

-   The gyros installed in the robot are relatively cheap and do not
    have exactly the same properties. There has been observed about a
    10% difference in the linear rates reported by different units
    tested.
-   The odometry is affected by the floor surface. Between common
    livingroom carpet and linoleum floors at 10% difference in reporting
    has also been observed.

There are more areas to improve:

-   compensating for linear distance on different carpets
-   an effect of the traveling velocity on the odometry has also been
    observed, with a larger error at mid-range speeds.

## Use

To use this package please follow the
[Tutorial](/Tutorials/Calibrate Odometry and Gyro)
