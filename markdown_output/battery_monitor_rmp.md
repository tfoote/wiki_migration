## About

The `battery_monitor_rmp` package uses the feedback provided by the
RMP to monitor the segway batteries and then uses espeak to tell the
user if a battery is getting low. It also publishes this information.

## Nodes



```clearsilver
node.0 {
  name = monitor_rmp.py
  desc = `monitor_rmp.py` will take the feedback and publish that which corresponds to the batteries on the RMP. It will also use espeak to alert the user of battery states at 20%, 10% and 5%.
  sub {
    0.name = rmp_feedback
    0.type = 'rmp_msgs/RMPFeedback'
    0.desc = List of all of the feedback from the RMP
  }
  pub {
    0.name = battery_status_rmp
    0.type = 'rmp_msgs/RMPBatteryStatus'
    0.desc = publishes the battery status information for the RMP
  }
  param {
    0.name = ~front_base_batt_1
    0.type = `bool`
    0.default = False
    0.desc = does the robot have the front base battery 1  
    1.name = ~front_base_batt_2
    1.type = `bool`
    1.default = False
    1.desc = does the robot have the front base battery 2  
    2.name = ~rear_base_batt_1
    2.type = `bool`
    2.default = False
    2.desc = does the robot have the rear base battery 1  
    3.name = ~rear_base_batt_2
    3.type = `bool`
    3.default = False
    3.desc = does the robot have the rear base battery 2  
    4.name = ~aux_batt
    4.type = `bool`
    4.default = False
    4.desc = does the robot have an auxiliary battery
  }
}
```



## Installation

To install the `battery_monitor_rmp` package, you can choose to either
install from source, or from the Ubuntu package:

### Source

To install from source, execute the following: 

```shell
cd /path/to/your/catkin/workspace/src
git clone https://github.com/WPI-RAIL/battery_monitor_rmp.git
cd /path/to/your/catkin/workspace
catkin_make 
catkin_make install
```



### Ubuntu Package

To install the Ubuntu package, execute the following:


```
sudo apt-get install ros-indigo-battery-monitor-rmp
```



### Startup

The `battery_monitor_rmp` package contains a
`battery_monitor_rmp.launch` file. This file launches an instance of
the `battery_monitor_rmp.py`. To launch these nodes the following
command can be used:



```
roslaunch battery_monitor_rmp battery_monitor_rmp.launch
```



Now the node will publish the information as well as use espeak to
inform the user of a state of charge less than or equal to 20%.

## Support

Please send bug reports to the
[GitHub Issue Tracker](https://github.com/WPI-RAIL/rovio/issues). Feel
free to contact me at any point with questions and comments.

-   [Russell Toris](Russell Toris)
-   <rctoris@wpi.edu>
-   [Academic Website](http://users.wpi.edu/~rctoris/)
