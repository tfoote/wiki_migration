## Overview

This package provides the implementation of the
[cob_command_gui](cob_command_gui) as a RViz Plugin for operating
Care-O-bot.

*Note: The cob_command_gui_rviz package is written for ROS Electric
using the wxWidgets library. As of the ROS Fuerte release Rviz is moving
from the wxWidgets library to the Qt library.*

**There is no version for ROS Fuerte available at the moment!**

![\|width=100%](attachment:cob_command_gui_rviz.png)

## Hardware Requirements

To use this package you don't need any hardware, but it is intended to
be used with either a real Care-O-bot or a simulated one (see
[cob_bringup](cob_bringup) or [cob_bringup_sim](cob_bringup_sim)).

## ROS API

The [cob_command_gui_rviz](cob_command_gui_rviz) package provides a
configurable RViz Plugin for operating different hardware parts of
Care-O-bot. The command_gui_rviz uses the functionalities of the
[cob_script_server](cob_script_server) package.

### command_gui_rviz_panel.cpp

`command_gui_rviz_panel.cpp` is configurable by a .yaml file to send
[topics](Topics) and [services](Services). Inside the command_gui_rviz
mainly [actionlib](actionlib) calls are used.

### command_gui_rviz.cpp

`command_gui_rviz.cpp` creates the controls for the plugin, which is
described in the /lib/plugin.yaml file.

### init.cpp

`init.cpp` associates the registered class with the data in the yaml
file and is connected to the running RViz by calls to
!TypeRegistry.registerDisplay() in the plugin's rvizPluginInit()
function:



```cplusplus

#include "rviz/plugin/type_registry.h"
#include "cob_command_gui_rviz/command_gui_rviz.h"

extern "C" void rvizPluginInit(rviz::TypeRegistry* reg)
{
	reg->registerDisplay<rviz::CommandGuiRviz>("CommandGuiRviz");
}
```



see [rviz_PluginAPI](rviz/PluginAPI#Existing_Plugin_API)

### execute_commands.py

The [cob_script_server](cob_script_server) implementation.

## Usage/Examples

### Building and Uploading



```
rosdep install cob_command_gui_rviz
rosmake cob_command_gui_rviz
```

 You can upload the cob_command_gui_rviz plugin
by selecting the **Plugins->Manage\...** menu item in RViz.

A dialog will pop up letting you manage loading/unloading plugins:

![\|width=60%](attachment:manage_plugins.png)

To add the panel, click the **Add** button at the bottom:

![\|width=60%](attachment:new display.png)

For a more detailed introduction see [rviz/UserGuide](rviz/UserGuide).

### Usage

For starting the action server: 

```
roscd cob_rviz_movement_control/src
./execute_commands.py
```



For loading the parameters and starting RViz: 

```
export ROBOT=cob3-3
export ROBOT_ENV=ipa-kitchen
roslaunch cob_command_gui_rviz startup.launch
rosrun rviz rviz
```


The parameters of the command_gui_rviz are defined in
[cob_default_env_config](cob_default_env_config) and
[cob_default_robot_config](cob_default_robot_config) and loaded in the
parameter server.
