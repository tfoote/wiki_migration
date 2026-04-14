## Git

Please use the git for stable releases.

<https://github.com/parcon/ARL-sphero-command/tree/master/ARL_sphero_command>

## Overview

This package allows ROS to control a [Sphero](http://www.gosphero.com/).
ARL_sphero_command is in alpha/proof of concept stage. The package
currently changes the color of the robot then starts receiving joy
messages to command it\'s velocity!

Developed by Parker Conroy at the Algorithmic Robotics Lab @ University
of Utah.

## Fast Tutorial

-   sudo apt-get install bluez libbluetooth3 libbluetooth-dev ( you may
    also need bluez-alsa, bluez-gstreamer, and bluez-cups)
-   gedit src/sphero_command (you\'ll need to change the line labled
    with \"***\* SPHERO ID **\*\" to the ID of your robot)*
-   Connect/Pair your computer to the robot
-   rosmake ARL_sphero_command
-   rosrun ARL_sphero_command sphero

## Incoming Features

-   Ability to listen for other velocity commands messages (twist or
    joy)
-   Other robot message types (raw motor, timeout and more!)
