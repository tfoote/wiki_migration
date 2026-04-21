See <http://rc-visard.com> and <http://doc.rc-visard.com> for more
details.

```wiki
'''This package is not developed anymore'''. A new clients is available in the
[[rc_reason_clients]] package.
```

## Overview

The [SilhouetteMatch](https://roboception.com/product/silhouettematch/)
component is an optional on-board component of the rc_visard, which
detects objects by matching a predefined silhouette ("template") to
edges in an image.

For detail description check the following link:
<https://doc.rc-visard.com/latest/en/silhouettematch.html>

## Configuration

### Parameters

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

```{=html}
<!-- -->
```
-   \`host\`: If \`device\` is not used. The IP address or hostname of
    the rc_visard.

### Dynamic reconfigure parameters

-   \`max_number_of_detected_objects\`: Maximum number of detected
    objects.
-   \`edge_sensitivity\`: Sensitivity of the edge detector.
-   \`match_max_distance\`: Maximum allowed distance in pixels between
    the template and the detected edges in the image.
-   \`match_percentile\`: Percentage of template pixels that must be
    within the maximum distance to successfully match the template.
-   \`quality\`: Detection quality (H(igh), M(edium), or L(ow)).
-   \`publish_vis\`: Whether TF and markers should be published.

### Services

The following services are offered by the node:

-   \`detect_object\`: Triggers detection of an object.
-   \`calibrate_base_plane\`: Triggers base-plane calibration.
-   \`get_base_plane_calibration\`: Returns the configured base-plane
    calibration.
-   \`delete_base_plane_calibration\`: Deletes the configured base-plane
    calibration.

## Launch

Using command line parameters:

```bash
rosrun rc_silhouettematch_client rc_silhouettematch_client _device:=:<serial_number>
```

## Report a Bug

\<\<GitHubIssues(roboception/rc_visard_ros)\>\>

## Acknowledgements

[Included page rosin/acknowledgement not found](Included page rosin/acknowledgement not found)
