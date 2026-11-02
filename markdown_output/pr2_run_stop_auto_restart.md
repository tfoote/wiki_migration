## ROS API



```clearsilver
node.0 {
  name=run_stop_auto_restart
  desc=`run_stop_auto_restart` is a simple node for resetting the breakers and motors of the PR2. When the state of the run stop changes from off to on, it automatically enables the power to the motors and reset the motors.
  sub{
    0.name= power_board/state
    0.type= pr2_msgs/PowerBoardState
    0.desc= The state of the PR2 power board
  }  
  srv_called {
    0.name = power_board/control
    0.type = pr2_power_board/PowerBoardCommand
    0.desc = Calls power board to enable breakers.
    1.name = pr2_etherCAT/reset_motors
    1.type = std_srvs/Empty
    1.desc = Resets the motors
```
