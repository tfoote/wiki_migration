## Use

This plugin queries the ROS master for a list of all nodes, and attempts
to display process information about them. Currently, information is
only available for local nodes running on the same computer as the rqt
instance.

The node list can be filtered using the text box at the top. Unless the
\`regex\` box is checked, the node list will contain any node whose name
contains the text in the filter box. If the \`regex\` box is checked,
the filter will be treated as a python-style regular expression, and the
list will contain any node whose name matches the expression.

Hovering over the a node name will display the full command used to
start the node. Hovering over the memory will display the resident and
virtual memory for the node in mebibytes.

## Notes

This plugin requires a newer version of psutil than is available in the
rosdep-supported version on Ubuntu Precise (12.04). A newer version is
available from pip with \`pip install psutil\`.

## Screenshot

![](attachment:rostop_gui.png)
