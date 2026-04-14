## Supported Hardware

This driver should work with any SCIP 2.0-compliant laser range-finders.

## Parameter Ranges

The UTM-30LX laser can report corrupt data and even crash if settings
with an excessive data rate are requested. The following settings are
known to work:

\'\'\'Intensity mode off\'\'\':

-   \`cluster\`: 1
-   \`skip\`: 1
-   \`intensity\`: false
-   \`min_ang\`: -2.2689
-   \`max_ang\`: 2.2689

\'\'\'Intensity mode on\'\'\':

-   \`cluster\`: 1
-   \`skip\`: 1
-   \`intensity\`: true
-   \`min_ang\`: -1.047
-   \`max_ang\`: 1.047

### Allow Unsafe Settings Option

On the UTM-30LX, unless the \`allow_unsafe_settings\` option is
selected, the hokuyo_node will limit the angular range to values that
are known to work. The angular range limit depends on the firmware
version, and is proportional to the \`cluster\` parameter.

  -- -------------------------------------------------------------------- -- --------------------------------------------------- -- --------------------------------- --
     \<tablestyle=\"text-align: center;\"\>\'\'\'Firmware version\'\'\'      \'\'\'Maximum angular range / cluster (deg)\'\'\'      \'\'\'hokuyo_node version\'\'\'   
     1.16.01(16/Nov./2009)                                                   190                                                    \> 1.1.1                          
     1.16.02(19/Jan./2010)                                                   95                                                     \> 1.0.3                          
     Other                                                                   95                                                     \> 1.0.3                          
  -- -------------------------------------------------------------------- -- --------------------------------------------------- -- --------------------------------- --

## ROS API

```clearsilver
node.0 {
name=corobot_hokuyo
desc=`corobot_hokuyo` is a driver for SCIP 2.0 compliant Hokuyo laser range-finders. This driver was designed primarily for the Hokuyo UTM-30LX, also known as the Hokuyo Top-URG. The driver has been extended to support some SCIP1.0 compliant range-finders such as the URG-04LX. Hokuyo scans are taken in a counter-clockwise direction. Angles are measured counter clockwise with 0 pointing directly forward.
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
0.name= ~min_ang
0.default=-&pi;/2
0.type= double
0.desc= The angle of the first range measurement in radians (range is [-&pi;,&pi;], though most devices have a smaller feasible range).
1.name= ~max_ang
1.default=&pi;/2
1.type= double
1.desc= The angle of the last range measurement in radians (range is [-&pi;,&pi;], though most devices have a smaller feasible range).
2.name= ~intensity
2.default= `false`
2.type= bool
2.desc= Whether or not the hokuyo returns intensity values.
3.name= ~cluster
3.default=1
3.type= int
3.desc=The number of adjacent range measurements to cluster into a single reading; the shortest reading from the cluster is reported.
4.name= ~skip
4.default=0
4.type= int
4.desc= The number of scans to skip between each measured scan. This controls the update rate. For a UTM-30LX, the hokuyo will scan at 40Hz, so setting "skip" to 1 makes it publish at 20Hz.
5.name= ~port
5.default=`/dev/ttyACM0`
5.type= string
5.desc= The port where the hokuyo device can be found.
6.name= ~calibrate_time
6.default=`true`
6.type= bool
6.desc= Whether the node should calibrate the hokuyo's time offset on startup.  If true, the node will exchange of series of messages with the device in order to determine the time delay in the USB connection.  This calibration step is necessary to produce accurate time stamps on scans.
7.name= ~frame_id
7.default=`laser`
7.type= string
7.desc= The frame in which laser scans will be returned. This frame should be at the optical center of the laser, with the x-axis along the zero degree ray, and the y-axis along the 90 degree ray.
8.name= ~time_offset
8.default= 0.0
8.type= double
8.desc=An offet to add to the timestamp before publication of a scan Range: -0.25 to 0.25 (New in release 1.0.1)
9.name= ~allow_unsafe_settings
9.default= False
9.type= bool
9.desc=Turn this on if you wish to use the UTM-30LX with an unsafe angular range. Turning this option on may cause occasional crashes or bad data. This option is a tempory workaround that will hopefully be removed in an upcoming driver version. (New in release 1.0.3)
}
group.1 {
name=Read-only parameters
0.name= ~max_ang_limit
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
limitations of the laser\'s serial interface. For example:

-   if \`intensity\` is true and \`skip\` is 0, then the device will
    likely drop some scans;
-   if \`intensity\` is true and \`min_ang\` / \`max_ang\` are outside
    -70 / +70 degrees, then some problems have been observed.
