## Overview

This is an extension of [Slime](http://common-lisp.net/project/slime/)
(a "contrib") that helps you to deal with ASDF systems in ROS
packages. It also adds a REPL shortcut `ros-load-system` to the slime
REPL.

## Installation

### For a Debian package

```
$ sudo apt-get install ros-DISTRO-slime-ros
```

Then call the initialization script that generates `.sbclrc` in your
home directory for configuring your SBCL.

```
$ rosrun slime_ros slime_ros_init
```

And then add the following to your
[Emacs configuration file](http://www.emacswiki.org/emacs/InitFile):

```
(require 'slime-config "/opt/ros/DISTRO/share/slime_ros/slime-config.el")
```

### From source

The most up-to-date version of `slime_ros` code can be found
[here](https://github.com/code-iai/ros_emacs_utils). Installation
instructions are in the README file. What you'll need to do will be
something like the following:

```
$ cd YOUR_CATKIN_WS/src
$ wstool set ros_emacs_utils --git https://github.com/code-iai/ros_emacs_utils.git
$ wstool update ros_emacs_utils
$ cd ..
$ catkin_make
$ catkin_make install
$ emacs -nw ~/.emacs.d/init.el # edit your emacs configuration file
```

## How to use

If you've set up your emacs init file correctly you should be able to
start the REPL by typing `M-x slime`. Now, by pressing `,` (coma) in
an empty REPL prompt, you can select the shortcut `ros-load-system`.
Press enter and select a ROS package and an ASDF system inside this ROS
package. Slime will set the variable
`ros-load:\*current-ros-package\*` and perform a load operation on the
selected system.

The package contains one customization variable,
`slime-ros-completion-function`. It allows the user to select ido mode
completion or similar completion mechanisms. To change its value, use
`M-x customize-group slime-ros`.
