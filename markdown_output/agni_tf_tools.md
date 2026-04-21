![rviz plugin](attachment:rviz_plugin.png)

This package shall facilitate the definition of static transforms via an
appropriate GUI. Both, a standalone GUI and a rviz plugin are provided
to interactively define the orientation and translation part of a
transform. Transformations between any of the 24 possible Euler angle
representations is provided. An interactive marker in rviz allows to
define the transform via mouse.

# Transforming Euler representations

Dependent on the order of rotation axes, there are different sets of
Euler angles. One common set is roll-pitch-yaw (the default in ROS),
which corresponds to rotations about x, y, and z axes w.r.t. the fixed
frame. To specify Euler angles w.r.t. a different set or order of axes,
simply specify the desired order instead of rpy. For example,
`yxz: 30, 50, 70` will rotate by 30° about the y axis, then by 50° about
the x axis, and finally by 70° about the y axis. In order to transform a
given Euler angle representation into another one, simply enter the
desired axes order - replacing the whole text field including the
angular values.

To specify whether rotations should be performed w.r.t. the **s**tatic
or the moving / **r**otationg frame (corresponding to left resp. right
matrix multiplication), it\'s possible to prefix the axes order by
\"**s**\" or \"**r**\". Omitting the prefix, corresponds to \"**r**\" or
right matrix multiplication.

# Computing a transform w.r.t. another parent

The rviz plugin also supports frame transformations. If you want to
compute the entered transform w.r.t. another parent frame, simply enable
the checkbox \"`adapt transformation`\" and subsequently change the
`parent frame`. If the checkbox is not ticked, changing the parent frame
doesn\'t change the relative transform, but moves the interactive
marker.

# Publishing transforms

The entered transform is published as soon as a empty frame names are
provided and the \"`publish transform`\" checkbox is enabled.
