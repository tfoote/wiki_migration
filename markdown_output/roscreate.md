## Overview

\`roscreate\` contains the \`roscreate-pkg\` and \`roscreate-stack\`
tools, which are command-line tools for creating new ROS
[packages](Packages) and [stacks](Stacks), respectively. Packages are
frequently created by people copying an existing package and then
modifying it\'s build and [manifest.xml](Manifest) files. This
frequently results in errors, so the \`roscreate-pkg\` tool is meant to
be just as easy, but less error prone. Similarly,
[stack.xml](Stack Manifest) files are difficult to create by hand as one
must correctly specify the union of all package dependencies.

## Command-Line Tools

### roscreate-pkg

The \`roscreate-pkg\` command-line tool creates a new ROS
[package](Packages) with common package files: [manifest.xml](Manifest),
[CMakeLists.txt](CMakeLists), \`mainpage.dox\`, and \`Makefile\`. It
addresses the common problem of packages being created using
pre-existing packages, which leads to errors in build files and
manifests.

IMPORTANT: the directory that you run \`roscreate-pkg\` in matters. You
**must** run it in a directory that can be located from your
\`ROS_PACKAGE_PATH\` (see
[ROS environment variables](ROS/EnvironmentVariables)). Furthermore, you
cannot run it inside of another ROS package.

To create a new package in the current directory:

```
$ roscreate-pkg pkgname
```

To test that this worked, you can use \`roscd\`:
```
$ roscd pkgname
```

You can also specify dependencies of that package:

```
$ roscreate-pkg pkgname depend1 depend2 depend3
```

e.g.

```
$ roscreate-pkg foopkg roslib roscpp std_msgs
```

For common dependencies like [roscpp](roscpp) and [rospy](rospy),
\`roscreate-pkg\` may create some additional common directory
structures.

### roscreate-stack

**Note:** No longer supported in [fuerte](fuerte), see
[fuerte/Migration#No_more_roscreate-stack](fuerte/Migration#No_more_roscreate-stack).

The \`roscreate-stack\` command-line tool creates or updates a ROS
[stack](Stacks), which mainly involves the creation of a
[stack.xml](Stack Manifest) file. It is the most convenient way of
automatically updating a stack. It\'s best to use this tool with a
directory that already contains the [packages](Packages) you wish to put
into your stack. This tool can save a lot of effort in computing the
union of all the dependencies for a particular stack, so its use is
highly recommended.

To create or update a stack in the current directory:

```
$ roscreate-stack .
```

\`\--show-deps\`

Show the calculated stack dependencies only.
