See [Robots/CIR-KIT-Unit03](Robots/CIR-KIT-Unit03) for instructions and
tutorials.

## About

Installation and application packages for
[CIR-KIT-Unit03](Robots/CIR-KIT-Unit03).

## Installation

The following commands grab all required packages for
[CIR-KIT-Unit03](Robots/CIR-KIT-Unit03) navigation with [rosdep](rosdep)
and [wstool](wstool), and then execute \`catkin_make\` and \`catkin_make
run_tests\`.

### Clone this repository.

```
$ cd <catkin_ws>/src
$ git clone https://github.com/CIR-KIT-Unit03/cirkit_unit03_apps.git
```

### Run install script.

```
cd <catkin_ws>/src/cirkit_unit03_apps
sh install.sh
```

-   optional arguments:
-   -h: show the help message and exit
-   -i: eneble \`rosdep init\`
-   -t: enable \`catkin_make run_tests\`
-   -r: remove existing \`src/.rosinstall\`

## Applications

-   cirkit_unit03_autorun
-   runs whole packages for autonomous driving, such as the navigation
    related ([move_base](move_base), [amcl](amcl)), the sensor control
    related
    ([ira_laser_tools](https://github.com/iralabdisco/ira_laser_tools),
    filtered via [laser_filters](laser_filters)) and the simulation
    related ([Gazebo](http://gazebosim.org/)) with utility nodes
    ([timed_roslaunch](timed_roslaunch)) also for stable execution of
    system.
-   All of them are launched from packages with prefix
    \`cirkit_unit03\`, whose parameters are already set up in each
    package.

## Configuration

### Basical packages for CIR-KIT-Unit03

Cloned via cirkit_unit03_pkgs.rosinstall

-   [cirkit_unit03_common](cirkit_unit03_common)
-   [cirkit_unit03_control](cirkit_unit03_control)
-   [cirkit_unit03_description](cirkit_unit03_description)
-   [cirkit_unit03_navigation](cirkit_unit03_navigation)
-   [cirkit_unit03_amcl](cirkit_unit03_amcl)
-   [cirkit_unit03_gmapping](cirkit_unit03_gmapping)
-   [cirkit_unit03_maps](cirkit_unit03_maps)
-   [cirkit_unit03_move_base](cirkit_unit03_move_base)
-   [cirkit_unit03_robot](cirkit_unit03_robot)
-   [cirkit_unit03_base](cirkit_unit03_base)
-   [cirkit_unit03_bringup](cirkit_unit03_bringup)
-   [cirkit_unit03_simulator](cirkit_unit03_simulator)
-   [cirkit_unit03_gazebo](cirkit_unit03_gazebo)

### Dependent packages for CIR-KIT-Unit03

Cloned via cirkit_unit03_apps.rosinstall

-   [ira_laser_tools](https://github.com/AriYu/ira_laser_tools/tree/fix-eigen3cmake)
-   [lower_step_detector](lower_step_detector)
-   [steer_drive_ros](steer_drive_ros)
-   [steer_bot_hardware_gazebo](steer_bot_hardware_gazebo)
-   [steer_drive_controller](steer_drive_controller)
-   [stepback_and_steerturn_recovery](stepback_and_steerturn_recovery)

### Directory configuration after Installation

```
<catkin_ws>
│
└ src
   │ 
   ├ cirkit_unit03_apps 
   │   │
   │   ├ cirkit_unit03_apps (Metapackage)
   │   │
   │   ├ cirkit_unit03_autorun
   │   │
   │   ├ human_detector (Cloned via cirkit_unit03_apps.rosinstall)
   │   │
   │   └ timed_roslaunch (Cloned via cirkit_unit03_apps.rosinstall)
   │
   ├ cirkit_unit03_deps (Just a directory, not a metapacage)
   │   |
   |   ├ ira_laser_tools (Cloned via cirkit_unit03_pkgs.rosinstall)
   │   |
   |   ├ lower_step_detector (Cloned via cirkit_unit03_pkgs.rosinstall)
   │   |
   │   └ steer_drive_ros (Cloned via cirkit_unit03_pkgs.rosinstall)
   │
   └ cirkit_unit03_pkgs
       |
       ├ cirkit_unit03_pkgs (Metapackage)
       |
       ├ cirkit_unit03_common (Cloned via cirkit_unit03_pkgs.rosinstall)
       |
       ├ cirkit_unit03_navigation (Cloned via cirkit_unit03_pkgs.rosinstall)
       |
       ├ cirkit_unit03_robot (Cloned via cirkit_unit03_pkgs.rosinstall)
       |
       └ cirkit_unit03_simulator (Cloned via cirkit_unit03_pkgs.rosinstall)
```
