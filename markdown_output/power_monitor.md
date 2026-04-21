## Nodes

### power_monitor

\`power_monitor\` takes data from
[ocean_battery_driver](ocean_battery_driver) and
[pr2_power_board](pr2_power_board) and republishes it in a more
user-friendly message format.

The estimation method that \`power_monitor\` uses is reconfigurable via
[dynamic_reconfigure](dynamic_reconfigure). Two methods are currently
available:

-   ***Fuel Gauge***: simply publishes the state of charge and remaining
    time that the battery servers report.

```{=html}
<!-- -->
```
-   ***Advanced***: records a history of battery state over the lifetime
    of the robot (in a CSV file in \`/var/ros/power_monitor/power.log\`)
    and uses this data to improve the indicators.

#### Subscribed topics

```clearsilver
sub {
  no_header= True
  0.name= battery/server2
  0.type= pr2_msgs/BatteryServer2
  0.desc= Battery data
  1.name= power_board/power_state
  1.type= pr2_msgs/PowerBoardState
  1.desc= Power board state
}
```

#### Advertised topics

```clearsilver
pub {
  no_header= True
  0.name= power_state
  0.type= pr2_msgs/PowerState
  0.desc= State of the power system
}
```

#### Parameters

```clearsilver
param {
  no_header= True
  0.name= ~frequency
  0.type= float
  0.default= 0.1
  0.desc= Frequency at which messages are published on `power_state`
  1.name= ~estimation_method
  1.type= string
  1.default= advanced
  1.desc= State of charge estimation method to use
  2.name= ~advanced_log_file
  2.type= string
  2.default= /hwlog/power_monitor/power.log
  2.desc= Location of file to record battery data
  3.name = ~battery_update_timeout
  3.type = double
  3.default = 120
  3.desc = Stop publishing power estimate if batteries haven't updated within this timeout. Set to <0 to always publish estimate.
}
```
