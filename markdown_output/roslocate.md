This documentation is for the standalone release of \`roslocate\`, which
is distributed with [rosinstall](rosinstall). For older version of
\`roslocate\`, please see [C Turtle documentation](/cturtle).

## Installation

\`roslocate\` is installed with the [rosinstall](rosinstall) tool. To
install:

```
easy_install -U rosinstall
```

## Usage

```
roslocate
	info	Get rosinstall info of resource
	vcs	Get name of source control system
	type	Package or stack
	uri	Get source control URI of resource
	www	Get web page of resource
	repo	Get repository name of resource
	describe	Get description of resource
```

In order to assist with migrating users from the old version of
\`roslocate\`, the \`roslocate svn\` command is still supported. It will
be removed in future versions.

### info

\`roslocate info \<package-or-stack\>\` Return \`rosinstall\` fragment
for install the package or stack.

Example: ```
roslocate info mapping
 - git:
        local-name: mapping
        uri: http://code.in.tum.de/git/mapping.git
```

\`\--prefix\` Specify a file-system prefix for the rosinstall fragment.

Example: ```
roslocate info --prefix /home/bob/ros-pkg rospy
 - svn:
        local-name: /home/bob/ros-pkg/rospy
        uri: https://code.ros.org/svn/ros/stacks/ros_comm/trunk/clients/rospy
```

\`\--distro=DISTRO\` \'\'(Since 0.5.17)\'\' Get installation information
for stack released into a specific ROS distribution. \'\'(Released
stacks only)\'\'

\`\--dev\` \'\'(Since 0.5.17)\'\' Fetch the development branch instead
of versioned release (e.g. \"trunk\"). \'\'(Released stacks only)\'\'

[roadmap](/Roadmap)
