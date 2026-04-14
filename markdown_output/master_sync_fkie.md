## Overview

This package contains a node to synchronize the local ROS master to
remote ROS masters discovered by
[master_discovery](http://www.ros.org/wiki/master_discovery_fkie) node.
For synchronization the
[Master API](http://www.ros.org/wiki/ROS/Master_API) will be used.
Thereby the regitration of topics/services are performed only on the
local ROS master. To obtain a complete synchronization of two ROS master
one master_sync node in each \"ROS system\" have to be started.

The syncronization will be performed on each time the remote ROS master
is changed. The change detection is done by the
[master_discovery](http://www.ros.org/wiki/master_discovery_fkie) node.
To avoid multiple calls over unreliable connections e.g. WiFi, needed
for a synchronization, the XML-RPC server of the
[master_discovery](http://www.ros.org/wiki/master_discovery_fkie) node
is used to get the current state of the remote ROS master.

\'\'Note:\'\' in the current state the
[ROS Parameter server](http://www.ros.org/wiki/ROS/Parameter%20Server%20API)
will be not synchronized.

## Usage

### Getting started

Run the
[master_discovery](http://www.ros.org/wiki/master_discovery_fkie) node
first.

Run this node:

```
rosrun master_sync_fkie master_sync
```

\'\'\'Note:\'\'\' do not rename the master_sync node! If it does, use
the ignore_nodes filter to prevent synchronization of the master_sync
nodes, otherwise unpredictable effects will occur

The services and published topics of the master_discovery node are
detected automatically!

### Interface

{ }}}}

{ }}}}

```clearsilver
param{
0.name = ~interface_url
0.type = str
0.desc = The URL to the interface file, e.g. `pkg://master_sync_fkie///sync_interface.sync`. On valid interface all `ignore_` and `sync_` lists are ignored.
0.default = ``

01.name = ~resync_on_reconnect
01.type = bool
01.desc = Performs resync after the host was offline: unregister and register again to avoid connection losses to python topic. These does not suppot reconnection!
01.default = `True`

02.name = ~resync_on_reconnect_timeout
02.type = float
02.desc = A configurable period that controls how long the offline-online period [sec] is before the resync kicks in. (Since version 0.5.9)
02.default = `0`

03.name = ~do_not_sync
03.type = list
03.desc = A filter list with patterns. If this pattern merges to a node, topic or service it will not be synchronized. (Since version 0.5.4)
03.default = `[]`

1.name = ~ignore_hosts
1.type = array
1.desc = This list with names of ROS master to ignore
1.default = `[]`

2.name = ~sync_hosts
2.type = array
2.desc = This list with names of ROS master to synchronize. Only this ROS master in this list will be synchronized. The `~ignore_hosts` list is processed first.
2.default = `[]`

3.name = ~ignore_nodes
3.type = array
3.desc = The list of nodes, which are to be ignored while a synchroniation. All their topics and services are ignored! The defaults cannot be removed!
3.default = `[/rosout, "/*master_sync* node", "remote /*master_discovery* node", "/*node_manager", /*zeroconf]`

4.name = ~sync_nodes
4.type = array
4.desc = The list of nodes to synchronize. Only topics of this nodes are synchronized. The `~ignore_nodes`, `~ignore_topics` and `~ignore_services` lists are processed first.
4.default = `[]`

5.name = ~ignore_topics
5.type = array
5.desc = The list of topics, which are to be ignored while a synchroniation. The `~ignore_nodes` list is processed first. The defaults cannot be removed!
5.default = `['/rosout', '/rosout_agg']`

52.name = ~ignore_publishers
52.type = array
52.desc = The list of published topics, which are to be ignored while a synchroniation.
52.default = `[]`

53.name = ~ignore_subscribers
53.type = array
53.desc = The list of subscribed topics, which are to be ignored while a synchroniation.
53.default = `[]`

6.name = ~sync_topics
6.type = array
6.desc = The list of topics to synchronize. The `~ignore_nodes` and `~ignore_topics` lists are processed first.
6.default = `[]`

7.name = ~ignore_services
7.type = array
7.desc = The list of services, which are to be ignored while a synchroniation. The `~ignore_nodes` list is processed first. The defaults cannot be removed!
7.default = `['/*get_loggers', '/*set_logger_level']`

8.name = ~sync_services
8.type = array
8.desc = The list of services to synchronize. The `~ignore_nodes` and `~ignore_services` lists are processed first.
8.default = `[]`

8.name = ~sync_services
8.type = array
8.desc = The list of services to synchronize. The `~ignore_nodes` and `~ignore_services` lists are processed first.
8.default = `[]`

9.name = ~sync_topics_on_demand
9.type = boolean
9.desc = This parameter is only regarded, if `sync_nodes` or `sync_topics` are set. In this case the subscribed and published topics are synchronized even if they are not in the `sync_*` list
9.default = False

81.name = ~ignore_type
81.type = array
81.desc = The list of types to ignore.
81.default = `['bond/Status']`

91.name = ~sync_remote_nodes
91.type = boolean
91.desc = The nodes which are running not at the same host as the ROS master are not synchronized by default. Use sync_remote_nodes to sync these nodes also.
91.default = False
}
```
