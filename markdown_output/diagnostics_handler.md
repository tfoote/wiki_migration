## Package Overview

`diagnostics_handler` is a *tabpage handler* for the
[touchosc_bridge](touchosc_bridge) package. It provides an interface to
the diagnostics and diagnostics_agg topics that many pieces of hardware
utilize. It gives an at-a-glance look at the status of hardware and
software systems on your robot.

This package includes layouts for both iPad and iPhone-sized devices in
the `diagnostics_handler/layouts` directory. When launched, the node
will respond to incoming OSC messages from both sized layouts.

## Video Demo

[Youtube](https://www.youtube.com/watch?v=xgOYBcAzLBM)

## Screenshots

### iPod Sized

![Diagnostics Layout for iPod\|width=350](attachment:diag-ipod.png)

### iPad Sized

![Diagnostics Layout for iPad\|width=600](attachment:diag-ipad.png)

## Features

Some of the main features of the `diagnostics_handler`. These features
may be seen in the above YouTube video.

-   Multiple client support
-   Support for /diagnostics and /diagnostics_agg topics
-   Key/Value portion of message displayable
-   Nested message support with \[diagnostics_aggregator\] properly
    configured
-   System status LED
-   Shows current ROS time (iPad only)

## Configuration

Example launch and configuration files are included for the
`diagnostics_handler` in it's package directory. Also, an example
`diagnostics.yaml` file is included below. This file should be loaded
to the [Parameter Server](Parameter Server) using your configured
`.launch` file.



```
# Handler specific information
diagnostics:
  # Required parameters
  pkg: diagnostics_handler
  class: 'diagnosticstabpage/DiagnosticsTabpageHandler'
 
  start_topic: '/diagnostics'
```



More details on configuring launch files for
[touchosc_bridge](touchosc_bridge) can be found in the
[rososc_tutorials](rososc_tutorials) and in the
[touchosc_bridge](touchosc_bridge) package documentation.


```
<launch>
    <node pkg="touchosc_bridge" type="touchosc_bridge.py" name="touchosc_bridge" output="screen">
        <param name="osc_name" value="ROS Diagnostics"/>
        <param name="port" value="10000" />
        <param name="print_fallback" value="False"/>
        <param name="load_default" value="False"/>
        <rosparam param="handlers">[diagnostics]</rosparam>
        <rosparam command="load" file="$(find diagnostics_handler)/cfg/diagnostics.yaml" />
    </node>
</launch>
```





```clearsilver
name = DiagnosticsTabpageHandler
desc = Tabpage Handler to be used with touchosc_bridge

sub {
0.name = diagnostics
0.type = diagnostic_msgs/DiagnosticArray
0.desc = Raw diagnostics information from the various hardware and software systems on the robot.
1.name = diagnostics_agg
1.type = diagnostic_msgs/DiagnosticArray
1.desc = Aggregated diagnostics information
}
param {
0.name = ~<tabpage>/start_topic
0.type = string
0.desc = '/diagnostics' or '/diagnostics_agg', the topic that the tabpage will initialize to.
0.default = /diagnostics
}
```


