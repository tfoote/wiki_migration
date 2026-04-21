

```wiki
'''Note:''' This stack is designed for robots purchased before June 2014. 
For new robots, see the [[robotican|robotican]] stack.
```



# Package Description

This package handle the communication with the motors controller and the
odometry calculations. The package contains the Roboteq_Driver node
which publishes the odometry (nav_msgs/Odometry), rover battery voltage
(std_msgs::Float32) and the wheels encoders readings
(komodo_rover/StampedEncoders). The package is subscribed to the
/cmd_vel topic in order to receive geometry_msgs/Twist driving commands.
The package also subscribed to the /imu/data topic in order the merge
the imu orientation messages (sensor_msgs/Imu) into the odometry
messages. The odometry is also published through a TF broadcaster.

# Package Configuration

Package configuration files are:

○ **\\launch\\Roboteq_Driver.launch** - This launch file runs the
Roboteq_Driver node and loads the parameters from the chosen .yaml file.
This file can be launched from the main launch file
(komodo_launch.launch).

○ **\\config\\default.yaml** - This configuration file contains the
odometry parameters such as wheel diameter and wheel base length. The
file also contains the encoder resolution (ppr) and controllable loop
rates. The two imu related parameters (roll_pitch_from_imu and
yaw_from_imu) allows the user to enable or disable the merging of
orientation data into the odometry. When the roll_pitch_from_imu is set
to false the robot odometry roll and pitch will remain zero. When the
yaw_from_imu is set to false the robot yaw will be calculated only by
the odometry calculations, when this parameter will set to true, the yaw
will be set according the the magnetic north using the imu
magnetometers.
