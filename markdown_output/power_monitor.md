## Nodes

### power_monitor

`power_monitor` takes data from
[ocean_battery_driver](https://index.ros.org/p/ocean_battery_driver) and
[pr2_power_board](https://index.ros.org/p/pr2_power_board) and
republishes it in a more user-friendly message format.

The estimation method that `power_monitor` uses is reconfigurable via
[dynamic_reconfigure](https://index.ros.org/p/dynamic_reconfigure). Two
methods are currently available:

- **`'Fuel Gauge`**': simply publishes the state of charge and
  remaining time that the battery servers report.

<!-- -->

- **`'Advanced`**': records a history of battery state over the
  lifetime of the robot (in a CSV file in
  `/var/ros/power_monitor/power.log`) and uses this data to improve
  the indicators.

#### Subscribed topics

- `battery/server2`
  ([pr2_msgs/msg/BatteryServer2](https://docs.ros.org/en/rolling/p/pr2_msgs/msg/BatteryServer2.html)):
  Battery data
- `power_board/power_state`
  ([pr2_msgs/msg/PowerBoardState](https://docs.ros.org/en/rolling/p/pr2_msgs/msg/PowerBoardState.html)):
  Power board state

#### Advertised topics

- `power_state`
  ([pr2_msgs/msg/PowerState](https://docs.ros.org/en/rolling/p/pr2_msgs/msg/PowerState.html)):
  State of the power system

#### Parameters

- `~frequency` (`float`, default: `0.1`): Frequency at which messages
  are published on `power_state`
- `~estimation_method` (`string`, default: `advanced`): State of charge
  estimation method to use
- `~advanced_log_file` (`string`, default:
  `/hwlog/power_monitor/power.log`): Location of file to record battery
  data
- `~battery_update_timeout` (`double`, default: `120`): Stop publishing
  power estimate if batteries haven't updated within this timeout. Set
  to <0 to always publish estimate.

## Troubleshooting

### Errors when using package

#### Error: ERROR NAME

**Example:** 

```
the error output the user will see on the console
```



**Solution:**

- Is something not connected? No device is connected.
