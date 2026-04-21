For a graphical version of `rosgraph`, please see
[rqt_graph](rqt_graph).

## Command-line tools

### rosgraph

`rosgraph` is a console version of [rqt_graph](rqt_graph). It
periodically displays information about your current graph in a text
format. To use it, simply type:

```
$ rosgraph
```

## Python API

The `rosgraph` package contains the `rosgraph.masterapi` module,
which implements a Python library for interacting with the low-level ROS
Master API.

For other Python libraries for interacting with the ROS graph, see
[rostopic](rostopic), [rosnode](rosnode), [rosservice](rosservice), and
[rosparam](rosparam).

## Roadmap

There are no plans to update the `rosgraph` tool at this time. The
Python API may expand as necessary to provide access to other ROS graph
primitives, though those are currently covered by the
[rostopic](rostopic), [rosnode](rosnode), and [rosservice](rosservice)
libraries as well.
