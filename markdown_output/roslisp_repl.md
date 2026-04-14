## Overview

This package provides you with a Lisp REPL configured to be used to
program ROS packages as well as an integrated IDE for programming in
Common Lisp with Emacs (see
[Slime](http://common-lisp.net/project/slime/)).

What it actually does is just starting your Emacs with a nice
configuration for Lisp and then starting Slime.

## Installation

### Installation from a Debian package

\`roslisp_repl\` is distributed through the ROS release infrastructure.

```
$ sudo apt-get install ros-DISTRO-roslisp-repl
```

### Installation from source

The most up-to-date version of \`roslisp_repl\` code can be found
[here](https://github.com/code-iai/ros_emacs_utils). Installation
instructions are in the README file. What you\'ll need to do will be
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

To use the \`roslisp_repl\` just run the executable:

```
$ roslisp_repl
```

If it can\'t be found try

```
$ source ~/.bashrc
$ rospack profile
$ rosrun roslisp_repl roslisp_repl
```

If you would like to use your own Emacs configuration with the REPL and
you\'re on ROS Indigo+ see the installation instructions of the
[slime_ros](slime_ros) package. It is automatically installed as a
dependency of \`roslisp_repl\`. If you\'re sure you will always be using
the REPL only with your own Emacs configuration, consider installing
solely [slime_ros](slime_ros) instead of \`roslisp_repl\` in the future.

If you\'re on earlier versions of ROS, look through the \`roslisp_repl\`
configuration file, \`repl-config.el\` and copy-paste the relevant code
into your Emacs config file.
