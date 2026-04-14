This package provides a proxy server for expanding abridged messages
received over bandwidth limited connections.

Useful for resource limited devices like arduino or anything using
rosserial to be able to publish messages that may otherwise be too large
or bandwidth intensive to publish.

Currently implements proxy nodes for Odom messages (nav_msgs/Odometry.h)
and Imu messages (sensor_msgs/Imu.h).

## Reporting bugs

<https://github.com/ecostech/rosabridge/issues>
