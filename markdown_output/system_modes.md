# system_modes

`system_modes` is a small ROS 2 C++ package that assumes that the ROS
2 system is built from components with a lifecycle
([managed nodes](http://design.ros2.org/articles/node_lifecycle.html)).
It adds a notion of (sub-)systems, hierarchically grouping these nodes,
as well as a notion of modes that determine the configuration of these
nodes and (sub-)systems in terms of their parameter values.

## System Modes Library and Nodes

The
[system modes package](https://github.com/microROS/system_modes/tree/master/system_modes)
consists of a library that parses a *system modes and hierarchy model*
file (SHM file, yaml format). The modes specified in the SMH file extend
the
[default ROS 2 lifecycle](http://design.ros2.org/articles/node_lifecycle.html):

![\|width=760](attachment:lifecycle-extended.png)

The library is able to infer the modes of a system based in the known
states and modes of its nodes, which we call *mode inference*. Relying
on this library are a mode manager node that is able to manage lifecycle
states and modes of all nodes as well as a command-line mode monitor for
introspection.

For more information on the model, the library, the mode manager and the
mode monitor, see
<https://github.com/microROS/system_modes/tree/master/system_modes>

## Example

The
[system modes examples package](https://github.com/microROS/system_modes/tree/master/system_modes_examples)
contains a small example *actuation* sub-system containing two example
nodes, a *drive_base* node and a *manipulator* node. The example system
allow state and mode changes of the system as well as the nodes and
allows introspection of modes with the mode monitor:

![\|width=760](attachment:screenshot-monitor-performance.png)

For an example system and a step-by-step example, see
<https://github.com/microROS/system_modes/tree/master/system_modes_examples>
