## Package Summary

A ROS node that allows control of network emulation parameters such as
bandwidth, loss and latency for a Linux network interface. Traffic
control is separate for each direction: egress and ingress.

## ROS API

```clearsilver
node.0 {
name=traffic_control_node.py
desc=`traffic_control_node.py` provides control of the network emulation parameters of a  network interface. The node is controlled via a [[dynamic_reconfigure]] interface.

param {
group.0 {
name=Node parameters
desc=These are the startup parameters of the node.

0.name= ~interface
0.type= string
0.desc= The name of the interface that will be controlled (e.g. `lo`, `eth0`, `wlan1`). This parameter '''must''' be specified.

1.name = ~interface_ifb
1.type = string
1.default = `ifb0`
1.desc= The name of the ifb interface to be used for ingress traffic control. If controlling multiple interfaces on the same host (via multiple `traffic_control_node.py` nodes), this parameter will have to be specified so that each node uses a different interface (i.e. `ifb0`, `ifb1`, etc)

2.name = ~filter_egress
2.type = string
2.default = `u32 match u32 0 0` (i.e. match all packets)
2.desc = `tc` filter match string for egress. By default, the egress traffic control applies to all packets. Using this parameter, only packets that match the filter will be subject to traffic control. For example, `u32 match ip dport 12345 0xffff` matches only IP packets with destination port 12345. See the [[http://lartc.org/howto/lartc.qdisc.filters.html|tc documentation]] for more information.

3.name = ~filter_ingress
3.type = string
3.default = `u32 match u32 0 0` (i.e. match all packets)
3.desc = Same as `filter_egress`, but for the ingress direction.
}
group.1 {
name=Dynamically Reconfigurable Parameters
desc= See the [[dynamic_reconfigure]] package for details on dynamically reconfigurable parameters.

0.name= ~bandwidth_egress
0.default= 0.0
0.type= double
0.desc=Bandwidth limit for egress direction (in bits per second). Set to 0.0 to disable bandwidth control (in effect, a very large bandwidth limit would be set). Range: 0.0 to 10000000000.0

1.name= ~latency_egress
1.default= 0.0
1.type= double
1.desc=Egress latency (seconds). Each packet leaving the interface gets delayed by this amount. Set to 0.0 to disable. Range: 0.0 to 2.0

2.name= ~loss_egress
2.default= 0.0
2.type= double
2.desc=Egress loss (%). Percent of packets that get dropped as they leave the interface. Set to 0.0 to disable. Range: 0.0 to 100.0

3.name= ~bandwidth_ingress
3.default= 0.0
3.type= double
3.desc= Bandwidth limit for ingress direction (bps) Range: 0.0 to 10000000000.0

4.name= ~latency_ingress
4.default= 0.0
4.type= double
4.desc=Ingress latency (s). Range: 0.0 to 2.0

5.name= ~loss_ingress
5.default= 0.0
5.type= double
5.desc=Ingress loss (%). Range: 0.0 to 100.0

6.name= ~packet_size
6.default= 1500
6.type= int
6.desc=Packet size (bytes). This parameter is very important as it determines the sizing of the internal queues and hence the latency added when the link is saturated. Also, if controlling only bandwidth, packets larger than the specified size will get dropped. See the section below for a detailed discussion. Range: 0 to 65536

7.name= ~status
7.default= `OK`
7.type= string
7.desc= The status of the last operation. Possible values are: `OK`: operation successfully completed and `FAIL`: last operation failed. This parameter is '''read-only'''.

8.name= ~errmsg
8.default= `` 
8.type= string
8.desc= An error message describing the error (or warning) raised by the last operation or the empty string if the operation was succesful. This parameter is '''read-only'''.
}
}
```

## How it works

