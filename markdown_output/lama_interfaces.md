`lama_interfaces` provides the interfaces to the database as ROS
services for the Large Maps Framework ([LaMa](Large Maps Framework)).

## Overview

`lama_interfaces` provides the interfaces to the database as ROS
services.

The data storage is realized through a database. All databases supported
by Python sqlalchemy can be used. The default database is an SQLite
database which will be save as `/.ros/lama.sqlite`. The environment is
represented as a directed graph, where vertices are points of interest
such as crossings. Descriptors can be associated to vertices and edges,
they give some information about the environment, so that jockeys can
localize or drive the robot. Any ROS message can be saved as descriptor
after a trivial implementation of two services (srv files), one to write
the descriptor into the database and one to retrieve it. Other variable
types can use the [blob/Blob](blob) message type. Descriptor storage
occurs either in binary or clear-text mode.

## Usage

The first node that should be used when working with the !LaMa Framework
is `map_node`: 

```
rosrun lama_interfaces map_node
```

 This node will run several
services: `/lama_map_agent`, `/interface_factory`,
`/lama_object_getter`, and `/lama_object_setter`, which are
described in further sections.

### LaMa Map Agent

This service of type <<SrvLink(lama_interfaces/ActOnMap)>> is used
for all actions over vertices and edges in the map.

### Interface Factory

This service of type <<SrvLink(lama_interfaces/AddInterface)>> is
used to generate two services for each descriptor type, one to write the
descriptor into the database and one to retrieve it. Descriptor storage
occurs either in binary or clear-text mode (specified through the
`interface_type` service attribute. The name of these two services
will be the name of the interface (`interface_name` attribute) to
which "`_getter`" or "`_setter`" are added.

For example, to create a clear-text interface for `float64` in C++:


```cplusplus
ros::NodeHandle nh;
ros::ServiceClient client = nh.serviceClient<lama_interfaces::AddInterface>("interface_factory");
client.waitForExistence();
lama_interfaces::AddInterface srv;
srv.request.interface_name = "my_interface";
srv.request.interface_type = lama_interfaces::AddInterfaceRequest::CLEARTEXT;
srv.request.get_service_message = "lama_interfaces/GetDouble";
srv.request.set_service_message = "lama_interfaces/SetDouble";
if (!client.call(srv))
{
  ROS_ERROR("Failed to create the Lama interface %s", srv.request.interface_name.c_str());
  return false;
}
```



To add a database interface in Python, one can either use the
`/interface_factory` service or call the equivalent Python function.
For example, for a "`sensor_msgs/LaserScan\[\]`" descriptor with
binary storage: 

```python
from lama_interfaces.interface_factory import interface_factory
interface_name = 'my_laser_descriptor'
getter_service = 'lama_interfaces/GetVectorLaserScan'
setter_service = 'lama_interfaces/SetVectorLaserScan'

# The node must be running before calling interface_factory
iface = interface_factory(interface_name,
                          getter_service,
                          setter_service,
                          start=True)

# iface contains the service proxies for getter and setter services,
# if start=True is given.
get_srv = iface.getter_service_proxy
set_srv = iface.setter_service_proxy
```



### Direct vertex/edge access

The services `/lama_object_getter` and `/lama_object_setter` provide
direct access to the graph vertices or edges. These functionalities are
provided by the `/lama_map_agent`, which should be preferred.
