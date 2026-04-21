## Overview

ROSflight provides a simple, low-latency interface between a flight
controller running the ROSflight firmware and ROS. ROSflight can stream
both sensor data and motor commands at high speed. ROSflight is written
to work with a variety of airframes, including multirotor and fixed-wing
aircraft. The ROSflight package provided the interface for autopilots,
but does not include any control code. For examples of autopilots using
ROSflight, see [ROSPlane](https://github.com/byu-magicc/rosplane) or
[ROSCopter](https://github.com/byu-magicc/roscopter). For documentation
on the firmware, see <https://docs.rosflight.org>.

## Sample Usage

The following command will run the node that interfaces the autopilot
with ROS running on the onboard computer (this must be run on a computer
that is physically connected to the autopilot via USB or serial):



```
$ rosrun rosflight rosflight_io _port:=/dev/ttyUSB0
```



## Nodes



```clearsilver
node.0 {
name=rosflight_io
desc=Interfaces between ROS on the onboard computer and the ROSflight firmware on the autopilot. Streams sensor data to the onboard computer and control and configuration commands to the autopilot. Sensor stream topics are only advertised if they are being transmitted by the autopilot.
sub{
0.name= command
0.type= rosflight_msgs/Command
0.desc= Control setpoint to send to the autopilot. The interpretation of the setpoint values depends on the value of the `mode` field. Which setpoint values to listen to can be controlled by setting the bits of the `ignore` field.
1.name= aux_command
1.type= rosflight_msgs/AuxCommand
1.desc= Auxiliary command for the flight controller. This sets motors and/or servos that are not used by the mixer for flight. The `type_array` selects outputs and indicates whether they are motors or servos, and the `values` array sets the output value of the motor/servo.
2.name= external_attitude
2.type= geometry_msgs/Quaternion
2.desc= Corrected value for the internal estimator. Use this if you have an external sensor providing better estimates of the current attitude of the aircraft than the onboard estimator, such as a motion capture system. In between `external_attitude` messages, the estimator continues running to keep the estimate current. For fixed-wing aircraft, the internal estimator is only used for the `attitude` topic.
}
pub{
0.name= airspeed
0.type= rosflight_msgs/Airspeed
0.desc= Airspeed (meters/second) and differential pressure measurement (Pascals) from a differential pressure sensor, if attached.
1.name= attitude
1.type= rosflight_msgs/Attitude
1.desc= Attitude estimate from the autopilot, including orientation and angular velocity in the body frame with NED axes.
2.name= attitude/euler
2.type= geometry_msgs/Vector3Stamped
2.desc= Attitude estimate from the autopilot as Euler angles, in the NED frame
3.name= baro
3.type= rosflight_msgs/Barometer
3.desc= Barometer measurement, including pressure (Pascals), temperature (Kelvin), and computed altitude (meters). Computed altitude is relative to where the barometer was calibrated.
4.name= battery
4.type= rosflight_msgs/BatteryMonitor
4.desc= Current battery status, including voltage (Volts) and current (Amps), if a battery monitor is present
5.name= gnss
5.type= rosflight_msgs/GNSS
5.desc= Information from a GNSS receiver connected directly to the flight contoller. For more details, see the message definition. Not available in version 1.3 and earlier.
6.name= gnss_full
6.type= rosflight_msgs/GNSSFull
6.desc= The complete GNSS position, velocity, and time message from the receiver. This topic is intended for debugging, but may contain useful information. Some fields have strange units; see the message definition for details. Not available in version 1.3 and earlier.
7.name= imu/data
7.type= sensor_msgs/Imu
7.desc= Inertial measurement unit (IMU) data (3-axis accelerometer, 3-axis gyro) in the body frame with NED axes.
8.name= imu/temperature
8.type= sensor_msgs/Temperature
8.desc= Temperature from the IMU's internal sensor, in Degrees Celsius
9.name= magnetometer
9.type= sensor_msgs/MagneticField
9.desc= 3-axis magnetometer data in the NED frame, in Tesla
10.name= navsat_compat/fix
10.type= sensor_msgs/NavSatFix
10.desc= GNSS information from the attached GNSS receiver. This is intended to duplicate the API provided by the [[nmea_navsat_driver|nmea_navsat_driver package]]. Not currently functional.
11.name= navsat_compat/time_reference
11.type= sensor_msgs/TimeReference
11.desc= Provides the current GNSS time from the attached GNSS receiver. This is intended to duplicate the API provided by the [[nmea_navsat_driver|nmea_navsat_driver package]]. The header contains the ROS time when the time was valid, and the `time` field contains GNSS time. Not currently functional.
12.name= navsat_compat/vel
12.type= geometry_msgs/TwistStamped
12.desc= Velocity measurement from the attached GNSS receiver. Only the `linear` field is filled. This is intended to duplicate the API provided by the [[nmea_navsat_driver|nmea_navsat_driver package]]. Not currently functional.
13.name= output_raw
13.type= rosflight_msgs/OutputRaw
13.desc= Raw motor/servo outputs from the autopilot
14.name= rc_raw
14.type= rosflight_msgs/RCRaw
14.desc= Raw RC inputs to the autopilot from the RC receiver
15.name= rosflight_errors
15.type= rosflight_msgs/Error
15.desc= Major error messages from the firmware. This topic is only used for errors that crash the firmware, which are very unlikely in unmodified firmware. In event of a firmware crash, the firmware will restart and publish a message to this topic. There is some logic that attempts to prevent the aircraft from crashing (i.e. into the ground) in such a situation. See the [[https://docs.rosflight.org|firmware documentation]]
16.name= sonar
16.type= sensor_msgs/Range
16.desc= Distance measurement from an ultrasonic rangefinder, if attached
17.name= status
17.type= rosflight_msgs/Status
17.desc= Status of the autopilot, including armed state, failsafe state, and error states
18.name= unsaved_params
18.type= std_msgs/Bool
18.desc= Whether there are parameters that have been set on the autopilot but not saved to non-volatile memory
19.name= version
19.type= std_msgs/String
19.desc= String describing the firmware version running on the autopilot
20.name= named_value/int/<name>
20.type= std_msgs/Int32
20.desc= Raw named integer value sent from autopilot (used for debugging purposes)
21.name= named_value/float/<name>
21.type= std_msgs/Float32
21.desc= Raw named floating point value sent from autopilot (used for debugging purposes)
}
srv{
0.name= param_get
0.type= rosflight_msgs/ParamGet
0.desc= Gets the value of an autopilot parameter by name. There are many parameters; see the [[https://docs.rosflight.org/user-guide/parameter-configuration/|firmware documentation]].
1.name= param_set
1.type= rosflight_msgs/ParamSet
1.desc= Sets the value of an autopilot parameter by name. There are many parameters; see the [[https://docs.rosflight.org/user-guide/parameter-configuration/|firmware documentation]].
2.name= param_write
2.type= std_srvs/Trigger
2.desc= Writes all autopilot parameters to non-volatile memory
3.name= param_save_to_file
3.type= rosflight_msgs/ParamFile
3.desc= Saves all current autopilot parameters to specified file on onboard computer
4.name= param_load_from_file
4.type= rosflight_msgs/ParamFile
4.desc= Sets values of autopilot parameters to those saved in the specified file on the onboard computer
5.name= calibrate_imu
5.type= std_srvs/Trigger
5.desc= Starts an IMU calibration. IMU calibration will fail if the flight controller is not level or moves. Calibration errors are indicated through rosout, not from the service response.
6.name= calibrate_rc_trim
6.type= std_srvs/Trigger
6.desc= Sets the equilibrium feed-forward commands to those specified by the current RC trim setpoints. After calibrating, set RC trims back to zero. Does not work while the aircraft is armed.
7.name= calibrate_baro
7.type= std_srvs/Trigger
7.desc= Calibrates the barometer, setting the current altitude to 0. Calibration fails if the aircraft is moved during calibration.
8.name= calibrate_airspeed
8.type= std_srvs/Trigger
8.desc= Calibrates the airspeed sensor, setting the current airspeed to 0. To prevent errors, shield the airspeed sensor from wind during calibration. Calibration fails if the aircraft is moved during calibration.
9.name= reboot
9.type= std_srvs/Trigger
9.desc= Reboots the autopilot. Does nothing while armed.
10.name= reboot_to_bootloader
10.type= std_srvs/Trigger
10.desc= Reboots the autopilot to the bootloader for flashing firmware. Does nothing while armed. May not work on all flight controllers.
}
param{
0.name= ~port
0.type= string
0.default= /dev/ttyACM0
0.desc= Serial port to which the autopilot is connected
1.name= ~baud_rate
1.type= int
1.default= 921600
1.desc= Baud rate for the autopilot serial connection
2.name= ~frame_id
2.type= string
2.default= world
2.desc= The frame in which sensor data will be returned
3.name= ~udp
3.type= bool
3.default= false
3.desc= If true, use UDP instead of UART serial. Used for Gazebo software-in-the-loop simulator.
4.name= ~bind_host
4.type= string
4.default= localhost
4.desc= UDP bind host name
5.name= ~bind_port
5.type= int
5.default= 14520
5.desc= UDP bind port
6.name= ~remote_host
6.type= string
6.default= value of bind_host parameter
6.desc= UDP remote host name
7.name= ~remote_port
7.type= int
7.default= 14525
7.desc= UDP remote port
}
}
```


