rosproxy was mainly an experiment in having a single [rospy](rospy) node
interface with multiple masters and present dual interfaces. It resulted
in some improvements in the internal design of rospy and provided ideas
for future implementations. There are currently no efforts to continue
this experiment.

## Setting up the proxy

When using `rosproxy`, we refer to the `internal` side of the proxy
to mean the ROS graph that is providing the desired data, e.g. inside
the firewall. The `external` side refers to one or more ROS graphs
that are connecting to the proxy to retrieve this data.

Steps:

1\. Run the `proxy` node. The `proxy` accepts a whitelist of
services and topics that it proxies. You probably want to explicitly set
the TCPROS and XML-RPC ports as well to simplify configuration. 2. *For
each external master*, run the `register.py` script for each service
and topic that you wish to proxy into the external master.

## Scripts

`register.py service /service_name rosrpc:*HOSTNAME:PORT` Register the
service on the current ROS master.*

`register.py pub /topic_name topic/Type
[http://HOSTNAME:PORT](http://HOSTNAME:PORT)` Register the publication
on the current ROS master.

## Nodes



```clearsilver
 name = proxy
 desc = The `proxy` node can proxy service calls and subscriptions, which is useful when traversing firewalls or other configurations where you wish to limit access to another ROS graph. NOTE: the `proxy` only talks to the [[Master|master]] on the ''internal'' side. In order to enable the `proxy` to work with multiple external graphs, the `register.py` script should be used to register it with other masters.

 param{
    0.name = ~pubs
    0.type = [string]
    0.default = []
    0.desc = List of topics that `proxy` should provide as a publisher.
    1.name = ~services
    1.type = [string]
    1.default = []
    1.desc = List of services that `proxy` should provide.
    2.name = ~tcpros_port
    2.default = 11312
    2.type = int
    2.desc = Port number for external TCPROS server
    3.name = ~xmlrpc_port
    3.default = 11313
    3.desc = Port number for external XMLRPC server 
    3.type = int
  }

 }
```


