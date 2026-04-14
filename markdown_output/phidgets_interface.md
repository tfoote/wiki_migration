# Package Summary

A package to read voltage from Phidgets\'s analog and digital channels.

-   Maintainer: Luciana Borges
-   Author: Luciana Borges/ lumoreno.borges@gmail.com
-   License: BSD
-   Source: git <https://github.com/lumoreno17/phidgets_interface>

## Requirements

Phidgets Library: <https://www.phidgets.com/docs/OS_-_Linux>

Phidgets Python Module:
<https://www.phidgets.com/docs/Language_-_Python>

## Install the package

Open the terminal on your catkin workspace and type

```
$ cd src
$ git clone https://github.com/lumoreno17/phidgets_interface
$ cd ..
$ catkin_make
```

## How to use

On src/Phidgets_Interface.py you can publish each sensor data to a
specific topic, specify the name of the sensor and the channel mode
(analog or digital). On the end of the script you will find the
following examples:

```
monitor_0 = PhidgetMonitor(0, 'SENSOR_NAME','ANALOG0','ANALOG')
monitor_0.setup()
monitor_1 = PhidgetMonitor(1, 'SENSOR_NAME2','ANALOG1','ANALOG')
monitor_1.setup()
monitor_2 = PhidgetMonitor(0, 'SENSOR_NAME3','DIGITAL0','DIGITAL')
monitor_2.setup()
``` monitor_0 is an object of the class
PhidgetMonitor that receives as parameters:

1\. Channel number

2\. Name of the sensor connect to the channel

3\. Name of the topic to publish the data

4\. Channel mode (ANALOG or DIGITAL)

Its necessary to call the method setup to work properly. You need to
copy and paste the constructor and the setup method to each channel you
desire to read the voltage.

Don\'t forget to save the changes!

## Run it

Inside your catkin workspace write the following command

```
rosrun phidgets_interface Phidgets_Interface.py
``` See the topics being used

```
rostopic list
``` Read the data

```
rostopic echo <NAME_OF_THE_TOPIC>
```
