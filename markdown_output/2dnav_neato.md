This package has been renamed to [neato_2dnav](neato_2dnav) in groovy
and later to conform to package naming standards.

## Overview

This package contains configuration and launch files for running the
navigation stack with the Neato XV-11. It is currently still under
active development.

\<\<Youtube(<http://www.youtube.com/watch?v=bWwwssBjg6M>)\>\>

## Running

You\'ll likely need to create your own map, but:
```
roslaunch neato_node bringup.launch
roslaunch 2dnav_neato move_base.launch
```

## Creating Maps

[gmapping](gmapping) can be used to create maps, as with any other
robot. We\'ve yet to find just the right set of parameters (work on the
beam likelihood is probably needed), but the following seems to work on
the Neato for smaller maps: ```
rosrun gmapping slam_gmapping scan:=base_scan _srr:=0.001 _srt:=0.001 _str:=0.000001 _stt:=0.000001 _linearUpdate:=0.5 _angularUpdate:=0.4
```
