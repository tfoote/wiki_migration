## Overview

This package provides basic device handling for Velodyne 3D LIDARs. For
a list of all supported models refer to the
[Supported Devices](#Supported Devices) section.

The driver publishes device-dependent
[velodyne_msgs/VelodyneScan](http://docs.ros.org/indigo/api/velodyne_msgs/html/msg/VelodyneScan.html)
data. The [velodyne_pointcloud](velodyne_pointcloud) package provides
nodes and nodelets to convert those data into more-convenient
\<\<MsgLink(sensor_msgs/PointCloud2)\>\> messages.

The
[API review](http://ros.org/wiki/velodyne/Reviews/2012-02-02_API_Review)
describes the evolution of these interfaces.

### Supported Devices

This driver supports all current Velodyne HDL-64E, HDL-32E, VLP-32C, and
VLP-16 models. There is little difference in the way it handles those
devices.

Different models publish packets at a different rate. Up through the ROS
Groovy release, no distinction was made between the HDL-64E, HDL-64E S2,
HDL-64E S2.1, and HDL-64E S3 variants. Unfortunately, the packet data
rates for those devices are not all the same.: the \`model\` parameter
now expects an exact name: \"VLP16\", \"32C\", \"32E\", \"64E\",
\"64E_S2\", \"64E_S2.1\", or \"64E_S3\", and generates the correct
packet rates for them.\
: The VLP-16 (\"Puck\") model is now supported.\
: The VLP-32C (\"Ultra Puck\") model is now supported.\
: The HDL-64E S3 model is now supported.

## ROS Nodes

-   **velodyne_node**\
    ROS node that captures Velodyne 3D LIDAR data and publishes it in
    raw form. This uses the same device driver class as
    [velodyne_driver/DriverNodelet](#DriverNodelet).
-   **Publishes**
-   *velodyne_packets*\
    type = velodyne_msgs/VelodyneScan\
    Velodyne data packets (typically for one entire revolution of the
    device) in the \`/velodyne\` frame of reference.
-   *diagnostics*\
    type = diagnostic_msgs/DiagnosticStatus\
    Diagnostic status information.

```{=html}
<!-- -->
```
-   **Parameters**
-   *frame_id*\
    type = string\
    default = velodyne\
    Transform frame ID for the device (resolved using \`tf_prefix\`, if
    defined).
-   *model*\
    type = string\
    default = \"64E\"\
    Device model: \"32E\", \"64E\", \"64E_S2\" or \"64E_S2.1\",:
    \"64E_S3\"
-   *npackets*\
    type = int\
    default = enough for a complete revolution\
    Number of packets to publish per message.
-   *pcap*\<\<BR\> type = string\
    default = use real device (empty)\
    PCAP dump input file name.
-   *rpm*\
    type = double\
    default = 600\
    Device rotation speed in Revolutions per Minute. **Note:** This does
    not modify the device configuration, it is just a value that the
    driver uses for calculating the packets per rotation.
-   *port*\
    type = int\
    default = 2368\
    : UDP port to read.
-   *device_ip*\
    type = string\
    default = use any device\
    : dotted decimal IP address of device.

#### Examples

Read the Velodyne HDL-64E (default) input socket as fast as possible.
Publish each complete revolution to \`velodyne_packets\`.

```
$ rosrun velodyne_driver velodyne_node
``` Read the Velodyne Velodyne HDL-32E input socket
as fast as possible. Publish each complete revolution to
\`velodyne_packets\`.

```
$ rosrun velodyne_driver velodyne_node _model:=32E
``` Read previously captured Velodyne packets from
dump.pcap file. Publish messages to \`velodyne_packets\` at
approximately 10 Hz rate. Dump files can be grabbed by \`libpcap\`,
Velodyne\'s DSR software, \`ethereal\`, \`wireshark\`, \`tcpdump\`, or
the [vdump](#vdump) command.

```
$ rosrun velodyne_driver velodyne_node _pcap:=dump.pcap
``` ```clearsilver
node.0 {
 name = DriverNodelet
 desc = ROS nodelet that captures Velodyne 3D LIDAR data and publishes it in raw form. This uses the same device driver class as [[http://ros.org/wiki/velodyne_driver#velodyne_node|velodyne_node]]. All topics and parameters are identical.
}
```

## Utility Commands

### vdump

The \`vdump\` command dumps raw data from the Velodyne LIDAR in PCAP
format. It is a shell script wrapper providing some obscure options for
the powerful \`tcpdump\` command.

Other methods of acquiring PCAP data include using \`tcpdump\` directly,
\`wireshark\`, Velodyne\'s DSR software, and programming with
\`libpcap\`.

#### Usage

```
rosrun velodyne_driver vdump <file_prefix> [ <interface> ]

        <file_prefix>   file name to dump (with 3-digit number suffix)
        <interface>     interface to read from (default: "eth0")
```

#### Examples

Dump Velodyne packets from the \`eth1\` interface to a series of files
named \`pcap-000\`, \`pcap-001\`, etc. Each file will be about 100MB.
The time span that a single 100MB file covers depends on packet size and
sampling rate of a particular model (for VLP-16 that is about 100
seconds worth of packets). Type \`\^C\` when finished.

```
$ rosrun velodyne_driver vdump pcap- eth1
```

## Launch File Examples

Start a \`velodyne_nodelet_manager\` process running the driver nodelet.
Other nodelets using the same nodelet manager process will have
zero-copy access to the raw data messages the driver publishes.

```
$ roslaunch velodyne_driver nodelet_manager.launch
``` Start a \`velodyne_nodelet_manager\` process
for a Velodyne HDL-32E.

```
$ roslaunch velodyne_driver nodelet_manager.launch model:=32E
``` Start a driver nodelet with input from
\`tcpdump.pcap\`, in the current directory. The \`pwd\` provides a full
path name, as required for \`roslaunch\`.

```
$ roslaunch velodyne_driver nodelet_manager.launch pcap:=$(pwd)/tcpdump.pcap
```
