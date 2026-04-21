\[\[<https://www.raspberrypi.org/products/sense-hat/>\|![Astro PI Sense HAT\|width=400](https://raw.githubusercontent.com/allxone/sensehat_ros/master/doc/images/sense_hat.jpg)\|target="_blank"\]\]

## Overview

The sensehat_ros ROS package helps integrating the Astro Pi Sense HAT
module with the ROS ecosystem. Stick events together with environmental
and IMU sensors data are published to ROS topics. Several ROS services
are exposed to interact with the device, including the LED matrix.

The package has been tested on Melodic Python 2 and Noetic Python 3
environments. ROS 2 support is on the roadmap, any help would be
appreciated. Deployment tests with the Sense HAT device were
successfully run on different Raspberry PI models (Pi 2, Pi 3 and Pi 4),
either installing ROS on the Raspberry Pi OS or using Docker via the
Balena Cloud platform.

Thanks to the sense-emu Python package, the sensehat_ros package can be
run without the actual Sense HAT device on several Linux configs.
Simulated deployments were tested on x86 Ubuntu Bionic and Debian Buster
(via WSL 2) and with Docker on both x86 and QEMU-based arm32v7.

The Sense HAT Emulator GUI can be easily started with the
`sense_emu_gui` command.

\[\[<https://pypi.org/project/sense-emu/>\|![ debug level log output\|width=400](https://raw.githubusercontent.com/allxone/sensehat_ros/master/doc/images/sense_emu_gui.png)\|target="_blank"\]\]

## Setup

The sensehat_ros package is intended to be installed on a Raspberry PI
device equipped with an Astro Pi Sense HAT module and with a supported
ROS distro. Binary release is not an option with pip dependencies in the
package.xml, so the package have to be built and installed from source.

```
$ mkdir ~/catkin_ws
$ cd ~/catkin_ws
$ wstool init src
$ wstool set -t src sensehat_ros https://github.com/allxone/sensehat_ros.git --git --version=master
$ wstool up -t src
$ rosdep update
$ rosdep install --from-paths src --ignore-src -r -y
$ catkin_make
$ catkin_make install
```

Please, follow the Code API documentation link for additional details
about building and testing the package.

## Usage

### Test run

To verify if the sensehat_ros ROS package is working properly a ROS node
can be started with a modified logging level.

```
$ source install/setup.bash
$ roslaunch --screen -v sensehat_ros sensehat_ros.launch DEBUG:=True
```

The onscreen log output should present sensor data coming from the
device (or the emulator):
![ debug level log output\|width=600](https://raw.githubusercontent.com/allxone/sensehat_ros/master/doc/images/debug_output.png)

### Examples

The package includes two sample client nodes to show how to call
services interactively or consume messages from topics.

```
# Assuming "roslaunch sensehat_ros sensehat_ros.launch" already running in another shell
$ source install/setup.bash

# Example 1: invoking sensehat_ros ROS services
$ rosrun sensehat_ros sample_client
Received Environmental (H: 39.73828125, TH: 20.9375, TP: 20.9520833333, P: 995.614257812)
Reset the Matrix to white
Show some random pixel colors
Reset the Matrix to black

# Example 2: consuming sensehat_ros topics
$ rosrun sensehat_ros sample_listener
[INFO] [1597358715.590474]: Heard Environmental (H: 39.2265625, TH: 20.90625, TP: 20.8791666667, P: 995.602294922)
[INFO] [1597358715.597447]: Heard IMU (Mode: get_orientation_degrees_rpy, X: 67.4909682543, Y: 0.0, Z: 82.490182137)
[INFO] [1597358716.590834]: Heard IMU (Mode: get_orientation_degrees_rpy, X: 67.4909682543, Y: 0.0, Z: 82.490182137)
[INFO] [1597358717.590532]: Heard IMU (Mode: get_orientation_degrees_rpy, X: 67.4909682543, Y: 0.0, Z: 82.490182137)
^C
```

## ROS API

```clearsilver
name = sensehat_ros
desc = ROS node hosting the interface to the Sense HAT API
param {
  0.name = rotation
  0.type = int, optional
  0.desc = control Sense HAT LED matrix orientation
  0.default = 0
  1.name = low_light
  1.type = bool, optional
  1.desc = enable Sense HAT low-light mode
  1.default = False
  2.name = calibration 
  2.type = dict, optional
  2.desc = linear fixing for environmental readings (ex. {"humidity": -20.0})
  2.default = {}
  3.name = smoothing
  3.type = int, optional
  3.desc = number of observations to be used for median smoothing (0 = smoothing disabled)
  3.default = 0
  4.name = register_services
  4.type = bool, optional
  4.desc = control ROS services registration
  4.default = True
  5.name = environmental_publishing
  5.type = bool, optional
  5.desc = enable automatic publishing of environmental data (rate controlled by environmental_publishing_rate)
  5.default = True
  6.name = environmental_publishing_rate
  6.type = float, optional
  6.desc = environmental data publication frequency in seconds
  6.default = 12
  7.name = IMU_publishing
  7.type = bool, optional
  7.desc = enable automatic publishing of IMU data (rate controlled by imu_publishing_rate)
  7.default = False
  8.name = imu_publishing_mode
  8.type = string, optional
  8.desc = specify the Sense HAT API function to be used to get x,y,z/roll,pitch,yaw. Valid values are: get_orientation_radians_rpy, get_orientation_degrees_rpy, get_compass_raw_xyz, get_gyroscope_rpy, get_gyroscope_raw_xyz, get_accelerometer_rpy, get_compass_raw_xyz
  8.default = get_orientation_degrees_rpy
  9.name = imu_publishing_rate
  9.type = float, optional
  9.desc = IMU data publication frequency in seconds
  9.default = 1
  10.name = stick_publishing
  10.type = bool, optional
  10.desc = enable publishing of stick events
  10.default = True
  11.name = stick_sampling
  11.type = float, optional
  11.desc = indicates how frequently the Stick is checked for new events
  11.default = 0.2
}
pub {
  0.name = Environmental
  0.type = sensehat_ros/Environmental
  0.desc = Sense HAT Environmental sensors data (i.e. humidity, temperature and pressure)
  1.name = IMU
  1.type = sensehat_ros/IMU
  1.desc = Sense HAT IMU sensor data (e.g. pitch, roll, yaw).
  2.name = Stick
  2.type = sensehat_ros/Stick
  2.desc = Sense HAT Stick events
}
srv {
  0.name = Clear
  0.type = sensehat_ros/Clear
  0.desc = Sets all of the 64 LED matrix pixels to the specified RGB color and waits for the specified amount of seconds.
  1.name = EmulateStick
  1.type = sensehat_ros/EmulateStick
  1.desc = Remotely triggers a stick event without interacting with the Stick device.
  2.name = GetCompass
  2.type = sensehat_ros/
  2.desc = Gets the direction of North from the magnetometer in degrees. Warning: not allowed when imu_publishing=True due to potential set_imu_config interference.
  3.name = GetEnvironmental
  3.type = sensehat_ros/GetEnvironmental
  3.desc = gets the current humidity and temperature from the humidity sensor and temperature and pressure from the pressure sensor
  4.name = GetHumidity
  4.type = sensehat_ros/GetHumidity
  4.desc = Gets the percentage of relative humidity from the humidity sensor.
  5.name = GetIMU
  5.type = sensehat_ros/GetIMU
  5.desc = Queries Sense HAT IMU sensor. Warning: not allowed when imu_publishing=True due to potential set_imu_config interference.
  6.name = GetPressure
  6.type = sensehat_ros/GetPressure
  6.desc = Gets the current pressure in Millibars from the pressure sensor.
  7.name = GetTemperature
  7.type = sensehat_ros/GetTemperature
  7.desc = Gets the current temperature in degrees Celsius from the humidity sensor.
  8.name = SetPixels
  8.type = sensehat_ros/SetPixels
  8.desc = Sets each of the 64 LED matrix pixels to a specific RGB color and waits for the specified amount of seconds.
  9.name = ShowLetter
  9.type = sensehat_ros/ShowLetter
  9.desc = Shows a letter on the LED matrix and waits for the specified amount of seconds.
  10.name = ShowMessage
  10.type = sensehat_ros/ShowMessage
  10.desc = Scrolls a text message from right to left across the LED matrix and at the specified speed, in the specified colour and background colour.
  11.name = SwitchLowLight
  11.type = sensehat_ros/SwitchLowLight
  11.desc = Switches on/off the LED matrix “low light” mode and returns the current state.
}
```
