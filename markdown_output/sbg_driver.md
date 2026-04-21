# Overview

ROS package for SBG Systems IMU.

The driver allows the user to configure the IMU (if possible, according
to the device), to receive messages from the Sbg message protocol,
publish ROS standard messages , and to calibrate the magnetometers.

# Installation

## Installation from packages

User can install the sbg_ros_driver through the standard ROS
installation system. ```
sudo apt-get install ros-$ROS_DISTRO-sbg-driver
```

## Installation from sources

1\. Clone the repository (use a Release version)
<https://github.com/SBG-Systems/sbg_ros_driver> 2. Build using the
normal ROS catkin build system

# Usage

## Enable communication with the SBG device

To be able to communicate with the device, be sure that your user is
part of the dialout group. Once added, restart your machine to save and
apply the changes.

```
sudo adduser $USER dialout
```

Afterwards, detect the port where your SBG device is connected (e.g.
/dev/ttyUSB0) using

```
dmesg | grep tty
```

and edit `sbg_device_uart_default.yaml` accordingly or (recommended)
define a [udev](https://wiki.debian.org/udev) rule (e.g. pointing to
/dev/sbg)

## Ros node for IMUs data

Run the ros node to receive messages from the SBG IMU.

Config files are available for uart or udp connection. Users should
properly define the device parameters. ```
roslaunch sbg_driver sbg_device.launch
```

## Ros node for magnetometers calibration

```
roslaunch sbg_driver sbg_device_mag_calibration.launch
```

## Configuration files

### Default config files

#### sbg_device_uart_default.yaml

This config file is the default one for Uart connection with the device.
It does not configure the device through the ROS node, so it has to be
previously configured (manually or with the ROS node).

It define a few outputs for the device :

-   /sbg/imu_data, /sbg/ekf_quat at 25Hz,
-   ROS standard outputs /imu/data, /imu/velocity, /imu/temp at 25Hz,
-   /sbg/status; /sbg/utc_time, /imu/utc_ref at 1 Hz.

#### sbg_device_udp_default.yaml

This config file is the default one for an Udp connection with the
device. It does not configure the device through the ROS node, so it has
to be previously configured (manually or with the ROS node).

It defines a few outputs for the device :

-   /sbg/imu_data, /sbg/ekf_quat at 25Hz
-   ROS standard outputs /imu/data, /imu/velocity, /imu/temp at 25Hz
-   /sbg/status, /sbg/utc_time and /imu/utc_ref at 1Hz.

### Example config files

-   *ellipse_A_default.yaml*, default config file for an Ellipse-A
-   *ellipse_E_default.yaml*, default config file for an Ellipse-E with
    an external antenna and external Gnss
-   *ellipse_N_default.yaml*, default config file for an Ellipse-N with
    an external antenna and internal Gnss

## Messages publishing

### SBG custom messages

The sbg_driver defines some custom ROS messages, corresponding to the
SBG message protocol.

-   **/sbg/air_data**
    [SbgAirData](http://docs.ros.org/api/sbg_driver/html/msg/SbgAirData.html)
-   **/sbg/ekf_euler**
    [SbgEkfEuler](http://docs.ros.org/api/sbg_driver/html/msg/SbgEkfEuler.html)
-   **/sbg/ekf_nav**
    [SbgEkfNav](http://docs.ros.org/api/sbg_driver/html/msg/SbgEkfNav.html)
-   **/sbg/ekf_quat**
    [SbgEkfQuat](http://docs.ros.org/api/sbg_driver/html/msg/SbgEkfQuat.html)
-   **/sbg/ekf_event{A,B,C,D,E}**
    [SbgEvent](http://docs.ros.org/api/sbg_driver/html/msg/SbgEvent.html)
-   **/sbg/gps_hdt**
    [SbgGpsHdt](http://docs.ros.org/api/sbg_driver/html/msg/SbgGpsHdt.html)
-   **/sbg/gps_pos**
    [SbgGpsPos](http://docs.ros.org/api/sbg_driver/html/msg/SbgGpsPos.html)
-   **/sbg/gps_raw**
    [SbgGpsRaw](http://docs.ros.org/api/sbg_driver/html/msg/SbgGpsRaw.html)
-   **/sbg/gps_vel**
    [SbgGpsVel](http://docs.ros.org/api/sbg_driver/html/msg/SbgGpsVel.html)
-   **/sbg/imu_data**
    [SbgImuData](http://docs.ros.org/api/sbg_driver/html/msg/SbgImuData.html)
-   **/sbg/imu_short**
    [SbgImuShort](http://docs.ros.org/api/sbg_driver/html/msg/SbgImuShort.html)
-   **/sbg/mag**
    [SbgMag](http://docs.ros.org/api/sbg_driver/html/msg/SbgMag.html)
-   **/sbg/mag_calib**
    [SbgMagCalib](http://docs.ros.org/api/sbg_driver/html/msg/SbgMagCalib.html)
-   **/sbg/odo_vel**
    [SbgOdoVel](http://docs.ros.org/api/sbg_driver/html/msg/SbgOdoVel.html)
-   **/sbg/ship_motion**
    [SbgShipMotion](http://docs.ros.org/api/sbg_driver/html/msg/SbgShipMotion.html)
-   **/sbg/utc_time**
    [SbgUtcTime](http://docs.ros.org/api/sbg_driver/html/msg/SbgUtcTime.html)

### ROS standard messages

In order to define ROS standard topics, it requires sometimes several
SBG messages to be merged. You have to active the needed SBG outputs.

-   **/imu/data**, IMU dara, requires **/sbg/imu_data** and
    **/sbg/ekf_quat**
-   **/imu/temp**, IMU temperature, requires **/sbg/imu_data**
-   **/imu/velocity**, IMU velocity data, requires **/sbg/imu_data**
-   **/imu/mag**, IMU magnetic field, requires **/sbg/mag**
-   **/imu/pres**, IMU pressure data, requires **/sbg/air_data**
-   **/imu/pos_ecef**, Earth-Centered Earth_Fixed position, requires
    **/sbg/ekf_nav**
-   **/imu/utc_ref**, UTC time reference, requires **/sbg/utc_time**
-   **/imu/nav_sat_fix**, Navigation satellite, requires
    **/sbg/gps_pos**

## Services

The sbg_device_mag node handles the magnetic calibration for suitable
devices. It uses services to control the calibration process.

-   **/sbg/mag_calibration**
    [Trigger](http://docs.ros.org/api/std_srvs/html/srv/Trigger.html),
    service to start/stop the magnetic calibration
-   **/sbg/mag_calibration_save**,
    [Trigger](http://docs.ros.org/api/std_srvs/html/srv/Trigger.html),
    service to save the magnetic calibration.

# HowTo

## Configure the SBG device

For compatible devices, the SBG ROS driver allows the user to configure
the device before starting the data handling.

To do so, the configuration yaml file should be modified.
```
# Configuration of the device with ROS.
confWithRos: true
```

## Calibrate the magnetometers

```
$ roslaunch sbg_driver sbg_device_mag_calibration.launch
$ rosservice call /sbg/mag_calibration
// Proceed rotations on the IMU
$ rosservice call /sbg/mag_calibration
// If the magnetic calibration results are satisfaying, it could be uploaded
$ rosserive call /sbg/mag_calibration_save
```

# Contributing

Bugs, issues, or features additions should be done on the Github
repository.
