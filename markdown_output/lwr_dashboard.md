## Running

Run `lwr_dashboard` with: ```
rosrun lwr_dashboard lwr_dashboard
```

You may have to set your
[ROS_MASTER_URI](ROS/EnvironmentVariables#ROS_MASTER_URI) environment
variable before you start your dashboard: ```
export ROS_MASTER_URI=http://MY_ROBOT:11311
```

## Dashboard

![](attachment:main.png)

The main window of the dashboard is composed entirely of status
indicators, the idea being that if they are all green the robot should
be working fine from a hardware and built-in systems standpoint.

Each of the indicators has a tooltip with some extra detail.
