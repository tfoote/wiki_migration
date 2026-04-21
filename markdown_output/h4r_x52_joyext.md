## Overview

ROS package to access the MFD of the Saitek X52 Pro Joystick.

## Installation

Firstly, make sure git is installed. On Ubuntu, run:

```
$ sudo apt-get install git-core
```

### Install system dependencies

Ubuntu has .deb packages for libx52pro, which can be easily installed
using apt-get:

```
$ sudo apt-get install libx52pro0 libx52pro-dev
```

### Download and build package source

Assuming a catkin workspace has been created as described in
[catkin/Tutorials/create_a_workspace](catkin/Tutorials/create_a_workspace),
follow the steps below.

Download the source code to your catkin workspace and build it:

```
$ cd ~/catkin_ws/src
$ git clone https://github.com/Hacks4ROS/h4r_x52_joyext.git -b master
$ cd ~/catkin_ws
$ catkin_make
```

## API

For detailed information regarding nodes and so forth, please check the
Code API.

## Bug reports and feature requests

<<GitHubIssues(Hacks4ROS/h4r_x52_joyext)>>
