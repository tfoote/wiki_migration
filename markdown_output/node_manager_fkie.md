[Node Manager Manual on GitHub](http://fkie.github.io/multimaster_fkie/node_manager.html)

[cheatsheet (with thanks to Lorenz Halt!)](http://www.ros.org/wiki/multimaster_fkie?action=AttachFile&do=get&target=nm_cheatsheet.pdf)

## Overview

This package offers a graphical user interface (GUI) to manage ROS
nodes, topics, services, parameters, and launch files in a ROS network.
Combined with other tools of the
[multimaster_fkie stack](http://www.ros.org/wiki/multimaster_fkie) it is
possible to operate a network with multiple masters.

![](attachment:node_manager_overview.png)

{

It is possible to add a node to multiple groups using a prefix for
\`capability_group\`, e.g.:

```
<node name="node_manager" pkg="node_manager_fkie" type="nm" >
    <param name="capability_group" value="Management"/>
    <param name="1.capability_group" value="Node Manager"/>
  </node>
```

The description of a capability group is stored in a global
\`capabilities\` parameter. This parameter is defined as
[rosparam](http://www.ros.org/wiki/roslaunch/XML/rosparam) and contains
the list with all groups and their description. To describe a group adds
a list with \`group name\`, \`group type\`, \`image\` and
\`description\`. \`image\` is a relative path to \`node_manager_fkie\`
package. The \`description\` can be coded as
[reStructeredText](http://docutils.sourceforge.net/docs/ref/rst/restructuredtext.html)
and contains also image references relative to \`node_manager_fkie\`
package path. Since after loading the XML the new line separators are
removed, you must enter \`\\n\` to insert a new line.

```
<rosparam param="capabilities">
      [
        ["Management",
         "core",
         "images/crystal_clear_app_network2.png",
         "The ``management`` group provides nodes needed to detect and synchronize
          other robots in the ROS network. These are:\n\n- Node Manager\n- Master
          Discovery\n- Master Synchronization"
        ]
      ]

    </rosparam>
```

The capability group do not change the \`namespace\` of the included ROS
nodes.

![](attachment:capability_nodes.png)

Further parameter \`robots\` describes in same manner the roboter. The
list must contains \`host name\`, \`robot type\`, \`displayed name\`,
\`image\` and \`description\`:

```
<rosparam param="robots">
    [
      ["tiderko",
       "Workstation",
       "tiderko",
       "images/veryicon_devcom_workstation.png",
       "Workstation\n\n|ws|\n\n.. |ws| image::
        images/veryicon_devcom_workstation.png\n"
      ]
    ]
  </rosparam>
```

This description will also shown in
[Description Dock](#description dock) and tooltip.

### Default Configuration

The default configuration of a robot is represented by
[default_cfg node](http://www.ros.org/wiki/default_cfg_fkie). This node
loads a launch file and offers services to run contained nodes. It also
offers the additional capabilities description extraceted from the
launch file. If a new host is discovered or the ROS Master state is
changed, the \`Node Manager\` searches for node, which offers default
configuration by parsing the service names for \`list_nodes\`. The nodes
provided by \`default_cfg\` are added to the [Nodes View](#nodes view)
with ![](attachment:default_cfg.png) icon in the \`Cfgs\` column. This
nodes can be launched without loading a configuration.

Furthermore based on detected capabilities the
[ Capability View](#Capability View) will be created.

/!\\ The nodes with remote machine tag are ignored.

### Capability View

The \`Capability View\` shows tabularly the detected robots and their
capabilities. The view is created based on the running default
configurations of corresponding robots. Each available capability
provides buttons to start or stop these.

![](attachment:capability_view.png)

Click on the header to show the description in
[Description Dock](#description dock).

## Getting started

Although the node is written in Python we need to run \`rosmake\` to
generate message and service types:

```
rosmake master_discovery_fkie default_cfg_fkie
```

Run the node:

```
rosrun node_manager_fkie nm
```

## Interface

The services of
[master_discovery_fkie](http://www.ros.org/wiki/master_discovery_fkie)
and [default_cfg_fkie](http://www.ros.org/wiki/default_cfg_fkie) are
detected automatically by whose names.

```clearsilver
sub {
0.name = changes
0.type = master_discovery_fkie/MasterState
0.desc = Subscribes to this topic to get the changes in the ROS network. /!\ The name of the topic will be detect automatically by type. All found fopics are subscribed.

1.name = linkstats
1.type = master_discovery_fkie/LinkStatesStamped
1.desc = Subscribes this topic to get the link quality informations to other ROS master. /!\ The name of the topic will be detect automatically by type. All found fopics are subscribed.

}
```

## Key Bindings

  -- ------------------------- -- ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- --
     **Ctrl**+**R**               Opens a dialog to launch a [master_discovery](http://www.ros.org/wiki/master_discovery_fkie) node on entered host.                                                                                                                 
                                                                                                                                                                                                                                                                     
     **Ctrl**+**E**, **F4**       Opens an \`XML Editor\` for selected launch file.                                                                                                                                                                                  
     **Ctrl**+**L**               Loads the selected launch file into selected host.                                                                                                                                                                                 
     **Ctrl**+**O**               Runs on selected host [default_cfg node](http://www.ros.org/wiki/default_cfg_fkie) with selected launch file as parameter.                                                                                                         
     **Ctrl**+**S**               Runs a synchronization dialog.                                                                                                                                                                                                     
                                                                                                                                                                                                                                                                     
     **Alt**+**N**                Opens a dialog to run a ROS node without a configuration. This node will be launched in a \`SCREEN\`.                                                                                                                              
     **Alt**+**K**                Runs the \`rxconsole\` connected to the ROS master of selected host.                                                                                                                                                               
     **Alt**+**G**                Runs the \`rxgraph\` connected to the ROS master of selected host.                                                                                                                                                                 
                                                                                                                                                                                                                                                                     
     **Alt**+**R**                Runs selected nodes. Ignores already running nodes.                                                                                                                                                                                
     **Alt**+**S**                Stops selected nodes. If more then one node is selected, nodes ending with \`rosout\`, \`node_manager\`, \`master_discovery\`, \`master_sync\` or \`default_cfg\` are ignored.                                                     
     **Ctrl**+**Backspace**       Sends a \`SIGKILL\` to selected nodes. If more then one node is selected, nodes ending with \`rosout\`, \`node_manager\`, \`master_discovery\`, \`master_sync\` and \`default_cfg\` are ignored.                                   
     **Ctrl**+**Delete**          Unregister selected nodes (their topics and services) from ROS master. If more then one node is selected, nodes ending with \`rosout\`, \`node_manager\`, \`master_discovery\`, \`master_sync\` and \`default_cfg\` are ignored.   
     **Shift**+**Backspace**      Sends a \`SIGKILL\` to assigned \`SCREEN\` of selected nodes.                                                                                                                                                                      
     **Shift**+**S**              Shows all available \`SCREEN\'s\` which contains the ROS nodes launched by node manager.                                                                                                                                           
     **Ctrl**+**F4**              Closes the loaded configurations.                                                                                                                                                                                                  
                                                                                                                                                                                                                                                                     
     **Alt**+**E**                Expands all groups in \`Nodes\` tab.                                                                                                                                                                                               
     **Alt**+**C**                Collapses all groups in \`Nodes\` tab.                                                                                                                                                                                             
     **Alt**+**{1..5}**           Selects all nodes of the {first\...fifth} host in \`Nodes\` tab excepting the manage nodes.                                                                                                                                        
                                                                                                                                                                                                                                                                     
     **Delete**                   \[Launch-Dock\] Removes the selected history file from view in the root.                                                                                                                                                           
     **Ctrl**+**X**               Copies the alternative values to clipboard. On Node view this is PID. On Topic and Service view it is the type. On Parameter view it is the parameter value.                                                                       
     **Ctrl**+**7**               Comment/Uncomment selected lines in Launch Editor                                                                                                                                                                                  
  -- ------------------------- -- ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- --

}}}}

{

It is possible to add a node to multiple groups using a prefix for
\`capability_group\`, e.g.:

```
<node name="node_manager" pkg="node_manager_fkie" type="nm" >
    <param name="capability_group" value="Management"/>
    <param name="1.capability_group" value="Node Manager"/>
  </node>
```

The description of a capability group is stored in a global
\`capabilities\` parameter. This parameter is defined as
[rosparam](http://www.ros.org/wiki/roslaunch/XML/rosparam) and contains
the list with all groups and their description. To describe a group adds
a list with \`group name\`, \`group type\`, \`image\` and
\`description\`. \`image\` is a relative path to \`node_manager_fkie\`
package. The \`description\` can be coded as
[reStructeredText](http://docutils.sourceforge.net/docs/ref/rst/restructuredtext.html)
and contains also image references relative to \`node_manager_fkie\`
package path. Since after loading the XML the new line separators are
removed, you must enter \`\\n\` to insert a new line.

```
<rosparam param="capabilities">
      [
        ["Management",
         "core",
         "images/crystal_clear_app_network2.png",
         "The ``management`` group provides nodes needed to detect and synchronize
          other robots in the ROS network. These are:\n\n- Node Manager\n- Master
          Discovery\n- Master Synchronization"
        ]
      ]

    </rosparam>
```

The capability group do not change the \`namespace\` of the included ROS
nodes.

![](attachment:capability_nodes.png)

Further parameter \`robots\` describes in same manner the roboter. The
list must contains \`host name\`, \`robot type\`, \`displayed name\`,
\`image\` and \`description\`:

```
<rosparam param="robots">
    [
      ["tiderko",
       "Workstation",
       "tiderko",
       "images/veryicon_devcom_workstation.png",
       "Workstation\n\n|ws|\n\n.. |ws| image::
        images/veryicon_devcom_workstation.png\n"
      ]
    ]
  </rosparam>
```

This description will also shown in
[Description Dock](#description dock) and tooltip.

### Default Configuration

The default configuration of a robot is represented by
[default_cfg node](http://www.ros.org/wiki/default_cfg_fkie). This node
loads a launch file and offers services to run contained nodes. It also
offers the additional capabilities description extraceted from the
launch file. If a new host is discovered or the ROS Master state is
changed, the \`Node Manager\` searches for node, which offers default
configuration by parsing the service names for \`list_nodes\`. The nodes
provided by \`default_cfg\` are added to the [Nodes View](#nodes view)
with ![](attachment:default_cfg.png) icon in the \`Cfgs\` column. This
nodes can be launched without loading a configuration.

Furthermore based on detected capabilities the
[ Capability View](#Capability View) will be created.

/!\\ The nodes with remote machine tag are ignored.

### Capability View

The \`Capability View\` shows tabularly the detected robots and their
capabilities. The view is created based on the running default
configurations of corresponding robots. Each available capability
provides buttons to start or stop these.

![](attachment:capability_view.png)

Click on the header to show the description in
[Description Dock](#description dock).

## Getting started

Although the node is written in Python we need to run \`rosmake\` to
generate message and service types:

```
rosmake master_discovery_fkie default_cfg_fkie
```

Run the node:

```
<rosparam param="capabilities">
      [
        ["Management",
         "core",
         "images/crystal_clear_app_network2.png",
         "The ``management`` group provides nodes needed to detect and synchronize
          other robots in the ROS network. These are:\n\n- Node Manager\n- Master
          Discovery\n- Master Synchronization"
        ]
      ]

    </rosparam>
```0

## Interface

The services of
[master_discovery_fkie](http://www.ros.org/wiki/master_discovery_fkie)
and [default_cfg_fkie](http://www.ros.org/wiki/default_cfg_fkie) are
detected automatically by whose names.

```
<rosparam param="capabilities">
      [
        ["Management",
         "core",
         "images/crystal_clear_app_network2.png",
         "The ``management`` group provides nodes needed to detect and synchronize
          other robots in the ROS network. These are:\n\n- Node Manager\n- Master
          Discovery\n- Master Synchronization"
        ]
      ]

    </rosparam>
```1

## Key Bindings

  -- ------------------------- -- ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- --
     **F2**                       Renames a selected launch file.                                                                                                                                                                                                    
     **Ctrl**+**R**               Opens a dialog to launch a [master_discovery](http://www.ros.org/wiki/master_discovery_fkie) node on entered host.                                                                                                                 
                                                                                                                                                                                                                                                                     
     **Ctrl**+**E**               Opens an \`XML Editor\` for selected launch file.                                                                                                                                                                                  
     **Ctrl**+**L**               Loads the selected launch file into selected host.                                                                                                                                                                                 
     **Ctrl**+**O**               Runs on selected host [default_cfg node](http://www.ros.org/wiki/default_cfg_fkie) with selected launch file as parameter.                                                                                                         
     **Ctrl**+**S**               Runs a synchronization dialog.                                                                                                                                                                                                     
                                                                                                                                                                                                                                                                     
     **Alt**+**N**                Opens a dialog to run a ROS node without a configuration. This node will be launched in a \`SCREEN\`.                                                                                                                              
     **Alt**+**K**                Runs the \`rxconsole\` connected to the ROS master of selected host.                                                                                                                                                               
     **Alt**+**G**                Runs the \`rxgraph\` connected to the ROS master of selected host.                                                                                                                                                                 
                                                                                                                                                                                                                                                                     
     **Alt**+**R**                Runs selected nodes. Ignores already running nodes.                                                                                                                                                                                
     **Alt**+**S**                Stops selected nodes. If more then one node is selected, nodes ending with \`rosout\`, \`node_manager\`, \`master_discovery\`, \`master_sync\` or \`default_cfg\` are ignored.                                                     
     **Ctrl**+**Backspace**       Sends a \`SIGKILL\` to selected nodes. If more then one node is selected, nodes ending with \`rosout\`, \`node_manager\`, \`master_discovery\`, \`master_sync\` and \`default_cfg\` are ignored.                                   
     **Ctrl**+**Delete**          Unregister selected nodes (their topics and services) from ROS master. If more then one node is selected, nodes ending with \`rosout\`, \`node_manager\`, \`master_discovery\`, \`master_sync\` and \`default_cfg\` are ignored.   
     **Shift**+**Backspace**      Sends a \`SIGKILL\` to assigned \`SCREEN\` of selected nodes.                                                                                                                                                                      
     **Shift**+**S**              Shows all available \`SCREEN\'s\` which contains the ROS nodes launched by node manager.                                                                                                                                           
     **Ctrl**+**F4**              Closes the loaded configurations.                                                                                                                                                                                                  
                                                                                                                                                                                                                                                                     
     **Alt**+**E**                Expands all groups in \`Nodes\` tab.                                                                                                                                                                                               
     **Alt**+**C**                Collapses all groups in \`Nodes\` tab.                                                                                                                                                                                             
     **Alt**+**{1..5}**           Selects all nodes of the {first\...fifth} host in \`Nodes\` tab excepting the manage nodes.                                                                                                                                        
  -- ------------------------- -- ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- --

}}}}

## Getting started

Although the node is written in Python we need to run \`catkin_make\` to
generate message and service types:

```
<rosparam param="capabilities">
      [
        ["Management",
         "core",
         "images/crystal_clear_app_network2.png",
         "The ``management`` group provides nodes needed to detect and synchronize
          other robots in the ROS network. These are:\n\n- Node Manager\n- Master
          Discovery\n- Master Synchronization"
        ]
      ]

    </rosparam>
```2

Run the node:

```
<rosparam param="capabilities">
      [
        ["Management",
         "core",
         "images/crystal_clear_app_network2.png",
         "The ``management`` group provides nodes needed to detect and synchronize
          other robots in the ROS network. These are:\n\n- Node Manager\n- Master
          Discovery\n- Master Synchronization"
        ]
      ]

    </rosparam>
```3 or ```
<rosparam param="capabilities">
      [
        ["Management",
         "core",
         "images/crystal_clear_app_network2.png",
         "The ``management`` group provides nodes needed to detect and synchronize
          other robots in the ROS network. These are:\n\n- Node Manager\n- Master
          Discovery\n- Master Synchronization"
        ]
      ]

    </rosparam>
```4

## Interface

The services of
[master_discovery_fkie](http://www.ros.org/wiki/master_discovery_fkie)
and [default_cfg_fkie](http://www.ros.org/wiki/default_cfg_fkie) are
detected automatically by whose names.

```
<rosparam param="capabilities">
      [
        ["Management",
         "core",
         "images/crystal_clear_app_network2.png",
         "The ``management`` group provides nodes needed to detect and synchronize
          other robots in the ROS network. These are:\n\n- Node Manager\n- Master
          Discovery\n- Master Synchronization"
        ]
      ]

    </rosparam>
```5

## Troubleshooting

1\. Error while launch a node on remote host: *bash: rosrun: command not
found* To run a node on remote host, an SSH connection will be
established without setting any enviroment variables. Try to comment out
in .bashrc: ```
<rosparam param="capabilities">
      [
        ["Management",
         "core",
         "images/crystal_clear_app_network2.png",
         "The ``management`` group provides nodes needed to detect and synchronize
          other robots in the ROS network. These are:\n\n- Node Manager\n- Master
          Discovery\n- Master Synchronization"
        ]
      ]

    </rosparam>
```6

2\. The \`Node Manager\` crashes on load a launch file with error:
*QSpiAccessible::accessibleEvent not handled: \"8008\"* This \"bug\"
seems to be resolved by removing the *qt-at-spi* package.

3\. You don\'t see the correct output of your nodes. Try to change your
default terminal: ```
<rosparam param="capabilities">
      [
        ["Management",
         "core",
         "images/crystal_clear_app_network2.png",
         "The ``management`` group provides nodes needed to detect and synchronize
          other robots in the ROS network. These are:\n\n- Node Manager\n- Master
          Discovery\n- Master Synchronization"
        ]
      ]

    </rosparam>
```7
