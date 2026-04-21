![\|width="333",height="200"](attachment:Logo-white-medium.jpg)

## Description

This package is used to access the SICK LMS400 laser range-finder. It
contains all necessary functionalities to communicate with the sensor
via ROS messages.

## Functionality

With this package you can connect to the SICK LMS 400 laserscanner. You
can parameterize the scanner with filters, resolution, scan frequency,
\... (see 4.3. Parameters). The parametrization can be specified via ROS
parameters in a yaml file.

The package creates a connection to the SICK LMS 400 with the wanted
parameters and shows/publish the data onto a ROS topic.

## Usage

You must build the package and parameterize the connection parameters
(in a yaml file or in the source code: lms400_node.cpp).

### Needed hardware

![SICK LMS 400 2D Laserscanner\|height="362",width="485"](https://www.sick.com/media/ZOOM/2/02/502/IM0008502.png)

A
[SICK lms400 2D Laserscanner](https://www.sick.com/de/en/detection-and-ranging-solutions/2d-laser-scanners/lms4xx/lms400-1000/p/p109851)
is required to use this package.

### Start system

```
rosrun asr_sick_lms_400 asr_sick_lms_400
```

## ROS Nodes

### Published Topics

_/laser_scan_
([sensor_msgs/LaserScan.msg](http://docs.ros.org/api/sensor_msgs/html/msg/LaserScan.html)*)*

Includes an array of all scanned points of one iteration, with its
distance information.

### Parameters

**Connection parameters: **

*hostname* (string)

-   Hostname of the PC (IP address).

*passwort* (string)

-   Passwort of the laserscanner.

*port* (int)

-   Number of the port, to which the laserscanner is connected.

**Filter parameters: **

*filter* (int)

-   Indicates which filter should be used.
-   0 (disabled)\
    1 (enable median filter)\
    2 (enable edge filter)\
    4 (enable range filter)\
    8 (enable mean filter)

*enable_eRIS* (int)

-   Enables extended RIS detectivity. If you want to measure objects
    with remission values < 10%, you can extend the so-called Remission
    Information System (RIS) on the LMS4000.

*mean_filter_parameter* (int)

-   Defines the number of means for the mean filter. Possible values: 2
    \... 200

*range_filter_parameter_min, range_filter_parameter_max* (int)

-   Define a specific range within which measured values are valid and
    are output. Possible values: \[+700.0 \... +3000.0 <bottom limit>
    \... +3000.0\]

**Lascerscan parameters: **

*angular_resolution* (double)

-   Angular resolution. Valid values are: 0.1 \... 1 (with 0.1 degree
    increments)

*scanning_frequency* (int)

-   Scanning frequency. Valid values are: -200 \... 500Hz (on the
    LMS400-0000) / 360 \... 500Hz (on the LMS400-1000)

*enable_laser* (bool)

-   Enables/Disables the laserscanner.

*min_angle, max_angle* (int)

-   Defines the minimum / maximum angle of the laser unit (where the
    scan should start / end). Valid values: 55 \... 125 degrees
