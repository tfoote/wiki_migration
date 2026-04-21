This package provides a driver node for the SICK LD-MRS400001 Laser
Scanner. The node can be initiated using: *rosrun sick_ldmrs
sickldmrs.py*

The node publishes on five separate topics:

-   [PointCloud2](http://www.ros.org/wiki/pcl/FAQ) topic - containing
    the 3D points, layer, echo number, echo widths and time deltas.
-   Four
    [LaserScan](http://www.ros.org/doc/api/sensor_msgs/html/msg/LaserScan.html)
    topics (one for each scan layer of the device).

Parameters can be modified via the dynamic_reconfigure gui: *rosrun
dynamic_reconfigure reconfigure_gui*

The node is written in Python/Numpy.

No facility is provided for changing the IP address or port of the
device. This can be achieved by using the software provided with the
device (LD-MRS View).
