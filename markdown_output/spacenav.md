  -- ------------------------------------------------------------------------------------------------------------------- --
     \<#FFFF00\> \'\'\'As of joystick_drivers 1.9.0 (ROS Groovy release), the spacenav package has been removed.\'\'\'   
     \<#FFFF00\> \'\'\'The low-level spacenav driver is now supplied by system-level package management systems.\'\'\'   
  -- ------------------------------------------------------------------------------------------------------------------- --

## Using this Package

This package is provided because [spacenav_node](spacenav_node) requires
\'\'\'spacenavd\'\'\' and \'\'\'libspacenav\'\'\' which are not present
in all supported Linux distributions. The
[spacenav_node tutorial](spacenav_node/Tutorials/UsingTheSpacenavNode)
explains how to use this package.

## Building SpaceNav

Simply type:

```
$ rosmake spacenav
``` The \"rosmake\" checks out and builds a version
of \'\'\'spacenavd\'\'\' and \'\'\'libspacenav\'\'\' that has been
tested with [spacenav_node](spacenav_node).
