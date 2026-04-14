# rosprofiler package

The rosprofiler package provides tools for collecting and publishing
information and statistics about node processes and the hosts they are
running on, as well as information about system connectivity. These
tools are designed to work together with topic statstics tools released
in ROS Indigo to give a complete picture of the ROS system that is
published over ros topics. Other ROS nodes can then subscribe to this
information, or it can be recorded using rosbag and played back later
for analysis.

The rosprofiler package is commonly used with
[rqt_graphprofiler](rqt_graphprofiler).

## rosprofiler node

The rosprofiler node publishes statistics about the host machine and
corresponding node processes on which it is run. In a distributed system
where nodes are running on multiple host machines, rosprofiler should be
run once on each machine.

### Running rosprofiler

Before running rosprofiler, topic statistics must be enabled. To collect
statistics about all topics, this should be done before running any
other nodes. ```
rosparam set enable_statistics true
```

Once enabled, rosprofiler can be started using ```
rosrun rosprofiler rosprofiler
```

### Published Topics

```clearsilver
pub {
  no_header= True
  0.name= /host_statistics
  0.type= ros_statistics_msgs/HostStatistics
  0.desc= Host machine information and resource statistics
  1.name= /node_statistics
  1.type= ros_statistics_msgs/NodeStatistics
  1.desc= Process information and statistics for each node running on the host
}
```

## rosgrapher node

The rosgrapher node publishes information about the ROS System State
queried from the ROS Master and individual nodes. Unlike the rosprofiler
node, the rosgrapher tries to collect information about all the nodes
and topics in the system. Therefore, it is only necessary to run the
rosgrapher once even if there are nodes on multiple host machines.

### Running rosgrapher

```
rosrun rosprofiler rosgrapher
```

### Published Topics

```clearsilver
pub {
  no_header= True
  0.name= /topology
  0.type= ros_topology_msgs/Graph
  0.desc= Information about node and topic connectivity
}
```
