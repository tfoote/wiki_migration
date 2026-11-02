{}

## Tutorials

- [Simulating Husky](#simulating-husky):
  How to bring up a simulated Husky robot using the Gazebo simulator.

## Simulating Husky

- **Description:** How to bring up a simulated Husky robot using the
  Gazebo simulator.
- **Keywords:** Clearpath Husky
- **Tutorial Level:** BEGINNER
- **Next Tutorial:**
  [Interfacing with Husky](https://index.ros.org/p/husky_control)

Husky can be simulated in several environments using the
husky_gazebo packages. To start a
simulation:

1\. Make sure the simulation package is installed:



```
$ sudo apt-get install ros-<distro>-husky-simulator
```

 Using the short name of your ROS distribution
instead of <distro>.

2\. Set an environmental variable HUSKY_GAZEBO_DESCRIPTION:


```
$ export HUSKY_GAZEBO_DESCRIPTION=$(rospack find husky_gazebo)/urdf/description.gazebo.xacro
```



3\. Run one of the two provided simulation environments: i. Simulate
Husky in an empty world. You can add new objects to this world using the
Gazebo controls
([Gazebo Tutorial - Building a World](http://gazebosim.org/tutorials?tut=build_world).



```
$ roslaunch husky_gazebo husky_empty_world.launch
```



i\. Simulate Husky in a Clearpath designed world. This is the base
environment for the
[navigation tutorials](https://index.ros.org/p/husky_navigation). It
will take some time to start, as the simulator will need to download
resources from the Gazebo servers.



```
$ roslaunch husky_gazebo husky_playpen.launch
```



4\. Pick your own world in which to simulate Husky
([Using roslaunch with Gazebo](http://gazebosim.org/tutorials/?tut=ros_roslaunch#UsingroslaunchtoOpenWorldModels)).



```
$ roslaunch husky_gazebo husky_empty_world.launch world_name:=worlds/willowgarage.world
```
