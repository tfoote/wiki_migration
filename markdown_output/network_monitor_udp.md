## Overview

A UDP-based system for measuring network link metrics such as bandwidth,
latency and loss. It is highly configurable and versatile provides
support for multiple concurrent link tests, one-way or round-trip
measurements, constant or adaptive bandwidth rates and more.

### MonitorSource and udpmonsink

The basic link measurements are implemented by the class
`MonitorSource` (defined in `udpmonclient.py`) and the
`udpmonsink` node. `MonitorSource` sends UDP packets at a specified
rate to `udpmonsink` which timestamps them and echoes them back either
via UDP or via ROS topic message.

`MonitorSource` records packets receive times and sorts them into
latency bins based on their travel time. These latency bins can be
periodically retrieved and information such as packet loss, average
latency and bandwidth can be therefrom determined.

Multiple stream support is built in so multiple `MonitorSource`s on
the same ROS node can ping packets off the same `udpmonsink`.

For a ROS independent setup, `udpmonserv` can be used instead of
`udpmoncli`. The former is not a ROS node, but rather a standalone UDP
server. By default, `MonitorSource` does not use ROS messages for the
return path and no ROS dependency is created on the class.

### udpmonsourcenode.py

`udpmonsourcenode` is a node that implements an action server which
receives link testing goals. It instantiates and collects statistics
from multiple `MonitorSource`s. Each source (i.e. link test) is
independent of all others and can be parametrized differently in terms
of bandwidth, latency bin thresholds, update (i.e. stats collection)
interval and so on. It sends periodical feedback to the action client.

`udpmonsourcenode` also implements logic for adaptive bandwidth tests:
link tests that strive to saturate a link in terms of bandwidth while
maintaining latency and loss within specified thresholds.

Typically there would be one `udpmonsourcenode.py` node running on
every machine in a test setup as each `sourcenode` supports any number
of tests with destination sinks on different machines.

### linktest.py

The `linktest.py` implements the action client for link tests, as well
as logging and test control logic via three classes:

-   `UdpmonsourceHandle`: is a handle to a `udpmonsourcenode.py`
    (i.e. an action client); typically there would be as many instances
    as there are `udpmonsourcenode`s in the test setup.
    `UdpmonsourceHandle` also act as link test factories creating
    `Linktest` objects.
-   `LinkTest`: an instance of this class corresponds to one link
    test. Instances are created from the `UdpmonsourceHandle` class.
    It receives the periodic link test statistics (measured bandwidth,
    latency and loss) and it logs these measurements in the
    `MetricLog` class.
-   `MetricLog`: records a log of measurement for a variable and
    calculates aggregated statistics.

## ROS API

```clearsilver
node.0 {
name=udpmonsourcenode.py
desc=Implements an action server which receives link testing goals. Tracks multiple concurrently running link tests and reports feedback periodically.

param {
group.0 {
name=LinktestGoal: goal sent via actionlib that configures a link test.

0.name=duration
0.type=float
0.default=`0.0` (unlimited)
0.desc=Test duration in seconds. `0.0` means ''unlimited'' duration.

1.name=update_interval
1.type=float
1.default=`0.15` (stats are collected and reported every 150 ms)
1.desc=Interval between statistics collection and reporting (in seconds). Also, used an update interval of the adaptive bandwidth algorithm.

2.name=bw
2.type=float
2.default=`5000000.0` (the default start bandwidth is 5 Mbit/s)
2.desc=TX bandwidth (in bits per seconds). For the adaptive bandwidth algorithm this is the initial bandwidth.
 
3.name=bw_type
3.type=char
3.default=`'c'` (constant bandwidth test)
3.desc=Bandwidth test type: constant (`'c'`) or adaptive (`'a'`).

4.name=latency_threshold
4.type=float
4.default=`0.01` (10ms)
4.desc=Latency threshold (in seconds). For the adaptive bandwidth algorithm this is the threshold under which latency must be maintained.

5.name=pktloss_threshold
5.type=float
5.default=`0.5` (0.5%)
5.desc=Packet loss threshold (percentage). For the adaptive bandwidth algorithm this is the threshold under which packet loss must be maintained.

6.name=tos
6.type=byte
6.default=`0x00`
6.desc=TOS (type of service) IP packet field. Note that superuser privilege is needed for non-zero values.

7.name=pktsize
7.type=int
7.default=`1500`
7.desc=UDP packet size in bytes.

8.name=ros_returnpath
8.type=boolean
8.default=`False` (return path is over UDP)
8.desc=Whether the return path should be over ROS topics (reliable) instead of the default UDP.

9.name=roundtrip
9.type=boolean
9.default=`False` (one-way measurements)
9.desc=Whether the measurements should be round-trip or just one-way (default).

10.name=max_return_time
10.type=float
10.default=0.0
10.desc=For one-way measurements, this specifies the maximum expected return path travel time for a packet. If the maximum total travel time (the highest bin in latencybins, see below) is exceeded due to return path time running over max_return_time, statistics will be incorrect. 

11.name=rostopic_prefix
11.type=string
11.default=`""`
11.desc=The ROS return path (i.e. `udpmonsink`'s node `udpsink_feedback` topic) topic prefix used when namespaces are used because there are multiple `udpmonsink`s running concurrently.

12.name=sink_ip
12.type=string
12.default=`""`
12.desc=The IP address which the `udpmonsink` for this test is bound to.

13.name=sink_port
13.type=int
13.default=`0`
13.desc=The UDP port the `udpmonsink` is listening on.

14.name=latency_bins
14.type=float[]
14.default=`[.005, .01, .025, .05, .075, .1]` (the maximum allowed latency is 100ms)
14.desc=An array of floats (seconds) specifying the latency bins used when measuring travel time. The last (and maximum) value is the maximum allowed latency: if travel time is higher than this value, packets will be considered lost.
}

group.1 {
name=LinktestFeedback and LinktestResult: link test statistics periodic feedback and final results

0.name=latency
0.type=float
0.desc=Average latency (in seconds) of ''restricted'' packets received in the last update window (or over the whole tests). Restricted packets are those packets whose total travel time is smaller than max_allowed_latency + max_return_time.

1.name=loss
1.type=float
1.desc=Packet loss over the last update windows, or average over the whole test.

2.name=bandwidth
2.type=float
2.desc=Received (RX) bandwidth in bps in the last update windows, or average over the whole test, respectively.

3.name=latency_histogram
3.type=float
3.desc=Histogram of packet latencies. Count of packets that fell into each of the latency bins specified in the link test goal.
}
}
}
node.1 {
name=udpmonsink
desc=`udpmonsink` is a lightweight node that echoes back received packets either over UDP or as messages via a ROS topic named `udpsink_feedback`. It takes a single command-line argument: the UDP port it should listen on.
}
}
```

