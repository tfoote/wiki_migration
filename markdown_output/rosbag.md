## See Especially

1\. [rosbag/Commandline](rosbag/Commandline) 1.
[rosbag/Cookbook](rosbag/Cookbook) 1. [rosbag/Code API](rosbag/Code API)

## Overview

The `rosbag` package provides a command-line tool for working with
[bags](Bags) as well as code APIs for reading/writing bags in
[C++](rosbag/Code API#cpp_api) and [Python](rosbag/Code API#py_api).

-   To find out more about the `rosbag` command-line tool, see
    [rosbag Command-line Usage](rosbag/Commandline) and
    [Cookbook examples](rosbag/Cookbook)

```{=html}
<!-- -->
```
-   `rosbag` has code APIs for reading and writing bags in either C++
    or Python. For a description of these APIs, see
    [rosbag Code API](rosbag/Code API)

```{=html}
<!-- -->
```
-   For technical details on the contents of bag files, see
    [Bag file format](Bags/Format)

```{=html}
<!-- -->
```
-   Outside of `rosbag` package, from [groovy](groovy) there's a gui
    client [rqt_bag](rqt_bag).

Overview in addition:

[Youtube](https://www.youtube.com/watch?v=pwlbArh_neU)

## Stability

The rosbag command-line tool and code APIs are **stable**. Every effort
will be made to maintain backwards compatibility.

The main new feature being planned for `rosbag` is the addition of a
ROS API for interacting with the playing and recording nodes via service
calls.
