## ROS API

### run_stop_auto_restart

`run_stop_auto_restart` is a simple node for resetting the breakers
and motors of the PR2. When the state of the run stop changes from off
to on, it automatically enables the power to the motors and reset the
motors.

#### Subscribed Topics

- `power_board/state`
  ([pr2_msgs/msg/PowerBoardState](https://docs.ros.org/en/rolling/p/pr2_msgs/msg/PowerBoardState.html)):
  The state of the PR2 power board

#### Services Called

- `power_board/control`
  ([pr2_power_board/srv/PowerBoardCommand](https://docs.ros.org/en/rolling/p/pr2_power_board/srv/PowerBoardCommand.html)):
  Calls power board to enable breakers.
- `pr2_etherCAT/reset_motors`
  ([std_srvs/srv/Empty](https://docs.ros.org/en/rolling/p/std_srvs/srv/Empty.html)):
  Resets the motors
