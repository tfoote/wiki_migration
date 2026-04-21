**ATOM** is a set of calibration tools for multi-sensor, multi-modal,
robotic systems, based on the optimization of atomic transformations as
provided by a ROS based robot description.

<https://github.com/lardemua/atom>

## Introduction

ATOM is a general methodology so it should be able to calibrate a vast
spectrum of robotic system configurations. It is able to tackle classic
configurations with fixed sensors, or hand-eye configurations with
sensors positioned at the end-effector of robotic manipulators.

Currently, supported sensors are:

-   RGB Cameras
-   3D LiDARs
-   Depth cameras

Moreover, ATOM provides several scripts to facilitate all the steps of a
calibration procedure. Available functionalities include:

-   Creation and configuration of ATOM calibration packages
-   Interactive positioning of sensors for setting initial estimate
-   Interactive data labeling and collection
-   Dataset review and manual correction of labels
-   Calibration
-   Several evaluation methods to assess the calibration

**ATOM** is extensively integrated into ROS, making use of several ROS
features to implement nice functionalities.

## How to use

For instructions on how to install and use, check the documentation:

<https://lardemua.github.io/atom_documentation/>

## Report a Bug

Report bugs or request features
[on GitHub](https://github.com/lardemua/atom/issues).
