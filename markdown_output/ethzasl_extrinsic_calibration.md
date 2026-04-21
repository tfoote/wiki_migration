## Overview

This package allows for the calibration of two rigidly-linked reference
frames given a series of transformations. You can see this package in
action in our ROS contest entry:
[openni/Contests/ROS 3D/Automatic Calibration of Extrinsic Parameters](openni/Contests/ROS 3D/Automatic Calibration of Extrinsic Parameters).

There are two programs in this package: `tf_logger`, a node that dumps
the transformations regularly and `optimizer`, a stand-alone program
that computes the transformation between the frames.

For installation instructions, see the
[ethzasl_icp_mapping](ethzasl_icp_mapping) stack page.

## Program: Logging

`tf_logger` will record the changes of two frames published in `tf`
each with respect to its own reference and dump it as text into an
output file.



```
rosrun ethzasl_extrinsic_calibration tf_logger
```



### Parameters

`/baseLinkFrame` (`string`, default: `"/base_link"`) First
reference frame to log. `/odomFrame` (`string`, default:
`"/odom"`) Parent frame for the first reference frame.
`/kinectFrame` (`string`, default:
`"/openni_rgb_optical_frame"`) Second reference frame to log.
`/worldFrame` (`string`, default: `"/world"`) Parent frame for
the second reference frame. `/outputFileName` (`string`, default:
`"output.txt"`)

## Program: Calibration

`optimizer` will use an evolutionary strategy to compute the
transformation from the first reference frame to the second, reading
these frames from a text file. 

```
rosrun ethzasl_extrinsic_calibration optimizer <dtf_file> [inlier_ratio] [restart_count] [gen_count]
```



### Arguments

`<dtf_file>` (`filename`) Name of output file from `tf_logger`
or from `modular_cloud_matcher_bag`.

`\[inlier_ratio\]` (`double`, default: `0.8`) Ratio of inlier to
keep when computing the error. The pair of transforms with the largest
errors will be discarded. This allows to find a good-quality transform
even if the tracker used to produce the transforms sometimes failed.

`\[restart_count\]` (`positive integer`, default: `1`) Number of
random restarts of the evolution strategy. Setting this value to more
than 1 will run the optimization multiple times starting from random
values and will give you the average result and an estimate of its
variance.

`\[gen_count\]` (`positive integer`, default: `64`) Number of
generation for the evolution strategy. Increasing this setting will
reduce the variance between random restarts, but will take more time.

### Output

`optimizer` prints both a line that can be added to a `launch` file
to provide the computed transformation in the `tf` tree and the
command to publish this transformation directly from the command line:


```
Optimization completed, code to COPY-PASTE in to use the transformation:

<node pkg="tf" type="static_transform_publisher" name="base_link_to_kinect"
args=0.182129 0.00632656 0 -0.491826 0.498884 -0.499452 0.509676 /base_link /kinect 100"/>

OR

rosrun tf static_transform_publisher 0.182129 0.00632656 0 -0.491826 0.498884 -0.499452 0.509676 /base_link /kinect 100
```



Also, if random restarts are used, it gives an estimate of the variance.

### File Format

The text file between `tf_logger` and `optimizer` consists of a
sequence of lines, each line providing a pair of transforms. This, the
format for one line is the following: 

```
timestamp
tr1_trans_x tr1_trans_y tr1_trans_z tr1_quat_x tr1_quat_y tr1_quat_z tr1_quat_w tr2_trans_x tr2_trans_y tr2_trans_z tr2_quat_x tr2_quat_y tr2_quat_z tr2_quat_w
```



## Known issues

On x86-32, sometimes the optimizer segfaults. Either retry or use an
amd64 kernel.

## Report a Bug

Please report bugs and request features using the
[github page](https://github.com/ethz-asl/ethzasl_icp_mapping/issues).
