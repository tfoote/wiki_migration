## Overview

This package provides implementations for [zeroconf](zeroconf) on top of
linux\'s \'\'avahi-daemon\'\'. There are two implementations:

-   C++ library.
-   Ros node.

The c++ library can be manipulated directly through the
[Zeroconf](http://www.ros.org/doc/api/zeroconf_avahi/html/classzeroconf__avahi_1_1Zeroconf.html)
class whereas the
[ros node](http://www.ros.org/doc/api/zeroconf_avahi/html/node_2zeroconf_8cpp_source.html)
provides similar handles through ros topics, services and parameters
exposed by the.

## How it Works

Both the c++ and node implementations operate on two entities,
\'\'Listeners\'\' and \'\'Services\'\'.

\'\'\'Listeners\'\'\' are used to discover the appearance and
disappearance of all services belong to a specific service type (e.g.
\_ros-master.\_tcp). The usual process is to add a listener and then sit
back and wait for the callbacks (either c++ or ros subscription) to
arrive signifying addition or removal of the specified services.

\'\'\'Services\'\'\' are zeroconf services you wish to publish on the
network. They require a name, service type, port and description. If
there is a name collision, this package and avahi will rename the
service so that it is unique for the lifetime of the current connection.

## Usage

If you\'re using the library, it should be relatively straightforward -
simply follow the
[Zeroconf](http://www.ros.org/doc/api/zeroconf_avahi/html/classzeroconf__avahi_1_1Zeroconf.html)
class documentation. There is also an example in
[zeroconf_avahi_demos](zeroconf_avahi_demos).

Alternatively, using the ros node can be done in a variety of ways,
refer to the [Tutorials](zeroconf_avahi/Tutorials).

## Ros API

```clearsilver
name = Zeroconf Node
desc = Provides a ros api for listening and publishing of services.
srv {
  0.name = add_listener
  0.type = zeroconf_comms/AddListener
  0.desc = will add a listener for services of the specified type
}
srv {
  1.name = add_service
  1.type = zeroconf_comms/AddService
  1.desc = publishes the specified zeroconf service on the network
}
srv {
  2.name = remove_service
  2.type = zeroconf_comms/RemoveService
  2.desc = removes the specified zeroconf service on the network
}
srv {
  3.name = list_discovered_services
  3.type = zeroconf_comms/ListDiscoveredServices
  3.desc = lists the currently found services of the specified type
}
srv {
  4.name = list_published_services
  4.type = zeroconf_comms/ListPublishedServices
  4.desc = lists all zeroconf services published by this node
}
pub {
  5.name = new_connections
  5.type = zeroconf_comms/DiscoveredService
  5.desc = streams all new zeroconf services as discovered by the listeners
}
pub {
  6.name = lost_connections
  6.type = zeroconf_comms/DiscoveredService
  6.desc = streams all removed zeroconf services as discovered by the listeners
}
param {
  7.name = ~listeners
  7.type = array[string]
  7.desc = array of strings specifying service types, on startup the node will add listeners for each of these types
  7.default = []
}
param {
  7.name = ~services
  7.type = array[structs]
  7.desc = array of structs specifying services to publish (see example code)
  7.default = []
}
```

See the example on static configuration for an illustration of the usage
of the \'\'listeners\'\' and \'\'services\'\' parameters:
