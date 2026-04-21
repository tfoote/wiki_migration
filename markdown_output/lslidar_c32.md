## Overview

This *lslidar_c32* package is a linux ROS driver for lslidar c32 from
Shenzhen Leishen Intelligence System Co, Ltd.

lslidar-c32 is a 16 channels hybird solid state lidar based on TOF
working principle. The maximum detection range is up to 200m (different
model has different maximum range).

-   Vertical viewing angle is from -15 degree to 15 degree
-   Horizontal viewing angle is 360 degree
-   Maximum angular resolution is 0.09 degree at 5Hz.
-   Normal angular resolution is 0.18 degree at 10Hz

This package is tested on Ubuntu 14.04 with ROS indigo and Ubuntu 16.04
with ROS kinetic.

## ROS

### lslidar_c32_msgs

Package contains self-defined ROS message type used for lslidar-c32

-   <<MsgLink(lslidar_c32_msgs/LslidarC32Packet)>> Original UDP
    packet block data
-   <<MsgLink(lslidar_c32_msgs/LslidarC32Point)>> Resolved point
    infomation
-   <<MsgLink(lslidar_c32_msgs/LslidarC32Scan)>> Point information
    for specific channel
-   <<MsgLink(lslidar_c32_msgs/LslidarC32Sweep)>> Whole point cloud
    data of 16 channels

### lslidar_c32_driver

#### Parameters

-   `lidar_ip` (`string`, `default: 192.168.1.200`) By default,
    the IP address of the device is 192.168.1.200.

```{=html}
<!-- -->
```
-   `device_port` (`int`, `default: 2368`) By default, the Port
    address of the device is 2368.

```{=html}
<!-- -->
```
-   `frame_id` (`string`, `default: laser`) The frame ID entry for
    the sent messages.

```{=html}
<!-- -->
```
-   `add_multicast` (`bool`, `default: false`) Whether using group
    multicast or not

```{=html}
<!-- -->
```
-   `group_ip` (`string`, `default: 234.2.3.2`) The group IP
    address of the device. Only useful when setting add_multicast to
    true

#### Published Topics

-   `lslidar_packets` (`lslidar_c32_msgs/LslidarC32Packet`) Each
    message corresponds to a lslidar packet sent by the device through
    the Ethernet.

### lslidar_c32_decoder

#### Parameters

-   `min_range` (`double`, `0.15`)

```{=html}
<!-- -->
```
-   `max_range` (`double`, `150.0`) Points outside this range will
    be removed.

```{=html}
<!-- -->
```
-   `frequency` (`frequency`, `10.0`) Note that the driver does
    not change the frequency of the sensor.

```{=html}
<!-- -->
```
-   `publish_point_cloud` (`bool`, `true`) If set to true, the
    decoder will send out a full revolution point cloud data

```{=html}
<!-- -->
```
-   `use_gps_ts` (`bool`, `false`) If set to true, the decoder
    synchronized with GPS timestamp

```{=html}
<!-- -->
```
-   `angle3_disable_min` (`double`, `-1`) Ignore 3D point cloud
    data from angle3_disable_min to angle3_disable_max; Default -1 means
    disable this function; Value should from 0 to 2\*pi

```{=html}
<!-- -->
```
-   `angle3_disable_max` (`double`, `-1`) Ignore 3D point cloud
    data from angle3_disable_min to angle3_disable_max; Default -1 means
    disable this function; Value should from 0 to 2\*pi

#### Published Topics

-   `lslidar_sweep` (`lslidar_c32_msgs/LslidarC32Sweep`) The message
    arranges the points within each sweep based on its scan index and
    azimuth.

```{=html}
<!-- -->
```
-   `lslidar_point_cloud` (`sensor_msgs/PointCloud2`) This is only
    published when the `publish_point_cloud` is set to `true` in the
    launch file.

#### Subscribed Topics

-   `lslidar_packets` (`lslidar_c32_msgs/LslidarC32Packet`) Each
    message corresponds to a lslidar packet sent by the device through
    the Ethernet.

## Usage

Before running lslidar-c32 driver, make sure you set up IP address
correctly. Using following command to check if device is communicating.
Replace `eth0` with your correct computer network interface

```
sudo tcpdump -i eth0
```

Running following commmand to launch lslidar c32 driver

```
roslaunch lslidar_c32_decoder lslidar_c32.launch --screen
```

Note that this launch file launches both the driver and the decoder,
which is the only launch file needed to be used.

## FAQ

### Cannot open UDP port

Make Sure your IP setting for bot device IP and computer IP is correct.
Default device IP is 192.168.1.200 and port is 2368. Default computer IP
is 192.168.1.102

### lslidar poll() timeout

Make Sure your IP setting for bot device IP and computer IP is correct.
Default device IP is 192.168.1.200 and port is 2368. Default computer IP
is 192.168.1.102

## Related Links

<http://en.leishen-lidar.com/>

<https://github.com/leishen-lidar/LSC32>
