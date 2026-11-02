## Overview

The Willow Garage 100 Mbps Ethernet (WGE100) camera is a 752x480
Ethernet camera developed for the PR2 robot. The PR2's narrow stereo
camera is a monochrome WGE100, while its wide stereo camera and forearm
cameras are in color. This package contains the
[wge100_camera_node](#Wge100CameraNode), a ROS
driver for a monocular WGE100 camera, the
[wge100_multi_configurator](#Wge100MultiConfigurator)
node, which allows two cameras in a stereo pair to be configured from
one centralized location, and a suite of
[command-line tools](#CommandLineTools) to
manage the camera.

### Using the Dual Stereo Cameras or Forearm Cameras on the PR2

Most PR2 users will not need the information on this page as the cameras
are brought up at the same time as the robot. Instead they can refer to
the following sources:

- For simplified instructions on setting up camera frame rate, or
  synchronization with the PR2's texture projector refer to the
  [pr2_camera_synchronizer](https://index.ros.org/p/pr2_camera_synchronizer)
  documentation.

<!-- -->

- For calibrating the cameras or doing vision processing, you will also
  want to look at the
  [image pipeline stack](https://index.ros.org/p/image_pipeline).

<!-- -->

- Other packages are available to use and process data coming from
  [monocular](https://index.ros.org/p/image_proc) or
  [stereo](https://index.ros.org/p/stereo_image_proc) cameras.

<!-- -->

- Tutorials are available showing how to dynamically reconfigure a
  node's parameters using [a GUI](https://index.ros.org/p/hokuyo_node),
  [from the command-line, a launch file or C++ code](https://index.ros.org/p/hokuyo_node).

<!-- -->

- For a reference of the WGE100 parameters you can skip directly to the
  [ROS API](#ROS_API) to learn about various
  parameters.

### Concurrent Access

Except for the
[access_register](#accessing-imager-registers-access_register)
and [discover](#Discover) tools, which can be
used at any time, the WGE100 tools are not designed for concurrent
access to the camera.

If you try to use two tools on different IP addresses, the second one
will override the settings from the previous one. If you try to use two
nodes at once, they will fight each other, neither one managing to take
control of the camera.

### Time Stamping

The timestamps returned by the `wge100_camera_node` are with respect
to the end of the exposure. The timestamps can be produced in one of two
ways:

- If the camera is externally triggered, the driver expects timestamps
  to be provided on a
  [roslib/msg/Header](https://docs.ros.org/en/rolling/p/roslib/msg/Header.html)
  topic. The topic the camera subscribes to is defined by the
  trig_timestamp_topic parameter. The driver then attempts to match
  timestamps with image arrival times.
- If the camera is internally triggered, the driver uses the arrival
  time of the first packet in the message, offset by
  `first_packet_offset` as an estimate of the end of the exposure.
  These estimates are then filtered based on the known frame rate to get
  a more accurate estimate with less jitter.

## Camera URLs

When working with a WGE100 camera, the user needs to identify the camera
she wishes to work with. Cameras are identified using URLs, which can
refer either to the camera's serial number or to its descriptive name
(set using [set_name](#SetName)). If there is
only one camera present, a URL can indicate that whatever camera is
found should be used.

### Types of URLs

There are three types of camera URLs:

- **name** URLs indicate the name of the camera to be found. You can set
  the name of a camera using the
  [set_name](#SetName) utility. E.g.:
  `name://wide_stereo_l`
- **serial** URLs indicate the serial number of the camera to be found.
  E.g.: `serial://2701025`
- **any** URLs will match any camera. E.g.: `any://`

If a URL matches more than one camera, none of them will be selected,
and an error will be reported. This situation cannot happen with a
**serial** URL as camera serial numbers are unique.

### Specifying an IP address

In normal use, the WGE100 camera has an IP address stored in flash that
it will use for communication. However it is sometimes useful to have
the camera use a different IP address, for example when the IP address
in flash is invalid, or if is transiently placed on a different network
from the one it is configured for. In that case, an IP address can be
added to the URL. An IP address is introduced with the `@` sign. E.g.:
`name://my_camera@192.168.1.2`

When an IP address is specified, WGE100 camera tools will configure the
camera to use that address before they try to work with it. The IP
address that is specified using @ will get reset each time a new tool is
used. To set a camera's IP address permanently, use the
[set_name](#SetName) tool.

### Specifying a Network Interface

In some cases, a single camera may be visible on multiple interfaces, or
cameras with the same name may be visible on different network
interfaces. In this case, an interface name can be included in the
camera URL to force a particular interface to be used for communication.
An interface name is introduced with the `#` sign. For example, on the
PR2, only the `lan0` interface is searched to avoid potential
conflicts with identically named cameras on the wan0 interface:
`name://wide_stereo_l#lan0`

### Putting it all Together

The most general form for a WGE100 camera URL is:



```
name://camera_name[@camera_ip][#local_interface]
serial://serial_number[@camera_ip][#local_interface]
any://[@camera_ip][#local_interface]
```



Some example URLs:

  -- ----------------------------------- -- -------------------------------------------------------------------------------- --
     `any://`                               Matches any camera                                                               
     `serial://15#eth2`                     Matches the camera with serial number 15, and only looks on interface eth2       
     `name://left_forearm@10.68.0.210`      Matches the left_forearm camera, and configures it to work from IP 10.68.0.210   
  -- ----------------------------------- -- -------------------------------------------------------------------------------- --

<a id="ROS_API"></a>

## ROS API

<a id="Wge100CameraNode"></a>


```clearsilver
node.0 {
name=wge100_camera_node
desc=`wge100_camera_node` is a driver for the WGE100 camera that is found in the PR2 forearms and in the PR2 dual stereo camera. The black and white cameras support two register sets in hardware, allowing the imager settings to be swapped back and forth between two settings for even and odd frames. The driver publishes the images for each register set in its own namespace. This is a purely monocular driver. A stereo WGE100 camera needs one `wge100_camera_node` for each camera in the pair.
pub{
0.name= camera/image_raw
0.type= sensor_msgs/Image
0.desc= Images taken with the primary register set
1.name= camera/camera_info
1.type= sensor_msgs/CameraInfo
1.desc= Camera intrinsics for images published on camera/image_raw
2.name= camera_alternate/image_raw
2.type= sensor_msgs/Image
2.desc= Images taken with the alternate register set
3.name= camera_alternate/camera_info
3.type= sensor_msgs/CameraInfo
3.desc= Camera intrinsics for images published on camera_alternate/image_raw
4.name= /diagnostics
4.type= diagnostic_msgs/DiagnosticStatus
4.desc= Diagnostic status information.
}
sub{
0.name= <~trig_timestamp_topic>
0.type= roslib/Header
0.desc= In external mode only: topic on which the `wge100_camera_node` gets timestamps at which the camera was triggered. The node matches these timestamps to incoming images and uses them to timestamp the frame. The name of this topic is extracted from the ~trig_timestamp_topic parameter.
}
srv{
0.name= ~self_test
0.type= diagnostic_msgs/SelfTest
0.desc= Starts the self test.
1.name= camera/set_camera_info
1.type= sensor_msgs/SetCameraInfo
1.desc= Sets the camera's intrinsics
2.name= ~board_config
2.type= wge100_camera/BoardConfig
2.desc= Internal use only. (Used to set the camera's MAC address and serial number during production. Can only be used once.)
}
param {
group.0 {
name=Dynamically Reconfigurable Parameters
desc=All the `wge100_camera_node` parameters are dynamically reconfigurable. See the [[dynamic_reconfigure]] package for details on dynamically reconfigurable parameters.
0.name= ~camera_url
0.default= any://
0.type= str
0.desc=URL defining which camera to connect to, on what interface and with which IP address. 
8.name= ~frame_id
8.default= 
8.type= str
8.desc=Sets the TF frame from which the camera is publishing. 
17.name= ~register_set
17.default=0
17.type= int
17.desc=Select the register set to work with. In auto mode, an extra pulse on the trigger signal indicates that the alternate set should be used. Possible values are: !PrimaryRegisterSet (0): The primary register set is always used., !AlternateRegisterSet (1): The alternate register set is always used., Auto (2): The trigger signal selects which register set to use.
31.name = ~packet_debug
31.default = false
31.type = bool
31.desc = If true, warns on diagnostics for any dropped packet event.
}

group.1 {
name=Region of Interest Parameters
desc=The following parameters define the region of interest on the imager, and how it is mapped into the resulting image. The `camera_info` topics will only be valid if these parameters are set to the same values as when the camera was calibrated. Currently the camera driver will detect mismatches in `width` and `height`, but not for the other parameters.
1.name= ~width
1.default= 640
1.type= int
1.desc=Number of pixels horizontally. Range: 1 to 752
2.name= ~height
2.default= 480
2.type= int
2.desc=Number of pixels vertically. Range: 1 to 480
3.name= ~imager_rate
3.default= 30.0
3.type= double
3.desc=Sets the frame rate of the imager. In externally triggered mode this must be more than trig_rate Range: 1.0 to 100.0
4.name= ~horizontal_binning
4.default= 1
4.type= int
4.desc=Number of pixels to bin together horizontally. Range: 1 to 4
5.name= ~vertical_binning
5.default= 1
5.type= int
5.desc=Number of pixels to bin together vertically. Range: 1 to 4
6.name= ~horizontal_offset
6.default= 0
6.type= int
6.desc=Horizontal offset between the center of the image and the center of the imager in pixels. Range: -376 to 376
7.name= ~vertical_offset
7.default= 0
7.type= int
7.desc=Vertical offset between the center of the image and the center of the imager in pixels. Range: -240 to 240
9.name= ~mirror_x
9.default= False
9.type= bool
9.desc=Mirrors the image left to right. 
10.name= ~mirror_y
10.default= False
10.type= bool
10.desc=Mirrors the image top to bottom. 
11.name= ~rotate_180
11.default= False
11.type= bool
11.desc=Rotates the image 180 degrees. Acts in addition to the mirror parameters
}

group.2 {
name=Triggering Parameters
desc=The following parameters define how the camera is triggered, and how the driver estimates the time at which the exposure ended. Details of how camera timestamps are produced can be found [[#TimeStamping|here]].
13.name= ~ext_trig
13.default= False
13.type= bool
13.desc=Set the camera to trigger from the external trigger input. 
14.name= ~rising_edge_trig
14.default= True
14.type= bool
14.desc=Indicates that the camera should trigger on rising edges (as opposed to falling edges). 
15.name= ~trig_timestamp_topic
15.default= 
15.type= str
15.desc=Sets the topic from which an externally triggered camera receives its trigger timestamps. 
16.name= ~trig_rate
16.default= 30.0
16.type= double
16.desc=Sets the expected triggering rate in externally triggered mode. Range: 1.0 to 100.0
12.name= ~first_packet_offset
12.default= 0.0025
12.type= double
12.desc=Offset between the end of exposure and the minimal arrival time for the first frame packet. Only used when using internal triggering. Range: 0.0 to 0.02
}

group.3 {
name=Shared Imager Settings
desc=The following imager settings parameters are shared between the two register sets.
18.name= ~brightness
18.default= 58
18.type= int
18.desc=The camera brightness for automatic gain/exposure. Range: 1 to 64
19.name= ~black_level
19.default= 0
19.type= int
19.desc=Sets the black level. Range: -127 to 127
20.name= ~max_exposure
20.default= 0.0
20.type= double
20.desc=Maximum exposure time in seconds in automatic exposure mode. Zero for automatic. Range: 0.0 to 0.1
}

group.4 {
name=Primary Imager Settings
desc=The following imager settings apply only to the primary register set.
21.name= ~auto_exposure
21.default= True
21.type= bool
21.desc=Sets the camera exposure duration to automatic. Causes the exposure setting to be ignored. 
22.name= ~exposure
22.default= 0.01
22.type= double
22.desc=Maximum camera exposure time in seconds. The valid range depends on the video mode. Range: 0.0 to 0.1
23.name= ~auto_gain
23.default= True
23.type= bool
23.desc=Sets the analog gain to automatic. Causes the gain setting to be ignored. 
24.name= ~gain
24.default= 32
24.type= int
24.desc=The camera analog gain. Range: 16 to 64
25.name= ~companding
25.default= True
25.type= bool
25.desc=Turns on companding (a non-linear intensity scaling to improve sensitivity in dark areas).
}

group.5 {
name=Alternate Imager Settings
desc=The following imager settings apply only to the alternate register set.
26.name= ~auto_exposure_alternate
26.default= True
26.type= bool
26.desc=Sets the alternate camera exposure duration to automatic. Causes the  exposure_alternate setting to be ignored. 
27.name= ~exposure_alternate
27.default= 0.01
27.type= double
27.desc=Alternate camera exposure in seconds. The valid range depends on the video mode. Range: 0.0 to 0.1
28.name= ~auto_gain_alternate
28.default= True
28.type= bool
28.desc=Sets the alternate analog gain to automatic. Causes the gain_alternate setting to be ignored. 
29.name= ~gain_alternate
29.default= 32
29.type= int
29.desc=The alternate camera analog gain. Range: 16 to 64
30.name= ~companding_alternate
30.default= True
30.type= bool
30.desc=Turns on companding for the alternate imager register set 
}
}
}
```



<a id="Wge100MultiConfigurator"></a>


```clearsilver
node.0 {
name=wge100_multi_configurator
desc=`wge100_multi_configurator` is a node that allows multiple `wge100_camera_node`s to receive identical configurations. It acts like a [[dynamic_reconfigure]] that passes each request it receives to each one of the `wge100_camera_node`s that it manages. This node's intended use is to allow both `wge100_camera_node`s in a stereo pair to be configured from one centralized location.
param {
group.0 {
name=Dynamically Reconfigurable Parameters
desc=See the [[dynamic_reconfigure]] package for details on dynamically reconfigurable parameters.
0.name=~camera_nodes
0.default= "wge100_camera"
0.type= str
0.desc= Space separated list of nodes that should be controlled by this multi-configurator.
1.name= ~<any wge100_camera_node parameter except camera_url>
1.default= same
1.type= same
1.desc= When this parameter is set, a reconfigure request is passed down to each underlying wge100_camera_node. Currently changes in the underlying nodes are not passed back up to this node's parameters.
}
}
```



<a id="CommandLineTools"></a>

## Command-Line Tools

The following command-line tools are helpful when configuring the
camera.

<a id="Discover"></a>

### Camera Discovery: discover

The **discover** tool uses a broadcast packet to find cameras on the
network. It can be run on a single network interface:



```
$ rosrun wge100_camera discover eth1
Found camera serial://13 name://test MAC: 00:24:cd:00:00:83 iface: eth2:avahi current IP: 169.254.8.124, PCB rev: C HDL rev: 400 FW rev: 118
```

 or on all network interfaces:



```
$ rosrun wge100_camera discover
Found camera serial://13 name://test MAC: 00:24:cd:00:00:83 iface: eth2:avahi current IP: 169.254.8.124, PCB rev: C HDL rev: 400 FW rev: 118
```

 The IP address that is reported by the
**discover** tool is the currently configured address for the camera.
This may be different from the IP address stored in the camera's flash,
and to which the camera defaults when it is reset. This IP may or may
not be valid for the interface on which the camera is located, and it is
quite possible that you will not be able to communicate with the camera
at this particular IP address.

Sometimes a camera can be seen from multiple interfaces. The
**discover** tool only reports the first interface on which a response
is seen. The camera can nevertheless be configured to run from an
interface other than the one on which it was reported.

<a id="SetName"></a>

### Camera Setup: set_name

The camera name and IP address that are stored in the camera's flash
can be accessed using the **set_name** tool. With a single camera URL
argument, set_name reports the current settings.



```
$ rosrun wge100_camera set_name serial://15@169.254.8.200
Previous camera name was: test.
Previous camera IP: 169.254.8.124.
```



With an additional name and IP argument, the values in the flash are
modified, and the camera is automatically reset so that they become the
new defaults.



```
$ rosrun wge100_camera set_name serial://15@169.254.8.200 new_name 169.254.8.200
Previous camera name was: test
Previous camera IP: 169.254.8.124
Success! Restarting camera, should take about 10 seconds to come back up after this.
$ rosrun wge100_camera set_name serial://15
Previous camera name was: new_name
Previous camera IP: 169.254.8.200
```



### Camera Intrinsics: set_calibration

The camera intrinsics that are stored in the camera's flash can be
accessed using the **set_calibration** tool. With a single camera URL
argument, set_name reports the current settings.



```
$ rosrun wge100_camera set_calibration name://wide_stereo_l
Unable to create ARP entry (are you root?), continuing anyway
Reading old calibration...
[image]
...
```

 With an additional file name argument, the
values in the flash are modified.



```
$ rosrun wge100_camera set_calibration serial://15@169.254.8.200 intrinsics.ini
```



In general, calibration of the camera and uploading of the parameters
should be done through the
[ camera calibration ](https://index.ros.org/p/camera_calibration)
package. These programs will perform the calibration, and make the
service call to flash the intrinsics back onto the camera.

### Resetting a Camera: reset_cam

The camera can be reset using the **reset_cam** command, which takes a
single camera_url argument.



```
$ rosrun wge100_camera reset_cam any://
```

 Note: The **reconfigure_cam** tool currently
has the same effect as **reset_cam**. In future firmware versions
**reconfigure_cam** will always cause the camera FPGA to reconfigure
itself, whereas **reset_cam** may do a softer reset that resets all
components without reconfiguring the FPGA.

### Advanced Command-Line Tools

For advanced functionality such as

1\.
[Accessing Imager Registers: access_register](#accessing-imager-registers-access_register) 1.
[Reflashing the Camera Firmware: upload_mcs](#reflashing-the-camera-firmware-upload_mcs) 1.
[Checking Flash Programming: check_flash](#checking-flash-programming-check_flash) 1.
[Dumping the Flash Contents: read_all_flash](#dumping-the-flash-contents-read_all_flash)

## Flash Contents

For information on contents of the WGE100 flash memory, you may consult
[this page](#flashcontents).

## Tutorials

- [How to Configure and Use the WGE100 Camera](#how-to-configure-and-use-the-wge100-camera):
  This tutorial is an introduction to using the WGE100 camera connected
  to a desktop. After reading it you should be able to bring up the
  WGE100 camera, configure the camera, and display the images.
- [How to Configure and Use the WGE100 Stereo Camera on a PR2](#how-to-configure-and-use-the-wge100-stereo-camera-on-a-pr2):
  This tutorial is an introduction to using the WGE100 stereo camera
  connected to a PR2 robot. After reading it you should be able to bring
  up the WGE100 stereo camera and display the images.
- [Running the WGE100 camera in externally triggered mode](#running-the-wge100-camera-in-externally-triggered-mode):
  This tutorial covers using an external trigger with the WGE100 camera
  on the PR2.

## AdvancedCommandLine

### Advanced WGE100 Command-Line Tools

#### Accessing Imager Registers: access_register

For experimentation purposes, the camera's imager registers can be
viewed and modified using the **access_register** command. Unlike other
commands, this command will never change the current IP address of the
camera in order to avoid interrupting the image stream if the camera is
currently running. Hence, if the camera is currently communicating on an
IP address different from the one that is determined from the URL,
communication will fail. Finally, the **access_register** tool will only
work if the camera has previously been accessed by some other tool.

All values displayed and read by this tool are in hexadecimal. Depending
on the arguments, it will dump all the registers


```
$ rosrun wge100_camera access_register name://my_camera
00:  1313 0001 0004 01e0 0280 0174 002f 0388 - 01bb 01d9 0164 01e0 0000 0320 0000 0011 
10:  0040 8042 0022 2d32 0e02 7f32 2802 3e38 - 3e38 2802 0428 0000 0002 0000 0000 0000 
20:  01d1 0020 0020 0010 0010 0020 0010 0010 - 0010 0010 0020 0004 0004 0004 0007 0004 
30:  0003 001d 0018 0015 0004 0010 0040 0000 - 0000 0000 0000 0001 0000 0000 0000 0000 
40:  0007 e00a 0020 0000 0000 0000 231d 8080 - 0010 0000 0000 0000 0002 0000 0000 0000 
50:  0000 0000 0000 0000 0000 0000 0000 0000 - 0000 0000 0000 0000 0000 0000 0000 0000 
60:  0000 0000 0000 0000 0000 0000 0000 0000 - c083 04ce 2910 6848 0000 0000 0000 0000 
70:  0034 0000 002a 02f7 0000 0000 0000 0000 - 0000 0000 0000 0000 0000 0000 0000 0000 
80:  00f4 00f4 00f4 00f4 00f4 00f4 00f4 00f4 - 00f4 00f4 00f4 00f4 00f4 00f4 00f4 00f4 
90:  00f4 00f4 00f4 00f4 00f4 00f4 00f4 00f4 - 00f4 0000 0096 012c 01c2 0258 02f0 0000 
a0:  0060 00c0 0120 0180 01e0 003a 0002 0000 - 0000 0002 0000 0002 0000 0000 0000 0003 
b0:  abe0 0002 0010 0010 0000 0000 0000 0000 - 0000 0000 0040 01f1 0006 01f1 0014 0016 
c0:  000a 0158 0840 0000 4416 4421 0000 0000 - 0000 0000 0000 0000 0000 0000 0000 0000 
d0:  0000 0000 0000 0000 0000 0000 0000 0000 - 0000 0000 0000 0000 0000 0000 0000 0000 
e0:  0000 0000 0000 0000 0000 0000 0000 0000 - 0000 0000 0000 0000 0000 0000 0000 0000 
f0:  0000 0000 0000 0000 0000 0000 0000 0000 - 0000 0000 0000 0000 0000 0000 beef 1313
```

 show the contents of a single register


```
$ rosrun wge100_camera access_register serial://12 fe
Reg fe read: beef
```

 or set a single register


```
$ rosrun wge100_camera access_register name://my_camera 1 1
Reg 01 was: 0002 set: 0001 read: 0001
```



If the word **stresstest** precedes the register to read/write, the
camera will repeatedly read/write that register until it is interrupted
with CTRL+C.

#### Reflashing the Camera Firmware: upload_mcs

The camera's firmware is stored in a .mcs file that can be uploaded to
the camera using the **upload_mcs** tool. This is a critical operation
that could render your camera inoperable if the camera is reset while
programming is in progress. If programming fails, immediately retry the
operation as the camera's flash may be in an invalid state that will
prevent the camera from turning on the next time it is reset. If you are
worried that programming may fail, you can use the **check_flash** tool
to exercise the flash reading and writing functionality of the camera
without overwriting the camera's firmware. When programming and
verification is complete, the camera is reset so that the new firmware
goes into effect.

To reprogram the flash, **upload_mcs** needs the name of the .mcs file
to read and a URL for the camera. Usually, the most up-to-date firmware
can be found in wge100_camera/firmware_images/default.mcs



```
$ roscd wge100_camera/firmware_images
$ rosrun wge100_camera upload_mcs default.mcs any://
******************************************************************
Firmware file parsed successfully. Will start writing to flash in 5 seconds.
Hit CTRL+C to abort now.
******************************************************************
Writing to flash. DO NOT ABORT OR TURN OFF CAMERA!!
...........
Verifying flash.
...........
Success! Restarting camera, should take about 10 seconds to come back up after this.
```



In some cases, it is useful to convert a .mcs file to raw binary. For
example, it could be desirable to compare the flash contents read using
**read_all_flash** to the contents of an MCS file. If no camera URL is
specified when running **upload_mcs**, the .mcs contents are dumped to
standard output, from which they can be redirected to a file.


```
$ roscd wge100_camera/firmwares
$ rosrun wge100_camera upload_mcs default.mcs > default.bin
```



#### Checking Flash Programming: check_flash

The **check_flash** tool can be used to check that reading and writing
to the camera's flash is reliable. Most users will not need to use this
tool. Its only argument is the URL of the camera to test.

**Warning: This program will erase any user settings from the flash
memory.**



```
$ rosrun wge100_camera check_flash serial://15
Unable to create ARP entry (are you root?), continuing anyway

*************************************************************************
Warning, this will overwrite potentially important flash memory contents.
You have 5 seconds to press CTRL+C to abort this operation.
*************************************************************************
....................
....................
Check completed, 0 errors.
```



#### Dumping the Flash Contents: read_all_flash

The **read_all_flash** tool can be used to dump the complete camera
flash contents. The output goes to standard output, and should usually
be redirected to a file. The single argument to **read_all_flash** is
the camera's URL



```
$ rosrun wge100_camera read_all_flash any:// > flashdump.bin
```

## FlashContents

### WGE100 Flash Contents

The WGE100 camera contains a 8Mbit serial flash chip. It is divided into
4096 pages numbered from 0 to 4095 containing 264 bytes each. Its
contents are used as follows:

  -- ----------- -- --------------------------------------------------------------------------------------------------------------------------------- --
     Pages          Contents                                                                                                                          
     0-1075         FPGA configuration bitstream. If you write to this area you will have to use a JTAG programmer to get the camera working again.   
     4093-4094      Camera intrinsics                                                                                                                 
     4095           Camera name and IP address                                                                                                        
  -- ----------- -- --------------------------------------------------------------------------------------------------------------------------------- --

The flash chip also contains a special one-time writable page that is
used to store the camera's MAC address and serial number.

## How to Configure and Use the WGE100 Camera

### Compiling

Start by getting the dependencies and compiling the driver.



```
$ rosdep install wge100_camera
$ rosmake wge100_camera
```



### Powered On and Plugged in

Make sure that your WGE100 camera is powered at 12V and connected to an
Ethernet port on your computer using the cables provided by Willow
Garage. You should have a green flashing light like below.

[Youtube](https://www.youtube.com/watch?v=z-Ni8ya_XvI)

### Making Sure the Network is Configured for IPv4 Networking

Before you can find a camera on the network, the network adapter to
which the camera is connected must be configured for IPv4 networking. In
many cases this will be done already, so try skipping to the next
section of this tutorial, and come back here if the `discover` command
can't find your camera.

Configuring a network interface is beyond the scope of this tutorial.
The following tips may allow you to get started, but may get you in
trouble with your network administrator. Moreover, the setup you get by
following these tips will not persist when the computer is rebooted.

On Linux, to check that an interface is configured for IPv4 networking,
use the `ifconfig` command. For example if your camera is connected to
eth2, do: 

```
$ ifconfig eth2
eth2      Link encap:Ethernet  HWaddr 00:50:b6:03:f4:60  
          inet6 addr: fe80::250:b6ff:fe03:f460/64 Scope:Link
          UP BROADCAST RUNNING MULTICAST  MTU:1500  Metric:1
          RX packets:0 errors:0 dropped:0 overruns:0 frame:0
          TX packets:6 errors:0 dropped:0 overruns:0 carrier:0
          collisions:0 txqueuelen:1000 
          RX bytes:0 (0.0 B)  TX bytes:492 (492.0 B)
```

 In this case, the Ethernet interface
has an **inet6 addr**, but no **inet addr**, so it is not configured for
IPv4 networking.

We can give the interface an IPv4 address with the following command
(this address probably won't get you in trouble):


```
$ sudo ifconfig eth2 192.168.123.1 netmask 255.255.255.0
```



Now we can check that the interface does indeed have an **inet addr**:


```
$ ifconfig eth2 
eth2      Link encap:Ethernet  HWaddr 00:50:b6:03:f4:60  
          inet addr:192.168.123.1  Bcast:192.168.123.255  Mask:255.255.255.0
          inet6 addr: fe80::250:b6ff:fe03:f460/64 Scope:Link
          UP BROADCAST RUNNING MULTICAST  MTU:1500  Metric:1
          RX packets:0 errors:0 dropped:0 overruns:0 frame:0
          TX packets:20 errors:0 dropped:0 overruns:0 carrier:0
          collisions:0 txqueuelen:1000 
          RX bytes:0 (0.0 B)  TX bytes:3641 (3.5 KB)
```



### Finding the Camera on the Network

Use the `discover` utility to find the camera:



```
$ rosrun wge100_camera discover
```





```
Found camera serial://13 name://test MAC: 00:24:cd:00:00:83 iface: eth2 current IP: 10.0.1.123, PCB rev: C HDL rev: 400 FW rev: 119
Found camera serial://15 name://cam15 MAC: 00:24:cd:00:00:86 iface: eth1 current IP: 10.0.1.125, PCB rev: C HDL rev: 400 FW rev: 119
```



When `discover` reports multiple cameras, you can figure out which one
is yours by its serial number (written on the back of the camera), by
its name, when the name has been set to a descriptive value, or by the
interface it is connected to.

### Understanding Camera URLs

The tools that work with the WGE100 camera expect to be given a camera
URL that tells them which camera to work with, and how to talk to that
camera. There are three types of URLs:



```
name://camera_name[@camera_ip][#local_interface] 
serial://serial_number[@camera_ip][#local_interface]
any://[@camera_ip][#local_interface]
```

*(e.g. `name:*camera_name`,
`serial:*serial_number@192.168.0.23`, or
`any:*\@192.168.0.23#eth2`)//

A `name:*` URL identifies the camera by a descriptive name that was
given to it, and that is reported by the discover utility. We will see
shortly how to set the name. A `serial:*` URL identifies a camera by
its serial number. Finally, the `any:*` URL will match any camera. In
some cases a URL may match many cameras. If that happens, the WGE100
camera tools will refuse to work, and you will have to use a different
non-ambiguous URL. For example, you cannot use the `any:*` URL if
there are two cameras visible from your computer. You may be able to use
`any:*#eth2` if only one of the cameras is on interface eth2, or you
could use `serial:*13` to talk to the camera with serial number 13.

Your camera may have been configured with a default IP address. If that
IP address is invalid on the network the camera is connected to, you
will have to indicate the address for the camera to use in the camera
URL. For example, in the examples above, camera 13 is configured to be
at IP address 10.0.1.123, but the network interface eth2 it is connected
to has an IP of 192.168.123.1. To talk to the camera, you will have to
give it an address that is valid for eth2. For example, you might use
`serial:*13@192.168.123.2`, which would tell a tool to access the
camera with serial number 13, and have the camera use IP address
192.168.123.2.*

In some cases it is useful to specify the interface over which the
camera should be accessed. We have already seen how this can be used to
disambiguate the `any:*` URL; it could also be used if more than one
interface can see the camera and you want to access the camera via a
specific interface.*

For more information on Camera URLs see the
[ wge100_camera main page](#camera-urls)

### Configuring the Camera (optional)

We have just seen that a camera can be accessed using its default IP
address, or using a temporary address indicated in its URL. If you are
going to permanently set up a camera in a given network environment, you
probably want to set its IP address once and for all, simplifying the
URLs with which the camera is accessed. Likewise, you will probably want
to give the camera a descriptive name rather than referring to it by
serial number.

The `set_name` utility allows the camera's name and IP address to be
set:



```
$ rosrun wge100_camera set_name
Usage: set_name <camera_url> <new_name> <new_default_ip>   # Sets the camera name and default IP
       set_name <camera_url>                               # Reads the camera name and default IP
```



Here is an example of configuring the camera: 

```
$ rosrun wge100_camera set_name serial://13@192.168.123.10 my_camera 192.168.123.10
Unable to create ARP entry (are you root?), continuing anyway
Previous camera name was: test.
Previous camera IP: 10.0.1.123.
Success! Restarting camera, should take about 10 seconds to come back up after this.
```



Thereafter, you can access the camera via the URL **name:*my_camera**,
and the camera will be at IP address 192.168.123.10*****

On the PR2, you may have to set the interface to set the name of a
camera: 

```
rosrun wge100_camera set_name serial://180XXXX#lan0 forearm_l 10.68.0.41
```

 If you don't use the "#lan0" syntax,
you may see the error message "IP address configuration failed" if the
robot tries to use the "lan1" network.

### Launching the WGE100 Camera Node

Use the wge100_camera_demo.launch in the wge100_camera directory as an
example configuration file. You will have to specify a camera url that
the camera should communicate from in camera_url. If you want a tf frame
to be associated with the camera, specify a frame_id.


```
$ roscd wge100_camera
```



Main fragment of `wge100_camera_demo.launch:`


```
<launch>
  <!-- The camera node -->
  
  <node name="wge100_camera_demo" pkg="wge100_camera" type="wge100_camera_node" output="screen">
    <param name="camera_url" type="str" value="any://" />
    <param name="imager_rate" type="double" value="25" />
    <remap from="camera" to="wge100_demo" />
  </node>
</launch>
```



Once you have created the launch file:



```
$ roslaunch your_wge100_camera.launch
```

 This will return something similar to:



```
[ INFO] 1251220032.176747000: Configured camera. Complete URLs: serial://13@192.168.123.10#eth2 name://my_camera@192.168.123.10#eth2
[ INFO] 1251220032.250105000: Loaded intrinsics from camera
[ INFO] 1251220032.253953000: Camera streaming.
```



If you see a warning that your camera intrinsics couldn't been loaded,
don't worry. It means that your camera has never been calibrated. Refer
to [camera_calibration](https://index.ros.org/p/camera_calibration) for
instructions on calibrating a camera. Having an uncalibrated camera will
not prevent progress through the rest of this tutorial.

You can verify that frames are streaming by running


```
rostopic hz wge100_camera_demo/image_raw
```



### Viewing the WGE100 Camera Images

This will display images coming from the WGE100 camera.

First you will need to build image_view. In a new window, run:


```
$ rosmake image_view
```



Then you can use image_view to view the raw image stream:


```
$ rosrun image_view image_view image:=wge100_camera_demo/image_raw
```



If you have a color camera, the image will be black and white with a
strange texture. This is because the image is being returned as a
[ bayer pattern](http://en.wikipedia.org/wiki/Bayer_filter ). You will
have to use [image_proc](https://index.ros.org/p/image_proc) to convert
it to a color image. First build image_proc: 

```
$ rosmake image_proc
```



Then run image_proc: 

```
ROS_NAMESPACE=wge100_camera_demo rosrun image_proc image_proc
```



With image_proc still running, open a **new window** and launch a
viewer: 

```
$ rosrun image_view image_view image:=wge100_camera_demo/image_color
```



You could run all these commands from a launch file if you like. Have a
look at the commented example in wge100_camera_demo.launch to see how it
is done: 

```
$ rosed wge100_camera wge100_camera_demo.launch
```



------------------------------------------------------------------------

## How to Configure and Use the WGE100 Stereo Camera on a PR2

### Launch File

Typically there will be no need to launch the stereo camera
configuration on the PR2 because it is launched at startup with the rest
of the robot. **Most users should skip directly to
[ Viewing Stereo Images](#viewing_stereo_images)**.
In the case that the stereo camera configuration is not loaded, the
following launch files will need to be launched.

#### If PR2 is not started

If the robot is not up and able to move (i.e.
[pr2_etherCAT](pr2_etherCAT) is not running) you will need to launch the
robot:



```
$ sudo robot start
```



This should bringup the stereo cameras and you can **proceed to the
[ Viewing Stereo Images](#viewing_stereo_images)
step** unless you need to start the stereo cameras independently or just
want to learn more about what happens behind the scenes.

#### If PR2 is already started

If the robot is up and able to move (i.e. [pr2_etherCAT](pr2_etherCAT)
is running) but the stereo cameras were not brought up, you will need to
launch the dual stereo configuration:



```
$ roslaunch pr2_bringup config/dualstereo_camera.launch
```



This launch file loads the following:

- A wge100_camera_node per WGE100 camera.
- A wge100_multi_configurator for each
  stereo pair, which replicates its parameters to each camera's driver.
- [Stereo image processing](https://index.ros.org/p/stereo_image_proc)
  for each stereo pair
- [pr2_controller_manager](https://index.ros.org/p/pr2_controller_manager)
  with suitable controllers running:
- One
  [MultiTriggerController](https://index.ros.org/p/ethercat_trigger_controllers)
  per WGE100 camera trigger line (i.e.one for both of the stereo
  cameras).
- A
  [pr2_camera_synchronizer](https://index.ros.org/p/pr2_camera_synchronizer)
  node in charge of setting the triggers and camera drivers into
  triggering states that are consistent with the user's desires. This
  is important for stereo cameras firing at the same time and
  controlling the relationship between the
  [ texture projector](#texture_projector)
  and the camera exposure.

### Calibrating the Stereo

Before you can reconstruct depth from a pair of stereo images, the
cameras need to be calibrated. The robots initially ship with calibrated
stereo cameras, but this calibration can degrade or be lost over time.
If you need to calibrate your stereo cameras, see the
[ tutorial](https://index.ros.org/p/camera_calibration).

<a id="viewing_stereo_images"></a>

### Viewing Stereo Images



```
stereo_view stereo:=<stereo namespace> image:=<image topic identifier>
```



For example, to view stereo image pairs on topics
`/my_stereo_cam/left/image_rect_color` and
`/my_stereo_cam/right/image_rect_color`, use: 

```
$ stereo_view stereo:=/my_stereo_cam image:=image_rect_color
```



`stereo_view` also shows the disparity image computed from the stereo
pair, color-mapped for clarity.

You may save the current image pair by left-clicking on either display
window. By default, images will be saved as `left0000.jpg`,
`right0000.jpg`, `left0001.jpg`, `right0001.jpg`\....

On the robot, you can view the unrectified images from the monochrome,
narrow field-of-view stereo pair with: 

```
$ stereo_view stereo:=narrow_stereo image:=image_raw
```



Or you could view the unrectified color images from the color, wide
field-of-view stereo pair with: 

```
$ stereo_view stereo:=wide_stereo image:=image_color
```



<a id="texture_projector"></a>

### Using the Texture Projector

To improve the effectiveness of stereo reconstruction, the PR2 is
equipped with a projector that can project a texture onto featureless
surfaces. The easiest way to use the projector is from a
[dynamic reconfigure GUI](https://index.ros.org/p/dynamic_reconfigure):

```
rosrun dynamic_reconfigure reconfigure_gui camera_synchronizer_node
```



You can then decide, for each camera, what its `_trig_mode` setting
should be. For example, to start streaming textured images on
`narrow_stereo_textured`, set `narrow_stereo_trigger_mode` to
`WithProjector`. The PR2's texture projector should turn on, and you
should be able to see unrectified textured images with:


```
$ stereo_view stereo:=narrow_stereo_textured image:=image_raw
```



Note: `narrow_stereo_textured` and `narrow_stereo` will only be
streaming images when the camera is taking images with the correct
projector state. For example, if the projector is off, there will be no
images on `narrow_stereo_textured`.

To learn about other ways of using dynamic reconfiguration to change a
node's settings, look at
[this tutorial](https://index.ros.org/p/hokuyo_node)

### Further Reading

For an in depth view of the PR2's camera systems and how to configure
them, you can refer to the
[pr2_camera_synchronizer](https://index.ros.org/p/pr2_camera_synchronizer)
documentation.

## Running the WGE100 camera in externally triggered mode

### This tutorial is out of date and needs to be updated. Please do not attempt to follow it.

The WGE100 camera can use an external trigger to synchronize its
exposure with other cameras or motion-control systems. On the PR2, this
is done through the motor-controllers. The following tutorial assumes
that you are working on a PR2 running pr2_etherCAT.

Follow the instructions in
[ConfiguringAndUsingTheWGE100Camera](#how-to-configure-and-use-the-wge100-camera)
tutorial except that now you should base yourself on
wge100_camera_triggered.launch. You now need to set trigger_controller,
trigger_rate and trigger_phase to configure the triggering. The motor
controller board that does the triggering needs to be set in
trigger_controller.xml.

**The trigger_rate should be such that there is at least 1 to 2 ms of
slack between it and the frame rate in video_mode or some triggers could
be missed.**

An example wge100_camera_triggered.launch file:



```
<launch>
  <node pkg="pr2_etherCAT" type="pr2_etherCAT" args="-i eth0 -x $(find wge100_camera)/mb_configuration.xml" output="screen"/>
  <node pkg="pr2_controller_manager" type="spawner" args="$(find wge100_camera)/trigger_controller.xml" />
  <group ns="wge100_camera_node">
    <param name="if_name" type="str" value="eth2"/>
    <param name="ip_address" type="str" value="192.168.202.2"/>
    <param name="serial_number" type="int" value="7"/>
    <param name="video_mode" type="str" value="640x480x30"/>
    <!--param name="frame_id" type="str" value="???"/-->
    <param name="do_colorize" type="bool" value="True"/>
    <param name="do_rectify" type="bool" value="True"/>
    <param name="ext_trigger" type="bool" value="True"/>
    <param name="trigger_controller" type="string" value="trig_controller"/>
    <param name="trigger_rate" type="double" value="10"/>
    <param name="trigger_phase" type="double" value="0"/>
    <param name="port" type="int" value="60000"/>
  </group>
  <node name="wge100_camera_node" pkg="wge100_camera" type="wge100_camera_node" respawn="false" output="screen"/>
  <node name="wge100_camera_proc" pkg="stereo_image_proc" type="imageproc" respawn="false" output="screen">
    <remap from="camera" to="wge100_camera_node"/>
  </node>
</launch>
```



The trigger_controller.xml file:



```
<controller name="trig_controller" type="TriggerControllerNode">
    <actuator name="fl_caster_l_wheel_motor" />
    <waveform rep_rate="1" active_low="0" phase="0" duty_cycle=".5" running="0" pulsed="1" />
</controller>
```



And the mb_configuration.xml file: 

```
<robot name="pr2"> </robot>
```



------------------------------------------------------------------------

## Tutorials

- [How to Configure and Use the WGE100 Camera](#how-to-configure-and-use-the-wge100-camera):
  This tutorial is an introduction to using the WGE100 camera connected
  to a desktop. After reading it you should be able to bring up the
  WGE100 camera, configure the camera, and display the images.
- [How to Configure and Use the WGE100 Stereo Camera on a PR2](#how-to-configure-and-use-the-wge100-stereo-camera-on-a-pr2):
  This tutorial is an introduction to using the WGE100 stereo camera
  connected to a PR2 robot. After reading it you should be able to bring
  up the WGE100 stereo camera and display the images.
- [Running the WGE100 camera in externally triggered mode](#running-the-wge100-camera-in-externally-triggered-mode):
  This tutorial covers using an external trigger with the WGE100 camera
  on the PR2.

Create a new tutorial:

## Troubleshooting

1.  format wiki
2.  language en

### Errors when using package

#### Error: Cannot find the camera on the network



```
user@prX: roslaunch wge100_camera.launch
 [FATAL] 1239932051.129499000: No cameras found
```





```
user@prX: roslaunch wge100_camera.launch
 MAC Address: 00:24:CD:00:00:67
 Product #6805018 : Unit #0003
 PCB rev B : HDL rev 103 : FW rev 108
 [FATAL] 1239932051.129499000: Couldn't find camera with S/N 10
```



**Solution:**

- Does the camera have power? Check that the camera board LEDs are on.

<!-- -->

- Does the camera have a working ethernet connection? If one of the LEDs
  on the camera board is yellow, the connection is probably bad. If the
  link light on the router is off, the connection is probably bad.

<!-- -->

- Is the Linux anti-spoof filter swallowing response packets from the
  camera? The filter for your ethernet interface should be set to 0:
  

```
user@prX: cat /proc/sys/net/ipv4/conf/eth?/rp_filter
 1
 user@prX: sudo bash
 root@prX: echo 0 > /proc/sys/net/ipv4/conf/eth?/rp_filter
```



##### Reset Cameras

You can try to reset all wge100 cameras on a PR2. The reset command
sends a special command to the firmware that can allow the cameras to
recover without power cycling the cameras.

- rosrun dynamic_reconfigure reconfigure_gui
- Select "pr2_camera_synchronizer"
- Check the "Reset" button at the bottom
- Wait until the reset button becomes unchecked.

After running this command, the cameras should recover. You can verify
that all cameras are present by running `pr2-systemcheck`.

#### Error: Trigger mode set error



```
user@prX: roslaunch wge100_camera.launch
 Warning, was unable to create ARP entry (are you root?): Operation not permitted
 [ WARN] 1239932049.130394000: Unable to create ARP entry (are you root?), continuing anyway
 [ INFO] 1239932049.130577000: Configured camera #0, S/N #10, IP address 10.0.3.68
 [FATAL] 1239932051.129499000: Trigger mode set error
```



**Solution:**

- Is the camera ARP entry missing? Run the node as root:



```
user@prX: sudo bash
 root@prX: roslaunch wge100_camera.launch
```



This will create the ARP entry during camera configuration, as you can
verify:



```
user@prX: arp
 Address                  HWtype  HWaddress           Flags Mask            Iface
 10.0.3.68                ether   00:24:CD:00:00:67   CM                    eth0
```



After this running the WGE100 node as normal user should work fine,
until you reboot the computer or attempt to use a different camera.

- Is the IP address assigned to the camera visible? This is likely to be
  a problem if you are running the node on a robot for the first time.

Check ifconfig: 

```
user@prX: ifconfig
 eth0      Link encap:Ethernet  HWaddr 00:01:80:76:67:e3  
           inet addr:10.68.0.2  Bcast:10.68.0.255  Mask:255.255.255.0
```



The camera IP address 10.0.3.68 is not visible to this interface. Find
an unused visible IP address with ping (let's say 10.68.0.68) and
change the ip_address parameter in the launch file:


```
<param name="ip_address" type="str" value="10.68.0.68"/>
```



Don't forget to run the WGE100 node as root after this.

#### Error: Discover error / ioctl failed



```
user@prX: roslaunch wge100_camera.launch
 wgIpGetLocalAddr ioctl failed: No such device
 wgEthGetLocalMac ioctl failed: No such device
 Unable to create socket
 [FATAL] 1239943371.795521000: Discover error
```



**Solution:**

- Is the node broadcasting to the correct ethernet interface? In
  wge100_camera.launch, set parameter "if_name" to "eth0" or
  "eth1" as needed.

#### Error: I'm getting images from the wrong camera



```
user@prX: roslaunch wge100_camera.launch
 MAC Address: 00:24:CD:00:00:67
 Product #6805018 : Unit #0003
 PCB rev B : HDL rev 103 : FW rev 108
 MAC Address: 00:24:CD:00:00:6E
 Product #6805018 : Unit #0010
 PCB rev B : HDL rev 103 : FW rev 108
 [ INFO] 1239943961.243337000: Configured camera #0, S/N #3, IP address 10.0.3.68
```



**Solution:**

- Is the node discovering multiple cameras? In wge100_camera.launch, set
  parameter "serial_number" to that of the camera you want. If you
  don't know, check the list of discovered cameras printed by the node
  (Unit #). In this case we probably want: 

```
<param name="serial_number" type="int" value="10"/>
```



<!-- -->

- Is the camera in the list of discovered cameras? If not, see Error:
  Cannot find the camera on the network.

#### Error: Many packets are dropped



```
user@prX: roslaunch wge100_camera.launch
 [ INFO] 1239993196.341647000: Configured camera #1, S/N #10, IP address 10.0.3.68
[ WARN] 1239993197.820380000: Short frame (video lines were missing)
[ WARN] 1239993197.842489000: Short frame (video lines were missing)
[ WARN] 1239993197.932087000: Short frame (video lines were missing)
[ WARN] 1239993197.985493000: Short frame (video lines were missing)
[ WARN] 1239993197.985972000: Short frame (video lines were missing)
[ WARN] 1239993197.986327000: Frame was missing EOF, no frame information available
[ WARN] 1239993198.009111000: Short frame (video lines were missing)
```



**Solution:**

- Is the Linux UDP buffer size large enough? Set the UDP buffer size to
  8MB: 

```
user@prX: sudo sysctl -w net.core.rmem_max=8388608
```



#### Dropped Frames and "rmem_max"

One common reason for dropped frames on Ethernet connected sensors is a
buffer overrun in the kernel. The default kernel buffer size is
rmem_default. Programs can increase the buffer size up to rmem_max using
setsockopt, but they cannot change rmem_max. Only root can change
rmem_max. When working with Ethernet cameras it is usually necessary to
increase rmem_max so that the camera driver can allocate a large enough
buffer. A poorly written driver might not know that it needs to increase
its buffer, in which case rmem_default can also be adjusted (this will
cause all applications to use large buffers though, so beware).

##### Temporary Changes

You can view rmem_max using sysctl 

```
sysctl net.core.rmem_max
```

 or using
the /proc filesystem 

```
cat /proc/sys/net/core/rmem_max
```



The same two ways are available to set rmem_max


```
sudo sysctl net.core.rmem_max=20000000
```

 or using the /proc filesystem


```
echo 10000000 | sudo tee /proc/sys/net/core/rmem_max
```



##### Permanent Changes

The changes made using sysctl or writing to /proc are lost when the
system is rebooted. To make the changes permanent, add a line to
/etc/sysctl.conf 

```
net.core.rmem_max=20000000
```



##### Programatic Changes

To set rmem_default for a socket, do 

```
size_t bufsize = 20000000; 
if(setsockopt(s, SOL_SOCKET,SO_RCVBUF, &bufsize, sizeof(bufsize)) == -1) {
}
```

 and read
it using 

```
socklen_t bufsizesize = sizeof(bufsize);
if( getsockopt(s, SOL_SOCKET,SO_RCVBUF, &bufsize, &bufsizesize) == 0) {
}
```



Note that the read-back value will be double the written value on linux
systems. Linux allocates more than is requested because user programs
are not expected to anticipate packet storage overhead in the kernel.

You will need to include <sys/socket.h> (and possibly <sys/types.h>,
see the setsockopt man page).

#### Error: No frames received for more than one second.

**Solution:**

- Is the trigger controller running?

#### Error: Trigger matcher dropping frames.

**Solution:**

- Is the driver running on a different computer from the controller? Is
  there a clock skew between the two computers?

#### Error: Failed to set trigger mode/IP.

**Solution:**

- Does the ARP table have a stale entry?
- Is the IP you specified or the default IP correct for the subnet the
  camera is on?

#### Warn: Camera Intrinsics have bad Checksum

**Solution:**

- Has the camera been calibrated? Use the
  [camera_calibration](https://index.ros.org/p/camera_calibration)
  package to calibrate the camera.

#### Warn: Camera Intrinsics have bad Checksum

**Solution:**

- Use the
  [camera_calibration](https://index.ros.org/p/camera_calibration)
  package to calibrate the camera.

#### Error: Image resolution from intrinsics file does not match current video mode

**Solution:**

- Use the
  [camera_calibration](https://index.ros.org/p/camera_calibration)
  package to calibrate the camera for the current video mode.
- Revert to the previous video mode.

#### Camera Calibration is Wrong

**Solution:**

- Have you changed the Region of Interest settings since calibrating the
  camera?
- You can use the
  [camera_calibration](https://index.ros.org/p/camera_calibration)
  package to calibrate the camera for the current video mode.
- You can try reverting to the former Region of Interest settings.

### Things that can go wrong and that need to be handled

- 100 Mbps cable to the head.
- Projector board not powered.
- Cameras not named right.
- Wrong firmware version.
