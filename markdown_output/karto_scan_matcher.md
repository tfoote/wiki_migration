**NOTE: From [ROS Hydro](hydro) functionality of this package is
migrated into [slam_karto](slam_karto)**.

## Overview

This package provides a C++ library that wraps the Karto scan matcher
for use in ROS nodes. Code that uses it looks like:

```
geometry_msgs::Pose2D laser_offset;
sensor_msgs::LaserScan example_scan;
// Initialize these
// ...

karto_scan_matcher::KartoScanMatcher matcher(example_scan, laser_offset, 1.0, 0.1);

vector<karto_scan_matcher::ScanWithPose> reference_scans;
geometry_msgs::Pose2D initial_pose_estimate;
sensor_msgs::LaserScan new_scan;
// Initialize these
// ..

karto_scan_matcher::ScanMatchResult res = matcher.scanMatch(new_scan, initial_pose_estimate, reference_scans);

geometry_msgs::Pose corrected = res.first;
double response = res.second;
```

The numerical arguments to the matcher constructor are the grid size and
search resolution. You can also make these vectors, in which case a
sequence of searches will be done, each initialized using the answer of
the previous one (presumably because you want to start with a coarse
search and refine it).
