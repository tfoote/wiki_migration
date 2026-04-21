## Documentation

This package provides communication interface between ROS and
[OPC UA](https://opcfoundation.org/about/opc-technologies/opc-ua/)
communication standard using
[freeopcua](https://github.com/FreeOpcUa/freeopcua) written in C++. This
package currently implements an OPC UA Client with basic functionality.
For more details see the node description.

### Installing the package

Check the [ros_opcua_communication](ros_opcua_communication) page.

### Starting the nodes

The easiest way to start the nodes is using launch file:



```
roslaunch ros_opcua_impl_freeopcua clinet.launch
```



### Nodes



```clearsilver
name = client_node
desc = Implements OPC UA client functionality in ROS.
srv {
  0.name = connect
  0.type = ros_opcua_srvs/Connect
  0.desc = Connect to the OPC UA server defined in request.
  1.name = disconnects
  1.type = ros_opcua_srvs/Disconnect
  1.desc = Disconnects from the OPC UA server.
  2.name = list_node
  2.type = ros_opcua_srvs/ListNode
  2.desc = List child nodes from the node ID request.
  3.name = call_method
  3.type = ros_opcua_srvs/CallMethod
  3.desc = Call OPC UA method.
  4.name = read
  4.type = ros_opcua_srvs/Read
  4.desc = Read a value from node in OPC UA server.
  5.name = write
  5.type = ros_opcua_srvs/Write
  5.desc = Write a value to the node in OPC UA server.
  6.name = subscribe
  6.type = ros_opcua_srvs/Subscribe
  6.desc = Subscribe to data-change event for the node in OPC UA server. Topic for publishing event will be automatically created.
  7.name = unsubscribe
  7.type = ros_opcua_srvs/Unsubscribe
  7.desc = Unsubscribe from a node in the OPC UA server.
}
```



## Report a Bug
