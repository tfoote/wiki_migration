## About

The \`rail_worlds\` package contains a set of worlds developed by the
[RAIL lab](http://web.cs.wpi.edu/~rail/) at [WPI](http://www.wpi.edu/)
for [gazebo](gazebo). The worlds were developed with the Kuka youBot and
\`PR2\` robots in mind, but can be used with other types of robots as
well.

## Worlds

The \`rail_worlds\` package contains several pre-defined worlds: the
\`YouBot\` world and the \`PR2\` world. These worlds contain appropriate
cameras and objects for their respective robots.

### youBot World

  -- --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- -- -------------------------------- --
     \<tablewidth=\"100%\" tablestyle=\"text-align:left\"\>The youBot world populates the upper portion of the lab model from the [rail_models](rail_models) package (closest to the window) with children's furniture and objects that are appropriate for the youBot. In particular, the children\'s kitchen, table and chair set, toy chest, stool, cups, and cookware are placed throughout the room. Furthermore, overhead cameras are placed above the room.      ![](attachment:youbot_lab.png)   
  -- --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- -- -------------------------------- --

### PR2 World

  -- -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- -- ----------------------------- --
     \<tablewidth=\"100%\" tablestyle=\"text-align:left\"\>The PR2 world populates the lower portion of the lab model from the [rail_models](rail_models) package (closest to the door) with furniture that is appropriate for the PR2. In particular, the lab table is placed inside of the room. Furthermore, overhead cameras are placed above the room.      ![](attachment:pr2_lab.png)   
  -- -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- -- ----------------------------- --

### Fuller 318 Two Tables World

  -- ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- -- -------------------------------------- --
     \<tablewidth=\"100%\" tablestyle=\"text-align:left\"\>The Fuller 318 Two Tables world populates the full lab model from the [rail_models](rail_models) package with furniture that is appropriate for the PR2. In particular, two lab tables are placed near the window inside of the room. Furthermore, overhead cameras are placed above the room. A map from the [rail_maps](rail_maps) stack can be used with this world.      ![](attachment:318_2_tables_lab.png)   
  -- ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- -- -------------------------------------- --

## Installation

To install the \`rail_gazebo\` stack, you can choose to either install
from source, or from the Ubuntu package:

### Source

To install from source, execute the following: ```shell
cd /path/to/your/ros/stacks
git clone https://github.com/WPI-RAIL/rail_gazebo.git
roscd rail_gazebo
rosdep install rail_gazebo
rosmake rail_gazebo
```

### Ubuntu Package

To install the Ubuntu package, execute the following:
```
sudo apt-get install ros-fuerte-rail-gazebo
```

### Startup

Separate launch files are provided to launch each of the above worlds.
To launch the youBot world, simply execute the following command:
```
roslaunch rail_worlds youbot_world.launch
```

To launch the PR2 world, simply execute the following command:
```
roslaunch rail_worlds pr2_world.launch
```

To launch the Fuller 318 Two Tables world, simply execute the following
command: ```
roslaunch rail_worlds fuller_318_full_2_tables_world
```

Note that these launch files will ***not*** place any robots inside of
the world.

## Support

Please send bug reports to the
[GitHub Issue Tracker](https://github.com/WPI-RAIL/rail_gazebo/issues).
Feel free to contact me at any point with questions and comments.

-   [Russell Toris](Russell Toris)
-   <rctoris@wpi.edu>
-   [Academic Website](http://users.wpi.edu/~rctoris/)

------------------------------------------------------------------------

  -- ------------------------------------------------- -- ---------- -- -------------------------- --
     \<tablewidth=\"100%\"\> ![](attachment:wpi.png)      \<:99%\>      ![](attachment:rail.png)   
  -- ------------------------------------------------- -- ---------- -- -------------------------- --
