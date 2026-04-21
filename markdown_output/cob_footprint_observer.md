The \`cob_footprint_observer\` observes the setup of the Care-O-Bot
(including arm and tray) and inflates the footprint to contain the arm
and the tray. It allows for reading the adjusted footprint using either
the \`GetFootprint\` service or the published \`adjusted_footprint\`
topic.

**Note:** The \`cob_footprint_observer\` only works with rectangular
footprints.

## Hardware Requirements

To use this package you need either need a real or a simulated
Care-O-Bot (see [cob_bringup](cob_bringup) and
[cob_bringup_sim](cob_bringup_sim) respectively).

## ROS API

The [cob_footprint_observer](cob_footprint_observer) package provides a
configurable node for checking and adjusting the footprint based on the
current setup. ```clearsilver
 name = cob_footprint_observer
 desc = The `cob_footprint_observer` node uses a `tf::TransformListener` to check the transformations for desired frames and adjusts the footprint accordingly. It publishes the adjusted footprint as a [[Topics|topic]] and sets the footprint using a [[Services|service]].

goal{
}

result{
}

feedback{
}

sub{
}

pub{
 0.name = adjusted_footprint
 0.type = geometry_msgs/PolygonStamped
 0.desc = Publishes the adjusted footprint of the robot.
}

srv{
 0.name = /get_footprint
 0.type = cob_footprint_observer/GetFootprint
 0.desc = Responds with the adjusted footprint.
}

param{
 0.name = ~footprint_source
 0.type = string
 0.default = "/local_costmap_node/costmap"
 0.desc = Specifies which node to search for the initial footprint, e.g. /local_costmap_node/costmap.

 1.name = ~frames_to_check
 1.type = string
 1.default = ""
 1.desc = Frames which should be checked for footprint adjustment (separated by spaces), e.g. /base_link /sdh_tip_link /arm_4_link.

 2.name = ~robot_base_frame
 2.type = string
 2.default = "/base_link"
 2.desc = Specifies the robot base frame, e.g. /base_link.

}

req_tf{
}

prov_tf{
}
```

## Usage/Examples

This package is not intended to be used directly, but with the
corresponding launch and yaml files. For starting the footprint observer
with the \`collision_velocity_filter\` use ```
roslaunch cob_bringup base_collision_observer.launch
``` For
including the footprint observer in your overall launch file use
```
<!-- start footprint observer node -->
<node pkg="cob_footprint_observer" type="footprint_observer" name="footprint_observer" output="screen">
  <!-- load parameter file -->
  <rosparam file="$(find cob_hardware_config)/$(env ROBOT)/config/footprint_observer_params.yaml" command="load" />
</node>
``` A sample parameter file could look like this
```
# node from which initial footprint is read
footprint_source: /local_costmap_node/costmap

# 
robot_base_frame: /base_link
# frames to check for footprint adjustment
frames_to_check: /sdh_tip_link /arm_6_link /arm_4_link
```
