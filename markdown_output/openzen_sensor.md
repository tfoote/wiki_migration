## OpenZen Node for ROS

This software allows to forward sensor data from sensor connected via
OpenZen to ROS. It supports a wide range of
[LP-Research LPMS Sensor models](https://lp-research.com/lpms-inertial-measurement-unit-imu-series/).

OpenZen is a library for high performance sensor data streaming and
processing and supports multiple sensor models:
[OpenZen](https://bitbucket.org/lpresearch/openzen/)

The full documentation for OpenZen ROS can be found here:
[OpenZen ROS documentation](https://lpresearch.bitbucket.io/openzen/latest/ros.html#ros-api)

For the list of all supported LPMS sensor models, please check
[List of supported Sensors](https://lpresearch.bitbucket.io/openzen/latest/supported_sensors.html).
Please note that this ROS driver does not support Bluetooth sensor
models in the default configuration. If you need Bluetooth support, you
need to compile the ROS package yourself by following these
[Instructions](https://lpresearch.bitbucket.io/openzen/latest/ros.html#compilation)
and make sure you read the instructions on
[Bluetooth usage in ROS](https://lpresearch.bitbucket.io/openzen/latest/ros.html#limitations-of-openzen-ros-driver)

## Installing via the Package Manager

The OpenZen ROS driver is part of the official ROS distribution and you
can conveniently install it via the package manager of your Linux
distribution. Please check this website to see if the OpenZen ROS driver
is available for the ROS distribution you use:

[OpenZen ROS Package](https://index.ros.org/p/openzen_sensor/bitbucket-lpresearch-openzenros/#melodic)

For example, on Ubuntu 18.04 and with ROS distribution Melodic Morenia,
the OpenZen ROS driver can be installed with this command:

```
apt install ros-melodic-openzen-sensor
```

## Running the Driver

You can then run the OpenZen ROS driver with this command in the window
you used to compile the software:

```
rosrun openzen_sensor openzen_sensor_node
```

By default, it will connect to the first available sensor. If you want
to connect to a specific sensor, you can use the serial name of the
sensor as parameter, for example:

```
rosrun openzen_sensor openzen_sensor_node _sensor_name:="LPMSCU2000573"
```

If your sensor is configured for a different baud rate, you can use the
baudrate parameter to give a specfic baud rate setting:

```
rosrun openzen_sensor openzen_sensor_node _sensor_name:="LPMSCU2000573" _baudrate:=115200
```

Now you can print the IMU values from ROS with:

```
rostopic echo /imu/data
```

To output the values of a GPS unit (if available) use this command:

```
rostopic echo /imu/nav
```

Or plot some values (for example linear acceleration) with

```
rosrun rqt_plot rqt_plot /imu/data/linear_acceleration
```

If you want to readout the values of two OpenZen sensors simultaneously,
you need to rename the topics and the node names likes this:

```
rosrun openzen_sensor openzen_sensor __name:="cu2node" _sensor_name:="LPMSCU2000573" imu:=/cu2_imu 
rosrun openzen_sensor openzen_sensor __name:="ig1_node" _sensor_name:="LPMSIG1000032" imu:=/ig1_imu
```

Alternatively, we have prepared a sample launch file
openzen_lpms_ig1.launch to demonstrate data acquisition and plotting
using openzen_sensor_node: ```
roslaunch openzen_sensor openzen_lpms_ig1.launch
```

## Published Topics

Tor the full list of published ROS topics, please have a look at this
list:
[OpenZen ROS Topics](https://lpresearch.bitbucket.io/openzen/latest/ros.html#ros-api)
