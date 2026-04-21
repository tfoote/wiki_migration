## NOTICE

This package should be replaced by newer
[denso_robot_ros](denso_robot_ros) package which is made and maintained
by the robot vendor (DENSO) officially. \'denso\' package remains for
reference but may not be released in next ROS distro.

## Robots using denso package

  -- ------------------------------------------------------------------------------ -- ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------- -- ---------------------------------- --
     \'\'\'Maker\'s web site\'\'\'                                                     \'\'\'Image of robots\'\'\'                                                                                                                                                     \'\'\'ROS package (if any)\'\'\'   
     [VS-060](http://www.denso-wave.com/ja/robot/product/five-six/vs050-060.html)      [![VS-060 taken at iREX2013 by @ysuga\|height=\"175\"](attachment:vs060_denso_bySugaSan_irex2013.jpg)](http://www.denso-wave.com/ja/robot/product/five-six/vs050-060.html)      [vs060](vs060)                     
  -- ------------------------------------------------------------------------------ -- ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------- -- ---------------------------------- --

## Install

On your \`Ubuntu\` machine where \`ROS\` [hydro](hydro) is installed:

```
$ sudo apt-get install ros-hydro-denso
``` This command will have the following packages
at minimum installed:

-   From \`denso\` package suite: [denso_controller](denso_controller),
    [denso_launch](denso_launch), [denso](denso), [vs060](vs060),
    [vs060_moveit_config](vs060_moveit_config)
-   [open_controllers_interface](open_controllers_interface)

### During experimental phase

It\'s recommended while this package is still in the experimental status
that you install the latest binary from \`shadow-fixed\` repository. If
you\'re unsure what it is, do the following:

1\. Open /etc/apt/sources.list.d/ros-latest.list. If it doesn\'t exist,
create one. 1. Comment out any entries taht contain packages.ros.org 1.
Add these lines: ```
# Shadow-fixed
        deb http://packages.ros.org/ros-shadow-fixed/ubuntu precise main
        deb-src http://packages.ros.org/ros-shadow-fixed/ubuntu precise main
``` 1. Run on terminal:
```
$ sudo apt-get update
        $ sudo apt-get dist-upgrade
``` 1. Remove above portion of entries once
\`apt-get\` finishes.

Again, do NOT forget to roll back \`apt\`\'s source list by number 5
above. \`shadow-fixed\` is a testing bed and binaries stored are not yet
officially released.

Latest version is, as of 12/11/2013, \`0.2.5\`, or if you\'re doubtful
about it (yes we can easily forget to update the wiki), check it out
[at build status page](http://www.ros.org/debbuild/hydro.html?q=denso).

## Running robots

[denso_launch](denso_launch) package wiki page shows how to run robots
virtually.

[Included page denso_launch,,from=\"##begin_howto_roslaunch_vs060\",to=\"##end_howto_roslaunch_vs060\" not found](Included page denso_launch,,from="##begin_howto_roslaunch_vs060",to="##end_howto_roslaunch_vs060" not found)

## Software Design, Writing Programs

### Module Relations

[![](https://docs.google.com/drawings/d/1-AcMxG_kE2yUP-11OwdutZuTR2hOF0DUjF5nnitHhNs/pub?w=909&h=634)](https://docs.google.com/drawings/d/1-AcMxG_kE2yUP-11OwdutZuTR2hOF0DUjF5nnitHhNs/pub?w=909&h=634)

. Fig. (click to magnify) Software components diagram for DENSO robot.

### How to write programs

See [tutorial page](open_industrial_ros_controllers/Tutorials) in
[open_industrial_ros_controllers](open_industrial_ros_controllers)
package.

### Software architecture thoughts

As of today \`denso\` is built on top of
[open_industrial_ros_controllers](open_industrial_ros_controllers), yet
another controller package in \`ROS\` (in addition to
[industrial](industrial), [ros_control](ros_control), [hrpsys](hrpsys)
to name a few) for a number of reasons. This should be considered
temporary and is planned to change. Please see
[a summary here](open_industrial_ros_controllers#Relationship_to_existing_contoller_components)
for a bit more detail.

## Community

-   Ask on [answers](http://answers.ros.org/) with appropriate tags eg.
    \`denso\`, \`vs060\`.
-   If you\'re confident enough that the issue you\'re seeing is a bug,
    opening a ticket on the issue tracker on github (should be noted at
    the top of this page) is very appreciated.

## Future plan

-   Core controller refactoring as mentioned above.

## Reference

Okada et.al (2013), \"Design and Development of Open Source Contoller
for Industrial Robots\", 14th System Integration Division Annual
Conference, Kobe, Japan (in Japanese)
