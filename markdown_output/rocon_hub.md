## Overview

Backed by a redis key-value store, a rocon hub provides a centralised
place to store relevant information for multiple ros systems interacting
over a LAN. It's most common use is to act as a kind of name server
assisting ros subsystems to find each other
([gateway model](rocon_gateway)).

### Gateway Hubs

The gateway model uses the hub to databases gateway, connection and
network status information for each gateway. It also provides redis
communication channels for multimaster interactions between the gateways
themselves.

## Starting a Hub

The hub (and redis server) is not terribly fussy and can be launched in
various ways. It can be started without a ros master, a standalone ros
master, or alongside one of the ros masters (robots) that will be part
of the multimaster system.

It can also be started with or without zeroconf. Starting without simply
requires the zeroconf parameter to be set to false. There are two
default launchers in [rocon_hub](rocon_hub) that can be used to fire up
'default' hub configurations:



```
> roslaunch rocon_hub hub.launch
# OR
> roslaunch rocon_hub hub_no_zeroconf.launch
```



Currently, there is only [avahi](zeroconf_avahi) support for zeroconf on
linux.

## Configuration



```clearsilver
node.0 {
  name = rocon_gateway_hub/hub.py
  desc = Node to run, manage the centralised redis server for multimaster gateways.
  param {
    0.name = name
    0.type = string
    0.default = Rocon Hub
    0.desc = Identifier used for selective gateway-hub connections.
    1.name = port
    1.type = int
    1.default = 6380
    1.desc = Port on which to run the redis server.
    2.name = max_memory
    2.type = string
    2.default = 10mb
    2.desc = Max. amount of memory to allocate to the redis server.
    3.name = zeroconf
    3.type = bool
    3.default = true
    3.desc = Whether to publish the redis server uri on zeroconf or not.
  }
}
```



Of these, the `name` and the `zeroconf` flag are the most oft used.
The name can be used to enable gateways to selectively filter which
gateway they want to connect to via their own `hub_whitelist` and
`hub_blacklist` parameters. The zeroconf flag will depend on whether
you have a local zeroconf implementation. Currently only
[avahi](zeroconf_avahi) on linux is supported.

## Examples

Examples of how to launch a hub and use it with the gateway system can
be found in the [tutorials](rocon_hub/Tutorials).
