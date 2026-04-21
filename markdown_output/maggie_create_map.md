## Overview

This package provides basic functionality for create a map.

### Device Dependencies

For launching this project, it is necessary to have the next device:

-   [Maggie's Base](maggie_base)
-   [Sick](sicktoolbox)
-   [Hokuyo](hokuyo_node)

## Launch File Examples

In a terminal window, start the process to get the map information:



```
$ roslaunch maggie_create_map maggie_mapping.launch robot:=maggie
```



In another terminal window, start the process to save the map:



```
$ roslaunch maggie_create_map save_map.launch robot:=maggie
```


