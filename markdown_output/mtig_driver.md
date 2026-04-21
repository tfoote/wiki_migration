## Installation

Download the MT Software Suite and install it on a Windows machine (you
may skip this step and use default sensor configuration), then download
the MT SDK for Linux and install it on a Linux machine (this should be
the machine that ROS is installed on). Here is the software website:
<http://www.xsens.com/en/mt-software-suite>.

Follow the instructions in the MT SDK for Linux to install the software
and make sure the examples run correctly with the sensor. You may need
to install the kernel available at <https://github.com/xsens/xsens_mt>.

Verify if the usb device was recognized by using the following command
(pay attention to the fact that the 0 in ttyUSB0 may be a different
number in your setup):

```
$ ls /dev/ttyUSB0
``` You may have to the current user to the dialout
group, using ```
$ sudo adduser this_user dialout
``` Now you can run the node using
roslaunch

```
$ roslaunch mtig_driver mtig_driver.launch
```

## Configuration

A default launch file can be found in the mtig_driver package directory.
The launchfile contains the following types of parameters.

-   Module Enabler: This type of parameters enables or disables the
    different sensor readings available in the device. This parameters
    have no use if the **override** parameter is false.
-   Module Frequency: This parameters set the frequency with which we
    want to read from each sensor. This can vary greatly between sensor
    type. See the Xsens Mti User Manual for more details. If we set this
    value to 0, it will adjust to the maximum possible frequency.
-   Override: If this parameter is true, then the device's current
    settings will be erased and the configuration set in the launchfile
    will be loaded to the device - Modules Enabled and Frequency. If
    this parameter is false, then the current settings will be used.
    This can be useful for configuring the device with the Windows tool
    provided by Xsens.
-   Frame_id: This parameter will set the frame on which the topics are
    published. Default value is "xsens"
-   Error: This parameters will be used in the covariance matrix of
    different sensors readings. We are not completely sure of the
    correctness in this. The values were obtained from the Xsens Mti
    User Manual.

Below is an example of an configuration file "all_zero.launch" where
all the modules are used with the maximum frequency available.

```
<launch>
        <arg name="frame" default="xsens" />
        <node pkg="mtig_driver" type="mtig_driver_node" name="mtig_driver">
                <!-- Error parameters /-->
                <param name="roll_error" value="0.2" />
                <param name="pitch_error" value="0.2" />
                <param name="yaw_error" value="1.0" />
                <param name="acc_noise" value="0.00015" />
                <param name="gyr_noise" value="0.01" />

                <!-- Frame Parameter /-->
                <param name="frame_id" value="$(arg frame)" />

                <!-- Override Mode /-->
                <param name="override" value="true" />

                <!-- Module Setup Parameters /-->
                <param name="orientation_enabled" value="true"/>
                <param name="orientation_frequency" value="0"/>
                <param name="gps_enabled" value="true"/>
                <param name="gps_frequency" value="0"/>
                <param name="temperature_enabled" value="true"/>
                <param name="temperature_frequency" value="0"/>
                <param name="acceleration_enabled" value="true"/>
                <param name="acceleration_frequency" value="0"/>
                <param name="pressure_enabled" value="true"/>
                <param name="pressure_frequency" value="0"/>
                <param name="magnetic_enabled" value="true"/>
                <param name="magnetic_frequency" value="0"/>
                <param name="altitude_enabled" value="true"/>
                <param name="altitude_frequency" value="0"/>
                <param name="velocity_enabled" value="true"/>
                <param name="velocity_frequency" value="0"/>
                <param name="gyroscope_enabled" value="true"/>
                <param name="gyroscope_frequency" value="0"/>
        </node>
</launch>
```

## Nodes

```clearsilver
name = mtig_driver
desc =  This is a ROS driver for MTi-G-700 GPS/INS. It provides GPS fix reading capabilities, as well as IMU and other sensors. To use the driver, a license number is required for the MT Software Suite (a.k.a. the Xsens API). This driver also enables configuration, i.e., turn different sensors in the device on and off, via ROS node. It is also possible to adjust the settings using MT Manager in Windows, and using the driver in read-only mode.
pub {
  0.name = /xsens/imu
  0.type = sensor_msgs/Imu
  0.desc = Uses data collected from the device's inertial measurement unit(IMU) angular velocity from gyroscope linear acceleration from accelerometer  orientation fusioned from the magnetometer.
  1.name = /xsens/gps
  1.type = sensor_msgs/NavSatFix
  1.desc = Uses data collected from the device's GPS. The covariance is given using DOP and Position Acuraccy. We assumed Position Accuracy is the std dev.
  2.name = /xsens/velocity
  2.type = geometry_msgs/TwistWithCovariance
  2.desc = Publishes angular and linear speed information in the ENU frame of reference. The data is collected from the device's gyroscopes and GPS.
  3.name = /xsens/temperature
  3.type = sensor_msgs/Temperature
  3.desc = Uses data collected from the device's thermometer.
  4.name = /xsens/pressure
  4.type = sensor_msgs/FluidPressure
  4.desc = Uses data collected from the device's barometer.
  5.name = /xsens/magnetic
  5.type = sensor_msgs/MagneticField
  5.desc = Uses data collected from the device's magnetometer
  6.name = /xsens/gps_extra
  6.type = mtig_driver/GpsInfo
  6.desc = This message contains important information from the Xsens' GPS that no other ROS Message accounted for.
}
```
