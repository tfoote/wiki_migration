## Documentation

This package provides communication interface between ROS and
[OPC UA](https://opcfoundation.org/about/opc-technologies/opc-ua/)
communication standard using
[python-opcua](https://github.com/FreeOpcUa/python-opcua) library
written in Python. This package currently implements an OPC UA Server
mapping all ROS Topics, Services and Actions under defined namespace in
the OPC UA address space.

### Installing the package

Check the [ros_opcua_communication](ros_opcua_communication) page.

### Starting the Nodes

The easiest way to start the nodes is using launch file:

```
roslaunch ros_opcua_impl_python_opcua rosopcua.launch
```

### Nodes

```clearsilver
name = rosopcua
desc = Implements OPC UA server functionality in ROS by mapping the ros topics, services and actions in he OPC UA address space.
param {
  0.name = namespace
  0.type = String
  0.default = /
  0.desc = Namespace from which all topics, services and actions will be mapped into OPC UA address space.
}
```

## Report a Bug

<<GitHubIssues(iirob/ros_opcua_communication)>>
