![](attachment:Hokuyo.jpg)

Image credit:
[RobotShop](http://www.robotshop.com/hokuyo-utm-03lx-laser-scanning-rangefinder-1.html)

## For newer ROS distro than Indigo



```wiki
Looking for a newer driver?  [[urg_node|urg_node]] is fully [[http://ros.org/reps/rep-0138.html|REP-138]] compliant AND compatible with Ethernet/MultiEcho Hokuyos!  Hokuyo_node will remain maintained for current users and PR2s.

Check it out at:
[[urg_node|http://ros.org/wiki/urg_node]]
```



## Supported Hardware

This driver should work with any SCIP 2.0-compliant laser range-finders.

## API Stability

The ROS API of this driver should be considered stable.

## Parameter Ranges

The UTM-30LX laser can report corrupt data and even crash if settings
with an excessive data rate are requested. The following settings are
known to work:

**Intensity mode off**:

-   `cluster`: 1
-   `skip`: 1
-   `intensity`: false
-   `min_ang`: -2.2689
-   `max_ang`: 2.2689

**Intensity mode on**:

-   `cluster`: 1
-   `skip`: 1
-   `intensity`: true
-   `min_ang`: -1.047
-   `max_ang`: 1.047

### Allow Unsafe Settings Option

On the UTM-30LX, unless the `allow_unsafe_settings` option is
selected, the hokuyo_node will limit the angular range to values that
are known to work. The angular range limit depends on the firmware
version, and is proportional to the `cluster` parameter.

  -- ----------------------------------------------------------- -- ------------------------------------------- -- ------------------------- --
     <tablestyle="text-align:center;">**Firmware version**      **Maximum angular range / cluster (deg)**      **hokuyo_node version**   
     1.16.01(16/Nov./2009)                                          190                                            > 1.1.1                  
     1.16.02(19/Jan./2010)                                          95                                             > 1.0.3                  
     Other                                                          95                                             > 1.0.3                  
  -- ----------------------------------------------------------- -- ------------------------------------------- -- ------------------------- --

## ROS API



```clearsilver
node.0 {
name=hokuyo_node
desc=`hokuyo_node` is a driver for SCIP 2.0 compliant Hokuyo laser range-finders. This driver was designed primarily for the Hokuyo UTM-30LX, also known as the Hokuyo Top-URG. The driver has been extended to support some SCIP1.0 compliant range-finders such as the URG-04LX. Hokuyo scans are taken in a counter-clockwise direction. Angles are measured counter clockwise with 0 pointing directly forward.
pub{
0.name= scan
0.type= sensor_msgs/LaserScan
0.desc= Scan data from the laser.
1.name= diagnostics
1.type= diagnostic_msgs/DiagnosticStatus
1.desc= Diagnostic status information.
}
srv{
0.name= ~self_test
0.type= diagnostic_msgs/SelfTest
0.desc= Starts the Hokuyo self test, which runs a series of tests on the device.  The laser stops publishing scans during the test, which takes about a minute.  The result of the test is in the response returned by this service.  At the conclusion of the test, the laser is returned to its normal operating mode.
}
param {
group.0 {
name=Dynamically Reconfigurable Parameters
desc=See the [[dynamic_reconfigure]] package for details on dynamically reconfigurable parameters.
0.name= ~use_rep_117
0.default= true
0.type= bool
0.desc= Whether or not to use REP 117 output parameters.  See http://ros.org/wiki/rep_117/migration for more information.  This parameter was default to false in Fuerte; the default was true for Groovy.  This parameter was removed for the Hydromedusa release.
1.name= ~min_ang
1.default=-&pi;/2
1.type= double
1.desc= The angle of the first range measurement in radians (range is [-&pi;,&pi;], though most devices have a smaller feasible range).
2.name= ~max_ang
2.default=&pi;/2
2.type= double
2.desc= The angle of the last range measurement in radians (range is [-&pi;,&pi;], though most devices have a smaller feasible range).
3.name= ~intensity
3.default= `false`
3.type= bool
3.desc= Whether or not the hokuyo returns intensity values.
4.name= ~cluster
4.default=1
4.type= int
4.desc=The number of adjacent range measurements to cluster into a single reading; the shortest reading from the cluster is reported.
5.name= ~skip
5.default=0
5.type= int
5.desc= The number of scans to skip between each measured scan. This controls the update rate. For a UTM-30LX, the hokuyo will scan at 40Hz, so setting "skip" to 1 makes it publish at 20Hz.
6.name= ~port
6.default=`/dev/ttyACM0`
6.type= string
6.desc= The port where the hokuyo device can be found.
7.name= ~calibrate_time
7.default=`true`
7.type= bool
7.desc= Whether the node should calibrate the hokuyo's time offset on startup.  If true, the node will exchange a series of messages with the device in order to determine the time delay in the USB connection.  This calibration step is necessary to produce accurate time stamps on scans.
8.name= ~frame_id
8.default=`laser`
8.type= string
8.desc= The frame in which laser scans will be returned. This frame should be at the optical center of the laser, with the x-axis along the zero degree ray, and the y-axis along the 90 degree ray.
9.name= ~time_offset
9.default= 0.0
9.type= double
9.desc=An offet to add to the timestamp before publication of a scan Range: -0.25 to 0.25 (New in release 1.0.1)
10.name= ~allow_unsafe_settings
10.default= False
10.type= bool
10.desc=Turn this on if you wish to use the UTM-30LX with an unsafe angular range. Turning this option on may cause occasional crashes or bad data. This option is a tempory workaround that will hopefully be removed in an upcoming driver version. (New in release 1.0.3)
}
group.1 {
name=Read-only parameters
0.name= ~min_ang_limit
0.type= double
0.desc= Read only parameter indicating the smallest allowed value for `~min_ang` on the currently connected device.
1.name= ~max_ang_limit
1.type= double
1.desc= Read only parameter indicating the largest allowed value for `~max_ang` on the currently connected device.
2.name= ~min_range
2.type= double
2.desc= Read only parameter indicating the smallest distance that can be measured by the currently connected device.
3.name= ~max_range
3.type= double
3.desc= Read only parameter indicating the largest distance that can be measured by the currently connected device.
}
}
}
```



##### Parameter interactions

Some parameter settings can cause problems, usually due to speed
limitations of the laser's serial interface. For example:

-   if `intensity` is true and `skip` is 0, then the device will
    likely drop some scans;
-   if `intensity` is true and `min_ang` / `max_ang` are outside
    -70 / +70 degrees, then some problems have been observed.

## Command-Line Tools

The `getID` and `getFirmwareVersion` programs can be used to get
information about a hokuyo laser scanner. Each of them can be invoked in
a human readable way:



```
$ rosrun hokuyo_node getID /dev/ttyACM0
Device at /dev/ttyACM0 has ID H0807228
```

 or in a script friendly way:



```
$ rosrun hokuyo_node getID /dev/ttyACM0 --
H0807228
```

 If they fail to connect to the device they will
retry for about ten seconds before giving up.

## Using udev to Give Hokuyos Consistent Device Names

The `getID` program can be used to get the hardware ID of a Hokuyo
device given its port. Combined with udev, this allows a consistent
device name to be given to each device, even if the order in which they
are plugged in varies. The following udev rule should work universally
on any ROS system:



```
KERNEL=="ttyACM[0-9]*", ACTION=="add", ATTRS{idVendor}=="15d1", MODE="0666", GROUP="dialout", PROGRAM="/opt/ros/hydro/env.sh rosrun hokuyo_node getID %N q", SYMLINK+="sensors/hokuyo_%c"
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



## Communication Protocol Documentation

-   The SCIP 2.0 protocol is described in
    <attachment:URG-Series_SCIP2_Compatible_Communication_Specification_ENG.pdf>.

```{=html}
<!-- -->
```
-   The extension for intensity scans is documented in
    <attachment:UTM-30LX_Specification.pdf>.
