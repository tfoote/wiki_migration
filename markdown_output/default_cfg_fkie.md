[Default Configuration Manual on GitHub](http://fkie.github.io/multimaster_fkie/default_cfg.html)

## Overview

The `default_cfg` node offers a list of nodes, which can be started by
calling a service with name of the node. Thus the needed nodes can be
launched on demand without knowing the details of the configuration to
run those. To configure the list with nodes a ROS launch file is used.

## Additional node description

While loading a launch file by the `default_cfg` some addtional
parameters are parsed to obtain a description of robots, nodes and
capabilities configured by the launch file. This description is used in
[Node manager](http://www.ros.org/wiki/node_manager_fkie#capabilities)
to show additional information for nodes. The
[detailed description](http://www.ros.org/wiki/node_manager_fkie#capabilities)
shows the usage of additional description.

## Usage

### Getting started

Although the node is written in Python we need to generate message and
service types:

{ }}}} { }}}}

Run the node:



```
rosrun default_cfg_fkie default_cfg _package:=@PACKAGE_NAME@ _launch_file:=@FILE_NAME@
```



You can run the node without parameter and use the `load` service to
load a launch configuration.

### Interface

{ }}}}

{ }}}}



```clearsilver
param {
0.name = ~package
0.type = String
0.desc = The package name containing the launch file.
0.default = `''`

1.name = ~launch_file
1.type = String
1.desc = The launch file to load.
1.default = `''`

2.name = ~argv
2.type = list
2.desc = A list with command-line arguments required to load a launch file. See [[http://ros.org/doc/electric/api/roslaunch/html/|XmlLoader.load() (roslaunch API)]]
2.default = `[str]`
}
```


