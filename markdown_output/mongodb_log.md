## Overview

Autonomous mobile robots produce an astonishing amount of run-time data
during their operation. Data is acquired from sensors and actuator
feedback, processed to extract information, and further refined as the
basis for decision making or parameter estimation. In today\'s robot
systems, this data is typically volatile. It is generated, used, and
disposed right away. However, some of this data might be useful later,
for example to analyze faults or evaluate the robot\'s performance. A
system is required to store this data as well as enable efficient and
flexible querying mechanisms.

This package provides nodes that can record any and all data transmitted
via ROS topics and stores them in the document-oriented database
[MongoDB](http://www.mongodb.org) replicating the message type as
document structure. Afterwards, data can be used and queried
independently of a particular robot software framework using the
existing MongoDB query features with indexes, data locality (sharding)
and [MapReduce](http://www.mongodb.org/display/DOCS/MapReduce). This
means you can also freely mix in data acquired from other sources, for
example using [Fawkes](http://www.fawkesrobotics.org).

This project is joint work of the
[Personal Robotics Lab](http://personalrobotics.ri.cmu.edu/) at The
Robotics Institute of the Carnegie Mellon University and the
[Knowledge-based Systems Group](http://www.kbsg.rwth-aachen.de) at the
RWTH Aachen University. For more details please visit the
[project page](http://www.fawkesrobotics.org/projects/mongodb-log/).
Around 2014 it was taken within the STRANDS Project to log data from
long-term autonomous robots.

## How to get started

You can obtain mongodb_log either via the official ROS repositories
(e.g. \`apt install ros-melodic-mongodb-log\`) or install via source.
Source code is available with the
[mongodb_store repository](https://github.com/strands-project/mongodb_store).
The original source for the project can be found in
[here](https://github.com/timn/ros-mongodb_log).

Afterwards the logger can be started. To record all topics advertised in
the system execute ```
rosrun mongodb_log mongodb_log -a
``` You should start with a
small number of topics and see how the system performs. Then increase
the number of topics and see what your system can handle and the
influence of the actual robot task. You can use the tools mentioned
below to analyze this.

## Monitoring the Logging Performance

The logger regularly creates graphs based an a round-robin database
(RRD) using [RRDtool](http://oss.oetiker.ch/rrdtool/). Additionally, the
\`mongodb_rrd\` script can be run to create graphs showing the
performance of MongoDB. Example graphs look like the following.

![](http://www.fawkesrobotics.org/media/blog_images/robodb-rrd-opcounters-20101221.png)

In this graph, you see the number of operations performed, in particular
inserts during operation. Note that this graph has been edited to show
operations/sec, while graphs generated online show operations per 10
secs for performance reasons (data is only collected every 10 seconds).

## Comparing mongo_ros and mongodb_log

The [mongo_ros](mongo_ros) package provides two functionalities. For one
there is a node to store all messags of one specific topic to the
database, for another it provides a library for other nodes to interact
with the database. This mongodb_log package compares to the former part.

The \`record_to_db\` node of the [mongo_ros](mongo_ros) package stores
incoming messages as serialized blobs, much like rosbag does. This way,
queries can only be made based on the time of the message. More powerful
queries and usage of the data is only possible of a specific node has
been created or modified to record data in more verbose documents.

mongodb_log however stores all data taking the message type structure
over into the document structure. Here is an example of a TF message and
the document used to store it. Note that we have added a few empty lines
to match left and right sides more closely.

```
MongoDB document                          rostopic echo /tf
------------------------------------------------------------------------------
{                                        |
  "_id" : ObjectId("5011..."),           |
  "__topic" : "/tf",                     |
  "__recorded" : ISODate("2012-07..."),  |
  "transforms" : [                       |  transforms:
    {                                    |  -
      "header" : {                       |    header:
        "stamp" : ISODate("2012-07..."), |    stamp:
                                         |      secs: 1343297357
                                         |      nsecs: 291
        "frame_id" : "/from",            |      frame_id: /from
        "seq" : 0                        |      seq: 0
      },                                 |
      "transform" : {                    |    transform:
        "translation" : {                |      translation:
        "x" : 1,                         |        x: 1.0
        "y" : 0,                         |        y: 0.0
        "z" : 0                          |        z: 0.0
      },                                 |
      "rotation" : {                     |      rotation:
        "x" : 0,                         |        x: 0.0
        "y" : 0,                         |        y: 0.0
        "z" : 0,                         |        z: 0.0
        "w" : 1                          |        w: 1.0
      },                                 |
      "child_frame_id" : "/some_other"   |    child_frame_id: /some_other
    }                                    |
  ]                                      |
}                                        |
``` What is easy to spot is that there is a direct
one-to-one correspondence of the ROS message type and the resulting
document. Additionally, because all of the values are accessible by keys
in the document, we can formulate queries based on these keys. Hence
mongo_ros and mongodb_log cater to different audiences.

## Comparing rosbag and mongodb_log Performance

We have conducted benchmarks comparing rosbag and mongodb_log, the
results are shown in the graphs below.

![](http://www.fawkesrobotics.org/media/blog_images/robodb-rrd-cpu-mem-20120719.png)

![](http://www.fawkesrobotics.org/media/blog_images/robodb-rrd-iobw-20120719.png)

The upper graphs shows CPU and memory usage of rosbag, the generic
mongodb_log python logger, and the specific C++ logger mongodb_log_tf,
all recording the /tf topic at the same time, with transform messages
containing 5 transforms at a rate of 100 Hz. We see that the MongoDB C++
logger and rosbag perform with about the same overhead. However, MongoDB
is more efficient when writing, because rosbag writes the message type
specification for each recorded message (note that MongoDB was writing
two topics, one for the Python and the C++ logger each, while rosbag
logged only one). The generic Python logger is much more demanding in
terms of both, CPU and memory usage. The problem is the inherent Python
overhead for deserializing message, which we had also analyzed when
developing roslua (cf. [roslua README](http://timn.github.com/roslua/)).
Hence, logging many unknown topics can put a considerable burden on your
logging machine.

There are two immediate ways to avoid this. First, you can off-load
logging to a separate machine or laptop. We have done this and recorded
about 170 topics at an average rate of 120 MB/min on a Quad Core laptop
with 8 GB of RAM easily. Secondly, you can create more specific C++
loggers for your high-frequency or high-bandwidth topics following the
existing template (create a C++ logger, add to CMakeLists.txt, update
script to use it). The long-term solution will be to add support for
message introspection in C++ to ROS.

## Applications

The data acquired can be useful for a plethora of tasks. We have used it
for fault analysis and performance evaluation, as described on the
[project page](http://www.fawkesrobotics.org/projects/mongodb-log/) and
in the
[paper](http://www.fawkesrobotics.org/publications/2012/robodb-iros2012/).
More information will be provided at a later point in time.

## Documentation

More documentation has yet to be created.

## Get Involved

If you want to get in touch please contact
[Tim Niemueller](http://kbsg.rwth-aachen.de/user/1). Feel free to fork
the [github repository](http://www.github.com/timn/ros-mongodb_log) and
let us know about your changes. Please report issues on the
[issues page](https://github.com/timn/ros-mongodb_log/issues).
