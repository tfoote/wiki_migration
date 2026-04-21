## Overview

The `roslaunch` [package](Packages) contains the `roslaunch` tools,
which reads the [roslaunch .launch/XML format](roslaunch/XML). It also
contains a variety of other support tools to help you use these files.

Many ROS packages come with "launch files", which you can run with:
```
$ roslaunch package_name file.launch
```

These launch files usually bring up a set of nodes for the package that
provide some aggregate functionality.

To find out more about the main `roslaunch` tool and other
command-line tools, please consult:

-   [roslaunch Command-line Usage](/Commandline Tools)

`roslaunch` uses XML files that describe the nodes that should be run,
parameters that should be set, and other attributes of launching a
collection of ROS [nodes](Nodes). For a specification of this XML
format, please see:

-   [roslaunch .launch/XML format](roslaunch/XML)

`roslaunch` was designed to fit the ROS architecture of complexity via
composition. Understanding `roslaunch`'s architecture will give you
better insight in how to construct your `.launch` files and better
debug remote vs. local launches.

-   [roslaunch Architecture](/Architecture)

A simple usage example of the Python API can be found here:

-   [roslaunch/API Usage](roslaunch/API Usage)

## roscore

[roscore](roscore) is a specialization of the `roslaunch` tool for
bringing up the "core" ROS system. A roslaunch will automatically
start roscore if it detects that it is not already running (unless the
\--wait argument is supplied). For more information, please see the
[roscore](roscore) documentation. Note: due to a
[race condition](https://github.com/ros/ros_comm/issues/1831), roslaunch
should not be used to guarantee a singleton instance of roscore.

## Stability/Roadmap

The launch file syntax itself is **stable**, and every effort will be
made to provide backwards compatibility with new features.

The code API of `roslaunch` is **very unstable** and should not be
used directly. In order to support the new features that are being
planned, it may be necessary to make major, incompatible changes to the
programmatic API.

There are many new features being planned for `roslaunch`. These
include new features within the launch file syntax, GUI tools for
interacting with launch files more effectively, network API, better
coordination between separate launch files, and more.

Ref. [SIG for roslaunch](sig/roslaunch)

## Tutorials

<<TutorialChain(roslaunch/Tutorials/Roslaunch tips for larger
projects)>>

## Syntax Highlighting

Since roslaunch XML allows inline YAML parsing, it is beneficial to have
syntax (highlighting and indentation) support in your favorite editor.

-   [Emacs](roslaunch/Tutorials/Using Roslaunch with Emacs)
-   [Vim](https://gist.github.com/jbohren/5964014)

## Catkin

The `roslaunch_add_file_check` CMake macro can be used to check launch
files for common errors such as missing arguments, dependencies,
packages, or nodes.

The following is how you would check all `\*.launch` files in a
package's "`launch`" directory:

```cmake
find_package(catkin REQUIRED COMPONENTS roslaunch)
roslaunch_add_file_check(launch)
```

NOTE: `roslaunch_add_file_check` takes only one directory at a time.

The check runs during
[tests](http://docs.ros.org/api/catkin/html/howto/format2/run_tests.html).
So something like following is cleaner.

```cmake
if (CATKIN_ENABLE_TESTING)
  find_package(roslaunch REQUIRED)
  roslaunch_add_file_check(launch)
endif()
```

Since you need to find `roslaunch` in `find_package` as above, you
better explicitly add a dependency in your `package.xml` as following:

```
<build_depend>roslaunch</build_depend>
```

The macro accepts either a single directory or file argument. Basically,
it adds additional test targets into catkin generated Makefile.

**Note:** these \*.launch file tests can also be initiated using console
tool called
[roslaunch-check](roslaunch/Commandline Tools#roslaunch-check) OR
[roslaunch-deps](roslaunch/Commandline Tools#roslaunch-deps).

### Options for check during Catkin

Pass an optional argument "`USE_TEST_DEPENDENCIES`" to
`roslaunch_add_file_check` as the following example, if your package
defines dependency for the tests (e.g. `test_depend`). This avoids
issues that happen during tests such as
[this issue](http://answers.ros.org/question/262558/buildfarm-missing-package-dependencies-pkg_namepackagexml).

```cmake
find_package(catkin REQUIRED COMPONENTS roslaunch)
roslaunch_add_file_check(launch USE_TEST_DEPENDENCIES)
```

## GUI

A few graphical tools are available to support `launch`
functionalities of ROS.

-   [rqt_launch](rqt_launch) (very experimental) can run launch files.
-   [rqt_launchtree](rqt_launchtree) allows you to interactively
    introspect launch files.
-   [roslaunch_to_dot](roslaunch_to_dot) converts a launch file tree to
    a graph and save into a dot file.

## Video Tutorial on Launch Files

[Youtube](https://www.youtube.com/watch?v=cTXHIEYXKpM)
