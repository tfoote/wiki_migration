## Overview

This package contains a ROS driver node for
[Allied Vision Tech Gigabit Ethernet (GigE) cameras](http://www.alliedvisiontec.com/us/products/cameras/gigabit-ethernet/manta.html).
It is built on top of the
[Prosilica GigE SDK](https://index.ros.org/p/prosilica_gige_sdk).

The ROS API of this package is stable. The driver node has been tested
extensively with the
[GC2450C](http://www.alliedvisiontec.com/us/products/cameras/gigabit-ethernet/prosilica-gc/gc2450.html)
model, which was used in the Willow Garage
[Milestone 2](http://www.willowgarage.com/blog/2009/06/03/watch-milestone-2).
The node should work with any AVT/Prosilica GigE camera, and we welcome
reports of use with other cameras.

This page and the [tutorials](#tutorials)
cover expected use of this package. Features of interest to advanced
users only are documented
[here](#advanced).

For basic vision processing of camera images, see the
[image_pipeline](https://index.ros.org/p/image_pipeline).

## Nodes

<a id="NodeAPI"></a> 

```clearsilver
name = prosilica_node
desc = ROS driver for Prosilica GigE cameras. Note that the ROS API varies depending on whether the driver is in streaming or polled mode. In streaming mode it publishes to `camera/image_raw` and `camera/camera_info` like any other camera. In polled mode it publishes on request to a client-specified namespace, following the [[polled_camera]] protocol.<<BR>><<BR>>[[image_transport]] is used for all image publications.
pub {
  group.0 {
    name = Streaming mode
    0.name = camera/image_raw
    0.type = sensor_msgs/Image
    0.desc = The raw image topic.
    1.name = camera/camera_info
    1.type = sensor_msgs/CameraInfo
    1.desc = Calibration info for each image.
  }
  group.1 {
    name = Polled mode
    desc = There may be multiple clients, each with their own `response_namespace`. These topics are only published in response to the `request_image` service.
    0.name = <response_namespace>/image_raw
    0.type = sensor_msgs/Image
    0.desc = The polled image topic for a particular client.
    1.name = <response_namespace>/camera_info
    1.type = sensor_msgs/CameraInfo
    1.desc = The corresponding camera state.
  }
}
srv {
  group.0 {
    0.name = set_camera_info
    0.type = sensor_msgs/SetCameraInfo
    0.desc = Sets the calibration parameters stored internally on the camera.
  }
  group.1 {
    name = Polled mode
    0.name = request_image
    0.type = polled_camera/GetPolledImage
    0.desc = Captures an image and publishes it in the namespace specified by the request message. Returns the timestamp.
  }
}
param {
group.0 {
name=Camera selection
desc=If `~ip_address` is set, the node opens the camera at that IP. If only `~guid` is set, the node opens the camera with that unique ID. If both, the camera is opened by IP address and the GUID verified. If neither, the node opens the first available camera.
  0.name = ~ip_address
  0.type = string
  0.desc = IP address of the camera to open.
  1.name = ~guid
  1.type = string
  1.desc = Unique ID of the camera to open.
}
}
```



## Command-line tools

### set_ip

Sets the camera to a fixed IP address. The camera must be visible to
[ListCameras](https://index.ros.org/p/prosilica_gige_sdk), and must be
the only camera listed. The camera must be unopened (i.e.
`prosilica_node` should not be running). This tool is normally used
once to configure a new camera (see the
[tutorials](#tutorials)).

Usage: 

```
$ set_ip <IP address>
```

## Tutorials

- [Configuring the Prosilica GigE for a Desktop](#configuring-the-prosilica-gige-for-a-desktop):
  This tutorial covers configuring the Prosilica camera for a desktop
  and viewing images.
- [How to Determine Your Prosilica GigE Camera's IP Address](#how-to-determine-your-prosilica-gige-cameras-ip-address):
  This tutorial will show you how to determine the prosilica camera's
  IP address if you do not remember it.
- [Configuring the Prosilica GigE for the PR2](#configuring-the-prosilica-gige-for-the-pr2):
  This tutorial covers configuring the Prosilica camera for a PR2 and
  viewing images.
- [Introduction to working with the Prosilica camera.](#introduction-to-working-with-the-prosilica-camera):
  This introduction will teach you how to work with a pre-configured
  Prosilica camera.

## Advanced

This page documents features of the
prosilica_camera package that most
users will not need, but may be useful to advanced users.

### Command-line tools

These work only for an unopened camera (i.e. `prosilica_node` should
not be running).

#### read_memory

Outputs the current contents of the camera's non-volatile user memory.
This is where `prosilica_node` saves the camera calibration, so this
tool can be used to view the saved calibration, if any.

Usage: 

```
$ read_memory <IP address>
```



#### write_memory

Overwrites the contents of the camera's non-volatile user memory with
the contents of a file. The file must be 512 bytes or less. This tool
can be used to upload a set of calibration parameters archived in one of
the [file formats](https://index.ros.org/p/camera_calibration_parsers)
understood by `prosilica_node`.

The normal way of setting the calibration is by running
[camera_calibration](https://index.ros.org/p/camera_calibration).

Usage: 

```
$ write_memory <IP address> <file>
```

## Troubleshooting

1.  format wiki
2.  language en

### Basic Configuration

Be sure you have followed the basic configuration instructions in the
[tutorials](#tutorials).

### Errors when using prosilica_camera

#### Error: Found no cameras on local subnet



```
[ INFO] 1236977839.419999000: Starting node [/prosilica]
 [ INFO] 1236977839.420245000: Started XML-RPC server on port [44787]
 [ INFO] 1236977839.420305000: Started TCPROS server on port [59486]
 [ WARN] 1236977844.424645000: Found no cameras on local subnet
```



**Solution:**

- Is the prosilica camera connected and setup properly? Please follow
  the tutorials for instructions on configuring the
  [camera](#how-to-determine-your-prosilica-gige-cameras-ip-address)
  and the ROS node
  ([standalone](#configuring-the-prosilica-gige-for-a-desktop),
  [on the PR2](#configuring-the-prosilica-gige-for-the-pr2)).

#### Warning: Failed to load intrinsics from camera

**Solution:**

- Is your camera calibrated? Please follow the tutorial for
  [calibrating a monocular camera](https://index.ros.org/p/camera_calibration).

### FAQ

#### I can connect to the camera, but images are not getting through.

Chances are that your firewall (packet filter) is getting in the way.
The GigE camera protocol uses a control connection to negotiate a port
for data transfer. The camera then tries to connect to that port on the
host. The issue is that the packet filter is unaware of that negotiation
and considers the incoming video stream as an unrequested (possibly
hostile) connection attempt from the outside and blocks it.

**Solution:**

- Allow external connection on the interface that is connected to the
  camera. Consult the documentation of your distribution on how to do
  that.
- You can also disable the packet filter completely
  (System->Administration->Firewall->"Disable" on Fedora).
- Note that in both cases you should not be connected to any hostile
  networks.

## Configuring the Prosilica GigE for a Desktop

### Compiling

Start by getting the dependencies and compiling the driver.


```
$ rosdep install prosilica_camera image_view
$ rosmake prosilica_camera image_view
```



### Plugged In and Power On

First power on the camera and connect it to any computer. Wait for both
the green and orange LEDs on the camera ethernet port to stay lit.

### Host Computer Configuration

If you connect the camera to a non-robot host computer, you will need to
configure the computer's network stack so that it can find the camera.
The initial IP address of the camera is `169.254.x.x` (out of the box)
and we can this information to configure our host computer. If the
camera IP has changed and you don't know the IP, please see the section
on
[how to determine Prosilica IP address](#how-to-determine-your-prosilica-gige-cameras-ip-address).

#### Shared Ethernet Port

Use these instructions if you are using the same ethernet interface to
communicate with the camera and with another network. (For example, your
desktop computer is connected to a hub that is connected to the LAN and
to the camera.)

Figure out which network interface the camera is connected to
(`ifconfig` or `route` may help). In this example we will assume
that the camera is connected to `eth0`.

Create an alias through which the camera's IP address can be accessed:



```
$ sudo ifconfig eth0:0 X.X.X.99 netmask 255.255.255.0
```



where `X.X.X` is the same as the camera's IP address.

#### Dedicated Ethernet Port

Figure out which interface the camera is connected to. In this example,
it is connected to `eth0`.

Setup the interface so that it can communicate with the camera:



```
$ sudo ifconfig eth0 X.X.X.99 netmask 255.255.255.0
```



where `X.X.X` is the same as the camera's IP address.

#### Finding the Camera

Run `ListCameras` to find the camera's unique ID (and make sure it is
visible). `ListCameras` will repeatedly discover cameras on the
network until you exit with Ctrl-C.



```
$ rosrun prosilica_gige_sdk ListCameras
```





```
***********************************
No camera detected ...
***********************************
02-2171A-06167 -  GC2450C - Unique ID =   103732 IP@ =       169.254.1.86 [available]
***********************************
02-2171A-06167 -  GC2450C - Unique ID =   103732 IP@ =       169.254.1.86 [available]
```



You can also trying pinging the camera



```
$ rosrun prosilica_gige_sdk Ping CAMERA_IP
```

 

```
-> 02-2171A-06167 - GC2450C
Mode supported:         FIXED,DHCP,AutoIP
Current mode:           FIXED
Current address:        10.68.0.20
Current subnet:         255.255.255.0
Current gateway:        0.0.0.0
```



Now that you can see the camera let's look at some images from the
camera.

### Software Bringup

To start the Prosilica camera node in continuous mode, create a copy of
the example launch file from `prosilica_camera`:



```
$ cp `rospack find prosilica_camera`/streaming.launch prosilica.launch
```



Now edit **prosilica.launch** to set parameter `ip_address` to the
prosilica IP address from the previous step. The relevant snippet of the
launch file is reproduced below:



```
<launch>
  <node name="prosilica_driver" pkg="prosilica_camera" type="prosilica_node" output="screen">
    <param name="ip_address" type="str" value="IP_ADDRESS"/>
    <param name="trigger_mode" type="str" value="streaming"/>
    <remap from="camera" to="prosilica" />
    <rosparam command="load" file="$(find prosilica_camera)/cam_settings.yaml" />
  </node>
</launch>
```



Now roslaunch your launch file:



```
$ roslaunch prosilica.launch
```



### Viewing Images

To view images coming from the camera:



```
$ rosrun image_view image_view image:=/prosilica/image_raw
```



Now that you can view images from your camera you can learn how to
calibrate it in this tutorial,
[how to calibrate a monocular camera](https://index.ros.org/p/camera_calibration).

## How to Determine Your Prosilica GigE Camera's IP Address

### Compiling

Start by getting the dependencies and compiling the driver.



```
$ rosdep install prosilica_camera
$ rosmake prosilica_camera
```



### Powered On and Plugged in

Make sure that your Prosilica camera is powered at 12V, connected to
your computer, and the green and orange network lights are lit.

### Making Sure the Network is Configured for IPv4 Networking

Before you can find a camera on the network, the network adapter to
which the camera is connected must be configured for IPv4 networking. In
many cases this will be done already, so try skipping to the next
section of this tutorial, and come back here if the discover command
can't find your camera.

Configuring a network adapter is beyond the scope of this tutorial. The
following tips may allow you to get started, but may get you in trouble
with your network administrator. Moreover, the setup you get by
following these tips will not persist when the computer is rebooted.

To check that an adapter is configured for IPv4 networking, use the
`ifconfig` command. For example if your camera is connected to
`eth0`, do:



```
$ ifconfig eth0
eth0      Link encap:Ethernet  HWaddr 00:50:b6:03:f4:60
          inet6 addr: fe80::250:b6ff:fe03:f460/64 Scope:Link
          UP BROADCAST RUNNING MULTICAST  MTU:1500  Metric:1
          RX packets:0 errors:0 dropped:0 overruns:0 frame:0
          TX packets:6 errors:0 dropped:0 overruns:0 carrier:0
          collisions:0 txqueuelen:1000
          RX bytes:0 (0.0 B)  TX bytes:492 (492.0 B)
```

 In this case, the camera has an **inet6 addr**,
but no **inet addr**, so it is not configured for IPv4 networking.

We can give the adapter an IPv4 address with the following command (this
address probably won't get you in trouble):



```
$ sudo ifconfig eth0 192.168.123.1 netmask 255.255.255.0
```

 Now we can check that the computer does indeed
have an **inet addr**:



```
$ ifconfig eth0
eth0      Link encap:Ethernet  HWaddr 00:50:b6:03:f4:60
          inet addr:192.168.123.1  Bcast:192.168.123.255  Mask:255.255.255.0
          inet6 addr: fe80::250:b6ff:fe03:f460/64 Scope:Link
          UP BROADCAST RUNNING MULTICAST  MTU:1500  Metric:1
          RX packets:0 errors:0 dropped:0 overruns:0 frame:0
          TX packets:20 errors:0 dropped:0 overruns:0 carrier:0
          collisions:0 txqueuelen:1000
          RX bytes:0 (0.0 B)  TX bytes:3641 (3.5 KB)
```



### Capturing the IP address

Run:



```
sudo tcpdump -n src port 3956 -i ethx
```

 where `ethx` is the interface the camera is
connected to. This will be listening for traffic and return the IP
address of our camera.

In another window run:



```
rosrun prosilica_gige_sdk ListCameras
```

 The tcpdump command will output a line similar
to this one:

. 

```
23:14:47.009127 IP 10.68.0.20.3956 > 10.68.0.1.41020: UDP, length 256
```



The address of the camera is `10.68.0.20`. (Note that `ListCameras`
will probably not see the camera.)

You can now configure the network interface (or an alias) in such a way
that the camera is on the same subnet, and you can set the camera's IP
address as described in the
[configuring the Prosilica gigE for a desktop](#configuring-the-prosilica-gige-for-a-desktop)
tutorial.

## Configuring the Prosilica GigE for the PR2

### Compiling

Start by getting the dependencies and compiling the driver.


```
$ rosdep install prosilica_camera image_view
$ rosmake prosilica_camera image_view
```



### Camera Preliminaries (things you do only once for each camera)

This section is for brand-new, just-out-of-the-box cameras. Cameras on
PR2s should already be configured correctly.

#### Set the IP address

The camera must be given a fixed IP address so we can find it over the
PR2 ethernet network. First power on the camera and connect it to any
computer. Wait for both the green and orange LEDs on the camera ethernet
port to stay lit. \[Note: if you are reconfiguring a camera which has
already been given a fixed IP address, connecting through a hub will not
work. You will need to connect the camera to a dedicated ethernet port.
See
[Host Computer Configuration](#host-computer-configuration-1).\]

Run `ListCameras` to make sure the camera is visible. `ListCameras`
will repeatedly discover cameras on the network until you exit with
Ctrl-C.



```
$ rosrun prosilica_gige_sdk ListCameras
```





```
***********************************
No camera detected ...
***********************************
02-2171A-06167 -  GC2450C - Unique ID =   103732 IP@ =       10.0.1.86 [available]
***********************************
02-2171A-06167 -  GC2450C - Unique ID =   103732 IP@ =       10.0.1.86 [available]
```



The ROS launch scripts expect to find the camera at address
`10.68.X.20`, where X is the subnet of the robot. We'll assume our
robot has IP address `10.68.0.2`, so our camera should have address
`10.68.0.20`. Configure the camera using this command, substituting
the desired IP address:



```
$ rosrun prosilica_camera set_ip 10.68.0.20
```





```
No camera found at 10.68.0.20, trying to change settings of a local camera...
Detected camera.
Original settings:
	02-2171A-06167 - GC2450C - Unique ID = 103732
	Mode:		DHCP&AutoIP
	Address:	169.254.0.10
	Subnet:		255.255.255.0
	Gateway:	0.0.0.0
Applying new settings...
New settings:
	02-2171A-06167 - GC2450C - Unique ID = 103732
	Mode:		FIXED
	Address:	10.68.0.20
	Subnet:		255.255.255.0
	Gateway:	0.0.0.0
```



Now let's verify success. Since we have just changed the IP address of
the camera, if you are using a non-robot host computer you will probably
need to add an alias to the new subnet of the camera as described in
[Host Computer Configuration](#host-computer-configuration-1).

The camera may no longer be visible to `ListCameras`, so we will ping
it directly:



```
$ rosrun prosilica_gige_sdk Ping 10.68.0.20
```





```
-> 02-2171A-06167 - GC2450C
Mode supported:		FIXED,DHCP,AutoIP
Current mode:		FIXED
Current address:	10.68.0.20
Current subnet:		255.255.255.0
Current gateway:	0.0.0.0
```



If you instead see:



```
$ rosrun prosilica_gige_sdk Ping 10.68.0.20
```





```
no camera was detected at the address you supplied ...
```

 something has gone wrong, and you should ask
Patrick.

#### Save pr2-specific settings

While exposing, the camera must send a sync signal to inhibit the stereo
light projector. This step ensures that the camera always powers on with
the proper settings to do so.

Configure the camera using this command, substituting the IP address
from the previous step: 

```
$ rosrun prosilica_camera set_inhibition 10.68.0.20
```





```
Configured camera successfully.
```



### Host Computer Configuration

If you connect the camera to a non-robot host computer, you will need to
configure the computer's network stack so that it can find the camera.

#### Shared Ethernet Port

Use these instructions if you are using the same ethernet interface to
communicate with the camera and with another network. (For example, your
desktop computer is connected to a hub that is connected to the LAN and
to the camera.)

Figure out which network interface the camera is connected to
(`ifconfig` or `route` may help). In this example we will assume
that the camera is connected to `eth0`.

Create an alias through which the camera's IP address can be accessed:



```
$ sudo ifconfig eth0:0 10.68.X.99 netmask 255.255.255.0
```



You should now be able to ping the camera as described above.

#### Dedicated Ethernet Port

Figure out which interface the camera is connected to. In this example,
it is connected to `eth1`.

Setup the interface so that it can communicate with the camera:



```
$ sudo ifconfig eth1 10.68.X.99 netmask 255.255.255.0
```



You should now be able to ping the camera as described above.

### Software Bringup

To start the Prosilica camera node in continuous mode, create the launch
file below using the prosilica IP:



```
<launch>
  <group ns="prosilica">
    <include file="cam_settings.xml"/>
    <param name="trigger_mode" type="str" value="streaming"/>
    <param name="ip_address" type="str" value="10.68.0.20"/>
  </group>
  <node name="prosilica" pkg="prosilica_camera" type="prosilica_node" respawn="\
false" output="screen"/>
</launch>
```



### Viewing Images

To view images coming from the camera:



```
$ rosrun image_view image_view image:=/prosilica/image_raw
```

## Introduction to working with the Prosilica camera.

This is an introduction to using the high-resolution Prosilica camera.
It assumes that the camera has already been configured. If you need to
configure a new Prosilica camera, please see the other tutorials in this
package.

### Starting the camera

The camera is started by running the driver node, `prosilica_node`. An
example can be found in the launch file `prosilica.launch` in the
`prosilica_camera` package. It was most likely started from your robot
launch file (for example, on the PR2s, prX.launch). Use `rosnode list`
to see if the node is running.

### Streaming mode

The camera can start in two modes. The first is `streaming`. This mode
looks like most other cameras.



```clearsilver
pub{
0.name= image_raw
0.type= sensor_msgs/Image
0.desc= The raw image topic. 
1.name= camera_info
1.type= sensor_msgs/CameraInfo
1.desc= Camera intrinsics for images published on `image_raw`.
}
```



### Polled mode

Since the camera is high resolution, continuous streaming may use up too
much bandwidth. So the Prosilica can also be run in a `polled` mode.
In this mode, nothing is published until an image is requested using the
`request_image`
([polled_camera/srv/GetPolledImage](https://docs.ros.org/en/rolling/p/polled_camera/srv/GetPolledImage.html))
service. For example, from the command line, you can request a 100x100
pixel image using:



```
rosservice call /prosilica/request_image /<response_namespace> '{x_offset: 0, y_offset: 0, height: 100, width: 100}'
```





```clearsilver
pub{
0.name= <response_namespace>/image_raw
0.type= sensor_msgs/Image
0.desc= The polled image topic for a particular client.
1.name= <response_namespace>/camera_info
1.type= sensor_msgs/CameraInfo
1.desc= Camera intrinsics for images published on `<response_namespace>/image_raw`.
}
```



### Changing parameters

As for all cameras, the easiest way to change parameters is to use
**dynamic_reconfigure**.

From a GUI: 

```
rosmake dynamic_reconfigure
rosrun dynamic_reconfigure reconfigure_gui
```

 and select **prosilica** from the
drop-down menu.

From the command line or code, use `dynparam` in the
[dynamic_reconfigure](https://index.ros.org/p/dynamic_reconfigure)
package.

#### Switching modes

The mode is controlled by the parameter `trigger_mode` and can be set to
`polled` or `streaming` mode.

In the **reconfigure_gui**, switch the "trigger_mode" field between
`polled` and `streaming` mode.

#### Setting other parameters

The **reconfigure_gui** can be used to set any other of the
[prosilica_node's parameters](#NodeAPI).

### Viewing Images

#### Streaming mode

To view images streaming from the camera:



```
$ rosrun image_view image_view image:=prosilica/image_raw
```



#### Polled mode

In polled mode we specify an output namespace to the camera driver. In
this example we'll use `my_output`. First start the image viewer:


```
$ rosrun image_view image_view image:=my_output/image_raw
```



This should bring up a blank window. No image is displayed yet because
in polled mode, the camera publishes images only on request (by service
call). We can issue a request from the command line like this:


```
$ rosservice call prosilica/request_image my_output '{x_offset: 0, y_offset: 0, height: 100, width: 100}'
```



This requests an image of the camera's top-left 100x100 region, with
publications in `my_output`.
[polled_camera](https://index.ros.org/p/polled_camera) contains a node
to continually request images, like this: 

```
$ rosrun polled_camera poller 2 camera:=prosilica output:=my_output
```



This requests images from the camera at 2 Hz.

### Processing images

To learn how to process images from the Prosilica camera, see the
[image pipeline](https://index.ros.org/p/image_pipeline), in particular
[camera_calibration](https://index.ros.org/p/camera_calibration) and
[image_proc](https://index.ros.org/p/image_proc).
