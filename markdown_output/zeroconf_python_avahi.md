![](attachment:zeroconf.png)

## Overview

[Zeroconf](http://en.wikipedia.org/wiki/Zeroconf) is a set of network
protocols that provide automatic discovery of network resources. This
package provides tools to announce the availability of the ROS Master
and to locate ROS Master nodes on the local network. This package uses
[Avahi](http://avahi.org/) to implement Zeroconf. Avahi is installed by
default on many Linux distributions. Compatibility with MacOS may be
possible in the future, and patches are greatly appreciated.

Any feedback on this package would be useful, as automatic discovery of
robots connected to the local network will be a needed for
[some applications](rind) in the near future.

## Installation

Install the ihr_tools stack.



```shell
cd ~/ros/stacks
git clone git://github.com/IHeartRobotics/iheart-ros-pkg.git
cd iheart-ros-pkg/ihr_tools
rosdep install zeroconf
rosmake zeroconf
```



For the lazy or reckless, the following should update all the config
files correctly on Ubuntu 10.04. There is currently no guarantee this
will work and it might delete your computer. 

```shell
make install
```



### Service types

Avahi does not currently support ROS service types and the build script
isn't installed by default.

The following commands will install updated files if you have not
modified them, if you have previously modified these files you should
know what to do. In the future a patch needs to be sent to the Avahi
maintainers.

Additional translations or corrections are welcome.



```shell
cp `rospack find zeroconf`/config/service-types /usr/share/avahi/service-types
cp `rospack find zeroconf`/config/service-types.db /usr/lib/avahi/service-types.db
```



### service-discovery-applet

While not required, this is a useful GUI tool for using zeroconf. It can
be installed on Ubuntu 10.04 by running the following and right clicking
the top panel and selecting add to panel.



```shell
sudo aptitude install service-discovery-applet
```



The service-discovery-applet does not support ROS service types by
default, however the following command will add support.



```shell
gconftool --load `rospack find zeroconf`/config/service-discovery-applet.xml
```



## Running

At this point there are three primary methods for using zeroconf at this
point. In the future, it may be worth looking at integrating this
functionality into [rosmaster](rosmaster).

### Launch File

The easiest option is to add a zeroconf node to the launch file of the
master. The obvious downside to this approach is that each launch file
will need to be modified to include zeroconf. The upside is that it is
simple and free of unintended consequences.



```shell
roslaunch zeroconf zeroconf.launch
```



### /etc/avahi/services

Avahi supports system-wide service configuration files. This will
announce the availability of the ROS Master service without running a
separate node. The downside of this approach is that the service will be
announced to the local network regardless of that state of rosmaster.



```shell
cp `rospack find zeroconf`/config/ros-master.service /etc/avahi/services/.
```



The provided launch file can be modified so that the zeroconf node only
provide discovery of network resources without announcing the
availability of the master.

### Patching roscore

Another approach is to add zeroconf directly to roscore startup via this
patch. This has the advantage that the services will only be announce
when rosmaster is running, and that individual launch files do not need
to be modified. The downside is that it modifies roslaunch and that
might be bad.

Think before patching\... 

```shell
more `rospack find zeroconf`/config/roscore.xml.patch
patch `rospack find roslaunch`/roscore.xml < `rospack find zeroconf`/config/roscore.xml.patch
```



## Service Example

The following command will call the discover_masters service and return
a list of Masters and its associated MASTER_URI.



```shell
rosservice call /zeroconf/discover_masters
```





```
$ rosservice call /zeroconf/discover_masters
masters: 
  - 
    master_name: Winston X. Robot
    master_uri: http://foo.local:11311
  - 
    master_name: Rob D. Robot
    master_uri: http://bar.local:11311
```



## Nodes



```shell
make install
```

0

<<MsgSrvDoc(zeroconf)>>

## Known Bugs

-   Service types probably need some sort of official approval
-   Patches need to be sent to Avahi maintainers
-   ROS Launch URIs are not currently announced, is this useful?
