## Overview

[Youtube](https://www.youtube.com/watch?v=oajlOQfqJiw)

## How to try

### Install

{ }}}}

{ }}}}

### Startup

1\. run as a single GUI

```
$ rosrun rqt_ez_publisher rqt_ez_publisher
```

2\. run as plugin of [rqt](rqt)

```
$ rqt
```

Plugins -\> Topics -\> Easy Message Publisher

Input topic name -\> You got GUI

## How to Use

![](attachment:cmd_vel_with_caption.png)

![](attachment:joint_states_with_caption.png)

You can input topic name and attributes string, like rqt_plot instead of
topic name. For example, \'\'\'\'\'/cmd_vel/linear/x\'\'\'\'\' or
\'\'\'\'\'/joint_states/position\[1\]\'\'\'\'\'

## Examples

It is ok if there are many topics. ![](attachment:mix.png)

## Preconditions

-   The topic you want to publish should be already subscribed by other
    nodes. 1. launch other nodes 1. start rqt_ez_publisher 1. select
    topics from combobox
-   header/stamp is updated by rospy.Time.now()
-   geometry_msgs/Quaternion is converted to RPY angles
-   string is updated when input Enter key

## Feedbacks

Any feedback is welcome! (Sorry for slow response\...) Please add issues
on [github](https://github.com/OTL/rqt_ez_publisher/issues).

## FAQ

### Q. Plugin not found!

```
qt_gui_main() found no plugin matching "rqt_ez_publisher"
```

A. Try this

```
$ rm ~/.config/ros.org/rqt_gui.ini
```

### Q. How can I change publish repeat rate

A. Click \"config (gear) icon\" -\> set repeat interval \[ms\]

### Q. Can I save/load the settings

-   save: Click \"config (gear) icon\" -\> click \"save to file\" button
-   load: rosrun rqt_ez_publisher rqt_ez_publisher \--slider-file
    /a.yaml
