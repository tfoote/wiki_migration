This package simply wraps around GraspIt!, allowing it to build under
the ROS build system. It will get the GraspIt! source code from its
original repository, then build it.

As any released ROS stack, it is available as a debian package:

```
sudo apt-get install ros-[distro]-graspit-simulator
```

The debian version of this stack comes with a fully built version of
GraspIt!. This should allow you to start GraspIt! easily. More often
though, you will need to compile GraspIt! from source code yourself in
order to add new features.

In this case, still start by installing this stack as a debian as above,
as that will pull in all the system dependencies that GraspIt! needs.
Then, download this ROS stack and build it from code, which will in turn
pull GraspIt!'s code and build it.

By default, this package will pull a tarball with the latest released
version of GraspIt!. If you want the latest development version instead,
edit `CMakeLists.txt` and replace `Makefile.graspit.tarball` with
`Makefile.graspit.svn`.

Summarizing, an easy way to get GraspIt! under ROS from source code is
do the following: ```
sudo apt-get install ros-[distro]-graspit
svn co https://code.ros.org/svn/wg-ros-pkg/stacks/graspit_simulator/tags/[distro] graspit_simulator
//add graspit_simulator to your ROS_PACKAGE_PATH
rosmake graspit
```
