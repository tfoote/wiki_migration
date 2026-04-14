## Introduction

To run this node, you need to have the
[sr_hand](sr_hand/Tutorials/Getting Started: running the hand and arm interface)
and the [cyberglove](cyberglove) node running. You can then run:
```
$ roslaunch sr_remappers remapper_glove.launch
```

It will remap the calibrated data coming from the cyberglove to the
targets of the hand.

This node subscribe to the specified
[sensor_msgs](sensor_msgs)/joint_states topic, and publishes a remapped
vector on the specified sendupdate topic. It simply multiplies the input
vector by a mapping matrix which is loaded into the parameter server by
the \'\'\'remapper_glove.launch\'\'\' file.

You can find the default mapping matrix in
[sr_control_gui](sr_control_gui)/param/GloveToHandMappings_generic.

## ROS API

### Subscribed Topics

-   \'\'\'{cyberglove_prefix}/calibrated/joint_states\'\'\': Subscribes
    to the calibrated data coming from the Cyberglove.
    \'\'\'{cyberglove_prefix}\'\'\' is defined in the parameters.

### Published Topics

-   \'\'\'{sendupdate_prefix}/sendupdate\'\'\': Publishes the targets to
    this topic, where \'\'\'{sendupdate_prefix}\'\'\' is defined in the
    parameters.

### Parameters

-   \'\'\'cyberglove_prefix\'\'\': The prefix on which the Cyberglove
    published data, generally \'\'\'/cyberglove\'\'\'.
-   \'\'\'sendupdate_prefix\'\'\': The prefix on which the robot listens
    for targets, generally \'\'\'/srh\'\'\'
-   \'\'\'cyberglove_mapping_path\'\'\': The path to the file containing
    the mapping matrix.

## Internal Mechanics

The current default matrix is not optimal at all. The mapping from the
Cyberglove to the Dexterous Hand is not a trivial task. There\'s some
research being done on it, and we developed a mapping process using a
simplex algorithm but it\'s in a very alpha stage and not yet released.
