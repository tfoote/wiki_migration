# Overview

The **stdr_samples** package provides code and launchers to demonstrate
the [STDR Simulator](stdr_simulator) functionalities. The available
samples follow.

## Obstacle avoidance

To perform simple obstacle avoidance spawn a robot equipped with a laser
sensor. Then simply execute the following command:

```
rosrun stdr_obstacle_avoidance robotX laser_Y
``` , where X the robot\'s ID and Y the laser\'s
ID. It is assumed that the laser has an orientation of 0 degrees,
relatively to the robot.
