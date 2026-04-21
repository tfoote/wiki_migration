# Overview

This page describes the message and service types used by arni. This
information might be out of date, for recent data look here:
<https://github.com/ROS-PSE/arni/tree/master/arni_msgs>

## Message Types

### HostStatistics

Contains statistics about a host's resource usage.


```
# ip of the host  
string host

# the statistics apply to this time window
time window_start
time window_stop

# cpu  
float32 cpu_temp_mean
float32 cpu_temp_stddev
float32 cpu_temp_max

float32 cpu_usage_mean
float32 cpu_usage_stddev
float32 cpu_usage_max

float32[] cpu_usage_core_mean
float32[] cpu_usage_core_stddev
float32[] cpu_usage_core_max

float32[] cpu_temp_core  
float32[] cpu_temp_core_mean
float32[] cpu_temp_core_stddev
float32[] cpu_temp_core_max


# gpu
float32[] gpu_temp_mean
float32[] gpu_temp_stddev
float32[] gpu_temp_max

float32[] gpu_usage_mean
float32[] gpu_usage_stddev
float32[] gpu_usage_max
 

# ram  
float32 ram_usage_mean
float32 ram_usage_stddev
float32 ram_usage_max
  
# network

string[] interface_name 
int32[] message_frequency_mean
int32[] message_frequency_stddev
int32[] message_frequency_max

# bandwith of each network interface

float32[] bandwidth_mean
float32[] bandwidth_stddev
float32[] bandwidth_max
```



### NodeStatistics

Contains statistics about a node's resource usage.


```
#ip of the host this node belongs to
string host

#identifier of this node
string node

# the statistics apply to this time window
time window_start
time window_stop

#CPU

float32 node_cpu_usage_mean
float32 node_cpu_usage_stddev
float32 node_cpu_usage_max

float32[] node_cpu_usage_core_mean
float32[] node_cpu_usage_core_stddev
float32[] node_cpu_usage_core_max


#GPU 

float32[] node_gpu_usage_mean
float32[] node_gpu_usage_stddev
float32[] node_gpu_usage_max

# ram  
float32 node_ramusage_mean
float32 node_ramusage_stddev
float32 node_ramusage_max
  
# network load of the node
 
float32 node_message_frequency_mean
float32 node_message_frequency_stddev
float32 node_message_frequency_max

float32 node_bandwidth_mean
float32 node_bandwidth_stddev
float32 node_bandwidth_max

# Drive I/O statistics of the node 

float32 node_write_mean
float32 node_write_stddev
float32 node_write_max

float32 node_read_mean
float32 node_read_stddev
float32 node_read_max
```



### RatedStatisticsEntity

Contains comparisons of expected value and actual value for a statistic.


```
# type of statistic like cpu_usage_core or cpu_usage
string statistic_type

# the value of the type
string[] actual_value

# the expected value like "40 - 70"
string[] expected_value

# constant
uint8 HIGH=0
uint8 LOW=1
uint8 UNKNOWN=2
uint8 OK=3

# state of the metadata from the node/host/connection : 
# state: { 0 = high ; 1 = low ; 2 = unknown; 3 = ok}  
uint8[] state
```



### RatedStatistics

Contains an array of RatedStatisticsEntities for a node, host , or
connection. 

```
# name of node/host/connection 
string seuid

# only used if seuid is a node. is the host ip the node runs on.
string host  

# the rated statistics apply to statistics from this time window
time window_start
time window_stop

# an array of rated entities
RatedStatisticsEntity[] rated_statistics_entity
```



### MasterAPIEntity

Represents a single entry of the master API

```
string name
string[] content
```



### MasterApi

Contains all the information masterApi.Master.getSystemState returns
which is information about publishers, subscribers and services.


```
# publisher
MasterApiEntity[] pubs
# subscriber
MasterApiEntity[] subs
# services
MasterApiEntity[] srvs
```



## Service Types

### NodeReaction

Stop or restart a node on a host or execute a shell command on host


```
# identifier of the affected node
string node

# action  [restart, stop, command]
string action

# command (for action command)
string command
---
# message returned upon completion
string returnmessage
```



### StatisticHistory

Receive a History of the last few statistics send out


```
# get all statistics where timestamp in ms is > than timestamp
time timestamp
---
# each statistic has its own rated statistic. 
# timestamps can be found at the time windows of each statistic

HostStatistics[] host_statistics
RatedStatistics[] rated_host_statistics

NodeStatistics[] node_statistics
RatedStatistics[] rated_node_statistics

rosgraph_msgs/TopicStatistics[] topic_statistics
RatedStatistics[] rated_topic_statistics
```


