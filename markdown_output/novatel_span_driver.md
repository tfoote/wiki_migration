![\|align=\"right\"](attachment:ProPak6.png)

## Archived Status

The GitHub repository for this driver has been marked as Archived. Thus,
this driver is not under active development and is not being maintained.

## Support Status

This driver is specific to older OEM6 type NovAtel products and is not
supported by !NovAtel.

!NovAtel released a supported driver in early 2020. It is available
here: [novatel_oem7_driver](novatel_oem7_driver)

## Overview

This is a driver for
[NovAtel devices running SPAN](http://www.novatel.com/products/span-gnss-inertial-systems/),
especially the
[ProPak6](http://www.novatel.com/products/gnss-receivers/enclosures/propak6/).

SPAN technology couples precision GNSS receivers with robust Inertial
Measurement Units to provide reliable, continuously available, position,
velocity and attitude---even through short periods of time when
satellite signals are blocked or unavailable.

This driver publishes GNSS data as a
\<\<MsgLink(sensor_msgs/NavSatFix)\>\>, and inertial navigation system
(INS) data as \<\<MsgLink(nav_msgs/Odometry)\>\>. You can plot this
using [rviz](rviz), as well as monitoring your overall system using
[diagnostics](diagnostics):

![\|height=\"180\"](attachment:rviz-novatel.png)
![\|height=\"180\"](attachment:span-robot-monitor.png)

## Usage

### Initial Setup

This driver assumes that your unit has been configured with the ethernet
port enabled for TCP. There are various ways this can be set up, but the
easiest is to connect to your receiver with **Novatel Connect**
([zip](http://www.novatel.com/assets/Documents/Downloads/NovAtelConnect_Setup_1_6_0.zip)),
using the serial or USB interface. Then, using the device\'s console:

```
wificonfig state disabled
ethconfig etha auto auto auto auto
icomconfig icom1 tcp :3001
ipconfig etha static [address] 255.255.255.0 [gateway]
saveconfig
saveethernetdata etha
``` You can confirm that the settings were saved by
power-cycling the device, reconnecting, and outputting these settings
like so:

```
log wificonfig once
log ethconfig once
log icomconfig once
log ipconfig once
``` From the **Wizards** menu, select **SPAN
Alignment**, which will take you through the position and orientation of
the IMU relative to your vehicle\'s base_link, and the relative position
of the GNSS antenna(s).

Note that if you only need the console and won\'t need to run the SPAN
setup wizard, you may bypass Novatel Connect and just use an ordinary
serial console at 9600 baud. If you are configuring multiple units, you
can run the SPAN wizard only once, and enter the supplied SPAN setup
commands into the other devices using the console or the
\`configuration/command\` rosparam.

### Launch

Run the example launchfile:

```
roslaunch novatel_span_driver example.launch ip:=[address] --screen
``` You should see topics come up for
\`navsat/fix\`, \`navsat/odom\`, \`imu/data\`, \`/diagnostics\`, etc.
These will publish data once the system has acquired an initial GNSS
fix.

## Nodes

```clearsilver
node.0 {
 name = driver
 desc = Basic ethernet driver.
 pub {
  0.name = imu/data
  0.type = sensor_msgs/Imu
  0.desc = Filtered orientation, rotation, and acceleration data from device. Note that because of the message being used for this data, it will not be published until the GNSS has achieved a fix and the SPAN system has performed its initial alignment.
  1.name = navsat/fix
  1.type = sensor_msgs/NatSavFix
  1.desc = GNSS position fix.
  2.name = navsat/odom
  2.type = nav_msgs/Odometry
  2.desc = Full system solution (position, orientation, velocity, angular velocity).
  3.name = navsat/origin
  3.type = geometry_msgs/Pose
  3.desc = Offset of odom origin to origin of UTM zone. Is [0, 0] by default, but with the '''zero_start''' parameter set, will be the easting and northing of the initial fix.
 }
 param {
  0.name = ~ip
  0.type = string
  0.desc = IP address of SPAN device.
  0.default = 198.161.73.9
  1.name = ~port
  1.type = int
  1.desc = Network port of SPAN device.
  1.default = 3001
  2.name = ~pcap_file
  2.type = string
  2.desc = For testing, play back data from this recording, rather than a live system.
  2.default = None
  3.name = ~configuration/log_request
  3.type = dict
  3.desc = Set data types and frequencies to log from device.
  4.name = ~configuration/imu_connect
  4.type = dict
  4.desc = Set IMU port and type.
  5.name = ~configuration/command
  5.type = dict
  5.desc = Arbitrary commands to execute on device after connection.
 }
}
```

## Implementation

The driver exists in four parts, all of which run together in a single
process:

-   A translator which receives the binary !NovAtel data logs and use
    them to populate the messages supplied by
    [novatel_msgs](novatel_msgs).
-   A
    [NovatelPublisher](http://docs.ros.org/api/novatel_span_driver/html/classnovatel__span__driver_1_1publisher_1_1NovatelPublisher.html)
    class, which subscribes to those !NovAtel-specific messages, and
    republishes them as standard ROS messages like
    \<\<MsgLink(sensor_msgs/NavSatFix)\>\> and
    \<\<MsgLink(nav_msgs/Odometry)\>\>.
-   A
    [NovatelDiagnostics](http://docs.ros.org/api/novatel_span_driver/html/classnovatel__span__driver_1_1diagnostics_1_1NovatelDiagnostics.html)
    class, which specifically handles publishing a
    [diagnostics](diagnostics), so that you can monitor the state of the
    SPAN system using [rqt_robot_monitor](rqt_robot_monitor).
-   A
    [NovatelWheelVelocity](http://docs.ros.org/api/novatel_span_driver/html/classnovatel__span__driver_1_1wheel__velocity_1_1NovatelWheelVelocity.html)
    class, which optionally subscribes to your platform\'s encoder
    \`odom\` topic, and passes that data through to the SPAN system so
    that it can use it in its fused pose estimate.

## Tests

The source repository includes example captures from a ProPak6 mounted
on a [Husky](Robots/Husky). To create your own captures, use
\`tcpdump\`:

```
sudo tcpdump -i br0 port 3001 -w capture.pcap
gzip capture.pcap
```

## Resources

The following documents from !NovAtel are helpful in understanding what
this driver is about and how it works:

-   [SPAN on OEM6 Firmware Reference Manual](http://www.novatel.com/assets/Documents/Manuals/OM-20000144UM.pdf)
-   [OEM6 Family Firmware Reference Manual](http://www.novatel.com/assets/Documents/Manuals/om-20000129.pdf)
-   [ProPak6 User Manual](http://www.novatel.com/assets/Documents/Manuals/OM-20000148.pdf)

If you\'d like more information about [Husky](Robots/Husky) or would
like a quote for Husky equipped with SPAN, please use
[the form here](http://www.clearpathrobotics.com/gen-request-a-quote/).

## Roadmap

In the fullness of time, it may make sense to rewrite this driver in
C++, but this is not immediately planned. Other possible next steps:

-   Allow the driver to deduce the SPAN setup parameters using URDF,
    rather than requiring a separate, parallel configuration.
-   Disable logs associated with messages not being subscribed to.
-   Output IMU data regardless of whether a GNSS fix has been achieved.
-   Interpret more of the system\'s diagnostic bitfields.

If you\'re interested in working on these or other extensions, please
use the Github issue tracker to get in touch.