There are some peculiarities about the way
[tbf](http://lartc.org/howto/lartc.qdisc.classless.html#AEN691), used
for bandwidth control, and
[netem](http://www.linuxfoundation.org/collaborate/workgroups/networking/netem),
used for latency and loss emulation, interact that affect the link
emulation metrics. This section describes what the expected network
emulation result is depending on the usage scenario.

A few definitions:

-   \`bandwidth_limit\` is the specified link capacity to be emulated
    (so either \`bandwidth_egress\` or \`bandwidth_ingress\` depending
    on the direction)
-   \`tx_bandwidth\` is the rate at which data enters the emulation
    mechanism (e.g. the rate at which data is sent from a process or it
    comes in from the network)
-   \`tx_bandwidth_loss_adjusted\` is the adjusted rate after applying
    the \`loss\` specification; for example if \`tx_bandwidth\` is
    2Mbit/s and \`loss\` is 50%, then \`tx_bandwidth_loss_adjusted\`
    will be 1Mbit/s
-   the link is \`saturated\` when bandwidth control is in effect
    (\`bandwidth_limit \> 0.0\`) and \`tx_bandwidth_loss_adjusted \>
    bandwidth_limit\` (i.e. even after adjusting for loss the data rate
    is greater than the link capacity)
-   \`packet_send_time_at_capacity\` is the time to send one packet at
    the \`bandwidth_limit\` rate (**Note:** this is where the
    \`packet_size\` parameter comes into play!)
-   \`measured_bandwidth\`, \`measured_loss\` and \`measured_latency\`
    are the metrics measured at the output of the emulation system (i.e.
    on the receiving end)

Using these definitions we distinguish a few scenarios and the actual
network metrics that result from the network emulator implementation:

1\. When the link is **not saturated**, the metrics are as expected:

-   \`measured_bandwidth == tx_bandwidth_loss_adjusted\`
-   \`measured_latency == latency\`
-   \`measured_loss == loss\`

2\. When the link is **saturated** and **only bandwidth control** is in
place (i.e. \`latency\` and \`loss\` are \`0.0\`). **Note that under
this scenario all packets with size greater than \`packet_size\` will be
dropped!**

-   \`measured_bandwidth == bandwidth_limit\`
-   \`measured_latency == packet_send_time_at_capacity\`, is not 0ms due
    to the time spent by each packet in the internal tbf queue (whose
    size is one packet)
-   \`measured_loss = 100% - bandwidth_limit/tx_bandwidth(%)\`, the
    percentage by which bitrate overruns the link capacity

3\. When the link is **saturated** and **both bandwidth control and
latency and/or loss control** is in place:

-   \`measured_bandwidth == min(bandwidth_limit,
    tx_bandwidth_loss_adjusted)\`, either the link capacity or the loss
    adjusted \`tx_bandwidth\`, whichever is smaller.
-   \`measured_latency\` is the specified \`latency\`, but adjusted up
    to the nearest multiple of \`packet_send_time_at_capacity\`
-   \`measured_loss\` is either the specified \`loss\` or the \`loss\`
    due to capacity overrun, whichever is greater

## Command-line tools

There are two tools intended to help in determining the effect of a
combination of link emulation parameters and send bitrate on the
measured (or \"received\") metrics.

The first tool infers these values based on the algorithm described in
the previous section while the second one actually measures them using
the loopback interface.

### projected_link_metrics.py

This tool takes as parameters:

-   the \`bandwidth_limit\`, \`loss\` and \`latency\`
-   the \`packet_size\`
-   the \`tx_bandwidth\` and projects the expected network emulation
    metrics:
-   \`measured_bandwidth\`
-   \`measured_latency\`
-   \`measured_loss\`

For example, for a link with capacity 1Mbit/s which is saturated since
the TX rate is 1.5MBit/s:

```
# rosrun network_traffic_control projected_link_metrics.py 1000000 0.0 0.0 1500 1500000
Projected metrics: bandwidth 1000.00Kbit/s latency 12.00ms loss 33.33%
```

The bandwidth is the link capacity, the latency is the time to send one
packet (i.e. 1500 bytes at 1Mbit/s) and the loss is due to the
overrunning the link capacity.

Other examples:

-   link saturated, bandwidth and latency control
    ```
# rosrun network_traffic_control projected_link_metrics.py 1000000 0.04 0.0 1500 1500000
Projected metrics: bandwidth 1000.00Kbit/s latency 60.00ms loss 33.33%
```

```{=html}
<!-- -->
```
-   link saturated, bandwidth and latency and loss control
    ```
# rosrun network_traffic_control projected_link_metrics.py 1000000 0.04 80.0 1500 1500000
Projected metrics: bandwidth 300.00Kbit/s latency 40.00ms loss 80.00%
```

```{=html}
<!-- -->
```
-   link not saturated, bandwidth and latency and loss control
    ```
# rosrun network_traffic_control projected_link_metrics.py 1000000 0.02 20.0 1500 500000
Projected metrics: bandwidth 400.00Kbit/s latency 20.00ms loss 20.00%
```

### measure_link_node.py

In order, to verify experimentally the theoretical projections of the
\`projected_link_metrics.py\` tool, a node (\`measure_link_node.py\`)
and an associated launch file (\`measure_link.launch\`) have been
created which implement the network emulation on the \`lo\` (loopback)
interface and use the [network_monitor_udp](network_monitor_udp) package
for metric measurement.

This node and the associated launch file live in the
[network_control_tests](network_control_tests) package in the \`test/\`
subdirectory.

Here\'s an example, whose results agree quite closely with the
theoretical projection made previously:

```
# roslaunch measure_link.launch tx_bandwidth:=1500000 bandwidth_limit:=1000000 latency:=0.0 loss:=0.0

[...]

[INFO] 1288966581.041664: Link measurement completed!
[INFO] 1288966581.042628: Link parameters: bandwidth_limit 1000.00kbit/s latency 0.00ms loss 0.00% tx_bandwidth 1500.00kbit/s
                 packet_size 1500bytes max_allowed_latency 100.00ms max_return_time 0.00ms
                 direction egress duration 10.00s
[INFO] 1288966581.043424: RESULTS: measured_bandwidth 974.48kbit/s measured_latency 8.41ms measured_loss 35.02%
```

The launch file (and node) takes the following parameters:

-   \`tx_bandwidth\`: the rate at which data is sent. This is the only
    **mandatory** parameter.
-   \`bandwidth_limit\`, \`latency\`, \`loss\`: network emulation
    parameters (they all default to 0.0 - i.e. control disabled)
-   \`packet_size\`: default 1500 bytes
-   \`max_allowed_latency\`: the maximum latency before which packets
    are considered lost (default: 100ms). It\'s important that this
    parameter is larger then the expected packet latency (in fact, an
    automatic check is made with an estimate obtained with the
    \`projected_link_metrics.py\` tool and if the condition fails, the
    test is rejected)
-   \`max_return_time\`: this parameter is only relevant if the test is
    ran on a \"real\" interface (i.e. not \`lo\`). It specifies the
    maximum delay expected on the return path (i.e. one-way travel time
    on the link). Default: 0.0ms.
-   \`direction\`: \`egress\` or \`ingress\`
-   \`duration\`: in seconds (default: 10 seconds)

Some more examples:

```
# roslaunch measure_link.launch tx_bandwidth:=1500000 bandwidth_limit:=1000000 latency:=0.04 loss:=0.0

[...]

[INFO] 1288967237.290097: Link measurement completed!
[INFO] 1288967237.291093: Link parameters: bandwidth_limit 1000.00kbit/s latency 40.00ms loss 0.00% tx_bandwidth 1500.00kbit/s
                 packet_size 1500bytes max_allowed_latency 100.00ms max_return_time 0.00ms
                 direction egress duration 10.00s
[INFO] 1288967237.291811: RESULTS: measured_bandwidth 978.08kbit/s measured_latency 69.74ms measured_loss 34.80%
```

```
# roslaunch measure_link.launch tx_bandwidth:=1500000 bandwidth_limit:=1000000 latency:=0.04 loss:=80.0

[...]

[INFO] 1288967298.388572: Link measurement completed!
[INFO] 1288967298.389555: Link parameters: bandwidth_limit 1000.00kbit/s latency 40.00ms loss 80.00% tx_bandwidth 1500.00kbit/s
                 packet_size 1500bytes max_allowed_latency 100.00ms max_return_time 0.00ms
                 direction egress duration 10.00s
[INFO] 1288967298.390246: RESULTS: measured_bandwidth 279.58kbit/s measured_latency 39.58ms measured_loss 81.36%
```

```
# roslaunch measure_link.launch tx_bandwidth:=500000 bandwidth_limit:=1000000 latency:=0.02 loss:=20.0

[...]

[INFO] 1288967485.547524: Link measurement completed!
[INFO] 1288967485.548481: Link parameters: bandwidth_limit 1000.00kbit/s latency 20.00ms loss 20.00% tx_bandwidth 500.00kbit/s
                 packet_size 1500bytes max_allowed_latency 100.00ms max_return_time 0.00ms
                 direction egress duration 10.00s
[INFO] 1288967485.549177: 
RESULTS: measured_bandwidth 394.65kbit/s measured_latency 20.19ms measured_loss 21.28%
```

## Implementation details

### Egress

An htb qdisc is created on the root of the interface with a single htb
class with a very high limit (10Gbps). This htb class at the root is
needed in order to attach the filter as only classful qdisc\'s can have
filters (and tbf is classless).

Next, a tbf
([Token Bucket Filter](http://lartc.org/howto/lartc.qdisc.classless.html#AEN691))
qdisc for bandwidth control is attached. Finally, if latency or loss
control is enabled, a netem qdisc child is attached to the tbf qdisc.

### Ingress

An [ingress](http://lartc.org/howto/lartc.adv-qdisc.ingress.html) qdisc
is created on the interface and an
[ifb](http://www.linuxfoundation.org/collaborate/workgroups/networking/ifb)
interface is created. A filter is attached to the ingress qdisc that
redirects matching packets to the ifb interface. A setup identical to
that described for egress is then created on this ifb interface.

### tbf parameters

For bandwidth control there are three parameters of interest:

-   \`rate\`: the bandwidth limit
-   \`limit\`: the length of the queue in bytes. This is set to the
    packet size which means that exactly one packet can wait in the
    queue. If the size would be smaller than the packet size, all
    packets would be dropped. Larger limit values would mean more time
    spent in queue when sending at a rate higher than \`rate\` (and thus
    a higher added latency). With the current implementation, if the
    incoming bitrate is smaller than the set limit then no delay is
    added to the total travel time of a packet while if the rate limit
    is overran then a latency equal to one packet\'s transmission time
    is added (e.g. 10ms for a 1500bytes packet at 1.2Mbit/s).
-   \`buffer\`: this defines the maximum packet burst that may be sent
    when having a fluctuating send rate. It is currently defined to be
    equal to 5 packet sizes.

### netem parameters

The parameter of interest for netem is \`limit\` which defines the size
of an internal queue in packets. If no bandwidth control is in place,
then this parameter is set to a high value (1000). If there is bandwidth
control then the value of this parameter is selected as a function of
latency and packet size, more specifically, it is equal to the number of
packets whose transfer time at link capacity is equal to the specified
latency.
