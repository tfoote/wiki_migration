## The Gateway Model

The gateway model is based on the lan concept where a gateway stands
inbetween your lan and the rest of the internet, controlling both what
communications are allowed through, and what is sent out.

Gateways for ros systems are very similar conceptually. They interpose
themselves between a ros system and other ros systems and are the
co-ordinators of traffic going in and out of a ros system to remote ros
systems.

![Gateway Model\|width=100%](https://docs.google.com/drawings/pub?id=1R7Pu_BZkNU70Jn4l4GpDC95iZevK8sLDJx-UKj3lcw0&w=726&h=477)

Note that the gateways are not a point to point multimaster solution.
They have been designed to be a convenient building block for a variety
of more complete solutions on top. Some ideas for
[use cases](http://www.robotconcert.org/wiki/Concert_Framework/Gateway_Use_Cases).

## Notes

-   [Gateway Model Concept - More Detail](http://www.robotconcert.org/index.php/Concert_Framework/Gateway_Concept)
-   [Differences from MasterSync](http://www.robotconcert.org/index.php/Differences_from_MasterSync)
-   [Troubleshooting](rocon_gateway/Troubleshooting) - some constraints
    to be aware of if building a system on top of the gateways.
-   [First Api Review](rocon_multimaster/Reviews/Gateway_API_Review - Oct 2012)

## Ros API

### Parameters



```clearsilver
param{
  no_header=True
  1{
  name = ~hub_whitelist
  type = list of string
  default = `[]`
  desc = Use this to control which hubs you wish to work with.
  }
  2{
  name = ~hub_blacklist
  type = list of string
  default = `[]`
  desc = Use this to control which hubs you wish to not work with.
  }
  3{
  name = ~watch_loop_period
  type = int
  default = `10`
  desc = How long the watcher should sleep inbetween checking if the system state needs synchronisation (secs).
  }
  4{
  name = ~firewall
  type = bool
  default = `false`
  desc = Used to block/permit remote gateway's from flipping to this gateway.
  }
  5{
  name = ~advertise_all
  type = bool
  default = `false`
  desc = Make everything (except the default_blacklist) publicly available for pulling.
  }
  6{
  name = ~default_blacklist
  type = list of connections (name, node, type)
  default = rocon_gateway/param/default_blacklist.yaml
  desc = Connections that should never get advertised. Usually good to rosparam load this file as the default for your gateway.
  }
  7{
  name = ~default_advertisements
  type = list of connections (name, node, type)
  default = `[]`
  desc = Connections to advertise by default (watched for from startup). Can use python regex patterns to full effect for these. See `rocon_gateway/param/default.yaml` for an example.
  }
  8{
  name = ~default_flips
  type = list of remote_connections (gateway, (name, node, type) )
  default = `[]`
  desc = Connections to flip by default (watched for from startup). Can use python regex patterns to full effect for these. See `rocon_gateway/param/default.yaml` for an example.
  }
  9{
  name = ~default_pulls
  type = list of remote_connections (gateway, (name, node, type) )
  default = `[]`
  desc = Connections to pull by default (watched for from startup). Can use python regex patterns to full effect for these. See `rocon_gateway/param/default.yaml` for an example.
  }
  9{
  name = ~disable_uuids
  type = boolean
  default = `False`
  desc = Manage unique naming of multiple gateways yourself.
  }
}
```



### Services



```clearsilver
srv{
  no_header=True
  1{
  name = ~advertise
  type = gateway_msgs/Advertise
  desc = Advertise a connection to be shared to other ros systems.
  }
  2{
  name = ~advertise_all
  type = gateway_msgs/AdvertiseAll
  desc = Advertise all connections except the a specified blacklist.
  }
  3{
  name = ~connect_hub
  type = gateway_msgs/ConnectHub
  desc = Specify manually the location of the hub to connect to.
  }
  4{
  name = ~flip
  type = gateway_msgs/Remote
  desc = Flip the specified remote rule.
  }
  5{
  name = ~flip_all
  type = gateway_msgs/Remote
  desc = Flip all connections except the specified blacklist.
  }
  6{
  name = ~gateway_info
  type = gateway_msgs/GatewayInfo
  desc = Current status and info about the local gateway.
  }
  7{
  name = ~pull
  type = gateway_msgs/Remote
  desc = Pull rule from the specified remote gateway.
  }
  8{
  name = ~pull_all
  type = gateway_msgs/RemoteAll
  desc = Pull all except a specified blacklist from the remote gateway.
  }
  9{
  name = ~remote_gateway_info
  type = gateway_msgs/RemoteGatewayInfo
  desc = Current status and info about currently connected remote gateways.
  }
```



## Utilities

These scripts are located in either the global bin directory or are
rosrunnable from the rocon_gateway package (prefixing the latter with a
`` to distinguish them)

-   `gateway_info` : pretty prints local gateway info
-   `remote_gateway_info` : pretty prints remote gateway info
-   `flip` : manual command line tool to flip connections (useful for
    debugging)
-   `advertise` : manual command line tool to advertise connections
    (useful for \*
-   `pull` : manual command line tool to pull connections (useful for
    debugging)

## Tutorials

An introduction to the tools and some explanatory examples about the
gateways can be found in the [Tutorials](rocon_gateway/Tutorials).
