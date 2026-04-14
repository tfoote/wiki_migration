Tracking PID

## Overview

Tracking PID offers a tuneable PID control loop to accurately follow a
trajectory. An interpolator moves a goal over a
\`\`\`nav_msgs/Path\`\`\` with a tuneable velocity, and a separate node
tracks the given point.

The PID contains three loops: Longitudinal, lateral and angular loops.
Source code at <https://github.com/nobleo/tracking_pid>.

### Tracking a carrot

One of the tracking options uses a carrot of length l in front of the
robot to determine the velocity commands based on the lateral and
longitudinal error between current Global Point (GP) and the Control
point (CP):

![\|width=\"600\"](attachment:tracking.png)

### Tracking the base link

If a smooth path is provided, the controller has the option to track the
path with the base_link directly instead of lagging behind a carrot. In
this case a Projected Global Point (PGP) is computed as well which is
tracked by the CP.

![\|width=\"600\"](attachment:tracking_base_link.png)

## Tutorials

See [tracking_pid/Tutorials](tracking_pid/Tutorials).

## Acknowledgement

\<\<Include(rosin/acknowledgement)\>\>
