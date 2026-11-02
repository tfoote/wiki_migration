## Overview

This software package provides a driver and a ROS interface for Bota
Systems 6 axis force-torque sensors. Since 17/11/2020, the driver
supports Rokubi and SenseONE sensors in both configurations with
Serial(RS422) and EtherCAT electronics.

**Authors(s):** Ilias Patsiaouras, Mike Karamousadakis

## Installation

### Installing from binaries

Run in a terminal: 

```
$ sudo apt install ros-$ROS_DISTRO-bota-driver
```



### Installing from Source

In order to install the `bota_driver` package from source, you need to
have the following dependencies:

#### Dependencies

- [Robot Operating System (ROS)](http://wiki.ros.org) (middleware for
  robotics - obviously),
- [soem](https://github.com/mgruhler/soem)

**Note:** The [soem](http://wiki.ros.org/soem) dependency is released in
ROS, so it's a binary dependency for a source installation.

#### Fetching the code

To build the `bota_driver` from source, clone the latest version from
the source code repository into your catkin workspace:


```
$ cd catkin_workspace/src
$ git clone https://gitlab.com/botasys/bota_driver.git
```



Before building, you need to make sure that all the binary dependencies
are installed. To do so, run in a terminal:



```
$ cd catkin_workspace && rosdep update && rosdep install --from-path src --ignore-src -y
```



#### Building

Compile the package using:

1\. The `catkin_tools` package:



```
$ cd catkin_workspace
$ catkin build bota_driver
```



2\. If you don't have the `catkin_tools` package, you can still build
from source with `catkin_make`:



```
$ cd catkin_workspace
$ catkin_make --only-pkg-with-deps bota_driver
# Don't forget to switch back to building all packages when you are done:
# catkin_make -DCATKIN_WHITELIST_PACKAGES=""
```



3\. Finally, you can build from source with `catkin_make_isolated`.
The only difference is that each package will be processed sequentially:



```
$ cd catkin_workspace
$ catkin_make_isolated --pkg bota_driver
```



## Packages

**\*`rokubimini`**: The core C++ library to interface one or multiple
rokubimini devices. Contains abstract interfaces to start the
communication.

**\*`rokubimini_ethercat`**: The ethercat implementation of
rokubimini.

**\*`rokubimini_serial`**: The serial implementation of rokubimini.

**\*`rokubimini_manager`**: The manager of multiple rokubiminis,
independently of their implementation (ethercat or serial).

**\*`rokubimini_bus_manager`**: An abstract class for managing a bus.

**\*`rokubimini_factory`**: The factory that creates each
implementation based on the configuration file `setup.yaml`.

**\*`bota_device_driver`**: Contains a ROS node that communicates with
a manager that handles one or multiple rokubiminis (depends on the
config file `setup.yaml`). This package contains config files
`config/setup.yaml` and `config/rokubimini_sensor.yaml` to configure
the communication and the sensor itself.

**\*`bota_node`**: ROS node wrapper with some convenience functions
using **`bota_worker`**.

**\*`bota_worker`**: High resolution and threaded version of the ROS
rate class.

**\*`bota_signal_handler`**: Contains a static signal handling helper
class.

**\*`rokubimini_msgs`**: Contains the definitions of the ROS messages
and services used for communication over ROS.

## Nodes

### rokubimini

ROS node that establishes communication with the available rokubi mini
devices and publishes their captured data in standardized ROS messages.

#### Published Topics

- `/rokubimini/<name>/ft_sensor_readings/reading`
  ([rokubimini_msgs/msg/Reading](https://docs.ros.org/en/rolling/p/rokubimini_msgs/msg/Reading.html)):
  The whole reading structure (including Force/torque, IMU and
  temperature data) measured from the device with name <name>
- `/rokubimini/<name>/ft_sensor_readings/imu`
  ([sensor_msgs/msg/Imu](https://docs.ros.org/en/rolling/p/sensor_msgs/msg/Imu.html)):
  The IMU data measured from the device with name <name>
- `/rokubimini/<name>/ft_sensor_readings/wrench`
  ([geometry_msgs/msg/WrenchStamped](https://docs.ros.org/en/rolling/p/geometry_msgs/msg/WrenchStamped.html)):
  The Wrench (3-axis Force + 3-axis Torque) data measured from the
  device with name <name>
- `/rokubimini/<name>/ft_sensor_readings/temperature`
  ([sensor_msgs/msg/Temperature](https://docs.ros.org/en/rolling/p/sensor_msgs/msg/Temperature.html)):
  The temperature measured from the device with name <name>

#### Parameters

- `~num_spinners` (`int`, default: `1`): Number of concurrent spinners
  to use
- `~rokubimini_setup_file` (`string`, default:
  `"$(find bota_device_driver)/config/setup.yaml"`): The location of the
  rokubimini setup file
- `~sensor_config_name` (`string`, default: `""`): The name of the
  sensor (used for debugging a single sensor)
- `~standalone` (`boolean`, default: `true`): Checks if the node runs in
  standalone mode
- `~time_step` (`double`, default: `0.01`): The time step for polling
  the sensors

## Configuration

### Configuration Parameters

The following parameters can be set in the `setup.yaml`:

- `name`: The name of the rokubimini devices. Needed to handle
  multiple devices on the master side. **Note:** The `<name>` in the
  published topics is taken from this configuration parameter.
- `configuration_file`: The relative path to the configuration file of
  the sensor
- `product_code`: The product code of each device.
- For the ethercat devices:
- `ethercat_bus`: The ethercat bus containing the sensor. Is the
  ethernet adapter name on which the sensor is connected, as indicated
  in the `ifconfig` command output.
- `ethercat_address`: The address of the slave. Ethercat addresses are
  distributed to each slave incrementally. The slave closest to the
  master has address 1, the second one 2 etc.
- For the serial devices:
- `port`: The serial port to connect to communicate with the serial
  sensor.
- `baud_rate`: The baud rate used for serial communication.

The following parameters can be set in `rokubimini_sensor.yaml` in the
`bota_device_driver` package:

- `set_reading_to_nan_on_disconnect`: (`true`\|`false`) Sets the
  reading to nan when the sensor disconnects
- `imu_acceleration_range`:
- 0 = ±2g,
- 1 = ±4g,
- 2 = ±8g,
- 3 = ±16g
- `imu_angular_rate_range`:
- 0 = ±250°/s,
- 1 = ±500°/s,
- 2 = ±1000°/s,
- 3 = ±2000°/s
- `imu_acceleration_filter`: (cut-off Freq)
- 1 = 460Hz,
- 2 = 184Hz,
- 3 = 92Hz,
- 4 = 41Hz,
- 5 = 21Hz,
- 6 = 10Hz,
- 7 = 5Hz
- `imu_angular_rate_filter`: (cut-off Freq)
- 3 = 184Hz,
- 4 = 92Hz,
- 5 = 41Hz,
- 6 = 21Hz,
- 7 = 10Hz,
- 8 = 5Hz
- `sinc_filter_size`: (cut-off Freq high/low@sampling Freq)
- 51 = 1674/252Hz@1000Hz,
- 64 = 1255/189Hz@800Hz,
- 128 = 628/94.5hz@400Hz,
- 205 = 393/59.5Hz@250Hz,
- 256 = 314/47.5Hz@200Hz,
- 512 = 157/23.5@100Hz
- `fir_disable`:
- false = low cut-off frequency,
- true = high cut-off frequency from the above result
- e.g. for sinc filter_size: 48 and fir_disable: 1 you get cut-off freq
  1674Hz@1000Hz sample rate
- `chop_enable`: should be always false
- `fast_enable`: (only applies if fir_disable is false) True = will
  result in low cut-off frequency but would be still able to catch step
  impulses of high cut-off frequency
- `calibration_matrix_active`: Use the calibration matrix to compute
  sensor output
- `temperature_compensation_active`: Compensate drift due to
  temperature !not supported yet!
- `imu_active`: Chooses which IMU type is active:
- 0 = no imu active,
- 1 = internal IMU active,
- 2 = external IMU active (if available),
- 3 = both IMUs active
- `coordinate_system_active`: Set a user-defined coordinate system
- `inertia_compensation_active`: Enables compensation due to inertia
  effect
- `orientation_estimation_active`: Enables orientation estimation and
  outputs a quaternion

### Configuration File Examples

1\. `setup.yaml` example 

```
rokubiminis:
  - name:                     ft_sensor0
    configuration_file:       rokubimini_sensor.yaml
    product_code:             1
    port:                     /dev/ttyUSB0
    baud_rate:                460800
  - name:                     ft_sensor1
    configuration_file:       rokubimini_sensor.yaml
    product_code:             2
    ethercat_bus:             eth0
    ethercat_address:         1
```

 2.
`rokubimini_sensor.yaml` example 

```
set_reading_to_nan_on_disconnect:  false

imu_acceleration_range: 3
imu_angular_rate_range: 3

imu_acceleration_filter: 1
imu_angular_rate_filter: 3

force_torque_filter:
  sinc_filter_size: 512
  chop_enable:      false
  fir_disable:      true
  fast_enable:      false

force_torque_offset:
  Fx: 0.0
  Fy: 0.0
  Fz: 0.0
  Tx: 0.0
  Ty: 0.0
  Tz: 0.0

sensor_configuration:        
  calibration_matrix_active:            true
  temperature_compensation_active:      false
  imu_active:                           1   #0=no IMU, 1=internal, 2=external, 3=both
  coordinate_system_active:             false
  inertia_compensation_active:          0
  orientation_estimation_active:        0
use_custom_calibration:                 false
sensor_calibration:
  calibration_matrix:
    1_1:  -0.0120389
    1_2:  0.0206676
    1_3:  0.0011164
    1_4:  0.0010681
    1_5:  0.0006295
    1_6:  0.0002029
    2_1:  -0.0109678
    2_2:  -0.0207696
    2_3:  -0.0004745
    2_4:  -0.0010578
    2_5:  0.0005841
    2_6:  0.0001810
    3_1:  0.0217535
    3_2:  -0.0005980
    3_3:  -0.0002701
    3_4:  -0.0000395
    3_5:  -0.0011409
    3_6:  0.0001944
    4_1:  0.0155252
    4_2:  0.0100866
    4_3:  -0.0148265
    4_4:  0.0003659
    4_5:  -0.0005838
    4_6:  0.0000055
    5_1:  -0.0169726
    5_2:  0.0114251
    5_3:  -0.0146247
    5_4:  0.0004339
    5_5:  0.0006094
    5_6:  0.0000011
    6_1:  -0.0001013
    6_2:  -0.0197085
    6_3:  -0.0146952
    6_4:  -0.0007251
    6_5:  -0.0000145
    6_6:  -0.0000077
```



## Launch File Examples

### Default parameters

**Note:** You need to have root privileges to the network card, if you
want to have access to the EtherCAT devices. For example, this can be
done with escalated privileges (e.g. `su root`):



```
$ su root
# source /path/to/catkin_workspace/devel/setup.bash
# roslaunch bota_device_driver rokubimini.launch
```



**Note:** In the above example it is assumed that the `root` user has
a bash terminal. If this isn't the case change it accordingly.

**Note:** If no EtherCAT device is present, the above command could work
without `root` privileges provided that the user is in the `dialout`
group. This can be done with:



```
$ sudo usermod -a -G dialout username
```

 Please log off and log in again for the changes
to take effect!

### Custom parameters

1\. Example with custom `time_step`: 

```
$ roslaunch bota_device_driver rokubimini.launch time_step:=0.1
```



2\. Example with custom `rokubimini_setup_file`:


```
$ roslaunch bota_device_driver rokubimini.launch rokubimini_setup_file:=$(pwd)/myawesomesetup.yaml
```



## Unit Tests

No unit tests so far.

## Support

For any queries or problems found with the software provided, please
contact us at `sw-support@botasys.com`
