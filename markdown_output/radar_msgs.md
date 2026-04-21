## Purpose

To supplement the messages provided in [sensor_msgs](sensor_msgs) with a
set of radar-specific messages.

## Types of Messages

The types of messages provided in this package are mostly broken down
into three categories:

1\. Detections - These are un-tracked returns from the radar which
provide estimates of only position and velocity measurements in the X
and Y planes as well as the return's amplitude. 2. Tracks - These are
aggregated objects fused and filtered from several detections. These
provide not only the estimated size and shape of the track (represented
as a
[geometry_msgs/Polygon](http://docs.ros.org/melodic/api/geometry_msgs/html/msg/Polygon.html)),
the track's estimated X and Y velocity, but also the linear
acceleration in the X direction. 3. Statuses - The sensor status
associated with the radar. Also a separate message for the radar's
error status.