## Command-line tools

`udpmoncli.py` can also be used stand-alone, independent of ROS with
`udpmonserv` as in the example below:

```
# rosrun network_monitor_udp udpmonserv 12345

# rosrun network_monitor_udp udpmoncli.py 127.0.0.1 12345 10 1500
  0.501: 100   0   0   /   0   0   0   0 avg:   0.3 ms avgr:   0.3 ms loss:   0.00 %
  1.001: 100   0   0   /   0   0   0   0 avg:   0.3 ms avgr:   0.3 ms loss:   0.00 %
  1.501: 100   0   0   /   0   0   0   0 avg:   0.3 ms avgr:   0.3 ms loss:   0.00 %
  2.001: 100   0   0   /   0   0   0   0 avg:   0.4 ms avgr:   0.4 ms loss:   0.00 %
  2.501: 100   0   0   /   0   0   0   0 avg:   0.4 ms avgr:   0.4 ms loss:   0.00 %
  3.000: 100   0   0   /   0   0   0   0 avg:   0.4 ms avgr:   0.4 ms loss:   0.00 %
```

## Usage example

The following launch file starts a source and a sink node as well as a
bandwidth test node:

```
<launch>
<node name="sink" pkg="network_monitor_udp" type="udpmonsink" args="12345" output="screen"/>
<node name="source" pkg="network_monitor_udp" type="udpmonsourcenode.py" output="screen"/>
<node name="test_node" pkg="network_monitor_udp" type="sample_bwtest.py" required="true" output="screen"/>
</launch>
```

The test node starts a link capacity test on the loopback interface and
prints the resulting capacity: ```/usr/bin/env

import roslib; roslib.load_manifest('network_monitor_udp')
import rospy

from network_monitor_udp.linktest import UdpmonsourceHandle
from network_monitor_udp.linktest import LinkTest
from network_monitor_udp.msg import LinktestGoal

if __name__ == '__main__':
    rospy.init_node('test_node')
        
    source = UdpmonsourceHandle() 
    source.cancel_all_tests()

    try:
        print "Link capacity: %.2fMbit/s"%(source.get_link_capacity(sink_ip="127.0.0.1", sink_port=12345)/1e6)
    finally:
        source.cancel_all_tests()
```

Here's an example run:

```
# roslaunch launch_nodes.launch

[...]

core service [/rosout] found
process[sink-1]: started with pid [20043]
process[source-2]: started with pid [20044]
process[test_node-3]: started with pid [20055]
Link capacity: 68.71Mbit/s
```

More usage examples with more complex configurations can be found in the
[network_control_tests](network_control_tests) package.

## Tips

-   if source/sink nodes are ran on different machines, these should be
    time synchronized if measurements are made on a single direction (as
    opposed to round-trip) so that latencies are correct
