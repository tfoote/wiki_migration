## Overview

A small GUI for checking the status of your Kobuki and access some of
its basic functionalities (e.g. LEDs).

## Usage

1\. Fire up Kobuki and launch the minimal configuration in a new
terminal ```
$ roslaunch kobuki_node minimal.launch
```

2\. To start the dashboard execute the below in a separate terminal.
```
$ rosrun kobuki_dashboard kobuki_dashboard
```

3\. Play with it!

  -- ----------------------------------------------------------------------------------------------------- --
     \<tablestyle=\"width: 100%\"\>                                                                        
     \<style=\"text-align: center;\"\>![Kobuki\'s dashboard\|width=70%](attachment:kobuki_dashboard.png)   
  -- ----------------------------------------------------------------------------------------------------- --

The kobuki_dashboard is also part of the
[turtlebot_dashboard](turtlebot_dashboard). In order to get the battery
statuses, you need to launch the
[minimal configuration of TurtleBot](turtlebot_bringup#Launch_Files).
