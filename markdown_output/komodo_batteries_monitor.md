

```wiki
'''Note:''' This stack is designed for robots purchased before June 2014. 
For new robots, see the [[robotican|robotican]] stack.
```



# Package Description

This package monitor the voltages of the three robot batteries. The
batteries_monitor node reads the batteries voltages messages published
by the komodo_sensors and komodo_rover packages. It also reads the robot
arm battery voltage from the arm controllers
(dynamixel_msgs/MotorState). The node sends an error message if one of
the batteries dropped below its minimum voltage. The node will also
initiate a 30 seconds countdown before powering off the computer when
its battery drops its minimum voltage. The node publish the batteries
voltages with their corresponding time of reading in one message into
the /batteries_monitor topic.

# Package Configuratoin

Package configuration files are:

○ **\\launch\\batteries_monitor_launch.launch** - This launch file runs
the batteries_monitor node. Users can specify the batteries minimum
voltage limits. This file can be launched from the main launch file
(komodo_launch.launch).
