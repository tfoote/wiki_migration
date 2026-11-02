## Overview

This package contains nodes and libraries for storing and retrieving
ROS-related data in a [MongoDB](http://www.mongodb.org) database using
C++ and Python. It is intended to support data persistence and
inspection, including in running systems (i.e. introspection). The main
functions are the storage and retrieval of single message (this is the
*message store*); the rosbag-like logging of topics to the db (via
[mongodb_log](https://index.ros.org/p/mongodb_log)) and their playback
(mongodb_play); and the storage and recreation of parameters.

## Launching

The nodes provided by this package can be started together using the
mongodb_store.launch file:



```
HOSTNAME=yourhost roslaunch mongodb_store mongodb_store.launch db_path:=/path/to/db db_port:=62345
```

 Without the HOSTNAME env variable the host will
revert to localhost, db_path will default to /opt/ros/mongodb_store and
db_port will default to 62345.

## Starting the MongoDB Store: mongodb_server

First set the host and port you want the datacentre to run on. We do
this via `rosparam` so that other nodes know where to find the server.



```
rosparam set mongodb_port 62345
rosparam set mongodb_host bob
```

 If these are not set the server uses a
generated port number and `localhost` then sets the above parameters
to its chosen values.

Start the server:



```
rosrun mongodb_store mongodb_server.py
```

 This runs the `mongod` server and also
provides some utility functions around this. By default, the mongod
database will be stored in `/opt/ros/mongodb_store`. This can be
overridden by setting the private parameter database_path for the node.
If it is the first time that the database is used, be sure to first
create the database path (e.g. `mkdir -p /opt/strands/mongodb_store`).

## Logging of Topics: mongodb_log

To create "[rosbag](https://index.ros.org/p/rosbag) record"-like
logging of topics to the `mongodb_store` use
[mongodb_log](https://index.ros.org/p/mongodb_log). This has been
updated to store logged data in a format that can be easily recreated
into ROS messages for replay.

## Replay of Topics: mongodb_play

The `mongodb_play` node reads logged messages from the store and
replays them on their original topics. This provides a similar function
to "[rosbag](https://index.ros.org/p/rosbag) play". Currently this
node always creates its own [sim clock](Clock) in order to play back the
messages at the time they were originally recorded.

To run the playback node, use the following options:



```
Usage: mongodb_play.py [options] [TOPICs...]

Options:
  -h, --help           show this help message and exit
  --mongodb-name=NAME  Name of DB in which to store values
```

 E.g.



```
rosrun mongodb_store mongodb_play.py  /map /tf /scan
```

 will play back messages previously from the
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
```

 This will load all parameters onto the ros
parameter server, which can be checked with:



```
rosparam list
```



### Reading parameters

There are three methods to access parameter values:

1\. Use the copy on the ros parameter server:



```
rosparam get /my/parameter
```

 and likewise with the rospy and roscpp
libraries.

2\. Use the config_manager service:



```
rosservice call /config_manager/get_param "param_name: '/my/parameter'"
```

 3. Using the database server directly

### Setting parameters

Default parameters are set by placing them in the yaml files in the
defaults directory in mongodb_store. This way, default parameters are
added to the github repo and shared between all users.

The local parameter overrides can be set in 2 ways:

1\. Using the config_manager service:



```
rosservice call /config_manager/set_param "param: '{\"path\":\"/chris\",\"value\":43}'"
```

 Note the syntax of the parameter: it is a json
representation of a dictionary with path and value keys.

2\. Using the config_manager service:



```
rosservice call /config_manager/save_param name_of_the_parameter_to_be_saved
```

 Note: This will save the current value of the
parameter into the locals database

3\. Using the database server directly

## Message Persistence: message_store_node.py

The message store node provides services to allow clients to add, update
and remove ROS messages in the mongo store via the `MessageStoreProxy`
object in both Python and C++. This is best demonstrated by examples.
With the mongodb server running, run the message store:



```
rosrun mongodb_store message_store_node.py
```



### Python Message Store Client



```python
#!/usr/bin/env python
# -*- coding: utf-8 -*-

import rospy
import mongodb_store_msgs.srv as dc_srv
import mongodb_store.util as dc_util
from mongodb_store.message_store import MessageStoreProxy
from geometry_msgs.msg import Pose, Point, Quaternion
import StringIO


if __name__ == '__main__':
    rospy.init_node("example_message_store_client")


    msg_store = MessageStoreProxy()

    p = Pose(Point(0, 1, 2), Quaternion(3, 4,  5, 6))

    try:


        # insert a pose object with a name, store the id from db
        p_id = msg_store.insert_named("my favourite pose", p)

        # you don't need a name (note that this p_id is different than one above)
        p_id = msg_store.insert(p)

        p_id = msg_store.insert(['test1', 'test2'])

        # get it back with a name
        print msg_store.query_named("my favourite pose", Pose._type)

        p.position.x = 666

        # update it with a name
        msg_store.update_named("my favourite pose", p)

        p.position.y = 2020

        # update the other inserted one using the id
        msg_store.update_id(p_id, p)

        stored_p, meta = msg_store.query_id(p_id, Pose._type)

        assert stored_p.position.x == 666
        assert stored_p.position.y == 2020
        print "stored object ok"
        print "stored object inserted at %s (UTC rostime) by %s" % (meta['inserted_at'], meta['inserted_by'])
        print "stored object last updated at %s (UTC rostime) by %s" % (meta['last_updated_at'], meta['last_updated_by'])

        # some other things you can do...

        # get it back with a name
        print msg_store.query_named("my favourite pose", Pose._type)


        # try to get it back with an incorrect name, so get None instead
        print msg_store.query_named("my favourite position", Pose._type)

        # get all poses
        print msg_store.query(Pose._type)
        # get all non-existant typed objects, so get an empty list back
        print msg_store.query( "not my type")

        # get all poses where the y position is 1
        print msg_store.query(Pose._type, {"position.y": 1})

        # get all poses where the y position greater than 0
        print msg_store.query(Pose._type, {"position.y": {"$gt": 0}})


    except rospy.ServiceException, e:
        print "Service call failed: %s"%e
```



### C++ Message Store Client



```cplusplus
#include "mongodb_store/message_store.h"
#include "geometry_msgs/Pose.h"
#include <boost/foreach.hpp>

#include <sstream>
#include <cassert>

using namespace geometry_msgs;
using namespace mongodb_store;
using namespace std;
/**
 * This tutorial demonstrates simple sending of messages over the ROS system.
 */
int main(int argc, char **argv)
{
        ros::init(argc, argv, "example_mongodb_store_cpp_client");
        ros::NodeHandle nh;

        //Create object which does the work for us.
        MessageStoreProxy messageStore(nh);

        //This is the message we want to store
        Pose p;
        string name("my pose");
        //Insert something with a name, storing id too
        string id(messageStore.insertNamed(name, p));
        cout<<"Pose \""<<name<<"\" inserted with id "<<id<<endl;

        p.position.z = 666;
        messageStore.updateID(id, p);

        // now test it worked
        assert(messageStore.queryID<Pose>(id).first->position.z == 666);

        vector< boost::shared_ptr<Pose> > results;

        //Get it back, by default get one
        if(messageStore.queryNamed<Pose>(name, results)) {

                BOOST_FOREACH( boost::shared_ptr<Pose> p,  results)
                {
                        ROS_INFO_STREAM("Got by name: " << *p);
                }
        }

        results.clear();
        if(messageStore.queryID<Pose>(id, results)) {

                BOOST_FOREACH( boost::shared_ptr<Pose> p,  results)
                {
                        ROS_INFO_STREAM("Got by ID: " << *p);
                }
        }

        p.position.x = 999;
        messageStore.updateNamed(name, p);

        results.clear();
        // try to get it back with an incorrect name, so get None instead
        messageStore.queryNamed<Pose>("my favourite position", results);
        BOOST_FOREACH( boost::shared_ptr<Pose> p,  results)
        {
                ROS_INFO_STREAM("Got: " << *p);
        }

        results.clear();
        // get all poses, should show updated named position
        messageStore.query<Pose>(results);
        BOOST_FOREACH( boost::shared_ptr<Pose> p,  results)
        {
                ROS_INFO_STREAM("Got: " << *p);
        }

        messageStore.deleteID(id);

        results.clear();
        if(messageStore.queryID<Pose>(id, results)) {

                BOOST_FOREACH( boost::shared_ptr<Pose> p,  results)
                {
                        ROS_INFO_STREAM("Got by ID: " << *p);
                }

        }
        return 0;
}
```



## Replicating Stored Messages: replicator_node.py

If the constructor argument to the message store node
`replicate_on_write` is set to true, replication of the message store
parts of the store is done manually to allow different content to appear
on different hosts. A list of hosts and ports where replications should
be made can be set via the `mongodb_store_extras` ros parameter:



```
mongodb_store_extras: [["localhost", 62344], ["localhost", 62333]]
```

 Inserts and updates are performed across the
main and replicant stores.

If `mongodb_store_extras` is set (regardless of
`replicate_on_write`), queries are performed on the main first, and if
nothing found, the replicants are tried.

You can launch additional datacentres as follows, e.g.



```
rosrun mongodb_store mongodb_server.py _master:=false _database_path:=/opt/strands/strands_mongodb_62344 _host:=localhost _port:=62344
rosrun mongodb_store mongodb_server.py _master:=false _database_path:=/opt/strands/strands_mongodb_62333 _host:=localhost _port:=62333
```

 You can test if this works by adding some
things to the message store, deleting them from the master using
[RoboMongo](http://robomongo.org) (not the message store as the deletes
are replicated), then running queries.

### Action Server for Replication

The `MoveEntries` action and the corresponding action server:



```
rosrun mongodb_store replicator_node.py
```

 (which is included in `datacentre.launch`)

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
rosrun mongodb_store replicator_client.py message_store robblog scheduling_problems
```

 **\*NOTE THAT this all makes `update`
operations a bit uncertain, so please do not use this type of
replication on collections you plan to use update on.**\*

## Nodes

### mongodb_server.py

Starts the mongod server and provides utility services.

#### Parameters

- `~test_mode` (`bool`, default: `false`): Starts the datacentre with a
  random port and database path on localhost. Used for testing.
- `~database_path` (`string`, default: `/opt/ros/mongodb_store`):
  Directory path for the mongo database. This path must exist.
- `~master` (`bool`, default: `true`): Whether this the master mongodb
  store or a replication store. This is a feature only used with
  replication and can be ignored if you only use a single store.
- `mongodb_host` (`string`, default: `localhost`): Host to run the
  mongod server as
- `mongodb_port` (`int`, default: `27017`): Port to run the mongod
  server on

#### Parameters Set

- `mongodb_host` (`string`, default: `localhost`): Host to run the
  mongod server as
- `mongodb_port` (`int`, default: `27017`): Port to run the mongod
  server on

### config_manager.py

Publishes persistent parameters via rosparam

#### Parameters

- `~defaults_path` (`string`): Path from which to load default
  configuration
- `mongodb_host` (`string`, default: `localhost`): Host to find the
  mongod server on
- `mongodb_port` (`int`, default: `27017`): Port to find the mongod
  server on

### message_store_node.py

Provides services to store and retrieve ROS messages in the mongodb
store.

#### Parameters

- `mongodb_host` (`string`): Host of the master server to store messages
  in.
- `mongodb_port` (`int`): Port of the master server to store messages
  in.
- `mongodb_store_extras` (`list`, default: `[]`): List of hosts, port
  pairs to replicate to.

### replicator_node.py

Uses `mongodump` to replicate mongodb store content across multiple
hosts.

#### Parameters

- `mongodb_store_extras` (`list`): List of hosts, port pairs to
  replicate to.
- `mongodb_host` (`string`): Host of the master server to replicate
  from.
- `mongodb_port` (`int`): Port to the master server to replicate from.
