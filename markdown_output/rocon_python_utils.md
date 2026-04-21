## Overview

This package is a collection of simple tools for working with python in
and around both linux and ros systems.



```wiki
||<style="text-align: center;" tablewidth="100%">Full details and usage examples are in the sphinx documentation ([[http://docs.ros.org/hydro/api/rocon_python_utils/html/|indigo]]).||
```



\

An example of some of the functions included (this will quickly get
outdated):

-   **Network**
-   Wrapper around the `ping` command to monitor connectivity of
    remote machines.
-   **Ros**
-   Catkin package crawler, generates a complete index of all catkin
    packages.
-   Rocon icon/msg converters
-   Find [resource](ROS/Concepts#Names.Package_Resource_Names) helpers
-   Retrieve the ros version in runtime.
-   **System**
-   Pythonic `which` command.
-   Pid manipulators.
-   A subprocess style `Popen` that automagically manages groups and
    accepts a callback function for process termination.
