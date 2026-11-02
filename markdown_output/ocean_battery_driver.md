## Associated Hardware

- Ocean Server: <http://www.ocean-server.com/overview.html>
- IBPS specific documentation
  [IBPS Protocol](http://pr.willowgarage.com/wiki/IBPSBatteryInterface/IBPS_Protocol)
- The Smart Battery Standard [sbdat110.pdf](doc/sbdat110.pdf)

## Nodes

### ocean_server

`ocean_server` controls an array of battery controllers. The API below
is for informational purposes only; it is not intended for use by
anything other than
[power_monitor](https://index.ros.org/p/power_monitor), which is where
you should look for power data.

The `ocean_server` node will report the status of the batteries to
diagnostics. It will warn on the diagnostics if a battery does not
update within a timeout.

#### Advertised topics



```clearsilver
pub {
  no_header= True
  0.name= /diagnostics
  0.type= diagnostics_msgs/DiagnosticArray
  0.desc= Diagnostic information
  1.name= /battery/server2
  1.type= pr2_msgs/BatteryServer2
  1.desc= Battery data
  2.name= /battery/server
  2.type= pr2_msgs/BatteryServer
  2.desc= Battery data (DEPRECATED)
}
```



#### Parameters



```clearsilver
param {
  no_header= True
  0.name= ~number_of_ports
  0.type= int
  0.default= if no value specified on command-line, 4
  0.desc= Number of ports to monitor
  1.name= ~debug_level
  1.type= int
  1.default= if no value specified on command-line, 0
  1.desc= Debug level
  2.name= ~port<ID>
  2.type= string
  2.default= `"/dev/ttyUSB<ID>"`
  2.desc= Which device file is associated with the battery on port <ID>
  3.name= ~lag_timeout
  3.type= int
  3.default= `60`
  3.desc= Maximum time between battery messages before a battery reports a warning. Set to <0 to disable
  4.name= ~stale_timeout
  4.type= int
  4.default= `120`
  4.desc= Maximum time between battery messages before a battery reports an error. Set to <0 to disable
}
```

## Troubleshooting

1.  format wiki
2.  language en

### Errors when using ocean_battery_driver

#### Error: Cannot open /dev/ttyUSB0



```
user@prX: rosrun ocean_battery_driver monitor 
 sh: cannot open /dev/ttyUSB0: No such file
 cannot open port [/dev/ttyUSB0]
```



**Solution:**

- Is the battery system connected? No device is connected.
- You can run `battery_check` to try to get more information.
  

```
rosrun ocean_battery_driver battery_check -v /dev/ttyUSB0
```



#### Error: Battery status gui comes up empty

![attachment:Screenshot-PR2 Power State.png](doc/Screenshot-PR2_Power_State.png)

**Solution:**

- Is the battery monitor running on your robot?
- On the robot 

```
$~/ros/ros-pkg/drivers/robot/pr2/ocean_battery_driver/ ./scripts/view_batteries
```


- Off the robot 

```
$ ssh prX2 rosrun ocean_battery_driver view_batteries
```


- [Is your ROS_MASTER_URI pointing at the right place?](http://pr.willowgarage.com/wiki/CommonTroubleshooting#head-284b2d1fa3bf38c9dfedeb10526297ba2963e541)

#### Error: Batteries report "No Good"

The "No Good" message means the batteries are in a lockout/error
state. When a battery is drained too low, it can disable itself to
prevent further damage, and enable the "No Good" state.

In order to reset this message, the ocean battery server needs to be
completely power cycled.

If you see this message on a PR2, contact Willow Garage Support.

#### Error: Battery Report "Stale updates" or "No updates"

The batteries periodically publish their status to the ocean battery
driver. If they go too long before publishing status, the battery driver
will report a warning or error. The timeouts for these warnings and
errors can be adjusted with the `lag_timeout` and `stale_timeout`
parameters to the battery driver.

If a battery reports this message, and the timeout is sufficiently long
(over 60 seconds, for most purposes), this probably means a connection
problem with the battery.

At the end of the diagnostic message for each battery, they report
"Time since update (s)". If this value is "N/A", this means the
battery has not updated, and is probably disconnected.
