

```wiki
(2/20/2013) pr2_dashboard has reached End Of Life and is replaced by [[rqt_pr2_dashboard|rqt_pr2_dashboard]].
```



## Running

Run `pr2_dashboard` with: 

```
rosrun pr2_dashboard pr2_dashboard
```



You may have to set your
[ROS_MASTER_URI](ROS/EnvironmentVariables#ROS_MASTER_URI) environment
variable before you start your dashboard: 

```
export ROS_MASTER_URI=http://MY_ROBOT:11311
```



## Dashboard

![](attachment:main.png)

The main window of the dashboard is composed entirely of status
indicators, the idea being that if they are all green the robot should
be working fine from a hardware and built-in systems standpoint.

Each of the indicators has a tooltip with some extra detail.

The indicators are broken into four categories:

### Diagnostic

  -- ------------------- -- ------------------------------------- -- --------------------------------------- -- ---------------------------------------- -- ---------------------------------------- -- ----------------------------------------------------------------------------------------------------------------------------------------- --
     **Component**          **OK**                                   **Warn**                                   **Error**                                   **Stale**                                   **Description**                                                                                                                           
     <\^>Diagnostics      <\^>![](attachment:diag_ok.png)        <\^>![](attachment:diag_warn.png)        <\^>![](attachment:diag_error.png)        <\^>![](attachment:diag_stale.png)        <\^>Clicking pops up the [Robot Monitor](robot_monitor). The OK/Warn/Error state is determined from the top level of its tree.          
     <\^>Rosout           <\^>![](attachment:rosout_ok.png)      <\^>![](attachment:rosout_warn.png)      <\^>![](attachment:rosout_error.png)      <\^>![](attachment:rosout_stale.png)      <\^>Clicking pops up [rxconsole](rxconsole). The OK/Warn/Error state is determined by the messages received over the last 30 seconds.   
     <\^>Motors           <\^>![](attachment:motors_ok.png)      <\^>N/A                                  <\^>![](attachment:motors_error.png)      <\^>![](attachment:motors_stale.png)      <\^>Clicking pops up a menu allowing you to halt or reset motors: ![](attachment:motors_menu.png)                                       
  -- ------------------- -- ------------------------------------- -- --------------------------------------- -- ---------------------------------------- -- ---------------------------------------- -- ----------------------------------------------------------------------------------------------------------------------------------------- --

### Circuit Breakers

The circuit breakers are labeled L/B/R, which stand for *Left Arm*,
*Base/Spine*, and *Right Arm*. Each breaker can be in one of four
states, and clicking on any of the breakers will pop up a menu allowing
you to change the state of one or all of them:

![](attachment:breakers_menu.png)

  -- -------------------------------------------------------------------------------------------------- -- ----------------------------------------------------------------------------------------------------------------- -- -------------------------------------------------------------------------------------------------------------------- -- ----------------------------------------------------------------------------------------------------------- --
     <tablestyle="width: 100%; text-align: center;"> **Enabled**                                       **Standby**                                                                                                          **Disabled**                                                                                                            **Stale**                                                                                                   
     ![](attachment:breaker_l_ok.png)![](attachment:breaker_b_ok.png)![](attachment:breaker_r_ok.png)      ![](attachment:breaker_l_standby.png)![](attachment:breaker_b_standby.png)![](attachment:breaker_r_standby.png)      ![](attachment:breaker_l_disabled.png)![](attachment:breaker_b_disabled.png)![](attachment:breaker_r_disabled.png)      ![](attachment:breaker_l_stale.png)![](attachment:breaker_b_stale.png)![](attachment:breaker_r_stale.png)   
  -- -------------------------------------------------------------------------------------------------- -- ----------------------------------------------------------------------------------------------------------------- -- -------------------------------------------------------------------------------------------------------------------- -- ----------------------------------------------------------------------------------------------------------- --

Enabled is the only state in which the robot's motors will move. Stale
occurs when no messages are received from the breakers in more than 3
seconds.

### Runstops

The runstop indicators are just that \-- indicators, with no way of
changing their state from within the dashboard. There are two runstops
on the robot, a wireless one and a physical one on the back of the
robot.

The runstops can be in one of four states:

  -- ---------------------------------------------------------------------------- -- ------------------------------------------------------------------------------ -- ----------------------------------------------------------------------------------- -- ---------------------------------------------------------------------------------- --
     <tablestyle="width: 100%; text-align: center;">**OK**                       <:>**Physical Stopped**                                                         <:>**Wireless Stopped**                                                              **Stale**                                                                          
     <:>![](attachment:runstop_ok.png)![](attachment:runstop_wireless_ok.png)      <:>![](attachment:runstop_stop.png)![](attachment:runstop_wireless_ok.png)      <:>![](attachment:runstop_unknown.png)![](attachment:runstop_wireless_stop.png)      <:>![](attachment:runstop_stale.png)![](attachment:runstop_wireless_stale.png)   
  -- ---------------------------------------------------------------------------- -- ------------------------------------------------------------------------------ -- ----------------------------------------------------------------------------------- -- ---------------------------------------------------------------------------------- --

There are only four states because the wireless runstop "overrides"
the physical one, and we cannot get the state of the physical one if the
wireless one is stopped.

### Battery

The battery is also just an indicator with no way of changing its state.
The battery will change its color and % filled based on the amount of
battery remaining. It will also show a power-plug symbol if the robot is
charging.

  -- ---------------------------------------------------------------------- -- ------------------------------------ -- --------------------------------- -- -------------------------------------- --
     <tablestyle="width: 100%; text-align: center;"> **Charge >50%**      **Charge 30-50%**                       **Charge <30%**                     **Charging**                           
     ![](attachment:battery_green.png)                                         ![](attachment:battery_yellow.png)      ![](attachment:battery_red.png)      ![](attachment:battery_charging.png)   
  -- ---------------------------------------------------------------------- -- ------------------------------------ -- --------------------------------- -- -------------------------------------- --

## ROS API



```clearsilver
node.0 {
  name = pr2_dashboard
  desc = Starts the pr2 dashboard
  sub {
    0.name = /diagnostics_agg
    0.type = diagnostic_msgs/DiagnosticArray
    0.desc = Subscribed to by [[robot_monitor]]
    1.name = /rosout_agg
    1.type = roslib/Log
    1.desc = Subscribed to by [[rxconsole]]
    2.name = motors_halted
    2.type = std_msgs/Bool
    2.desc = Provides yes/no on whether or not the motors are halted and need to be reset.
    3.name = power_state
    3.type = pr2_msgs/PowerState
    3.desc = Provides information on the current battery state
    4.name = power_board_state
    4.type = pr2_msgs/PowerBoardState
    4.desc = Provides information about the current breaker state
  }
  srv_called {
    0.name = power_board_control
    0.type = pr2_power_board/PowerBoardCommand
    0.desc = Controls breaker state
    1.name = reset_motors
    1.type = std_srvs/Empty
    1.desc = Resets the motors
    2.name = halt_motors
    2.type = std_srvs/Empty
    2.desc = Halts the motors
  }
```


