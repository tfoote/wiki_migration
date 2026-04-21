\`rosdep\` is a command-line tool for installing system dependencies.

## New documentation

As of ROS [fuerte](fuerte), \`rosdep\` is now a stand-alone tool that
you can download and use separately:
[External rosdep documentation](http://ros.org/doc/independent/api/rosdep/html/).

## Quick reference

### Installing rosdep

Do prefer \`apt\` over \`pip\` as it\'s updated automatically and
faster. ```
# ROS Noetic
sudo apt-get install python3-rosdep
# ROS Melodic and earlier
sudo apt-get install python-rosdep
```

#### On non ubuntu platforms

Use [pip](ROS/Installation/EasyInstallConfig): ```
sudo pip install -U rosdep
```

### Initializing rosdep

Needs to be called only *once* after installation:
```
sudo rosdep init
```

Needs to be called at least once or when updating (there might be new
needed definitions your local installation of \`rosdep\` doesn\'t know
about yet):

```wiki
Do '''NOT''' run `rosdep update` with sudo. It is not required and will result in permission errors later on.
```

```
rosdep update
```

```wiki
As of version 0.14.0 `rosdep update` will only fetch ROS package names for non-EOL ROS distributions.
If you are still using an EOL ROS distribution (which you probably shouldn't) you can pass the argument `--include-eol-distros` to also fetch the ROS package names of those.
```

If you experienced network error, you may use a mirror site like
[TUNA](https://mirrors.tuna.tsinghua.edu.cn/help/rosdistro/) and
[BFSU](https://mirrors.bfsu.edu.cn/help/rosdistro/).

### Using rosdep

#### Install dependency of a particular package

You can use \`rosdep\` and [catkin](catkin) to build any package in the
ROS repository. Say that you want to build a package called
AMAZING_PACKAGE, that you hadn\'t built on your machine before.

```
rosdep install AMAZING_PACKAGE
```

#### Install dependency of all packages in the workspace

This usecase shows even more powerful feature of \`rosdep\`.

Go to the top directory of your [catkin workspace](catkin/workspaces)
where the source code of the ROS packages you\'d like to use are. Then
run:

```
rosdep install --from-paths src --ignore-src -r -y
```

This command magically installs all the packages that the packages in
your \`catkin workspace\` depend upon but are missing on your computer.

### Use source-installed rosdep

Clone the development repository. This doesn\'t need to be done in a
directory in \`ROS_PACKAGE_PATH\`. Then at its top directory, source
\`setup.sh\`. In concrete: ```
$ git clone https://github.com/ros-infrastructure/rosdep
$ cd rosdep
$ source setup.sh
``` Then calling
\`rosdep\` should use the source just downloaded.

## Change list

See
[changelog in the development repository](https://github.com/ros-infrastructure/rosdep/blob/master/CHANGELOG.rst).

## Bugs/Feature Requests

[ View or file new issues on github](https://github.com/ros-infrastructure/rosdep/issues)

## Tutorial

See [this page](ROS/Tutorials/rosdep). There\'s also
[a list of rosdep tutorials](rosdep/Tutorials).
