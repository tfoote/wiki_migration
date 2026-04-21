## Overview

This package contains discovery nodes to detect a ROS master in a multi
robot system. There are currently two nodes 'master_discovery' and
'zeroconf' which uses different discovery strategies. 'zeroconf'
node uses an avahi implementation of zeroconf technique. The
'master_discovery' node sends periodically a multicast message to
notify about an available ROS master. Furthermore the ROS master will be
monitored for changes. On changes other discovery nodes are notified
using a timestamp. This feature is used e.g. by
[master_sync](http://www.ros.org/wiki/master_sync_fkie) to syncronize
the ROS masters. Moreover an XML-RPC server created by a discovery node
helps to avoid a lot of requests on remote ROS master for a
synchronization.

## Usage

### Getting started

Although the nodes are written in Python we need to generate message and
service types:

{ }}}} { }}}} Run the node:

```
rosrun master_discovery_fkie master_discovery
``` To use `zeroconf` for discovering you need to
run:

```
rosrun master_discovery_fkie zeroconf
``` *In this case you have to install
`python-avahi` and `avahi-daemon`!*

### Interface

{ }}}} { }}}}

## XML-RPC API

`masterContacts()`

. Retrieve the contact information of the ROS master and remote
discovery node.\
*Parameters* . `empty` *Returns* . `\[str, str, str, str, str\]` .
(timestamp of the ROS master state, ROS master URI, master name, name of
this service, URI of this RPC server)

`masterInfo()`

. Retrieve list representation of *complete* ROS system state (i.e.
publishers, subscribers, services and their types, URI's).\
*Parameters* . `empty` *Returns* . `(float, float, str, str,` . `\[
\[str,\[str\] \] \],` `\[ \[str,\[str\] \] \],` `\[ \[str,\[str\] \]
\],` `\[ \[str,str\] \],` `\[ \[str,str,str,int,str\] \],` `\[
\[str,str,str,str,str\] \])` . (stamp, stamp of local changes,
masteruri, name, publishers, subscribers, services, topicTypes, nodes,
serviceProvider)\
System state is in list representation: ```
[stamp, stamp of local changes, masteruri, name, publishers, subscribers, services, topicTypes, nodes, serviceProvider]
```
`publishers` is of the form: ```
[ [topic1, [topic1Publisher1...topic1PublisherN]] ... ]
``` `subscribers`
is of the form: ```
[ [topic1, [topic1Subscriber1...topic1SubscriberN]] ... ]
``` `services` is of the form:
```
[ [service1, [service1Provider1...service1ProviderN]] ... ]
``` `nodes` is of the form:
```
[ [topicName1, topicType1], ... ]
``` `topicTypes` is of the form:
```
[ [nodename, XML-RPC URI, origin ROS_MASTER_URI, pid, {str(local) or str(remote)} ], ... ]
``` `serviceProvider` is of the form:
```
[ [service, XML-RPC URI, origin ROS_MASTER_URI, type, {str(local) or str(remote)} ], ... ]
```
