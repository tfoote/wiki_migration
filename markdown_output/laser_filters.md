## Overview

The primary content of the \`laser_filters\` package is a number of
general purpose filters for processing
\<\<MsgLink(sensor_msgs/LaserScan)\>\> messages. These filters are
exported as plugins designed to work with with the
[filters package](filters). At the moment all of these filters run
directly on \<\<MsgLink(sensor_msgs/LaserScan)\>\>, but filters may be
added in the future which process
\<\<MsgLink(sensor_msgs/PointCloud)\>\> instead. Please review the
[filters documentation](filters) for an overview of how filters and
filter chains are intended to work.

This package provides two nodes that can run multiple filters
internally. Using these nodes to run your filters is considered best
practice, since it allows multiple nodes to consume the output while
only performing the filtering computation once. The nodes are minimal
wrappers around filter chains of the given type. The
[scan_to_scan_filter_chain](#scan_to_scan_filter_chain) applies a series
of filters to a \<\<MsgLink(sensor_msgs/LaserScan)\>\>. The
[scan_to_cloud_filter_chain](#scan_to_cloud_filter_chain) first applies
a series of filters to a \<\<MsgLink(sensor_msgs/LaserScan)\>\>,
transforms it into a \<\<MsgLink(sensor_msgs/PointCloud)\>\>, and then
applies a series of filters to the
\<\<MsgLink(sensor_msgs/PointCloud)\>\>.

## Using Laser Filters

Each [ laser filter](#plugins ) is a separate plugin exported by the
laser_filters package. This allows them to be specified in a
configuration file which can be loaded into an arbitrary filter_chain
templated on a \<\<MsgLink(sensor_msgs/LaserScan)\>\>. You can
instantiate a laser filter into a filter_chain in C++
([example](laser_filters/Tutorials/Laser filtering in C++)), or you can
use the [ scan_to_scan_filter_chain](#scan_to_scan_filter_chain ) and
[ scan_to_cloud_filter_chain](#scan_to_cloud_filter_chain ) nodes which
contain appropriate filter chains internally
([example](laser_filters/Tutorials/Laser filtering using the filter nodes)).

[ Filter chains](filters ) are configured from the parameter server.
They expect a parameter which is a list made up of repeating blocks of
filter configurations. These should almost always be specified in a
\`.yaml\` file to be pushed to the parameter server. Each filter
specified in the chain will be applied in order.

The individual filters configurations contain a \`name\` which is used
for debugging purposes, a \`type\` which is used to locate the plugin,
and a \`params\` which is a dictionary of additional variables. Consult
the documentation for the particular filter plugin to see what variables
may be set in the params field.

**Note** that the \`type\` should be specified as
\`pkg_name/FilterClass\` as the
[matching behavior of the filters implementation before lunar](https://github.com/ros/filters/issues/14)
is
[not necessarily matching the exact name](https://github.com/ros-perception/laser_filters/issues/50),
if only the \`FilterClass\` is used.

For example, in a package, \`mypkg\`, to launch a
[ scan_to_scan_filter_chain](#scan_to_scan_filter_chain ) with two
filters: \`LaserFilterClass1\` and \`LaserFilterClass2\`, you could use
the file:

\`my_laser_config.yaml\`: ```yaml
scan_filter_chain:
- name: unique_name1
  type: mypkg/LaserFilterClass1
  params:
    param1: a
    param2: b
- name: unique_name2
  type: mypkg/LaserFilterClass2
  params:
    param1: a
    param2: b
```

You could then push this configuration to the parameter server using
[rosparam](rosparam) by running: ```
$ rosparam load my_laser_config.yaml scan_to_scan_filter_chain
```

And then launching the \`scan_to_scan_filter_chain\`:
```
$ rosrun laser_filters scan_to_scan_filter_chain
```

## Laser Filter Nodes

### scan_to_scan_filter_chain (new in laser_pipeline-0.5)

The scan_to_scan_filter_chain is a very minimal node which wraps an
instance of a \`filters::FilterChain\<sensor_msgs::LaserScan\>\`. This
node can be used to run any filter in this package on an incoming laser
scan. If the \`tf_message_filter_target_frame\` parameter is set, it
will wait for the transform between the laser and the target_frame to be
available before running the filter chain.

![](attachment:scan_to_scan_filter_chain.png)

#### ROS Parameters

\`scan_filter_chain\` (list) **\[Required\]** The list of laser filters
to load.

\`tf_message_filter_target_frame\` (string) A target_frame for which a
transform must exist at the current time before the filter_chain will be
executed. This is the target_frame internally passed to the
\`tf::MessageFilter\`. If this parameter is not set, the chain will
simply be executed immediately upon the arrival of each new scan.

#### Subscribed Topics

\`scan\` (\<\<MsgLink(sensor_msgs/LaserScan)\>\>) The incoming laser
scan to filter

#### Published Topics

\`scan_filtered\` (\<\<MsgLink(sensor_msgs/LaserScan)\>\>) The outgoing
filtered laser scan

#### Example Launch File

\`my_laser_filter.launch\`: ```
<launch>
  <node pkg="laser_filters" type="scan_to_scan_filter_chain"
      name="laser_filter">
    <rosparam command="load" file="$(find mypkg)/my_laser_config.yaml" />
    <remap from="scan" to="base_scan" />
  </node>
