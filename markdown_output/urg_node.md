![](attachment:hokuyo.jpg)

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
legacy [hokuyo_node](hokuyo_node) for UTM-30LX with certain
configurations. (Or provide a
[pull request to urg_node](https://github.com/ros-drivers/urg_node/issues/3)
to add support for unsafe_settings.)

## ROS API



```clearsilver
node.0 {
name=hokuyo_node
desc=`hokuyo_node` is a driver for SCIP 2.2 and earlier compliant Hokuyo laser range-finders.Hokuyo scans are taken in a counter-clockwise direction. Angles are measured counter clockwise with 0 pointing directly forward.
pub{
0.name= scan
0.type= sensor_msgs/LaserScan
0.desc= Traditional single return output. This is the most compatible topic and represents output from a laser scanner that is not providing multiple returns per beam. This topic is not present for multi-echo laserscanners in multi-echo modes.
1.name= echoes
1.type= sensor_msgs/MultiEchoLaserScan
1.desc= Output of a laser scanner capable of multiple returns per beam. This is the topic that is designed to give the most information to users of LaserScans. sensor_msgs/MultiEchoLaserScan is not required to be used by clients. This topic is not present for single echo laserscanners or multi-echo laserscanners in single echo mode.
2.name= first
2.type= sensor_msgs/LaserScan
2.desc= Output of the first return from a multi echo laser scanner. This topic represents the first return (distance closest to the laser scanner). It is typically published by a support library that converts sensor_msgs/MultiEchoLaserScans into sensor_msgs/LaserScans.
3.name= last
3.type= sensor_msgs/LaserScan
3.desc= Output of the last return from a multi echo laser scanner. This topic represents the last return (distance furthest from the laser scanner). It is typically published by a support library that converts sensor_msgs/MultiEchoLaserScans into sensor_msgs/LaserScans.
4.name= most_intense
4.type= sensor_msgs/LaserScan
4.desc= Output of the most intense return from a multi echo laser scanner. This topic represents the most intense return (brightest value). It is typically published by a support library that converts sensor_msgs/MultiEchoLaserScans into sensor_msgs/LaserScans.
5.name= diagnostics
5.type= diagnostic_msgs/DiagnosticStatus
5.desc= Diagnostic status information.
}
param {
0.name= ~ip_address
0.default= ""
0.type= string
0.desc= Location of the device on the network (only valid for ethernet devices).  If this is left blank or is the empty string, the driver assumes the device is serial and will only attempt to connect using the '~serial_port' and '~serial_baud' parameters.  Hokuyo factory IP addresses default to "192.168.0.10".
1.name= ~ip_port
1.default= 10940
1.type= int
1.desc= IP port number. (1 to 65535)
2.name= ~serial_port
2.default= /dev/ttyACM0
2.type= string
2.desc= This represents the serial port device (COM4, /dev/tty/USB0).
3.name= ~serial_baud
3.default= 115200
3.type= int
3.desc= Data transfer rate for a serial device (9600, 115200, and so on)
4.name= ~frame_id
4.default=laser
4.type= string
4.desc=The frame in which laser scans will be returned. This frame should be at the optical center of the laser, with the x-axis along the zero degree ray, and the y-axis along the 90 degree ray.
5.name= ~calibrate_time
5.default=false
5.type= bool
5.desc= Whether the node should calibrate the device's time offset on startup. If true, the node will exchange of series of messages with the device in order to determine the time delay in the connection. This calibration step is necessary to produce accurate timestamps on scans.
6.name= ~time_offset
6.default= 0.0
6.type= double
6.desc= A manually calibrated offset (in seconds) to add to the timestamp before publication of a message.
7.name= ~publish_intensity
7.default= false
7.type= bool
7.desc= If true, the laser will publish intensity. If false, the laser will not publish intensity to save bandwidth. Should be implemented in hardware if possible, but otherwise may be implemented in software.
8.name= ~publish_multiecho
8.default=false
8.type= bool
8.desc= If true, a multiecho laserscanner will publish sensor_msgs/MultiEchoLaserScan. If false, the laser will publish sensor_msgs/LaserScan. (If supported by the hardware; otherwise, please use a support library to convert MultiEchoLaserScans to LaserScans.) This parameter is only valid for multiecho laserscanners.
9.name= ~angle_min
9.default= -&pi
9.type= double
9.desc=Controls the angle of the first range measurement in radians. (If supported by the hardware; it is not recommended to implement this feature in software.)
10.name= ~angle_max
10.default= &pi
10.type= double
10.desc=Controls the angle of the last range measurement in radians. (If supported by the hardware; it is not recommended to implement this feature in software.)
11.name= ~cluster
11.default= 1
11.type= int
11.desc=The number of adjacent range measurements to cluster into a single reading; the shortest reading from the cluster is reported. (If supported by the hardware; it is not recommended to implement this feature in software.)
12.name= ~skip
12.default= 0
12.type= int
12.desc=The number of input messages to skip between each output message. The device will publish 1 message for every N skipped messages. Example: if skip is set to '2', the device will publish 1 message and then 'drop' the following 2 message - a 66.7% reduction in output rate. (If supported by the hardware; it is not recommended to implement this feature in software.)
13.name= ~diagnostics_tolerance
13.default= 0.05
13.type= double
13.desc = Fractional percent tolerance for published scan frequency to vary from expected.  0.05 is 5%, so for 40Hz it means acceptable limits between 38Hz and 42Hz.
14.name= ~diagnostics_window_time
14.default= 5.0
14.type= double
14.desc = Number of seconds in which to consider published data to determine publish frequency for diagnostics.
}
}
```



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


