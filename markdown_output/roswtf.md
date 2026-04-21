## roswtf Command-line Tool

`roswtf` will examine your ROS setup, such as your
[environment variables](ROS/EnvironmentVariables), and look for
configuration issues. If you have a ROS system online, it will look at
it and check for any potential issues.

### check targets

Other than the general checks, `roswtf` has two usages.

#### Checking packages or stacks

You can either run it just by typing: 

```
$ roswtf
```

 which
will check the current package or stack for problems.

**IMPORTANT**: `roswtf` performs those checks based on the directory
you run it from. For example, if you run it in the
[navigation](navigation) stack, it will perform it's filesystem checks
based on files in the `navigation` stack and its dependencies.

#### Checking a launch file

Or you can also run `roswtf` on a [roslaunch](roslaunch) file:


```
$ roswtf yourfile.launch
```



in which case it will check the given launch file for any potential
issues.

### Options

`roswtf` accepts the following command-line options:

`\--all` Run `roswtf` rules against all packages in your
`ROS_PACKAGE_PATH`

`\--no-plugins` Disable `roswtf` plugins

`\--offline` Run offline tests only.

## What does roswtf look for?

`roswtf` looks for many, many things, and the list is always growing.
There are two categories of what it looks for: file-system issues and
online/graph issues.

For file-system issues, `roswtf` looks at your environment variables,
package configurations, stack configurations, and more. It can also take
in a [roslaunch](roslaunch) file and attempt to find any potential
configuration issues in it, such as packages that haven't been built
properly.

For online issues, `roswtf` examines the state of your current graph
and tries to find any potential issues. These issues might be
unresponsive nodes, missing connections between nodes, or potential
machine-configuration issues with [roslaunch](roslaunch).

## Warnings vs. errors

`roswtf` produces a report containing both warnings and errors based
on the checks it performed. In general, warnings are something that
seems odd, but may be just fine. Errors are known problems that you
should probably address if you are experiencing problems.

## Advanced: roswtf plugins

Please see [roswtf plugin API](/Plugins).

## Roadmap

`roswtf` will continue to evolve to try and diagnose more complex
problems that may arise in large ROS systems. There are currently plans
to do checks for multi-machine setups, as well as expand the range of
its checks via the plugin API. Recommendations for checks that can be
performed are always welcome.
