## About

The \`rail_youbot_teleop\` package contains a node that can be used to
teleoperate a Kuka youBot with a joystick. The node is responsible for
converting \`sensor_msgs/Joy\` messages into \`geometry_msgs/Twist\`
messages. A launch file is also included to launch both the
teleoperation node and the joy stick listener node.

## Nodes

```clearsilver
node.0 {
  name = youbot_joy_teleop
  desc = ||<tablewidth="100%" tablestyle="text-align:left">`youbot_joy_teleop` can control the motors of a Kuka youBot using a joystick. This node listens to a `joy` topic and sends messages to the `cmd_vel` topic. The left and right joysticks control the movement of the youBot. An example gamepad is shown to the right with its buttons labeled. || {{attachment:youbot_teleop_joy.png}} ||
  sub {
    0.name = joy
    0.type = sensor_msgs/Joy
    0.desc = Listens for joystick commands.
  }
  pub {
    0.name = cmd_vel
    0.type = geometry_msgs/Twist
    0.desc = Control the movement of the Rovio using the left and right joysticks.
  }
}
```

## Installation

Before installing the \`rail_youbot\` stack, be sure to install the
necessary dependencies. Instructions on installing the various youBot
packages can be found
[in this tutorial](rail_youbot/Tutorials/AddingAUserAndInstallingTheirLocalDrivers).

To install the \`rail_youbot\` stack, simply run the following commands
in your shell:

```shell
cd /path/to/your/local/ros/stacks
git clone https://github.com/WPI-RAIL/rail_youbot.git
roscd rail_youbot
rosmake rail_youbot
```

### Startup

The \`rail_youbot_teleop\` package contains a
\`youbot_joy_teleop.launch\` that can be used to control your robot.
This file launches an instance of the \`youbot_joy_teleop\` and
\`joy_node\` nodes. To launch these nodes, the following command can be
used:

```
roslaunch rail_youbot_teleop youbot_joy_teleop.launch
```

You should now be able to teleoperate your youBot with a joystick.

## Support

Please send bug reports to the
[GitHub Issue Tracker](https://github.com/WPI-RAIL/rail_youbot/issues).
Feel free to contact me at any point with questions and comments.

-   [Russell Toris](Russell Toris)
-   <rctoris@wpi.edu>
-   [Academic Website](http://users.wpi.edu/~rctoris/)

------------------------------------------------------------------------

  -- ------------------------------------------------- -- ---------- -- -------------------------- --
     \<tablewidth=\"100%\"\> ![](attachment:wpi.png)      \<:99%\>      ![](attachment:rail.png)   
  -- ------------------------------------------------- -- ---------- -- -------------------------- --
