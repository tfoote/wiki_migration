## Overview

The primary content of the `laser_filters` package is a number of
general purpose filters for processing
[sensor_msgs/msg/LaserScan](https://docs.ros.org/en/rolling/p/sensor_msgs/msg/LaserScan.html)
messages. These filters are exported as plugins designed to work with
with the [filters package](https://index.ros.org/p/filters). At the
moment all of these filters run directly on
[sensor_msgs/msg/LaserScan](https://docs.ros.org/en/rolling/p/sensor_msgs/msg/LaserScan.html),
but filters may be added in the future which process
[sensor_msgs/msg/PointCloud](https://docs.ros.org/en/rolling/p/sensor_msgs/msg/PointCloud.html)
instead. Please review the
[filters documentation](https://index.ros.org/p/filters) for an overview
of how filters and filter chains are intended to work.

This package provides two nodes that can run multiple filters
internally. Using these nodes to run your filters is considered best
practice, since it allows multiple nodes to consume the output while
only performing the filtering computation once. The nodes are minimal
wrappers around filter chains of the given type. The
[scan_to_scan_filter_chain](#scan_to_scan_filter_chain)
applies a series of filters to a
[sensor_msgs/msg/LaserScan](https://docs.ros.org/en/rolling/p/sensor_msgs/msg/LaserScan.html).
The
[scan_to_cloud_filter_chain](#scan_to_cloud_filter_chain)
first applies a series of filters to a
[sensor_msgs/msg/LaserScan](https://docs.ros.org/en/rolling/p/sensor_msgs/msg/LaserScan.html),
transforms it into a
[sensor_msgs/msg/PointCloud](https://docs.ros.org/en/rolling/p/sensor_msgs/msg/PointCloud.html),
and then applies a series of filters to the
[sensor_msgs/msg/PointCloud](https://docs.ros.org/en/rolling/p/sensor_msgs/msg/PointCloud.html).

## Using Laser Filters

Each [ laser filter](#plugins) is a separate
plugin exported by the laser_filters package. This allows them to be
specified in a configuration file which can be loaded into an arbitrary
filter_chain templated on a
[sensor_msgs/msg/LaserScan](https://docs.ros.org/en/rolling/p/sensor_msgs/msg/LaserScan.html).
You can instantiate a laser filter into a filter_chain in C++
([example](#laser-filtering-in-c)),
or you can use the
[ scan_to_scan_filter_chain](#scan_to_scan_filter_chain)
and
[ scan_to_cloud_filter_chain](#scan_to_cloud_filter_chain)
nodes which contain appropriate filter chains internally
([example](#using-the-laser-filtering-nodes)).

[ Filter chains](https://index.ros.org/p/filters) are configured from
the parameter server. They expect a parameter which is a list made up of
repeating blocks of filter configurations. These should almost always be
specified in a `.yaml` file to be pushed to the parameter server. Each
filter specified in the chain will be applied in order.

The individual filters configurations contain a `name` which is used
for debugging purposes, a `type` which is used to locate the plugin,
and a `params` which is a dictionary of additional variables. Consult
the documentation for the particular filter plugin to see what variables
may be set in the params field.

**Note** that the `type` should be specified as
`pkg_name/FilterClass` as the
[matching behavior of the filters implementation before lunar](https://github.com/ros/filters/issues/14)
is
[not necessarily matching the exact name](https://github.com/ros-perception/laser_filters/issues/50),
if only the `FilterClass` is used.

For example, in a package, `mypkg`, to launch a
[ scan_to_scan_filter_chain](#scan_to_scan_filter_chain)
with two filters: `LaserFilterClass1` and `LaserFilterClass2`, you
could use the file:

`my_laser_config.yaml`: 

```yaml
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
[rosparam](https://index.ros.org/p/rosparam) by running:


```
$ rosparam load my_laser_config.yaml scan_to_scan_filter_chain
```



And then launching the `scan_to_scan_filter_chain`:


```
$ rosrun laser_filters scan_to_scan_filter_chain
```



## Laser Filter Nodes

<a id="scan_to_scan_filter_chain"></a>

### scan_to_scan_filter_chain (new in laser_pipeline-0.5)

The scan_to_scan_filter_chain is a very minimal node which wraps an
instance of a `filters::FilterChain<sensor_msgs::LaserScan>`. This
node can be used to run any filter in this package on an incoming laser
scan. If the `tf_message_filter_target_frame` parameter is set, it
will wait for the transform between the laser and the target_frame to be
available before running the filter chain.

![attachment:scan_to_scan_filter_chain.png](doc/scan_to_scan_filter_chain.png)

#### ROS Parameters

`scan_filter_chain` (list) **\[Required\]** The list of laser filters
to load.

`tf_message_filter_target_frame` (string) A target_frame for which a
transform must exist at the current time before the filter_chain will be
executed. This is the target_frame internally passed to the
`tf::MessageFilter`. If this parameter is not set, the chain will
simply be executed immediately upon the arrival of each new scan.

#### Subscribed Topics

`scan`
([sensor_msgs/msg/LaserScan](https://docs.ros.org/en/rolling/p/sensor_msgs/msg/LaserScan.html))
The incoming laser scan to filter

#### Published Topics

`scan_filtered`
([sensor_msgs/msg/LaserScan](https://docs.ros.org/en/rolling/p/sensor_msgs/msg/LaserScan.html))
The outgoing filtered laser scan

#### Example Launch File

`my_laser_filter.launch`: 

```
<launch>
  <node pkg="laser_filters" type="scan_to_scan_filter_chain"
      name="laser_filter">
    <rosparam command="load" file="$(find mypkg)/my_laser_config.yaml" />
    <remap from="scan" to="base_scan" />
  </node>
</launch>
```



`my_laser_config.yaml`: 

```
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



<a id="scan_to_cloud_filter_chain"></a>

### scan_to_cloud_filter_chain

The scan_to_cloud_filter_chain is a very minimal node which wraps an
instances of `filters::FilterChain<sensor_msgs::LaserScan>` and
`filters::FilterChain<sensor_msgs::PointCloud>`. This node can be
used to run any filter in this package on an incoming laser scan. After
performing the laser filtering, it will use the `LaserProjection` from
[laser_geometry](https://index.ros.org/p/laser_geometry) to transform
each scan into a point cloud. It will then run any cloud-based
filtering, and finally publish the resultant cloud.

![attachment:scan_to_cloud_filter_chain.png](doc/scan_to_cloud_filter_chain.png)

#### ROS Parameters

`scan_filter_chain` (list) **\[Required\]** The list of laser filters
to load. `cloud_filter_chain` (list) **\[Required\]** The list of
cloud filters to load. `target_frame` (string) **\[Required\]** The
frame to transform the point_cloud into. `high_fidelity` (bool,
default: false) Whether to perform a high fidelity transform. This
approach assumes that the laser scanner is moving while capturing laser
scans. High fidelity transform works only correctly, if the target frame
is set to a fixed frame.

#### Subscribed Topics

`scan`
([sensor_msgs/msg/LaserScan](https://docs.ros.org/en/rolling/p/sensor_msgs/msg/LaserScan.html))
The incoming laser scan to filter.

#### Published Topics

`cloud_filtered`
([sensor_msgs/msg/PointCloud](https://docs.ros.org/en/rolling/p/sensor_msgs/msg/PointCloud.html))
The outgoing filtered point cloud.

#### Example Launch File

`my_laser_cloud_filter.launch`: 

```
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



`my_laser_config.yaml`: 

```
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



`my_cloud_config.yaml`: 

```
cloud_filter_chain:
- type: PR2PointCloudFootprintFilter
  name: footprint_filter
  params:
    inscribed_radius: 0.325
```



<a id="plugins"></a>

## Laser Filter Plugins

### LaserArrayFilter

This filter internally makes use of the the
[filters](https://index.ros.org/p/filters) implementation of float-array
filters. It extracts the range and intensity values and treats each as
an independent float array passed through an internal filter chain.

#### Parameters

`range_filter_chain` (`FilterChain`) A nested filter chain
description, describing an appropriate chain of
`MultiChannelMedianFilterFloat` type filters.

`intensity_filter_chain` (`FilterChain`) A nested filter chain
description, describing an appropriate chain of
`MultiChannelMedianFilterFloat` type filters.

**Make sure to use both parameters ( *range_filter_chain* and
*intensity_filter_chain* )**

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

`min_angle` (`double`) Minimum perpendicular angle (degrees)
`max_angle` (`double`) Maximum perpendicular angle (degrees)
`window` (`int`) Number of consecutive measurements to consider
angles inside of `neighbors` (`int`) Number of further-away
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
scan_filter_chain:
- name: interpolation
  type: laser_filters/InterpolationFilter
```



### LaserScanIntensityFilter

This filter removes all measurements from the
[sensor_msgs/msg/LaserScan](https://docs.ros.org/en/rolling/p/sensor_msgs/msg/LaserScan.html)
which have an intensity greater than `upper_threshold` or less than
`lower_threshold`. These points are "removed" by setting the
corresponding range value to `range_max` + 1, which is assumed to be
an error case.

#### Parameters

`lower_threshold` (`double`) Intensity value below which readings
will be dropped. `upper_threshold` (`double`) Intensity value above
which readings will be dropped. `disp_histogram` (`int`) Whether or
not to write an intensity histogram to standard out. (0 or 1)

#### Example configuration



```
scan_filter_chain:
- name: intensity
  type: laser_filters/LaserScanIntensityFilter
  params:
    lower_threshold: 8000
    upper_threshold: 100000
    disp_histogram: 0
```



### LaserScanRangeFilter

This filter removes all measurements from the
[sensor_msgs/msg/LaserScan](https://docs.ros.org/en/rolling/p/sensor_msgs/msg/LaserScan.html)
which are greater than `upper_threshold` or less than
`lower_threshold`. These points are "removed" by setting the
corresponding range value to `NaN`, which is assumed to be an error
case or `lower_replacement_value`/`upper_replacement_value`. If
`use_message_range_limits` is true, the range within the laserscan
message is used.

#### Parameters

`lower_threshold` (`double`) Lower range threshold
`upper_threshold` (`double`) Upper range threshold
`use_message_range_limits` (`bool`) Use the `range_min` and
`range_max` values from the laserscan message as threshold. Defaults
to `false` `lower_replacement_value` (`double`) Use this value for
all measurements <`lower_threshold`. Default: `NaN`
`upper_replacement_value` (`double`) Use this value for all
measurements >`upper_threshold`. Default: `NaN`

#### Example configuration



```
scan_filter_chain:
- name: range
  type: laser_filters/LaserScanRangeFilter
  params:
    use_message_range_limits: false
    lower_threshold: 0.3
    upper_threshold: .inf
    lower_replacement_value: -.inf
    upper_replacement_value: .inf
```



### LaserScanAngularBoundsFilter

This filter removes points in a
[sensor_msgs/msg/LaserScan](https://docs.ros.org/en/rolling/p/sensor_msgs/msg/LaserScan.html)
outside of certain angular bounds by changing the minimum and maximum
angle.

#### Parameters

`lower_angle` (`double`) Minimum angle (radians) `upper_angle`
(`double`) Maximum angle (radians)

#### Example configuration



```
scan_filter_chain:
- name: angle
  type: laser_filters/LaserScanAngularBoundsFilter
  params:
    lower_angle: -1.57
    upper_angle: 1.57
```



### LaserScanAngularBoundsFilterInPlace

This filter removes points in a
[sensor_msgs/msg/LaserScan](https://docs.ros.org/en/rolling/p/sensor_msgs/msg/LaserScan.html)
inside of certain angular bounds. These points are "removed" by
setting the corresponding range value to `range_max` + 1, which is
assumed to be an error case.

#### Parameters

`lower_angle` (`double`) Minimum angle (radians) `upper_angle`
(`double`) Maximum angle (radians)

#### Example configuration



```
scan_filter_chain:
- name: angle
  type: laser_filters/LaserScanAngularBoundsFilterInPlace
  params:
    lower_angle: 0.685398163
    upper_angle: 0.885398163
```



### LaserScanBoxFilter

This filter removes points in a
[sensor_msgs/msg/LaserScan](https://docs.ros.org/en/rolling/p/sensor_msgs/msg/LaserScan.html)
inside of a cartesian box. These points are "removed" by setting the
corresponding range value to NaN which is assumed to be an error case.

#### Parameters

`box_frame` (`string`) [tf](https://index.ros.org/p/tf) frame_id
`min_x` (`double`) Minimum cartesian x `max_x` (`double`)
Maximum cartesian x `min_y` (`double`) Minimum cartesian y `max_y`
(`double`) Maximum cartesian y `min_z` (`double`) Minimum
cartesian z `max_z` (`double`) Maximum cartesian z

#### Example configuration



```
scan_filter_chain:
- name: box
  type: laser_filters/LaserScanBoxFilter
  params:
    box_frame: scan_link
    min_x: -1.0
    max_x: 1.0
    min_y: -1.0
    max_y: 1.0
    min_z: -1.0
    max_z: 1.0
```



### LaserScanSpeckleFilter

This filter removes outliers in a
[sensor_msgs/msg/LaserScan](https://docs.ros.org/en/rolling/p/sensor_msgs/msg/LaserScan.html).
There are two filter methods that are available for this filter.

These points are "removed" by setting the corresponding range value to
NaN.

#### Parameters

`filter_type` (`int`) Filtering method selection

- 0: Range based filtering (distance between consecutive points)
- 1: Euclidean filtering based on radius outlier search `max_range`
  (`double`) Only ranges smaller than this range are taken into
  account `max_range_difference` (`double`) Distance: max distance
  between consecutive points - RadiusOutlier: max distance between
  points `filter_window` (`double`) Minimum number of neighbors

#### Example configuration



```
scan_filter_chain:
- name: speckle_filter
  type: laser_filters/LaserScanSpeckleFilter
  params:
    filter_type: 0
    max_range: 2.0
    max_range_difference: 0.1
    filter_window: 2
```

## Laser filtering in C++

Let's take a look at `generic_laser_filter_node.cpp` to see how to
run a set of filters from within a node:



```cplusplus
#include "ros/ros.h"
#include "sensor_msgs/LaserScan.h"
#include "message_filters/subscriber.h"
#include "tf/message_filter.h"
#include "tf/transform_listener.h"
#include "filters/filter_chain.h"

class GenericLaserScanFilterNode
{
protected:
  // Our NodeHandle
  ros::NodeHandle nh_;

  // Components for tf::MessageFilter
  tf::TransformListener tf_;
  message_filters::Subscriber<sensor_msgs::LaserScan> scan_sub_;
  tf::MessageFilter<sensor_msgs::LaserScan> tf_filter_;

  // Filter Chain
  filters::FilterChain<sensor_msgs::LaserScan> filter_chain_;

  // Components for publishing
  sensor_msgs::LaserScan msg_;
  ros::Publisher output_pub_;

public:
  // Constructor
  GenericLaserScanFilterNode() :
      scan_sub_(nh_, "scan_in", 50),
      tf_filter_(scan_sub_, tf_, "base_link", 50),
      filter_chain_("sensor_msgs::LaserScan")
  {
    // Configure filter chain
    filter_chain_.configure("~");

    // Setup tf::MessageFilter for input
    tf_filter_.registerCallback(
        boost::bind(&GenericLaserScanFilterNode::callback, this, _1));
    tf_filter_.setTolerance(ros::Duration(0.03));

    // Advertise output
    output_pub_ = nh_.advertise<sensor_msgs::LaserScan>("output", 1000);
  }

  // Callback
  void callback(const sensor_msgs::LaserScan::ConstPtr& msg_in)
  {
    // Run the filter chain
    filter_chain_.update (*msg_in, msg_);

    // Publish the output
    output_pub_.publish(msg_);
  }
};

int main(int argc, char **argv)
{
  ros::init(argc, argv, "scan_filter_node");

  GenericLaserScanFilterNode t;
  ros::spin();

  return 0;
}
```



As we can see from this node, a series of filters is called a
`filter_chain` and running a filter chain on a laser scan only
involves 4 lines of code: Declare a filter chain templated to run on
laser scans. Construct a filter chain, telling it the type of filters
that will be loaded ("sensor_msgs::LaserScan" \-- this always must be
the same as the templated type). Tell the filter chain to read its
configuration (always named "filter_chain") from our private
namespace. Call the `update` function to filter the scan.

Now you can use the filtered scan in your own node.

## Using the laser filtering nodes

The laser filters package provides nodes
that can run multiple filters internally. These nodes are useful if you
want to do all the laser filtering in your system only once, and then
let multiple other nodes use the result. This tutorial provides an
example of how to use the
[scan_to_scan_filter_chain](#scan_to_scan_filter_chain)
node.

### Data

As in the
[introduction to using laser scanners tutorial](https://index.ros.org/p/laser_pipeline),
you can try the tools in this tutorial on the bag found
[here](http://media.willowgarage.com/media/index/wiki_docs/laser_tutorials/laser.bag)
(save link as\...).

### Filtering a Scan: The Scan Shadows Filter

Laser scans sometimes hit objects at a grazing angle, resulting in
"split pixels" or "shadows". These laser hits show up in the scan as
single points in the middle of space, part-way between the object they
grazed and a background object. For many tasks such as object model
fitting, these points are simply noise and should be removed by using
the scan shadows filter.

Filters can be applied to a laser scan in three ways: through calling
the
generic_laser_filter_node
which applies the filter and then publishes the filtered scan, by
including the code in your own node, or through the
[laser scan assembler](https://index.ros.org/p/laser_assembler). As
always, the choice between filtering in a generic node versus within the
node that will use the filtered scan is based on efficiency in your
particular system set up.

The file `shadow_filter_example.launch` in the
laser_filters package (`examples`
folder) provides an example of calling the scan shadows filter as a node
on the scan topic `base_scan`: 

```
<launch>
<node pkg="laser_filters" type="scan_to_scan_filter_chain" output="screen" name="laser_filter">
      <remap from="scan" to="base_scan" />
      <rosparam command="load" file="$(find laser_filters)/examples/shadow_filter_example.yaml" />
</node>
</launch>
```

 The launch
file above refers to the following
`laser_filters/examples/shadow_filters_example.yaml` file:


```
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

 As this example shows,
[filters](https://index.ros.org/p/filters) are defined in the
`filters` tag. Each filter has a filter type and a name that
differentiates it from filters of the same type. This particular example
runs two filters, first the `ScanShadowsFilter` which removes shadow
hits, and then the `LaserScanIntensityFilter` with parameters set to
remove any hits with very low or very high intensity.

#### Exercise

Try creating a node and launch file that:

- filter an incoming laser scanner data stream using the filters in
  shadow_filters_example.xml, and
- listen to the resulting filtered laser scan, convert it into a point
  cloud in the `base_link` frame and publish the cloud. (Recall that
  you completed the second step in the previous tutorial:
  [introduction to using laser scanners tutorial](https://index.ros.org/p/laser_pipeline).)

Visualize the output of your node in rviz.

### All in One Node: scan_to_cloud_filter_chain

The above exercise is so useful it's already been written up as one
node. The `scan_to_cloud_filter_chain` node in the `laser_filters`
package listens to a laser scan stream, applies the above filters, and
outputs the result as a cloud.

IMPORTANT: scan_to_cloud_filter_chain has a parameter, use_hack, that
defaults to true. If it is set to true, the resulting cloud will be
offset slightly to "correct for incident angles", which is apparently
very useful for navigation and using laser clouds at longer distances.
If you are using the laser cloud at close ranges, i.e., for
manipulation, you should set this parameter to be false, or your robot
is likely to thwack into things.

Try running the `scan_to_cloud_filter_chain` on the `/base_scan`
topic and visualize the resulting point cloud.

## Tutorials

- [Laser filtering in C++](#laser-filtering-in-c):
  Raw laser scans contain all points returned from the scanner without
  processing. Many applications, however, are better served by filtered
  scans which remove unnecessary points (such as unreliable laser hits
  or hits on the robot itself), or pre-process the scans in some way
  (such as by median filtering). This tutorial will teach you how to
  apply pre-existing filters to laser scans.
- [Using the laser filtering nodes](#using-the-laser-filtering-nodes):
  Raw laser scans contain all points returned from the scanner without
  processing. Many applications, however, are better served by filtered
  scans which remove unnecessary points (such as unreliable laser hits
  or hits on the robot itself), or pre-process the scans in some way
  (such as by median filtering). This tutorial will teach you how to
  apply pre-existing filters to laser scans.

## Troubleshooting

### Reporting Errors

If you encounter a problem that isn't addressed on this page, please
[file a ticket](https://code.ros.org/trac/ros-pkg/newticket?component=laser_pipeline&keywords=laser_filters&owner=tfoote)

The current list of open issues is available on
[trac](https://code.ros.org/trac/ros-pkg/query?status=assigned&status=new&status=reopened&group=milestone&order=priority&col=id&col=summary&col=status&col=type&col=priority&col=milestone&col=component&keywords=~laser_filters)

### Common Problems When Using Package

(There are currently no recorded commonly occurring errors)
