## Overview

`power_node2` controls with the PR2 power board. The API below is for
informational purposes only; it is not intended for use by anything
other than [power_monitor](https://index.ros.org/p/power_monitor), which
is where you should look for power data.

The `power_node2` runs on the PR2 and controls the PR2 power board.
The node regulates the main fan speed of the PR2 based on battery and
power board temperature.

## Nodes



```clearsilver
name = power_node2
pub {
  0.name= /diagnostics
  0.type= diagnostics_msgs/DiagnosticArray
  0.desc= Diagnostic information
  1.name= ~state
  1.type= pr2_msgs/PowerBoardState
  1.desc= Power board state
}
sub {
  0.name = battery/server2
  0.type = pr2_msgs/BatteryServer2
  0.desc = Battery data, for temperatures
}
srv {
  0.name= ~control2
  0.type= pr2_power_board/PowerBoardCommand2
  0.desc= Send a command to the power board
  1.name= ~control
  1.type= pr2_power_board/PowerBoardCommand
  1.desc= Send a command to the power board (DEPRECATED)
}
param {
  0.name= ~sample_frequency
  0.type= float
  0.default= 10.0
  0.desc= Sampling frequency
  1.name= ~transition_frequency
  1.type= float
  1.default= 0.1
  1.desc= Transition frequency
}
```





```clearsilver
name = power_node
desc = Deprecated node for controller Rev. A and B power boards.
pub {
  0.name= /diagnostics
  0.type= diagnostics_msgs/DiagnosticArray
  0.desc= Diagnostic information
  1.name= ~state
  1.type= pr2_msgs/PowerBoardState
  1.desc= Power board state
}
srv {
  1.name= ~control
  1.type= pr2_power_board/PowerBoardCommand
  1.desc= Send a command to the power board
}
```

## Troubleshooting

1.  format wiki
2.  language en

### Errors when using pr2_power_board

#### Error: Power board "stuck" in standby

##### Is the wireless estop in RunStop?

The display will look like below
![attachment:wirelessestop.png](doc/wirelessestop.png)

**Solution:**

- Is the wireless RunStop (the yellow OMNEX box) in the vacinity of the
  robot? ( In the same room)
- If not find it and bring it into the room, it may be out of range.
- Is the wireless RunStop working and with a yellow light flashing next
  to the start button?
- If not press start
- If the light does not blink after you press start
- Replace the batteries.

##### Is the RunStop button pressed?

The display will look like below.

![attachment:buttonestop.png](doc/buttonestop.png)

**Solution:**

- Is the RunStop button pushed in? (It's the big red button on the
  back.) Twist the button to put in run mode.

#### Error: Power board "stuck" in disable

The display will look like below

![attachment:disabled.png](doc/disabled.png)

**Solution:**

- Try pressing the Reset Disable button for the circuit breaker you want
  on.
- If Reset Disable doesn't work, contact Curt M., Derek K., or Mike S.

#### Error: Power board gui comes up empty

The display will look like below.

![attachment:blankpower.png](doc/blankpower.png)

**Solution:**

- Is the power node running on your robot? Check by running
  

```
rosnode list
```

 and see if pr2_power_board is running.
- If it is not running:
- [ Is your ROS_MASTER_URI pointing at the right place?](CommonTroubleshooting#head-284b2d1fa3bf38c9dfedeb10526297ba2963e541)
- Can you run it manually? On the robot 

```
rosrun pr2_power_board power_node
```


- If it comes up you probably have a problem with your launch script(s).
  Check to make sure they launch the pr2_power_board power_node
  correctly. It might look like: 

```
<!-- Power Board Control Node -->
<node pkg="pr2_power_board" type="power_node"  respawn="true"/>
```


- If you cannot run it manually
- Make sure it's compiled and try again 

```
rosmake pr2_power_board
```
