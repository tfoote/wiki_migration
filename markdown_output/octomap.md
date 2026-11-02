## Documentation

General information about !OctoMap is available at
<http://octomap.github.io> and in the publication
["OctoMap: An Efficient Probabilistic 3D Mapping Framework Based on Octrees"](http://www.informatik.uni-freiburg.de/~hornunga/pub/hornung13auro.pdf)
by A. Hornung, K. M. Wurm, M. Bennewitz, C. Stachniss, and W. Burgard
(Autonomous Robots Journal, 2013).

BibTeX: 

```
@ARTICLE{hornung13auro,
  author = {Armin Hornung and Kai M. Wurm and Maren Bennewitz and Cyrill
  Stachniss and Wolfram Burgard},
  title = {{OctoMap}: An Efficient Probabilistic {3D} Mapping Framework Based
  on Octrees},
  journal = {Autonomous Robots},
  year = 2013,
  url = {http://octomap.github.com},
  doi = {10.1007/s10514-012-9321-0},
  note = {Software available at \url{http://octomap.github.com}}
}
```

 Please cite our paper if you use
!OctoMap in your research.

Doxygen documentation based on the latest !OctoMap release is available
[online](https://octomap.github.io/octomap/doc/).

If you want to use !OctoMap in ROS,
[octomap_ros](https://index.ros.org/p/octomap_ros) and
[octomap_msgs](https://index.ros.org/p/octomap_msgs) provide messages,
wrappers and conversion methods.
[octomap_server](https://index.ros.org/p/octomap_server) provides map
building and serving capabilities. A visualization tool is available at
[octovis](https://index.ros.org/p/octovis).



```
{{#!wiki version fuerte_and_newer
== Using OctoMap ==
Run
{{{
sudo apt-get install ros-$ROS_DISTRO-octomap
```



to install !OctoMap as stand-alone libraries with no ROS dependencies
(so the package can also be used in a non-ROS setting).

This means that you compile against !OctoMap without requiring any
ROS-specific build tools or catkin macros (in fact, they won't work).
For convenience, the system install includes CMake config files for
easily finding and configuring !OctoMap in your CMakeLists.txt using the
regular `find_package()` macro:



```
find_package(octomap REQUIRED)
include_directories(${OCTOMAP_INCLUDE_DIRS})
target_link_libraries(${OCTOMAP_LIBRARIES})
```



(Add ```link_directories(\${OCTOMAP_LIBRARY_DIRS})``` only if
required - usually it's not needed).



```
{#!wiki version groovy_and_newer

Finally, add to your `package.xml`:
{{{
<build_depend>octomap</build_depend>
<run_depend>octomap</run_depend>
```



}}}}

}}}}}

## Report a Bug

Report bugs or request features
[on GitHub](https://github.com/OctoMap/octomap/issues). For questions
and discussions, use the mailing list at
<http://groups.google.com/group/octomap>

## Tutorials

- [Creating an OctoMap from existing 3D (mesh) data](#creating-an-octomap-from-existing-3d-mesh-data):
  \## the next tutorial description (optional)

## Creating an OctoMap from existing 3D (mesh) data

- **Note:** This is only a rough outline at the moment.
- **Tutorial Level:** INTERMEDIATE

This tutorial has moved:
<https://github.com/OctoMap/octomap/wiki/Importing-Data-into-OctoMap>
