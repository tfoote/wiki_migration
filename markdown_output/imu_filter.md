# Introduction

This package provides a library for filtering inertial measurement units
(IMU).

In general an IMU consists of an accelerometer and a gyroscope. Both,
the measured accelerations and angular rates have biases which drift
over time.

This package provides an Extended Kalman Filter implementation for
tracking movements of an IMU considering these biases.

The state contains the following elements:

-   Orientation
-   Position
-   Velocity
-   Gyroscope bias
-   Accelerometer bias
-   Gravity vector

# Usage

In order to demonstrate the usage of the filter, we are going to develop
a little sample application.

We will have the IMU lying on the table and running the propagation of
the filter as when we receive measurements. Every n-th iteration, we\'ll
create an artificial measurement, including the Identity pose (which
should tell the filter, that the IMU didn\'t move.

TODO: Step by step walk through \...
