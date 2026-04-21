## About

This package contains a useful launch file that can be used on a Kuka
youBot to launch its motors, a Kinect sensor, load the robot
description, and start the state publisher. This package will load the
URDF found in the [rail_youbot_description](rail_youbot_description)
package as its robot description.

## Installation

Before installing the `rail_youbot` stack, be sure to install the
necessary dependencies. Instructions on installing the various youBot
packages can be found
[in this tutorial](rail_youbot/Tutorials/AddingAUserAndInstallingTheirLocalDrivers).

To install the `rail_youbot` stack, simply run the following commands
in your shell:

```shell
cd /path/to/your/local/ros/stacks
git clone https://github.com/WPI-RAIL/rail_youbot.git
roscd rail_youbot
rosmake rail_youbot
```

This will ensure all dependencies are met and that the package is ready
for use.

### Startup

This package contains a `rail_youbot.launch` file which should require
no modifications for use you your youBot. To start the script, run the
following command on your robot:

```
roslaunch rail_youbot_launch rail_youbot_launch.launch
```

### Remote ROS Core

In some cases you may want to run on off-board `roscore` server. If
this is the case, you need to tell ROS to do so before launching the
above file. In the `/.bashrc` file on your robot, add the following
lines (replacing the parts in `< >` with the appropriate
information.

```shell
export ROS_HOSTNAME=<hostname>
export ROS_MASTER_URI=http://<remote-roscore-server-ip>:11311
```

After saving the file, reload your `.bashrc` file with the following
command:

```
. ~/.bashrc
```

Now, when launching the launch file above, the robot will communicate
with a remote `roscore` instead of its own local `roscore`.

## Support

Please send bug reports to the
[GitHub Issue Tracker](https://github.com/WPI-RAIL/rail_youbot/issues).
Feel free to contact me at any point with questions and comments.

-   [Russell Toris](Russell Toris)
-   <rctoris@wpi.edu>
-   [Academic Website](http://users.wpi.edu/~rctoris/)

------------------------------------------------------------------------

  -- ------------------------------------------------- -- ---------- -- -------------------------- --
     <tablewidth="100%"> ![](attachment:wpi.png)      <:99%>      ![](attachment:rail.png)   
  -- ------------------------------------------------- -- ---------- -- -------------------------- --
