# Roboception GenICam Convenience Layer

This package combines the Roboception convenience layer for images with
the GenICam reference implementation and a GigE Vision transport layer.
It is a self contained package that permits configuration and image
streaming of GenICam / GigE Vision 2.0 compatible cameras like the
Roboception rc_visard. The API is based on C++ 11 and can be compiled
under Linux and Windows.

This package also provides some tools that can be called from the
command line for discovering cameras, changing their configuration and
streaming images. Although the tools are meant to be useful when working
in a shell or in a script, their main purpose is to serve as example on
how to use the API for reading and setting parameters, streaming and
synchronizing images.

## Tools

The tools do not offer a graphical user interface. They are meant to be
called from a shell (e.g. Power Shell under Windows) or script and
controlled by command line parameters. Calling the tools without any
parameters prints a help text on the standard output.

NOTE: If any tool returns the error 'No transport layers found in path
\...', then read the section 'Transport Layer' below.

- gc_info . Lists all available systems (i.e. transport layers),
  interfaces and devices with some information. If a device ID is given
  on the command line, then the complete GenICam nodemap with all
  parameters and their current values are listed.

<!-- -->

- gc_config . Can be used to list network specific information of
  GenICam compatible GigE Vision 2 cameras. The network settings as well
  as all other parameters provided via GenICam can be changed.

<!-- -->

- gc_stream . This tool shows how to configure and stream images from a
  camera. GenICam features can be configured directly from the command
  line. Images will be stored in PGM or PPM format, depending on the
  image format. Streams of the Roboception rc_visard can be enabled or
  disabled directly on the command line by setting the appropriate
  GenICam parameters. The following command enables intensity images,
  disables disparity images and stores 10 images:
  

```
gc_stream <ID> ComponentSelector=Intensity ComponentEnable=1 ComponentSelector=Disparity ComponentEnable=0 n=10
```

 NOTE: Many image viewers can display PGM and
  PPM format. The sv tool of cvkit
  (<https://github.com/roboception/cvkit>) can also be used.

<!-- -->

- gc_pointcloud . This tool streams the left image, disparity,
  confidence and error from a Roboception rc_visard sensor. It takes the
  first set of time synchronous images, computes a colored point cloud
  and stores it in PLY ASCII format. This tool demonstrates how to
  synchronize different images according to their timestamps. NOTE: PLY
  is a standard format for scanned 3D data that can be read by many
  programs. The plyv tool of cvkit
  (<https://github.com/roboception/cvkit>) can also be used for
  visualization.

## Device ID

There are multiple ways of specifying an ID to identify a device.

1\. In the most basic version, the device ID is actually defined by the
GenTL producer (see Transport Layer section below). The GenTL producer
included in rc_genicam_api uses the lower case MAC address with the
colons `:` replaced by underscores `_`.

Example: `00_14_2d_2c_6e_bb`

2\. The given ID can also be a user defined name. The user defined name
is set to `rc_visard` by default and can be changed with:

gc_config <ID> -n <user-defined-name>

This way of identifying a device can fail if there is more than one
device with the same name. No device is returned in this case.

If the user defined name contains one or more colons, it must be
preceded by a colon (e.g. `:my:name`) or an interface ID (see below).

3\. The serial number of the device can also be used as ID. Example:
`02911931`

All three options can be seen in the output of `gc_config -l`.

### Optional Interface ID prefix

If the given ID contains a colon (i.e. `:`), the part before the
(first) colon is interpreted as interface ID and the part after the
first colon is treated as device ID. This is the format that `gc_config
-l` shows. A device with the given ID is only sought on the specified
interface. This can be useful if there are several ways to reach a
device from a host computer, e.g. via wireless and wired network
connection, but a certain connection type (e.g. wired) is preferred due
to higher bandwidth and lower latency.

Examples: `eth0:00_14_2d_2c_6e_bb`, `eth1:02911931` or
`wlan0:rc_visard`

A colon at the beginning of the ID effectively defines an empty
interface ID which triggers looking on all interfaces.

If the given ID does not contain a colon, the ID is interpreted as the
device ID itself and is sought throughout all interfaces as well.

## Transport Layer

The communication to the device is done through a so called transport
layer (i.e. GenTL producer version 1.5 or higher). This package provides
and installs a default transport layer that implements the GigE Vision
protocol for connecting to the Roboception rc_visard. According to the
GenICam specification, the transport layer has the suffix '.cti'. The
environment variable GENICAM_GENTL32_PATH (for 32 bit applications) or
GENICAM_GENTL64_PATH (for 64 bit applications) must contain a list of
paths that contain transport layers. All transport layers are provided
as systems to the application.

For convenience, if the environment variable is not defined or empty, it
is internally defined with the install path of the provided transport
layer (as known at compile time!). If the package is not installed, the
install path is changed after compilation or the package is moved to
another location after installation, then the transport layer may not be
found. In this case, the tools show an error that looks on 64 bit
systems like:

. 'No transport layers found in path GENICAM_GENTL64_PATH'

In this case, the corresponding environment variable (see above) must be
set to the directory in which the transport layer (i.e. file with suffix
'.cti') resides.

Under Windows, as second fall back additionally to the install path, the
directory of the executable is also added to the environment variable.
Thus, the install directory can be moved, as long as the cti file stays
in the same directory as the executable.

## Network Optimization under Linux

When images are received at a lower rate than set/exepected the most
likely problem is that this (user space) library cannot read the many
UDP packets fast enough resulting in incomplete image buffers.

### Test Script

The `net_perf_check.sh` script performs some simple checks and should
be run while or after streaming images via GigE Vision.



```
./net_perf_check.sh --help
```



### Jumbo Frames

First of all increasing the UDP packet size (using jubo frames) is
strongly recommended! Increase the MTU of your network interface to
9000, e.g.



```sh
sudo ifconfig eth0 mtu 9000
```

 Also make sure that all network
devices/switches between your host and the sensor support this.

### sysctl settings

There are several Linux sysctl options that can be modified to increase
performance for the GigE Vision usecase.

These values can be changed during runtime with `sysctl` or written to
`/etc/sysctl.conf` for persistence across reboots.

#### rmem_max

If the number of UDP `RcvbufErrors` increases while streaming,
increasing the socket receive buffer size usually fixes the problem.

Check the `RcvbufErrors with` `net_perf_check.sh` or



```
netstat -us | grep RcvbufErrors
```

 Increase max receive buffer size:



```sh
sudo sysctl -w net.core.rmem_max=33554432
```



#### softirq

Changing these values is usually not necessary, but can help if the
kernel is already dropping packets.

Check with `net_perf_check.sh` and increase the values if needed:



```sh
sudo sysctl -w net.core.netdev_max_backlog=2000
sudo sysctl -w net.core.netdev_budget=600
```