</launch>
```

\`my_laser_config.yaml\`: ```
scan_filter_chain:
- name: shadows
  type: laser_filters/ScanShadowsFilter
  params:
    min_angle: 10
    max_angle: 170
    neighbors: 20
    window: 1
- name: dark_shadows
  type: laser_filters/LaserScanIntensityFilter
  params:
    lower_threshold: 100
    upper_threshold: 10000
    disp_histogram: 0
```

### scan_to_cloud_filter_chain

The scan_to_cloud_filter_chain is a very minimal node which wraps an
instances of \`filters::FilterChain\<sensor_msgs::LaserScan\>\` and
\`filters::FilterChain\<sensor_msgs::PointCloud\>\`. This node can be
used to run any filter in this package on an incoming laser scan. After
performing the laser filtering, it will use the \`LaserProjection\` from
[laser_geometry](laser_geometry) to transform each scan into a point
cloud. It will then run any cloud-based filtering, and finally publish
the resultant cloud.

![](attachment:scan_to_cloud_filter_chain.png)

#### ROS Parameters

\`scan_filter_chain\` (list) **\[Required\]** The list of laser filters
to load. \`cloud_filter_chain\` (list) **\[Required\]** The list of
cloud filters to load. \`target_frame\` (string) **\[Required\]** The
frame to transform the point_cloud into. \`high_fidelity\` (bool,
default: false) Whether to perform a high fidelity transform. This
approach assumes that the laser scanner is moving while capturing laser
scans. High fidelity transform works only correctly, if the target frame
is set to a fixed frame.

#### Subscribed Topics

\`scan\` (\<\<MsgLink(sensor_msgs/LaserScan)\>\>) The incoming laser
scan to filter.

#### Published Topics

\`cloud_filtered\` (\<\<MsgLink(sensor_msgs/PointCloud)\>\>) The
outgoing filtered point cloud.

#### Example Launch File

\`my_laser_cloud_filter.launch\`: ```
<launch>
  <node pkg="laser_filters" type="scan_to_cloud_filter_chain"
      name="tilt_shadow_filter">
    <rosparam command="load" file="$(find mypkg)/my_laser_config.yaml" />
    <rosparam command="load" file="$(find mypkg)/my_cloud_config.yaml" />
    <param name="high_fidelity" value="true" />
    <param name="target_frame" type="string" value="base_link" />
    <remap from="scan" to="tilt_scan" />
    <remap from="cloud_filtered" to="tilt_scan_cloud_filtered" />
  </node>
</launch>
```

\`my_laser_config.yaml\`: ```
scan_filter_chain:
- name: shadows
  type: laser_filters/ScanShadowsFilter
  params:
    min_angle: 10
    max_angle: 170
    neighbors: 20
    window: 1
- name: dark_shadows
  type: laser_filters/LaserScanIntensityFilter
  params:
    lower_threshold: 100
    upper_threshold: 10000
    disp_histogram: 0
```

\`my_cloud_config.yaml\`: ```
cloud_filter_chain:
- type: PR2PointCloudFootprintFilter
  name: footprint_filter
  params:
    inscribed_radius: 0.325
```

## Laser Filter Plugins

### LaserArrayFilter

This filter internally makes use of the the [filters](filters)
implementation of float-array filters. It extracts the range and
intensity values and treats each as an independent float array passed
through an internal filter chain.

#### Parameters

\`range_filter_chain\` (\`FilterChain\`) A nested filter chain
description, describing an appropriate chain of
\`MultiChannelMedianFilterFloat\` type filters.

\`intensity_filter_chain\` (\`FilterChain\`) A nested filter chain
description, describing an appropriate chain of
\`MultiChannelMedianFilterFloat\` type filters.

**Make sure to use both parameters ( *range_filter_chain* and
*intensity_filter_chain* ) **

#### Example Configuration

```
scan_filter_chain:
- type: laser_filters/LaserArrayFilter
  name: laser_median_filter
  params:
    range_filter_chain:
      - name: median_5
        type: filters/MultiChannelMedianFilterFloat
        params:
          number_of_observations: 5
          unused: 10
    intensity_filter_chain:
      - name: median_5
        type: filters/MultiChannelMedianFilterFloat
        params:
          number_of_observations: 5
          unused: 10
```

### ScanShadowsFilter

This filter removes laser readings that are most likely caused by the
veiling effect when the edge of an object is being scanned. For any two
points p_1 and p_2, we do this by computing the perpendicular angle. If
the perpendicular angle is less than a particular min or greater than a
particular max, we remove all neighbors further away than that point.

#### Parameters

\`min_angle\` (\`double\`) Minimum perpendicular angle (degrees)
\`max_angle\` (\`double\`) Maximum perpendicular angle (degrees)
\`window\` (\`int\`) Number of consecutive measurements to consider
angles inside of \`neighbors\` (\`int\`) Number of further-away
neighbors to remove

#### Example configuration

```
scan_filter_chain:
- name: shadows
  type: laser_filters/ScanShadowsFilter
  params:
    min_angle: 10
    max_angle: 170
    neighbors: 20
    window: 1
