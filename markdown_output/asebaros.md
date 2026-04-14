## Introduction

### Aseba

[Aseba](http://aseba.wikidot.com) is an event-based architecture for
distributed control of mobile robots. It targets integrated
multi-processors robots or groups of single-microcontroller units, real
or simulated. The core of Aseba is a lightweight virtual machine tiny
enough to run even on microcontrollers. With Aseba, we program the robot
low-level software in a user-friendly scripting language using a cosy
integrated development environment.

You can learn more about Aseba in the following papers:

-   For multi-microcontrollers robots
    [IEEE Tr. Mech. 2010 paper](http://infoscience.epfl.ch/record/144059/files/aseba-ieee-tr.pdf?version=2)
-   For collective robotics
    [SIMPAR 2008 paper](http://infoscience.epfl.ch/getfile.py?recid=129025&mode=best)
-   In educational robots
    [FNG 2008 paper](http://infoscience.epfl.ch/getfile.py?recid=128742&mode=best)
    You can also access documentation at
    [aseba\'s homepage](http://aseba.wikidot.com).

### asebaros

asebaros is a bridge between Aseba and ROS. It allows to load Aseba
scripts, inspect the network structure, read and write variables, and
send and receive events from ROS. It maps the Aseba named events to ROS
topics in a dynamic way, when loading source code.

## Installation

The following commands will fetch and compile the \`asebaros\` package.
The latter will fetch all required dependencies automatically.
```
# Fetch ethzasl_aseba stack
git clone --recursive git://github.com/ethz-asl/ros-aseba.git ethzasl_aseba

# Update ROS_PACKAGE_PATH (if necessary)
export ROS_PACKAGE_PATH=$ROS_PACKAGE_PATH:`pwd`/ethzasl_aseba

# Install dependencies
rosdep install asebaros

# Build
rosmake
```

## Usage

### Node: asebaros

The bridge with Aseba is called \`asebaros\`:

```
asebaros [options] [additional targets]
Options:
  -l, --loop   : makes the switch transmit messages back
                 to the sender, not only forward them
  -p port      : listens to incoming connections on
                 this port
  -h, --help   : shows this help
  ROS_OPTIONS  : see ROS documentation
Additional targets are any valid Dashel targets.
```

When started with no option, asebaros will listen to incoming Aseba
connections and respond to ROS requests. You can specify additional
Aseba targets that asebaros will try to connect on startup. Aseba
targets follow the
[Dashel target naming scheme](http://download.gna.org/dashel/1.0.3/doc/index.html).
For example, to connect Aseba to a serial port on a UNIX, setting
hardware flow control and a speed of 921.6&nbsp;kbps, write:
```
asebaros "ser:device=/dev/ttyUSB0;fc=hard;baud=921600"
```

```clearsilver
srv {
  0.name = load_script
  0.type = asebaros/LoadScripts
  0.desc = Loads an Aseba script from an `.aesl` file. It creates the topics corresponding to the named events in the script, under the namespaces `~/events/NAME` where `NAME` is the name of each topic.
  1.name = get_node_list
  1.type = asebaros/GetNodeList
  1.desc = Get the names of the nodes.
  2.name = get_node_id
  2.type = asebaros/GetNodeId
  2.desc = Get the identifier of a node given by its name.
  3.name = get_node_name
  3.type = asebaros/GetNodeName
  3.desc = Get the name of a node given by its identifier.
  4.name = get_variable_list
  4.type = asebaros/GetVariableList
  4.desc = Get the names of the variables of a given node.
  5.name = set_variable
  5.type = asebaros/SetVariable
  5.desc = Set the value of a variable of a given node.
  6.name = get_variable
  6.type = asebaros/GetVariable
  6.desc = Get the value of a variable of a given node.
  7.name = get_event_id
  7.type = asebaros/GetEventId
  7.desc = Get the identifier of an event given by its name.
  8.name = get_event_name
  8.type = asebaros/GetEventName
  8.desc = Get the name of an event given by its identifier.
}
sub {
  0.name = ~/anonymous_events
  0.type = asebaros/AsebaAnonymousEvent
  0.desc = Topic on which events without a name are received and forwarded to Aseba. When sending Aseba events through ROS, use a source value of `0`.
  1.name = ~/events/NAME
  1.type = asebaros/AsebaEvent
  1.desc = Topic on which events named `NAME` are received and forwarded to Aseba. When sending Aseba events through ROS, use a source value of `0`.
}
pub {
  0.name = ~/anonymous_events
  0.type = asebaros/AsebaAnonymousEvent
  0.desc = Topic on which Aseba events without a name are published. 
  1.name = ~/events/NAME
  1.type = asebaros/AsebaEvent
  1.desc = Topic on which Aseba events named `NAME` are published.
}
```

### Developing for Aseba

Once the \`ethzasl_asebaros\` stack is compiled, you will find
\`aseba/build/studio/asebastudio\` in this stack. \`asebastudio\` is the
Integrated Development Environment that you will use to write programs
for Aseba nodes. Inside studio, you can find help on the Aseba language
from \`Help -\> Language\` and on \`asebastudio\` itself from \`Help -\>
Studio\`.
