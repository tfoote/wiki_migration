## Overview

This package contains nodes and libraries for storing and retrieving
ROS-related data in a [MongoDB](http://www.mongodb.org) database using
C++ and Python. It is intended to support data persistence and
inspection, including in running systems (i.e. introspection). The main
functions are the storage and retrieval of single message (this is the
*message store*); the rosbag-like logging of topics to the db (via
[mongodb_log](mongodb_log)) and their playback (mongodb_play); and the
storage and recreation of parameters.

## Launching

The nodes provided by this package can be started together using the
mongodb_store.launch file:

```
HOSTNAME=yourhost roslaunch mongodb_store mongodb_store.launch db_path:=/path/to/db db_port:=62345
``` Without the HOSTNAME env variable the host will
revert to localhost, db_path will default to /opt/ros/mongodb_store and
db_port will default to 62345.

## Starting the MongoDB Store: mongodb_server

First set the host and port you want the datacentre to run on. We do
this via `rosparam` so that other nodes know where to find the server.

```
rosparam set mongodb_port 62345
rosparam set mongodb_host bob
``` If these are not set the server uses a
generated port number and `localhost` then sets the above parameters
to its chosen values.

Start the server:

```
rosrun mongodb_store mongodb_server.py
``` This runs the `mongod` server and also
provides some utility functions around this. By default, the mongod
database will be stored in `/opt/ros/mongodb_store`. This can be
overridden by setting the private parameter database_path for the node.
If it is the first time that the database is used, be sure to first
create the database path (e.g. `mkdir -p /opt/strands/mongodb_store`).

## Logging of Topics: mongodb_log

To create "[rosbag](rosbag) record"-like logging of topics to the
`mongodb_store` use [mongodb_log](mongodb_log). This has been updated
to store logged data in a format that can be easily recreated into ROS
messages for replay.

## Replay of Topics: mongodb_play

The `mongodb_play` node reads logged messages from the store and
replays them on their original topics. This provides a similar function
to "[rosbag](rosbag) play". Currently this node always creates its own
[sim clock](Clock) in order to play back the messages at the time they
were originally recorded.

To run the playback node, use the following options:

```
Usage: mongodb_play.py [options] [TOPICs...]

Options:
  -h, --help           show this help message and exit
  --mongodb-name=NAME  Name of DB in which to store values
``` E.g.

```
rosrun mongodb_store mongodb_play.py  /map /tf /scan
``` will play back messages previously from the
`/map` `/tf` and `/scan` topics which were previously stored in
the default database (`roslog`). `mongodb_log` and `mongodb_play`
respect latched topics.

## Parameter persistence: config_manager.py

The config manager provides a centralised way to store robot application
parameters, with optional site-specific overrides. All configurations
are stored inside the mongodb_store mongodb, within a database named
"configs".

Two levels of parameters are considered:

1\. **Global default parameters**. These should be "working
defaults" - so all essential parameters at least have a default value.
For example, if a robot application requires some calibration data then
default values should be provided. Default parameters can be shared
among sites and stored inside a shared ROS package. When the config
manager is started, all .yaml files stored in a 'defaults' folder will
be examined. Any new default parameters will automatically be inserted
into the "defaults" collection within the configs database. The
defaults folder should be supplied as a private parameter:
`defaults_path` either set to a system path or in the form
`pkg:*ros_package_name/inside/package`.*

2\. **Local parameters**. These parameters override the same named
global default parameters, allowing site-specific parameter setting.
They are stored within the database inside the "local" collection.

At start up, the config manager places all parameters onto the ros
parameter server to allow interoperability with existing software.
Parameters can also be queried using the `/config_manager/get_param
service`, or by directly connection to and querying the mongo database
server.

Likewise, local parameter overrides can be set using the
`/config_manager/set_param` service or by directly editing the
"local" collection in the configs database.

To start the config manager, make sure that you have the mongo db
running then:

```
rosrun mongodb_store config_manager.py _defaults_path:=pkg://my_package/defaults
``` This will load all parameters onto the ros
parameter server, which can be checked with:

```
rosparam list
```

### Reading parameters

There are three methods to access parameter values:

1\. Use the copy on the ros parameter server:

```
rosparam get /my/parameter
``` and likewise with the rospy and roscpp
libraries.

2\. Use the config_manager service:

```
rosservice call /config_manager/get_param "param_name: '/my/parameter'"
``` 3. Using the database server directly

### Setting parameters

Default parameters are set by placing them in the yaml files in the
defaults directory in mongodb_store. This way, default parameters are
added to the github repo and shared between all users.

The local parameter overrides can be set in 2 ways:

1\. Using the config_manager service:

```
rosservice call /config_manager/set_param "param: '{\"path\":\"/chris\",\"value\":43}'"
``` Note the syntax of the parameter: it is a json
representation of a dictionary with path and value keys.

2\. Using the config_manager service:

```
rosparam set mongodb_port 62345
rosparam set mongodb_host bob
```0 Note: This will save the current value of the
parameter into the locals database

3\. Using the database server directly

## Message Persistence: message_store_node.py

The message store node provides services to allow clients to add, update
and remove ROS messages in the mongo store via the `MessageStoreProxy`
object in both Python and C++. This is best demonstrated by examples.
With the mongodb server running, run the message store:

```
rosparam set mongodb_port 62345
rosparam set mongodb_host bob
```1

### Python Message Store Client

```
rosparam set mongodb_port 62345
rosparam set mongodb_host bob
```2

### C++ Message Store Client

```
rosparam set mongodb_port 62345
rosparam set mongodb_host bob
```3

## Replicating Stored Messages: replicator_node.py

If the constructor argument to the message store node
`replicate_on_write` is set to true, replication of the message store
parts of the store is done manually to allow different content to appear
on different hosts. A list of hosts and ports where replications should
be made can be set via the `mongodb_store_extras` ros parameter:

```
rosparam set mongodb_port 62345
rosparam set mongodb_host bob
```4 Inserts and updates are performed across the
main and replicant stores.

If `mongodb_store_extras` is set (regardless of
`replicate_on_write`), queries are performed on the main first, and if
nothing found, the replicants are tried.

You can launch additional datacentres as follows, e.g.

```
rosparam set mongodb_port 62345
rosparam set mongodb_host bob
```5 You can test if this works by adding some
things to the message store, deleting them from the master using
[RoboMongo](http://robomongo.org) (not the message store as the deletes
are replicated), then running queries.

### Action Server for Replication

The `MoveEntries` action and the corresponding action server:

```
rosparam set mongodb_port 62345
rosparam set mongodb_host bob
```6 (which is included in `datacentre.launch`)

allows you to bulk copy or move entries from message store collections
to the mongod instances defined under `mongodb_store_extras`. The
client accepts a list of collection names and uses the
`meta\["inserted_at"\]` field of the message store entries to
replicate or move all entries that were inserted before a particular
time. If no time is provided then the default is 24 hours ago. There is
an example client that does this for a list of collections specified on
the command line. This \*moves\* entries inserted 24 hours ago or
earlier.

```
rosparam set mongodb_port 62345
rosparam set mongodb_host bob
```7 **\*NOTE THAT this all makes `update`
operations a bit uncertain, so please do not use this type of
replication on collections you plan to use update on.**\*

## Nodes

```
rosparam set mongodb_port 62345
rosparam set mongodb_host bob
```8
