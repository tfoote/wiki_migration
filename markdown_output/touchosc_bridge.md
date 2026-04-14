## Overview

The main components of using TouchOSC with ROS are:

-   The TouchOSC app for iPad or iPhones
-   A TouchOSC layout, which is composed of \'\'tabpages\'\'
-   The \`touchosc_bridge\` ROS node, which is composed of \'\'tabpage
    handlers\'\'

### TouchOSC

From hexler.net: \'\'\'TouchOSC is a modular OSC and MIDI control
surface for iPhone / iPod Touch / iPad.\'\'\' It supports sending and
receiving Open Sound Control messages over a Wi-Fi network using the UDP
protocol.

TouchOSC is published and created by hexler (<http://hexler.net>), and
is available on the \[Apple App Store for
4.99\](<http://itunes.apple.com/app/touchosc/id288120394?mt=8>).

TouchOSC allows for the creation of touch interactive control layouts
separated onto \"tabpages\". The app supports up to 25 tabpages in a
single layout file. Layouts are created using the freely available
\[TouchOSC Editor\](<http://hexler.net/software/touchosc>). For more
information on all of the controls available, as well as their behavior
with ROS, check out the [Controls Reference](touchosc_bridge/Controls).

### Video Demo

[Youtube](https://www.youtube.com/watch?v=ZHHp1WSbQQU)

## Quick Reference

A few links of interest:

-   [Controls Reference](touchosc_bridge/Controls) - A list of TouchOSC
    controls along with their behavior with the
    [touchosc_bridge/DefaultTabpageHandler](touchosc_bridge/DefaultTabpageHandler)

```{=html}
<!-- -->
```
-   [Tabpage Handler Reference](touchosc_bridge/TabpageHandler) - A
    reference for creating your own tabpage handlers.

## Node API

This is the node configuration regardless of which tabpage handlers are
loaded. For parameters for individual tabpage handlers, check the
respective documentation.

```clearsilver
name = touchosc_bridge
desc = TouchOSC to ROS bridge node
pub {
0.name = touchosc_bridge/accxyz
0.type = sensor_msgs/Imu
0.desc = Accelerometer data from iOS clients.  `msg.header.frame_id` will contain the IP address of the sending client.
1.name = touchosc_bridge/tabpage
1.type = touchosc_msgs/Tabpage
1.desc = Sent when a client switches tabpages.  Contains tabpage name. `msg.header.frame_id` will contain the IP address of the sending client.
2.name = /diagnostics
2.type = diagnostic_msgs/DiagnosticArray
2.desc = Diagnostic information about the state of the `touchosc_bridge` node.  Also includes <<MsgLink(diagnostic_msgs/DiagnosticStatus)>> messages from each of the registered tabpage handlers.
}
sub {
0.name = touchosc_bridge/vibrate
0.type = std_msgs/Empty
0.desc = When a message is received, will turn on the vibrate motors of all capable devices for approximately half a second
1.name = touchosc_bridge/tabpage
1.type = touchosc_msgs/Tabpage
1.desc = When a message is received, change tabpages on all clients.  Populate `msg.header.frame_id` with an IP address to change the tabpage on a single client.
}
param {
0.name = ~osc_name
0.type = string
0.desc = Name of the node as it will appear in the Bonjour/Zeroconf system.
0.default = Test
1.name = ~port
1.type = int
1.desc = Port that the OSC server will listen on
1.default = 8000
2.name = ~regtype
2.type = string
2.desc = Bonjour registration type of the OSC server
2.default = _osc._udp
3.name = ~print_fallback
3.type = bool
3.desc = setting the parameter to "True" will cause unhandled incoming OSC messages to be printed to the console.
3.default = False
4.name = ~vibrate
4.type = bool
4.desc = When True, the node will create a `touchosc_bridge/vibrate` subscriber.
4.default = True
5.name = ~publish_accel
5.type = bool
5.desc = When True, the node will publish iPod and iPad accelerometer data on `touchosc_bridge/accxyz`.  Note: "Send Accelerometer Data" must be enabled in the TouchOSC application for this to work
5.default = True
6.name = ~publish_diag
6.type = bool
6.desc = When True, the node publishes <<MsgLink(diagnostic_msgs/DiagnosticArray)>> message on `/diagnostics`
6.default = True
7.name = ~tabpage_sub
7.type = bool
7.desc = When True, the node will send tabpage switch messages received on the `touchosc_bridge/tabpage` topic to clients.
7.default = True
8.name = ~load_default
8.type = bool
8.desc = When True, and when a layout file is loaded, any loaded tabpages not matching a tabpage handler will go to the [[touchosc_bridge/DefaultTabpageHandler]].
9.name = ~layout_path or layout_path
9.type = string
9.desc = A path to a group of layout files to use with `touchosc_bridge`.
9.default = None
10.name = ~layouts or layouts
10.type = list
10.desc = A list of layout files to use with `touchosc_bridge`
10.default = None
11.name = ~layout_file or layout_file
11.type = path
11.desc = Path (including filename) of a layout to use with `touchosc_bridge`
11.default = None
}
```
