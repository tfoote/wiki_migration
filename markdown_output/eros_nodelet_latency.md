## Overview

This package has code for two nodelets, Publisher and Subscriber which
communicate on a common topic "/big_object" to which a very large
timestamped array is published (BigObject).

The nodelets are packaged in a library, and two launch configurations
are setup for testing latencies across the big_object communication
channel.

## Usage

### Internal

The launcher internal.launch loads both publisher and subscriber
nodelets on the same manager (i.e. they coexist in the same process). In
this situation, the transport communication medium passes the BigObject
via pointers, so we can expect to see very low latencies being generated
by this.



```
roslaunch eros_nodelet_latency internal.launch
```



Upon execution, you should see the average latency continually being
communicated to standard output. Ctrl-c to terminate the application.

### External

The launcher `external.launch` launches both publisher and subscriber
as standalone processes. In this situation, the BigObject is copied
across TCP/IP (some 4MB!), so expect very high latencies here.

roslaunch eros_nodelet_latency external.launch
