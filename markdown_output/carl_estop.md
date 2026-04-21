## About

The `carl_estop` package is a software estop which contains nodes to
stop the Segway RMP without having to kill power to the Segway RMP and
its peripherals.

## Nodes



```clearsilver
node.0 {
  name = carl_estop_node
  desc = `carl_estop_node` runs on the on board computer. It will cancel goals given to 'move_base' and it will switch the RMP to standby mode when it no longer recieves messages from 'pc_estop_node'. When it starts to receive messages again the Segway is returned to Tractor mode and normal operation can resume.  
  sub {
    0.name = carl_estop
    0.type = std_msgs/Empty
    0.desc = The estop link used to stop the robot.
  }
  pub {
    0.name = rmp_command
    0.type = 'rmp_msgs/RMPCommand'
    0.desc = changes the mode the RMP is in.
  }
  act_called {
    0.name = move_base/cancel
    0.type = 'actionlib_msgs/GoalID'
    0.desc = A request to cancel a specific goal
  }
  param {
    0.name = ~stop_time_delay
    0.type = `double`
    0.default = 1.5
    0.desc = time in second after the connection is lost that the Segway should stop 
    1.name = ~check_frequency
    1.type = `double`
    1.default = 3.0
    1.desc = number of times per second to check the time delay between when the last message was received and the current time.
  }
}   
node.1 {
  name = pc_estop_node
  desc = `pc_estop_node` runs on an off board computer. It will publishes to the 'carl_estop' topic to make sure the 'carl_estop_node' does not cancel the goal and turn the segway to standby.
  pub {
    0.name = carl_estop
    0.type = std_msgs/Empty
    0.desc = The estop link used to stop the robot.
  }
  param {
    0.name = ~send_frequency
    0.type = `double`
    0.default = 3.0
    0.desc = time in second at which the message should be published 
  }
}
```



## Installation

To install the `carl_estop` package, you can choose to either install
from source, or from the Ubuntu package:

### Source

To install from source, execute the following: 

```shell
cd /path/to/your/catkin/workspace/src
git clone https://github.com/WPI-RAIL/carl_estop.git
cd /path/to/your/catkin/workspace
catkin_make 
catkin_make install
```



### Ubuntu Package

To install the Ubuntu package, execute the following:


```
sudo apt-get install ros-indigo-carl-estop
```



### Startup

The `carl_estop` package also contains a `pc_estop.launch` file
which should be launched on **the off board PC**. This file launches an
instance of the `pc_estop_node`. To launch, the following command can
be used:



```
roslaunch carl_estop pc_estop.launch
```



The `carl_estop` package also contains a `carl_estop.launch` file
which should be launched on **the robot**. This file launches an
instance of the `carl_estop_node`. To launch, the following command
can be used:



```
roslaunch carl_estop carl_estop.launch
```



After both nodes are launched you should now be able to stop the robot
by shutting down the pc_estop_node using CTRL\^C.

### Operation

When the PC Node is stopped, the carl node will issue commands to the
move_base/cancel action to cancel the current goal, and turn the RMP to
Standby mode so not even the teleop will work.

Once the PC node is restarted the Segway will be turned to tractor mode
and teleop will resume working. The robot however, will not remember the
goal. Therefore, once the robot is in a safe position a new goal can be
set.

## Support

Please send bug reports to the
[GitHub Issue Tracker](https://github.com/WPI-RAIL/rovio/issues). Feel
free to contact me at any point with questions and comments.

-   [Russell Toris](Russell Toris)
-   <rctoris@wpi.edu>
-   [Academic Website](http://users.wpi.edu/~rctoris/)
