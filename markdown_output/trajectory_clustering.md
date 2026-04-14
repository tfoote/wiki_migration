[cyphy_people_mapping](cyphy_people_mapping):[people_tracker](people_tracker)/trajectory_clustering/[map_creation](map_creation)

## Installation

This package depends on Kasper Peeters\' tree.hh library for C++. Follow
the instructions [here](http://tree.phi-sci.com/download.html) to
install and compile it.

You\'ll need to edit CMakeLists.txt to reflect the location of the
tree.hh library. Specifically, set THIRDPARTY_SRCS to the parent
directory of the \'\'tree-2.81\'\' directory.

```
set(THIRDPARTY_SRCS "/home/your_name/Thirdparty" CACHE STRING "Location of Thirdparty Source Directory")
```
