## Overview

This package provides communication driver for various autopilots with
MAVLink communication protocol. Additional it provides UDP MAVLink
bridge for ground control stations (e.g. QGroundControl).

Main node can be extended by plugins (see [pluginlib](pluginlib)). See
also [mavros_extras](mavros_extras) package.

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

-   APM2.5/2.6 always APM stack
-   Pixhawk from manufacturer usually comes with APM stack
-   Pixhawk may be flashed by PX4 firmware using QGC or by upload make
    target.

If you unsure what firmware your FCU runs start apm.launch and see
[diagnostics](diagnostics). Starting from 0.11 mavros knows string
representation for autopilot mavlink enum. For older you shall manually
find autopilot type value in mavlink documentation.

## Connection URL

Connection defined by URL, you can use any supported type for FCU and
GCS.

Supported schemas:

-   Serial: \`/path/to/serial/device\[:baudrate\]\`
-   Serial:
    \`serial:*/path/to/serial/device\[:baudrate\]\[/?ids=sysid,compid\]\`
    \* Serial with hardware flow control:
    \`serial-hwfc:*/path/to/serial/device\[:baudrate\]\[?ids=sysid,compid\]\`
-   UDP:
    \`udp:*\[bind_host\]\[:port\]@\[remote_host\]\[:port\]\[/?ids=sysid,compid\]\`
    \* UDP Broadcast:
    \`udp-b:*\[bind_host\]\[:port\]@\[:port\]\[/?ids=sysid,compid\]\`
-   TCP client: \`tcp:*\[server_host\]\[:port\]\[/?ids=sysid,compid\]\`
    \* TCP server:
    \`tcp-l:*\[bind_host\]\[:port\]\[/?ids=sysid,compid\]\`

Notes:

-   ids from URL overrides ids given by parameters \`system_id\` and
    \`component_id\`.
-   \`baudrate\` default value is 57600
-   \`bind_host\` default value is \"0.0.0.0\" (IPv4 ANY)
-   \`remote_host\` by default unknown. mavros will awaiting data at
    bind_host:port
-   \`server_host\` default value is \"localhost\"
-   \`port\` default values: 14555 for UDP bind, 14550 for UDP remote,
    5760 for TCP
-   UDP broadcast used on discovery stage, later it switch to GCS
    address
-   Currently supports only IPv4.

## Utility commands

All utilities provides \`\<util\> \--help\` and \`\<util\> \<command\>
\--help\` information.

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

\'\'\'PX4\'\'\' only. ```
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
[mavros/CustomModes](mavros/CustomModes).

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

Note: this list for [0.18.0](mavros/Plugins) version. Older versions:
[0.6.0](mavros/Plugins_0.6), [0.7.0](mavros/Plugins_0.7),
[0.8.0](mavros/Plugins_0.8), [0.10.0](mavros/Plugins_0.10),
[0.11.0](mavros/Plugins_0.11),
[0.12.0 --- 0.15.0](mavros/Plugins_0.12-0.15),
[0.16.0 --- 0.17.0](mavros/Plugins_0.16-0.17).

\<\<Include(mavros/Plugins)\>\>
