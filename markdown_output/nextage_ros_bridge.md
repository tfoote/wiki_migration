\<\<Include(Industrial/Software_Status/Developmental)\>\>

## Operate via Robot Client

[NextageClient](http://docs.ros.org/hydro/api/nextage_ros_bridge/html/classnextage__ros__bridge_1_1nextage__client_1_1NextageClient.html)
is a python class that functions as a programming interface for the
robot users. As seen in the api document, it extends
[HIRONX](http://docs.ros.org/hydro/api/hironx_ros_bridge/html/classhironx__ros__bridge_1_1hironx__client_1_1HIRONX.html)
class so that all the public methods are inherited from there on.

The reason \`NextageClient\` was created separately from \`HIRONX\` is
because of the \`DIO\` design unique to
[NEXTAGE OPEN](http://nextage.kawada.jp/en/) robot.

[![Class relationship](http://docs.ros.org/hydro/api/nextage_ros_bridge/html/classnextage__ros__bridge_1_1nextage__client_1_1NextageClient__inherit__graph.png)](http://docs.ros.org/hydro/api/nextage_ros_bridge/html/classnextage__ros__bridge_1_1nextage__client_1_1NextageClient.html)
