## Overview

This packages contains the ROS interface for
[socketcan_interface](socketcan_interface) and
[canopen_master](canopen_master). It can be used as a stand-alone ROS
node, but as well as a base class for profile specific ROS interfaces,
e.g. [canopen_motor_node](canopen_motor_node).

It manages a CANopen bus with one or more nodes, which are configures
with CANopen EDS/DCF files. The ROS node runs a control loop with
CANopen SYNC interval (or with an alternative update interval if the
SYNC protocol is not used).

## Configuration

The configuration can be split into different parts. First the bus has
to be set-up, these settings are shared for all node. Then all must be
configured with their CANopen and ROS interfaces. All parameters must be
loaded into the nodes private namespace

### CANopen Bus layer

The bus settings consists of a CAN interface
([socketcan_interface](socketcan_interface)) and the shared bus settings
for [canopen_master](canopen_master).



```highlight
bus:
  device: can0 # socketcan network
  # loopback: false # socket should loop back messages
  # driver_plugin: can::SocketCANInterface
  # master_allocator: canopen::SimpleMaster::Allocator
sync:
  interval_ms: 10 # set to 0 to disable sync
  # update_ms: <interval_ms> #update interval of control loop, must be set explecitly if sync is disabled
  overflow: 0 # overflow sync counter at value or do not set it (0, default)
heartbeat: # simple heartbeat producer, optional!
  rate: 20 # heartbeat rate
  msg: "77f#05" # message to send, cansend format: heartbeat of node 127 with status 5=Started
```



### Node layer

All nodes are listed in the nodes parameter, either as list or a struct,
and require a node ID, a name and the path to the EDS/DCF file.



```highlight
# struct syntax
nodes:
  node1:
    id: 1
    eds_pkg: my_config_package # optionals package  name for relative path
    eds_file: "my_config.dcf" # path to EDS/DCF file
  node2:
    id: 85
    name: other_mode # optional name
    eds_file: "/path/to/my_config.eds" # absolute name
```

 

```highlight
# list syntax
nodes:
  - name: node1
    id: 1
    eds_pkg: my_config_package # optionals package  name for relative path
    eds_file: "my_config.eds" # path to EDS/DCF file
  - name: node2
    id: 85
    eds_file: "/path/to/my_config.dcf" # absolute name
```

 Additional parameters
can set either for each node or in a defaults section:



```highlight
defaults: # optional, all defaults can be overwritten per node
  eds_pkg: my_config_package # optional package  name for relative path
  eds_file: "my_config.dcf" # path to EDS/DCF file
  dcf_overlay: # "ObjectID": "ParameterValue" (both as strings)
    "1016sub1" : "0x7F0064" # heartbeat timeout of 100 ms for master at 127
    "1017": "100" # heartbeat producer
```

 The dcf_overlay can be used to overwrite
specific settings in the EDS/DCF.

### ROS layer

Each node (or in the defaults) can be passed a publish parameter with a
list of object names. The topic types correspond to the object types,
e.g. UNSIGNED16 to <<MsgLink(std_msgs/UInt16)>>. It is meant for
debugging or for simple CANopen interfaces, since it blocks the control
loop. Each entry can have an exclamation mark appended that forces the
driver to reread the object form the node in each step.

For example: 

```highlight
defaults: # optional, all defaults can be overwritten per node
  publish: ["1001"] # list of objects to be published (one topic per node)
nodes:
  node1:
    # ...
    publish: ["1003sub0!"] # list of objects to be published (one topic per node)
  node2:
    # ...
  node3:
    # ...
```

 will publish on three topics with
the sync/update_rate:

-   node1_1003sub0 (<<MsgLink(std_msgs/UInt8)>>): number of errors
    for node1 (not cached)
-   node2_1001 (<<MsgLink(std_msgs/UInt8)>>): error register of
    node2 (cached)
-   node3_1001 (<<MsgLink(std_msgs/UInt8)>>): error register of
    node3 (cached)

The [diagnostic_updater](diagnostic_updater) can be passed the
diagnostic_period parameter in fractional seconds.

## ROS API



```clearsilver
name = canopen_chain_node
pub {
  0.name = /diagnostics
  0.type = diagnostic_msgs/DiagnosticStatus
  0.desc = diagnostic information for the chain and each individual node
}
srv {
  0.name = driver/init
  0.type = std_svrs/Trigger
  0.desc = initialize the driver
  1.name = driver/halt
  1.type = std_svrs/Trigger
  1.desc = halt movements
  2.name = driver/recover
  2.type = std_svrs/Trigger
  2.desc = recover from emergency stops etc.
  3.name = driver/shutdown
  3.type = std_svrs/Trigger
  3.desc = shutdown all driver connections
  4.name = driver/get_object
  4.type = canopen_chain_node/GetObject
  4.desc = read CANOpen object. Specify the node using the joint name. If cached=False an SDO is sent to retrieve the current value, otherwise returns the last value received.
  5.name = driver/set_object
  5.type = canopen_chain_node/SetObject
  5.desc = write CANOpen register value.
}
param {
  0.name = ~diagnostic_period
  0.type = double
  0.desc = period for diagnostics updater
  0.default = 1.0
  1.name = ~bus
  1.type = struct
  1.desc = bus settings
  2.name = ~sync
  2.type = struct
  2.desc = SYNC interval settings
  3.name = ~heartbeat
  3.type = struct
  3.desc = heartbeat settings
  4.name = ~defaults
  4.type = struct
  4.desc = default settings for all nodes
  5.name = ~nodes
  5.type = struct/list
  5.desc = settings for the nodes
}
```

 Further topics will be published according to
the publish parameters.

## C++ API

This package provides a `canopen::RosChain` class that implements a
`canopen::LayerStack` interface and takes care of the parameter
parsing and the life-cycle. It can be customized via its virtual
interface, especially with `RosChain::nodeAdded`
