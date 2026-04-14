+\'\'\'Note that as of laser_pipeline-0.4.0 this API is deprecated.
Please refer to the [laser_assembler](laser_assembler) page for the
latest API\'\'\'+\~

## Overview

The !LaserAssembler package provides two ROS nodes:

-   \'\'\'laser_scan_assembler_srv:\'\'\' Assembles a stream of
    !LaserScan messages into point clouds
-   \'\'\'point_cloud_assembler_srv:\'\'\' Assembles a stream of
    !PointCloud messages into larger point clouds

The general data flow can be descibed as follows:

![](attachment:assembler.png)

The \`LaserScanAssemblerSrv\` simply listens to the appropriate topic
and accumulates messages in a ring buffer of a specific size. When the
\`AssembleScans\` service is called, the scans in the requested interval
are assembled into a single cloud and returned.

## ROS Interface

+\'\'\'Parameters:\'\'\'+\~

The !PointCloudAssemblerSrv and !LaserScanAssemblerSrv share almost the
exact same set of parameters

-   \'\'\'tf_cache_time_secs\'\'\' (double) - The cache time (seconds)
    to hold past transforms
-   \'\'\'tf_tolerance_secs\'\'\' (double) - The time (seconds) to wait
    after the transform for scan_in is available.
-   \'\'\'max_scans\'\'\' (unsigned int) - The number of scans to store
    in the assembler\'s buffer
-   \'\'\'fixed_frame\'\'\' (string) - A stationary frame to convert the
    scans to on reception
-   \'\'\'ignore_laser_skew\'\'\' (bool) - For the
    laser_scan_assembler_srv only. Defaults to true. If true, pretend
    that all hits in a single scan correspond to the same tf transforms.
    If false, individually transform each hit to the fixed_frame (this
    is a fairly cpu intensive operation).

+\'\'\'Services:\'\'\'+\~

-   \'\'\'build_cloud\'\'\' (laser_assembler/AssembleScans)
-   \'\'request:\'\' The time interval on which we want to aggregate
    scans
-   \'\'response:\'\' Assembled cloud for the requested interval

+\'\'\'Input Topic:\'\'\'+\~

-   \'\'\'scan_in\'\'\' - Topic on which to receive a stream of scans
    (or clouds). The laser_scan_assembler_srv expects a stream of
    \`LaserScan\` messages, and the point_cloud_assembler_srv expects a
    stream of \`PointCloud\` messages

## Interfacing with a Snapshotter

There are several robot systems (including the PR2) that have an
articulated laser sensor. In these systems, it\'s often useful to get a
\"snapshot of the world\". This can be done by writing a snapshotter.

The general data flow can be described as follows:

![](attachment:snapshotter.png)

A snapshotter listens to the state of the mechanism, and then computes
the interval on which to assemble scans. This interval is requested from
!LaserScanAssemblerSrv, and then published on a topic.

In the case of the [pr2_laser_snapshotter](pr2_laser_snapshotter), it
listens to special messages from the control system that indicate when
the tilting mechanism has reached the very top or bottom of its sweep.
