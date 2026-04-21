**Package Summary** ROSRemote is a framework that helps users to control
remote robots and recover information from them as well as from remote
masters. It is possible to send common ROS commands like \"rostopic
list\" to a remote master and recover all the topics it is publishing at
the time.

-   Maintainer: Alyson Benoni Matias Pereira \<alysonmp AT gmail DOT
    com\>
-   Author: Alyson Benoni Matias Pereira \<alysonmp AT gmail DOT com\>,
    Guilherme Sousa Bastos \<sousa AT unifei.edu DOT br\>
-   Source: git <https://github.com/alysonmp/ROSRemote.git> (branch:
    master)

## Overview

ROS is becoming a widespread tool for controlling robots, but it was
build to work offline and trust in third part packages for working on
cloud. ROSRemote was created to help user to easily control a robot on
cloud. To do so, it was used [SpaceBrew](http://docs.spacebrew.cc/)
framework that helps creating connections between two or more devices by
finding their public IPs and establishing a connection among them, this
connection is done through a server that can be easily implemented by
the user, in case he/she does not want to use the free
[SpaceBrew](http://docs.spacebrew.cc/) server.

ROSRemote is simple and only use one node to work. This node creates a
[Spacebrew](http://docs.spacebrew.cc/) client and also start a ROS
service called /send_data, that is responsible for sending the
information to the remote device. In order to run ROS, the devices must
have a master instance running on them, so, ROSRemote are able to
connect two masters through [SpaceBrew](http://docs.spacebrew.cc/), as
shown in the figure below.

![text describing image\|width=\"600\"](attachment:fluxo_pacote.png)

Since [SpaceBrew](http://docs.spacebrew.cc/) gives the user the
possibility to connect two or more masters among themselves, it is
possible for the user to send a command from his local machine and
receive the answer at the same time that other connected machines also
receive the answer.

## Paper

A paper named *ROSRemote, using ROS on cloud to access robots remotely*
was presented at ICAR 2017.

## Basic Usage

### Starting ROSRemote service

In order to use ROSRemote first it is necessary to start the master on
all devices that the user want to connect, it includes robots and
computers. This is done by using the command.

```
roscore
```

After that, the user needs to start the package that has the service
needed to send the information, tha package is called cloud_ros and the
main file, that starts the node, is main_cloud_ros. So, to run the
package the user needs the following command.

```
rosrun cloud_ros main_cloud_ros
```

This will create [Spacebrew](http://docs.spacebrew.cc/) client as well
as start the service /send_data, that will be called to send the
information to the remote devices. The last thing the user needs to do
to connect the devices is open the
[Spacebrew](http://docs.spacebrew.cc/) *Web Admin Tool* and connect the
clients, this tool is opened by typing the server URL in the browser. If
the user is using the [Spacebrew](http://docs.spacebrew.cc/) free
server, the address would be
[Spacebrew server](http://spacebrew.github.io/spacebrew/admin/admin.html?server=sandbox.spacebrew.cc/).

After the connection is made, all the user has to do is type the ros
command in quotes preceded by the calling of the /send_data service. In
the next example the user is calling the command rostopic list and will
receive the answer from a remote master or robot.

```
rosservice call /send_data "rostopic list"
```

Not all ros features were already implemented, but can be done in the
future. Also new developers can create their own application using
ROSRemote to run on cloud and access remote devices.

## ROSRemote features

As described before, not all ros features were introduced in this
package, but some of the most important ones were implemented. They make
possible a huge range of applications to be created and there is also
the possibility for the user/developer to create more, increasing the
usability of the package.

All the existing features will be demonstrated in the next sections, as
well as a brief tutorial on how to use them in ROSRemote.

### Rostopic

Rostopic is designed to get information about the topics running on a
device, in the features implemented in ROSRemote includes rostopic list,
rostopic echo and rostopic info and they are explained next.

#### Rostopic list

Rostopic list returns to the user a list of all currently published
topics. In order to use this command in ROSRemote, the user needs to
insert the following.

```
rosservice call /send_data "rostopic list"
```

#### Rostopic echo

Rostopic echo returns to the user what a certain topic is publishing.
The main difference in this command between ros and ROSRemote, is that,
due to a [Spacebrew](http://docs.spacebrew.cc/) limitation, the user
needs to send the publishing frequency, which cannot be too high, like
15 or more hertz, for example, this means that in each second, the user
will receive 15 answers from the topic running on remote devices.

Differently from rostopic list, where the user just need to send the
command, in echo it is necessary to send the topic name and also the
publication frequency.

```
rosservice call /send_data "rostopic echo /topic_name frequency_rate"
```

If the user wants to echo the cmd_vel topic, for example, in a rate of
five times per second, the command would be.

```
rosservice call /send_data "rostopic echo /cmd_vel 5"
```

#### Rostopic info

Rostopic info shows the information about topics, such as the node that
is publishing it. Its syntax is the same as the rostopic echo but in
this case it is not necessary to send the publish rate.

```
rosservice call /send_data "rostopic info /topic_name"
```

Using the cmd_vel example, the user can send the command to recover the
cmd_vel information.

```
rosservice call /send_data "rostopic info /cmd_vel"
```

### Rosrun

Rosrun is designed to start a package in ros, the same way the user can
start a package remotely by using the simple command.

```
rosservice call /send_data "rosrun package_name executable_name"
```

The only package that the user can not start remotely is the ROSRemote
package, because it already has to be running on the remote machine. But
assuming that the user would do that, just for example purposes, the
syntax would be.

```
rosservice call /send_data "rosrun cloud_ros main_cloud_ros"
```

### Rosservice

Rosservice is designed to get information and start services running in
a device. In the features implemented in ROSRemote includes rosservice
list, rosservice args, rosservice call, rosservice node, rosservice type
and they are explained next.

#### Rosservice list

Lists all the services running in a device. The syntax of this
functionality is almost the same as the rostopic list. It is also
important to remember that whenever the user wants to send the commands
to a remote master, it needs to call the /send_data service.

```
rosrun cloud_ros main_cloud_ros
```0

#### Rosservice args

Shows all the arguments needed to call a determined service. The syntax
is also simple and very similar to rostopic echo, but instead of sending
the topic name, the user sends the service name.

```
rosrun cloud_ros main_cloud_ros
```1

#### Rosservice call

Call a service that is running in a device. The syntax is the same as
the one in the rosservice args, but the user needs to change args by
call.

```
rosrun cloud_ros main_cloud_ros
```2

In ROSRemote, if the user wants to, it can call the /send_data service
in a remote device, it is not necessary since one can connect to which
device is wanted, but to exemplify, users can use the command to call
itself in a remote master and send any command, like rostopic list, for
instance.

```
rosrun cloud_ros main_cloud_ros
```3

In this case the remote device will send the command to another remote
device and the user will receive the answer.

#### Rosservice node

Rosservice node shows which node is providing a certain service, the
only thing the user needs to know is the service name.

```
rosrun cloud_ros main_cloud_ros
```4

#### Rosservice type

ROsservice type shows what is the type of a service, very useful when
the user needs to create a software that call this service, because it
is necessary to know which type it has in order do correctly call it.
The syntx is also the same than most of the rosservice commands.

```
rosrun cloud_ros main_cloud_ros
```5

Alternatively, the user can send an extra parameter to the command to
recover the srv file of the service, in case this service was developed
by a user and uses a srv that was created by him/her.

```
rosrun cloud_ros main_cloud_ros
```6

### Roscommands

The roscommands is a feature specially developed for ROSRemote that
helps user to remotely control robots. For the purpose of this
development, it was used RosAria teleop. The fisrt thing the user needs
to do is to connect to the remote robot using ROSRemote and RosAria, in
this case, the command is.

```
rosrun cloud_ros main_cloud_ros
```7

This will start RosAria on the robot connected in the IP given by the
user. It is necessary to send the IP and the port, an example would be
as follows.

```
rosrun cloud_ros main_cloud_ros
```8

When calling this package in ROS, the user has to use := instead of @,
but since := is a reserved Python command, it was not possible to use it
in the project, so it was necessary to change into an @ and them,
internally, make ROSRemote change to the correct one.

After starting the RosAria, the user needs to find out what is the name
of the topic that the robot publishes, in the testes made in ROSRemote,
the topic name was Rosaria and that is the name needed to set the robot
that will receive the commands. Since ROSRemote publishes directly on
the cmd_vel of the robot to make it walk, the user needs to set this
name to make the ROSRemote work.

```
rosrun cloud_ros main_cloud_ros
```9

Then users are already able to send teleoperational commands to the
robot by using the arrow keys on keyboard, just like it would do if the
robot was in a local network.
