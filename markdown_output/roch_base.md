  -- ---------------------- -- -- -- -------------------------- --
     [English](roch_base)            [简体中文](cn/roch_base)   
  -- ---------------------- -- -- -- -------------------------- --

See [Robots/Roch](Robots/Roch) get more installation or tutorials and
information, roch_base based on [ros_control](ros_control).

And also refrence [husky_base](husky_base).

## Overview

The \`roch_base\` package has some demos for testing whether normal for
data of sensors, such as ultrasonic， psd, cliff etc. And also has a
demo of launch files, you can checkout what in. \'\'\'roch_node\'\'\' is
core node for \`roch_base\` package. And all hardware interface is
configured by [roch_control](roch_control) package. { }}}}

## Demos

There are have about 5 demos you can run for testing:

-   test_encoder
-   test_imu
-   test_platformInfo
-   test_rangefinder
-   test_speed

And they have common steps for using:

At first, make sure you had finished under:

-   1.Roch has power on.
-   2.USB cable Roch and your computer.
-   3.Make sure you has run \'\'\'\'\'roscore\'\'\'\'\'.

```
rosrun roch_base test_<name_you_want>
```

## Report a Bug

Use github to
[report bugs](https://github.com/SawYer-Robotics/roch_robot/issues) or
[request features](https://github.com/SawYer-Robotics/roch_robot/issues).
