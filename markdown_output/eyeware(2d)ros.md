## Eyeware ROS utilities for 3D eye tracking

### GazeSense ROS bridge

The GazeSense ROS bridge exposes 3D eye tracking data from the GazeSense
application into the Robot Operating System (ROS).

GazeSense is an application developed by Eyeware Tech SA
(<http://www.eyeware.tech>) that provides real-time 3D eye tracking by
relying on consumer 3D sensors. GazeSense allows to define virtual 3D
objects of the environment, and measure the attention of people towards
those objects.

The GazeSense ROS bridge publishes 3D eye tracking data on ROS topics.
In addition, this tracking data can be visualized in Rviz:

![](attachment:eyeware-gazesense-ros.gif)

Left: GazeSense eye tracking. Right: ROS bridge eye tracking. Both
visualizations show the position of a camera (purple glyph) and a
tracked person\'s estimated gaze (orange rays), as the person is looking
at different areas of the environment (yellow screens).

The area that is being fixated at a given instant is highlighted in red.
The black cube represents the point that the person is looking at.

For more information, please refer to
<https://github.com/eyeware/eyeware-ros>
