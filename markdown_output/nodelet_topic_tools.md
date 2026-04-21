The `nodelet_topic_tools` package contains a MUX (`NodeletMUX`) and
a DEMUX (`NodeletDEMUX`) nodelet.

## MUX

`NodeletMUX` represent a mux nodelet for topics: it takes N (<=8)
input topics, and publishes all of them on one output topic. One
implementation of `NodeletMUX` can be found in [pcl_ros](pcl_ros).

Usage example: ```xml
  <node pkg="nodelet" type="nodelet" name="pcl_manager" args="manager" output="screen" />
  <!-- MUX the data onto one topic -->
  <node pkg="nodelet" type="nodelet" name="data_mux" args="load pcl/NodeletMUX pcl_manager" output="screen">
    <rosparam>
      input_topics: [/passthrough/output, /normal_estimation/output]
    </rosparam>
  </node>
```

The above accepts data from `/passthrough/output` and
`/normal_estimation/output`, and republishes it on
`/data_mux/output`.

To compile the `NodeletMUX` nodelet in your library, add something
like: ```cplusplus
typedef nodelet::NodeletMUX<sensor_msgs::PointCloud2, message_filters::Subscriber<sensor_msgs::PointCloud2> > NodeletMUX;
PLUGINLIB_DECLARE_CLASS (pcl, NodeletMUX, NodeletMUX, nodelet::Nodelet);
```

(replace `sensor_msgs::PointCloud2` with the message type of choice).

## DEMUX

`NodeletDEMUX` represent a demux nodelet for topics: it takes 1 input
topic, and publishes on N (<=8) output topics. One implementation of
`NodeletDEMUX` can be found in [pcl_ros](pcl_ros).

Usage example: ```xml
  <node pkg="nodelet" type="nodelet" name="pcl_manager" args="manager" output="screen" />
  <!-- MUX the data onto one topic -->
  <node pkg="nodelet" type="nodelet" name="data_demux" args="load pcl/NodeletDEMUX pcl_manager" output="screen">
    <rosparam>
      output_topics: [/output1, /output2]
    </rosparam>
  </node>
```

The above accepts data from `/data_demux/input`, and republishes it on
`/data_demux/output1` and `/data_demux/output2`.

To compile the `NodeletDEMUX` nodelet in your library, add something
like: ```cplusplus
typedef nodelet::NodeletDEMUX<sensor_msgs::PointCloud2> NodeletDEMUX;
PLUGINLIB_DECLARE_CLASS (pcl, NodeletDEMUX, NodeletDEMUX, nodelet::Nodelet);
```

(replace `sensor_msgs::PointCloud2` with the message type of choice).

## Throttle

`NodeletThrottle` can throttle a topic in a nodelet to a specified
rate. Note that this tool is in the `nodelet_topic_tools` namespace.

Usage example: ```xml
  <node pkg="nodelet" type="nodelet" name="nodelet_manager" args="manager" output="screen" />

  <node pkg="nodelet" type="nodelet" name="data_throttle" args="load my_pkg/NodeletThrottleImage nodelet_manager" output="screen">
    <remap from="topic_in"  to="camera/rgb/image_color"/>
    <remap from="topic_out" to="camera/rgb/image_color_throttle"/>
  </node>
```

To compile the `NodeletThrottle` nodelet in your library, add
something like: ```cplusplus
#include <nodelet_topic_tools/nodelet_throttle.h>
#include <sensor_msgs/Image.h>
#include <pluginlib/class_list_macros.h>

typedef nodelet_topic_tools::NodeletThrottle<sensor_msgs::Image> NodeletThrottleImage;
PLUGINLIB_DECLARE_CLASS (my_pkg, NodeletThrottleImage, NodeletThrottleImage, nodelet::Nodelet);
```

(replace `sensor_msgs::Image` with the message type of choice).
