## About

  -- ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ -- --------------------------------- --
     <tablewidth="100%" tablestyle="text-align:left">The `rms_pr2_gazebo_environment` package contains launch files that can launch an example RMS Gazebo environment for use with the [rms](rms). These files will launch the simulator with a PR2 world from the [rail_worlds](rail_worlds) package, place a PR2 into the world, and start appropriate server nodes (e.g., [rosbridge_server](rosbridge_server)).      ![](attachment:environment.png)   
  -- ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ -- --------------------------------- --

## Installation

To install the `rms_pr2_gazebo_environment` stack, you can choose to
either install from source, or from the Ubuntu package:

### Source

To install from source, execute the following: 

```shell
cd /path/to/your/ros/stacks
git clone https://github.com/WPI-RAIL/rms_pr2_gazebo_environment.git
roscd rms_pr2_gazebo_environment
rosdep install rms_pr2_gazebo_environment
rosmake rms_pr2_gazebo_environment
```



### Ubuntu Package

To install the Ubuntu package, execute the following:


```
sudo apt-get install ros-fuerte-rms-pr2-gazebo-environment
```



### Startup

Two launch files are included with this package: one to launch
everything needed to run the entire server environment, and one to just
spawn the robot into an existing Gazebo instance. To launch the entire
server environment (i.e., with all server nodes such as
[rosbridge_server](rosbridge_server)), simply run the following:



```
roslaunch rms_pr2_gazebo_environment rms_pr2_gazebo_environment.launch
```



If instead you wish to start Gazebo and spawn the robot without starting
the actual server nodes, run the following set of commands in two shell
sessions:



```shell
roslaunch rail_worlds fuller_318_full_2_tables_world.launch
roslaunch rms_pr2_gazebo_environment pr2_gazebo_start.launch
```



## Tutorials

More detailed instructions are provided for installing, setting up, and
running an instance of the PR2 RMS Gazebo Environment server. For more
information, start with the following tutorial:

A full list of all RMS related tutorials is provided on the [rms](rms)
stack page.

## Support

Please send bug reports to the
[GitHub Issue Tracker](https://github.com/WPI-RAIL/rms_pr2_gazebo_environment/issues).
Feel free to contact me at any point with questions and comments.

-   [Russell Toris](Russell Toris)
-   <rctoris@wpi.edu>
-   [Academic Website](http://users.wpi.edu/~rctoris/)

------------------------------------------------------------------------

  -- ------------------------------------------------- -- ---------- -- -------------------------- --
     <tablewidth="100%"> ![](attachment:wpi.png)      <:99%>      ![](attachment:rail.png)   
  -- ------------------------------------------------- -- ---------- -- -------------------------- --
