![attachment:hokuyo.jpg](doc/hokuyo.jpg)

Image credit:
[RobotShop](http://www.robotshop.com/ProductInfo.aspx?pc=RB-Hok-16)

## Supported Hardware

This driver should work with any SCIP 2.2 or earlier compliant laser
range-finders.

## API Stability

The ROS API of this driver should be considered stable.

## Parameter Ranges

The UTM-30LX laser can report corrupt data and even crash if settings
with an excessive data rate are requested. The following settings are
known to work:

**Intensity mode off**:

- `cluster`: 1
- `skip`: 1
- `intensity`: false
- `min_ang`: -2.2689
- `max_ang`: 2.2689

**Intensity mode on**:

- `cluster`: 1
- `skip`: 1
- `intensity`: true
- `min_ang`: -1.047
- `max_ang`: 1.047

### Allow Unsafe Settings Option

Allow Unsafe Settings Option is not available, please consider using the
legacy [hokuyo_node](https://index.ros.org/p/hokuyo_node) for UTM-30LX
with certain configurations. (Or provide a
[pull request to urg_node](https://github.com/ros-drivers/urg_node/issues/3)
to add support for unsafe_settings.)

## ROS API

<a id="NodeApi"></a>

### hokuyo_node

`hokuyo_node` is a driver for SCIP 2.2 and earlier compliant Hokuyo
laser range-finders.Hokuyo scans are taken in a counter-clockwise
direction. Angles are measured counter clockwise with 0 pointing
directly forward.

#### Published Topics

- `scan`
  ([sensor_msgs/msg/LaserScan](https://docs.ros.org/en/rolling/p/sensor_msgs/msg/LaserScan.html)):
  Traditional single return output. This is the most compatible topic
  and represents output from a laser scanner that is not providing
  multiple returns per beam. This topic is not present for multi-echo
  laserscanners in multi-echo modes.
- `echoes`
  ([sensor_msgs/msg/MultiEchoLaserScan](https://docs.ros.org/en/rolling/p/sensor_msgs/msg/MultiEchoLaserScan.html)):
  Output of a laser scanner capable of multiple returns per beam. This
  is the topic that is designed to give the most information to users of
  LaserScans. sensor_msgs/MultiEchoLaserScan is not required to be used
  by clients. This topic is not present for single echo laserscanners or
  multi-echo laserscanners in single echo mode.
- `first`
  ([sensor_msgs/msg/LaserScan](https://docs.ros.org/en/rolling/p/sensor_msgs/msg/LaserScan.html)):
  Output of the first return from a multi echo laser scanner. This topic
  represents the first return (distance closest to the laser scanner).
  It is typically published by a support library that converts
  sensor_msgs/MultiEchoLaserScans into sensor_msgs/LaserScans.
- `last`
  ([sensor_msgs/msg/LaserScan](https://docs.ros.org/en/rolling/p/sensor_msgs/msg/LaserScan.html)):
  Output of the last return from a multi echo laser scanner. This topic
  represents the last return (distance furthest from the laser scanner).
  It is typically published by a support library that converts
  sensor_msgs/MultiEchoLaserScans into sensor_msgs/LaserScans.
- `most_intense`
  ([sensor_msgs/msg/LaserScan](https://docs.ros.org/en/rolling/p/sensor_msgs/msg/LaserScan.html)):
  Output of the most intense return from a multi echo laser scanner.
  This topic represents the most intense return (brightest value). It is
  typically published by a support library that converts
  sensor_msgs/MultiEchoLaserScans into sensor_msgs/LaserScans.
- `diagnostics`
  ([diagnostic_msgs/msg/DiagnosticStatus](https://docs.ros.org/en/rolling/p/diagnostic_msgs/msg/DiagnosticStatus.html)):
  Diagnostic status information.

#### Parameters

- `~ip_address` (`string`, default: `""`): Location of the device on the
  network (only valid for ethernet devices). If this is left blank or is
  the empty string, the driver assumes the device is serial and will
  only attempt to connect using the 'serial_port' and 'serial_baud'
  parameters. Hokuyo factory IP addresses default to "192.168.0.10".
- `~ip_port` (`int`, default: `10940`): IP port number. (1 to 65535)
- `~serial_port` (`string`, default: `/dev/ttyACM0`): This represents
  the serial port device (COM4, /dev/tty/USB0).
- `~serial_baud` (`int`, default: `115200`): Data transfer rate for a
  serial device (9600, 115200, and so on)
- `~frame_id` (`string`, default: `laser`): The frame in which laser
  scans will be returned. This frame should be at the optical center of
  the laser, with the x-axis along the zero degree ray, and the y-axis
  along the 90 degree ray.
- `~calibrate_time` (`bool`, default: `false`): Whether the node should
  calibrate the device's time offset on startup. If true, the node will
  exchange of series of messages with the device in order to determine
  the time delay in the connection. This calibration step is necessary
  to produce accurate timestamps on scans.
- `~time_offset` (`double`, default: `0.0`): A manually calibrated
  offset (in seconds) to add to the timestamp before publication of a
  message.
- `~publish_intensity` (`bool`, default: `false`): If true, the laser
  will publish intensity. If false, the laser will not publish intensity
  to save bandwidth. Should be implemented in hardware if possible, but
  otherwise may be implemented in software.
- `~publish_multiecho` (`bool`, default: `false`): If true, a multiecho
  laserscanner will publish sensor_msgs/MultiEchoLaserScan. If false,
  the laser will publish sensor_msgs/LaserScan. (If supported by the
  hardware; otherwise, please use a support library to convert
  MultiEchoLaserScans to LaserScans.) This parameter is only valid for
  multiecho laserscanners.
- `~angle_min` (`double`, default: `-&pi`): Controls the angle of the
  first range measurement in radians. (If supported by the hardware; it
  is not recommended to implement this feature in software.)
- `~angle_max` (`double`, default: `&pi`): Controls the angle of the
  last range measurement in radians. (If supported by the hardware; it
  is not recommended to implement this feature in software.)
- `~cluster` (`int`, default: `1`): The number of adjacent range
  measurements to cluster into a single reading; the shortest reading
  from the cluster is reported. (If supported by the hardware; it is not
  recommended to implement this feature in software.)
- `~skip` (`int`, default: `0`): The number of input messages to skip
  between each output message. The device will publish 1 message for
  every N skipped messages. Example: if skip is set to '2', the device
  will publish 1 message and then 'drop' the following 2 message - a
  66.7% reduction in output rate. (If supported by the hardware; it is
  not recommended to implement this feature in software.)
- `~diagnostics_tolerance` (`double`, default: `0.05`): Fractional
  percent tolerance for published scan frequency to vary from expected.
  0.05 is 5%, so for 40Hz it means acceptable limits between 38Hz and
  42Hz.
- `~diagnostics_window_time` (`double`, default: `5.0`): Number of
  seconds in which to consider published data to determine publish
  frequency for diagnostics.

## Command-Line Tools

The `getID` program can be used to get information about a hokuyo
laser scanner. Each of them can be invoked in a human readable way:



```
$ rosrun urg_node getID /dev/ttyACM0
Device at /dev/ttyACM0 has ID H0807228
```

 or in a script friendly way:



```
$ rosrun urg_node getID /dev/ttyACM0 --
H0807228
```

 If they fail to connect to the device they will
retry for about ten seconds before giving up.

## Using udev to Give Hokuyos Consistent Device Names

The `getID` program can be used to get the hardware ID of a Hokuyo
device given its port. Combined with udev, this allows a consistent
device name to be given to each device, even if the order in which they
are plugged in varies. On the PR2 we use the following udev rule:



```
SUBSYSTEMS=="usb", KERNEL=="ttyACM[0-9]*", ACTION=="add", ATTRS{idVendor}=="15d1", ATTRS{idProduct}=="0000", MODE="666", PROGRAM="/opt/ros/hydro/lib/urg_node/getID /dev/%k q", SYMLINK+="sensors/hokuyo_%c", GROUP="dialout"
```

 This udev rule sets up a device name that is
based on the Hokuyo's hardware ID. The PR2 then has a symlink to that
name that gets changed if the Hokuyo is replaced:



```
$ ls -l /etc/ros/sensors/base_hokuyo
lrwxrwxrwx 1 root root 28 2010-01-12 15:53 /etc/ros/sensors/base_hokuyo -> /dev/sensors/hokuyo_H0902620
$ ls -l /dev/sensors/hokuyo_H0902620
lrwxrwxrwx 1 root root 10 2010-04-12 12:34 /dev/sensors/hokuyo_H0902620 -> ../ttyACM1
```
