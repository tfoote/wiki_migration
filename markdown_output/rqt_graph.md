## Overview

![ launch top window \| width=800](attachment:snap_rqt_graph_moveit_demo.png )

`rqt_graph` is the successor of [rxgraph](rxgraph).

## Topic statistics

[roscpp](roscpp) and [rospy](rospy) can measure certain statistics for
every topic connection (see [Topics](Topics) for more details. This has
to be enabled beforehand through:



```
$ rosparam set enable_statistics true
```



After that, rqt_graph will automatically annotate the ROS graph with
statistics information.

Note: rqt_graph currently does not automatically update the statistics
annotations. You have to hit the `Refresh` button to update them.

### Example

This is an example of rqt_graph with statistics measurement enabled:

![ ROS graph with statistics annotations \| width=800 ](attachment:topic_statistics_cropped.png )

Legend:

- "5.0 Hz" indicates the observed publish frequency.
-  *"110.0ms" indicates the average age of the message (might be very
  large when replaying bag files without simtime).*
- line color: red marks a high average age, green a young age. The
  limits are normed to the ages observed in the ROS graph.
- line thickness: A thick line means the connection has a large
  throughput in Bytes/s (e.g. an unfiltered PointCloud).
