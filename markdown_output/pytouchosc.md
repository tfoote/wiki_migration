## Overview

[pytouchosc](pytouchosc) is a package for manipulating and loading
\`.touchosc\` files. It features a Python library for parsing layout
files that are created by the TouchOSC Editor. It also has a
command-line script for displaying details of layout files, as well as a
script and node for loading layout files to a compatible device.

For more information on TouchOSC and layouts, check out the
[touchosc_bridge](touchosc_bridge) package documentation.

## Node

There are two ways of creating a layoutserver_node, either with a single
file, or a path and a list of files. For more information on loading
layout files to devices, check out the
[TouchOSC Basics Tutorial](rososc_tutorials/Tutorials/TouchOSC Basics).
```clearsilver
name = layoutserver_node
desc = ROS wrapper to the pytouchosc layout server
param {
0.name = ~name
0.type = string
0.desc = Name that TouchOSC clients will see in the "Add Layout" screen
0.default = OSC Server
1.name = ~port
1.type = int
1.desc = Port that layout files will be hosted on, useful for creating more than one layout server on the same computer
1.default = 9658
2.name = ~layout_path or layout_path
2.type = string
2.desc = A path to a group of layout files to create TouchOSC layout servers for.
2.default = None
3.name = ~layouts or layouts
3.type = list
3.desc = A list of layout files to create TouchOSC layout servers for.
3.default = None
4.name = ~layout_file or layout_file
4.type = path
4.desc = Path (including filename) of a layout to create a TouchOSC layout server for.
4.default = None
}
```

### Example Launch File for Single Layout Server

This will create a single layout server on port 9658.
```
<launch>
    <param name="layout_file" 
           value="$(find rososc_tutorials)/layouts/ROS-Demo-iPad.touchosc "/>
    <node pkg="pytouchosc" type="layoutserver_node" name="layoutserver"/>
</launch>
```

### Example Launch File for Multiple Layouts

This will create a layout server hosting
\`rososc_tutorials/layouts/ROS-Demo-iPad.touchosc\` on port 9658, and a
second layout server hosting
\`rososc_tutorials/layouts/ROS-Demo-iPhone.touchosc\` on port 9659.

In this case, two \"Found Hosts\" will appear in the \"Add Layout\"
screen of TouchOSC, with the name of their respective layouts as a
listing. ```
<launch>
    <param name="layout_path" value="$(find rososc_tutorials)/layouts"/>
    <rosparam param="layouts">
        [ "ROS-Demo-iPad.touchosc", "ROS-Demo-iPod.touchosc" ]
    </rosparam> 
    <node pkg="pytouchosc" type="layoutserver_node" name="layoutserver"/>
</launch>
```

## Helper Scripts

In addition to the layout server node, and the Python pytouchosc module,
there are a few scripts to help interact with TouchOSC layouts.

### layoutserver.py

A command line (ROS not needed) utility to spawn a layout server.

Example: ```
rosrun pytouchosc layoutserver.py ~/teleop.touchosc
```

Available command line options: ```
Usage: layoutserver.py [options] /path/to/layout.touchosc

Options:
  -h, --help            show this help message and exit
  -p PORT, --port=PORT  Port that the layout server will host on.
  -n NAME, --name=NAME  Name that will appear in TouchOSC's Server List
  --log=LOGGING         Set logging level
```

### inspectLayout

A command line utility for inspecting the tabpages and controls in a
given layout file.

Example: ```
rosrun pytouchosc inspectLayout -tc slider-ipad.touchosc 
************************************************************
Layout Filename               slider-ipad.touchosc          
Layout Location                                             
************************************************************
Version                       11                            
Orientation                   vertical                      
Mode (Device)                 1-iPad                        
************************************************************
Number of Tabpages            1                             
     1                             
/1/multifader                 MultiDial
```

Usage: ```
rosrun pytouchosc inspectLayout --help
Usage: inspectLayout [options]

Options:
  -h, --help  show this help message and exit
  -t          List tabpages in this layout
  -c          List controls addresses and types in this layout
```

## Code API

If you wish to utilize the pytouchosc module in your own package or
stack, it is suggested that you read over the
[API Docs](http://www.ros.org/doc/api/pytouchosc/html/).

The major components of the API are:

### pytouchosc.bonjour

Wrapper to [pybonjour](http://code.google.com/p/pybonjour/) to provide
Zero Configuration hostname browsing and resolution for clients. This is
the protocol used by TouchOSC to identify layout servers and osc servers
in the local network.

### pytouchosc.layout

Class for creating and loading existing layouts.

### pytouchosc.layoutserver

Script (and class) for creating a layout server for TouchOSC devices in
a local network.

### pytouchosc.tabpage

Class for interacting whith TouchOSC tabpages.

### pytouchosc.controls

Listing of all of the available TouchOSC controls. Also responsible for
creating the message dictionaries used to interact with the default
tabpage handler in the [touchosc_bridge](touchosc_bridge) package.

For detailed information on all of the controls, consult the
[TouchOSC Controls Reference](touchosc_bridge/Controls).
