## Package Overview

`teleop_handler` is a *tabpage handler* for the
[touchosc_bridge](touchosc_bridge) package. It provides a basic
teleoperation example that you can run out of the box on your robot, or
modify for your own purposes.

This package includes layouts for both iPad and iPhone-sized devices in
the `teleop_handler/layouts` directory. When launched, the node will
respond to incoming OSC messages from both sized layouts.

## Video Demo

[Youtube](https://www.youtube.com/watch?v=iPB_6XdgOwA)

## Screenshots

### iPod Sized

![Teleop Layout for iPod](attachment:teleop-ipod.png)

### iPad Sized

![Teleop Layout for iPad\|width=700](attachment:teleop-ipad.png)

## Features

Some of the main features of the `teleop_handler`. These features may
be seen in the above YouTube video.

-   Control "Master"
-   When the node starts, all devices are "reset" to a default status
    (joysticks center on screen, control button deselects.
-   When a client touches the "Control" button in the center of the
    screen, then control privileges are set to that device, and all
    other devices are notified of the new master client.
-   If the client closes, or the tabpage switches, then "master"
    status will be lost.
-   Display sync
-   All active clients (for a discussion of what constitutes "active",
    check the [touchosc_bridge](touchosc_bridge) documentation) will
    synchronize their displays to the master.

## Configuration

Example launch and configuration files are included for the
`teleop_handler` in it's package directory. Also, an example
`teleop.yaml` file is included below. This file should be loaded to
the [Parameter Server](Parameter Server) using your configured
`.launch` file.



```
teleop:
  # Required parameters
  pkg: teleop_handler
  class: 'teleoptabpage/TeleopTabpageHandler'
  tabpage_aliases: [ 'teleop-ipad', 'teleop-ipod' ]
  
  max_vx: 0.8
  max_vy: 0.8
  max_vw: 0.4
  max_run_vx: 1.2
  max_run_vy: 1.2
  max_run_vw: 1.0
  min_freq: 5
```



More details on configuring launch files for
[touchosc_bridge](touchosc_bridge) can be found in the
[rososc_tutorials](rososc_tutorials) and in the
[touchosc_bridge](touchosc_bridge) package documentation.


```
<node pkg="touchosc_bridge" type="touchosc_bridge.py" name="touchosc_bridge">
    <param name="osc_name" value="ROS Teleop"/>
    <param name="port" value="9000" />
    <param name="print_fallback" value="False"/>
    <param name="load_default" value="False"/>
    <rosparam param="handlers">[teleop]</rosparam>
    <rosparam command="load" file="$(find teleop_handler)/cfg/teleop.yaml" />
</node>
```





```clearsilver
name = TeleopTabpageHandler
desc = Tabpage Handler to be used with touchosc_bridge

pub {
0.name = cmd_vel
0.type = geometry_msgs/Twist
0.desc = A stream of velocity commands meant for execution by a mobile base
}
param {
0.name = ~<tabpage>/max_vx
0.type = float32
0.desc = Maximum x velocity
0.default = 0.6
1.name = ~<tabpage>/max_vy
1.type = float32
1.desc = Maximum y velocity
1.default = 0.6
2.name = ~<tabpage>/max_vw
2.type = float32
2.desc = Maximum rotational velocity
2.default = 0.8
3.name = ~<tabpage>/max_run_vx
3.type = float32
3.desc = Maximum x velocity
3.default = 1.0
4.name = ~<tabpage>/max_run_vy
4.type = float32
4.desc = Maximum y velocity
4.default = 1.0
5.name = ~<tabpage>/max_run_vw
5.type = float32
5.desc = Maximum rotational velocity
5.default = 1.0
6.name = ~<tabpage>/max_freq
6.type = float32
6.desc = Minimum publish frequency on `cmd_vel`
6.default = 10.0}
```


