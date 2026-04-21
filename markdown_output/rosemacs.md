![](attachment:real_programmers.png)

-Credit: Randall Munroe, xkcd.com-\~

## Overview

This is an emacs extension for dealing with ros. Simplifies navigating
the package system, tracking topics and nodes, and running various
commands (`roscore`, `rosrun`, `roslaunch`) directly from emacs.

Setting up `rosemacs` defines a set of ROS-related emacs commands.
These can be either called using the full command names given below
(using `M-x command-name`) or using a keyboard shortcut, if you've
set a prefix for the ros-keymap. For example, given the setup below,
`C-x C-r C-f` will find a package or file using rospack. Type `C-h f
command-name` to see if there's a shortcut for a given command. Type
`C-x C-r C-h` to see the entire list of keyboard shortcuts. In this
document, we'll list the keyboard shortcut with each command, which has
to be preceded with whatever prefix you're using (in our case `C-x
C-r`).

## Installation

### Installation from Debian package

If you are a Lisp developer you'll probably need the
[roslisp_repl](roslisp_repl) package. It installs `rosemacs`
automatically as a dependency.

#### ROS Indigo +

Since ROS Indigo rosemacs is distributed through the ROS release
infrastructure.

```
$ sudo apt-get install ros-DISTRO-rosemacs
```

#### ROS Fuerte, Groovy and Hydro

For ROS Fuerte, Groovy and Hydro, the package was distributed through
Ubuntu Debian package repositories:

```
$ sudo apt-get install rosemacs-el
```

### Installation from source

The most up-to-date version of rosemacs code can be found
[here](https://github.com/code-iai/ros_emacs_utils). Installation
instructions can be found in the README file. What you'll need to do
will be something like the following:

```
$ cd YOUR_CATKIN_WS/src
$ wstool set ros_emacs_utils --git https://github.com/code-iai/ros_emacs_utils.git
$ wstool update ros_emacs_utils
$ cd ..
$ catkin_make
$ catkin_make install
```

## Setup

IMPORTANT: Make sure the standard ROS variables are always set in the
emacs process environment. For example, if you use bash, follow the
standard ROS installation instructions about sourcing `setup.bash` in
your `.bashrc`, and launch emacs from a bash shell.

### ROS Indigo +

Update your
[emacs configuration file](http://www.emacswiki.org/emacs/InitFile),
e.g.:

```
$ emacs -nw ~/.emacs.d/init.el
```

Add the following:

```
(add-to-list 'load-path "/opt/ros/DISTRO/share/emacs/site-lisp")
;; or whatever your install space is + "/share/emacs/site-lisp"
(require 'rosemacs-config)
```

For troubleshooting consult the
[README](https://github.com/code-iai/ros_emacs_utils/blob/master/README.md)
file.

### ROS Fuerte, Groovy and Hydro

Put the following in your
[emacs configuration file](http://www.emacswiki.org/emacs/InitFile)
(e.g. `/.emacs`):

```
;; Load the library and start it up
(require 'rosemacs)
(invoke-rosemacs)

;; Optional but highly recommended: add a prefix for quick access
;; to the rosemacs commands
(global-set-key "\C-x\C-r" ros-keymap)
```

## Navigating the ros file system

Rosemacs provides various commands to simplify working with ROS. In each
case, we give the long name of the command followed by the key that can
be used to invoke it following the shortcut sequence for the ROS keymap.
For example, if you used the above init file that binds control-x
control-r to the ROS keymap, then the first command below
(find-ros-file) can be invoked using control-x control-r control-f.

### Visiting files

`find-ros-file` (`C-f`)\
`view-ros-file` (`f`)\
`find-ros-message` (`C-m`)\
`view-ros-message` (`m`)\
`find-ros-service` (`C-s`)\
`view-ros-service` (`s`)

The commands `{find\|view}-ros-{file\|message\|service}` for
navigating the ros libraries are available. The file versions take in a
package name and relative path, and the message/service versions just
take the message/service name. All of these can be tab-completed.

`ros-load-package-locations` (`r`)

`rosemacs` caches the list of packages for speed. This command causes
the list to be reloaded, which is useful if you've just created a new
package.

### Searching and replacing in packages

`ros-rgrep-package` (`g`) Recursively grep in a ros package. This
command is similar to rgrep but asks for a ROS package instead of a
directory.

`ros-find-dired` Execute `find` in a ROS package and use the output
in a dired buffer. This command is similar to find-dired but asks for a
ROS package to run find in instead of a directory.

## Interacting with a live ROS system

### Topic tracking

`rosemacs` maintains information about current ROS topics. The topic
list is used for tab completion, both in the shell and emacs commands,
of topics in the appropriate places.

`display-ros-topic-info` (`C-t`) Display the `\*ros-topics\*`
buffer, which contains the set of published and subscribed topics

`add-hz-update` (`h`) Make `rosemacs` track the hz rate of the
topics matching one or more regexps, and display this in the
`\*ros-topics\*` buffer.

`remove-hz-update` (`H`) Stop tracking topics matching a given
regexp.

`echo-ros-topic` (`t`) Echo a ROS topic into a new buffer.

### Node tracking

Analogous to topic tracking. Provides completion of node names in the
appropriate places. Also, when nodes die, displays a message in the
minibuffer and the ros-events buffer.

`rosemacs/display-nodes` (`C-n`) Display current list of ros nodes.

### Running/launching things

`ros-launch` (`C-l`) Start a launch file in an appropriately named
buffer. In that buffer, `k` kills the launch (and the launched
processes), `r` restarts, and `q` quits.

`ros-run` (`C-r`) Analogous to `ros-launch` with the same
keybindings.

`ros-core` (`C-c`) Start a core that sends output to the
`\*ros-core\*` or switch to that buffer if a core is already active.

### Ros events

The `\*ros-events\*` buffer contains a timestamped list of noteworthy
events in the ros system. Useful for answering the question "did
something unexpectedly die?" when your system is behaving strangely.
Currently, it keeps track of nodes starting and stopping.

`rosemacs/display-event-buffer` (`C-e`) Display the ros event buffer

## Programming aids

### Shell tab completion

By default, ROS tab completion does not work if you use shell-mode in
emacs. `rosemacs` fixes this and adds completion of current nodes and
topics.

### yasnippet integration

[yasnippet](http://code.google.com/p/yasnippet/) is an Emacs extension
that allows you to write snippets, which are templates for recurring
patterns in source code. Rosemacs (trunk) provides a few ros-specific
ones in the `snippets/` directory. E.g., if you enable snippets
support and set up your path as per the above instructions, if you open
up a new file `bar.h` in the `foo` package and type `wgh` followed
by `\[TAB\]`, it will:

-   Figure out that it's in the `foo` ROS package
-   Generate an include guard named `FOO_BAR_H`
-   Add a declaration for namespace `foo`
-   Add a doxygen block for the file

### Current package in the Mode Line

You can add the following expression to the customization
`mode-line-format`: ```
(:eval (ros-current-pkg-modeline-entry))
``` With this, the current
buffer's ROS package becomes part of the mode line.

### Editing yaml files

You may also want to add a yaml mode to your .emacs file. 1. Download a
yaml mode .el file from here: <http://www.emacswiki.org/emacs/YamlMode>
and put it next to rosemacs.el or somewhere else in your emacs load
path. 1. Add these lines to your .emacs file: ```
(require 'yaml-mode)
(add-to-list 'auto-mode-alist '("\\.yml$" . yaml-mode))
(add-to-list 'auto-mode-alist '("\\.yaml$" . yaml-mode))
```

### Editing message, service, and action files

Invoking rosemacs makes files with extension `.msg`, `.srv` and
`.action` open in Emacs's gdb-script-mode for syntax highlighting.
You can override this behavior by updating the `auto-mode-alist`
variable after calling `invoke-rosemacs`.

### Editing launch and manifest files

Emacs 23 and later includes
[NXML mode](http://www.thaiopensource.com/nxml-mode/) which, given a
RELAX NG schema, validates xml documents online as you edit them and
provides intelligent completion. Rosemacs includes schemas for roslaunch
and manifest.xml files. This is now automatically setup (with Emacs 23
and later).

### Integration with roslisp and slime

For more information on programming ROS packages in Lisp see the
[roslisp_repl](roslisp_repl) package wiki.

## Customization

There are various customizable options. You can set these using emacs's
customization system (in the `rosemacs` customization group), or by
just doing `(setq variable value)` in your .emacs.

`ros-completion-function` The default is to use standard emacs
completion. You can instead use the awesome
[ido-mode](http://www.emacswiki.org/emacs/InteractivelyDoThings) which
already comes with emacs22 and higher. To use this, first activate
ido-mode following the instructions at the above page. Then customize
`ros-completion-function` to `ido-completing-read`.

`ros-topic-update-interval` How often (seconds) rosemacs polls the
list of ros topics. Default is 8.

`ros-node-update-interval` How often (seconds) rosemacs polls the list
of ros nodes. Default is 8.