```

### InterpolationFilter

For any measurement in the scan which is invalid, the interpolation
comes up with a measurement which is an interpolation between the
surrounding good values.

#### Parameters

NONE

#### Example configuration

```
$ rosparam load my_laser_config.yaml scan_to_scan_filter_chain
```0

### LaserScanIntensityFilter

This filter removes all measurements from the
\<\<MsgLink(sensor_msgs/LaserScan)\>\> which have an intensity greater
than \`upper_threshold\` or less than \`lower_threshold\`. These points
are \"removed\" by setting the corresponding range value to
\`range_max\` + 1, which is assumed to be an error case.

#### Parameters

\`lower_threshold\` (\`double\`) Intensity value below which readings
will be dropped. \`upper_threshold\` (\`double\`) Intensity value above
which readings will be dropped. \`disp_histogram\` (\`int\`) Whether or
not to write an intensity histogram to standard out. (0 or 1)

#### Example configuration

```
$ rosparam load my_laser_config.yaml scan_to_scan_filter_chain
```1

### LaserScanRangeFilter

This filter removes all measurements from the
\<\<MsgLink(sensor_msgs/LaserScan)\>\> which are greater than
\`upper_threshold\` or less than \`lower_threshold\`. These points are
\"removed\" by setting the corresponding range value to \`NaN\`, which
is assumed to be an error case or
\`lower_replacement_value\`/\`upper_replacement_value\`. If
\`use_message_range_limits\` is true, the range within the laserscan
message is used.

#### Parameters

\`lower_threshold\` (\`double\`) Lower range threshold
\`upper_threshold\` (\`double\`) Upper range threshold
\`use_message_range_limits\` (\`bool\`) Use the \`range_min\` and
\`range_max\` values from the laserscan message as threshold. Defaults
to \`false\` \`lower_replacement_value\` (\`double\`) Use this value for
all measurements \<\`lower_threshold\`. Default: \`NaN\`
\`upper_replacement_value\` (\`double\`) Use this value for all
measurements \>\`upper_threshold\`. Default: \`NaN\`

#### Example configuration

```
$ rosparam load my_laser_config.yaml scan_to_scan_filter_chain
```2

### LaserScanAngularBoundsFilter

This filter removes points in a \<\<MsgLink(sensor_msgs/LaserScan)\>\>
outside of certain angular bounds by changing the minimum and maximum
angle.

#### Parameters

\`lower_angle\` (\`double\`) Minimum angle (radians) \`upper_angle\`
(\`double\`) Maximum angle (radians)

#### Example configuration

```
$ rosparam load my_laser_config.yaml scan_to_scan_filter_chain
```3

### LaserScanAngularBoundsFilterInPlace

This filter removes points in a \<\<MsgLink(sensor_msgs/LaserScan)\>\>
inside of certain angular bounds. These points are \"removed\" by
setting the corresponding range value to \`range_max\` + 1, which is
assumed to be an error case.

#### Parameters

\`lower_angle\` (\`double\`) Minimum angle (radians) \`upper_angle\`
(\`double\`) Maximum angle (radians)

#### Example configuration

```
$ rosparam load my_laser_config.yaml scan_to_scan_filter_chain
```4

### LaserScanBoxFilter

This filter removes points in a \<\<MsgLink(sensor_msgs/LaserScan)\>\>
inside of a cartesian box. These points are \"removed\" by setting the
corresponding range value to NaN which is assumed to be an error case.

#### Parameters

\`box_frame\` (\`string\`) [tf](tf) frame_id \`min_x\` (\`double\`)
Minimum cartesian x \`max_x\` (\`double\`) Maximum cartesian x \`min_y\`
(\`double\`) Minimum cartesian y \`max_y\` (\`double\`) Maximum
cartesian y \`min_z\` (\`double\`) Minimum cartesian z \`max_z\`
(\`double\`) Maximum cartesian z

#### Example configuration

```
$ rosparam load my_laser_config.yaml scan_to_scan_filter_chain
```5

### LaserScanSpeckleFilter

This filter removes outliers in a
\<\<MsgLink(sensor_msgs/LaserScan)\>\>. There are two filter methods
that are available for this filter.

These points are \"removed\" by setting the corresponding range value to
NaN.

#### Parameters

\`filter_type\` (\`int\`) Filtering method selection

-   0: Range based filtering (distance between consecutive points)
-   1: Euclidean filtering based on radius outlier search \`max_range\`
    (\`double\`) Only ranges smaller than this range are taken into
    account \`max_range_difference\` (\`double\`) Distance: max distance
    between consecutive points - RadiusOutlier: max distance between
    points \`filter_window\` (\`double\`) Minimum number of neighbors

#### Example configuration

```
$ rosparam load my_laser_config.yaml scan_to_scan_filter_chain
```6
