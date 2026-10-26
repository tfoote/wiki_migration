## Overview

The Willow Garage 100 Mbps Ethernet (WGE100) camera is a 752x480
Ethernet camera developed for the PR2 robot. The PR2's narrow stereo
camera is a monochrome WGE100, while its wide stereo camera and forearm
cameras are in color. This package contains the
[wge100_camera_node](#Wge100CameraNode), a ROS driver for a monocular
WGE100 camera, the [wge100_multi_configurator](#Wge100MultiConfigurator)
node, which allows two cameras in a stereo pair to be configured from
one centralized location, and a suite of
[command-line tools](#CommandLineTools) to manage the camera.

### Using the Dual Stereo Cameras or Forearm Cameras on the PR2

Most PR2 users will not need the information on this page as the cameras
are brought up at the same time as the robot. Instead they can refer to
the following sources:

- For simplified instructions on setting up camera frame rate, or
  synchronization with the PR2's texture projector refer to the
  [pr2_camera_synchronizer](pr2_camera_synchronizer#UsingOnThePr2)
  documentation.

<!-- -->

- For calibrating the cameras or doing vision processing, you will also
  want to look at the [image pipeline stack](image_pipeline).

<!-- -->

- Other packages are available to use and process data coming from
  [monocular](image_proc) or [stereo](stereo_image_proc) cameras.

<!-- -->

- Tutorials are available showing how to dynamically reconfigure a
  node's parameters using
  [a GUI](hokuyo_node/Tutorials/UsingReconfigureGUIToChangeHokuyoLaserParameters),
  [from the command-line, a launch file or C++ code](hokuyo_node/Tutorials/UsingDynparamToChangeHokuyoLaserParameters).

<!-- -->

- For a reference of the WGE100 parameters you can skip directly to the
  [ROS API](#ROS_API) to learn about various parameters.

### Concurrent Access

Except for the
[access_register](/AdvancedCommandLine#Accessing_Imager_Registers:_access_register)
and [discover](#Discover) tools, which can be used at any time, the
WGE100 tools are not designed for concurrent access to the camera.

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
(set using [set_name](#SetName)). If there is only one camera present, a
URL can indicate that whatever camera is found should be used.

### Types of URLs

There are three types of camera URLs:

- **name** URLs indicate the name of the camera to be found. You can set
  the name of a camera using the [set_name](#SetName) utility. E.g.:
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

## ROS API



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



## Command-Line Tools

The following command-line tools are helpful when configuring the
camera.

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
should be done through the [ camera calibration ](camera_calibration )
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
[Accessing Imager Registers: access_register](/AdvancedCommandLine#Accessing_Imager_Registers:_access_register) 1.
[Reflashing the Camera Firmware: upload_mcs](/AdvancedCommandLine#Reflashing_the_Camera_Firmware:_upload_mcs) 1.
[Checking Flash Programming: check_flash](/AdvancedCommandLine#Checking_Flash_Programming:_check_flash) 1.
[Dumping the Flash Contents: read_all_flash](/AdvancedCommandLine#Dumping_the_Flash_Contents:_read_all_flash)

## Flash Contents

For information on contents of the WGE100 flash memory, you may consult
[this page](/FlashContents).

## Tutorials
