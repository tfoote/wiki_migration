## Overview

This package provides communication driver for various autopilots with
MAVLink communication protocol. Additional it provides UDP MAVLink
bridge for ground control stations (e.g. QGroundControl).

Main node can be extended by plugins (see
[pluginlib](https://index.ros.org/p/pluginlib)). See also
[mavros_extras](https://index.ros.org/p/mavros_extras) package.

## Nodes



```clearsilver
node.0 {
 name = mavros_node
 desc = main communication node.
 pub {
  0.name= mavlink/from
  0.type= mavros_msgs/Mavlink
  0.desc= Mavlink stream from autopilot.
  1.name= diagnostics
  1.type= diagnostic_msgs/DiagnosticStatus
  1.desc= Diagnostic status information.
 }
 sub {
  0.name= mavlink/to
  0.type= mavros_msgs/Mavlink
  0.desc= Mavlink stream to autopilot.
 }
 param {
  7.name= ~system_id
  7.type= int
  7.desc= Node MAVLink System ID.
  7.default= 1
  8.name= ~component_id
  8.type= int
  8.desc= Node MAVLink Component ID.
  8.default= 240
  9.name= ~target_system_id
  9.type= int
  9.desc= FCU MAVLink System ID.
  9.default= 1
  10.name= ~target_component_id
  10.type= int
  10.desc= FCU MAVLink Component ID.
  10.default= 1
  11.name= ~startup_px4_usb_quirk
  11.type= bool
  11.desc= Define apply quirk for PX4 or not.
  11.default= false
  12.name= ~plugin_blacklist
  12.type= string[]
  12.desc= Alias blacklist (glob syntax, example: ['rc*'])
  12.default= []
  15.name= ~plugin_whitelist
  15.type= string[]
  15.desc= Alias whitelist (glob syntax, overrides blacklist)
  15.default= []
  13.name= ~fcu_url
  13.type= string
  13.desc= FCU connection URL.
  13.default= /dev/ttyACM0:57600
  16.name= ~fcu_protocol
  16.type= string
  16.desc= MAVLink protocol version. Supported: "v1.0", "v2.0" <<Version(0.18)>>
  16.default= v2.0
  14.name= ~gcs_url
  14.type= string
  14.desc= GCS bridge connection URL.
  14.default= udp://@
 }
}
node.1 {
 name = gcs_bridge
 desc = Additional proxy. Old name `ros_udp`.
 pub {
  0.name= mavlink/to
  0.type= mavros_msgs/Mavlink
  0.desc= Mavlink stream to autopilot.
 }
 sub {
  0.name= mavlink/from
  0.type= mavros_msgs/Mavlink
  0.desc= Mavlink stream from autopilot.
 }
 param {
  14.name= ~gcs_url
  14.type= string
  14.desc= Connection URL.
  14.default= udp://@
 }
}
node.2 {
 name = event_launcher
 desc = Listens to arming status, triggers and run programs on event. [[https://github.com/mavlink/mavros/blob/master/mavros/launch/event_launcher.yaml|Example config.]]
 sub {
  0.name= mavros/state
  0.type= mavros_msgs/State
  0.desc= Source of arming events.
 }
 srv {
  0.name= <trigger_event>
  0.type= std_srvs/Trigger
  0.desc= Optional event triggers. You may create several services using configuration.
 }
 param {
  0.name= ~<event_name>/service
  0.type= string
  0.desc= Create event (with name <event_name>) triggered by service (param value).
  1.name= ~<event_handler>/event
  1.type= string[]
  1.desc= List of events triggered that handler.
  2.name= ~<event_handler>/action
  2.type= string[]
  2.desc= List of actions to do on corresponding event. Supported actions: '''run''', '''stop'''.
  3.name= ~<event_handler>/shell
  3.type= string
  3.desc= Command to run/stop on event.
  4.name= ~<event_handler>/logfile
  4.type= string
  4.desc= File to save stdout and stderr output of command. Optional.
  4.default= ""
 }
}
```



## Usage

Example launch files are in the mavros/launch directory. If the
autopilot is on the PX4 native stack use the following to launch an
example configuration:



```
roslaunch mavros px4.launch
```



If the autopilot is on the ArduPilot/APM stack firmware use the
following:



```
roslaunch mavros apm.launch
```



Example configurations for the various mavros plugins can also be found
in similarly named yaml files. For more details on the choices between
APM and PX4 stacks checkout the
[pixhawk wiki](https://pixhawk.org/choice).

Hardware notes:

- APM2.5/2.6 always APM stack
- Pixhawk from manufacturer usually comes with APM stack
- Pixhawk may be flashed by PX4 firmware using QGC or by upload make
  target.

If you unsure what firmware your FCU runs start apm.launch and see
[diagnostics](https://index.ros.org/p/diagnostics). Starting from 0.11
mavros knows string representation for autopilot mavlink enum. For older
you shall manually find autopilot type value in mavlink documentation.

## Connection URL

Connection defined by URL, you can use any supported type for FCU and
GCS.

Supported schemas:

- Serial: `/path/to/serial/device\[:baudrate\]`
- Serial:
  `serial:*/path/to/serial/device\[:baudrate\]\[/?ids=sysid,compid\]`
  \* Serial with hardware flow control:
  `serial-hwfc:*/path/to/serial/device\[:baudrate\]\[?ids=sysid,compid\]`
- UDP:
  `udp:*\[bind_host\]\[:port\]@\[remote_host\]\[:port\]\[/?ids=sysid,compid\]`
  \* UDP Broadcast:
  `udp-b:*\[bind_host\]\[:port\]@\[:port\]\[/?ids=sysid,compid\]`
- TCP client: `tcp:*\[server_host\]\[:port\]\[/?ids=sysid,compid\]` \*
  TCP server: `tcp-l:*\[bind_host\]\[:port\]\[/?ids=sysid,compid\]`

Notes:

- ids from URL overrides ids given by parameters `system_id` and
  `component_id`.
- `baudrate` default value is 57600
- `bind_host` default value is "0.0.0.0" (IPv4 ANY)
- `remote_host` by default unknown. mavros will awaiting data at
  bind_host:port
- `server_host` default value is "localhost"
- `port` default values: 14555 for UDP bind, 14550 for UDP remote,
  5760 for TCP
- UDP broadcast used on discovery stage, later it switch to GCS address
- Currently supports only IPv4.

## Utility commands

All utilities provides `<util> \--help` and `<util> <command>
\--help` information.

### mavcmd



```
usage: mavcmd [-h] [-n MAVROS_NS] [-v] [--wait]
              {long,int,sethome,takeoff,land,takeoffcur,landcur,trigger_control}
              ...

Commad line tool for sending commands to MAVLink device.

positional arguments:
  {long,int,sethome,takeoff,land,takeoffcur,landcur,trigger_control}
    long                Send any command (COMMAND_LONG)
    int                 Send any command (COMMAND_INT)
    sethome             Request change home position
    takeoff             Request takeoff
    land                Request land
    takeoffcur          Request takeoff from current GPS coordinates
    landcur             Request land on current GPS coordinates
    trigger_control     Control onboard camera trigerring system (PX4)

optional arguments:
  -h, --help            show this help message and exit
  -n MAVROS_NS, --mavros-ns MAVROS_NS
                        ROS node namespace
  -v, --verbose         verbose output
  --wait                Wait for establishing FCU connection
```



### mavftp

**PX4** only. 

```
usage: mavftp [-h] [-n MAVROS_NS] [-v]
              {cd,list,cat,remove,mkdir,rmdir,download,upload,verify,reset}
              ...

File manipulation tool for MAVLink-FTP.

positional arguments:
  {cd,list,cat,remove,mkdir,rmdir,download,upload,verify,reset}
    cd                  change directory
    list                list files and dirs
    cat                 cat file
    remove              remove file
    mkdir               create direcotory
    rmdir               remove directory
    download            download file
    upload              upload file
    verify              verify files
    reset               reset

optional arguments:
  -h, --help            show this help message and exit
  -n MAVROS_NS, --mavros-ns MAVROS_NS
                        ROS node namespace
  -v, --verbose         verbose output
```



### mavparam



```
usage: mavparam [-h] [-n MAVROS_NS] [-v] {load,dump,get,set} ...

Commad line tool for getting, setting, parameters from MAVLink device.

positional arguments:
  {load,dump,get,set}
    load                load parameters from file
    dump                dump parameters to file
    get                 get parameter
    set                 set parameter

optional arguments:
  -h, --help            show this help message and exit
  -n MAVROS_NS, --mavros-ns MAVROS_NS
                        ROS node namespace
  -v, --verbose         verbose output
```



### mavsafety



```
usage: mavsafety [-h] [-n MAVROS_NS] [-v] {arm,disarm,safetyarea} ...

Commad line tool for manipulating safty on MAVLink device.

positional arguments:
  {arm,disarm,safetyarea}
    arm                 Arm motors
    disarm              Disarm motors
    safetyarea          Send safety area

optional arguments:
  -h, --help            show this help message and exit
  -n MAVROS_NS, --mavros-ns MAVROS_NS
                        ROS node namespace
  -v, --verbose         verbose output
```



### mavsetp

Testing utility for setpoint plugins.



```
usage: mavsetp [-h] [-n MAVROS_NS] [-V] {local} ...

Commad line tool for control the device by setpoints.

positional arguments:
  {local}
    local               Send local setpoint

optional arguments:
  -h, --help            show this help message and exit
  -n MAVROS_NS, --mavros-ns MAVROS_NS
                        ROS node namespace
  -V, --verbose         verbose output
```



### mavsys



```
usage: mavsys [-h] [-n MAVROS_NS] [-v] [--wait] {mode,rate} ...

Change mode and rate on MAVLink device.

positional arguments:
  {mode,rate}
    mode                Set mode
    rate                Set stream rate

optional arguments:
  -h, --help            show this help message and exit
  -n MAVROS_NS, --mavros-ns MAVROS_NS
                        ROS node namespace
  -v, --verbose         verbose output
  --wait                Wait for establishing FCU connection
```



Supported custom modes listed at
[CustomModes](#custommodes).

### mavwp



```
usage: mavwp [-h] [-n MAVROS_NS] [-v]
             {show,load,pull,dump,clear,setcur,goto} ...

Commad line tool for manipulating mission on MAVLink device.

positional arguments:
  {show,load,pull,dump,clear,setcur,goto}
    show                Show waypoints
    load                load waypoints from file
    pull                pull waypoints from FCU
    dump                dump waypoints to file
    clear               clear waypoints on device
    setcur              set current waypoints on device
    goto                send goto waypoint (APM only)

optional arguments:
  -h, --help            show this help message and exit
  -n MAVROS_NS, --mavros-ns MAVROS_NS
                        ROS node namespace
  -v, --verbose         verbose output
```



## Plugins

Standard set of communication plugins loaded by
mavros_node.

Note: this list for 0.18.0 version.
Older versions: [0.6.0](#plugins_06),
[0.7.0](#plugins_07),
[0.8.0](#plugins_08),
[0.10.0](#plugins_010),
[0.11.0](#plugins_011),
[0.12.0 --- 0.15.0](#plugins_012-015),
[0.16.0 --- 0.17.0](#plugins_016-017).



```clearsilver

node.14 {
 name= 3dr_radio
 desc= Publish 3DR Radio status to diagnostics and topic.
 pub {
  0.name= ~radio_status
  0.type= mavros_msgs/RadioStatus
  0.desc= Status received from modem, same as RADIO_STATUS message.
 }
}

node.20 {
 name= actuator_control
 desc= Sends acruator commands to FCU.
 sub {
  0.name= ~actuator_control
  0.type= mavros_msgs/ActuatorControl
  0.desc= actuator command
 }
}

node.23 {
 name= altitude
 desc= Publish altitude information.
 pub {
  0.name= ~altitude
  0.type= mavros_msgs/Altitude
  0.desc= Direct copy of altitude data provided by Mavlink.
 }
 param {
  0.name= ~frame_id
  0.type= string
  0.desc= frame for altitude messages
  0.default= "map"
 }
}

node.6 {
 name= command
 desc= Send COMMAND_LONG to FCU.
 srv {
  0.name= ~cmd/command
  0.type= mavros_msgs/CommandLong
  0.desc= Send any COMMAND_LONG to FCU.
  4.name= ~cmd/command_int
  4.type= mavros_msgs/CommandInt
  4.desc= Send any COMMAND_INT to FCU.
  1.name= ~cmd/arming
  1.type= mavros_msgs/CommandBool
  1.desc= Change Arming status.
  3.name= ~cmd/set_home
  3.type= mavros_msgs/CommandHome
  3.desc= Change HOME location.
  6.name= ~cmd/takeoff
  6.type= mavros_msgs/CommandTOL
  6.desc= Send takeoff command.
  7.name= ~cmd/land
  7.type= mavros_msgs/CommandTOL
  7.desc= Send land command.
  8.name= ~cmd/trigger_control
  8.type= mavros_msgs/CommandTriggerControl
  8.desc= Send camera trigger control command.
 }
 param {
  0.name= ~cmd/use_comp_id_system_control
  0.type= bool
  0.desc= Use `SYSTEM_CONTROL` component id instead of mavros target component.
  0.default= false
 }
}

node.18 {
 name= ftp
 desc= Support plugin for MAVLink-FTP ('''PX4''').
 srv {
  0.name= ~ftp/open
  0.type= mavros_msgs/FileOpen
  0.desc= Open file (acquire session).
  1.name= ~ftp/close
  1.type= mavros_msgs/FileClose
  1.desc= Close file (release session).
  2.name= ~ftp/read
  2.type= mavros_msgs/FileRead
  2.desc= Read from opened file.
  3.name= ~ftp/write
  3.type= mavros_msgs/FileWrite
  3.desc= Write to opened file.
  4.name= ~ftp/list
  4.type= mavros_msgs/FileList
  4.desc= List directory.
  5.name= ~ftp/truncate
  5.type= mavros_msgs/FileTruncate
  5.desc= Truncate file.
  6.name= ~ftp/remove
  6.type= mavros_msgs/FileRemove
  6.desc= Unlink file.
  7.name= ~ftp/rename
  7.type= mavros_msgs/FileRename
  7.desc= Rename file/directory.
  8.name= ~ftp/mkdir
  8.type= mavros_msgs/FileMakeDir
  8.desc= Create directory.
  9.name= ~ftp/rmdir
  9.type= mavros_msgs/FileRemoveDir
  9.desc= Remove directory.
  10.name= ~ftp/checksum
  10.type= mavros_msgs/FileChecksum
  10.desc= Request to calculate CRC32 of file on FCU.
  11.name= ~ftp/reset
  11.type= std_srvs/Empty
  11.desc= Reset FCU server (dangerous).
 }
}

node.17 {
 name= global_position
 desc= Publish global position information fused by FCU and raw GPS data.
 pub {
  0.name= ~global_position/global
  0.type= sensor_msgs/NavSatFix
  0.desc= GPS Fix. '''IMPORTANT:''' Altitude is specified as ellipsoid height and care must be taken to avoid a common pitfall. [[https://wiki.ros.org/mavros#mavros.2FPlugins.Avoiding_Pitfalls_Related_to_Ellipsoid_Height_and_Height_Above_Mean_Sea_Level|See this section for more]].
  1.name= ~global_position/local
  1.type= geometry_msgs/PoseWithCovarianceStamped
  1.desc= UTM coords.
  2.name= ~global_position/gp_vel
  2.type= geometry_msgs/TwistStamped
  2.desc= Velocity fused by FCU.
  3.name= ~global_position/rel_alt
  3.type= std_msgs/Float64
  3.desc= Relative altitude.
  4.name= ~global_position/compass_hdg
  4.type= std_msgs/Float64
  4.desc= Compass heading in degrees.
  5.name= ~global_position/raw/fix
  5.type= sensor_msgs/NavSatFix
  5.desc= GPS position fix reported by the device.
  6.name= ~global_position/raw/gps_vel
  6.type= geometry_msgs/TwistStamped
  6.desc= Velocity output from the GPS device.
 }
 param {
  1.name= ~global_position/frame_id
  1.type= string
  1.desc= frame_id for messages.
  1.default= fcu
  0.name= ~global_position/tf/send
  0.type= bool
  0.desc= Send or not local UTM coords via TF?
  0.default= true
  3.name= ~global_position/tf/frame_id
  3.type= string
  3.desc= frame_id for TF.
  3.default= local_origin
  2.name= ~global_position/tf/child_frame_id
  2.type= string
  2.desc= Child frame_id for TF.
  2.default= fcu_utm
 }
}

node.23 {
 name= hil_controls
 desc= Publish HIL_CONTROLS <<Version(0.18)>>
 pub {
  0.name= ~hil_controls/hil_controls
  0.type= mavros_msgs/HilControls
  0.desc= HIL data
 }
}

node.1 {
 name= imu_pub
 desc= Publish IMU state
 pub {
  0.name= ~imu/data
  0.type= sensor_msgs/Imu
  0.desc= Imu data, orientation computed by FCU
  1.name= ~imu/data_raw
  1.type= sensor_msgs/Imu
  1.desc= Raw IMU data without orientation
  2.name= ~imu/mag
  2.type= sensor_msgs/MagneticField
  2.desc= FCU compass data
  3.name= ~imu/temperature
  3.type= sensor_msgs/Temperature
  3.desc= Temperature reported by FCU (usually from barometer)
  4.name= ~imu/atm_pressure
  4.type= sensor_msgs/FluidPressure
  4.desc= Air pressure.
 }
 param {
  0.name= ~imu/frame_id
  0.type= string
  0.desc= Frame ID for this plugin.
  0.default= fcu
  1.name= ~imu/linear_acceleration_stdev
  1.type= double
  1.desc= Gyro's standard deviation
  1.default= 0.0003
  2.name= ~imu/angular_velocity_stdev
  2.type= double
  2.desc= Accel's standard deviation
  2.default= !dec 0.02
  3.name= ~imu/orientation_stdev
  3.type= double
  3.desc= Standard deviation for IMU.orientation
  3.default= 1.0
  4.name= ~imu/magnetic_stdev
  4.type= double
  4.desc= Standard deviation for magnetic field message (undefined if: 0.0)
  4.default= 0.0
 }
}

node.7 {
 name= local_position
 desc= Publish LOCAL_POSITION_NED in [[tf|TF]] and PoseStamped topic.
 pub {
  0.name= ~local_position/pose
  0.type= geometry_msgs/PoseStamped
  0.desc= Local position from FCU.
  1.name= ~local_position/velocity
  1.type= geometry_msgs/TwistStamped
  1.desc= Velocity data from FCU.
 }
 param {
  1.name= ~local_position/frame_id
  1.type= string
  1.desc= frame_id for message.
  1.default= fcu
  0.name= ~local_position/tf/send
  0.type= bool
  0.desc= TF send switch.
  0.default= true
  3.name= ~local_position/tf/frame_id
  3.type= string
  3.desc= Origin frame_id for TF.
  3.default= local_origin
  2.name= ~local_position/tf/child_frame_id
  2.type= string
  2.desc= Child frame_id for TF.
  2.default= fcu
 }
}

node.21 {
 name= manual_control
 desc= Publish MANUAL_CONTROL message (user input).
 pub {
  0.name= ~manual_control/control
  0.type= mavros_msgs/ManualControl
  0.desc= RC Rx, interpreted and normalized.
  }
  sub{
  0.name= ~manual_control/send
  0.type= mavros_msgs/ManualControl
  0.desc= RC Rx, interpreted and normalized.
 }
}



node.3 {
 name= param
 desc= Allows to access to FCU parameters and map it to ROS parameters in `~param/`.
 srv {
  0.name= ~param/pull
  0.type= mavros_msgs/ParamPull
  0.desc= Request parameter from device (or internal cache).
  1.name= ~param/push
  1.type= mavros_msgs/ParamPush
  1.desc= Request send parameters from ROS to FCU.
  2.name= ~param/get
  2.type= mavros_msgs/ParamGet
  2.desc= Return FCU parameter value.
  3.name= ~param/set
  3.type= mavros_msgs/ParamSet
  3.desc= Set parameter on FCU immidiatly.
 }
}

node.5 {
 name= rc_io
 desc= Publish RC receiver inputs.
 pub {
  0.name= ~rc/in
  0.type= mavros_msgs/RCIn
  0.desc= Publish RC inputs (in raw milliseconds)
  1.name= ~rc/out
  1.type= mavros_msgs/RCOut
  1.desc= Publish FCU servo outputs
 }
 sub {
  2.name= ~rc/override
  2.type= mavros_msgs/OverrideRCIn
  2.desc= Send RC override message to FCU. '''APM''' and '''PX4''' only. APM requires setup FCU param `SYSID_MYGCS` to match mavros system id. '''Not recommended''' to use in automatic control because lack of safety mechanisms. Use one of setpoint plugins and OFFBOARD mode.
 }
}

node.13 {
 name= safety_area
 desc= Sends safety allowed area to FCU. Initial area can be loaded from parameters.
 sub {
  0.name= ~safety_area/set
  0.type= geometry_msgs/PolygonStamped
  0.desc= Volumetric area described by two corners.
 }
 param {
  0.name= ~safety_area/p1/x
  0.type= double
  0.desc= Corner 1 X.
  1.name= ~safety_area/p1/y
  1.type= double
  1.desc= Corner 1 Y.
  2.name= ~safety_area/p1/z
  2.type= double
  2.desc= Corner 1 Z.
  3.name= ~safety_area/p2/x
  3.type= double
  3.desc= Corner 2 X.
  4.name= ~safety_area/p2/y
  4.type= double
  4.desc= Corner 2 Y.
  5.name= ~safety_area/p2/z
  5.type= double
  5.desc= Corner 2 Z.
 }
}

node.9 {
 name= setpoint_accel
 desc= Send acceleration setpoint.
 sub {
  0.name= ~setpoint_accel/accel
  0.type= geometry_msgs/Vector3Stamped
  0.desc= Acceleration or force setpoint vector.
 }
 param {
  0.name= ~setpoint_accel/send_force
  0.type= bool
  0.desc= Send force setpoint.
 }
}

node.10 {
 name= setpoint_attitude
 desc= Send attitude setpoint using SET_ATTITUDE_TARGET.
 sub {
  0.name= ~setpoint_attitude/cmd_vel
  0.type= geometry_msgs/TwistStamped
  0.desc= Send angular velocity.
  1.name= ~setpoint_attitude/attitude
  1.type= geometry_msgs/PoseStamped
  1.desc= Send attitude setpoint.
  2.name= ~setpoint_attitude/thrust
  2.type= mavros_msgs/Thrust
  2.desc= Send throttle value(0~1).
 }
 param {
  6.name= ~setpoint_attitude/reverse_throttle
  6.type= bool
  6.desc= Allow to send -1.0 throttle or not.
  6.default= false
  7.name= ~setpoint_attitude/use_quaternion
  7.type= bool
  7.desc= Enable ~setpoint_attitude/target_attitude PoseStamped topic subscriber and disable ~setpoint_attitude/cmd_vel Twist topic.
  7.default= false
  0.name= ~setpoint_attitude/tf/listen
  0.type= bool
  0.desc= TF listen switch. Disable topics if enabled.
  0.default= false
  3.name= ~setpoint_attutude/tf/frame_id
  3.type= string
  3.desc= Origin frame_id for TF.
  3.default= local_origin
  4.name= ~setpoint_attitude/tf/child_frame_id
  4.type= string
  4.desc= Child frame_id for TF.
  4.default= attitude
  5.name= ~setpoint_attitude/tf/rate_limit
  5.type= double
  5.desc= Rate limit for TF listener [Hz].
  5.default= 10.0
 }
}

node.11 {
 name= setpoint_position
 desc= Sends position setpoint using SET_POSITION_TARGET_GLOBAL_INT or SET_POSITION_TARGET_LOCAL_NED.
 sub {
  0.name= ~setpoint_position/global
  0.type= geographic_msgs/GeoPoseStamped
  0.desc= Global frame setpoint position. Sends an LLA to the flight controller. Only YAW axis extracted from orientation field. '''IMPORTANT:''' Altitude is interpreted as AMSL and care must be taken to avoid a common pitfall. [[https://wiki.ros.org/mavros#mavros.2FPlugins.Avoiding_Pitfalls_Related_to_Ellipsoid_Height_and_Height_Above_Mean_Sea_Level|See this section for more]].
  1.name= ~setpoint_position/local
  1.type= geometry_msgs/PoseStamped
  1.desc= Local frame setpoint position. Only YAW axis extracted from orientation field.
  2.name= ~setpoint_position/global_to_local
  2.type= geographic_msgs/GeoPoseStamped
  2.desc= The old implementation of `~setpoint_position/global`. Converts LLA to local ENU. This was done as a workaround before the flight controller could accept LLA setpoints directly. Consider using `~setpoint_position/global` instead. [[https://github.com/mavlink/mavros/pull/1306|See the details here]]. Only YAW axis extracted from orientation field.
 }
 param {
  0.name= ~setpoint_position/tf/listen
  0.type= bool
  0.desc= TF listen switch. Disable topic if enabled.
  0.default= false
  1.name= ~setpoint_position/tf/frame_id
  1.type= string
  1.desc= Origin frame_id for TF.
  1.default= local_origin
  2.name= ~setpoint_position/tf/child_frame_id
  2.type= string
  2.desc= Child frame_id for TF.
  2.default= setpoint
  3.name= ~setpoint_position/tf/rate_limit
  3.type= double
  3.desc= Rate limit for TF listener [Hz].
  3.default= 50.0
 }
}

node.22 {
 name= setpoint_raw
 desc= Send RAW setpoint messages to FCU and provide loopback topics (PX4).
 pub {
  0.name= ~setpoint_raw/target_local
  0.type= mavros_msgs/PositionTarget
  0.desc= Local target loopback.
  1.name= ~setpoint_raw/target_global
  1.type= mavros_msgs/GlobalPositionTarget
  1.desc= Global target loopback.
  2.name= ~setpoint_raw/target_attitude
  2.type= mavros_msgs/AttitudeTarget
  2.desc= Attitude target loopback.
 }
 sub {
  0.name= ~setpoint_raw/local
  0.type= mavros_msgs/PositionTarget
  0.desc= Local position, velocity and acceleration setpoint.
  1.name= ~setpoint_raw/global
  1.type= mavros_msgs/GlobalPositionTarget
  1.desc= Global position, velocity and acceleration setpoint.
  2.name= ~setpoint_raw/attitude
  2.type= mavros_msgs/AttitudeTarget
  2.desc= Attitude, angular rate and thrust setpoint.
 }
}

node.12 {
 name= setpoint_velocity
 desc= Send velocity setpoint to FCU.
 sub {
  0.name= ~setpoint_velocity/cmd_vel
  0.type= geometry_msgs/TwistStamped
  0.desc= Velocity setpoint.
  0.name= ~setpoint_velocity/cmd_vel_unstamped
  0.type= geometry_msgs/Twist
  0.desc= Velocity setpoint.
 }
}

node.0 {
 name= sys_status
 desc= System status plugin. Handles FCU detection. '''REQUIRED''' never blacklist it!.
 pub {
  0.name= ~state
  0.type= mavros_msgs/State
  0.desc= FCU state
  1.name= ~battery
  1.type= mavros_msgs/BatteryStatus
  1.desc= FCU battery status report. '''DEPRECATED'''
  3.name= ~battery
  3.type= sensor_msgs/BatteryState
  3.desc= FCU battery status report. <<Version(Kinetic)>>
  2.name= ~extended_state
  2.type= mavros_msgs/ExtendedState
  2.desc= Landing detector and VTOL state.
 }
 srv {
  0.name= ~set_stream_rate
  0.type= mavros_msgs/StreamRate
  0.desc= Send stream rate request to FCU.
  1.name= ~set_mode
  1.type= mavros_msgs/SetMode
  1.desc= Set FCU operation mode. See custom mode identifiers at [[mavros/CustomModes|modes page]].
 }
 param {
  0.name= ~conn/timeout
  0.type= double
  0.desc= Connection time out in seconds.
  0.default= 30.0
  1.name= ~conn/heartbeat_rate
  1.type= double
  1.desc= Send HEARTBEAT message rate [Hz] (or disabled if 0.0)
  1.default= 0.0
  2.name= ~sys/min_voltage
  2.type= double
  2.desc= Minimal battery voltage for diagnostics.
  2.default= 6.0
  3.name= ~sys/disable_diag
  3.type= bool
  3.desc= Disable all diag except HEARTBEAT message.
  3.default= false
 }
}

node.19 {
 name= sys_time
 desc= System time plugin. Does time syncronization on '''PX4'''.
 pub {
  1.name= ~time_reference
  1.type= sensor_msgs/TimeReference
  1.desc= Time reference computed from SYSTEM_TIME.
 }
 param {
  0.name= ~conn/system_time_rate
  0.type= double
  0.desc= Send `SYSTEM_TIME` to device rate [Hz] (disabled if 0.0).
  0.default= 0.0
  1.name= ~conn/timesync_rate
  1.type= double
  1.desc= TIMESYNC rate. '''PX4''' only.
  1.default= 0.0
  2.name= ~time/time_ref_source
  2.type= string
  2.desc= Ref source for time_reference message.
  2.default= "fcu"
  3.name= ~time/timesync_avg_alpha
  3.type= double
  3.desc= Alpha for exponential moving average.
  3.default= 0.6
 }
}

node.16 {
 name= vfr_hud
 desc= Publish VFR_HUD and WIND messages.
 pub {
  0.name= ~vfr_hud
  0.type= mavros_msgs/VFR_HUD
  0.desc= Data for HUD.
  1.name= ~wind_estimation
  1.type= geometry_msgs/TwistStamped
  1.desc= Wind estimation from FCU ('''APM''').
 }
}

node.4 {
 name= waypoint
 desc= Allows to access to FCU mission (waypoints).
 pub {
  0.name= ~mission/reached
  0.type= mavros_msgs/WaypointReached
  0.desc= Publishes on reaching a waypoint from MISSION_ITEM_REACHED message.
  1.name= ~mission/waypoints
  1.type= mavros_msgs/WaypointList
  1.desc= Current waypoint table. Updates on changes.
 }
 srv {
  0.name= ~mission/pull
  0.type= mavros_msgs/WaypointPull
  0.desc= Request update waypoint list.
  1.name= ~mission/push
  1.type= mavros_msgs/WaypointPush
  1.desc= Send new waypoint table.
  2.name= ~mission/clear
  2.type= mavros_msgs/WaypointClear
  2.desc= Clear mission on FCU.
  3.name= ~mission/set_current
  3.type= mavros_msgs/WaypointSetCurrent
  3.desc= Set current seq. number in list.
 }
 param {
  0.name= ~mission/pull_after_gcs
  0.type= bool
  0.desc= Defines pull or not waypoints if detected GCS activity.
  0.default= false
 }
}
```



### Notes

Plugins: [`vision_position`](https://index.ros.org/p/mavros_extras)
and [`vision_speed`](https://index.ros.org/p/mavros_extras) moved to
[mavros_extras](https://index.ros.org/p/mavros_extras). Experimental
MAVLink 2.0 support (without packet signing).

#### Avoiding Pitfalls Related to Ellipsoid Height and Height Above Mean Sea Level

When controlling the FCU using
[global setpoints](https://wiki.ros.org/mavros#mavros.2FPlugins.setpoint_position),
you specify the altitude as meters above mean sea level (AMSL). But when
sensing the
[global position](https://wiki.ros.org/mavros#mavros.2FPlugins.global_position),
the altitude reported by `global_position/global` is specified as
meters above the WGS-84 ellipsoid. This can lead to differences in
altitude that are dozens of meters apart.

MAVROS uses [GeographicLib](https://geographiclib.sourceforge.io/) to
convert AMSL to ellipsoid height. When you install MAVROS using a
package manager, this library gets installed as a dependency in Ubuntu.

To convert between AMSL and ellipsoid height, you add or subtract the
*geoid separation* to the altitude. To go from AMSL to ellipsoid height,
you add the value. And to go from ellipsoid height to AMSL you subtract
the value. Consider these examples.

- [This is how mavros converts AMSL to ellipsoid height in C++](https://github.com/mavlink/mavros/blob/8b9a32ac323e79cef826ee5f39aeb07a1162d240/mavros/src/plugins/global_position.cpp#L232)
- Here is an example using python:



```python
#!/usr/bin/env python3
# Example code that helps you convert between AMSL and ellipsoid height
# To run this code you need:
#
# 1) the egm96-5.pgm file from geographiclib.
# To get it on Ubuntu run:
# sudo apt install geographiclib-tools
# sudo geographiclib-get-geoids egm96-5
#
# 2) PyGeodesy
# To get it using pip:
# pip install PyGeodesy

from pygeodesy.geoids import GeoidPGM

_egm96 = GeoidPGM('/usr/share/GeographicLib/geoids/egm96-5.pgm', kind=-3)

def geoid_height(lat, lon):
    """Calculates AMSL to ellipsoid conversion offset.
    Uses EGM96 data with 5' grid and cubic interpolation.
    The value returned can help you convert from meters 
    above mean sea level (AMSL) to meters above
    the WGS84 ellipsoid.

    If you want to go from AMSL to ellipsoid height, add the value.

    To go from ellipsoid height to AMSL, subtract this value.
    """
    return _egm96.height(lat, lon)
```



In general, the ellipsoid height is better for calculations and AMSL is
better for user interfaces. If you're calculating the distance between
LLA positions, you most likely want to specify both altitudes in terms
of height above the ellipsoid. Both representations have their uses.

For background information regarding ellipsoid height and AMSL, see this
video: [Youtube](https://www.youtube.com/watch?v=dX6a6kCk3Po)

## CustomModes

### ArduPilot custom modes

#### APM:Plane

  -- ------------- -- ------------------ -- --------------------------- --
     **Numeric**      **String**            **Description and notes**   
     0                `MANUAL`                                        
     1                `CIRCLE`                                        
     2                `STABILIZE`                                     
     3                `TRAINING`                                      
     4                `ACRO`                                          
     5                `FBWA`              Fly by wire A               
     6                `FBWB`              Fly by wire B               
     7                `CRUISE`                                        
     8                `AUTOTUNE`                                      
     10               `AUTO`                                          
     11               `RTL`               Return To Launch            
     12               `LOITER`                                        
     14               `LAND`              *not in list now*           
     15               `GUIDED`                                        
     16               `INITIALISING`                                  
     17               `QSTABILIZE`                                    
     18               `QHOVER`                                        
     19               `QLOITER`                                       
     20               `QLAND`                                         
     21               `QRTL`                                          
  -- ------------- -- ------------------ -- --------------------------- --

Documentation: <http://plane.ardupilot.com/wiki/flight-modes/>

#### APM:Copter

  -- ------------- -- ------------------ -- -------------------------------- --
     **Numeric**      **String**            **Description and notes**        
     0                `STABILIZE`                                          
     1                `ACRO`                                               
     2                `ALT_HOLD`                                           
     3                `AUTO`                                               
     4                `GUIDED`                                             
     5                `LOITER`                                             
     6                `RTL`                                                
     7                `CIRCLE`                                             
     8                `POSITION`          *not in list*                    
     9                `LAND`                                               
     10               `OF_LOITER`                                          
     11               `DRIFT`             *renamed, prev name: APPROACH*   
     13               `SPORT`                                              
     14               `FLIP`                                               
     15               `AUTOTUNE`                                           
     16               `POSHOLD`                                            
     17               `BRAKE`                                              
     18               `THROW`                                              
     19               `AVOID_ADSB`                                         
     20               `GUIDED_NOGPS`                                       
  -- ------------- -- ------------------ -- -------------------------------- --

Documentation: <http://copter.ardupilot.com/wiki/flight-modes/>

#### APM:Rover

  -- ------------- -- ------------------ -- --------------------------- --
     **Numeric**      **String**            **Description and notes**   
     0                `MANUAL`                                        
     2                `LEARNING`                                      
     3                `STEERING`                                      
     4                `HOLD`                                          
     10               `AUTO`                                          
     11               `RTL`                                           
     15               `GUIDED`                                        
     16               `INITIALISING`                                  
  -- ------------- -- ------------------ -- --------------------------- --

Documentation: <http://rover.ardupilot.com/wiki/rover-control-modes/>

### PX4 native flight stack

  -- ------------------ -- -------------------------------------------------------------------------------------- --
     **String**            **Description and notes**                                                              
     `MANUAL`                                                                                                   
     `ACRO`                                                                                                     
     `ALTCTL`                                                                                                   
     `POSCTL`                                                                                                   
     `OFFBOARD`                                                                                                 
     `STABILIZED`                                                                                               
     `RATTITUDE`                                                                                                
     `AUTO.MISSION`                                                                                             
     `AUTO.LOITER`       disable RC failsafe, which can be done by setting **NAV_RCL_ACT** parameter to **0**   
     `AUTO.RTL`                                                                                                 
     `AUTO.LAND`                                                                                                
     `AUTO.RTGS`                                                                                                
     `AUTO.READY`                                                                                               
     `AUTO.TAKEOFF`                                                                                             
  -- ------------------ -- -------------------------------------------------------------------------------------- --

## Plugins_0.6

### Plugins for mavros 0.6

Standard plugin set for mavros version 0.6.



```clearsilver
node.0 {
 name= sys_status
 desc= Handles SYSTEM_STATUS and HEARTBEAT messages. Changes UAS.connection_status().
 pub {
  0.name= ~state
  0.type= mavros/State
  0.desc= FCU state
  1.name= ~battery
  1.type= mavros/BatteryStatus
  1.desc= FCU battery status report.
 }
 srv {
  0.name= ~set_stream_rate
  0.type= mavros/StreamRate
  0.desc= Send stream rate request to FCU. (Since 0.5.0)
 }
 param {
  0.name= ~conn_timeout
  0.type= double
  0.desc= Connection time out in seconds.
  0.default= 30.0
  1.name= ~conn_heartbeat
  1.type= double
  1.desc= Period to send HEARTBEAT messages (or disabled if 0.0)
  1.default= 0.0
  2.name= ~sys/min_voltage
  2.type= double
  2.desc= Minimal battery voltage for diagnostics.
  2.default= 6.0
 }
}
node.1 {
 name= imu_pub
 desc= Publish IMU state
 pub {
  0.name= ~imu/data
  0.type= sensor_msgs/Imu
  0.desc= Imu data, orientation computed by FCU
  1.name= ~imu/data_raw
  1.type= sensor_msgs/Imu
  1.desc= Raw IMU data without orientation
  2.name= ~imu/mag
  2.type= sensor_msgs/MagneticField
  2.desc= FCU compass data
  3.name= ~imu/temperature
  3.type= sensor_msgs/Temperature
  3.desc= Temperature reported by FCU (usually from barometer)
  4.name= ~imu/atm_pressure
  4.type= sensor_msgs/FluidPressure
  4.desc= Air pressure.
 }
 param {
  0.name= ~imu/frame_id
  0.type= string
  0.desc= Frame ID for this plugin.
  0.default= fcu
  1.name= ~imu/linear_acceleration_stdev
  1.type= double
  1.desc= Gyro's standard deviation
  1.default= 0.0003
  2.name= ~imu/angular_velocity_stdev
  2.type= double
  2.desc= Accel's standard deviation
  2.default= !dec 0.02
  3.name= ~imu/orientation_stdev
  3.type= double
  3.desc= Standard deviation for IMU.orientation
  3.default= 1.0
  4.name= ~imu/magnetic_stdev
  4.desc= Standard deviation for magnetic field message (undefined if: 0.0) (Since 0.6.0)
  4.default= 0.0
 }
}
node.2 {
 name= gps
 desc= Publish GPS Fix (like [[nmea_navsat_driver]])
 pub {
  0.name= ~fix
  0.type= sensor_msgs/NavSatFix
  0.desc= GPS position fix reported by the device.
  1.name= ~time_reference
  1.type= sensor_msgs/TimeReference
  1.desc= Time reference computed from SYSTEM_TIME.
  2.name= ~gps_vel
  2.type= geometry_msgs/TwistStamped
  2.desc= Velocity output from the GPS device.
 }
 param {
  0.name= ~gps/frame_id
  0.type= string
  0.desc= Frame ID for fix message.
  0.default= gps
  1.name= ~gps/time_ref_source
  1.type= string
  1.desc= Ref source for time_reference message.
  1.default= same as ~gps/frame_id
 }
}
node.3 {
 name= param
 desc= Allows to access to FCU parameters and map it to ROS parameters in `~param/`.
 srv {
  0.name= ~param/pull
  0.type= mavros/ParamPull
  0.desc= Request parameter from device (or internal cache).
  1.name= ~param/push
  1.type= mavros/ParamPush
  1.desc= Request send parameters from ROS to FCU.
  2.name= ~param/get
  2.type= mavros/ParamGet
  2.desc= Return FCU parameter value.
  3.name= ~param/set
  3.type= mavros/ParamSet
  3.desc= Set parameter on FCU immidiatly.
 }
}
node.4 {
 name= waypoint
 desc= Allows to access to FCU mission (waypoints).
 pub {
  0.name= ~mission/waypoints
  0.type= mavros/WaypointList
  0.desc= Current waypoint table. Updates on changes.
 }
 srv {
  0.name= ~mission/pull
  0.type= mavros/WaypointPull
  0.desc= Request update waypoint list.
  1.name= ~mission/push
  1.type= mavros/WaypointPush
  1.desc= Send new waypoint table.
  2.name= ~mission/clear
  2.type= mavros/WaypointClear
  2.desc= Clear mission on FCU.
  3.name= ~mission/set_current
  3.type= mavros/WaypointSetCurrent
  3.desc= Set current seq. number in list.
  4.name= ~mission/goto
  4.type= mavros/WaypointGOTO
  4.desc= Send goto point (APM specific).
 }
 param {
  0.name= ~mission/pull_after_gcs
  0.type= bool
  0.desc= Defines pull or not waypoints if detected GCS activity.
  0.default= false
 }
}
node.5 {
 name= rc_io
 desc= Publish RC receiver inputs.
 pub {
  0.name= ~rc/in
  0.type= mavros/RCIn
  0.desc= Publish RC inputs (in raw milliseconds)
  1.name= ~rc/out
  1.type= mavros/RCOut
  1.desc= Publish FCU servo outputs
 }
 srv {
  0.name= ~rc/override
  0.type= mavros/OverrideRCIn
  0.desc= Send RC override message to FCU (Since 0.5.0)
 }
}
node.6 {
 name= command
 desc= Send COMMAND_LONG to FCU.
 srv {
  0.name= ~cmd/command
  0.type= mavros/CommandLong
  0.desc= Send any COMMAND_LONG to FCU.
  1.name= ~cmd/arming
  1.type= mavros/CommandBool
  1.desc= Change Arming status.
  2.name= ~cmd/set_mode
  2.type= mavros/CommandMode
  2.desc= Change FCU operation mode.
  3.name= ~cmd/set_home
  3.type= mavros/CommandHome
  3.desc= Change HOME location.
 }
}
node.7 {
 name= local_position
 desc= Publish LOCAL_POSITION_NED in [[tf|TF]] and PoseStamped topic. (Since 0.6.0)
 pub {
  0.name= ~position/local
  0.type= geometry_msgs/PoseStamped
  0.desc= Local position from FCU.
 }
 param {
  0.name= ~position/local/send_tf
  0.type= bool
  0.desc= TF send switch.
  0.default= true
  1.name= ~position/local/frame_id
  1.type= string
  1.desc= Origin frame_id for TF.
  1.default= local_origin
  2.name= ~position/local/child_frame_id
  2.type= string
  2.desc= Child frame_id for TF and PoseStamped.
  2.default= fcu
 }
}
node.8 {
 name= vision_position
 desc= Sent VISION_POSITION_ESTIMATE to FCU from PoseStamped topic. (Since 0.6.0)
 sub {
  0.name= ~position/vision
  0.type= geometry_msgs/PoseStamped
  0.desc= Vision position.
  1.name= ~position/vision
  1.type= geometry_msgs/PoseWithCovarianceStamped
  1.desc= Vision position with covariance (optional alternative).
 }
 param {
  0.name= ~position/vision/pose_with_covariance
  0.type= bool
  0.desc= Selector for vision position message type.
  0.default= false
  1.name= ~position/vision/listen_tf
  1.type= bool
  1.desc= TF listen switch. Disable topic if enabled.
  1.default= false
  2.name= ~position/vision/frame_id
  2.type= string
  2.desc= Origin frame_id for TF.
  2.default= local_origin
  3.name= ~position/vision/child_frame_id
  3.type= string
  3.desc= Child frame_id for TF.
  3.default= vision
  4.name= ~position/vision/tf_rate_limit
  4.type= double
  4.desc= Rate limit for TF listener [Hz]. (Since '''UPCOMING''')
  4.default= 50.0
 }
}
node.9 {
 name= setpoint_position
 desc= Sent LOCAL_NED_POSITION_SETPOINT_EXTERNAL to FCU. (Since 0.6.0)
 sub {
  0.name= ~position/local_setpoint
  0.type= geometry_msgs/PoseStamped
  0.desc= Setpoint position. Orientation not used.
 }
 param {
  0.name= ~position/setpoint/listen_tf
  0.type= bool
  0.desc= TF listen switch. Disable topic if enabled.
  0.default= false
  1.name= ~position/setpoint/frame_id
  1.type= string
  1.desc= Origin frame_id for TF.
  1.default= local_origin
  2.name= ~position/setpoint/child_frame_id
  2.type= string
  2.desc= Child frame_id for TF.
  2.default= setpoint
  3.name= ~position/setpoint/tf_rate_limit
  3.type= double
  3.desc= Rate limit for TF listener [Hz]. (Since '''UPCOMING''')
  3.default= 50.0
 }
}
node.10 {
 name= safety_area
 desc= Sends safety allowed area to FCU. Initial area can be loaded from parameters. (Since '''UPCOMING''')
 sub {
  0.name= ~safety_area/set
  0.type= geometry_msgs/PolygonStamped
  0.desc= Volumetric area described by two corners.
 }
 param {
  0.name= ~safety_area/p1/x
  0.type= double
  0.desc= Corner 1 X.
  1.name= ~safety_area/p1/y
  1.type= double
  1.desc= Corner 1 Y.
  2.name= ~safety_area/p1/z
  2.type= double
  2.desc= Corner 1 Z.
  3.name= ~safety_area/p2/x
  3.type= double
  3.desc= Corner 2 X.
  4.name= ~safety_area/p2/y
  4.type= double
  4.desc= Corner 2 Y.
  5.name= ~safety_area/p2/z
  5.type= double
  5.desc= Corner 2 Z.
 }
}
```

## Plugins_0.7

### Plugins for mavros 0.7

Standard plugin set for mavros version 0.7.



```clearsilver
node.0 {
 name= sys_status
 desc= Handles SYSTEM_STATUS and HEARTBEAT messages. Changes UAS.connection_status().
 pub {
  0.name= ~state
  0.type= mavros/State
  0.desc= FCU state
  1.name= ~battery
  1.type= mavros/BatteryStatus
  1.desc= FCU battery status report.
 }
 srv {
  0.name= ~set_stream_rate
  0.type= mavros/StreamRate
  0.desc= Send stream rate request to FCU. (Since 0.5.0)
 }
 param {
  0.name= ~conn_timeout
  0.type= double
  0.desc= Connection time out in seconds.
  0.default= 30.0
  1.name= ~conn_heartbeat
  1.type= double
  1.desc= Period to send HEARTBEAT messages (or disabled if 0.0)
  1.default= 0.0
  2.name= ~sys/min_voltage
  2.type= double
  2.desc= Minimal battery voltage for diagnostics.
  2.default= 6.0
 }
}
node.1 {
 name= imu_pub
 desc= Publish IMU state
 pub {
  0.name= ~imu/data
  0.type= sensor_msgs/Imu
  0.desc= Imu data, orientation computed by FCU
  1.name= ~imu/data_raw
  1.type= sensor_msgs/Imu
  1.desc= Raw IMU data without orientation
  2.name= ~imu/mag
  2.type= sensor_msgs/MagneticField
  2.desc= FCU compass data
  3.name= ~imu/temperature
  3.type= sensor_msgs/Temperature
  3.desc= Temperature reported by FCU (usually from barometer)
  4.name= ~imu/atm_pressure
  4.type= sensor_msgs/FluidPressure
  4.desc= Air pressure.
 }
 param {
  0.name= ~imu/frame_id
  0.type= string
  0.desc= Frame ID for this plugin.
  0.default= fcu
  1.name= ~imu/linear_acceleration_stdev
  1.type= double
  1.desc= Gyro's standard deviation
  1.default= 0.0003
  2.name= ~imu/angular_velocity_stdev
  2.type= double
  2.desc= Accel's standard deviation
  2.default= !dec 0.02
  3.name= ~imu/orientation_stdev
  3.type= double
  3.desc= Standard deviation for IMU.orientation
  3.default= 1.0
  4.name= ~imu/magnetic_stdev
  4.desc= Standard deviation for magnetic field message (undefined if: 0.0)
  4.default= 0.0
 }
}
node.2 {
 name= gps
 desc= Publish GPS Fix (like [[nmea_navsat_driver]])
 pub {
  0.name= ~fix
  0.type= sensor_msgs/NavSatFix
  0.desc= GPS position fix reported by the device.
  1.name= ~time_reference
  1.type= sensor_msgs/TimeReference
  1.desc= Time reference computed from SYSTEM_TIME.
  2.name= ~gps_vel
  2.type= geometry_msgs/TwistStamped
  2.desc= Velocity output from the GPS device.
 }
 param {
  0.name= ~gps/frame_id
  0.type= string
  0.desc= Frame ID for fix message.
  0.default= gps
  1.name= ~gps/time_ref_source
  1.type= string
  1.desc= Ref source for time_reference message.
  1.default= same as ~gps/frame_id
 }
}
node.3 {
 name= param
 desc= Allows to access to FCU parameters and map it to ROS parameters in `~param/`.
 srv {
  0.name= ~param/pull
  0.type= mavros/ParamPull
  0.desc= Request parameter from device (or internal cache).
  1.name= ~param/push
  1.type= mavros/ParamPush
  1.desc= Request send parameters from ROS to FCU.
  2.name= ~param/get
  2.type= mavros/ParamGet
  2.desc= Return FCU parameter value.
  3.name= ~param/set
  3.type= mavros/ParamSet
  3.desc= Set parameter on FCU immidiatly.
 }
}
node.4 {
 name= waypoint
 desc= Allows to access to FCU mission (waypoints).
 pub {
  0.name= ~mission/waypoints
  0.type= mavros/WaypointList
  0.desc= Current waypoint table. Updates on changes.
 }
 srv {
  0.name= ~mission/pull
  0.type= mavros/WaypointPull
  0.desc= Request update waypoint list.
  1.name= ~mission/push
  1.type= mavros/WaypointPush
  1.desc= Send new waypoint table.
  2.name= ~mission/clear
  2.type= mavros/WaypointClear
  2.desc= Clear mission on FCU.
  3.name= ~mission/set_current
  3.type= mavros/WaypointSetCurrent
  3.desc= Set current seq. number in list.
  4.name= ~mission/goto
  4.type= mavros/WaypointGOTO
  4.desc= Send goto point (APM specific).
 }
 param {
  0.name= ~mission/pull_after_gcs
  0.type= bool
  0.desc= Defines pull or not waypoints if detected GCS activity.
  0.default= false
 }
}
node.5 {
 name= rc_io
 desc= Publish RC receiver inputs.
 pub {
  0.name= ~rc/in
  0.type= mavros/RCIn
  0.desc= Publish RC inputs (in raw milliseconds)
  1.name= ~rc/out
  1.type= mavros/RCOut
  1.desc= Publish FCU servo outputs
  2.name= ~rc/override
  2.type= mavros/OverrideRCIn
  2.desc= Send RC override message to FCU. This topic replace override service. <<Version(0.7.0)>>
 }
}
node.6 {
 name= command
 desc= Send COMMAND_LONG to FCU.
 srv {
  0.name= ~cmd/command
  0.type= mavros/CommandLong
  0.desc= Send any COMMAND_LONG to FCU.
  1.name= ~cmd/arming
  1.type= mavros/CommandBool
  1.desc= Change Arming status.
  2.name= ~cmd/set_mode
  2.type= mavros/CommandMode
  2.desc= Change FCU operation mode.
  3.name= ~cmd/set_home
  3.type= mavros/CommandHome
  3.desc= Change HOME location.
 }
}
node.7 {
 name= local_position
 desc= Publish LOCAL_POSITION_NED in [[tf|TF]] and PoseStamped topic.
 pub {
  0.name= ~position/local
  0.type= geometry_msgs/PoseStamped
  0.desc= Local position from FCU.
 }
 param {
  0.name= ~position/local/send_tf
  0.type= bool
  0.desc= TF send switch.
  0.default= true
  1.name= ~position/local/frame_id
  1.type= string
  1.desc= Origin frame_id for TF.
  1.default= local_origin
  2.name= ~position/local/child_frame_id
  2.type= string
  2.desc= Child frame_id for TF and PoseStamped.
  2.default= fcu
 }
}
node.8 {
 name= vision_position
 desc= Sent VISION_POSITION_ESTIMATE to FCU from PoseStamped topic.
 sub {
  0.name= ~position/vision
  0.type= geometry_msgs/PoseStamped
  0.desc= Vision position.
  1.name= ~position/vision
  1.type= geometry_msgs/PoseWithCovarianceStamped
  1.desc= Vision position with covariance (optional alternative).
 }
 param {
  0.name= ~position/vision/pose_with_covariance
  0.type= bool
  0.desc= Selector for vision position message type.
  0.default= false
  1.name= ~position/vision/listen_tf
  1.type= bool
  1.desc= TF listen switch. Disable topic if enabled.
  1.default= false
  2.name= ~position/vision/frame_id
  2.type= string
  2.desc= Origin frame_id for TF.
  2.default= local_origin
  3.name= ~position/vision/child_frame_id
  3.type= string
  3.desc= Child frame_id for TF.
  3.default= vision
  4.name= ~position/vision/tf_rate_limit
  4.type= double
  4.desc= Rate limit for TF listener [Hz]. (Since '''UPCOMING''')
  4.default= 50.0
 }
}
node.9 {
 name= setpoint_accel
 desc= Send acceleration setpoint to FCU.
 sub {
  0.name= ~setpoint/accel
  0.type= geometry_msgs/Vector3
  0.desc= Acceleration or force setpoint vector.
 }
 param {
  0.name= ~setpoint/accel/send_force
  0.type= bool
  0.desc= Send force setpoint.
 }
}
node.10 {
 name= setpoint_attitude
 desc= Send ATTITUDE_SETPOINT_EXTERNAL to FCU.
 sub {
  0.name= ~setpoint/att_vel
  0.type= geometry_msgs/Twist
  0.desc= Send angular velocity.
  1.name= ~setpoint/attitude
  1.type= geometry_msgs/PoseStamped
  1.desc= Send attitude setpoint.
  2.name= ~setpoint/attitude
  2.type= geometry_msgs/PoseWithCovarianceStamped
  2.desc= Send attitude setpoint with covariance (alternative).
 }
 param {
  0.name= ~setpoint/attitude/listen_tf
  0.type= bool
  0.desc= TF listen switch. Disable topics if enabled.
  0.default= false
  1.name= ~setpoint/attitude/listen_twist
  1.type= bool
  1.desc= Use att_vel topic instead of attitude.
  1.default= false
  2.name= ~setpoint/attitude/pose_with_covariance
  2.type= bool
  2.desc= Selector for attitude message type.
  2.default= false
  3.name= ~setpoint/attitude/frame_id
  3.type= string
  3.desc= Origin frame_id for TF.
  3.default= local_origin
  4.name= ~setpoint/attitude/child_frame_id
  4.type= string
  4.desc= Child frame_id for TF.
  4.default= attitude
  5.name= ~setpoint/attitude/tf_rate_limit
  5.type= double
  5.desc= Rate limit for TF listener [Hz].
  5.default= 10.0
 }
}
node.11 {
 name= setpoint_position
 desc= Sent LOCAL_NED_POSITION_SETPOINT_EXTERNAL to FCU.
 sub {
  0.name= ~setpoint/local_setpoint
  0.type= geometry_msgs/PoseStamped
  0.desc= Setpoint position. Orientation not used.
 }
 param {
  0.name= ~setpoint/position/listen_tf
  0.type= bool
  0.desc= TF listen switch. Disable topic if enabled.
  0.default= false
  1.name= ~setpoint/position/frame_id
  1.type= string
  1.desc= Origin frame_id for TF.
  1.default= local_origin
  2.name= ~setpoint/position/child_frame_id
  2.type= string
  2.desc= Child frame_id for TF.
  2.default= setpoint
  3.name= ~setpoint/position/tf_rate_limit
  3.type= double
  3.desc= Rate limit for TF listener [Hz].
  3.default= 50.0
 }
}
node.12 {
 name= setpoint_velocity
 desc= Send velocity setpoint to FCU.
 sub {
  0.name= ~setpoint/cmd_vel
  0.type= geometry_msgs/Twist
  0.desc= Velocity setpoint.
 }
}
node.13 {
 name= safety_area
 desc= Sends safety allowed area to FCU. Initial area can be loaded from parameters.
 sub {
  0.name= ~safety_area/set
  0.type= geometry_msgs/PolygonStamped
  0.desc= Volumetric area described by two corners.
 }
 param {
  0.name= ~safety_area/p1/x
  0.type= double
  0.desc= Corner 1 X.
  1.name= ~safety_area/p1/y
  1.type= double
  1.desc= Corner 1 Y.
  2.name= ~safety_area/p1/z
  2.type= double
  2.desc= Corner 1 Z.
  3.name= ~safety_area/p2/x
  3.type= double
  3.desc= Corner 2 X.
  4.name= ~safety_area/p2/y
  4.type= double
  4.desc= Corner 2 Y.
  5.name= ~safety_area/p2/z
  5.type= double
  5.desc= Corner 2 Z.
 }
}
node.14 {
 name= 3dr_radio
 desc= Publish 3DR Radio status to diagnostics and topic.
 pub {
  0.name= ~radio_status
  0.type= mavros/RadioStatus
  0.desc= Status received from modem, same as RADIO_STATUS message.
 }
}
node.15 {
 name= vision_speed
 desc= Send vision speed estimates to FCU. <<Version(0.7.0)>>
 sub {
  0.name= ~vision_speed/speed_vector
  0.type= geometry_msgs/Vector3Stamped
  0.desc= Send speed vector.
  1.name= ~vision_speed/speed_twist
  1.type= geometry_msgs/TwistStamped
  1.desc= Send linear speed. (alternative)
 }
 param {
  0.name= ~vision_speed/listen_twist
  0.type= bool
  0.desc= Topic type selector.
  0.default= false
 }
}
```



#### Notes

Setpoint plugins are mutually exclusive, please blacklist all unused
plugins. Also APM does not support this commands.

Also blacklist `3dr_radio` if you dont use 3DR Radio for FCU
connection.

## Plugins_0.8

### Plugins for mavros 0.8

Standard plugin set for mavros version 0.8.



```clearsilver
node.0 {
 name= sys_status
 desc= Handles SYSTEM_STATUS and HEARTBEAT messages. Changes UAS.connection_status().
 pub {
  0.name= ~state
  0.type= mavros/State
  0.desc= FCU state
  1.name= ~battery
  1.type= mavros/BatteryStatus
  1.desc= FCU battery status report.
 }
 srv {
  0.name= ~set_stream_rate
  0.type= mavros/StreamRate
  0.desc= Send stream rate request to FCU. (Since 0.5.0)
  1.name= ~set_mode
  1.type= mavros/SetMode
  1.desc= Set FCU operation mode. See custom mode identifiers at [[mavros/FcuModes|modes page]]. <<Version(0.8.0)>>
 }
 param {
  0.name= ~conn_timeout
  0.type= double
  0.desc= Connection time out in seconds.
  0.default= 30.0
  1.name= ~conn_heartbeat
  1.type= double
  1.desc= Period to send HEARTBEAT messages (or disabled if 0.0)
  1.default= 0.0
  2.name= ~sys/min_voltage
  2.type= double
  2.desc= Minimal battery voltage for diagnostics.
  2.default= 6.0
  3.name= ~sys/disable_diag
  3.type= bool
  3.desc= Disable all diag except HEARTBEAT message.
  3.default= false
 }
}

node.1 {
 name= imu_pub
 desc= Publish IMU state
 pub {
  0.name= ~imu/data
  0.type= sensor_msgs/Imu
  0.desc= Imu data, orientation computed by FCU
  1.name= ~imu/data_raw
  1.type= sensor_msgs/Imu
  1.desc= Raw IMU data without orientation
  2.name= ~imu/mag
  2.type= sensor_msgs/MagneticField
  2.desc= FCU compass data
  3.name= ~imu/temperature
  3.type= sensor_msgs/Temperature
  3.desc= Temperature reported by FCU (usually from barometer)
  4.name= ~imu/atm_pressure
  4.type= sensor_msgs/FluidPressure
  4.desc= Air pressure.
 }
 param {
  0.name= ~imu/frame_id
  0.type= string
  0.desc= Frame ID for this plugin.
  0.default= fcu
  1.name= ~imu/linear_acceleration_stdev
  1.type= double
  1.desc= Gyro's standard deviation
  1.default= 0.0003
  2.name= ~imu/angular_velocity_stdev
  2.type= double
  2.desc= Accel's standard deviation
  2.default= !dec 0.02
  3.name= ~imu/orientation_stdev
  3.type= double
  3.desc= Standard deviation for IMU.orientation
  3.default= 1.0
  4.name= ~imu/magnetic_stdev
  4.desc= Standard deviation for magnetic field message (undefined if: 0.0)
  4.default= 0.0
 }
}

node.2 {
 name= gps
 desc= Publish GPS Fix (like [[nmea_navsat_driver]])
 pub {
  0.name= ~fix
  0.type= sensor_msgs/NavSatFix
  0.desc= GPS position fix reported by the device.
  1.name= ~time_reference
  1.type= sensor_msgs/TimeReference
  1.desc= Time reference computed from SYSTEM_TIME.
  2.name= ~gps_vel
  2.type= geometry_msgs/TwistStamped
  2.desc= Velocity output from the GPS device.
 }
 param {
  0.name= ~gps/frame_id
  0.type= string
  0.desc= Frame ID for fix message.
  0.default= gps
  1.name= ~gps/time_ref_source
  1.type= string
  1.desc= Ref source for time_reference message.
  1.default= same as ~gps/frame_id
 }
}

node.3 {
 name= param
 desc= Allows to access to FCU parameters and map it to ROS parameters in `~param/`.
 srv {
  0.name= ~param/pull
  0.type= mavros/ParamPull
  0.desc= Request parameter from device (or internal cache).
  1.name= ~param/push
  1.type= mavros/ParamPush
  1.desc= Request send parameters from ROS to FCU.
  2.name= ~param/get
  2.type= mavros/ParamGet
  2.desc= Return FCU parameter value.
  3.name= ~param/set
  3.type= mavros/ParamSet
  3.desc= Set parameter on FCU immidiatly.
 }
}

node.4 {
 name= waypoint
 desc= Allows to access to FCU mission (waypoints).
 pub {
  0.name= ~mission/waypoints
  0.type= mavros/WaypointList
  0.desc= Current waypoint table. Updates on changes.
 }
 srv {
  0.name= ~mission/pull
  0.type= mavros/WaypointPull
  0.desc= Request update waypoint list.
  1.name= ~mission/push
  1.type= mavros/WaypointPush
  1.desc= Send new waypoint table.
  2.name= ~mission/clear
  2.type= mavros/WaypointClear
  2.desc= Clear mission on FCU.
  3.name= ~mission/set_current
  3.type= mavros/WaypointSetCurrent
  3.desc= Set current seq. number in list.
  4.name= ~mission/goto
  4.type= mavros/WaypointGOTO
  4.desc= Send goto point (APM specific).
 }
 param {
  0.name= ~mission/pull_after_gcs
  0.type= bool
  0.desc= Defines pull or not waypoints if detected GCS activity.
  0.default= false
 }
}

node.5 {
 name= rc_io
 desc= Publish RC receiver inputs.
 pub {
  0.name= ~rc/in
  0.type= mavros/RCIn
  0.desc= Publish RC inputs (in raw milliseconds)
  1.name= ~rc/out
  1.type= mavros/RCOut
  1.desc= Publish FCU servo outputs
  2.name= ~rc/override
  2.type= mavros/OverrideRCIn
  2.desc= Send RC override message to FCU. This topic replace override service. <<Version(0.7.0)>>
 }
}

node.6 {
 name= command
 desc= Send COMMAND_LONG to FCU.
 srv {
  0.name= ~cmd/command
  0.type= mavros/CommandLong
  0.desc= Send any COMMAND_LONG to FCU.
  4.name= ~cmd/command_int
  4.type= mavros/CommandInt
  4.desc= Send any COMMAND_INT to FCU.
  1.name= ~cmd/arming
  1.type= mavros/CommandBool
  1.desc= Change Arming status.
  3.name= ~cmd/set_home
  3.type= mavros/CommandHome
  3.desc= Change HOME location.
  5.name= ~cmd/guided_enable
  5.type= mavros/CommandBool
  5.desc= Enable guided mode by sending MAV_CMD_NAV_GUIDED_ENABLE command.
  6.name= ~cmd/takeoff
  6.type= mavros/CommandTOL
  6.desc= Send takeoff command.
  7.name= ~cmd/land
  7.type= mavros/CommandTOL
  7.desc= Send land command.
 }
}

node.7 {
 name= local_position
 desc= Publish LOCAL_POSITION_NED in [[tf|TF]] and PoseStamped topic.
 pub {
  0.name= ~position/local
  0.type= geometry_msgs/PoseStamped
  0.desc= Local position from FCU.
 }
 param {
  0.name= ~position/local/send_tf
  0.type= bool
  0.desc= TF send switch.
  0.default= true
  1.name= ~position/local/frame_id
  1.type= string
  1.desc= Origin frame_id for TF.
  1.default= local_origin
  2.name= ~position/local/child_frame_id
  2.type= string
  2.desc= Child frame_id for TF and PoseStamped.
  2.default= fcu
 }
}

node.9 {
 name= setpoint_accel
 desc= Send acceleration setpoint to FCU.
 sub {
  0.name= ~setpoint/accel
  0.type= geometry_msgs/Vector3
  0.desc= Acceleration or force setpoint vector.
 }
 param {
  0.name= ~setpoint/accel/send_force
  0.type= bool
  0.desc= Send force setpoint.
 }
}

node.10 {
 name= setpoint_attitude
 desc= Send ATTITUDE_SETPOINT_EXTERNAL to FCU.
 sub {
  0.name= ~setpoint/att_vel
  0.type= geometry_msgs/Twist
  0.desc= Send angular velocity.
  1.name= ~setpoint/attitude
  1.type= geometry_msgs/PoseStamped
  1.desc= Send attitude setpoint.
  2.name= ~setpoint/attitude
  2.type= geometry_msgs/PoseWithCovarianceStamped
  2.desc= Send attitude setpoint with covariance (alternative).
 }
 param {
  0.name= ~setpoint/attitude/listen_tf
  0.type= bool
  0.desc= TF listen switch. Disable topics if enabled.
  0.default= false
  1.name= ~setpoint/attitude/listen_twist
  1.type= bool
  1.desc= Use att_vel topic instead of attitude.
  1.default= false
  2.name= ~setpoint/attitude/pose_with_covariance
  2.type= bool
  2.desc= Selector for attitude message type.
  2.default= false
  3.name= ~setpoint/attitude/frame_id
  3.type= string
  3.desc= Origin frame_id for TF.
  3.default= local_origin
  4.name= ~setpoint/attitude/child_frame_id
  4.type= string
  4.desc= Child frame_id for TF.
  4.default= attitude
  5.name= ~setpoint/attitude/tf_rate_limit
  5.type= double
  5.desc= Rate limit for TF listener [Hz].
  5.default= 10.0
 }
}

node.11 {
 name= setpoint_position
 desc= Sent LOCAL_NED_POSITION_SETPOINT_EXTERNAL to FCU.
 sub {
  0.name= ~setpoint/local_setpoint
  0.type= geometry_msgs/PoseStamped
  0.desc= Setpoint position. Orientation not used.
 }
 param {
  0.name= ~setpoint/position/listen_tf
  0.type= bool
  0.desc= TF listen switch. Disable topic if enabled.
  0.default= false
  1.name= ~setpoint/position/frame_id
  1.type= string
  1.desc= Origin frame_id for TF.
  1.default= local_origin
  2.name= ~setpoint/position/child_frame_id
  2.type= string
  2.desc= Child frame_id for TF.
  2.default= setpoint
  3.name= ~setpoint/position/tf_rate_limit
  3.type= double
  3.desc= Rate limit for TF listener [Hz].
  3.default= 50.0
 }
}

node.12 {
 name= setpoint_velocity
 desc= Send velocity setpoint to FCU.
 sub {
  0.name= ~setpoint/cmd_vel
  0.type= geometry_msgs/Twist
  0.desc= Velocity setpoint.
 }
}

node.13 {
 name= safety_area
 desc= Sends safety allowed area to FCU. Initial area can be loaded from parameters.
 sub {
  0.name= ~safety_area/set
  0.type= geometry_msgs/PolygonStamped
  0.desc= Volumetric area described by two corners.
 }
 param {
  0.name= ~safety_area/p1/x
  0.type= double
  0.desc= Corner 1 X.
  1.name= ~safety_area/p1/y
  1.type= double
  1.desc= Corner 1 Y.
  2.name= ~safety_area/p1/z
  2.type= double
  2.desc= Corner 1 Z.
  3.name= ~safety_area/p2/x
  3.type= double
  3.desc= Corner 2 X.
  4.name= ~safety_area/p2/y
  4.type= double
  4.desc= Corner 2 Y.
  5.name= ~safety_area/p2/z
  5.type= double
  5.desc= Corner 2 Z.
 }
}

node.14 {
 name= 3dr_radio
 desc= Publish 3DR Radio status to diagnostics and topic.
 pub {
  0.name= ~radio_status
  0.type= mavros/RadioStatus
  0.desc= Status received from modem, same as RADIO_STATUS message.
 }
}

node.16 {
 name= vfr_hud
 desc= Publish VFR_HUD and WIND messages. <<Version(0.8.0)>>
 pub {
  0.name= ~vfr_hud
  0.type= mavros/VFR_HUD
  0.desc= Data for HUD.
  1.name= ~wind_estimation
  1.type= geometry_msgs/TwistStamped
  1.desc= Wind estimation from FCU ('''APM''').
 }
}

node.17 {
 name= global_position
 desc= Publish global position information fused by FCU. <<Version(0.8.0)>>
 pub {
  0.name= ~global_position/global
  0.type= sensor_msgs/NavSatFix
  0.desc= GPS Fix.
  1.name= ~global_position/local
  1.type= geometry_msgs/PoseWithCovarianceStamped
  1.desc= UTM coords.
  2.name= ~global_position/gps_vel
  2.type= geometry_msgs/Vector3Stamped
  2.desc= Velocity fused by FCU.
  3.name= ~global_position/rel_alt
  3.type= std_msgs/Float64
  3.desc= Relative altitude.
  4.name= ~global_position/compass_hdg
  4.type= std_msgs/Float64
  4.desc= Compass heading in degrees.
 }
 param {
  0.name= ~global_position/send_tf
  0.type= bool
  0.desc= Send or not local UTM coords?
  1.name= ~global_position/frame_id
  1.type= string
  1.desc= Origin frame_id for TF.
  1.default= local_origin
  2.name= ~global_position/child_frame_id
  2.type= string
  2.desc= Child frame_id for TF.
  2.default= fcu
 }
}

node.18 {
 name= ftp
 desc= Support plugin for MAVLink-FTP ('''PX4'''). <<Version(0.8.0)>>
 srv {
  0.name= ~ftp/open
  0.type= mavros/FileOpen
  0.desc= Open file (acquire session).
  1.name= ~ftp/close
  1.type= mavros/FileClose
  1.desc= Close file (release session).
  2.name= ~ftp/read
  2.type= mavros/FileRead
  2.desc= Read from opened file.
  3.name= ~ftp/write
  3.type= mavros/FileWrite
  3.desc= Write to opened file.
  4.name= ~ftp/list
  4.type= mavros/FileList
  4.desc= List directory.
  5.name= ~ftp/truncate
  5.type= mavros/FileTruncate
  5.desc= Truncate file.
  6.name= ~ftp/remove
  6.type= mavros/FileRemove
  6.desc= Unlink file.
  7.name= ~ftp/rename
  7.type= mavros/FileRename
  7.desc= Rename file/directory.
  8.name= ~ftp/mkdir
  8.type= mavros/FileMakeDir
  8.desc= Create directory.
  9.name= ~ftp/rmdir
  9.type= mavros/FileRemoveDir
  9.desc= Remove directory.
  10.name= ~ftp/checksum
  10.type= mavros/FileChecksum
  10.desc= Request to calculate CRC32 of file on FCU.
  11.name= ~ftp/reset
  11.type= std_srvs/Empty
  11.desc= Reset FCU server (dangerous).
 }
}
```



#### Notes

Setpoint plugins are mutually exclusive, please blacklist all unused
plugins. Also APM does not support this commands.

Also blacklist `3dr_radio` if you dont use 3DR Radio for FCU
connection.

Plugins: [`vision_position`](https://index.ros.org/p/mavros_extras)
and [`vision_speed`](https://index.ros.org/p/mavros_extras) moved to
[mavros_extras](https://index.ros.org/p/mavros_extras).

## Plugins_0.10

### Plugins for mavros 0.10

Standard plugin set for mavros version 0.10.



```clearsilver
node.0 {
 name= sys_status
 desc= System status plugin. Handles FCU detection.
 pub {
  0.name= ~state
  0.type= mavros/State
  0.desc= FCU state
  1.name= ~battery
  1.type= mavros/BatteryStatus
  1.desc= FCU battery status report.
 }
 srv {
  0.name= ~set_stream_rate
  0.type= mavros/StreamRate
  0.desc= Send stream rate request to FCU. (Since 0.5.0)
  1.name= ~set_mode
  1.type= mavros/SetMode
  1.desc= Set FCU operation mode. See custom mode identifiers at [[mavros/FcuModes|modes page]]. <<Version(0.8.0)>>
 }
 param {
  0.name= ~conn_timeout
  0.type= double
  0.desc= Connection time out in seconds.
  0.default= 30.0
  1.name= ~conn_heartbeat
  1.type= double
  1.desc= Period to send HEARTBEAT messages (or disabled if 0.0)
  1.default= 0.0
  2.name= ~sys/min_voltage
  2.type= double
  2.desc= Minimal battery voltage for diagnostics.
  2.default= 6.0
  3.name= ~sys/disable_diag
  3.type= bool
  3.desc= Disable all diag except HEARTBEAT message.
  3.default= false
 }
}

node.19 {
 name= sys_time
 desc= System time plugin. Does time syncronization on '''PX4'''.
 pub {
  1.name= ~time_reference
  1.type= sensor_msgs/TimeReference
  1.desc= Time reference computed from SYSTEM_TIME.
 }
 param {
  0.name= ~conn_system_time
  0.type= double
  0.desc= Send `SYSTEM_TIME` to device period in seconds.
  0.default= 0.0
  1.name= ~conn_timesync
  1.type= double
  1.desc= TIMESYNC period. '''PX4''' only.
  1.default= 0.0
 }
}

node.1 {
 name= imu_pub
 desc= Publish IMU state
 pub {
  0.name= ~imu/data
  0.type= sensor_msgs/Imu
  0.desc= Imu data, orientation computed by FCU
  1.name= ~imu/data_raw
  1.type= sensor_msgs/Imu
  1.desc= Raw IMU data without orientation
  2.name= ~imu/mag
  2.type= sensor_msgs/MagneticField
  2.desc= FCU compass data
  3.name= ~imu/temperature
  3.type= sensor_msgs/Temperature
  3.desc= Temperature reported by FCU (usually from barometer)
  4.name= ~imu/atm_pressure
  4.type= sensor_msgs/FluidPressure
  4.desc= Air pressure.
 }
 param {
  0.name= ~imu/frame_id
  0.type= string
  0.desc= Frame ID for this plugin.
  0.default= fcu
  1.name= ~imu/linear_acceleration_stdev
  1.type= double
  1.desc= Gyro's standard deviation
  1.default= 0.0003
  2.name= ~imu/angular_velocity_stdev
  2.type= double
  2.desc= Accel's standard deviation
  2.default= !dec 0.02
  3.name= ~imu/orientation_stdev
  3.type= double
  3.desc= Standard deviation for IMU.orientation
  3.default= 1.0
  4.name= ~imu/magnetic_stdev
  4.desc= Standard deviation for magnetic field message (undefined if: 0.0)
  4.default= 0.0
 }
}

node.2 {
 name= gps
 desc= Publish GPS Fix (like [[nmea_navsat_driver]])
 pub {
  0.name= ~fix
  0.type= sensor_msgs/NavSatFix
  0.desc= GPS position fix reported by the device.
  2.name= ~gps_vel
  2.type= geometry_msgs/TwistStamped
  2.desc= Velocity output from the GPS device.
 }
 param {
  0.name= ~gps/frame_id
  0.type= string
  0.desc= Frame ID for fix message.
  0.default= gps
  1.name= ~gps/time_ref_source
  1.type= string
  1.desc= Ref source for time_reference message.
  1.default= same as ~gps/frame_id
 }
}

node.3 {
 name= param
 desc= Allows to access to FCU parameters and map it to ROS parameters in `~param/`.
 srv {
  0.name= ~param/pull
  0.type= mavros/ParamPull
  0.desc= Request parameter from device (or internal cache).
  1.name= ~param/push
  1.type= mavros/ParamPush
  1.desc= Request send parameters from ROS to FCU.
  2.name= ~param/get
  2.type= mavros/ParamGet
  2.desc= Return FCU parameter value.
  3.name= ~param/set
  3.type= mavros/ParamSet
  3.desc= Set parameter on FCU immidiatly.
 }
}

node.4 {
 name= waypoint
 desc= Allows to access to FCU mission (waypoints).
 pub {
  0.name= ~mission/waypoints
  0.type= mavros/WaypointList
  0.desc= Current waypoint table. Updates on changes.
 }
 srv {
  0.name= ~mission/pull
  0.type= mavros/WaypointPull
  0.desc= Request update waypoint list.
  1.name= ~mission/push
  1.type= mavros/WaypointPush
  1.desc= Send new waypoint table.
  2.name= ~mission/clear
  2.type= mavros/WaypointClear
  2.desc= Clear mission on FCU.
  3.name= ~mission/set_current
  3.type= mavros/WaypointSetCurrent
  3.desc= Set current seq. number in list.
  4.name= ~mission/goto
  4.type= mavros/WaypointGOTO
  4.desc= Send goto point (APM specific).
 }
 param {
  0.name= ~mission/pull_after_gcs
  0.type= bool
  0.desc= Defines pull or not waypoints if detected GCS activity.
  0.default= false
 }
}

node.5 {
 name= rc_io
 desc= Publish RC receiver inputs.
 pub {
  0.name= ~rc/in
  0.type= mavros/RCIn
  0.desc= Publish RC inputs (in raw milliseconds)
  1.name= ~rc/out
  1.type= mavros/RCOut
  1.desc= Publish FCU servo outputs
  2.name= ~rc/override
  2.type= mavros/OverrideRCIn
  2.desc= Send RC override message to FCU. '''APM''' only. Requires setup FCU param `SYSID_MYGCS` to match mavros system id.
 }
}

node.6 {
 name= command
 desc= Send COMMAND_LONG to FCU.
 srv {
  0.name= ~cmd/command
  0.type= mavros/CommandLong
  0.desc= Send any COMMAND_LONG to FCU.
  4.name= ~cmd/command_int
  4.type= mavros/CommandInt
  4.desc= Send any COMMAND_INT to FCU.
  1.name= ~cmd/arming
  1.type= mavros/CommandBool
  1.desc= Change Arming status.
  3.name= ~cmd/set_home
  3.type= mavros/CommandHome
  3.desc= Change HOME location.
  5.name= ~cmd/guided_enable
  5.type= mavros/CommandBool
  5.desc= Enable guided mode by sending MAV_CMD_NAV_GUIDED_ENABLE command.
  6.name= ~cmd/takeoff
  6.type= mavros/CommandTOL
  6.desc= Send takeoff command.
  7.name= ~cmd/land
  7.type= mavros/CommandTOL
  7.desc= Send land command.
 }
 param {
  0.name= ~cmd/use_comp_id_system_control
  0.type= bool
  0.desc= Use `SYSTEM_CONTROL` component id instead of mavros target component.
  0.default= false
 }
}

node.7 {
 name= local_position
 desc= Publish LOCAL_POSITION_NED in [[tf|TF]] and PoseStamped topic.
 pub {
  0.name= ~position/local
  0.type= geometry_msgs/PoseStamped
  0.desc= Local position from FCU.
 }
 param {
  0.name= ~position/local/send_tf
  0.type= bool
  0.desc= TF send switch.
  0.default= true
  1.name= ~position/local/frame_id
  1.type= string
  1.desc= Origin frame_id for TF.
  1.default= local_origin
  2.name= ~position/local/child_frame_id
  2.type= string
  2.desc= Child frame_id for TF and PoseStamped.
  2.default= fcu
 }
}

node.9 {
 name= setpoint_accel
 desc= Send acceleration setpoint to FCU.
 sub {
  0.name= ~setpoint/accel
  0.type= geometry_msgs/Vector3
  0.desc= Acceleration or force setpoint vector.
 }
 param {
  0.name= ~setpoint/accel/send_force
  0.type= bool
  0.desc= Send force setpoint.
 }
}

node.10 {
 name= setpoint_attitude
 desc= Send ATTITUDE_SETPOINT_EXTERNAL to FCU.
 sub {
  0.name= ~setpoint/att_vel
  0.type= geometry_msgs/Twist
  0.desc= Send angular velocity.
  1.name= ~setpoint/attitude
  1.type= geometry_msgs/PoseStamped
  1.desc= Send attitude setpoint.
  2.name= ~setpoint/attitude
  2.type= geometry_msgs/PoseWithCovarianceStamped
  2.desc= Send attitude setpoint with covariance (alternative).
 }
 param {
  0.name= ~setpoint/attitude/listen_tf
  0.type= bool
  0.desc= TF listen switch. Disable topics if enabled.
  0.default= false
  1.name= ~setpoint/attitude/listen_twist
  1.type= bool
  1.desc= Use att_vel topic instead of attitude.
  1.default= false
  2.name= ~setpoint/attitude/pose_with_covariance
  2.type= bool
  2.desc= Selector for attitude message type.
  2.default= false
  3.name= ~setpoint/attitude/frame_id
  3.type= string
  3.desc= Origin frame_id for TF.
  3.default= local_origin
  4.name= ~setpoint/attitude/child_frame_id
  4.type= string
  4.desc= Child frame_id for TF.
  4.default= attitude
  5.name= ~setpoint/attitude/tf_rate_limit
  5.type= double
  5.desc= Rate limit for TF listener [Hz].
  5.default= 10.0
 }
}

node.11 {
 name= setpoint_position
 desc= Sent LOCAL_NED_POSITION_SETPOINT_EXTERNAL to FCU.
 sub {
  0.name= ~setpoint/local_setpoint
  0.type= geometry_msgs/PoseStamped
  0.desc= Setpoint position. Orientation not used.
 }
 param {
  0.name= ~setpoint/position/listen_tf
  0.type= bool
  0.desc= TF listen switch. Disable topic if enabled.
  0.default= false
  1.name= ~setpoint/position/frame_id
  1.type= string
  1.desc= Origin frame_id for TF.
  1.default= local_origin
  2.name= ~setpoint/position/child_frame_id
  2.type= string
  2.desc= Child frame_id for TF.
  2.default= setpoint
  3.name= ~setpoint/position/tf_rate_limit
  3.type= double
  3.desc= Rate limit for TF listener [Hz].
  3.default= 50.0
 }
}

node.12 {
 name= setpoint_velocity
 desc= Send velocity setpoint to FCU.
 sub {
  0.name= ~setpoint/cmd_vel
  0.type= geometry_msgs/Twist
  0.desc= Velocity setpoint.
 }
}

node.13 {
 name= safety_area
 desc= Sends safety allowed area to FCU. Initial area can be loaded from parameters.
 sub {
  0.name= ~safety_area/set
  0.type= geometry_msgs/PolygonStamped
  0.desc= Volumetric area described by two corners.
 }
 param {
  0.name= ~safety_area/p1/x
  0.type= double
  0.desc= Corner 1 X.
  1.name= ~safety_area/p1/y
  1.type= double
  1.desc= Corner 1 Y.
  2.name= ~safety_area/p1/z
  2.type= double
  2.desc= Corner 1 Z.
  3.name= ~safety_area/p2/x
  3.type= double
  3.desc= Corner 2 X.
  4.name= ~safety_area/p2/y
  4.type= double
  4.desc= Corner 2 Y.
  5.name= ~safety_area/p2/z
  5.type= double
  5.desc= Corner 2 Z.
 }
}

node.14 {
 name= 3dr_radio
 desc= Publish 3DR Radio status to diagnostics and topic.
 pub {
  0.name= ~radio_status
  0.type= mavros/RadioStatus
  0.desc= Status received from modem, same as RADIO_STATUS message.
 }
}

node.16 {
 name= vfr_hud
 desc= Publish VFR_HUD and WIND messages. <<Version(0.8.0)>>
 pub {
  0.name= ~vfr_hud
  0.type= mavros/VFR_HUD
  0.desc= Data for HUD.
  1.name= ~wind_estimation
  1.type= geometry_msgs/TwistStamped
  1.desc= Wind estimation from FCU ('''APM''').
 }
}

node.17 {
 name= global_position
 desc= Publish global position information fused by FCU. <<Version(0.8.0)>>
 pub {
  0.name= ~global_position/global
  0.type= sensor_msgs/NavSatFix
  0.desc= GPS Fix.
  1.name= ~global_position/local
  1.type= geometry_msgs/PoseWithCovarianceStamped
  1.desc= UTM coords.
  2.name= ~global_position/gps_vel
  2.type= geometry_msgs/Vector3Stamped
  2.desc= Velocity fused by FCU.
  3.name= ~global_position/rel_alt
  3.type= std_msgs/Float64
  3.desc= Relative altitude.
  4.name= ~global_position/compass_hdg
  4.type= std_msgs/Float64
  4.desc= Compass heading in degrees.
 }
 param {
  0.name= ~global_position/send_tf
  0.type= bool
  0.desc= Send or not local UTM coords?
  1.name= ~global_position/frame_id
  1.type= string
  1.desc= Origin frame_id for TF.
  1.default= local_origin
  2.name= ~global_position/child_frame_id
  2.type= string
  2.desc= Child frame_id for TF.
  2.default= fcu
 }
}

node.18 {
 name= ftp
 desc= Support plugin for MAVLink-FTP ('''PX4'''). <<Version(0.8.0)>>
 srv {
  0.name= ~ftp/open
  0.type= mavros/FileOpen
  0.desc= Open file (acquire session).
  1.name= ~ftp/close
  1.type= mavros/FileClose
  1.desc= Close file (release session).
  2.name= ~ftp/read
  2.type= mavros/FileRead
  2.desc= Read from opened file.
  3.name= ~ftp/write
  3.type= mavros/FileWrite
  3.desc= Write to opened file.
  4.name= ~ftp/list
  4.type= mavros/FileList
  4.desc= List directory.
  5.name= ~ftp/truncate
  5.type= mavros/FileTruncate
  5.desc= Truncate file.
  6.name= ~ftp/remove
  6.type= mavros/FileRemove
  6.desc= Unlink file.
  7.name= ~ftp/rename
  7.type= mavros/FileRename
  7.desc= Rename file/directory.
  8.name= ~ftp/mkdir
  8.type= mavros/FileMakeDir
  8.desc= Create directory.
  9.name= ~ftp/rmdir
  9.type= mavros/FileRemoveDir
  9.desc= Remove directory.
  10.name= ~ftp/checksum
  10.type= mavros/FileChecksum
  10.desc= Request to calculate CRC32 of file on FCU.
  11.name= ~ftp/reset
  11.type= std_srvs/Empty
  11.desc= Reset FCU server (dangerous).
 }
}
```



#### Notes

Setpoint plugins are mutually exclusive, please blacklist all unused
plugins. Also APM does not support this commands.

Also blacklist `3dr_radio` if you dont use 3DR Radio for FCU
connection.

Plugins: [`vision_position`](https://index.ros.org/p/mavros_extras)
and [`vision_speed`](https://index.ros.org/p/mavros_extras) moved to
[mavros_extras](https://index.ros.org/p/mavros_extras).

## Plugins_0.11

### Plugins for mavros 0.11

Standard plugin set for mavros version 0.11.



```clearsilver
node.14 {
 name= 3dr_radio
 desc= Publish 3DR Radio status to diagnostics and topic.
 pub {
  0.name= ~radio_status
  0.type= mavros/RadioStatus
  0.desc= Status received from modem, same as RADIO_STATUS message.
 }
}

node.20 {
 name= actuator_control
 desc= Sends acruator commands to FCU. <<Version(0.11.0)>>
 sub {
  0.name= ~actuator_control
  0.type= mavros/ActuatorControl
  0.desc= actuator command
 }
}

node.6 {
 name= command
 desc= Send COMMAND_LONG to FCU.
 srv {
  0.name= ~cmd/command
  0.type= mavros/CommandLong
  0.desc= Send any COMMAND_LONG to FCU.
  4.name= ~cmd/command_int
  4.type= mavros/CommandInt
  4.desc= Send any COMMAND_INT to FCU.
  1.name= ~cmd/arming
  1.type= mavros/CommandBool
  1.desc= Change Arming status.
  3.name= ~cmd/set_home
  3.type= mavros/CommandHome
  3.desc= Change HOME location.
  5.name= ~cmd/guided_enable
  5.type= mavros/CommandBool
  5.desc= Enable guided mode by sending MAV_CMD_NAV_GUIDED_ENABLE command.
  6.name= ~cmd/takeoff
  6.type= mavros/CommandTOL
  6.desc= Send takeoff command.
  7.name= ~cmd/land
  7.type= mavros/CommandTOL
  7.desc= Send land command.
 }
 param {
  0.name= ~cmd/use_comp_id_system_control
  0.type= bool
  0.desc= Use `SYSTEM_CONTROL` component id instead of mavros target component.
  0.default= false
 }
}

node.18 {
 name= ftp
 desc= Support plugin for MAVLink-FTP ('''PX4''').
 srv {
  0.name= ~ftp/open
  0.type= mavros/FileOpen
  0.desc= Open file (acquire session).
  1.name= ~ftp/close
  1.type= mavros/FileClose
  1.desc= Close file (release session).
  2.name= ~ftp/read
  2.type= mavros/FileRead
  2.desc= Read from opened file.
  3.name= ~ftp/write
  3.type= mavros/FileWrite
  3.desc= Write to opened file.
  4.name= ~ftp/list
  4.type= mavros/FileList
  4.desc= List directory.
  5.name= ~ftp/truncate
  5.type= mavros/FileTruncate
  5.desc= Truncate file.
  6.name= ~ftp/remove
  6.type= mavros/FileRemove
  6.desc= Unlink file.
  7.name= ~ftp/rename
  7.type= mavros/FileRename
  7.desc= Rename file/directory.
  8.name= ~ftp/mkdir
  8.type= mavros/FileMakeDir
  8.desc= Create directory.
  9.name= ~ftp/rmdir
  9.type= mavros/FileRemoveDir
  9.desc= Remove directory.
  10.name= ~ftp/checksum
  10.type= mavros/FileChecksum
  10.desc= Request to calculate CRC32 of file on FCU.
  11.name= ~ftp/reset
  11.type= std_srvs/Empty
  11.desc= Reset FCU server (dangerous).
 }
}

node.17 {
 name= global_position
 desc= Publish global position information fused by FCU.
 pub {
  0.name= ~global_position/global
  0.type= sensor_msgs/NavSatFix
  0.desc= GPS Fix.
  1.name= ~global_position/local
  1.type= geometry_msgs/PoseWithCovarianceStamped
  1.desc= UTM coords.
  2.name= ~global_position/gp_vel
  2.type= geometry_msgs/Vector3Stamped
  2.desc= Velocity fused by FCU.
  3.name= ~global_position/rel_alt
  3.type= std_msgs/Float64
  3.desc= Relative altitude.
  4.name= ~global_position/compass_hdg
  4.type= std_msgs/Float64
  4.desc= Compass heading in degrees.
 }
 param {
  0.name= ~global_position/send_tf
  0.type= bool
  0.desc= Send or not local UTM coords?
  1.name= ~global_position/frame_id
  1.type= string
  1.desc= Origin frame_id for TF.
  1.default= local_origin
  2.name= ~global_position/child_frame_id
  2.type= string
  2.desc= Child frame_id for TF.
  2.default= fcu
 }
}

node.2 {
 name= gps
 desc= Publish GPS Fix (like [[nmea_navsat_driver]])
 pub {
  0.name= ~gps/fix
  0.type= sensor_msgs/NavSatFix
  0.desc= GPS position fix reported by the device.
  2.name= ~gps/gps_vel
  2.type= geometry_msgs/TwistStamped
  2.desc= Velocity output from the GPS device.
 }
 param {
  0.name= ~gps/frame_id
  0.type= string
  0.desc= Frame ID for fix message.
  0.default= gps
 }
}

node.1 {
 name= imu_pub
 desc= Publish IMU state
 pub {
  0.name= ~imu/data
  0.type= sensor_msgs/Imu
  0.desc= Imu data, orientation computed by FCU
  1.name= ~imu/data_raw
  1.type= sensor_msgs/Imu
  1.desc= Raw IMU data without orientation
  2.name= ~imu/mag
  2.type= sensor_msgs/MagneticField
  2.desc= FCU compass data
  3.name= ~imu/temperature
  3.type= sensor_msgs/Temperature
  3.desc= Temperature reported by FCU (usually from barometer)
  4.name= ~imu/atm_pressure
  4.type= sensor_msgs/FluidPressure
  4.desc= Air pressure.
 }
 param {
  0.name= ~imu/frame_id
  0.type= string
  0.desc= Frame ID for this plugin.
  0.default= fcu
  1.name= ~imu/linear_acceleration_stdev
  1.type= double
  1.desc= Gyro's standard deviation
  1.default= 0.0003
  2.name= ~imu/angular_velocity_stdev
  2.type= double
  2.desc= Accel's standard deviation
  2.default= !dec 0.02
  3.name= ~imu/orientation_stdev
  3.type= double
  3.desc= Standard deviation for IMU.orientation
  3.default= 1.0
  4.name= ~imu/magnetic_stdev
  4.desc= Standard deviation for magnetic field message (undefined if: 0.0)
  4.default= 0.0
 }
}

node.7 {
 name= local_position
 desc= Publish LOCAL_POSITION_NED in [[tf|TF]] and PoseStamped topic.
 pub {
  0.name= ~local_position/local
  0.type= geometry_msgs/PoseStamped
  0.desc= Local position from FCU.
 }
 param {
  0.name= ~local_position/send_tf
  0.type= bool
  0.desc= TF send switch.
  0.default= true
  1.name= ~local_position/frame_id
  1.type= string
  1.desc= Origin frame_id for TF.
  1.default= local_origin
  2.name= ~local_position/child_frame_id
  2.type= string
  2.desc= Child frame_id for TF and PoseStamped.
  2.default= fcu
 }
}

node.3 {
 name= param
 desc= Allows to access to FCU parameters and map it to ROS parameters in `~param/`.
 srv {
  0.name= ~param/pull
  0.type= mavros/ParamPull
  0.desc= Request parameter from device (or internal cache).
  1.name= ~param/push
  1.type= mavros/ParamPush
  1.desc= Request send parameters from ROS to FCU.
  2.name= ~param/get
  2.type= mavros/ParamGet
  2.desc= Return FCU parameter value.
  3.name= ~param/set
  3.type= mavros/ParamSet
  3.desc= Set parameter on FCU immidiatly.
 }
}

node.5 {
 name= rc_io
 desc= Publish RC receiver inputs.
 pub {
  0.name= ~rc/in
  0.type= mavros/RCIn
  0.desc= Publish RC inputs (in raw milliseconds)
  1.name= ~rc/out
  1.type= mavros/RCOut
  1.desc= Publish FCU servo outputs
  2.name= ~rc/override
  2.type= mavros/OverrideRCIn
  2.desc= Send RC override message to FCU. '''APM''' only. Requires setup FCU param `SYSID_MYGCS` to match mavros system id.
 }
}

node.13 {
 name= safety_area
 desc= Sends safety allowed area to FCU. Initial area can be loaded from parameters.
 sub {
  0.name= ~safety_area/set
  0.type= geometry_msgs/PolygonStamped
  0.desc= Volumetric area described by two corners.
 }
 param {
  0.name= ~safety_area/p1/x
  0.type= double
  0.desc= Corner 1 X.
  1.name= ~safety_area/p1/y
  1.type= double
  1.desc= Corner 1 Y.
  2.name= ~safety_area/p1/z
  2.type= double
  2.desc= Corner 1 Z.
  3.name= ~safety_area/p2/x
  3.type= double
  3.desc= Corner 2 X.
  4.name= ~safety_area/p2/y
  4.type= double
  4.desc= Corner 2 Y.
  5.name= ~safety_area/p2/z
  5.type= double
  5.desc= Corner 2 Z.
 }
}

node.9 {
 name= setpoint_accel
 desc= Send acceleration setpoint to FCU.
 sub {
  0.name= ~setpoint_accel/accel
  0.type= geometry_msgs/Vector3Stamped
  0.desc= Acceleration or force setpoint vector.
 }
 param {
  0.name= ~setpoint_accel/send_force
  0.type= bool
  0.desc= Send force setpoint.
 }
}

node.10 {
 name= setpoint_attitude
 desc= Send ATTITUDE_SETPOINT_EXTERNAL to FCU.
 sub {
  0.name= ~setpoint_attitude/cmd_vel
  0.type= geometry_msgs/TwistStamped
  0.desc= Send angular velocity.
  1.name= ~setpoint_attitude/attitude
  1.type= geometry_msgs/PoseStamped
  1.desc= Send attitude setpoint.
  2.name= ~setpoint_attitude/attitude
  2.type= geometry_msgs/PoseWithCovarianceStamped
  2.desc= Send attitude setpoint with covariance (alternative).
 }
 param {
  0.name= ~setpoint_attitude/listen_tf
  0.type= bool
  0.desc= TF listen switch. Disable topics if enabled.
  0.default= false
  1.name= ~setpoint_attitude/listen_twist
  1.type= bool
  1.desc= Use att_vel topic instead of attitude.
  1.default= false
  2.name= ~setpoint_attutude/pose_with_covariance
  2.type= bool
  2.desc= Selector for attitude message type.
  2.default= false
  3.name= ~setpoint_attutude/frame_id
  3.type= string
  3.desc= Origin frame_id for TF.
  3.default= local_origin
  4.name= ~setpoint_attitude/child_frame_id
  4.type= string
  4.desc= Child frame_id for TF.
  4.default= attitude
  5.name= ~setpoint_attitude/tf_rate_limit
  5.type= double
  5.desc= Rate limit for TF listener [Hz].
  5.default= 10.0
 }
}

node.11 {
 name= setpoint_position
 desc= Sent LOCAL_NED_POSITION_SETPOINT_EXTERNAL to FCU.
 sub {
  0.name= ~setpoint_position/local
  0.type= geometry_msgs/PoseStamped
  0.desc= Setpoint position. Orientation not used.
 }
 param {
  0.name= ~setpoint_position/listen_tf
  0.type= bool
  0.desc= TF listen switch. Disable topic if enabled.
  0.default= false
  1.name= ~setpoint_position/frame_id
  1.type= string
  1.desc= Origin frame_id for TF.
  1.default= local_origin
  2.name= ~setpoint_position/child_frame_id
  2.type= string
  2.desc= Child frame_id for TF.
  2.default= setpoint
  3.name= ~setpoint_position/tf_rate_limit
  3.type= double
  3.desc= Rate limit for TF listener [Hz].
  3.default= 50.0
 }
}

node.12 {
 name= setpoint_velocity
 desc= Send velocity setpoint to FCU.
 sub {
  0.name= ~setpoint_velocity/cmd_vel
  0.type= geometry_msgs/TwistStamped
  0.desc= Velocity setpoint.
 }
}

node.0 {
 name= sys_status
 desc= System status plugin. Handles FCU detection. '''REQUIRED''' never blacklist it!.
 pub {
  0.name= ~state
  0.type= mavros/State
  0.desc= FCU state
  1.name= ~battery
  1.type= mavros/BatteryStatus
  1.desc= FCU battery status report.
 }
 srv {
  0.name= ~set_stream_rate
  0.type= mavros/StreamRate
  0.desc= Send stream rate request to FCU.
  1.name= ~set_mode
  1.type= mavros/SetMode
  1.desc= Set FCU operation mode. See custom mode identifiers at [[mavros/FcuModes|modes page]].
 }
 param {
  0.name= ~conn/timeout
  0.type= double
  0.desc= Connection time out in seconds.
  0.default= 30.0
  1.name= ~conn/heartbeat
  1.type= double
  1.desc= Period to send HEARTBEAT messages (or disabled if 0.0)
  1.default= 0.0
  2.name= ~sys/min_voltage
  2.type= double
  2.desc= Minimal battery voltage for diagnostics.
  2.default= 6.0
  3.name= ~sys/disable_diag
  3.type= bool
  3.desc= Disable all diag except HEARTBEAT message.
  3.default= false
 }
}

node.19 {
 name= sys_time
 desc= System time plugin. Does time syncronization on '''PX4'''.
 pub {
  1.name= ~time_reference
  1.type= sensor_msgs/TimeReference
  1.desc= Time reference computed from SYSTEM_TIME.
 }
 param {
  0.name= ~conn/system_time
  0.type= double
  0.desc= Send `SYSTEM_TIME` to device period in seconds.
  0.default= 0.0
  1.name= ~conn/timesync
  1.type= double
  1.desc= TIMESYNC period. '''PX4''' only.
  1.default= 0.0
  2.name= ~time/time_ref_source
  2.type= string
  2.desc= Ref source for time_reference message.
  2.default= "fcu"
  3.name= ~time/timesync_avg_alpha
  3.type= double
  3.desc= Alpha for exponential moving average.
  3.default= 0.6
 }
}

node.16 {
 name= vfr_hud
 desc= Publish VFR_HUD and WIND messages.
 pub {
  0.name= ~vfr_hud
  0.type= mavros/VFR_HUD
  0.desc= Data for HUD.
  1.name= ~wind_estimation
  1.type= geometry_msgs/TwistStamped
  1.desc= Wind estimation from FCU ('''APM''').
 }
}

node.4 {
 name= waypoint
 desc= Allows to access to FCU mission (waypoints).
 pub {
  0.name= ~mission/waypoints
  0.type= mavros/WaypointList
  0.desc= Current waypoint table. Updates on changes.
 }
 srv {
  0.name= ~mission/pull
  0.type= mavros/WaypointPull
  0.desc= Request update waypoint list.
  1.name= ~mission/push
  1.type= mavros/WaypointPush
  1.desc= Send new waypoint table.
  2.name= ~mission/clear
  2.type= mavros/WaypointClear
  2.desc= Clear mission on FCU.
  3.name= ~mission/set_current
  3.type= mavros/WaypointSetCurrent
  3.desc= Set current seq. number in list.
  4.name= ~mission/goto
  4.type= mavros/WaypointGOTO
  4.desc= Send goto point (APM specific).
 }
 param {
  0.name= ~mission/pull_after_gcs
  0.type= bool
  0.desc= Defines pull or not waypoints if detected GCS activity.
  0.default= false
 }
}
```



#### Notes

Plugins: [`vision_position`](https://index.ros.org/p/mavros_extras)
and [`vision_speed`](https://index.ros.org/p/mavros_extras) moved to
[mavros_extras](https://index.ros.org/p/mavros_extras).

## Plugins_0.12-0.15

### Plugins for mavros 0.12-0.15

Standard plugin set for mavros version 0.12---0.15.



```clearsilver
node.14 {
 name= 3dr_radio
 desc= Publish 3DR Radio status to diagnostics and topic.
 pub {
  0.name= ~radio_status
  0.type= mavros_msgs/RadioStatus
  0.desc= Status received from modem, same as RADIO_STATUS message.
 }
}

node.20 {
 name= actuator_control
 desc= Sends acruator commands to FCU. <<Version(0.11.0)>>
 sub {
  0.name= ~actuator_control
  0.type= mavros_msgs/ActuatorControl
  0.desc= actuator command
 }
}

node.6 {
 name= command
 desc= Send COMMAND_LONG to FCU.
 srv {
  0.name= ~cmd/command
  0.type= mavros_msgs/CommandLong
  0.desc= Send any COMMAND_LONG to FCU.
  4.name= ~cmd/command_int
  4.type= mavros_msgs/CommandInt
  4.desc= Send any COMMAND_INT to FCU.
  1.name= ~cmd/arming
  1.type= mavros_msgs/CommandBool
  1.desc= Change Arming status.
  3.name= ~cmd/set_home
  3.type= mavros_msgs/CommandHome
  3.desc= Change HOME location.
  5.name= ~cmd/guided_enable
  5.type= mavros_msgs/CommandBool
  5.desc= Enable guided mode by sending MAV_CMD_NAV_GUIDED_ENABLE command.
  6.name= ~cmd/takeoff
  6.type= mavros_msgs/CommandTOL
  6.desc= Send takeoff command.
  7.name= ~cmd/land
  7.type= mavros_msgs/CommandTOL
  7.desc= Send land command.
  8.name= ~cmd/trigger_control
  8.type= mavros_msgs/CommandTriggerControl
  8.desc= Send camera trigger control command.
 }
 param {
  0.name= ~cmd/use_comp_id_system_control
  0.type= bool
  0.desc= Use `SYSTEM_CONTROL` component id instead of mavros target component.
  0.default= false
 }
}

node.18 {
 name= ftp
 desc= Support plugin for MAVLink-FTP ('''PX4''').
 srv {
  0.name= ~ftp/open
  0.type= mavros_msgs/FileOpen
  0.desc= Open file (acquire session).
  1.name= ~ftp/close
  1.type= mavros_msgs/FileClose
  1.desc= Close file (release session).
  2.name= ~ftp/read
  2.type= mavros_msgs/FileRead
  2.desc= Read from opened file.
  3.name= ~ftp/write
  3.type= mavros_msgs/FileWrite
  3.desc= Write to opened file.
  4.name= ~ftp/list
  4.type= mavros_msgs/FileList
  4.desc= List directory.
  5.name= ~ftp/truncate
  5.type= mavros_msgs/FileTruncate
  5.desc= Truncate file.
  6.name= ~ftp/remove
  6.type= mavros_msgs/FileRemove
  6.desc= Unlink file.
  7.name= ~ftp/rename
  7.type= mavros_msgs/FileRename
  7.desc= Rename file/directory.
  8.name= ~ftp/mkdir
  8.type= mavros_msgs/FileMakeDir
  8.desc= Create directory.
  9.name= ~ftp/rmdir
  9.type= mavros_msgs/FileRemoveDir
  9.desc= Remove directory.
  10.name= ~ftp/checksum
  10.type= mavros_msgs/FileChecksum
  10.desc= Request to calculate CRC32 of file on FCU.
  11.name= ~ftp/reset
  11.type= std_srvs/Empty
  11.desc= Reset FCU server (dangerous).
 }
}

node.17 {
 name= global_position
 desc= Publish global position information fused by FCU and raw GPS data.
 pub {
  0.name= ~global_position/global
  0.type= sensor_msgs/NavSatFix
  0.desc= GPS Fix.
  1.name= ~global_position/local
  1.type= geometry_msgs/PoseWithCovarianceStamped
  1.desc= UTM coords.
  2.name= ~global_position/gp_vel
  2.type= geometry_msgs/TwistStamped
  2.desc= Velocity fused by FCU.
  3.name= ~global_position/rel_alt
  3.type= std_msgs/Float64
  3.desc= Relative altitude.
  4.name= ~global_position/compass_hdg
  4.type= std_msgs/Float64
  4.desc= Compass heading in degrees.
  5.name= ~global_position/raw/fix
  5.type= sensor_msgs/NavSatFix
  5.desc= GPS position fix reported by the device.
  6.name= ~global_position/raw/gps_vel
  6.type= geometry_msgs/TwistStamped
  6.desc= Velocity output from the GPS device.
 }
 param {
  1.name= ~global_position/frame_id
  1.type= string
  1.desc= frame_id for messages.
  1.default= fcu
  0.name= ~global_position/tf/send
  0.type= bool
  0.desc= Send or not local UTM coords via TF?
  0.default= true
  3.name= ~global_position/tf/frame_id
  3.type= string
  3.desc= frame_id for TF.
  3.default= local_origin
  2.name= ~global_position/tf/child_frame_id
  2.type= string
  2.desc= Child frame_id for TF.
  2.default= fcu_utm
 }
}

node.1 {
 name= imu_pub
 desc= Publish IMU state
 pub {
  0.name= ~imu/data
  0.type= sensor_msgs/Imu
  0.desc= Imu data, orientation computed by FCU
  1.name= ~imu/data_raw
  1.type= sensor_msgs/Imu
  1.desc= Raw IMU data without orientation
  2.name= ~imu/mag
  2.type= sensor_msgs/MagneticField
  2.desc= FCU compass data
  3.name= ~imu/temperature
  3.type= sensor_msgs/Temperature
  3.desc= Temperature reported by FCU (usually from barometer)
  4.name= ~imu/atm_pressure
  4.type= sensor_msgs/FluidPressure
  4.desc= Air pressure.
 }
 param {
  0.name= ~imu/frame_id
  0.type= string
  0.desc= Frame ID for this plugin.
  0.default= fcu
  1.name= ~imu/linear_acceleration_stdev
  1.type= double
  1.desc= Gyro's standard deviation
  1.default= 0.0003
  2.name= ~imu/angular_velocity_stdev
  2.type= double
  2.desc= Accel's standard deviation
  2.default= !dec 0.02
  3.name= ~imu/orientation_stdev
  3.type= double
  3.desc= Standard deviation for IMU.orientation
  3.default= 1.0
  4.name= ~imu/magnetic_stdev
  4.type= double
  4.desc= Standard deviation for magnetic field message (undefined if: 0.0)
  4.default= 0.0
 }
}

node.7 {
 name= local_position
 desc= Publish LOCAL_POSITION_NED in [[tf|TF]] and PoseStamped topic.
 pub {
  0.name= ~local_position/local
  0.type= geometry_msgs/PoseStamped
  0.desc= Local position from FCU.
 }
 param {
  1.name= ~local_position/frame_id
  1.type= string
  1.desc= frame_id for message.
  1.default= fcu
  0.name= ~local_position/tf/send
  0.type= bool
  0.desc= TF send switch.
  0.default= true
  3.name= ~local_position/tf/frame_id
  3.type= string
  3.desc= Origin frame_id for TF.
  3.default= local_origin
  2.name= ~local_position/tf/child_frame_id
  2.type= string
  2.desc= Child frame_id for TF.
  2.default= fcu
 }
}

node.21 {
 name= manual_control
 desc= Publish MANUAL_CONTROL message (user input). <<Version(0.15.0)>>
 pub {
  0.name= ~manual_control/control
  0.type= mavros_msgs/ManualControl
  0.desc= RC Rx, interpreted and normalized.
 }
}

node.3 {
 name= param
 desc= Allows to access to FCU parameters and map it to ROS parameters in `~param/`.
 srv {
  0.name= ~param/pull
  0.type= mavros_msgs/ParamPull
  0.desc= Request parameter from device (or internal cache).
  1.name= ~param/push
  1.type= mavros_msgs/ParamPush
  1.desc= Request send parameters from ROS to FCU.
  2.name= ~param/get
  2.type= mavros_msgs/ParamGet
  2.desc= Return FCU parameter value.
  3.name= ~param/set
  3.type= mavros_msgs/ParamSet
  3.desc= Set parameter on FCU immidiatly.
 }
}

node.5 {
 name= rc_io
 desc= Publish RC receiver inputs.
 pub {
  0.name= ~rc/in
  0.type= mavros_msgs/RCIn
  0.desc= Publish RC inputs (in raw milliseconds)
  1.name= ~rc/out
  1.type= mavros_msgs/RCOut
  1.desc= Publish FCU servo outputs
 }
 sub {
  2.name= ~rc/override
  2.type= mavros_msgs/OverrideRCIn
  2.desc= Send RC override message to FCU. '''APM''' only. Requires setup FCU param `SYSID_MYGCS` to match mavros system id.
 }
}

node.13 {
 name= safety_area
 desc= Sends safety allowed area to FCU. Initial area can be loaded from parameters.
 sub {
  0.name= ~safety_area/set
  0.type= geometry_msgs/PolygonStamped
  0.desc= Volumetric area described by two corners.
 }
 param {
  0.name= ~safety_area/p1/x
  0.type= double
  0.desc= Corner 1 X.
  1.name= ~safety_area/p1/y
  1.type= double
  1.desc= Corner 1 Y.
  2.name= ~safety_area/p1/z
  2.type= double
  2.desc= Corner 1 Z.
  3.name= ~safety_area/p2/x
  3.type= double
  3.desc= Corner 2 X.
  4.name= ~safety_area/p2/y
  4.type= double
  4.desc= Corner 2 Y.
  5.name= ~safety_area/p2/z
  5.type= double
  5.desc= Corner 2 Z.
 }
}

node.9 {
 name= setpoint_accel
 desc= Send acceleration setpoint.
 sub {
  0.name= ~setpoint_accel/accel
  0.type= geometry_msgs/Vector3Stamped
  0.desc= Acceleration or force setpoint vector.
 }
 param {
  0.name= ~setpoint_accel/send_force
  0.type= bool
  0.desc= Send force setpoint.
 }
}

node.10 {
 name= setpoint_attitude
 desc= Send attitude setpoint using SET_ATTITUDE_TARGET.
 sub {
  0.name= ~setpoint_attitude/cmd_vel
  0.type= geometry_msgs/TwistStamped
  0.desc= Send angular velocity.
  1.name= ~setpoint_attitude/attitude
  1.type= geometry_msgs/PoseStamped
  1.desc= Send attitude setpoint.
 }
 param {
  6.name= ~setpoint_attitude/reverse_throttle
  6.type= bool
  6.desc= Allow to send -1.0 throttle or not.
  6.default= false
  0.name= ~setpoint_attitude/tf/listen
  0.type= bool
  0.desc= TF listen switch. Disable topics if enabled.
  0.default= false
  3.name= ~setpoint_attutude/tf/frame_id
  3.type= string
  3.desc= Origin frame_id for TF.
  3.default= local_origin
  4.name= ~setpoint_attitude/tf/child_frame_id
  4.type= string
  4.desc= Child frame_id for TF.
  4.default= attitude
  5.name= ~setpoint_attitude/tf/rate_limit
  5.type= double
  5.desc= Rate limit for TF listener [Hz].
  5.default= 10.0
 }
}

node.11 {
 name= setpoint_position
 desc= Sent position setpoint using SET_POSITION_TARGET_LOCAL_NED.
 sub {
  0.name= ~setpoint_position/local
  0.type= geometry_msgs/PoseStamped
  0.desc= Setpoint position. Orientation field not used.
 }
 param {
  0.name= ~setpoint_position/tf/listen
  0.type= bool
  0.desc= TF listen switch. Disable topic if enabled.
  0.default= false
  1.name= ~setpoint_position/tf/frame_id
  1.type= string
  1.desc= Origin frame_id for TF.
  1.default= local_origin
  2.name= ~setpoint_position/tf/child_frame_id
  2.type= string
  2.desc= Child frame_id for TF.
  2.default= setpoint
  3.name= ~setpoint_position/tf/rate_limit
  3.type= double
  3.desc= Rate limit for TF listener [Hz].
  3.default= 50.0
 }
}

node.12 {
 name= setpoint_velocity
 desc= Send velocity setpoint to FCU.
 sub {
  0.name= ~setpoint_velocity/cmd_vel
  0.type= geometry_msgs/TwistStamped
  0.desc= Velocity setpoint.
 }
}

node.0 {
 name= sys_status
 desc= System status plugin. Handles FCU detection. '''REQUIRED''' never blacklist it!.
 pub {
  0.name= ~state
  0.type= mavros_msgs/State
  0.desc= FCU state
  1.name= ~battery
  1.type= mavros_msgs/BatteryStatus
  1.desc= FCU battery status report.
 }
 srv {
  0.name= ~set_stream_rate
  0.type= mavros_msgs/StreamRate
  0.desc= Send stream rate request to FCU.
  1.name= ~set_mode
  1.type= mavros_msgs/SetMode
  1.desc= Set FCU operation mode. See custom mode identifiers at [[mavros/CustomModes|modes page]].
 }
 param {
  0.name= ~conn/timeout
  0.type= double
  0.desc= Connection time out in seconds.
  0.default= 30.0
  1.name= ~conn/heartbeat_rate
  1.type= double
  1.desc= Send HEARTBEAT message rate [Hz] (or disabled if 0.0)
  1.default= 0.0
  2.name= ~sys/min_voltage
  2.type= double
  2.desc= Minimal battery voltage for diagnostics.
  2.default= 6.0
  3.name= ~sys/disable_diag
  3.type= bool
  3.desc= Disable all diag except HEARTBEAT message.
  3.default= false
 }
}

node.19 {
 name= sys_time
 desc= System time plugin. Does time syncronization on '''PX4'''.
 pub {
  1.name= ~time_reference
  1.type= sensor_msgs/TimeReference
  1.desc= Time reference computed from SYSTEM_TIME.
 }
 param {
  0.name= ~conn/system_time_rate
  0.type= double
  0.desc= Send `SYSTEM_TIME` to device rate [Hz] (disabled if 0.0).
  0.default= 0.0
  1.name= ~conn/timesync_rate
  1.type= double
  1.desc= TIMESYNC rate. '''PX4''' only.
  1.default= 0.0
  2.name= ~time/time_ref_source
  2.type= string
  2.desc= Ref source for time_reference message.
  2.default= "fcu"
  3.name= ~time/timesync_avg_alpha
  3.type= double
  3.desc= Alpha for exponential moving average.
  3.default= 0.6
 }
}

node.16 {
 name= vfr_hud
 desc= Publish VFR_HUD and WIND messages.
 pub {
  0.name= ~vfr_hud
  0.type= mavros_msgs/VFR_HUD
  0.desc= Data for HUD.
  1.name= ~wind_estimation
  1.type= geometry_msgs/TwistStamped
  1.desc= Wind estimation from FCU ('''APM''').
 }
}

node.4 {
 name= waypoint
 desc= Allows to access to FCU mission (waypoints).
 pub {
  0.name= ~mission/waypoints
  0.type= mavros_msgs/WaypointList
  0.desc= Current waypoint table. Updates on changes.
 }
 srv {
  0.name= ~mission/pull
  0.type= mavros_msgs/WaypointPull
  0.desc= Request update waypoint list.
  1.name= ~mission/push
  1.type= mavros_msgs/WaypointPush
  1.desc= Send new waypoint table.
  2.name= ~mission/clear
  2.type= mavros_msgs/WaypointClear
  2.desc= Clear mission on FCU.
  3.name= ~mission/set_current
  3.type= mavros_msgs/WaypointSetCurrent
  3.desc= Set current seq. number in list.
  4.name= ~mission/goto
  4.type= mavros_msgs/WaypointGOTO
  4.desc= Send goto point (APM specific).
 }
 param {
  0.name= ~mission/pull_after_gcs
  0.type= bool
  0.desc= Defines pull or not waypoints if detected GCS activity.
  0.default= false
 }
}
```



#### Notes

Plugins: [`vision_position`](https://index.ros.org/p/mavros_extras)
and [`vision_speed`](https://index.ros.org/p/mavros_extras) moved to
[mavros_extras](https://index.ros.org/p/mavros_extras). GPS and
global_position plugins are merged. TF params moved to `tf/`
subnamespace.

## Plugins_0.16-0.17

### Plugins for mavros 0.16-0.17

Standard plugin set for mavros version 0.16---0.17.



```clearsilver
node.14 {
 name= 3dr_radio
 desc= Publish 3DR Radio status to diagnostics and topic.
 pub {
  0.name= ~radio_status
  0.type= mavros_msgs/RadioStatus
  0.desc= Status received from modem, same as RADIO_STATUS message.
 }
}

node.23 {
 name= altitude
 desc= Publish altitude information.
 pub {
  0.name= ~altitude
  0.type= mavros_msgs/Altitude
  0.desc= Direct copy of altitude data provided by Mavlink.
 }
 param {
  0.name= ~frame_id
  0.type= string
  0.desc= frame for altitude messages
  0.default= "map"
 }
}

node.20 {
 name= actuator_control
 desc= Sends acruator commands to FCU. <<Version(0.11.0)>>
 sub {
  0.name= ~actuator_control
  0.type= mavros_msgs/ActuatorControl
  0.desc= actuator command
 }
}

node.6 {
 name= command
 desc= Send COMMAND_LONG to FCU.
 srv {
  0.name= ~cmd/command
  0.type= mavros_msgs/CommandLong
  0.desc= Send any COMMAND_LONG to FCU.
  4.name= ~cmd/command_int
  4.type= mavros_msgs/CommandInt
  4.desc= Send any COMMAND_INT to FCU.
  1.name= ~cmd/arming
  1.type= mavros_msgs/CommandBool
  1.desc= Change Arming status.
  3.name= ~cmd/set_home
  3.type= mavros_msgs/CommandHome
  3.desc= Change HOME location.
  6.name= ~cmd/takeoff
  6.type= mavros_msgs/CommandTOL
  6.desc= Send takeoff command.
  7.name= ~cmd/land
  7.type= mavros_msgs/CommandTOL
  7.desc= Send land command.
  8.name= ~cmd/trigger_control
  8.type= mavros_msgs/CommandTriggerControl
  8.desc= Send camera trigger control command.
 }
 param {
  0.name= ~cmd/use_comp_id_system_control
  0.type= bool
  0.desc= Use `SYSTEM_CONTROL` component id instead of mavros target component.
  0.default= false
 }
}

node.18 {
 name= ftp
 desc= Support plugin for MAVLink-FTP ('''PX4''').
 srv {
  0.name= ~ftp/open
  0.type= mavros_msgs/FileOpen
  0.desc= Open file (acquire session).
  1.name= ~ftp/close
  1.type= mavros_msgs/FileClose
  1.desc= Close file (release session).
  2.name= ~ftp/read
  2.type= mavros_msgs/FileRead
  2.desc= Read from opened file.
  3.name= ~ftp/write
  3.type= mavros_msgs/FileWrite
  3.desc= Write to opened file.
  4.name= ~ftp/list
  4.type= mavros_msgs/FileList
  4.desc= List directory.
  5.name= ~ftp/truncate
  5.type= mavros_msgs/FileTruncate
  5.desc= Truncate file.
  6.name= ~ftp/remove
  6.type= mavros_msgs/FileRemove
  6.desc= Unlink file.
  7.name= ~ftp/rename
  7.type= mavros_msgs/FileRename
  7.desc= Rename file/directory.
  8.name= ~ftp/mkdir
  8.type= mavros_msgs/FileMakeDir
  8.desc= Create directory.
  9.name= ~ftp/rmdir
  9.type= mavros_msgs/FileRemoveDir
  9.desc= Remove directory.
  10.name= ~ftp/checksum
  10.type= mavros_msgs/FileChecksum
  10.desc= Request to calculate CRC32 of file on FCU.
  11.name= ~ftp/reset
  11.type= std_srvs/Empty
  11.desc= Reset FCU server (dangerous).
 }
}

node.17 {
 name= global_position
 desc= Publish global position information fused by FCU and raw GPS data.
 pub {
  0.name= ~global_position/global
  0.type= sensor_msgs/NavSatFix
  0.desc= GPS Fix.
  1.name= ~global_position/local
  1.type= geometry_msgs/PoseWithCovarianceStamped
  1.desc= UTM coords.
  2.name= ~global_position/gp_vel
  2.type= geometry_msgs/TwistStamped
  2.desc= Velocity fused by FCU.
  3.name= ~global_position/rel_alt
  3.type= std_msgs/Float64
  3.desc= Relative altitude.
  4.name= ~global_position/compass_hdg
  4.type= std_msgs/Float64
  4.desc= Compass heading in degrees.
  5.name= ~global_position/raw/fix
  5.type= sensor_msgs/NavSatFix
  5.desc= GPS position fix reported by the device.
  6.name= ~global_position/raw/gps_vel
  6.type= geometry_msgs/TwistStamped
  6.desc= Velocity output from the GPS device.
 }
 param {
  1.name= ~global_position/frame_id
  1.type= string
  1.desc= frame_id for messages.
  1.default= fcu
  0.name= ~global_position/tf/send
  0.type= bool
  0.desc= Send or not local UTM coords via TF?
  0.default= true
  3.name= ~global_position/tf/frame_id
  3.type= string
  3.desc= frame_id for TF.
  3.default= local_origin
  2.name= ~global_position/tf/child_frame_id
  2.type= string
  2.desc= Child frame_id for TF.
  2.default= fcu_utm
 }
}

node.1 {
 name= imu_pub
 desc= Publish IMU state
 pub {
  0.name= ~imu/data
  0.type= sensor_msgs/Imu
  0.desc= Imu data, orientation computed by FCU
  1.name= ~imu/data_raw
  1.type= sensor_msgs/Imu
  1.desc= Raw IMU data without orientation
  2.name= ~imu/mag
  2.type= sensor_msgs/MagneticField
  2.desc= FCU compass data
  3.name= ~imu/temperature
  3.type= sensor_msgs/Temperature
  3.desc= Temperature reported by FCU (usually from barometer)
  4.name= ~imu/atm_pressure
  4.type= sensor_msgs/FluidPressure
  4.desc= Air pressure.
 }
 param {
  0.name= ~imu/frame_id
  0.type= string
  0.desc= Frame ID for this plugin.
  0.default= fcu
  1.name= ~imu/linear_acceleration_stdev
  1.type= double
  1.desc= Gyro's standard deviation
  1.default= 0.0003
  2.name= ~imu/angular_velocity_stdev
  2.type= double
  2.desc= Accel's standard deviation
  2.default= !dec 0.02
  3.name= ~imu/orientation_stdev
  3.type= double
  3.desc= Standard deviation for IMU.orientation
  3.default= 1.0
  4.name= ~imu/magnetic_stdev
  4.type= double
  4.desc= Standard deviation for magnetic field message (undefined if: 0.0)
  4.default= 0.0
 }
}

node.7 {
 name= local_position
 desc= Publish LOCAL_POSITION_NED in [[tf|TF]] and PoseStamped topic.
 pub {
  0.name= ~local_position/pose
  0.type= geometry_msgs/PoseStamped
  0.desc= Local position from FCU.
  1.name= ~local_position/velocity
  1.type= geometry_msgs/TwistStamped
  1.desc= Velocity data from FCU.
 }
 param {
  1.name= ~local_position/frame_id
  1.type= string
  1.desc= frame_id for message.
  1.default= fcu
  0.name= ~local_position/tf/send
  0.type= bool
  0.desc= TF send switch.
  0.default= true
  3.name= ~local_position/tf/frame_id
  3.type= string
  3.desc= Origin frame_id for TF.
  3.default= local_origin
  2.name= ~local_position/tf/child_frame_id
  2.type= string
  2.desc= Child frame_id for TF.
  2.default= fcu
 }
}

node.21 {
 name= manual_control
 desc= Publish MANUAL_CONTROL message (user input). <<Version(0.15.0)>>
 pub {
  0.name= ~manual_control/control
  0.type= mavros_msgs/ManualControl
  0.desc= RC Rx, interpreted and normalized.
 }
}

node.3 {
 name= param
 desc= Allows to access to FCU parameters and map it to ROS parameters in `~param/`.
 srv {
  0.name= ~param/pull
  0.type= mavros_msgs/ParamPull
  0.desc= Request parameter from device (or internal cache).
  1.name= ~param/push
  1.type= mavros_msgs/ParamPush
  1.desc= Request send parameters from ROS to FCU.
  2.name= ~param/get
  2.type= mavros_msgs/ParamGet
  2.desc= Return FCU parameter value.
  3.name= ~param/set
  3.type= mavros_msgs/ParamSet
  3.desc= Set parameter on FCU immidiatly.
 }
}

node.5 {
 name= rc_io
 desc= Publish RC receiver inputs.
 pub {
  0.name= ~rc/in
  0.type= mavros_msgs/RCIn
  0.desc= Publish RC inputs (in raw milliseconds)
  1.name= ~rc/out
  1.type= mavros_msgs/RCOut
  1.desc= Publish FCU servo outputs
 }
 sub {
  2.name= ~rc/override
  2.type= mavros_msgs/OverrideRCIn
  2.desc= Send RC override message to FCU. '''APM''' and '''PX4''' only. APM requires setup FCU param `SYSID_MYGCS` to match mavros system id. '''Not recommended''' to use in automatic control because lack of safety mechanisms. Use one of setpoint plugins and OFFBOARD mode.
 }
}

node.13 {
 name= safety_area
 desc= Sends safety allowed area to FCU. Initial area can be loaded from parameters.
 sub {
  0.name= ~safety_area/set
  0.type= geometry_msgs/PolygonStamped
  0.desc= Volumetric area described by two corners.
 }
 param {
  0.name= ~safety_area/p1/x
  0.type= double
  0.desc= Corner 1 X.
  1.name= ~safety_area/p1/y
  1.type= double
  1.desc= Corner 1 Y.
  2.name= ~safety_area/p1/z
  2.type= double
  2.desc= Corner 1 Z.
  3.name= ~safety_area/p2/x
  3.type= double
  3.desc= Corner 2 X.
  4.name= ~safety_area/p2/y
  4.type= double
  4.desc= Corner 2 Y.
  5.name= ~safety_area/p2/z
  5.type= double
  5.desc= Corner 2 Z.
 }
}

node.9 {
 name= setpoint_accel
 desc= Send acceleration setpoint.
 sub {
  0.name= ~setpoint_accel/accel
  0.type= geometry_msgs/Vector3Stamped
  0.desc= Acceleration or force setpoint vector.
 }
 param {
  0.name= ~setpoint_accel/send_force
  0.type= bool
  0.desc= Send force setpoint.
 }
}

node.10 {
 name= setpoint_attitude
 desc= Send attitude setpoint using SET_ATTITUDE_TARGET.
 sub {
  0.name= ~setpoint_attitude/cmd_vel
  0.type= geometry_msgs/TwistStamped
  0.desc= Send angular velocity.
  1.name= ~setpoint_attitude/attitude
  1.type= geometry_msgs/PoseStamped
  1.desc= Send attitude setpoint.
 }
 param {
  6.name= ~setpoint_attitude/reverse_throttle
  6.type= bool
  6.desc= Allow to send -1.0 throttle or not.
  6.default= false
  0.name= ~setpoint_attitude/tf/listen
  0.type= bool
  0.desc= TF listen switch. Disable topics if enabled.
  0.default= false
  3.name= ~setpoint_attutude/tf/frame_id
  3.type= string
  3.desc= Origin frame_id for TF.
  3.default= local_origin
  4.name= ~setpoint_attitude/tf/child_frame_id
  4.type= string
  4.desc= Child frame_id for TF.
  4.default= attitude
  5.name= ~setpoint_attitude/tf/rate_limit
  5.type= double
  5.desc= Rate limit for TF listener [Hz].
  5.default= 10.0
 }
}

node.11 {
 name= setpoint_position
 desc= Sent position setpoint using SET_POSITION_TARGET_LOCAL_NED.
 sub {
  0.name= ~setpoint_position/local
  0.type= geometry_msgs/PoseStamped
  0.desc= Setpoint position. Only YAW axis extracted from orientation field.
 }
 param {
  0.name= ~setpoint_position/tf/listen
  0.type= bool
  0.desc= TF listen switch. Disable topic if enabled.
  0.default= false
  1.name= ~setpoint_position/tf/frame_id
  1.type= string
  1.desc= Origin frame_id for TF.
  1.default= local_origin
  2.name= ~setpoint_position/tf/child_frame_id
  2.type= string
  2.desc= Child frame_id for TF.
  2.default= setpoint
  3.name= ~setpoint_position/tf/rate_limit
  3.type= double
  3.desc= Rate limit for TF listener [Hz].
  3.default= 50.0
 }
}

node.22 {
 name= setpoint_raw
 desc= Send RAW setpoint messages to FCU and provide loopback topics (PX4).
 pub {
  0.name= ~setpoint_raw/target_local
  0.type= mavros_msgs/PositionTarget
  0.desc= Local target loopback.
  1.name= ~setpoint_raw/target_global
  1.type= mavros_msgs/GlobalPositionTarget
  1.desc= Global target loopback.
  2.name= ~setpoint_raw/target_attitude
  2.type= mavros_msgs/AttitudeTarget
  2.desc= Attitude target loopback.
 }
 sub {
  0.name= ~setpoint_raw/local
  0.type= mavros_msgs/PositionTarget
  0.desc= Local position, velocity and acceleration setpoint.
  1.name= ~setpoint_raw/global
  1.type= mavros_msgs/GlobalPositionTarget
  1.desc= Global position, velocity and acceleration setpoint.
  2.name= ~setpoint_raw/attitude
  2.type= mavros_msgs/AttitudeTarget
  2.desc= Attitude, angular rate and thrust setpoint.
 }
}

node.12 {
 name= setpoint_velocity
 desc= Send velocity setpoint to FCU.
 sub {
  0.name= ~setpoint_velocity/cmd_vel
  0.type= geometry_msgs/TwistStamped
  0.desc= Velocity setpoint.
 }
}

node.0 {
 name= sys_status
 desc= System status plugin. Handles FCU detection. '''REQUIRED''' never blacklist it!.
 pub {
  0.name= ~state
  0.type= mavros_msgs/State
  0.desc= FCU state
  1.name= ~battery
  1.type= mavros_msgs/BatteryStatus
  1.desc= FCU battery status report.
  2.name= ~extended_state
  2.type= mavros_msgs/ExtendedState
  2.desc= Landing detector and VTOL state.
 }
 srv {
  0.name= ~set_stream_rate
  0.type= mavros_msgs/StreamRate
  0.desc= Send stream rate request to FCU.
  1.name= ~set_mode
  1.type= mavros_msgs/SetMode
  1.desc= Set FCU operation mode. See custom mode identifiers at [[mavros/CustomModes|modes page]].
 }
 param {
  0.name= ~conn/timeout
  0.type= double
  0.desc= Connection time out in seconds.
  0.default= 30.0
  1.name= ~conn/heartbeat_rate
  1.type= double
  1.desc= Send HEARTBEAT message rate [Hz] (or disabled if 0.0)
  1.default= 0.0
  2.name= ~sys/min_voltage
  2.type= double
  2.desc= Minimal battery voltage for diagnostics.
  2.default= 6.0
  3.name= ~sys/disable_diag
  3.type= bool
  3.desc= Disable all diag except HEARTBEAT message.
  3.default= false
 }
}

node.19 {
 name= sys_time
 desc= System time plugin. Does time syncronization on '''PX4'''.
 pub {
  1.name= ~time_reference
  1.type= sensor_msgs/TimeReference
  1.desc= Time reference computed from SYSTEM_TIME.
 }
 param {
  0.name= ~conn/system_time_rate
  0.type= double
  0.desc= Send `SYSTEM_TIME` to device rate [Hz] (disabled if 0.0).
  0.default= 0.0
  1.name= ~conn/timesync_rate
  1.type= double
  1.desc= TIMESYNC rate. '''PX4''' only.
  1.default= 0.0
  2.name= ~time/time_ref_source
  2.type= string
  2.desc= Ref source for time_reference message.
  2.default= "fcu"
  3.name= ~time/timesync_avg_alpha
  3.type= double
  3.desc= Alpha for exponential moving average.
  3.default= 0.6
 }
}

node.16 {
 name= vfr_hud
 desc= Publish VFR_HUD and WIND messages.
 pub {
  0.name= ~vfr_hud
  0.type= mavros_msgs/VFR_HUD
  0.desc= Data for HUD.
  1.name= ~wind_estimation
  1.type= geometry_msgs/TwistStamped
  1.desc= Wind estimation from FCU ('''APM''').
 }
}

node.4 {
 name= waypoint
 desc= Allows to access to FCU mission (waypoints).
 pub {
  0.name= ~mission/waypoints
  0.type= mavros_msgs/WaypointList
  0.desc= Current waypoint table. Updates on changes.
 }
 srv {
  0.name= ~mission/pull
  0.type= mavros_msgs/WaypointPull
  0.desc= Request update waypoint list.
  1.name= ~mission/push
  1.type= mavros_msgs/WaypointPush
  1.desc= Send new waypoint table.
  2.name= ~mission/clear
  2.type= mavros_msgs/WaypointClear
  2.desc= Clear mission on FCU.
  3.name= ~mission/set_current
  3.type= mavros_msgs/WaypointSetCurrent
  3.desc= Set current seq. number in list.
 }
 param {
  0.name= ~mission/pull_after_gcs
  0.type= bool
  0.desc= Defines pull or not waypoints if detected GCS activity.
  0.default= false
 }
}
```



#### Notes

Plugins: [`vision_position`](https://index.ros.org/p/mavros_extras)
and [`vision_speed`](https://index.ros.org/p/mavros_extras) moved to
[mavros_extras](https://index.ros.org/p/mavros_extras). GPS and
global_position plugins are merged. TF params moved to `tf/`
subnamespace. Waypoint GOTO service removed. Please use setpoint
plugins.
