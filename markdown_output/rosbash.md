## Overview

The `rosbash` package contains some useful bash functions and adds
tab-completion to a large number of the basic ros utilities.

{ This is done by default when following most of the standard install
instructions. The following source command only works with newer
versions of ROS. }}}} When you source the distro specific setup file
like:



```
source /opt/ros/$ROS_DISTRO/setup.bash
```

 you will implicitly get all bash-specific
command.

## Other Shells

The `rosbash` package includes limited support for `zsh` and
`tcsh` by way of sourcing the `roszsh` or `rostcsh` files
respectively. We currently do not provide documentation on these shells,
though much of the functionality is similar to the bash shell
extensions.

### fish

Fish support has been added to rosbash. To activate it:


```
source /opt/ros/$ROS_DISTRO/share/rosbash/rosfish
```

 you can add this statement to the `conf.d`
directory to execute it automatically on login, such as
`/.config/fish/conf.d/rosfish.fish`.

Sourcing a catkin workspace requires using
[bass](https://github.com/edc/bass): 

```
bass source ~/catkin_ws/devel/setup.bash
```



You can have this done automatically as soon as you `cd` to the
workspace directory, by adding a further config file (e.g.
`/.config/fish/conf.d/catkin.autosource.fish`):


```
function catkinSource --on-variable PWD
    status --is-command-substitution; and return
    if test -e ".catkin_workspace"; or test -e ".catkin_tools"
        bass source devel/setup.bash
        echo "Configured the folder as a workspace"
    end
end
```



## Command line utilities

`rosbash` includes the following command line utilities:

-   [roscd](#roscd) - change directory starting with package, stack, or
    location name
-   [rospd](#rospd) - `pushd` equivalent of `roscd`
-   [rosd](#rosd) - lists directories in the directory-stack
-   [rosls](#rosls) - list files of a ros package
-   [rosed](#rosed) - edit a file in a package
-   [roscp](#roscp) - copy a file from a package
-   [rosrun](#rosrun) - run executables of a ros package

### roscd

`roscd` allows you to change directories using a package name, stack
name, or special location.

Usage:



```
roscd <package-or-stack>[/subdir]
```

 For example:



```
roscd roscpp
```

 You can continue to use a relative path after
the package name to go further into the package:



```
roscd roscpp/include/ros
```

 `roscd` without argument will take you to
`$ROS_WORKSPACE`.

Additionally, the `ROS_LOCATIONS` environment variable can be used to
add additional special locations for use with `roscd`.
`ROS_LOCATIONS` is a colon-separated list of `key=path` pairs.

For example, adding the following to your `.bashrc` file:



```
export ROS_LOCATIONS="pkgs=~/ros/pkgs:dev=~/ros/dev"
```

 Will then allow you to type:



```
$ roscd dev
```

 and end up in `/ros/dev`.

### rospd

`rospd` is the `pushd` equivalent of `roscd`. It allows you to
keep multiple locations in a directory-stack while still using ros
package names. You can then use the number of any directory in your
directory stack to jump back there.

For example:



```
leibs@bar:~$ rospd hokuyo_node/
0 ~/ros/pkgs/laser_drivers/hokuyo_node
1 ~
leibs@bar:~/ros/pkgs/laser_drivers/hokuyo_node$ rospd roscpp_tutorials/
0 ~/ros/pkgs/ros_tutorials/roscpp_tutorials
1 ~/ros/pkgs/laser_drivers/hokuyo_node
2 ~
leibs@bar:~/ros/pkgs/ros_tutorials/roscpp_tutorials$ rospd laser_pipeline/
0 ~/ros/dev/laser_pipeline
1 ~/ros/pkgs/ros_tutorials/roscpp_tutorials
2 ~/ros/pkgs/laser_drivers/hokuyo_node
3 ~
leibs@bar:~/ros/dev/laser_pipeline$ rospd 1
0 ~/ros/pkgs/ros_tutorials/roscpp_tutorials
1 ~/ros/pkgs/laser_drivers/hokuyo_node
2 ~
3 ~/ros/dev/laser_pipeline
```



### rosd

`rosd` lists the directories in your directory stack. This is for use
with `rospd`.

For example:



```
source /opt/ros/$ROS_DISTRO/share/rosbash/rosfish
```

0

### rosls

`rosls` allows you to view the contents of a package, stack, or
location.

For example:



```
source /opt/ros/$ROS_DISTRO/share/rosbash/rosfish
```

1

### rosed

`rosed` allows you to easily edit files in a ROS package by typing the
package name and the name of the file you want to edit:



```
source /opt/ros/$ROS_DISTRO/share/rosbash/rosfish
```

2 Note: you can specify ANY file in a package,
including those further down within the file hierarchy. If you specify
an ambiguous file you will be prompted to select one.

For example:



```
source /opt/ros/$ROS_DISTRO/share/rosbash/rosfish
```

3 The default editor for rosed is vim. To use a
different editor, set the `EDITOR` environment variable. E.g., in your
/.bashrc:



```
source /opt/ros/$ROS_DISTRO/share/rosbash/rosfish
```

4 This example makes emacs the default editor.

You also can change the editor for one `rosed` call on the fly:



```
source /opt/ros/$ROS_DISTRO/share/rosbash/rosfish
```

5

### roscp

`roscp` allows you to conveniently copy a file from a package. Similar
to `rosed` you can specify any file in the package regardless of
hierarchy.

For example:



```
source /opt/ros/$ROS_DISTRO/share/rosbash/rosfish
```

6 Will end up copying the file from
`/ros/pkgs/ros_tutorials/roscpp_tutorials/talker/talker.cpp`

### rosrun

`rosrun` allows you to run an executable in an arbitrary package from
anywhere without having to give its full path or `cd`/`roscd` there
first.

Usage:



```
source /opt/ros/$ROS_DISTRO/share/rosbash/rosfish
```

7 Example:



```
source /opt/ros/$ROS_DISTRO/share/rosbash/rosfish
```

8 It's also possible to pass a `parameter`
using the following syntax (replace the `` with an `_`):



```
source /opt/ros/$ROS_DISTRO/share/rosbash/rosfish
```

9 Example:



```
bass source ~/catkin_ws/devel/setup.bash
```

0

\...or run with a given name:



```
bass source ~/catkin_ws/devel/setup.bash
```

1 Example:



```
bass source ~/catkin_ws/devel/setup.bash
```

2 For more information about remapping, see:
[Remapping Arguments](https://wiki.ros.org/Remapping%20Arguments)

Starting in **Indigo**, rosrun has a `\--prefix` option which can be
used to run a node in gdb or valgrind.

Example:



```
bass source ~/catkin_ws/devel/setup.bash
```

3 For more example prefixes, see:
[Roslaunch Nodes in Valgrind or GDB](http://wiki.ros.org/roslaunch/Tutorials/Roslaunch%20Nodes%20in%20Valgrind%20or%20GDB)

## Tab Completion

`rosbash` enables tab-completion for its own tools and for a number of
other ros utilities: [rosmake](rosmake), [roslaunch](roslaunch),
[rosparam](rosparam), [rosnode](rosnode), [rostopic](rostopic),
[rosservice](rosservice), [rosmsg](rosmsg), [rossrv](rossrv),
[rosbag](rosbag).

There are a couple of generic completion rules that may be appropriate
for other utilities. Looking through the `rosbash` source may provide
insights into replicating similar functionality for other nodes,
however, the code is not yet nicely generalized or re-usable. In a
future release of ROS, we plan to incorporate a more generically
re-usable tab-completion framework into rosbash and the other common
shells used by ROS.
