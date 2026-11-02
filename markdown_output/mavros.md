## Overview

This package provides communication driver for various autopilots with
MAVLink communication protocol. Additional it provides UDP MAVLink
bridge for ground control stations (e.g. QGroundControl).

Main node can be extended by plugins (see
[pluginlib](https://index.ros.org/p/pluginlib)). See also
[mavros_extras](https://index.ros.org/p/mavros_extras) package.

## Nodes

### mavros_node

main communication node.

#### Subscribed Topics

- `mavlink/to`
  ([mavros_msgs/msg/Mavlink](https://docs.ros.org/en/rolling/p/mavros_msgs/msg/Mavlink.html)):
  Mavlink stream to autopilot.

#### Published Topics

- `mavlink/from`
  ([mavros_msgs/msg/Mavlink](https://docs.ros.org/en/rolling/p/mavros_msgs/msg/Mavlink.html)):
  Mavlink stream from autopilot.
- `diagnostics`
  ([diagnostic_msgs/msg/DiagnosticStatus](https://docs.ros.org/en/rolling/p/diagnostic_msgs/msg/DiagnosticStatus.html)):
  Diagnostic status information.

#### Parameters

- `~system_id` (`int`, default: `1`): Node MAVLink System ID.
- `~component_id` (`int`, default: `240`): Node MAVLink Component ID.
- `~target_system_id` (`int`, default: `1`): FCU MAVLink System ID.
- `~target_component_id` (`int`, default: `1`): FCU MAVLink Component
  ID.
- `~startup_px4_usb_quirk` (`bool`, default: `false`): Define apply
  quirk for PX4 or not.
- `~plugin_blacklist` (`string[]`, default: `[]`): Alias blacklist (glob
  syntax, example: \['rc\*'\])
- `~plugin_whitelist` (`string[]`, default: `[]`): Alias whitelist (glob
  syntax, overrides blacklist)
- `~fcu_url` (`string`, default: `/dev/ttyACM0:57600`): FCU connection
  URL.
- `~fcu_protocol` (`string`, default: `v2.0`): MAVLink protocol version.
  Supported: "v1.0", "v2.0"
- `~gcs_url` (`string`, default: `udp://@`): GCS bridge connection URL.

### gcs_bridge

Additional proxy. Old name `ros_udp`.

#### Subscribed Topics

- `mavlink/from`
  ([mavros_msgs/msg/Mavlink](https://docs.ros.org/en/rolling/p/mavros_msgs/msg/Mavlink.html)):
  Mavlink stream from autopilot.

#### Published Topics

- `mavlink/to`
  ([mavros_msgs/msg/Mavlink](https://docs.ros.org/en/rolling/p/mavros_msgs/msg/Mavlink.html)):
  Mavlink stream to autopilot.

#### Parameters

- `~gcs_url` (`string`, default: `udp://@`): Connection URL.

### event_launcher

Listens to arming status, triggers and run programs on event.
[Example config.](https://github.com/mavlink/mavros/blob/master/mavros/launch/event_launcher.yaml)

#### Subscribed Topics

- `mavros/state`
  ([mavros_msgs/msg/State](https://docs.ros.org/en/rolling/p/mavros_msgs/msg/State.html)):
  Source of arming events.

#### Services

- `<trigger_event>`
  ([std_srvs/srv/Trigger](https://docs.ros.org/en/rolling/p/std_srvs/srv/Trigger.html)):
  Optional event triggers. You may create several services using
  configuration.

#### Parameters

- `~<event_name>/service` (`string`): Create event (with name
  <event_name>) triggered by service (param value).
- `~<event_handler>/event` (`string[]`): List of events triggered that
  handler.
- `~<event_handler>/action` (`string[]`): List of actions to do on
  corresponding event. Supported actions: **run**, **stop**.
- `~<event_handler>/shell` (`string`): Command to run/stop on event.
- `~<event_handler>/logfile` (`string`, default: `""`): File to save
  stdout and stderr output of command. Optional.

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
[mavros_node](#mavros_node).

Note: this list for 0.18.0 version.
Older versions: [0.6.0](#plugins_06),
[0.7.0](#plugins_07),
[0.8.0](#plugins_08),
[0.10.0](#plugins_010),
[0.11.0](#plugins_011),
[0.12.0 --- 0.15.0](#plugins_012-015),
[0.16.0 --- 0.17.0](#plugins_016-017).

### 3dr_radio

Publish 3DR Radio status to diagnostics and topic.

#### Published Topics

- `~radio_status`
  ([mavros_msgs/msg/RadioStatus](https://docs.ros.org/en/rolling/p/mavros_msgs/msg/RadioStatus.html)):
  Status received from modem, same as RADIO_STATUS message.

### actuator_control

Sends acruator commands to FCU.

#### Subscribed Topics

- `~actuator_control`
  ([mavros_msgs/msg/ActuatorControl](https://docs.ros.org/en/rolling/p/mavros_msgs/msg/ActuatorControl.html)):
  actuator command

### hil_controls

Publish HIL_CONTROLS

#### Published Topics

- `~hil_controls/hil_controls`
  ([mavros_msgs/msg/HilControls](https://docs.ros.org/en/rolling/p/mavros_msgs/msg/HilControls.html)):
  HIL data

#### Parameters

- `~frame_id` (`string`, default: `"map"`): frame for altitude messages

### command

Send COMMAND_LONG to FCU.

#### Services

- `~cmd/command`
  ([mavros_msgs/srv/CommandLong](https://docs.ros.org/en/rolling/p/mavros_msgs/srv/CommandLong.html)):
  Send any COMMAND_LONG to FCU.
- `~cmd/command_int`
  ([mavros_msgs/srv/CommandInt](https://docs.ros.org/en/rolling/p/mavros_msgs/srv/CommandInt.html)):
  Send any COMMAND_INT to FCU.
- `~cmd/arming`
  ([mavros_msgs/srv/CommandBool](https://docs.ros.org/en/rolling/p/mavros_msgs/srv/CommandBool.html)):
  Change Arming status.
- `~cmd/set_home`
  ([mavros_msgs/srv/CommandHome](https://docs.ros.org/en/rolling/p/mavros_msgs/srv/CommandHome.html)):
  Change HOME location.
- `~cmd/takeoff`
  ([mavros_msgs/srv/CommandTOL](https://docs.ros.org/en/rolling/p/mavros_msgs/srv/CommandTOL.html)):
  Send takeoff command.
- `~cmd/land`
  ([mavros_msgs/srv/CommandTOL](https://docs.ros.org/en/rolling/p/mavros_msgs/srv/CommandTOL.html)):
  Send land command.
- `~cmd/trigger_control`
  ([mavros_msgs/srv/CommandTriggerControl](https://docs.ros.org/en/rolling/p/mavros_msgs/srv/CommandTriggerControl.html)):
  Send camera trigger control command.

#### Parameters

- `~cmd/use_comp_id_system_control` (`bool`, default: `false`): Use
  `SYSTEM_CONTROL` component id instead of mavros target component.

### ftp

Support plugin for MAVLink-FTP (**PX4**).

#### Services

- `~ftp/open`
  ([mavros_msgs/srv/FileOpen](https://docs.ros.org/en/rolling/p/mavros_msgs/srv/FileOpen.html)):
  Open file (acquire session).
- `~ftp/close`
  ([mavros_msgs/srv/FileClose](https://docs.ros.org/en/rolling/p/mavros_msgs/srv/FileClose.html)):
  Close file (release session).
- `~ftp/read`
  ([mavros_msgs/srv/FileRead](https://docs.ros.org/en/rolling/p/mavros_msgs/srv/FileRead.html)):
  Read from opened file.
- `~ftp/write`
  ([mavros_msgs/srv/FileWrite](https://docs.ros.org/en/rolling/p/mavros_msgs/srv/FileWrite.html)):
  Write to opened file.
- `~ftp/list`
  ([mavros_msgs/srv/FileList](https://docs.ros.org/en/rolling/p/mavros_msgs/srv/FileList.html)):
  List directory.
- `~ftp/truncate`
  ([mavros_msgs/srv/FileTruncate](https://docs.ros.org/en/rolling/p/mavros_msgs/srv/FileTruncate.html)):
  Truncate file.
- `~ftp/remove`
  ([mavros_msgs/srv/FileRemove](https://docs.ros.org/en/rolling/p/mavros_msgs/srv/FileRemove.html)):
  Unlink file.
- `~ftp/rename`
  ([mavros_msgs/srv/FileRename](https://docs.ros.org/en/rolling/p/mavros_msgs/srv/FileRename.html)):
  Rename file/directory.
- `~ftp/mkdir`
  ([mavros_msgs/srv/FileMakeDir](https://docs.ros.org/en/rolling/p/mavros_msgs/srv/FileMakeDir.html)):
  Create directory.
- `~ftp/rmdir`
  ([mavros_msgs/srv/FileRemoveDir](https://docs.ros.org/en/rolling/p/mavros_msgs/srv/FileRemoveDir.html)):
  Remove directory.
- `~ftp/checksum`
  ([mavros_msgs/srv/FileChecksum](https://docs.ros.org/en/rolling/p/mavros_msgs/srv/FileChecksum.html)):
  Request to calculate CRC32 of file on FCU.
- `~ftp/reset`
  ([std_srvs/srv/Empty](https://docs.ros.org/en/rolling/p/std_srvs/srv/Empty.html)):
  Reset FCU server (dangerous).

### global_position

Publish global position information fused by FCU and raw GPS data.

#### Published Topics

- `~global_position/global`
  ([sensor_msgs/msg/NavSatFix](https://docs.ros.org/en/rolling/p/sensor_msgs/msg/NavSatFix.html)):
  GPS Fix. **IMPORTANT:** Altitude is specified as ellipsoid height and
  care must be taken to avoid a common pitfall.
  [See this section for more](https://wiki.ros.org/mavros#mavros.2FPlugins.Avoiding_Pitfalls_Related_to_Ellipsoid_Height_and_Height_Above_Mean_Sea_Level).
- `~global_position/local`
  ([geometry_msgs/msg/PoseWithCovarianceStamped](https://docs.ros.org/en/rolling/p/geometry_msgs/msg/PoseWithCovarianceStamped.html)):
  UTM coords.
- `~global_position/gp_vel`
  ([geometry_msgs/msg/TwistStamped](https://docs.ros.org/en/rolling/p/geometry_msgs/msg/TwistStamped.html)):
  Velocity fused by FCU.
- `~global_position/rel_alt`
  ([std_msgs/msg/Float64](https://docs.ros.org/en/rolling/p/std_msgs/msg/Float64.html)):
  Relative altitude.
- `~global_position/compass_hdg`
  ([std_msgs/msg/Float64](https://docs.ros.org/en/rolling/p/std_msgs/msg/Float64.html)):
  Compass heading in degrees.
- `~global_position/raw/fix`
  ([sensor_msgs/msg/NavSatFix](https://docs.ros.org/en/rolling/p/sensor_msgs/msg/NavSatFix.html)):
  GPS position fix reported by the device.
- `~global_position/raw/gps_vel`
  ([geometry_msgs/msg/TwistStamped](https://docs.ros.org/en/rolling/p/geometry_msgs/msg/TwistStamped.html)):
  Velocity output from the GPS device.

#### Parameters

- `~global_position/frame_id` (`string`, default: `fcu`): frame_id for
  messages.
- `~global_position/tf/send` (`bool`, default: `true`): Send or not
  local UTM coords via TF?
- `~global_position/tf/frame_id` (`string`, default: `local_origin`):
  frame_id for TF.
- `~global_position/tf/child_frame_id` (`string`, default: `fcu_utm`):
  Child frame_id for TF.

### imu_pub

Publish IMU state

#### Published Topics

- `~imu/data`
  ([sensor_msgs/msg/Imu](https://docs.ros.org/en/rolling/p/sensor_msgs/msg/Imu.html)):
  Imu data, orientation computed by FCU
- `~imu/data_raw`
  ([sensor_msgs/msg/Imu](https://docs.ros.org/en/rolling/p/sensor_msgs/msg/Imu.html)):
  Raw IMU data without orientation
- `~imu/mag`
  ([sensor_msgs/msg/MagneticField](https://docs.ros.org/en/rolling/p/sensor_msgs/msg/MagneticField.html)):
  FCU compass data
- `~imu/temperature`
  ([sensor_msgs/msg/Temperature](https://docs.ros.org/en/rolling/p/sensor_msgs/msg/Temperature.html)):
  Temperature reported by FCU (usually from barometer)
- `~imu/atm_pressure`
  ([sensor_msgs/msg/FluidPressure](https://docs.ros.org/en/rolling/p/sensor_msgs/msg/FluidPressure.html)):
  Air pressure.

#### Parameters

- `~imu/frame_id` (`string`, default: `fcu`): Frame ID for this plugin.
- `~imu/linear_acceleration_stdev` (`double`, default: `0.0003`):
  Gyro's standard deviation
- `~imu/angular_velocity_stdev` (`double`, default: `!dec 0.02`):
  Accel's standard deviation
- `~imu/orientation_stdev` (`double`, default: `1.0`): Standard
  deviation for IMU.orientation
- `~imu/magnetic_stdev` (`double`, default: `0.0`): Standard deviation
  for magnetic field message (undefined if: 0.0)

### local_position

Publish LOCAL_POSITION_NED in [TF](https://index.ros.org/p/tf) and
PoseStamped topic.

#### Published Topics

- `~local_position/pose`
  ([geometry_msgs/msg/PoseStamped](https://docs.ros.org/en/rolling/p/geometry_msgs/msg/PoseStamped.html)):
  Local position from FCU.
- `~local_position/velocity`
  ([geometry_msgs/msg/TwistStamped](https://docs.ros.org/en/rolling/p/geometry_msgs/msg/TwistStamped.html)):
  Velocity data from FCU.

#### Parameters

- `~local_position/frame_id` (`string`, default: `fcu`): frame_id for
  message.
- `~local_position/tf/send` (`bool`, default: `true`): TF send switch.
- `~local_position/tf/frame_id` (`string`, default: `local_origin`):
  Origin frame_id for TF.
- `~local_position/tf/child_frame_id` (`string`, default: `fcu`): Child
  frame_id for TF.

### manual_control

Publish MANUAL_CONTROL message (user input).

#### Subscribed Topics

- `~manual_control/send`
  ([mavros_msgs/msg/ManualControl](https://docs.ros.org/en/rolling/p/mavros_msgs/msg/ManualControl.html)):
  RC Rx, interpreted and normalized.

#### Published Topics

- `~manual_control/control`
  ([mavros_msgs/msg/ManualControl](https://docs.ros.org/en/rolling/p/mavros_msgs/msg/ManualControl.html)):
  RC Rx, interpreted and normalized.

### param

Allows to access to FCU parameters and map it to ROS parameters in
`param/`.

#### Services

- `~param/pull`
  ([mavros_msgs/srv/ParamPull](https://docs.ros.org/en/rolling/p/mavros_msgs/srv/ParamPull.html)):
  Request parameter from device (or internal cache).
- `~param/push`
  ([mavros_msgs/srv/ParamPush](https://docs.ros.org/en/rolling/p/mavros_msgs/srv/ParamPush.html)):
  Request send parameters from ROS to FCU.
- `~param/get`
  ([mavros_msgs/srv/ParamGet](https://docs.ros.org/en/rolling/p/mavros_msgs/srv/ParamGet.html)):
  Return FCU parameter value.
- `~param/set`
  ([mavros_msgs/srv/ParamSet](https://docs.ros.org/en/rolling/p/mavros_msgs/srv/ParamSet.html)):
  Set parameter on FCU immidiatly.

### rc_io

Publish RC receiver inputs.

#### Subscribed Topics

- `~rc/override`
  ([mavros_msgs/msg/OverrideRCIn](https://docs.ros.org/en/rolling/p/mavros_msgs/msg/OverrideRCIn.html)):
  Send RC override message to FCU. **APM** and **PX4** only. APM
  requires setup FCU param `SYSID_MYGCS` to match mavros system id.
  **Not recommended** to use in automatic control because lack of safety
  mechanisms. Use one of setpoint plugins and OFFBOARD mode.

#### Published Topics

- `~rc/in`
  ([mavros_msgs/msg/RCIn](https://docs.ros.org/en/rolling/p/mavros_msgs/msg/RCIn.html)):
  Publish RC inputs (in raw milliseconds)
- `~rc/out`
  ([mavros_msgs/msg/RCOut](https://docs.ros.org/en/rolling/p/mavros_msgs/msg/RCOut.html)):
  Publish FCU servo outputs

### safety_area

Sends safety allowed area to FCU. Initial area can be loaded from
parameters.

#### Subscribed Topics

- `~safety_area/set`
  ([geometry_msgs/msg/PolygonStamped](https://docs.ros.org/en/rolling/p/geometry_msgs/msg/PolygonStamped.html)):
  Volumetric area described by two corners.

#### Parameters

- `~safety_area/p1/x` (`double`): Corner 1 X.
- `~safety_area/p1/y` (`double`): Corner 1 Y.
- `~safety_area/p1/z` (`double`): Corner 1 Z.
- `~safety_area/p2/x` (`double`): Corner 2 X.
- `~safety_area/p2/y` (`double`): Corner 2 Y.
- `~safety_area/p2/z` (`double`): Corner 2 Z.

### setpoint_accel

Send acceleration setpoint.

#### Subscribed Topics

- `~setpoint_accel/accel`
  ([geometry_msgs/msg/Vector3Stamped](https://docs.ros.org/en/rolling/p/geometry_msgs/msg/Vector3Stamped.html)):
  Acceleration or force setpoint vector.

#### Parameters

- `~setpoint_accel/send_force` (`bool`): Send force setpoint.

### setpoint_attitude

Send attitude setpoint using SET_ATTITUDE_TARGET.

#### Subscribed Topics

- `~setpoint_attitude/cmd_vel`
  ([geometry_msgs/msg/TwistStamped](https://docs.ros.org/en/rolling/p/geometry_msgs/msg/TwistStamped.html)):
  Send angular velocity.
- `~setpoint_attitude/attitude`
  ([geometry_msgs/msg/PoseStamped](https://docs.ros.org/en/rolling/p/geometry_msgs/msg/PoseStamped.html)):
  Send attitude setpoint.
- `~setpoint_attitude/thrust`
  ([mavros_msgs/msg/Thrust](https://docs.ros.org/en/rolling/p/mavros_msgs/msg/Thrust.html)):
  Send throttle value(01).

#### Parameters

- `~setpoint_attitude/reverse_throttle` (`bool`, default: `false`):
  Allow to send -1.0 throttle or not.
- `~setpoint_attitude/use_quaternion` (`bool`, default: `false`): Enable
  setpoint_attitude/target_attitude PoseStamped topic subscriber and
  disable setpoint_attitude/cmd_vel Twist topic.
- `~setpoint_attitude/tf/listen` (`bool`, default: `false`): TF listen
  switch. Disable topics if enabled.
- `~setpoint_attutude/tf/frame_id` (`string`, default: `local_origin`):
  Origin frame_id for TF.
- `~setpoint_attitude/tf/child_frame_id` (`string`, default:
  `attitude`): Child frame_id for TF.
- `~setpoint_attitude/tf/rate_limit` (`double`, default: `10.0`): Rate
  limit for TF listener \[Hz\].

### setpoint_position

Sends position setpoint using SET_POSITION_TARGET_GLOBAL_INT or
SET_POSITION_TARGET_LOCAL_NED.

#### Subscribed Topics

- `~setpoint_position/global`
  ([geographic_msgs/msg/GeoPoseStamped](https://docs.ros.org/en/rolling/p/geographic_msgs/msg/GeoPoseStamped.html)):
  Global frame setpoint position. Sends an LLA to the flight controller.
  Only YAW axis extracted from orientation field. **IMPORTANT:**
  Altitude is interpreted as AMSL and care must be taken to avoid a
  common pitfall.
  [See this section for more](https://wiki.ros.org/mavros#mavros.2FPlugins.Avoiding_Pitfalls_Related_to_Ellipsoid_Height_and_Height_Above_Mean_Sea_Level).
- `~setpoint_position/local`
  ([geometry_msgs/msg/PoseStamped](https://docs.ros.org/en/rolling/p/geometry_msgs/msg/PoseStamped.html)):
  Local frame setpoint position. Only YAW axis extracted from
  orientation field.
- `~setpoint_position/global_to_local`
  ([geographic_msgs/msg/GeoPoseStamped](https://docs.ros.org/en/rolling/p/geographic_msgs/msg/GeoPoseStamped.html)):
  The old implementation of `setpoint_position/global`. Converts LLA
  to local ENU. This was done as a workaround before the flight
  controller could accept LLA setpoints directly. Consider using
  `setpoint_position/global` instead.
  [See the details here](https://github.com/mavlink/mavros/pull/1306).
  Only YAW axis extracted from orientation field.

#### Parameters

- `~setpoint_position/tf/listen` (`bool`, default: `false`): TF listen
  switch. Disable topic if enabled.
- `~setpoint_position/tf/frame_id` (`string`, default: `local_origin`):
  Origin frame_id for TF.
- `~setpoint_position/tf/child_frame_id` (`string`, default:
  `setpoint`): Child frame_id for TF.
- `~setpoint_position/tf/rate_limit` (`double`, default: `50.0`): Rate
  limit for TF listener \[Hz\].

### setpoint_raw

Send RAW setpoint messages to FCU and provide loopback topics (PX4).

#### Subscribed Topics

- `~setpoint_raw/local`
  ([mavros_msgs/msg/PositionTarget](https://docs.ros.org/en/rolling/p/mavros_msgs/msg/PositionTarget.html)):
  Local position, velocity and acceleration setpoint.
- `~setpoint_raw/global`
  ([mavros_msgs/msg/GlobalPositionTarget](https://docs.ros.org/en/rolling/p/mavros_msgs/msg/GlobalPositionTarget.html)):
  Global position, velocity and acceleration setpoint.
- `~setpoint_raw/attitude`
  ([mavros_msgs/msg/AttitudeTarget](https://docs.ros.org/en/rolling/p/mavros_msgs/msg/AttitudeTarget.html)):
  Attitude, angular rate and thrust setpoint.

#### Published Topics

- `~setpoint_raw/target_local`
  ([mavros_msgs/msg/PositionTarget](https://docs.ros.org/en/rolling/p/mavros_msgs/msg/PositionTarget.html)):
  Local target loopback.
- `~setpoint_raw/target_global`
  ([mavros_msgs/msg/GlobalPositionTarget](https://docs.ros.org/en/rolling/p/mavros_msgs/msg/GlobalPositionTarget.html)):
  Global target loopback.
- `~setpoint_raw/target_attitude`
  ([mavros_msgs/msg/AttitudeTarget](https://docs.ros.org/en/rolling/p/mavros_msgs/msg/AttitudeTarget.html)):
  Attitude target loopback.

### setpoint_velocity

Send velocity setpoint to FCU.

#### Subscribed Topics

- `~setpoint_velocity/cmd_vel_unstamped`
  ([geometry_msgs/msg/Twist](https://docs.ros.org/en/rolling/p/geometry_msgs/msg/Twist.html)):
  Velocity setpoint.

### sys_status

System status plugin. Handles FCU detection. **REQUIRED** never
blacklist it!.

#### Published Topics

- `~state`
  ([mavros_msgs/msg/State](https://docs.ros.org/en/rolling/p/mavros_msgs/msg/State.html)):
  FCU state
- `~battery`
  ([mavros_msgs/msg/BatteryStatus](https://docs.ros.org/en/rolling/p/mavros_msgs/msg/BatteryStatus.html)):
  FCU battery status report. **DEPRECATED**
- `~battery`
  ([sensor_msgs/msg/BatteryState](https://docs.ros.org/en/rolling/p/sensor_msgs/msg/BatteryState.html)):
  FCU battery status report.
- `~extended_state`
  ([mavros_msgs/msg/ExtendedState](https://docs.ros.org/en/rolling/p/mavros_msgs/msg/ExtendedState.html)):
  Landing detector and VTOL state.

#### Services

- `~set_stream_rate`
  ([mavros_msgs/srv/StreamRate](https://docs.ros.org/en/rolling/p/mavros_msgs/srv/StreamRate.html)):
  Send stream rate request to FCU.
- `~set_mode`
  ([mavros_msgs/srv/SetMode](https://docs.ros.org/en/rolling/p/mavros_msgs/srv/SetMode.html)):
  Set FCU operation mode. See custom mode identifiers at
  [modes page](#custommodes).

#### Parameters

- `~conn/timeout` (`double`, default: `30.0`): Connection time out in
  seconds.
- `~conn/heartbeat_rate` (`double`, default: `0.0`): Send HEARTBEAT
  message rate \[Hz\] (or disabled if 0.0)
- `~sys/min_voltage` (`double`, default: `6.0`): Minimal battery voltage
  for diagnostics.
- `~sys/disable_diag` (`bool`, default: `false`): Disable all diag
  except HEARTBEAT message.

### sys_time

System time plugin. Does time syncronization on **PX4**.

#### Published Topics

- `~time_reference`
  ([sensor_msgs/msg/TimeReference](https://docs.ros.org/en/rolling/p/sensor_msgs/msg/TimeReference.html)):
  Time reference computed from SYSTEM_TIME.

#### Parameters

- `~conn/system_time_rate` (`double`, default: `0.0`): Send
  `SYSTEM_TIME` to device rate \[Hz\] (disabled if 0.0).
- `~conn/timesync_rate` (`double`, default: `0.0`): TIMESYNC rate.
  **PX4** only.
- `~time/time_ref_source` (`string`, default: `"fcu"`): Ref source for
  time_reference message.
- `~time/timesync_avg_alpha` (`double`, default: `0.6`): Alpha for
  exponential moving average.

### vfr_hud

Publish VFR_HUD and WIND messages.

#### Published Topics

- `~vfr_hud`
  ([mavros_msgs/msg/VFR_HUD](https://docs.ros.org/en/rolling/p/mavros_msgs/msg/VFR_HUD.html)):
  Data for HUD.
- `~wind_estimation`
  ([geometry_msgs/msg/TwistStamped](https://docs.ros.org/en/rolling/p/geometry_msgs/msg/TwistStamped.html)):
  Wind estimation from FCU (**APM**).

### waypoint

Allows to access to FCU mission (waypoints).

#### Published Topics

- `~mission/reached`
  ([mavros_msgs/msg/WaypointReached](https://docs.ros.org/en/rolling/p/mavros_msgs/msg/WaypointReached.html)):
  Publishes on reaching a waypoint from MISSION_ITEM_REACHED message.
- `~mission/waypoints`
  ([mavros_msgs/msg/WaypointList](https://docs.ros.org/en/rolling/p/mavros_msgs/msg/WaypointList.html)):
  Current waypoint table. Updates on changes.

#### Services

- `~mission/pull`
  ([mavros_msgs/srv/WaypointPull](https://docs.ros.org/en/rolling/p/mavros_msgs/srv/WaypointPull.html)):
  Request update waypoint list.
- `~mission/push`
  ([mavros_msgs/srv/WaypointPush](https://docs.ros.org/en/rolling/p/mavros_msgs/srv/WaypointPush.html)):
  Send new waypoint table.
- `~mission/clear`
  ([mavros_msgs/srv/WaypointClear](https://docs.ros.org/en/rolling/p/mavros_msgs/srv/WaypointClear.html)):
  Clear mission on FCU.
- `~mission/set_current`
  ([mavros_msgs/srv/WaypointSetCurrent](https://docs.ros.org/en/rolling/p/mavros_msgs/srv/WaypointSetCurrent.html)):
  Set current seq. number in list.

#### Parameters

- `~mission/pull_after_gcs` (`bool`, default: `false`): Defines pull or
  not waypoints if detected GCS activity.

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

#### sys_status

Handles SYSTEM_STATUS and HEARTBEAT messages. Changes
UAS.connection_status().

##### Published Topics

- `~state`
  ([mavros/msg/State](https://docs.ros.org/en/rolling/p/mavros/msg/State.html)):
  FCU state
- `~battery`
  ([mavros/msg/BatteryStatus](https://docs.ros.org/en/rolling/p/mavros/msg/BatteryStatus.html)):
  FCU battery status report.

##### Services

- `~set_stream_rate`
  ([mavros/srv/StreamRate](https://docs.ros.org/en/rolling/p/mavros/srv/StreamRate.html)):
  Send stream rate request to FCU. (Since 0.5.0)

##### Parameters

- `~conn_timeout` (`double`, default: `30.0`): Connection time out in
  seconds.
- `~conn_heartbeat` (`double`, default: `0.0`): Period to send HEARTBEAT
  messages (or disabled if 0.0)
- `~sys/min_voltage` (`double`, default: `6.0`): Minimal battery voltage
  for diagnostics.

#### imu_pub

Publish IMU state

##### Published Topics

- `~imu/data`
  ([sensor_msgs/msg/Imu](https://docs.ros.org/en/rolling/p/sensor_msgs/msg/Imu.html)):
  Imu data, orientation computed by FCU
- `~imu/data_raw`
  ([sensor_msgs/msg/Imu](https://docs.ros.org/en/rolling/p/sensor_msgs/msg/Imu.html)):
  Raw IMU data without orientation
- `~imu/mag`
  ([sensor_msgs/msg/MagneticField](https://docs.ros.org/en/rolling/p/sensor_msgs/msg/MagneticField.html)):
  FCU compass data
- `~imu/temperature`
  ([sensor_msgs/msg/Temperature](https://docs.ros.org/en/rolling/p/sensor_msgs/msg/Temperature.html)):
  Temperature reported by FCU (usually from barometer)
- `~imu/atm_pressure`
  ([sensor_msgs/msg/FluidPressure](https://docs.ros.org/en/rolling/p/sensor_msgs/msg/FluidPressure.html)):
  Air pressure.

##### Parameters

- `~imu/frame_id` (`string`, default: `fcu`): Frame ID for this plugin.
- `~imu/linear_acceleration_stdev` (`double`, default: `0.0003`):
  Gyro's standard deviation
- `~imu/angular_velocity_stdev` (`double`, default: `!dec 0.02`):
  Accel's standard deviation
- `~imu/orientation_stdev` (`double`, default: `1.0`): Standard
  deviation for IMU.orientation
- `~imu/magnetic_stdev` (default: `0.0`): Standard deviation for
  magnetic field message (undefined if: 0.0) (Since 0.6.0)

#### gps

Publish GPS Fix (like
[nmea_navsat_driver](https://index.ros.org/p/nmea_navsat_driver))

##### Published Topics

- `~fix`
  ([sensor_msgs/msg/NavSatFix](https://docs.ros.org/en/rolling/p/sensor_msgs/msg/NavSatFix.html)):
  GPS position fix reported by the device.
- `~time_reference`
  ([sensor_msgs/msg/TimeReference](https://docs.ros.org/en/rolling/p/sensor_msgs/msg/TimeReference.html)):
  Time reference computed from SYSTEM_TIME.
- `~gps_vel`
  ([geometry_msgs/msg/TwistStamped](https://docs.ros.org/en/rolling/p/geometry_msgs/msg/TwistStamped.html)):
  Velocity output from the GPS device.

##### Parameters

- `~gps/frame_id` (`string`, default: `gps`): Frame ID for fix message.
- `~gps/time_ref_source` (`string`, default: `same as ~gps/frame_id`):
  Ref source for time_reference message.

#### param

Allows to access to FCU parameters and map it to ROS parameters in
`param/`.

##### Services

- `~param/pull`
  ([mavros/srv/ParamPull](https://docs.ros.org/en/rolling/p/mavros/srv/ParamPull.html)):
  Request parameter from device (or internal cache).
- `~param/push`
  ([mavros/srv/ParamPush](https://docs.ros.org/en/rolling/p/mavros/srv/ParamPush.html)):
  Request send parameters from ROS to FCU.
- `~param/get`
  ([mavros/srv/ParamGet](https://docs.ros.org/en/rolling/p/mavros/srv/ParamGet.html)):
  Return FCU parameter value.
- `~param/set`
  ([mavros/srv/ParamSet](https://docs.ros.org/en/rolling/p/mavros/srv/ParamSet.html)):
  Set parameter on FCU immidiatly.

#### waypoint

Allows to access to FCU mission (waypoints).

##### Published Topics

- `~mission/waypoints`
  ([mavros/msg/WaypointList](https://docs.ros.org/en/rolling/p/mavros/msg/WaypointList.html)):
  Current waypoint table. Updates on changes.

##### Services

- `~mission/pull`
  ([mavros/srv/WaypointPull](https://docs.ros.org/en/rolling/p/mavros/srv/WaypointPull.html)):
  Request update waypoint list.
- `~mission/push`
  ([mavros/srv/WaypointPush](https://docs.ros.org/en/rolling/p/mavros/srv/WaypointPush.html)):
  Send new waypoint table.
- `~mission/clear`
  ([mavros/srv/WaypointClear](https://docs.ros.org/en/rolling/p/mavros/srv/WaypointClear.html)):
  Clear mission on FCU.
- `~mission/set_current`
  ([mavros/srv/WaypointSetCurrent](https://docs.ros.org/en/rolling/p/mavros/srv/WaypointSetCurrent.html)):
  Set current seq. number in list.
- `~mission/goto`
  ([mavros/srv/WaypointGOTO](https://docs.ros.org/en/rolling/p/mavros/srv/WaypointGOTO.html)):
  Send goto point (APM specific).

##### Parameters

- `~mission/pull_after_gcs` (`bool`, default: `false`): Defines pull or
  not waypoints if detected GCS activity.

#### rc_io

Publish RC receiver inputs.

##### Published Topics

- `~rc/in`
  ([mavros/msg/RCIn](https://docs.ros.org/en/rolling/p/mavros/msg/RCIn.html)):
  Publish RC inputs (in raw milliseconds)
- `~rc/out`
  ([mavros/msg/RCOut](https://docs.ros.org/en/rolling/p/mavros/msg/RCOut.html)):
  Publish FCU servo outputs

##### Services

- `~rc/override`
  ([mavros/srv/OverrideRCIn](https://docs.ros.org/en/rolling/p/mavros/srv/OverrideRCIn.html)):
  Send RC override message to FCU (Since 0.5.0)

#### command

Send COMMAND_LONG to FCU.

##### Services

- `~cmd/command`
  ([mavros/srv/CommandLong](https://docs.ros.org/en/rolling/p/mavros/srv/CommandLong.html)):
  Send any COMMAND_LONG to FCU.
- `~cmd/arming`
  ([mavros/srv/CommandBool](https://docs.ros.org/en/rolling/p/mavros/srv/CommandBool.html)):
  Change Arming status.
- `~cmd/set_mode`
  ([mavros/srv/CommandMode](https://docs.ros.org/en/rolling/p/mavros/srv/CommandMode.html)):
  Change FCU operation mode.
- `~cmd/set_home`
  ([mavros/srv/CommandHome](https://docs.ros.org/en/rolling/p/mavros/srv/CommandHome.html)):
  Change HOME location.

#### local_position

Publish LOCAL_POSITION_NED in [TF](https://index.ros.org/p/tf) and
PoseStamped topic. (Since 0.6.0)

##### Published Topics

- `~position/local`
  ([geometry_msgs/msg/PoseStamped](https://docs.ros.org/en/rolling/p/geometry_msgs/msg/PoseStamped.html)):
  Local position from FCU.

##### Parameters

- `~position/local/send_tf` (`bool`, default: `true`): TF send switch.
- `~position/local/frame_id` (`string`, default: `local_origin`): Origin
  frame_id for TF.
- `~position/local/child_frame_id` (`string`, default: `fcu`): Child
  frame_id for TF and PoseStamped.

#### vision_position

Sent VISION_POSITION_ESTIMATE to FCU from PoseStamped topic. (Since
0.6.0)

##### Subscribed Topics

- `~position/vision`
  ([geometry_msgs/msg/PoseStamped](https://docs.ros.org/en/rolling/p/geometry_msgs/msg/PoseStamped.html)):
  Vision position.
- `~position/vision`
  ([geometry_msgs/msg/PoseWithCovarianceStamped](https://docs.ros.org/en/rolling/p/geometry_msgs/msg/PoseWithCovarianceStamped.html)):
  Vision position with covariance (optional alternative).

##### Parameters

- `~position/vision/pose_with_covariance` (`bool`, default: `false`):
  Selector for vision position message type.
- `~position/vision/listen_tf` (`bool`, default: `false`): TF listen
  switch. Disable topic if enabled.
- `~position/vision/frame_id` (`string`, default: `local_origin`):
  Origin frame_id for TF.
- `~position/vision/child_frame_id` (`string`, default: `vision`): Child
  frame_id for TF.
- `~position/vision/tf_rate_limit` (`double`, default: `50.0`): Rate
  limit for TF listener \[Hz\]. (Since **UPCOMING**)

#### setpoint_position

Sent LOCAL_NED_POSITION_SETPOINT_EXTERNAL to FCU. (Since 0.6.0)

##### Subscribed Topics

- `~position/local_setpoint`
  ([geometry_msgs/msg/PoseStamped](https://docs.ros.org/en/rolling/p/geometry_msgs/msg/PoseStamped.html)):
  Setpoint position. Orientation not used.

##### Parameters

- `~position/setpoint/listen_tf` (`bool`, default: `false`): TF listen
  switch. Disable topic if enabled.
- `~position/setpoint/frame_id` (`string`, default: `local_origin`):
  Origin frame_id for TF.
- `~position/setpoint/child_frame_id` (`string`, default: `setpoint`):
  Child frame_id for TF.
- `~position/setpoint/tf_rate_limit` (`double`, default: `50.0`): Rate
  limit for TF listener \[Hz\]. (Since **UPCOMING**)

#### safety_area

Sends safety allowed area to FCU. Initial area can be loaded from
parameters. (Since **UPCOMING**)

##### Subscribed Topics

- `~safety_area/set`
  ([geometry_msgs/msg/PolygonStamped](https://docs.ros.org/en/rolling/p/geometry_msgs/msg/PolygonStamped.html)):
  Volumetric area described by two corners.

##### Parameters

- `~safety_area/p1/x` (`double`): Corner 1 X.
- `~safety_area/p1/y` (`double`): Corner 1 Y.
- `~safety_area/p1/z` (`double`): Corner 1 Z.
- `~safety_area/p2/x` (`double`): Corner 2 X.
- `~safety_area/p2/y` (`double`): Corner 2 Y.
- `~safety_area/p2/z` (`double`): Corner 2 Z.

## Plugins_0.7

### Plugins for mavros 0.7

Standard plugin set for mavros version 0.7.

#### sys_status

Handles SYSTEM_STATUS and HEARTBEAT messages. Changes
UAS.connection_status().

##### Published Topics

- `~state`
  ([mavros/msg/State](https://docs.ros.org/en/rolling/p/mavros/msg/State.html)):
  FCU state
- `~battery`
  ([mavros/msg/BatteryStatus](https://docs.ros.org/en/rolling/p/mavros/msg/BatteryStatus.html)):
  FCU battery status report.

##### Services

- `~set_stream_rate`
  ([mavros/srv/StreamRate](https://docs.ros.org/en/rolling/p/mavros/srv/StreamRate.html)):
  Send stream rate request to FCU. (Since 0.5.0)

##### Parameters

- `~conn_timeout` (`double`, default: `30.0`): Connection time out in
  seconds.
- `~conn_heartbeat` (`double`, default: `0.0`): Period to send HEARTBEAT
  messages (or disabled if 0.0)
- `~sys/min_voltage` (`double`, default: `6.0`): Minimal battery voltage
  for diagnostics.

#### imu_pub

Publish IMU state

##### Published Topics

- `~imu/data`
  ([sensor_msgs/msg/Imu](https://docs.ros.org/en/rolling/p/sensor_msgs/msg/Imu.html)):
  Imu data, orientation computed by FCU
- `~imu/data_raw`
  ([sensor_msgs/msg/Imu](https://docs.ros.org/en/rolling/p/sensor_msgs/msg/Imu.html)):
  Raw IMU data without orientation
- `~imu/mag`
  ([sensor_msgs/msg/MagneticField](https://docs.ros.org/en/rolling/p/sensor_msgs/msg/MagneticField.html)):
  FCU compass data
- `~imu/temperature`
  ([sensor_msgs/msg/Temperature](https://docs.ros.org/en/rolling/p/sensor_msgs/msg/Temperature.html)):
  Temperature reported by FCU (usually from barometer)
- `~imu/atm_pressure`
  ([sensor_msgs/msg/FluidPressure](https://docs.ros.org/en/rolling/p/sensor_msgs/msg/FluidPressure.html)):
  Air pressure.

##### Parameters

- `~imu/frame_id` (`string`, default: `fcu`): Frame ID for this plugin.
- `~imu/linear_acceleration_stdev` (`double`, default: `0.0003`):
  Gyro's standard deviation
- `~imu/angular_velocity_stdev` (`double`, default: `!dec 0.02`):
  Accel's standard deviation
- `~imu/orientation_stdev` (`double`, default: `1.0`): Standard
  deviation for IMU.orientation
- `~imu/magnetic_stdev` (default: `0.0`): Standard deviation for
  magnetic field message (undefined if: 0.0)

#### gps

Publish GPS Fix (like
[nmea_navsat_driver](https://index.ros.org/p/nmea_navsat_driver))

##### Published Topics

- `~fix`
  ([sensor_msgs/msg/NavSatFix](https://docs.ros.org/en/rolling/p/sensor_msgs/msg/NavSatFix.html)):
  GPS position fix reported by the device.
- `~time_reference`
  ([sensor_msgs/msg/TimeReference](https://docs.ros.org/en/rolling/p/sensor_msgs/msg/TimeReference.html)):
  Time reference computed from SYSTEM_TIME.
- `~gps_vel`
  ([geometry_msgs/msg/TwistStamped](https://docs.ros.org/en/rolling/p/geometry_msgs/msg/TwistStamped.html)):
  Velocity output from the GPS device.

##### Parameters

- `~gps/frame_id` (`string`, default: `gps`): Frame ID for fix message.
- `~gps/time_ref_source` (`string`, default: `same as ~gps/frame_id`):
  Ref source for time_reference message.

#### param

Allows to access to FCU parameters and map it to ROS parameters in
`param/`.

##### Services

- `~param/pull`
  ([mavros/srv/ParamPull](https://docs.ros.org/en/rolling/p/mavros/srv/ParamPull.html)):
  Request parameter from device (or internal cache).
- `~param/push`
  ([mavros/srv/ParamPush](https://docs.ros.org/en/rolling/p/mavros/srv/ParamPush.html)):
  Request send parameters from ROS to FCU.
- `~param/get`
  ([mavros/srv/ParamGet](https://docs.ros.org/en/rolling/p/mavros/srv/ParamGet.html)):
  Return FCU parameter value.
- `~param/set`
  ([mavros/srv/ParamSet](https://docs.ros.org/en/rolling/p/mavros/srv/ParamSet.html)):
  Set parameter on FCU immidiatly.

#### waypoint

Allows to access to FCU mission (waypoints).

##### Published Topics

- `~mission/waypoints`
  ([mavros/msg/WaypointList](https://docs.ros.org/en/rolling/p/mavros/msg/WaypointList.html)):
  Current waypoint table. Updates on changes.

##### Services

- `~mission/pull`
  ([mavros/srv/WaypointPull](https://docs.ros.org/en/rolling/p/mavros/srv/WaypointPull.html)):
  Request update waypoint list.
- `~mission/push`
  ([mavros/srv/WaypointPush](https://docs.ros.org/en/rolling/p/mavros/srv/WaypointPush.html)):
  Send new waypoint table.
- `~mission/clear`
  ([mavros/srv/WaypointClear](https://docs.ros.org/en/rolling/p/mavros/srv/WaypointClear.html)):
  Clear mission on FCU.
- `~mission/set_current`
  ([mavros/srv/WaypointSetCurrent](https://docs.ros.org/en/rolling/p/mavros/srv/WaypointSetCurrent.html)):
  Set current seq. number in list.
- `~mission/goto`
  ([mavros/srv/WaypointGOTO](https://docs.ros.org/en/rolling/p/mavros/srv/WaypointGOTO.html)):
  Send goto point (APM specific).

##### Parameters

- `~mission/pull_after_gcs` (`bool`, default: `false`): Defines pull or
  not waypoints if detected GCS activity.

#### rc_io

Publish RC receiver inputs.

##### Published Topics

- `~rc/in`
  ([mavros/msg/RCIn](https://docs.ros.org/en/rolling/p/mavros/msg/RCIn.html)):
  Publish RC inputs (in raw milliseconds)
- `~rc/out`
  ([mavros/msg/RCOut](https://docs.ros.org/en/rolling/p/mavros/msg/RCOut.html)):
  Publish FCU servo outputs
- `~rc/override`
  ([mavros/msg/OverrideRCIn](https://docs.ros.org/en/rolling/p/mavros/msg/OverrideRCIn.html)):
  Send RC override message to FCU. This topic replace override service.

#### command

Send COMMAND_LONG to FCU.

##### Services

- `~cmd/command`
  ([mavros/srv/CommandLong](https://docs.ros.org/en/rolling/p/mavros/srv/CommandLong.html)):
  Send any COMMAND_LONG to FCU.
- `~cmd/arming`
  ([mavros/srv/CommandBool](https://docs.ros.org/en/rolling/p/mavros/srv/CommandBool.html)):
  Change Arming status.
- `~cmd/set_mode`
  ([mavros/srv/CommandMode](https://docs.ros.org/en/rolling/p/mavros/srv/CommandMode.html)):
  Change FCU operation mode.
- `~cmd/set_home`
  ([mavros/srv/CommandHome](https://docs.ros.org/en/rolling/p/mavros/srv/CommandHome.html)):
  Change HOME location.

#### local_position

Publish LOCAL_POSITION_NED in [TF](https://index.ros.org/p/tf) and
PoseStamped topic.

##### Published Topics

- `~position/local`
  ([geometry_msgs/msg/PoseStamped](https://docs.ros.org/en/rolling/p/geometry_msgs/msg/PoseStamped.html)):
  Local position from FCU.

##### Parameters

- `~position/local/send_tf` (`bool`, default: `true`): TF send switch.
- `~position/local/frame_id` (`string`, default: `local_origin`): Origin
  frame_id for TF.
- `~position/local/child_frame_id` (`string`, default: `fcu`): Child
  frame_id for TF and PoseStamped.

#### vision_position

Sent VISION_POSITION_ESTIMATE to FCU from PoseStamped topic.

##### Subscribed Topics

- `~position/vision`
  ([geometry_msgs/msg/PoseStamped](https://docs.ros.org/en/rolling/p/geometry_msgs/msg/PoseStamped.html)):
  Vision position.
- `~position/vision`
  ([geometry_msgs/msg/PoseWithCovarianceStamped](https://docs.ros.org/en/rolling/p/geometry_msgs/msg/PoseWithCovarianceStamped.html)):
  Vision position with covariance (optional alternative).

##### Parameters

- `~position/vision/pose_with_covariance` (`bool`, default: `false`):
  Selector for vision position message type.
- `~position/vision/listen_tf` (`bool`, default: `false`): TF listen
  switch. Disable topic if enabled.
- `~position/vision/frame_id` (`string`, default: `local_origin`):
  Origin frame_id for TF.
- `~position/vision/child_frame_id` (`string`, default: `vision`): Child
  frame_id for TF.
- `~position/vision/tf_rate_limit` (`double`, default: `50.0`): Rate
  limit for TF listener \[Hz\]. (Since **UPCOMING**)

#### setpoint_accel

Send acceleration setpoint to FCU.

##### Subscribed Topics

- `~setpoint/accel`
  ([geometry_msgs/msg/Vector3](https://docs.ros.org/en/rolling/p/geometry_msgs/msg/Vector3.html)):
  Acceleration or force setpoint vector.

##### Parameters

- `~setpoint/accel/send_force` (`bool`): Send force setpoint.

#### setpoint_attitude

Send ATTITUDE_SETPOINT_EXTERNAL to FCU.

##### Subscribed Topics

- `~setpoint/att_vel`
  ([geometry_msgs/msg/Twist](https://docs.ros.org/en/rolling/p/geometry_msgs/msg/Twist.html)):
  Send angular velocity.
- `~setpoint/attitude`
  ([geometry_msgs/msg/PoseStamped](https://docs.ros.org/en/rolling/p/geometry_msgs/msg/PoseStamped.html)):
  Send attitude setpoint.
- `~setpoint/attitude`
  ([geometry_msgs/msg/PoseWithCovarianceStamped](https://docs.ros.org/en/rolling/p/geometry_msgs/msg/PoseWithCovarianceStamped.html)):
  Send attitude setpoint with covariance (alternative).

##### Parameters

- `~setpoint/attitude/listen_tf` (`bool`, default: `false`): TF listen
  switch. Disable topics if enabled.
- `~setpoint/attitude/listen_twist` (`bool`, default: `false`): Use
  att_vel topic instead of attitude.
- `~setpoint/attitude/pose_with_covariance` (`bool`, default: `false`):
  Selector for attitude message type.
- `~setpoint/attitude/frame_id` (`string`, default: `local_origin`):
  Origin frame_id for TF.
- `~setpoint/attitude/child_frame_id` (`string`, default: `attitude`):
  Child frame_id for TF.
- `~setpoint/attitude/tf_rate_limit` (`double`, default: `10.0`): Rate
  limit for TF listener \[Hz\].

#### setpoint_position

Sent LOCAL_NED_POSITION_SETPOINT_EXTERNAL to FCU.

##### Subscribed Topics

- `~setpoint/local_setpoint`
  ([geometry_msgs/msg/PoseStamped](https://docs.ros.org/en/rolling/p/geometry_msgs/msg/PoseStamped.html)):
  Setpoint position. Orientation not used.

##### Parameters

- `~setpoint/position/listen_tf` (`bool`, default: `false`): TF listen
  switch. Disable topic if enabled.
- `~setpoint/position/frame_id` (`string`, default: `local_origin`):
  Origin frame_id for TF.
- `~setpoint/position/child_frame_id` (`string`, default: `setpoint`):
  Child frame_id for TF.
- `~setpoint/position/tf_rate_limit` (`double`, default: `50.0`): Rate
  limit for TF listener \[Hz\].

#### setpoint_velocity

Send velocity setpoint to FCU.

##### Subscribed Topics

- `~setpoint/cmd_vel`
  ([geometry_msgs/msg/Twist](https://docs.ros.org/en/rolling/p/geometry_msgs/msg/Twist.html)):
  Velocity setpoint.

#### safety_area

Sends safety allowed area to FCU. Initial area can be loaded from
parameters.

##### Subscribed Topics

- `~safety_area/set`
  ([geometry_msgs/msg/PolygonStamped](https://docs.ros.org/en/rolling/p/geometry_msgs/msg/PolygonStamped.html)):
  Volumetric area described by two corners.

##### Parameters

- `~safety_area/p1/x` (`double`): Corner 1 X.
- `~safety_area/p1/y` (`double`): Corner 1 Y.
- `~safety_area/p1/z` (`double`): Corner 1 Z.
- `~safety_area/p2/x` (`double`): Corner 2 X.
- `~safety_area/p2/y` (`double`): Corner 2 Y.
- `~safety_area/p2/z` (`double`): Corner 2 Z.

#### 3dr_radio

Publish 3DR Radio status to diagnostics and topic.

##### Published Topics

- `~radio_status`
  ([mavros/msg/RadioStatus](https://docs.ros.org/en/rolling/p/mavros/msg/RadioStatus.html)):
  Status received from modem, same as RADIO_STATUS message.

#### vision_speed

Send vision speed estimates to FCU.

##### Subscribed Topics

- `~vision_speed/speed_vector`
  ([geometry_msgs/msg/Vector3Stamped](https://docs.ros.org/en/rolling/p/geometry_msgs/msg/Vector3Stamped.html)):
  Send speed vector.
- `~vision_speed/speed_twist`
  ([geometry_msgs/msg/TwistStamped](https://docs.ros.org/en/rolling/p/geometry_msgs/msg/TwistStamped.html)):
  Send linear speed. (alternative)

##### Parameters

- `~vision_speed/listen_twist` (`bool`, default: `false`): Topic type
  selector.

#### Notes

Setpoint plugins are mutually exclusive, please blacklist all unused
plugins. Also APM does not support this commands.

Also blacklist `3dr_radio` if you dont use 3DR Radio for FCU
connection.

## Plugins_0.8

### Plugins for mavros 0.8

Standard plugin set for mavros version 0.8.

#### sys_status

Handles SYSTEM_STATUS and HEARTBEAT messages. Changes
UAS.connection_status().

##### Published Topics

- `~state`
  ([mavros/msg/State](https://docs.ros.org/en/rolling/p/mavros/msg/State.html)):
  FCU state
- `~battery`
  ([mavros/msg/BatteryStatus](https://docs.ros.org/en/rolling/p/mavros/msg/BatteryStatus.html)):
  FCU battery status report.

##### Services

- `~set_stream_rate`
  ([mavros/srv/StreamRate](https://docs.ros.org/en/rolling/p/mavros/srv/StreamRate.html)):
  Send stream rate request to FCU. (Since 0.5.0)
- `~set_mode`
  ([mavros/srv/SetMode](https://docs.ros.org/en/rolling/p/mavros/srv/SetMode.html)):
  Set FCU operation mode. See custom mode identifiers at
  [modes page](#fcumodes).

##### Parameters

- `~conn_timeout` (`double`, default: `30.0`): Connection time out in
  seconds.
- `~conn_heartbeat` (`double`, default: `0.0`): Period to send HEARTBEAT
  messages (or disabled if 0.0)
- `~sys/min_voltage` (`double`, default: `6.0`): Minimal battery voltage
  for diagnostics.
- `~sys/disable_diag` (`bool`, default: `false`): Disable all diag
  except HEARTBEAT message.

#### imu_pub

Publish IMU state

##### Published Topics

- `~imu/data`
  ([sensor_msgs/msg/Imu](https://docs.ros.org/en/rolling/p/sensor_msgs/msg/Imu.html)):
  Imu data, orientation computed by FCU
- `~imu/data_raw`
  ([sensor_msgs/msg/Imu](https://docs.ros.org/en/rolling/p/sensor_msgs/msg/Imu.html)):
  Raw IMU data without orientation
- `~imu/mag`
  ([sensor_msgs/msg/MagneticField](https://docs.ros.org/en/rolling/p/sensor_msgs/msg/MagneticField.html)):
  FCU compass data
- `~imu/temperature`
  ([sensor_msgs/msg/Temperature](https://docs.ros.org/en/rolling/p/sensor_msgs/msg/Temperature.html)):
  Temperature reported by FCU (usually from barometer)
- `~imu/atm_pressure`
  ([sensor_msgs/msg/FluidPressure](https://docs.ros.org/en/rolling/p/sensor_msgs/msg/FluidPressure.html)):
  Air pressure.

##### Parameters

- `~imu/frame_id` (`string`, default: `fcu`): Frame ID for this plugin.
- `~imu/linear_acceleration_stdev` (`double`, default: `0.0003`):
  Gyro's standard deviation
- `~imu/angular_velocity_stdev` (`double`, default: `!dec 0.02`):
  Accel's standard deviation
- `~imu/orientation_stdev` (`double`, default: `1.0`): Standard
  deviation for IMU.orientation
- `~imu/magnetic_stdev` (default: `0.0`): Standard deviation for
  magnetic field message (undefined if: 0.0)

#### gps

Publish GPS Fix (like
[nmea_navsat_driver](https://index.ros.org/p/nmea_navsat_driver))

##### Published Topics

- `~fix`
  ([sensor_msgs/msg/NavSatFix](https://docs.ros.org/en/rolling/p/sensor_msgs/msg/NavSatFix.html)):
  GPS position fix reported by the device.
- `~time_reference`
  ([sensor_msgs/msg/TimeReference](https://docs.ros.org/en/rolling/p/sensor_msgs/msg/TimeReference.html)):
  Time reference computed from SYSTEM_TIME.
- `~gps_vel`
  ([geometry_msgs/msg/TwistStamped](https://docs.ros.org/en/rolling/p/geometry_msgs/msg/TwistStamped.html)):
  Velocity output from the GPS device.

##### Parameters

- `~gps/frame_id` (`string`, default: `gps`): Frame ID for fix message.
- `~gps/time_ref_source` (`string`, default: `same as ~gps/frame_id`):
  Ref source for time_reference message.

#### param

Allows to access to FCU parameters and map it to ROS parameters in
`param/`.

##### Services

- `~param/pull`
  ([mavros/srv/ParamPull](https://docs.ros.org/en/rolling/p/mavros/srv/ParamPull.html)):
  Request parameter from device (or internal cache).
- `~param/push`
  ([mavros/srv/ParamPush](https://docs.ros.org/en/rolling/p/mavros/srv/ParamPush.html)):
  Request send parameters from ROS to FCU.
- `~param/get`
  ([mavros/srv/ParamGet](https://docs.ros.org/en/rolling/p/mavros/srv/ParamGet.html)):
  Return FCU parameter value.
- `~param/set`
  ([mavros/srv/ParamSet](https://docs.ros.org/en/rolling/p/mavros/srv/ParamSet.html)):
  Set parameter on FCU immidiatly.

#### waypoint

Allows to access to FCU mission (waypoints).

##### Published Topics

- `~mission/waypoints`
  ([mavros/msg/WaypointList](https://docs.ros.org/en/rolling/p/mavros/msg/WaypointList.html)):
  Current waypoint table. Updates on changes.

##### Services

- `~mission/pull`
  ([mavros/srv/WaypointPull](https://docs.ros.org/en/rolling/p/mavros/srv/WaypointPull.html)):
  Request update waypoint list.
- `~mission/push`
  ([mavros/srv/WaypointPush](https://docs.ros.org/en/rolling/p/mavros/srv/WaypointPush.html)):
  Send new waypoint table.
- `~mission/clear`
  ([mavros/srv/WaypointClear](https://docs.ros.org/en/rolling/p/mavros/srv/WaypointClear.html)):
  Clear mission on FCU.
- `~mission/set_current`
  ([mavros/srv/WaypointSetCurrent](https://docs.ros.org/en/rolling/p/mavros/srv/WaypointSetCurrent.html)):
  Set current seq. number in list.
- `~mission/goto`
  ([mavros/srv/WaypointGOTO](https://docs.ros.org/en/rolling/p/mavros/srv/WaypointGOTO.html)):
  Send goto point (APM specific).

##### Parameters

- `~mission/pull_after_gcs` (`bool`, default: `false`): Defines pull or
  not waypoints if detected GCS activity.

#### rc_io

Publish RC receiver inputs.

##### Published Topics

- `~rc/in`
  ([mavros/msg/RCIn](https://docs.ros.org/en/rolling/p/mavros/msg/RCIn.html)):
  Publish RC inputs (in raw milliseconds)
- `~rc/out`
  ([mavros/msg/RCOut](https://docs.ros.org/en/rolling/p/mavros/msg/RCOut.html)):
  Publish FCU servo outputs
- `~rc/override`
  ([mavros/msg/OverrideRCIn](https://docs.ros.org/en/rolling/p/mavros/msg/OverrideRCIn.html)):
  Send RC override message to FCU. This topic replace override service.

#### command

Send COMMAND_LONG to FCU.

##### Services

- `~cmd/command`
  ([mavros/srv/CommandLong](https://docs.ros.org/en/rolling/p/mavros/srv/CommandLong.html)):
  Send any COMMAND_LONG to FCU.
- `~cmd/command_int`
  ([mavros/srv/CommandInt](https://docs.ros.org/en/rolling/p/mavros/srv/CommandInt.html)):
  Send any COMMAND_INT to FCU.
- `~cmd/arming`
  ([mavros/srv/CommandBool](https://docs.ros.org/en/rolling/p/mavros/srv/CommandBool.html)):
  Change Arming status.
- `~cmd/set_home`
  ([mavros/srv/CommandHome](https://docs.ros.org/en/rolling/p/mavros/srv/CommandHome.html)):
  Change HOME location.
- `~cmd/guided_enable`
  ([mavros/srv/CommandBool](https://docs.ros.org/en/rolling/p/mavros/srv/CommandBool.html)):
  Enable guided mode by sending MAV_CMD_NAV_GUIDED_ENABLE command.
- `~cmd/takeoff`
  ([mavros/srv/CommandTOL](https://docs.ros.org/en/rolling/p/mavros/srv/CommandTOL.html)):
  Send takeoff command.
- `~cmd/land`
  ([mavros/srv/CommandTOL](https://docs.ros.org/en/rolling/p/mavros/srv/CommandTOL.html)):
  Send land command.

#### local_position

Publish LOCAL_POSITION_NED in [TF](https://index.ros.org/p/tf) and
PoseStamped topic.

##### Published Topics

- `~position/local`
  ([geometry_msgs/msg/PoseStamped](https://docs.ros.org/en/rolling/p/geometry_msgs/msg/PoseStamped.html)):
  Local position from FCU.

##### Parameters

- `~position/local/send_tf` (`bool`, default: `true`): TF send switch.
- `~position/local/frame_id` (`string`, default: `local_origin`): Origin
  frame_id for TF.
- `~position/local/child_frame_id` (`string`, default: `fcu`): Child
  frame_id for TF and PoseStamped.

#### setpoint_accel

Send acceleration setpoint to FCU.

##### Subscribed Topics

- `~setpoint/accel`
  ([geometry_msgs/msg/Vector3](https://docs.ros.org/en/rolling/p/geometry_msgs/msg/Vector3.html)):
  Acceleration or force setpoint vector.

##### Parameters

- `~setpoint/accel/send_force` (`bool`): Send force setpoint.

#### setpoint_attitude

Send ATTITUDE_SETPOINT_EXTERNAL to FCU.

##### Subscribed Topics

- `~setpoint/att_vel`
  ([geometry_msgs/msg/Twist](https://docs.ros.org/en/rolling/p/geometry_msgs/msg/Twist.html)):
  Send angular velocity.
- `~setpoint/attitude`
  ([geometry_msgs/msg/PoseStamped](https://docs.ros.org/en/rolling/p/geometry_msgs/msg/PoseStamped.html)):
  Send attitude setpoint.
- `~setpoint/attitude`
  ([geometry_msgs/msg/PoseWithCovarianceStamped](https://docs.ros.org/en/rolling/p/geometry_msgs/msg/PoseWithCovarianceStamped.html)):
  Send attitude setpoint with covariance (alternative).

##### Parameters

- `~setpoint/attitude/listen_tf` (`bool`, default: `false`): TF listen
  switch. Disable topics if enabled.
- `~setpoint/attitude/listen_twist` (`bool`, default: `false`): Use
  att_vel topic instead of attitude.
- `~setpoint/attitude/pose_with_covariance` (`bool`, default: `false`):
  Selector for attitude message type.
- `~setpoint/attitude/frame_id` (`string`, default: `local_origin`):
  Origin frame_id for TF.
- `~setpoint/attitude/child_frame_id` (`string`, default: `attitude`):
  Child frame_id for TF.
- `~setpoint/attitude/tf_rate_limit` (`double`, default: `10.0`): Rate
  limit for TF listener \[Hz\].

#### setpoint_position

Sent LOCAL_NED_POSITION_SETPOINT_EXTERNAL to FCU.

##### Subscribed Topics

- `~setpoint/local_setpoint`
  ([geometry_msgs/msg/PoseStamped](https://docs.ros.org/en/rolling/p/geometry_msgs/msg/PoseStamped.html)):
  Setpoint position. Orientation not used.

##### Parameters

- `~setpoint/position/listen_tf` (`bool`, default: `false`): TF listen
  switch. Disable topic if enabled.
- `~setpoint/position/frame_id` (`string`, default: `local_origin`):
  Origin frame_id for TF.
- `~setpoint/position/child_frame_id` (`string`, default: `setpoint`):
  Child frame_id for TF.
- `~setpoint/position/tf_rate_limit` (`double`, default: `50.0`): Rate
  limit for TF listener \[Hz\].

#### setpoint_velocity

Send velocity setpoint to FCU.

##### Subscribed Topics

- `~setpoint/cmd_vel`
  ([geometry_msgs/msg/Twist](https://docs.ros.org/en/rolling/p/geometry_msgs/msg/Twist.html)):
  Velocity setpoint.

#### safety_area

Sends safety allowed area to FCU. Initial area can be loaded from
parameters.

##### Subscribed Topics

- `~safety_area/set`
  ([geometry_msgs/msg/PolygonStamped](https://docs.ros.org/en/rolling/p/geometry_msgs/msg/PolygonStamped.html)):
  Volumetric area described by two corners.

##### Parameters

- `~safety_area/p1/x` (`double`): Corner 1 X.
- `~safety_area/p1/y` (`double`): Corner 1 Y.
- `~safety_area/p1/z` (`double`): Corner 1 Z.
- `~safety_area/p2/x` (`double`): Corner 2 X.
- `~safety_area/p2/y` (`double`): Corner 2 Y.
- `~safety_area/p2/z` (`double`): Corner 2 Z.

#### 3dr_radio

Publish 3DR Radio status to diagnostics and topic.

##### Published Topics

- `~radio_status`
  ([mavros/msg/RadioStatus](https://docs.ros.org/en/rolling/p/mavros/msg/RadioStatus.html)):
  Status received from modem, same as RADIO_STATUS message.

#### vfr_hud

Publish VFR_HUD and WIND messages.

##### Published Topics

- `~vfr_hud`
  ([mavros/msg/VFR_HUD](https://docs.ros.org/en/rolling/p/mavros/msg/VFR_HUD.html)):
  Data for HUD.
- `~wind_estimation`
  ([geometry_msgs/msg/TwistStamped](https://docs.ros.org/en/rolling/p/geometry_msgs/msg/TwistStamped.html)):
  Wind estimation from FCU (**APM**).

#### global_position

Publish global position information fused by FCU.

##### Published Topics

- `~global_position/global`
  ([sensor_msgs/msg/NavSatFix](https://docs.ros.org/en/rolling/p/sensor_msgs/msg/NavSatFix.html)):
  GPS Fix.
- `~global_position/local`
  ([geometry_msgs/msg/PoseWithCovarianceStamped](https://docs.ros.org/en/rolling/p/geometry_msgs/msg/PoseWithCovarianceStamped.html)):
  UTM coords.
- `~global_position/gps_vel`
  ([geometry_msgs/msg/Vector3Stamped](https://docs.ros.org/en/rolling/p/geometry_msgs/msg/Vector3Stamped.html)):
  Velocity fused by FCU.
- `~global_position/rel_alt`
  ([std_msgs/msg/Float64](https://docs.ros.org/en/rolling/p/std_msgs/msg/Float64.html)):
  Relative altitude.
- `~global_position/compass_hdg`
  ([std_msgs/msg/Float64](https://docs.ros.org/en/rolling/p/std_msgs/msg/Float64.html)):
  Compass heading in degrees.

##### Parameters

- `~global_position/send_tf` (`bool`): Send or not local UTM coords?
- `~global_position/frame_id` (`string`, default: `local_origin`):
  Origin frame_id for TF.
- `~global_position/child_frame_id` (`string`, default: `fcu`): Child
  frame_id for TF.

#### ftp

Support plugin for MAVLink-FTP (**PX4**).

##### Services

- `~ftp/open`
  ([mavros/srv/FileOpen](https://docs.ros.org/en/rolling/p/mavros/srv/FileOpen.html)):
  Open file (acquire session).
- `~ftp/close`
  ([mavros/srv/FileClose](https://docs.ros.org/en/rolling/p/mavros/srv/FileClose.html)):
  Close file (release session).
- `~ftp/read`
  ([mavros/srv/FileRead](https://docs.ros.org/en/rolling/p/mavros/srv/FileRead.html)):
  Read from opened file.
- `~ftp/write`
  ([mavros/srv/FileWrite](https://docs.ros.org/en/rolling/p/mavros/srv/FileWrite.html)):
  Write to opened file.
- `~ftp/list`
  ([mavros/srv/FileList](https://docs.ros.org/en/rolling/p/mavros/srv/FileList.html)):
  List directory.
- `~ftp/truncate`
  ([mavros/srv/FileTruncate](https://docs.ros.org/en/rolling/p/mavros/srv/FileTruncate.html)):
  Truncate file.
- `~ftp/remove`
  ([mavros/srv/FileRemove](https://docs.ros.org/en/rolling/p/mavros/srv/FileRemove.html)):
  Unlink file.
- `~ftp/rename`
  ([mavros/srv/FileRename](https://docs.ros.org/en/rolling/p/mavros/srv/FileRename.html)):
  Rename file/directory.
- `~ftp/mkdir`
  ([mavros/srv/FileMakeDir](https://docs.ros.org/en/rolling/p/mavros/srv/FileMakeDir.html)):
  Create directory.
- `~ftp/rmdir`
  ([mavros/srv/FileRemoveDir](https://docs.ros.org/en/rolling/p/mavros/srv/FileRemoveDir.html)):
  Remove directory.
- `~ftp/checksum`
  ([mavros/srv/FileChecksum](https://docs.ros.org/en/rolling/p/mavros/srv/FileChecksum.html)):
  Request to calculate CRC32 of file on FCU.
- `~ftp/reset`
  ([std_srvs/srv/Empty](https://docs.ros.org/en/rolling/p/std_srvs/srv/Empty.html)):
  Reset FCU server (dangerous).

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

#### sys_status

System status plugin. Handles FCU detection.

##### Published Topics

- `~state`
  ([mavros/msg/State](https://docs.ros.org/en/rolling/p/mavros/msg/State.html)):
  FCU state
- `~battery`
  ([mavros/msg/BatteryStatus](https://docs.ros.org/en/rolling/p/mavros/msg/BatteryStatus.html)):
  FCU battery status report.

##### Services

- `~set_stream_rate`
  ([mavros/srv/StreamRate](https://docs.ros.org/en/rolling/p/mavros/srv/StreamRate.html)):
  Send stream rate request to FCU. (Since 0.5.0)
- `~set_mode`
  ([mavros/srv/SetMode](https://docs.ros.org/en/rolling/p/mavros/srv/SetMode.html)):
  Set FCU operation mode. See custom mode identifiers at
  [modes page](#fcumodes).

##### Parameters

- `~conn_timeout` (`double`, default: `30.0`): Connection time out in
  seconds.
- `~conn_heartbeat` (`double`, default: `0.0`): Period to send HEARTBEAT
  messages (or disabled if 0.0)
- `~sys/min_voltage` (`double`, default: `6.0`): Minimal battery voltage
  for diagnostics.
- `~sys/disable_diag` (`bool`, default: `false`): Disable all diag
  except HEARTBEAT message.

#### sys_time

System time plugin. Does time syncronization on **PX4**.

##### Published Topics

- `~time_reference`
  ([sensor_msgs/msg/TimeReference](https://docs.ros.org/en/rolling/p/sensor_msgs/msg/TimeReference.html)):
  Time reference computed from SYSTEM_TIME.

##### Parameters

- `~conn_system_time` (`double`, default: `0.0`): Send `SYSTEM_TIME`
  to device period in seconds.
- `~conn_timesync` (`double`, default: `0.0`): TIMESYNC period. **PX4**
  only.

#### imu_pub

Publish IMU state

##### Published Topics

- `~imu/data`
  ([sensor_msgs/msg/Imu](https://docs.ros.org/en/rolling/p/sensor_msgs/msg/Imu.html)):
  Imu data, orientation computed by FCU
- `~imu/data_raw`
  ([sensor_msgs/msg/Imu](https://docs.ros.org/en/rolling/p/sensor_msgs/msg/Imu.html)):
  Raw IMU data without orientation
- `~imu/mag`
  ([sensor_msgs/msg/MagneticField](https://docs.ros.org/en/rolling/p/sensor_msgs/msg/MagneticField.html)):
  FCU compass data
- `~imu/temperature`
  ([sensor_msgs/msg/Temperature](https://docs.ros.org/en/rolling/p/sensor_msgs/msg/Temperature.html)):
  Temperature reported by FCU (usually from barometer)
- `~imu/atm_pressure`
  ([sensor_msgs/msg/FluidPressure](https://docs.ros.org/en/rolling/p/sensor_msgs/msg/FluidPressure.html)):
  Air pressure.

##### Parameters

- `~imu/frame_id` (`string`, default: `fcu`): Frame ID for this plugin.
- `~imu/linear_acceleration_stdev` (`double`, default: `0.0003`):
  Gyro's standard deviation
- `~imu/angular_velocity_stdev` (`double`, default: `!dec 0.02`):
  Accel's standard deviation
- `~imu/orientation_stdev` (`double`, default: `1.0`): Standard
  deviation for IMU.orientation
- `~imu/magnetic_stdev` (default: `0.0`): Standard deviation for
  magnetic field message (undefined if: 0.0)

#### gps

Publish GPS Fix (like
[nmea_navsat_driver](https://index.ros.org/p/nmea_navsat_driver))

##### Published Topics

- `~fix`
  ([sensor_msgs/msg/NavSatFix](https://docs.ros.org/en/rolling/p/sensor_msgs/msg/NavSatFix.html)):
  GPS position fix reported by the device.
- `~gps_vel`
  ([geometry_msgs/msg/TwistStamped](https://docs.ros.org/en/rolling/p/geometry_msgs/msg/TwistStamped.html)):
  Velocity output from the GPS device.

##### Parameters

- `~gps/frame_id` (`string`, default: `gps`): Frame ID for fix message.
- `~gps/time_ref_source` (`string`, default: `same as ~gps/frame_id`):
  Ref source for time_reference message.

#### param

Allows to access to FCU parameters and map it to ROS parameters in
`param/`.

##### Services

- `~param/pull`
  ([mavros/srv/ParamPull](https://docs.ros.org/en/rolling/p/mavros/srv/ParamPull.html)):
  Request parameter from device (or internal cache).
- `~param/push`
  ([mavros/srv/ParamPush](https://docs.ros.org/en/rolling/p/mavros/srv/ParamPush.html)):
  Request send parameters from ROS to FCU.
- `~param/get`
  ([mavros/srv/ParamGet](https://docs.ros.org/en/rolling/p/mavros/srv/ParamGet.html)):
  Return FCU parameter value.
- `~param/set`
  ([mavros/srv/ParamSet](https://docs.ros.org/en/rolling/p/mavros/srv/ParamSet.html)):
  Set parameter on FCU immidiatly.

#### waypoint

Allows to access to FCU mission (waypoints).

##### Published Topics

- `~mission/waypoints`
  ([mavros/msg/WaypointList](https://docs.ros.org/en/rolling/p/mavros/msg/WaypointList.html)):
  Current waypoint table. Updates on changes.

##### Services

- `~mission/pull`
  ([mavros/srv/WaypointPull](https://docs.ros.org/en/rolling/p/mavros/srv/WaypointPull.html)):
  Request update waypoint list.
- `~mission/push`
  ([mavros/srv/WaypointPush](https://docs.ros.org/en/rolling/p/mavros/srv/WaypointPush.html)):
  Send new waypoint table.
- `~mission/clear`
  ([mavros/srv/WaypointClear](https://docs.ros.org/en/rolling/p/mavros/srv/WaypointClear.html)):
  Clear mission on FCU.
- `~mission/set_current`
  ([mavros/srv/WaypointSetCurrent](https://docs.ros.org/en/rolling/p/mavros/srv/WaypointSetCurrent.html)):
  Set current seq. number in list.
- `~mission/goto`
  ([mavros/srv/WaypointGOTO](https://docs.ros.org/en/rolling/p/mavros/srv/WaypointGOTO.html)):
  Send goto point (APM specific).

##### Parameters

- `~mission/pull_after_gcs` (`bool`, default: `false`): Defines pull or
  not waypoints if detected GCS activity.

#### rc_io

Publish RC receiver inputs.

##### Published Topics

- `~rc/in`
  ([mavros/msg/RCIn](https://docs.ros.org/en/rolling/p/mavros/msg/RCIn.html)):
  Publish RC inputs (in raw milliseconds)
- `~rc/out`
  ([mavros/msg/RCOut](https://docs.ros.org/en/rolling/p/mavros/msg/RCOut.html)):
  Publish FCU servo outputs
- `~rc/override`
  ([mavros/msg/OverrideRCIn](https://docs.ros.org/en/rolling/p/mavros/msg/OverrideRCIn.html)):
  Send RC override message to FCU. **APM** only. Requires setup FCU
  param `SYSID_MYGCS` to match mavros system id.

#### command

Send COMMAND_LONG to FCU.

##### Services

- `~cmd/command`
  ([mavros/srv/CommandLong](https://docs.ros.org/en/rolling/p/mavros/srv/CommandLong.html)):
  Send any COMMAND_LONG to FCU.
- `~cmd/command_int`
  ([mavros/srv/CommandInt](https://docs.ros.org/en/rolling/p/mavros/srv/CommandInt.html)):
  Send any COMMAND_INT to FCU.
- `~cmd/arming`
  ([mavros/srv/CommandBool](https://docs.ros.org/en/rolling/p/mavros/srv/CommandBool.html)):
  Change Arming status.
- `~cmd/set_home`
  ([mavros/srv/CommandHome](https://docs.ros.org/en/rolling/p/mavros/srv/CommandHome.html)):
  Change HOME location.
- `~cmd/guided_enable`
  ([mavros/srv/CommandBool](https://docs.ros.org/en/rolling/p/mavros/srv/CommandBool.html)):
  Enable guided mode by sending MAV_CMD_NAV_GUIDED_ENABLE command.
- `~cmd/takeoff`
  ([mavros/srv/CommandTOL](https://docs.ros.org/en/rolling/p/mavros/srv/CommandTOL.html)):
  Send takeoff command.
- `~cmd/land`
  ([mavros/srv/CommandTOL](https://docs.ros.org/en/rolling/p/mavros/srv/CommandTOL.html)):
  Send land command.

##### Parameters

- `~cmd/use_comp_id_system_control` (`bool`, default: `false`): Use
  `SYSTEM_CONTROL` component id instead of mavros target component.

#### local_position

Publish LOCAL_POSITION_NED in [TF](https://index.ros.org/p/tf) and
PoseStamped topic.

##### Published Topics

- `~position/local`
  ([geometry_msgs/msg/PoseStamped](https://docs.ros.org/en/rolling/p/geometry_msgs/msg/PoseStamped.html)):
  Local position from FCU.

##### Parameters

- `~position/local/send_tf` (`bool`, default: `true`): TF send switch.
- `~position/local/frame_id` (`string`, default: `local_origin`): Origin
  frame_id for TF.
- `~position/local/child_frame_id` (`string`, default: `fcu`): Child
  frame_id for TF and PoseStamped.

#### setpoint_accel

Send acceleration setpoint to FCU.

##### Subscribed Topics

- `~setpoint/accel`
  ([geometry_msgs/msg/Vector3](https://docs.ros.org/en/rolling/p/geometry_msgs/msg/Vector3.html)):
  Acceleration or force setpoint vector.

##### Parameters

- `~setpoint/accel/send_force` (`bool`): Send force setpoint.

#### setpoint_attitude

Send ATTITUDE_SETPOINT_EXTERNAL to FCU.

##### Subscribed Topics

- `~setpoint/att_vel`
  ([geometry_msgs/msg/Twist](https://docs.ros.org/en/rolling/p/geometry_msgs/msg/Twist.html)):
  Send angular velocity.
- `~setpoint/attitude`
  ([geometry_msgs/msg/PoseStamped](https://docs.ros.org/en/rolling/p/geometry_msgs/msg/PoseStamped.html)):
  Send attitude setpoint.
- `~setpoint/attitude`
  ([geometry_msgs/msg/PoseWithCovarianceStamped](https://docs.ros.org/en/rolling/p/geometry_msgs/msg/PoseWithCovarianceStamped.html)):
  Send attitude setpoint with covariance (alternative).

##### Parameters

- `~setpoint/attitude/listen_tf` (`bool`, default: `false`): TF listen
  switch. Disable topics if enabled.
- `~setpoint/attitude/listen_twist` (`bool`, default: `false`): Use
  att_vel topic instead of attitude.
- `~setpoint/attitude/pose_with_covariance` (`bool`, default: `false`):
  Selector for attitude message type.
- `~setpoint/attitude/frame_id` (`string`, default: `local_origin`):
  Origin frame_id for TF.
- `~setpoint/attitude/child_frame_id` (`string`, default: `attitude`):
  Child frame_id for TF.
- `~setpoint/attitude/tf_rate_limit` (`double`, default: `10.0`): Rate
  limit for TF listener \[Hz\].

#### setpoint_position

Sent LOCAL_NED_POSITION_SETPOINT_EXTERNAL to FCU.

##### Subscribed Topics

- `~setpoint/local_setpoint`
  ([geometry_msgs/msg/PoseStamped](https://docs.ros.org/en/rolling/p/geometry_msgs/msg/PoseStamped.html)):
  Setpoint position. Orientation not used.

##### Parameters

- `~setpoint/position/listen_tf` (`bool`, default: `false`): TF listen
  switch. Disable topic if enabled.
- `~setpoint/position/frame_id` (`string`, default: `local_origin`):
  Origin frame_id for TF.
- `~setpoint/position/child_frame_id` (`string`, default: `setpoint`):
  Child frame_id for TF.
- `~setpoint/position/tf_rate_limit` (`double`, default: `50.0`): Rate
  limit for TF listener \[Hz\].

#### setpoint_velocity

Send velocity setpoint to FCU.

##### Subscribed Topics

- `~setpoint/cmd_vel`
  ([geometry_msgs/msg/Twist](https://docs.ros.org/en/rolling/p/geometry_msgs/msg/Twist.html)):
  Velocity setpoint.

#### safety_area

Sends safety allowed area to FCU. Initial area can be loaded from
parameters.

##### Subscribed Topics

- `~safety_area/set`
  ([geometry_msgs/msg/PolygonStamped](https://docs.ros.org/en/rolling/p/geometry_msgs/msg/PolygonStamped.html)):
  Volumetric area described by two corners.

##### Parameters

- `~safety_area/p1/x` (`double`): Corner 1 X.
- `~safety_area/p1/y` (`double`): Corner 1 Y.
- `~safety_area/p1/z` (`double`): Corner 1 Z.
- `~safety_area/p2/x` (`double`): Corner 2 X.
- `~safety_area/p2/y` (`double`): Corner 2 Y.
- `~safety_area/p2/z` (`double`): Corner 2 Z.

#### 3dr_radio

Publish 3DR Radio status to diagnostics and topic.

##### Published Topics

- `~radio_status`
  ([mavros/msg/RadioStatus](https://docs.ros.org/en/rolling/p/mavros/msg/RadioStatus.html)):
  Status received from modem, same as RADIO_STATUS message.

#### vfr_hud

Publish VFR_HUD and WIND messages.

##### Published Topics

- `~vfr_hud`
  ([mavros/msg/VFR_HUD](https://docs.ros.org/en/rolling/p/mavros/msg/VFR_HUD.html)):
  Data for HUD.
- `~wind_estimation`
  ([geometry_msgs/msg/TwistStamped](https://docs.ros.org/en/rolling/p/geometry_msgs/msg/TwistStamped.html)):
  Wind estimation from FCU (**APM**).

#### global_position

Publish global position information fused by FCU.

##### Published Topics

- `~global_position/global`
  ([sensor_msgs/msg/NavSatFix](https://docs.ros.org/en/rolling/p/sensor_msgs/msg/NavSatFix.html)):
  GPS Fix.
- `~global_position/local`
  ([geometry_msgs/msg/PoseWithCovarianceStamped](https://docs.ros.org/en/rolling/p/geometry_msgs/msg/PoseWithCovarianceStamped.html)):
  UTM coords.
- `~global_position/gps_vel`
  ([geometry_msgs/msg/Vector3Stamped](https://docs.ros.org/en/rolling/p/geometry_msgs/msg/Vector3Stamped.html)):
  Velocity fused by FCU.
- `~global_position/rel_alt`
  ([std_msgs/msg/Float64](https://docs.ros.org/en/rolling/p/std_msgs/msg/Float64.html)):
  Relative altitude.
- `~global_position/compass_hdg`
  ([std_msgs/msg/Float64](https://docs.ros.org/en/rolling/p/std_msgs/msg/Float64.html)):
  Compass heading in degrees.

##### Parameters

- `~global_position/send_tf` (`bool`): Send or not local UTM coords?
- `~global_position/frame_id` (`string`, default: `local_origin`):
  Origin frame_id for TF.
- `~global_position/child_frame_id` (`string`, default: `fcu`): Child
  frame_id for TF.

#### ftp

Support plugin for MAVLink-FTP (**PX4**).

##### Services

- `~ftp/open`
  ([mavros/srv/FileOpen](https://docs.ros.org/en/rolling/p/mavros/srv/FileOpen.html)):
  Open file (acquire session).
- `~ftp/close`
  ([mavros/srv/FileClose](https://docs.ros.org/en/rolling/p/mavros/srv/FileClose.html)):
  Close file (release session).
- `~ftp/read`
  ([mavros/srv/FileRead](https://docs.ros.org/en/rolling/p/mavros/srv/FileRead.html)):
  Read from opened file.
- `~ftp/write`
  ([mavros/srv/FileWrite](https://docs.ros.org/en/rolling/p/mavros/srv/FileWrite.html)):
  Write to opened file.
- `~ftp/list`
  ([mavros/srv/FileList](https://docs.ros.org/en/rolling/p/mavros/srv/FileList.html)):
  List directory.
- `~ftp/truncate`
  ([mavros/srv/FileTruncate](https://docs.ros.org/en/rolling/p/mavros/srv/FileTruncate.html)):
  Truncate file.
- `~ftp/remove`
  ([mavros/srv/FileRemove](https://docs.ros.org/en/rolling/p/mavros/srv/FileRemove.html)):
  Unlink file.
- `~ftp/rename`
  ([mavros/srv/FileRename](https://docs.ros.org/en/rolling/p/mavros/srv/FileRename.html)):
  Rename file/directory.
- `~ftp/mkdir`
  ([mavros/srv/FileMakeDir](https://docs.ros.org/en/rolling/p/mavros/srv/FileMakeDir.html)):
  Create directory.
- `~ftp/rmdir`
  ([mavros/srv/FileRemoveDir](https://docs.ros.org/en/rolling/p/mavros/srv/FileRemoveDir.html)):
  Remove directory.
- `~ftp/checksum`
  ([mavros/srv/FileChecksum](https://docs.ros.org/en/rolling/p/mavros/srv/FileChecksum.html)):
  Request to calculate CRC32 of file on FCU.
- `~ftp/reset`
  ([std_srvs/srv/Empty](https://docs.ros.org/en/rolling/p/std_srvs/srv/Empty.html)):
  Reset FCU server (dangerous).

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

#### 3dr_radio

Publish 3DR Radio status to diagnostics and topic.

##### Published Topics

- `~radio_status`
  ([mavros/msg/RadioStatus](https://docs.ros.org/en/rolling/p/mavros/msg/RadioStatus.html)):
  Status received from modem, same as RADIO_STATUS message.

#### actuator_control

Sends acruator commands to FCU.

##### Subscribed Topics

- `~actuator_control`
  ([mavros/msg/ActuatorControl](https://docs.ros.org/en/rolling/p/mavros/msg/ActuatorControl.html)):
  actuator command

#### command

Send COMMAND_LONG to FCU.

##### Services

- `~cmd/command`
  ([mavros/srv/CommandLong](https://docs.ros.org/en/rolling/p/mavros/srv/CommandLong.html)):
  Send any COMMAND_LONG to FCU.
- `~cmd/command_int`
  ([mavros/srv/CommandInt](https://docs.ros.org/en/rolling/p/mavros/srv/CommandInt.html)):
  Send any COMMAND_INT to FCU.
- `~cmd/arming`
  ([mavros/srv/CommandBool](https://docs.ros.org/en/rolling/p/mavros/srv/CommandBool.html)):
  Change Arming status.
- `~cmd/set_home`
  ([mavros/srv/CommandHome](https://docs.ros.org/en/rolling/p/mavros/srv/CommandHome.html)):
  Change HOME location.
- `~cmd/guided_enable`
  ([mavros/srv/CommandBool](https://docs.ros.org/en/rolling/p/mavros/srv/CommandBool.html)):
  Enable guided mode by sending MAV_CMD_NAV_GUIDED_ENABLE command.
- `~cmd/takeoff`
  ([mavros/srv/CommandTOL](https://docs.ros.org/en/rolling/p/mavros/srv/CommandTOL.html)):
  Send takeoff command.
- `~cmd/land`
  ([mavros/srv/CommandTOL](https://docs.ros.org/en/rolling/p/mavros/srv/CommandTOL.html)):
  Send land command.

##### Parameters

- `~cmd/use_comp_id_system_control` (`bool`, default: `false`): Use
  `SYSTEM_CONTROL` component id instead of mavros target component.

#### ftp

Support plugin for MAVLink-FTP (**PX4**).

##### Services

- `~ftp/open`
  ([mavros/srv/FileOpen](https://docs.ros.org/en/rolling/p/mavros/srv/FileOpen.html)):
  Open file (acquire session).
- `~ftp/close`
  ([mavros/srv/FileClose](https://docs.ros.org/en/rolling/p/mavros/srv/FileClose.html)):
  Close file (release session).
- `~ftp/read`
  ([mavros/srv/FileRead](https://docs.ros.org/en/rolling/p/mavros/srv/FileRead.html)):
  Read from opened file.
- `~ftp/write`
  ([mavros/srv/FileWrite](https://docs.ros.org/en/rolling/p/mavros/srv/FileWrite.html)):
  Write to opened file.
- `~ftp/list`
  ([mavros/srv/FileList](https://docs.ros.org/en/rolling/p/mavros/srv/FileList.html)):
  List directory.
- `~ftp/truncate`
  ([mavros/srv/FileTruncate](https://docs.ros.org/en/rolling/p/mavros/srv/FileTruncate.html)):
  Truncate file.
- `~ftp/remove`
  ([mavros/srv/FileRemove](https://docs.ros.org/en/rolling/p/mavros/srv/FileRemove.html)):
  Unlink file.
- `~ftp/rename`
  ([mavros/srv/FileRename](https://docs.ros.org/en/rolling/p/mavros/srv/FileRename.html)):
  Rename file/directory.
- `~ftp/mkdir`
  ([mavros/srv/FileMakeDir](https://docs.ros.org/en/rolling/p/mavros/srv/FileMakeDir.html)):
  Create directory.
- `~ftp/rmdir`
  ([mavros/srv/FileRemoveDir](https://docs.ros.org/en/rolling/p/mavros/srv/FileRemoveDir.html)):
  Remove directory.
- `~ftp/checksum`
  ([mavros/srv/FileChecksum](https://docs.ros.org/en/rolling/p/mavros/srv/FileChecksum.html)):
  Request to calculate CRC32 of file on FCU.
- `~ftp/reset`
  ([std_srvs/srv/Empty](https://docs.ros.org/en/rolling/p/std_srvs/srv/Empty.html)):
  Reset FCU server (dangerous).

#### global_position

Publish global position information fused by FCU.

##### Published Topics

- `~global_position/global`
  ([sensor_msgs/msg/NavSatFix](https://docs.ros.org/en/rolling/p/sensor_msgs/msg/NavSatFix.html)):
  GPS Fix.
- `~global_position/local`
  ([geometry_msgs/msg/PoseWithCovarianceStamped](https://docs.ros.org/en/rolling/p/geometry_msgs/msg/PoseWithCovarianceStamped.html)):
  UTM coords.
- `~global_position/gp_vel`
  ([geometry_msgs/msg/Vector3Stamped](https://docs.ros.org/en/rolling/p/geometry_msgs/msg/Vector3Stamped.html)):
  Velocity fused by FCU.
- `~global_position/rel_alt`
  ([std_msgs/msg/Float64](https://docs.ros.org/en/rolling/p/std_msgs/msg/Float64.html)):
  Relative altitude.
- `~global_position/compass_hdg`
  ([std_msgs/msg/Float64](https://docs.ros.org/en/rolling/p/std_msgs/msg/Float64.html)):
  Compass heading in degrees.

##### Parameters

- `~global_position/send_tf` (`bool`): Send or not local UTM coords?
- `~global_position/frame_id` (`string`, default: `local_origin`):
  Origin frame_id for TF.
- `~global_position/child_frame_id` (`string`, default: `fcu`): Child
  frame_id for TF.

#### gps

Publish GPS Fix (like
[nmea_navsat_driver](https://index.ros.org/p/nmea_navsat_driver))

##### Published Topics

- `~gps/fix`
  ([sensor_msgs/msg/NavSatFix](https://docs.ros.org/en/rolling/p/sensor_msgs/msg/NavSatFix.html)):
  GPS position fix reported by the device.
- `~gps/gps_vel`
  ([geometry_msgs/msg/TwistStamped](https://docs.ros.org/en/rolling/p/geometry_msgs/msg/TwistStamped.html)):
  Velocity output from the GPS device.

##### Parameters

- `~gps/frame_id` (`string`, default: `gps`): Frame ID for fix message.

#### imu_pub

Publish IMU state

##### Published Topics

- `~imu/data`
  ([sensor_msgs/msg/Imu](https://docs.ros.org/en/rolling/p/sensor_msgs/msg/Imu.html)):
  Imu data, orientation computed by FCU
- `~imu/data_raw`
  ([sensor_msgs/msg/Imu](https://docs.ros.org/en/rolling/p/sensor_msgs/msg/Imu.html)):
  Raw IMU data without orientation
- `~imu/mag`
  ([sensor_msgs/msg/MagneticField](https://docs.ros.org/en/rolling/p/sensor_msgs/msg/MagneticField.html)):
  FCU compass data
- `~imu/temperature`
  ([sensor_msgs/msg/Temperature](https://docs.ros.org/en/rolling/p/sensor_msgs/msg/Temperature.html)):
  Temperature reported by FCU (usually from barometer)
- `~imu/atm_pressure`
  ([sensor_msgs/msg/FluidPressure](https://docs.ros.org/en/rolling/p/sensor_msgs/msg/FluidPressure.html)):
  Air pressure.

##### Parameters

- `~imu/frame_id` (`string`, default: `fcu`): Frame ID for this plugin.
- `~imu/linear_acceleration_stdev` (`double`, default: `0.0003`):
  Gyro's standard deviation
- `~imu/angular_velocity_stdev` (`double`, default: `!dec 0.02`):
  Accel's standard deviation
- `~imu/orientation_stdev` (`double`, default: `1.0`): Standard
  deviation for IMU.orientation
- `~imu/magnetic_stdev` (default: `0.0`): Standard deviation for
  magnetic field message (undefined if: 0.0)

#### local_position

Publish LOCAL_POSITION_NED in [TF](https://index.ros.org/p/tf) and
PoseStamped topic.

##### Published Topics

- `~local_position/local`
  ([geometry_msgs/msg/PoseStamped](https://docs.ros.org/en/rolling/p/geometry_msgs/msg/PoseStamped.html)):
  Local position from FCU.

##### Parameters

- `~local_position/send_tf` (`bool`, default: `true`): TF send switch.
- `~local_position/frame_id` (`string`, default: `local_origin`): Origin
  frame_id for TF.
- `~local_position/child_frame_id` (`string`, default: `fcu`): Child
  frame_id for TF and PoseStamped.

#### param

Allows to access to FCU parameters and map it to ROS parameters in
`param/`.

##### Services

- `~param/pull`
  ([mavros/srv/ParamPull](https://docs.ros.org/en/rolling/p/mavros/srv/ParamPull.html)):
  Request parameter from device (or internal cache).
- `~param/push`
  ([mavros/srv/ParamPush](https://docs.ros.org/en/rolling/p/mavros/srv/ParamPush.html)):
  Request send parameters from ROS to FCU.
- `~param/get`
  ([mavros/srv/ParamGet](https://docs.ros.org/en/rolling/p/mavros/srv/ParamGet.html)):
  Return FCU parameter value.
- `~param/set`
  ([mavros/srv/ParamSet](https://docs.ros.org/en/rolling/p/mavros/srv/ParamSet.html)):
  Set parameter on FCU immidiatly.

#### rc_io

Publish RC receiver inputs.

##### Published Topics

- `~rc/in`
  ([mavros/msg/RCIn](https://docs.ros.org/en/rolling/p/mavros/msg/RCIn.html)):
  Publish RC inputs (in raw milliseconds)
- `~rc/out`
  ([mavros/msg/RCOut](https://docs.ros.org/en/rolling/p/mavros/msg/RCOut.html)):
  Publish FCU servo outputs
- `~rc/override`
  ([mavros/msg/OverrideRCIn](https://docs.ros.org/en/rolling/p/mavros/msg/OverrideRCIn.html)):
  Send RC override message to FCU. **APM** only. Requires setup FCU
  param `SYSID_MYGCS` to match mavros system id.

#### safety_area

Sends safety allowed area to FCU. Initial area can be loaded from
parameters.

##### Subscribed Topics

- `~safety_area/set`
  ([geometry_msgs/msg/PolygonStamped](https://docs.ros.org/en/rolling/p/geometry_msgs/msg/PolygonStamped.html)):
  Volumetric area described by two corners.

##### Parameters

- `~safety_area/p1/x` (`double`): Corner 1 X.
- `~safety_area/p1/y` (`double`): Corner 1 Y.
- `~safety_area/p1/z` (`double`): Corner 1 Z.
- `~safety_area/p2/x` (`double`): Corner 2 X.
- `~safety_area/p2/y` (`double`): Corner 2 Y.
- `~safety_area/p2/z` (`double`): Corner 2 Z.

#### setpoint_accel

Send acceleration setpoint to FCU.

##### Subscribed Topics

- `~setpoint_accel/accel`
  ([geometry_msgs/msg/Vector3Stamped](https://docs.ros.org/en/rolling/p/geometry_msgs/msg/Vector3Stamped.html)):
  Acceleration or force setpoint vector.

##### Parameters

- `~setpoint_accel/send_force` (`bool`): Send force setpoint.

#### setpoint_attitude

Send ATTITUDE_SETPOINT_EXTERNAL to FCU.

##### Subscribed Topics

- `~setpoint_attitude/cmd_vel`
  ([geometry_msgs/msg/TwistStamped](https://docs.ros.org/en/rolling/p/geometry_msgs/msg/TwistStamped.html)):
  Send angular velocity.
- `~setpoint_attitude/attitude`
  ([geometry_msgs/msg/PoseStamped](https://docs.ros.org/en/rolling/p/geometry_msgs/msg/PoseStamped.html)):
  Send attitude setpoint.
- `~setpoint_attitude/attitude`
  ([geometry_msgs/msg/PoseWithCovarianceStamped](https://docs.ros.org/en/rolling/p/geometry_msgs/msg/PoseWithCovarianceStamped.html)):
  Send attitude setpoint with covariance (alternative).

##### Parameters

- `~setpoint_attitude/listen_tf` (`bool`, default: `false`): TF listen
  switch. Disable topics if enabled.
- `~setpoint_attitude/listen_twist` (`bool`, default: `false`): Use
  att_vel topic instead of attitude.
- `~setpoint_attutude/pose_with_covariance` (`bool`, default: `false`):
  Selector for attitude message type.
- `~setpoint_attutude/frame_id` (`string`, default: `local_origin`):
  Origin frame_id for TF.
- `~setpoint_attitude/child_frame_id` (`string`, default: `attitude`):
  Child frame_id for TF.
- `~setpoint_attitude/tf_rate_limit` (`double`, default: `10.0`): Rate
  limit for TF listener \[Hz\].

#### setpoint_position

Sent LOCAL_NED_POSITION_SETPOINT_EXTERNAL to FCU.

##### Subscribed Topics

- `~setpoint_position/local`
  ([geometry_msgs/msg/PoseStamped](https://docs.ros.org/en/rolling/p/geometry_msgs/msg/PoseStamped.html)):
  Setpoint position. Orientation not used.

##### Parameters

- `~setpoint_position/listen_tf` (`bool`, default: `false`): TF listen
  switch. Disable topic if enabled.
- `~setpoint_position/frame_id` (`string`, default: `local_origin`):
  Origin frame_id for TF.
- `~setpoint_position/child_frame_id` (`string`, default: `setpoint`):
  Child frame_id for TF.
- `~setpoint_position/tf_rate_limit` (`double`, default: `50.0`): Rate
  limit for TF listener \[Hz\].

#### setpoint_velocity

Send velocity setpoint to FCU.

##### Subscribed Topics

- `~setpoint_velocity/cmd_vel`
  ([geometry_msgs/msg/TwistStamped](https://docs.ros.org/en/rolling/p/geometry_msgs/msg/TwistStamped.html)):
  Velocity setpoint.

#### sys_status

System status plugin. Handles FCU detection. **REQUIRED** never
blacklist it!.

##### Published Topics

- `~state`
  ([mavros/msg/State](https://docs.ros.org/en/rolling/p/mavros/msg/State.html)):
  FCU state
- `~battery`
  ([mavros/msg/BatteryStatus](https://docs.ros.org/en/rolling/p/mavros/msg/BatteryStatus.html)):
  FCU battery status report.

##### Services

- `~set_stream_rate`
  ([mavros/srv/StreamRate](https://docs.ros.org/en/rolling/p/mavros/srv/StreamRate.html)):
  Send stream rate request to FCU.
- `~set_mode`
  ([mavros/srv/SetMode](https://docs.ros.org/en/rolling/p/mavros/srv/SetMode.html)):
  Set FCU operation mode. See custom mode identifiers at
  [modes page](#fcumodes).

##### Parameters

- `~conn/timeout` (`double`, default: `30.0`): Connection time out in
  seconds.
- `~conn/heartbeat` (`double`, default: `0.0`): Period to send HEARTBEAT
  messages (or disabled if 0.0)
- `~sys/min_voltage` (`double`, default: `6.0`): Minimal battery voltage
  for diagnostics.
- `~sys/disable_diag` (`bool`, default: `false`): Disable all diag
  except HEARTBEAT message.

#### sys_time

System time plugin. Does time syncronization on **PX4**.

##### Published Topics

- `~time_reference`
  ([sensor_msgs/msg/TimeReference](https://docs.ros.org/en/rolling/p/sensor_msgs/msg/TimeReference.html)):
  Time reference computed from SYSTEM_TIME.

##### Parameters

- `~conn/system_time` (`double`, default: `0.0`): Send `SYSTEM_TIME`
  to device period in seconds.
- `~conn/timesync` (`double`, default: `0.0`): TIMESYNC period. **PX4**
  only.
- `~time/time_ref_source` (`string`, default: `"fcu"`): Ref source for
  time_reference message.
- `~time/timesync_avg_alpha` (`double`, default: `0.6`): Alpha for
  exponential moving average.

#### vfr_hud

Publish VFR_HUD and WIND messages.

##### Published Topics

- `~vfr_hud`
  ([mavros/msg/VFR_HUD](https://docs.ros.org/en/rolling/p/mavros/msg/VFR_HUD.html)):
  Data for HUD.
- `~wind_estimation`
  ([geometry_msgs/msg/TwistStamped](https://docs.ros.org/en/rolling/p/geometry_msgs/msg/TwistStamped.html)):
  Wind estimation from FCU (**APM**).

#### waypoint

Allows to access to FCU mission (waypoints).

##### Published Topics

- `~mission/waypoints`
  ([mavros/msg/WaypointList](https://docs.ros.org/en/rolling/p/mavros/msg/WaypointList.html)):
  Current waypoint table. Updates on changes.

##### Services

- `~mission/pull`
  ([mavros/srv/WaypointPull](https://docs.ros.org/en/rolling/p/mavros/srv/WaypointPull.html)):
  Request update waypoint list.
- `~mission/push`
  ([mavros/srv/WaypointPush](https://docs.ros.org/en/rolling/p/mavros/srv/WaypointPush.html)):
  Send new waypoint table.
- `~mission/clear`
  ([mavros/srv/WaypointClear](https://docs.ros.org/en/rolling/p/mavros/srv/WaypointClear.html)):
  Clear mission on FCU.
- `~mission/set_current`
  ([mavros/srv/WaypointSetCurrent](https://docs.ros.org/en/rolling/p/mavros/srv/WaypointSetCurrent.html)):
  Set current seq. number in list.
- `~mission/goto`
  ([mavros/srv/WaypointGOTO](https://docs.ros.org/en/rolling/p/mavros/srv/WaypointGOTO.html)):
  Send goto point (APM specific).

##### Parameters

- `~mission/pull_after_gcs` (`bool`, default: `false`): Defines pull or
  not waypoints if detected GCS activity.

#### Notes

Plugins: [`vision_position`](https://index.ros.org/p/mavros_extras)
and [`vision_speed`](https://index.ros.org/p/mavros_extras) moved to
[mavros_extras](https://index.ros.org/p/mavros_extras).

## Plugins_0.12-0.15

### Plugins for mavros 0.12-0.15

Standard plugin set for mavros version 0.12---0.15.

#### 3dr_radio

Publish 3DR Radio status to diagnostics and topic.

##### Published Topics

- `~radio_status`
  ([mavros_msgs/msg/RadioStatus](https://docs.ros.org/en/rolling/p/mavros_msgs/msg/RadioStatus.html)):
  Status received from modem, same as RADIO_STATUS message.

#### actuator_control

Sends acruator commands to FCU.

##### Subscribed Topics

- `~actuator_control`
  ([mavros_msgs/msg/ActuatorControl](https://docs.ros.org/en/rolling/p/mavros_msgs/msg/ActuatorControl.html)):
  actuator command

#### command

Send COMMAND_LONG to FCU.

##### Services

- `~cmd/command`
  ([mavros_msgs/srv/CommandLong](https://docs.ros.org/en/rolling/p/mavros_msgs/srv/CommandLong.html)):
  Send any COMMAND_LONG to FCU.
- `~cmd/command_int`
  ([mavros_msgs/srv/CommandInt](https://docs.ros.org/en/rolling/p/mavros_msgs/srv/CommandInt.html)):
  Send any COMMAND_INT to FCU.
- `~cmd/arming`
  ([mavros_msgs/srv/CommandBool](https://docs.ros.org/en/rolling/p/mavros_msgs/srv/CommandBool.html)):
  Change Arming status.
- `~cmd/set_home`
  ([mavros_msgs/srv/CommandHome](https://docs.ros.org/en/rolling/p/mavros_msgs/srv/CommandHome.html)):
  Change HOME location.
- `~cmd/guided_enable`
  ([mavros_msgs/srv/CommandBool](https://docs.ros.org/en/rolling/p/mavros_msgs/srv/CommandBool.html)):
  Enable guided mode by sending MAV_CMD_NAV_GUIDED_ENABLE command.
- `~cmd/takeoff`
  ([mavros_msgs/srv/CommandTOL](https://docs.ros.org/en/rolling/p/mavros_msgs/srv/CommandTOL.html)):
  Send takeoff command.
- `~cmd/land`
  ([mavros_msgs/srv/CommandTOL](https://docs.ros.org/en/rolling/p/mavros_msgs/srv/CommandTOL.html)):
  Send land command.
- `~cmd/trigger_control`
  ([mavros_msgs/srv/CommandTriggerControl](https://docs.ros.org/en/rolling/p/mavros_msgs/srv/CommandTriggerControl.html)):
  Send camera trigger control command.

##### Parameters

- `~cmd/use_comp_id_system_control` (`bool`, default: `false`): Use
  `SYSTEM_CONTROL` component id instead of mavros target component.

#### ftp

Support plugin for MAVLink-FTP (**PX4**).

##### Services

- `~ftp/open`
  ([mavros_msgs/srv/FileOpen](https://docs.ros.org/en/rolling/p/mavros_msgs/srv/FileOpen.html)):
  Open file (acquire session).
- `~ftp/close`
  ([mavros_msgs/srv/FileClose](https://docs.ros.org/en/rolling/p/mavros_msgs/srv/FileClose.html)):
  Close file (release session).
- `~ftp/read`
  ([mavros_msgs/srv/FileRead](https://docs.ros.org/en/rolling/p/mavros_msgs/srv/FileRead.html)):
  Read from opened file.
- `~ftp/write`
  ([mavros_msgs/srv/FileWrite](https://docs.ros.org/en/rolling/p/mavros_msgs/srv/FileWrite.html)):
  Write to opened file.
- `~ftp/list`
  ([mavros_msgs/srv/FileList](https://docs.ros.org/en/rolling/p/mavros_msgs/srv/FileList.html)):
  List directory.
- `~ftp/truncate`
  ([mavros_msgs/srv/FileTruncate](https://docs.ros.org/en/rolling/p/mavros_msgs/srv/FileTruncate.html)):
  Truncate file.
- `~ftp/remove`
  ([mavros_msgs/srv/FileRemove](https://docs.ros.org/en/rolling/p/mavros_msgs/srv/FileRemove.html)):
  Unlink file.
- `~ftp/rename`
  ([mavros_msgs/srv/FileRename](https://docs.ros.org/en/rolling/p/mavros_msgs/srv/FileRename.html)):
  Rename file/directory.
- `~ftp/mkdir`
  ([mavros_msgs/srv/FileMakeDir](https://docs.ros.org/en/rolling/p/mavros_msgs/srv/FileMakeDir.html)):
  Create directory.
- `~ftp/rmdir`
  ([mavros_msgs/srv/FileRemoveDir](https://docs.ros.org/en/rolling/p/mavros_msgs/srv/FileRemoveDir.html)):
  Remove directory.
- `~ftp/checksum`
  ([mavros_msgs/srv/FileChecksum](https://docs.ros.org/en/rolling/p/mavros_msgs/srv/FileChecksum.html)):
  Request to calculate CRC32 of file on FCU.
- `~ftp/reset`
  ([std_srvs/srv/Empty](https://docs.ros.org/en/rolling/p/std_srvs/srv/Empty.html)):
  Reset FCU server (dangerous).

#### global_position

Publish global position information fused by FCU and raw GPS data.

##### Published Topics

- `~global_position/global`
  ([sensor_msgs/msg/NavSatFix](https://docs.ros.org/en/rolling/p/sensor_msgs/msg/NavSatFix.html)):
  GPS Fix.
- `~global_position/local`
  ([geometry_msgs/msg/PoseWithCovarianceStamped](https://docs.ros.org/en/rolling/p/geometry_msgs/msg/PoseWithCovarianceStamped.html)):
  UTM coords.
- `~global_position/gp_vel`
  ([geometry_msgs/msg/TwistStamped](https://docs.ros.org/en/rolling/p/geometry_msgs/msg/TwistStamped.html)):
  Velocity fused by FCU.
- `~global_position/rel_alt`
  ([std_msgs/msg/Float64](https://docs.ros.org/en/rolling/p/std_msgs/msg/Float64.html)):
  Relative altitude.
- `~global_position/compass_hdg`
  ([std_msgs/msg/Float64](https://docs.ros.org/en/rolling/p/std_msgs/msg/Float64.html)):
  Compass heading in degrees.
- `~global_position/raw/fix`
  ([sensor_msgs/msg/NavSatFix](https://docs.ros.org/en/rolling/p/sensor_msgs/msg/NavSatFix.html)):
  GPS position fix reported by the device.
- `~global_position/raw/gps_vel`
  ([geometry_msgs/msg/TwistStamped](https://docs.ros.org/en/rolling/p/geometry_msgs/msg/TwistStamped.html)):
  Velocity output from the GPS device.

##### Parameters

- `~global_position/frame_id` (`string`, default: `fcu`): frame_id for
  messages.
- `~global_position/tf/send` (`bool`, default: `true`): Send or not
  local UTM coords via TF?
- `~global_position/tf/frame_id` (`string`, default: `local_origin`):
  frame_id for TF.
- `~global_position/tf/child_frame_id` (`string`, default: `fcu_utm`):
  Child frame_id for TF.

#### imu_pub

Publish IMU state

##### Published Topics

- `~imu/data`
  ([sensor_msgs/msg/Imu](https://docs.ros.org/en/rolling/p/sensor_msgs/msg/Imu.html)):
  Imu data, orientation computed by FCU
- `~imu/data_raw`
  ([sensor_msgs/msg/Imu](https://docs.ros.org/en/rolling/p/sensor_msgs/msg/Imu.html)):
  Raw IMU data without orientation
- `~imu/mag`
  ([sensor_msgs/msg/MagneticField](https://docs.ros.org/en/rolling/p/sensor_msgs/msg/MagneticField.html)):
  FCU compass data
- `~imu/temperature`
  ([sensor_msgs/msg/Temperature](https://docs.ros.org/en/rolling/p/sensor_msgs/msg/Temperature.html)):
  Temperature reported by FCU (usually from barometer)
- `~imu/atm_pressure`
  ([sensor_msgs/msg/FluidPressure](https://docs.ros.org/en/rolling/p/sensor_msgs/msg/FluidPressure.html)):
  Air pressure.

##### Parameters

- `~imu/frame_id` (`string`, default: `fcu`): Frame ID for this plugin.
- `~imu/linear_acceleration_stdev` (`double`, default: `0.0003`):
  Gyro's standard deviation
- `~imu/angular_velocity_stdev` (`double`, default: `!dec 0.02`):
  Accel's standard deviation
- `~imu/orientation_stdev` (`double`, default: `1.0`): Standard
  deviation for IMU.orientation
- `~imu/magnetic_stdev` (`double`, default: `0.0`): Standard deviation
  for magnetic field message (undefined if: 0.0)

#### local_position

Publish LOCAL_POSITION_NED in [TF](https://index.ros.org/p/tf) and
PoseStamped topic.

##### Published Topics

- `~local_position/local`
  ([geometry_msgs/msg/PoseStamped](https://docs.ros.org/en/rolling/p/geometry_msgs/msg/PoseStamped.html)):
  Local position from FCU.

##### Parameters

- `~local_position/frame_id` (`string`, default: `fcu`): frame_id for
  message.
- `~local_position/tf/send` (`bool`, default: `true`): TF send switch.
- `~local_position/tf/frame_id` (`string`, default: `local_origin`):
  Origin frame_id for TF.
- `~local_position/tf/child_frame_id` (`string`, default: `fcu`): Child
  frame_id for TF.

#### manual_control

Publish MANUAL_CONTROL message (user input).

##### Published Topics

- `~manual_control/control`
  ([mavros_msgs/msg/ManualControl](https://docs.ros.org/en/rolling/p/mavros_msgs/msg/ManualControl.html)):
  RC Rx, interpreted and normalized.

#### param

Allows to access to FCU parameters and map it to ROS parameters in
`param/`.

##### Services

- `~param/pull`
  ([mavros_msgs/srv/ParamPull](https://docs.ros.org/en/rolling/p/mavros_msgs/srv/ParamPull.html)):
  Request parameter from device (or internal cache).
- `~param/push`
  ([mavros_msgs/srv/ParamPush](https://docs.ros.org/en/rolling/p/mavros_msgs/srv/ParamPush.html)):
  Request send parameters from ROS to FCU.
- `~param/get`
  ([mavros_msgs/srv/ParamGet](https://docs.ros.org/en/rolling/p/mavros_msgs/srv/ParamGet.html)):
  Return FCU parameter value.
- `~param/set`
  ([mavros_msgs/srv/ParamSet](https://docs.ros.org/en/rolling/p/mavros_msgs/srv/ParamSet.html)):
  Set parameter on FCU immidiatly.

#### rc_io

Publish RC receiver inputs.

##### Subscribed Topics

- `~rc/override`
  ([mavros_msgs/msg/OverrideRCIn](https://docs.ros.org/en/rolling/p/mavros_msgs/msg/OverrideRCIn.html)):
  Send RC override message to FCU. **APM** only. Requires setup FCU
  param `SYSID_MYGCS` to match mavros system id.

##### Published Topics

- `~rc/in`
  ([mavros_msgs/msg/RCIn](https://docs.ros.org/en/rolling/p/mavros_msgs/msg/RCIn.html)):
  Publish RC inputs (in raw milliseconds)
- `~rc/out`
  ([mavros_msgs/msg/RCOut](https://docs.ros.org/en/rolling/p/mavros_msgs/msg/RCOut.html)):
  Publish FCU servo outputs

#### safety_area

Sends safety allowed area to FCU. Initial area can be loaded from
parameters.

##### Subscribed Topics

- `~safety_area/set`
  ([geometry_msgs/msg/PolygonStamped](https://docs.ros.org/en/rolling/p/geometry_msgs/msg/PolygonStamped.html)):
  Volumetric area described by two corners.

##### Parameters

- `~safety_area/p1/x` (`double`): Corner 1 X.
- `~safety_area/p1/y` (`double`): Corner 1 Y.
- `~safety_area/p1/z` (`double`): Corner 1 Z.
- `~safety_area/p2/x` (`double`): Corner 2 X.
- `~safety_area/p2/y` (`double`): Corner 2 Y.
- `~safety_area/p2/z` (`double`): Corner 2 Z.

#### setpoint_accel

Send acceleration setpoint.

##### Subscribed Topics

- `~setpoint_accel/accel`
  ([geometry_msgs/msg/Vector3Stamped](https://docs.ros.org/en/rolling/p/geometry_msgs/msg/Vector3Stamped.html)):
  Acceleration or force setpoint vector.

##### Parameters

- `~setpoint_accel/send_force` (`bool`): Send force setpoint.

#### setpoint_attitude

Send attitude setpoint using SET_ATTITUDE_TARGET.

##### Subscribed Topics

- `~setpoint_attitude/cmd_vel`
  ([geometry_msgs/msg/TwistStamped](https://docs.ros.org/en/rolling/p/geometry_msgs/msg/TwistStamped.html)):
  Send angular velocity.
- `~setpoint_attitude/attitude`
  ([geometry_msgs/msg/PoseStamped](https://docs.ros.org/en/rolling/p/geometry_msgs/msg/PoseStamped.html)):
  Send attitude setpoint.

##### Parameters

- `~setpoint_attitude/reverse_throttle` (`bool`, default: `false`):
  Allow to send -1.0 throttle or not.
- `~setpoint_attitude/tf/listen` (`bool`, default: `false`): TF listen
  switch. Disable topics if enabled.
- `~setpoint_attutude/tf/frame_id` (`string`, default: `local_origin`):
  Origin frame_id for TF.
- `~setpoint_attitude/tf/child_frame_id` (`string`, default:
  `attitude`): Child frame_id for TF.
- `~setpoint_attitude/tf/rate_limit` (`double`, default: `10.0`): Rate
  limit for TF listener \[Hz\].

#### setpoint_position

Sent position setpoint using SET_POSITION_TARGET_LOCAL_NED.

##### Subscribed Topics

- `~setpoint_position/local`
  ([geometry_msgs/msg/PoseStamped](https://docs.ros.org/en/rolling/p/geometry_msgs/msg/PoseStamped.html)):
  Setpoint position. Orientation field not used.

##### Parameters

- `~setpoint_position/tf/listen` (`bool`, default: `false`): TF listen
  switch. Disable topic if enabled.
- `~setpoint_position/tf/frame_id` (`string`, default: `local_origin`):
  Origin frame_id for TF.
- `~setpoint_position/tf/child_frame_id` (`string`, default:
  `setpoint`): Child frame_id for TF.
- `~setpoint_position/tf/rate_limit` (`double`, default: `50.0`): Rate
  limit for TF listener \[Hz\].

#### setpoint_velocity

Send velocity setpoint to FCU.

##### Subscribed Topics

- `~setpoint_velocity/cmd_vel`
  ([geometry_msgs/msg/TwistStamped](https://docs.ros.org/en/rolling/p/geometry_msgs/msg/TwistStamped.html)):
  Velocity setpoint.

#### sys_status

System status plugin. Handles FCU detection. **REQUIRED** never
blacklist it!.

##### Published Topics

- `~state`
  ([mavros_msgs/msg/State](https://docs.ros.org/en/rolling/p/mavros_msgs/msg/State.html)):
  FCU state
- `~battery`
  ([mavros_msgs/msg/BatteryStatus](https://docs.ros.org/en/rolling/p/mavros_msgs/msg/BatteryStatus.html)):
  FCU battery status report.

##### Services

- `~set_stream_rate`
  ([mavros_msgs/srv/StreamRate](https://docs.ros.org/en/rolling/p/mavros_msgs/srv/StreamRate.html)):
  Send stream rate request to FCU.
- `~set_mode`
  ([mavros_msgs/srv/SetMode](https://docs.ros.org/en/rolling/p/mavros_msgs/srv/SetMode.html)):
  Set FCU operation mode. See custom mode identifiers at
  [modes page](#custommodes).

##### Parameters

- `~conn/timeout` (`double`, default: `30.0`): Connection time out in
  seconds.
- `~conn/heartbeat_rate` (`double`, default: `0.0`): Send HEARTBEAT
  message rate \[Hz\] (or disabled if 0.0)
- `~sys/min_voltage` (`double`, default: `6.0`): Minimal battery voltage
  for diagnostics.
- `~sys/disable_diag` (`bool`, default: `false`): Disable all diag
  except HEARTBEAT message.

#### sys_time

System time plugin. Does time syncronization on **PX4**.

##### Published Topics

- `~time_reference`
  ([sensor_msgs/msg/TimeReference](https://docs.ros.org/en/rolling/p/sensor_msgs/msg/TimeReference.html)):
  Time reference computed from SYSTEM_TIME.

##### Parameters

- `~conn/system_time_rate` (`double`, default: `0.0`): Send
  `SYSTEM_TIME` to device rate \[Hz\] (disabled if 0.0).
- `~conn/timesync_rate` (`double`, default: `0.0`): TIMESYNC rate.
  **PX4** only.
- `~time/time_ref_source` (`string`, default: `"fcu"`): Ref source for
  time_reference message.
- `~time/timesync_avg_alpha` (`double`, default: `0.6`): Alpha for
  exponential moving average.

#### vfr_hud

Publish VFR_HUD and WIND messages.

##### Published Topics

- `~vfr_hud`
  ([mavros_msgs/msg/VFR_HUD](https://docs.ros.org/en/rolling/p/mavros_msgs/msg/VFR_HUD.html)):
  Data for HUD.
- `~wind_estimation`
  ([geometry_msgs/msg/TwistStamped](https://docs.ros.org/en/rolling/p/geometry_msgs/msg/TwistStamped.html)):
  Wind estimation from FCU (**APM**).

#### waypoint

Allows to access to FCU mission (waypoints).

##### Published Topics

- `~mission/waypoints`
  ([mavros_msgs/msg/WaypointList](https://docs.ros.org/en/rolling/p/mavros_msgs/msg/WaypointList.html)):
  Current waypoint table. Updates on changes.

##### Services

- `~mission/pull`
  ([mavros_msgs/srv/WaypointPull](https://docs.ros.org/en/rolling/p/mavros_msgs/srv/WaypointPull.html)):
  Request update waypoint list.
- `~mission/push`
  ([mavros_msgs/srv/WaypointPush](https://docs.ros.org/en/rolling/p/mavros_msgs/srv/WaypointPush.html)):
  Send new waypoint table.
- `~mission/clear`
  ([mavros_msgs/srv/WaypointClear](https://docs.ros.org/en/rolling/p/mavros_msgs/srv/WaypointClear.html)):
  Clear mission on FCU.
- `~mission/set_current`
  ([mavros_msgs/srv/WaypointSetCurrent](https://docs.ros.org/en/rolling/p/mavros_msgs/srv/WaypointSetCurrent.html)):
  Set current seq. number in list.
- `~mission/goto`
  ([mavros_msgs/srv/WaypointGOTO](https://docs.ros.org/en/rolling/p/mavros_msgs/srv/WaypointGOTO.html)):
  Send goto point (APM specific).

##### Parameters

- `~mission/pull_after_gcs` (`bool`, default: `false`): Defines pull or
  not waypoints if detected GCS activity.

#### Notes

Plugins: [`vision_position`](https://index.ros.org/p/mavros_extras)
and [`vision_speed`](https://index.ros.org/p/mavros_extras) moved to
[mavros_extras](https://index.ros.org/p/mavros_extras). GPS and
global_position plugins are merged. TF params moved to `tf/`
subnamespace.

## Plugins_0.16-0.17

### Plugins for mavros 0.16-0.17

Standard plugin set for mavros version 0.16---0.17.

#### 3dr_radio

Publish 3DR Radio status to diagnostics and topic.

##### Published Topics

- `~radio_status`
  ([mavros_msgs/msg/RadioStatus](https://docs.ros.org/en/rolling/p/mavros_msgs/msg/RadioStatus.html)):
  Status received from modem, same as RADIO_STATUS message.

#### altitude

Publish altitude information.

##### Published Topics

- `~altitude`
  ([mavros_msgs/msg/Altitude](https://docs.ros.org/en/rolling/p/mavros_msgs/msg/Altitude.html)):
  Direct copy of altitude data provided by Mavlink.

##### Parameters

- `~frame_id` (`string`, default: `"map"`): frame for altitude messages

#### actuator_control

Sends acruator commands to FCU.

##### Subscribed Topics

- `~actuator_control`
  ([mavros_msgs/msg/ActuatorControl](https://docs.ros.org/en/rolling/p/mavros_msgs/msg/ActuatorControl.html)):
  actuator command

#### command

Send COMMAND_LONG to FCU.

##### Services

- `~cmd/command`
  ([mavros_msgs/srv/CommandLong](https://docs.ros.org/en/rolling/p/mavros_msgs/srv/CommandLong.html)):
  Send any COMMAND_LONG to FCU.
- `~cmd/command_int`
  ([mavros_msgs/srv/CommandInt](https://docs.ros.org/en/rolling/p/mavros_msgs/srv/CommandInt.html)):
  Send any COMMAND_INT to FCU.
- `~cmd/arming`
  ([mavros_msgs/srv/CommandBool](https://docs.ros.org/en/rolling/p/mavros_msgs/srv/CommandBool.html)):
  Change Arming status.
- `~cmd/set_home`
  ([mavros_msgs/srv/CommandHome](https://docs.ros.org/en/rolling/p/mavros_msgs/srv/CommandHome.html)):
  Change HOME location.
- `~cmd/takeoff`
  ([mavros_msgs/srv/CommandTOL](https://docs.ros.org/en/rolling/p/mavros_msgs/srv/CommandTOL.html)):
  Send takeoff command.
- `~cmd/land`
  ([mavros_msgs/srv/CommandTOL](https://docs.ros.org/en/rolling/p/mavros_msgs/srv/CommandTOL.html)):
  Send land command.
- `~cmd/trigger_control`
  ([mavros_msgs/srv/CommandTriggerControl](https://docs.ros.org/en/rolling/p/mavros_msgs/srv/CommandTriggerControl.html)):
  Send camera trigger control command.

##### Parameters

- `~cmd/use_comp_id_system_control` (`bool`, default: `false`): Use
  `SYSTEM_CONTROL` component id instead of mavros target component.

#### ftp

Support plugin for MAVLink-FTP (**PX4**).

##### Services

- `~ftp/open`
  ([mavros_msgs/srv/FileOpen](https://docs.ros.org/en/rolling/p/mavros_msgs/srv/FileOpen.html)):
  Open file (acquire session).
- `~ftp/close`
  ([mavros_msgs/srv/FileClose](https://docs.ros.org/en/rolling/p/mavros_msgs/srv/FileClose.html)):
  Close file (release session).
- `~ftp/read`
  ([mavros_msgs/srv/FileRead](https://docs.ros.org/en/rolling/p/mavros_msgs/srv/FileRead.html)):
  Read from opened file.
- `~ftp/write`
  ([mavros_msgs/srv/FileWrite](https://docs.ros.org/en/rolling/p/mavros_msgs/srv/FileWrite.html)):
  Write to opened file.
- `~ftp/list`
  ([mavros_msgs/srv/FileList](https://docs.ros.org/en/rolling/p/mavros_msgs/srv/FileList.html)):
  List directory.
- `~ftp/truncate`
  ([mavros_msgs/srv/FileTruncate](https://docs.ros.org/en/rolling/p/mavros_msgs/srv/FileTruncate.html)):
  Truncate file.
- `~ftp/remove`
  ([mavros_msgs/srv/FileRemove](https://docs.ros.org/en/rolling/p/mavros_msgs/srv/FileRemove.html)):
  Unlink file.
- `~ftp/rename`
  ([mavros_msgs/srv/FileRename](https://docs.ros.org/en/rolling/p/mavros_msgs/srv/FileRename.html)):
  Rename file/directory.
- `~ftp/mkdir`
  ([mavros_msgs/srv/FileMakeDir](https://docs.ros.org/en/rolling/p/mavros_msgs/srv/FileMakeDir.html)):
  Create directory.
- `~ftp/rmdir`
  ([mavros_msgs/srv/FileRemoveDir](https://docs.ros.org/en/rolling/p/mavros_msgs/srv/FileRemoveDir.html)):
  Remove directory.
- `~ftp/checksum`
  ([mavros_msgs/srv/FileChecksum](https://docs.ros.org/en/rolling/p/mavros_msgs/srv/FileChecksum.html)):
  Request to calculate CRC32 of file on FCU.
- `~ftp/reset`
  ([std_srvs/srv/Empty](https://docs.ros.org/en/rolling/p/std_srvs/srv/Empty.html)):
  Reset FCU server (dangerous).

#### global_position

Publish global position information fused by FCU and raw GPS data.

##### Published Topics

- `~global_position/global`
  ([sensor_msgs/msg/NavSatFix](https://docs.ros.org/en/rolling/p/sensor_msgs/msg/NavSatFix.html)):
  GPS Fix.
- `~global_position/local`
  ([geometry_msgs/msg/PoseWithCovarianceStamped](https://docs.ros.org/en/rolling/p/geometry_msgs/msg/PoseWithCovarianceStamped.html)):
  UTM coords.
- `~global_position/gp_vel`
  ([geometry_msgs/msg/TwistStamped](https://docs.ros.org/en/rolling/p/geometry_msgs/msg/TwistStamped.html)):
  Velocity fused by FCU.
- `~global_position/rel_alt`
  ([std_msgs/msg/Float64](https://docs.ros.org/en/rolling/p/std_msgs/msg/Float64.html)):
  Relative altitude.
- `~global_position/compass_hdg`
  ([std_msgs/msg/Float64](https://docs.ros.org/en/rolling/p/std_msgs/msg/Float64.html)):
  Compass heading in degrees.
- `~global_position/raw/fix`
  ([sensor_msgs/msg/NavSatFix](https://docs.ros.org/en/rolling/p/sensor_msgs/msg/NavSatFix.html)):
  GPS position fix reported by the device.
- `~global_position/raw/gps_vel`
  ([geometry_msgs/msg/TwistStamped](https://docs.ros.org/en/rolling/p/geometry_msgs/msg/TwistStamped.html)):
  Velocity output from the GPS device.

##### Parameters

- `~global_position/frame_id` (`string`, default: `fcu`): frame_id for
  messages.
- `~global_position/tf/send` (`bool`, default: `true`): Send or not
  local UTM coords via TF?
- `~global_position/tf/frame_id` (`string`, default: `local_origin`):
  frame_id for TF.
- `~global_position/tf/child_frame_id` (`string`, default: `fcu_utm`):
  Child frame_id for TF.

#### imu_pub

Publish IMU state

##### Published Topics

- `~imu/data`
  ([sensor_msgs/msg/Imu](https://docs.ros.org/en/rolling/p/sensor_msgs/msg/Imu.html)):
  Imu data, orientation computed by FCU
- `~imu/data_raw`
  ([sensor_msgs/msg/Imu](https://docs.ros.org/en/rolling/p/sensor_msgs/msg/Imu.html)):
  Raw IMU data without orientation
- `~imu/mag`
  ([sensor_msgs/msg/MagneticField](https://docs.ros.org/en/rolling/p/sensor_msgs/msg/MagneticField.html)):
  FCU compass data
- `~imu/temperature`
  ([sensor_msgs/msg/Temperature](https://docs.ros.org/en/rolling/p/sensor_msgs/msg/Temperature.html)):
  Temperature reported by FCU (usually from barometer)
- `~imu/atm_pressure`
  ([sensor_msgs/msg/FluidPressure](https://docs.ros.org/en/rolling/p/sensor_msgs/msg/FluidPressure.html)):
  Air pressure.

##### Parameters

- `~imu/frame_id` (`string`, default: `fcu`): Frame ID for this plugin.
- `~imu/linear_acceleration_stdev` (`double`, default: `0.0003`):
  Gyro's standard deviation
- `~imu/angular_velocity_stdev` (`double`, default: `!dec 0.02`):
  Accel's standard deviation
- `~imu/orientation_stdev` (`double`, default: `1.0`): Standard
  deviation for IMU.orientation
- `~imu/magnetic_stdev` (`double`, default: `0.0`): Standard deviation
  for magnetic field message (undefined if: 0.0)

#### local_position

Publish LOCAL_POSITION_NED in [TF](https://index.ros.org/p/tf) and
PoseStamped topic.

##### Published Topics

- `~local_position/pose`
  ([geometry_msgs/msg/PoseStamped](https://docs.ros.org/en/rolling/p/geometry_msgs/msg/PoseStamped.html)):
  Local position from FCU.
- `~local_position/velocity`
  ([geometry_msgs/msg/TwistStamped](https://docs.ros.org/en/rolling/p/geometry_msgs/msg/TwistStamped.html)):
  Velocity data from FCU.

##### Parameters

- `~local_position/frame_id` (`string`, default: `fcu`): frame_id for
  message.
- `~local_position/tf/send` (`bool`, default: `true`): TF send switch.
- `~local_position/tf/frame_id` (`string`, default: `local_origin`):
  Origin frame_id for TF.
- `~local_position/tf/child_frame_id` (`string`, default: `fcu`): Child
  frame_id for TF.

#### manual_control

Publish MANUAL_CONTROL message (user input).

##### Published Topics

- `~manual_control/control`
  ([mavros_msgs/msg/ManualControl](https://docs.ros.org/en/rolling/p/mavros_msgs/msg/ManualControl.html)):
  RC Rx, interpreted and normalized.

#### param

Allows to access to FCU parameters and map it to ROS parameters in
`param/`.

##### Services

- `~param/pull`
  ([mavros_msgs/srv/ParamPull](https://docs.ros.org/en/rolling/p/mavros_msgs/srv/ParamPull.html)):
  Request parameter from device (or internal cache).
- `~param/push`
  ([mavros_msgs/srv/ParamPush](https://docs.ros.org/en/rolling/p/mavros_msgs/srv/ParamPush.html)):
  Request send parameters from ROS to FCU.
- `~param/get`
  ([mavros_msgs/srv/ParamGet](https://docs.ros.org/en/rolling/p/mavros_msgs/srv/ParamGet.html)):
  Return FCU parameter value.
- `~param/set`
  ([mavros_msgs/srv/ParamSet](https://docs.ros.org/en/rolling/p/mavros_msgs/srv/ParamSet.html)):
  Set parameter on FCU immidiatly.

#### rc_io

Publish RC receiver inputs.

##### Subscribed Topics

- `~rc/override`
  ([mavros_msgs/msg/OverrideRCIn](https://docs.ros.org/en/rolling/p/mavros_msgs/msg/OverrideRCIn.html)):
  Send RC override message to FCU. **APM** and **PX4** only. APM
  requires setup FCU param `SYSID_MYGCS` to match mavros system id.
  **Not recommended** to use in automatic control because lack of safety
  mechanisms. Use one of setpoint plugins and OFFBOARD mode.

##### Published Topics

- `~rc/in`
  ([mavros_msgs/msg/RCIn](https://docs.ros.org/en/rolling/p/mavros_msgs/msg/RCIn.html)):
  Publish RC inputs (in raw milliseconds)
- `~rc/out`
  ([mavros_msgs/msg/RCOut](https://docs.ros.org/en/rolling/p/mavros_msgs/msg/RCOut.html)):
  Publish FCU servo outputs

#### safety_area

Sends safety allowed area to FCU. Initial area can be loaded from
parameters.

##### Subscribed Topics

- `~safety_area/set`
  ([geometry_msgs/msg/PolygonStamped](https://docs.ros.org/en/rolling/p/geometry_msgs/msg/PolygonStamped.html)):
  Volumetric area described by two corners.

##### Parameters

- `~safety_area/p1/x` (`double`): Corner 1 X.
- `~safety_area/p1/y` (`double`): Corner 1 Y.
- `~safety_area/p1/z` (`double`): Corner 1 Z.
- `~safety_area/p2/x` (`double`): Corner 2 X.
- `~safety_area/p2/y` (`double`): Corner 2 Y.
- `~safety_area/p2/z` (`double`): Corner 2 Z.

#### setpoint_accel

Send acceleration setpoint.

##### Subscribed Topics

- `~setpoint_accel/accel`
  ([geometry_msgs/msg/Vector3Stamped](https://docs.ros.org/en/rolling/p/geometry_msgs/msg/Vector3Stamped.html)):
  Acceleration or force setpoint vector.

##### Parameters

- `~setpoint_accel/send_force` (`bool`): Send force setpoint.

#### setpoint_attitude

Send attitude setpoint using SET_ATTITUDE_TARGET.

##### Subscribed Topics

- `~setpoint_attitude/cmd_vel`
  ([geometry_msgs/msg/TwistStamped](https://docs.ros.org/en/rolling/p/geometry_msgs/msg/TwistStamped.html)):
  Send angular velocity.
- `~setpoint_attitude/attitude`
  ([geometry_msgs/msg/PoseStamped](https://docs.ros.org/en/rolling/p/geometry_msgs/msg/PoseStamped.html)):
  Send attitude setpoint.

##### Parameters

- `~setpoint_attitude/reverse_throttle` (`bool`, default: `false`):
  Allow to send -1.0 throttle or not.
- `~setpoint_attitude/tf/listen` (`bool`, default: `false`): TF listen
  switch. Disable topics if enabled.
- `~setpoint_attutude/tf/frame_id` (`string`, default: `local_origin`):
  Origin frame_id for TF.
- `~setpoint_attitude/tf/child_frame_id` (`string`, default:
  `attitude`): Child frame_id for TF.
- `~setpoint_attitude/tf/rate_limit` (`double`, default: `10.0`): Rate
  limit for TF listener \[Hz\].

#### setpoint_position

Sent position setpoint using SET_POSITION_TARGET_LOCAL_NED.

##### Subscribed Topics

- `~setpoint_position/local`
  ([geometry_msgs/msg/PoseStamped](https://docs.ros.org/en/rolling/p/geometry_msgs/msg/PoseStamped.html)):
  Setpoint position. Only YAW axis extracted from orientation field.

##### Parameters

- `~setpoint_position/tf/listen` (`bool`, default: `false`): TF listen
  switch. Disable topic if enabled.
- `~setpoint_position/tf/frame_id` (`string`, default: `local_origin`):
  Origin frame_id for TF.
- `~setpoint_position/tf/child_frame_id` (`string`, default:
  `setpoint`): Child frame_id for TF.
- `~setpoint_position/tf/rate_limit` (`double`, default: `50.0`): Rate
  limit for TF listener \[Hz\].

#### setpoint_raw

Send RAW setpoint messages to FCU and provide loopback topics (PX4).

##### Subscribed Topics

- `~setpoint_raw/local`
  ([mavros_msgs/msg/PositionTarget](https://docs.ros.org/en/rolling/p/mavros_msgs/msg/PositionTarget.html)):
  Local position, velocity and acceleration setpoint.
- `~setpoint_raw/global`
  ([mavros_msgs/msg/GlobalPositionTarget](https://docs.ros.org/en/rolling/p/mavros_msgs/msg/GlobalPositionTarget.html)):
  Global position, velocity and acceleration setpoint.
- `~setpoint_raw/attitude`
  ([mavros_msgs/msg/AttitudeTarget](https://docs.ros.org/en/rolling/p/mavros_msgs/msg/AttitudeTarget.html)):
  Attitude, angular rate and thrust setpoint.

##### Published Topics

- `~setpoint_raw/target_local`
  ([mavros_msgs/msg/PositionTarget](https://docs.ros.org/en/rolling/p/mavros_msgs/msg/PositionTarget.html)):
  Local target loopback.
- `~setpoint_raw/target_global`
  ([mavros_msgs/msg/GlobalPositionTarget](https://docs.ros.org/en/rolling/p/mavros_msgs/msg/GlobalPositionTarget.html)):
  Global target loopback.
- `~setpoint_raw/target_attitude`
  ([mavros_msgs/msg/AttitudeTarget](https://docs.ros.org/en/rolling/p/mavros_msgs/msg/AttitudeTarget.html)):
  Attitude target loopback.

#### setpoint_velocity

Send velocity setpoint to FCU.

##### Subscribed Topics

- `~setpoint_velocity/cmd_vel`
  ([geometry_msgs/msg/TwistStamped](https://docs.ros.org/en/rolling/p/geometry_msgs/msg/TwistStamped.html)):
  Velocity setpoint.

#### sys_status

System status plugin. Handles FCU detection. **REQUIRED** never
blacklist it!.

##### Published Topics

- `~state`
  ([mavros_msgs/msg/State](https://docs.ros.org/en/rolling/p/mavros_msgs/msg/State.html)):
  FCU state
- `~battery`
  ([mavros_msgs/msg/BatteryStatus](https://docs.ros.org/en/rolling/p/mavros_msgs/msg/BatteryStatus.html)):
  FCU battery status report.
- `~extended_state`
  ([mavros_msgs/msg/ExtendedState](https://docs.ros.org/en/rolling/p/mavros_msgs/msg/ExtendedState.html)):
  Landing detector and VTOL state.

##### Services

- `~set_stream_rate`
  ([mavros_msgs/srv/StreamRate](https://docs.ros.org/en/rolling/p/mavros_msgs/srv/StreamRate.html)):
  Send stream rate request to FCU.
- `~set_mode`
  ([mavros_msgs/srv/SetMode](https://docs.ros.org/en/rolling/p/mavros_msgs/srv/SetMode.html)):
  Set FCU operation mode. See custom mode identifiers at
  [modes page](#custommodes).

##### Parameters

- `~conn/timeout` (`double`, default: `30.0`): Connection time out in
  seconds.
- `~conn/heartbeat_rate` (`double`, default: `0.0`): Send HEARTBEAT
  message rate \[Hz\] (or disabled if 0.0)
- `~sys/min_voltage` (`double`, default: `6.0`): Minimal battery voltage
  for diagnostics.
- `~sys/disable_diag` (`bool`, default: `false`): Disable all diag
  except HEARTBEAT message.

#### sys_time

System time plugin. Does time syncronization on **PX4**.

##### Published Topics

- `~time_reference`
  ([sensor_msgs/msg/TimeReference](https://docs.ros.org/en/rolling/p/sensor_msgs/msg/TimeReference.html)):
  Time reference computed from SYSTEM_TIME.

##### Parameters

- `~conn/system_time_rate` (`double`, default: `0.0`): Send
  `SYSTEM_TIME` to device rate \[Hz\] (disabled if 0.0).
- `~conn/timesync_rate` (`double`, default: `0.0`): TIMESYNC rate.
  **PX4** only.
- `~time/time_ref_source` (`string`, default: `"fcu"`): Ref source for
  time_reference message.
- `~time/timesync_avg_alpha` (`double`, default: `0.6`): Alpha for
  exponential moving average.

#### vfr_hud

Publish VFR_HUD and WIND messages.

##### Published Topics

- `~vfr_hud`
  ([mavros_msgs/msg/VFR_HUD](https://docs.ros.org/en/rolling/p/mavros_msgs/msg/VFR_HUD.html)):
  Data for HUD.
- `~wind_estimation`
  ([geometry_msgs/msg/TwistStamped](https://docs.ros.org/en/rolling/p/geometry_msgs/msg/TwistStamped.html)):
  Wind estimation from FCU (**APM**).

#### waypoint

Allows to access to FCU mission (waypoints).

##### Published Topics

- `~mission/waypoints`
  ([mavros_msgs/msg/WaypointList](https://docs.ros.org/en/rolling/p/mavros_msgs/msg/WaypointList.html)):
  Current waypoint table. Updates on changes.

##### Services

- `~mission/pull`
  ([mavros_msgs/srv/WaypointPull](https://docs.ros.org/en/rolling/p/mavros_msgs/srv/WaypointPull.html)):
  Request update waypoint list.
- `~mission/push`
  ([mavros_msgs/srv/WaypointPush](https://docs.ros.org/en/rolling/p/mavros_msgs/srv/WaypointPush.html)):
  Send new waypoint table.
- `~mission/clear`
  ([mavros_msgs/srv/WaypointClear](https://docs.ros.org/en/rolling/p/mavros_msgs/srv/WaypointClear.html)):
  Clear mission on FCU.
- `~mission/set_current`
  ([mavros_msgs/srv/WaypointSetCurrent](https://docs.ros.org/en/rolling/p/mavros_msgs/srv/WaypointSetCurrent.html)):
  Set current seq. number in list.

##### Parameters

- `~mission/pull_after_gcs` (`bool`, default: `false`): Defines pull or
  not waypoints if detected GCS activity.

#### Notes

Plugins: [`vision_position`](https://index.ros.org/p/mavros_extras)
and [`vision_speed`](https://index.ros.org/p/mavros_extras) moved to
[mavros_extras](https://index.ros.org/p/mavros_extras). GPS and
global_position plugins are merged. TF params moved to `tf/`
subnamespace. Waypoint GOTO service removed. Please use setpoint
plugins.

## FcuModes

1.  redirect mavros/CustomModes
