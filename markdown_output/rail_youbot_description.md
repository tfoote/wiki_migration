## About

  -- -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- -- --------------------------------- --
     <tablewidth="100%" tablestyle="text-align:left">This package contains customized youBot URDFs used by the [Robot Autonomy and Interactive Learning](http://web.cs.wpi.edu/~rail/) research group at [WPI](http://www.wpi.edu/). Changes include slight color adjustments, the inclusion of a Kinect sensor, and color markers placed around the based (used for finding the robot using overhead cameras). This package only modifies the necessary URDF files and imports any reused files from the [pr2_description](pr2_description) and [youbot_description](https://github.com/youbot/youbot-ros-pkg) packages. The finalized robot file that can be loaded is `robots/rail_youbot.urdf.xacro`.      ![](attachment:rail_youbot.png)   
  -- -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- -- --------------------------------- --

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
