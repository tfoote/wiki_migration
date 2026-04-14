# Installation

```wiki
The C-API driver is (currently) only compatible with CB2 controllers running a 1.x version of Polyscope. It cannot be used on CB3 or newer controllers.
```

## UR Control Box

-   ssh into the control box (instructions for how to do this can be
    found on the support site)
-   Create a base directory for source code, e.g. ur_ros_ctrl
-   Clone the
    [industrial_core (hydro-devel)](https://github.com/gt-ros-pkg/industrial_core)
    (Note: this is a fork of the main repo. See
    <https://github.com/ros-industrial/universal_robot/issues/40>) and
    [universal_robot (hydro-devel-c-api)](https://github.com/gt-ros-pkg/universal_robot)
    repositories into this directory
-   Download the latest
    [UR C-API](http://ur-update.dk/URsupport/Software/C-API/) version
    and extract it into this directory
-   `cd ~/ur_ros_ctrl/universal_robot/ur_ctrl_server/scripts`
-   Run `./link_simple_message.sh` to create symbolic links for scons
    compiler
-   `cd ..`, then run `scons` to compile the control server
-   Two binaries should be generated in the `./bin` folder. The
    `ur_test_server` executable can be used for testing communication or
    the controller without commanding the actual robot. `ur_ctrl_server`
    is the actual robot-side driver.

## ROS-enabled UR master machine

-   Clone the
    [industrial_core (hydro-devel)](https://github.com/gt-ros-pkg/industrial_core)
    and
    [universal_robot (hydro-devel-c-api)](https://github.com/gt-ros-pkg/universal_robot)
    repositories into your catkin workspace. You also need to install
    the [ros-controls](https://github.com/ros-controls) repositories
    ros_control, ros_controllers, realtime_tools, and control_toolbox.
    There might be updated Debian packages for these.
-   You should also install rqt, rqt-robot-dashboard, and
    rqt-robot-monitor
-   After making, you should be done installing

# Starting the Controller Drivers

\[
[System design/ROS Industrial workshop slides](http://www.kelseyhawkins.com/images/ur_c_api_contribution.pdf)
\] You might want to begin by using the test binary on the robot to test
communication, then use the actual controller once you feel you have the
hang of it.

-   Begin by stopping the tablet controller using `./stopurcontrol.sh`
    in the root directory. To restart the tablet controller, you should
    bring down the ROS driver, then run `./starturcontrol.sh`
-   Start the server on the robot by running the binary in
    `ur_ctrl_server/bin`. You should not need to touch this terminal
    again. The real controller will print out junk until the interface
    is opened.
-   On the UR master, run
    `roslaunch ur_c_api_bringup ur<5/10>_bringup.launch robot_ip:=<robot's ip>`
-   Bring up the rqt GUI by running `rqt` in the terminal.
-   Enable the plugins \"UR Dashboard\" and \"UR Joint Control\" and
    customize the layout to your liking
-   We will now begin bringing up the robot controller. Click the 3rd
    button in the dashboard to open the interface to the robot.
-   Once the state reads \"NO_POWER\", click the 4th button to turn on
    the power to the robot
-   Once the state reads \"INITIALIZING\", click the 5th button to
    unlock the safety brakes to release
-   Use the joint control GUI to calibrate each of the joints, moving
    each of them in one direction until they all say \"RUNNING\". Once
    all the joints are callibrated, all of the buttons should turn green
    and all of the states will say \"RUNNING\".
-   Bringing up the robot can be a testy process and you might have to
    restart a few times to get it to work. However, once the joints are
    calibrated, the system is fairly stable.

# Managing the controllers

You can load/start/stop/unload controllers using the controller_manager
utility `rosrun controller_manager controller_manager help`. You can
also find a GUI interface for managing controllers in rqt. See the
[ros_control](http://wiki.ros.org/ros_control?distro=hydro) page for
more information.

## Control Modes

There are multiple ways of actuating the joints provided in the UR C
API, but only one can be activated at a time. Right now there are 2
interfaces supported, the velocity (prefix: vel\_) and
position/velocity/acceleration (prefix: pva) interfaces. Every
controller which uses that particular interface should be prefixed
accordingly.

In addition, there are `*_enable_mode` controllers. To run a controller
like `pva_forward_ctrl`, `pva_enable_mode` must also be started. To
switch to, say `vel_trajectory_ctrl`, you must first stop
`pva_enable_mode` (and optionally `pva_forward_ctrl`), then start both
`vel_enable_mode` and `vel_trajectory_ctrl` to enable the trajectory
controller. This feature keeps two interfaces from running
simultaneously.

## Test Code

You can find test code for two controllers in `ur_controllers/test`. Be
careful, as this code will move the robots. However, they assume that
the appropriate controllers are already running.
