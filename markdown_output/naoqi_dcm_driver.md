The hardware interface to connect to Nao, Romeo, and Pepper robots. You
can control the robot either by calling DCM commands or ALMotion (by
default). When calling DCM commands, you can achieve faster control
frequency but it can make the robot shaking because of the concurrence
between DCM and ALMotion. Especially when using DCM, please be careful
and use it at your own risks.

## What it does

The package allows to control a robot from ROS, while communicating with
Naoqi. The package is inspired by nao_dcm_driver, however it does not
require NAOqi SDK anymore and rather based on naoqi_libqi and
naoqi_libqicore. The package is more generic, and it works with any of
Nao, Romeo, and Pepper robots. It can run on a remote PC or locally on a
robot (after compiling on OpenNAO VM, deploying to your robot, and using
robot_ip:=127.0.0.1).

## How to use

The package should be used via the following wrapper-packages depending
on your robot (please, follow the links to get instructions on
installation and usage):

-   [nao_dcm_bringup](nao_dcm_bringup)

```{=html}
<!-- -->
```
-   [romeo_dcm_bringup](romeo_dcm_bringup)

```{=html}
<!-- -->
```
-   [pepper_dcm_bringup](pepper_dcm_bringup)
