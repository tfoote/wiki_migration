```wiki
'''Note:''' This stack is designed for robots purchased before June 2014. 
For new robots, see the [[robotican|robotican]] stack.
```

# Package Description

This package handle the communication with the APM 2.5 microcontroller
and publish the readings of the following sensors: IMU
(sensor_msgs/Imu), GPS (sensor_msgs/NavSatFix and
sensor_msgs/NavSatStatus), Ultrasonic and InfraRed range sensors
(sensor_msgs/Range) and PC battery voltage (std_msgs::Float32). The
komodo_sensors node uses the serial_node.py node from the rosserial
package (see <http://www.ros.org/wiki/rosserial> for more details). The
imu_filter_madgwick package (see <http://www.ros.org/wiki/imu_tools>) is
used to filter and fuse raw data from the IMU. It fuses angular
velocities, accelerations, and (optionally) magnetic readings from a
generic IMU device into an orientation quaternion, and publishes the
fused data on the imu/data topic.

# Package Configuration

Package configuration files are:

○ **\\launch\\sensors_launch.launch** - This launch file runs the serial
comunication node from the rosserial package. Users can specify the GPS
frame id. This file can be launched from the main launch file
(komodo_launch.launch).
