![Shipwreck scenario UWSim v1.1\|align="middle"](attachment:UWSim_v1.1.jpg)

## Requirements

The simulator has been tested in Ubuntu Linux from 9.10 to 12.04.
However, it should work on other linux-based distributions. MacOS and
Windows have not been tested for now, but it should be possible to run
UWSim also on these systems, since all the libraries used are also
available for them.

You will need a decent PC, with a good graphics card. It should work
well on recent NVidia and ATI cards with good driver support in
GNU/Linux. Have a look to the
<http://code.google.com/p/osgocean/wiki/HardwareSupport> list of cards
that are known to be working\]. If you see strange visualization
effects, or it just crashes before beginning, it probably means your
card does not meet the requirements (if this is the case, try with the
<tt>\--disableShaders</tt> option). As an example, it runs fluently
on a MacBook Pro 2.26 Ghz Intel Core 2 Duo, 4 GB DDR3 with an NVIDIA
GeForce 9400M, running Ubuntu 11.04.

Finally, you will also need ROS. It has been tested on ROS cturtle,
diamondback, electric, fuerte and groovy. For ROS installation
instructions, refer to the following link:

<http://wiki.ros.org/ROS/Installation>

## Package-based installation

There are deb packages pre-compiled for Ubuntu and ROS Groovy / Hydro.
Assuming you have the ROS repositories already added to your
sources.list, the following command will install UWSim and all its
dependencies:

```
apt-get install ros-groovy-uwsim
```

## Running

First be sure that a roscore is already running. If not, start it:

```
roscore
```

After that, the following command should start UWSim:

```
rosrun uwsim uwsim
```

The first time you run UWSim, it will ask for downloading a data package
that will be installed under /.uwsim. After that, a window should appear
showing a default scenario and robot. Inside the simulator, you can
freely move the camera with the mouse. With the simulator running, you
can check the list of ROS topics involved:

```
rostopic list
```

and subscribe/publish to them with rostopic and rospub, or with your
custom ros control nodes. The are some example ROS interface nodes in
the <tt>interface_examples</tt> folder. For example, the following
command should update the vehicle position in the default scenario (2
meters along positive X axis):

```
rosrun uwsim setVehiclePosition /dataNavigator 2 0 0 0 0 0
```

## Source-based installation previous to ROS Groovy

This section explain how to build UWSim from sources in ROS
distributions previous to Groovy.

### Download sources

Download the underwater_simulation stack to a folder in your
ROS_PACKAGE_PATH:

```
git clone https://github.com/uji-ros-pkg/underwater_simulation.git
```

### Configure & build

First install the UWSim dependencies with the following command:

```
rosdep install UWSim
```

This will ask for your password in order to install all the necessary
packages with apt-get. After this, you can build the simulator:

```
rosmake UWSim
```

This will first download and compile osgOcean. After that the UWSim
package will be built.

## Source-based installation in Groovy and later distributions

This section explain how to build UWSim from sources in ROS Groovy. For
hydro or later distributions, just replace 'groovy' by 'hydro' or
the corresponding distro name.

### Download sources

Create a [catkin workspace](catkin/Tutorials/create_a_workspace) and
place a .rosinstall file inside it with the following contents:

```
- other: {local-name: /opt/ros/groovy/share/ros}
- other: {local-name: /opt/ros/groovy/share}
- other: {local-name: /opt/ros/groovy/stacks}
- setup-file: {local-name: /opt/ros/groovy/setup.sh}
- git: {local-name: src/uwsim_osgocean, 
        uri: 'https://github.com/uji-ros-pkg/uwsim_osgocean.git', 
        version: groovy-devel}
- git: {local-name: src/uwsim_osgworks, 
        uri: 'https://github.com/uji-ros-pkg/uwsim_osgworks.git', 
        version: groovy-devel}
- git: {local-name: src/uwsim_bullet, 
        uri: 'https://github.com/uji-ros-pkg/uwsim_bullet.git', 
        version: groovy-devel}
- git: {local-name: src/uwsim_osgbullet, 
        uri: 'https://github.com/uji-ros-pkg/uwsim_osgbullet.git', 
        version: groovy-devel}
- git: {local-name: src/underwater_simulation, 
        uri: 'https://github.com/uji-ros-pkg/underwater_simulation.git', 
        version: groovy-devel}
```

Then download the sources with:

```
rosws update
```

### Configure & build

Install the dependencies and build the sources with cakin:

```
roscore
```0
