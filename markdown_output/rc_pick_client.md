See <http://rc-visard.com> and <http://doc.rc-visard.com> for more
details.

```wiki
'''This package is not developed anymore'''. New clients are available in the
[[rc_reason_clients]] package.
```

## Overview

The components provide out-of-the-box perception solutions for robotic
pick-and-place applications.
[ItemPick](https://roboception.com/product/itempick/) targets the
detection of flat surfaces of unknown objects for picking with a suction
gripper. [BoxPick](https://roboception.com/product/boxpick/) detects
rectangular surfaces and determines their position, orientation and size
for grasping. The interface of both components is very similar.
Therefore both components are described together in this chapter.

For detail description of the modules check the following link:
<https://doc.rc-visard.com/latest/en/itempick.html>

## Configuration

### Parameters

-   \`host\`: The IP address or hostname of the rc_visard that should be
    calibrated.

\'\'\'Since version 2.7, the device ID can be used instead of the
sensor\'s IP address:\'\'\'

-   \`device\`: The ID of the device, i.e. Roboception rc_visard sensor.
    This can be either:

```{=html}
<!-- -->
```
-   serial number, e.g. \`02912345\`. ```wiki
Preceed with a colon (`:02912345`) when passing this on the commandline or setting it via rosparam (see https://github.com/ros/ros_comm/issues/1339). This is not neccessary when specifying it as a string in a launch file.
```

```{=html}
<!-- -->
```
-   user defined name must be unique among all reachable sensors. If no
    device or host is given, this parameter works if just one rc_visard
    is connected.

### Dynamic reconfigure parameters

The following parameters are available for the
[ItemPick](https://roboception.com/product/itempick/) and
[BoxPick](https://roboception.com/product/boxpick/) modules:

-   \`max_grasps\`: Maximum number of provided grasps.
-   \`cluster_max_curvature\`: Maximum curvature allowed within one
    cluster. The smaller this value, the more clusters will be split
    apart.
-   \`clustering_max_surface_rmse\`: Maximum root-mean-square error
    (RMSE) in meters of points belonging to a surface.
-   \`clustering_discontinuity_factor\`: Factor used to discriminate
    depth discontinuities within a patch. The smaller this value, the
    more clusters will be split apart.

For the [ItemPick](https://roboception.com/product/itempick/) module,
two additional parameters are available:

-   \`cluster_max_dimension\`: Indicates how much the estimated load
    carrier dimensions are allowed to differ from the load carrier model
    dimensions in meters.
-   \`clustering_patch_size\`: Size in pixels of the square patches the
    depth map is subdivided into during the first clustering step.

### Services

The following services are offered by the nodes:

-   \`compute_grasps\`: Triggers the computation of grasping poses for a
    suction device. All images used by the node are guaranteed to be
    newer than the service trigger time.

The [BoxPick](https://roboception.com/product/boxpick/) node offers an
additional service:

-   \`detect_items\`: Triggers the detection of rectangles.

## Launch

Using command line parameters:

For the [ItemPick](https://roboception.com/product/itempick/) module:
```bash
$ rosrun rc_pick_client rc_itempick_client_node _host:=<sensor_ip>
```

Since version 2.7: ```bash
rosrun rc_pick_client rc_itempick_client_node _device:=:<serial_number>
```

For the [BoxPick](https://roboception.com/product/boxpick/) module:
```bash
$ rosrun rc_pick_client rc_boxpick_client_node _host:=<sensor_ip>
```

Since version 2.7: ```bash
rosrun rc_pick_client rc_boxpick_client_node _device:=:<serial_number>
```

## Report a Bug

\<\<GitHubIssues(roboception/rc_visard_ros)\>\>

## Acknowledgements

\<\<Include(rosin/acknowledgement)\>\>
