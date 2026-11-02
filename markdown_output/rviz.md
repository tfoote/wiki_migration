## Overview

[Youtube](https://www.youtube.com/watch?v=i--Sd4xH9ZE)

## User Documentation

1\. [User Guide](#userguide) 1.
[Troubleshooting](#troubleshooting-1) 1.
[Built-in Display Types](#displaytypes) 1.
[Basic Shapes API Wrapper - rviz_visual_tools](https://github.com/davetcoleman/rviz_visual_tools)

## Tutorials

- [Markers: Sending Basic Shapes (C++)](#markers-sending-basic-shapes-c):
  Shows how to use
  [visualization_msgs/msg/Marker](https://docs.ros.org/en/rolling/p/visualization_msgs/msg/Marker.html)
  messages to send basic shapes (cube, sphere, cylinder, arrow) to rviz.
- [Markers: Points and Lines (C++)](#markers-points-and-lines-c):
  Teaches how to use the
  [visualization_msgs/msg/Marker](https://docs.ros.org/en/rolling/p/visualization_msgs/msg/Marker.html)
  message to send points and lines to rviz.
- [Interactive Markers: Getting Started](#interactive-markers-getting-started):
  This tutorial explains what Interactive Marker are and teaches you
  some of the basic concepts.
- [Interactive Markers: Writing a Simple Interactive Marker Server](#interactive-markers-writing-a-simple-interactive-marker-server):
  This tutorial explains how to setup a minimalist server which manages
  a single interactive marker.
- [Interactive Markers: Basic Controls](#interactive-markers-basic-controls):
  This tutorial explains how the basic_controls tutorial code works.
- [Plugins: New Display Type](#plugins-new-display-type):
  How to write a plugin which adds a new display capability to RViz.
- [Plugins: New Dockable Panel](#plugins-new-dockable-panel):
  How to write a plugin which adds a new type of dock-able Panel widget
  to RViz.
- [Plugins: New Tool Type](#plugins-new-tool-type):
  How to write a plugin which adds a new tool to RViz.
- [Librviz: Incorporating RViz into a Custom GUI](#librviz-incorporating-rviz-into-a-custom-gui):
  How to write an application using an RViz visualization widget.
- [Rviz in Stereo](#rviz-in-stereo):
  Teaches how to set up Rviz to render in 3D Stereo.

## API Documentation

### Command Line Options

To see the list of command line options for your RViz release, run the
following command:



```
rosrun rviz rviz --help
```



## Recording Movies

rviz does not have a builtin capability to record movies. You can,
however, use an application like
[GLC](https://github.com/nullkey/glc/wiki) (or
[SimpleScreenRecorder](http://www.maartenbaert.be/simplescreenrecorder))
to do so. The [RecordingOpenGLAppsWithGLC](RecordingOpenGLAppsWithGLC)
page has more information on recording and encoding.

## Report a Bug

[Report a bug or request a feature](https://github.com/ros-visualization/rviz/issues/new).
\[
[View active tickets](https://github.com/ros-visualization/rviz/issues?state=open)
\]

## UserGuide

### Troubleshooting

If you're running into problems and have not seen the answer below, try
the [Troubleshooting Page](#troubleshooting-1)

### Install or build rviz

Obviously you don't need both and should prefer the install:

#### Install from debian repository

Until fuerte: 

```
sudo apt-get install ros-fuerte-visualization
```

 From groovy on:


```
sudo apt-get install ros-groovy-rviz
# or
sudo apt-get install ros-hydro-rviz
# or
sudo apt-get install ros-indigo-rviz
# or
sudo apt-get install ros-kinetic-rviz
# or
sudo apt-get install ros-melodic-rviz
# or
sudo apt-get install ros-noetic-rviz
```





```
{#!wiki comment
=== Build from source ===
Download the rviz sources into your ros_workspace or your overlay ([[fuerte/Installation/Overlays|help for fuerte]], [[groovy/Installation/Overlays|help for groovy]]).

First satisfy any system dependencies.
{{{
rosdep install rviz
```



Now build the visualizer: 

```
rosmake rviz
```



}}}}

### Startup

You might have to run a line such as 

```
source /opt/ros/indigo/setup.bash
roscore &
```

 Then start
the visualizer: 

```
rosrun rviz rviz
```



When rviz starts for the first time, you will see an empty window:
![width=100%](doc/initial_startup.png)

The big black thing is the 3D view (empty because there is nothing to
see). On the left is the Displays list, which will show any displays you
have loaded. Right now it just contains the global options and the time
view, which I'll get to later. On the right are some of the other
panels, described below.

### Displays

A display is something that draws something in the 3D world, and likely
has some options available in the displays list. An example is a point
cloud, the robot state, etc.

#### Adding a new display

To add a display, click the Add button at the bottom:

![attachment:add_display_button.png](doc/add_display_button.png)

This will pop up the new display dialog:

![attachment:new_display_dialog.png](doc/new_display_dialog.png)

The list at the top contains the display *type*. The type details what
kind of data this display will visualize. The text box in the middle
gives a description of the selected display type. Finally, you must give
the display a unique name. If you have, for example, two laser scanners
on your robot, you might create two "Laser Scan" displays named
"Laser Base" and "Laser Head".

#### Display Properties

Each display gets its own list of properties. For example:

![attachment:display_properties_example.png](doc/display_properties_example.png)

#### Display Status

**`'New in 0.4`**'

Each display gets its own status to help let you know if everything is
OK or not. The status can be one of 4: **OK**, **Warning**, **Error**
and **Disabled**. The status is indicated in the display's title by the
background color, as well as in the `Status` category that you can see
if the display is expanded:

![attachment:displays_with_all_statuses.png](doc/displays_with_all_statuses.png)

The `Status` category also expands to show specific status
information. This information is different for different displays, and
the messages should be self explanatory.

#### Moving Displays

You can move a display up or down in the list with the arrow buttons to
the right of the Add/Remove buttons:
![attachment:move_display.png](doc/move_display.png)

#### Built-in Display Types

  -- --------------------------------------------------------------------------- -- ------------------------------------------------------------------------------------------------------------------------------------------- -- ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ --
     **Name**                                                                       **Description**                                                                                                                                **Messages Used**                                                                                                                                                                                                        
     [Axes](#displaytypesaxes)                                Displays a set of Axes                                                                                                                                                                                                                                                                                                                                                  
     [Effort](#displaytypeseffort)                            Shows the effort being put into each revolute joint of a robot.                                                                                [sensor_msgs/msg/JointStates](https://docs.ros.org/en/rolling/p/sensor_msgs/msg/JointStates.html)                                                                                                                        
     [Camera](#displaytypescamera)                            Creates a new rendering window from the perspective of a camera, and overlays the image on top of it.                                          [sensor_msgs/msg/Image](https://docs.ros.org/en/rolling/p/sensor_msgs/msg/Image.html), [sensor_msgs/msg/CameraInfo](https://docs.ros.org/en/rolling/p/sensor_msgs/msg/CameraInfo.html)                                   
     [Grid](#displaytypesgrid)                                Displays a 2D or 3D grid along a plane                                                                                                                                                                                                                                                                                                                                  
     [Grid Cells](#displaytypesgridcells)                     Draws cells from a grid, usually obstacles from a costmap from the [navigation](https://index.ros.org/p/navigation) stack.                     [nav_msgs/msg/GridCells](https://docs.ros.org/en/rolling/p/nav_msgs/msg/GridCells.html)                                                                                                                                  
     [Image](#displaytypesimage)                              Creates a new rendering window with an Image. Unlike the Camera display, this display does not use a !CameraInfo. *Version: Diamondback+*      [sensor_msgs/msg/Image](https://docs.ros.org/en/rolling/p/sensor_msgs/msg/Image.html)                                                                                                                                    
     [InteractiveMarker](#displaytypesinteractivemarker)      Displays 3D objects from one or multiple Interactive Marker servers and allows mouse interaction with them. *Version: Electric+*               [visualization_msgs/msg/InteractiveMarker](https://docs.ros.org/en/rolling/p/visualization_msgs/msg/InteractiveMarker.html)                                                                                              
     [Laser Scan](#displaytypeslaserscan)                     Shows data from a laser scan, with different options for rendering modes, accumulation, etc.                                                   [sensor_msgs/msg/LaserScan](https://docs.ros.org/en/rolling/p/sensor_msgs/msg/LaserScan.html)                                                                                                                            
     [Map](#displaytypesmap)                                  Displays a map on the ground plane.                                                                                                            [nav_msgs/msg/OccupancyGrid](https://docs.ros.org/en/rolling/p/nav_msgs/msg/OccupancyGrid.html)                                                                                                                          
     [Markers](#displaytypesmarker)                           Allows programmers to display arbitrary primitive shapes through a topic                                                                       [visualization_msgs/msg/Marker](https://docs.ros.org/en/rolling/p/visualization_msgs/msg/Marker.html), [visualization_msgs/msg/MarkerArray](https://docs.ros.org/en/rolling/p/visualization_msgs/msg/MarkerArray.html)   
     [Path](#displaytypespath)                                Shows a path from the [navigation](https://index.ros.org/p/navigation) stack.                                                                  [nav_msgs/msg/Path](https://docs.ros.org/en/rolling/p/nav_msgs/msg/Path.html)                                                                                                                                            
     [Point](#displaytypespoint)                              Draws a point as a small sphere.                                                                                                               [geometry_msgs/msg/PointStamped](https://docs.ros.org/en/rolling/p/geometry_msgs/msg/PointStamped.html)                                                                                                                  
     [Pose](#displaytypespose)                                Draws a pose as either an arrow or axes.                                                                                                       [geometry_msgs/msg/PoseStamped](https://docs.ros.org/en/rolling/p/geometry_msgs/msg/PoseStamped.html)                                                                                                                    
     [Pose Array](#displaytypesposearray)                     Draws a "cloud" of arrows, one for each pose in a pose array                                                                                 [geometry_msgs/msg/PoseArray](https://docs.ros.org/en/rolling/p/geometry_msgs/msg/PoseArray.html)                                                                                                                        
     [Point Cloud(2)](#displaytypespointcloud)                Shows data from a point cloud, with different options for rendering modes, accumulation, etc.                                                  [sensor_msgs/msg/PointCloud](https://docs.ros.org/en/rolling/p/sensor_msgs/msg/PointCloud.html), [sensor_msgs/msg/PointCloud2](https://docs.ros.org/en/rolling/p/sensor_msgs/msg/PointCloud2.html)                       
     [Polygon](#displaytypespolygon)                          Draws the outline of a polygon as lines.                                                                                                       [geometry_msgs/msg/Polygon](https://docs.ros.org/en/rolling/p/geometry_msgs/msg/Polygon.html)                                                                                                                            
     [Odometry](#displaytypesodometry)                        Accumulates odometry poses from over time.                                                                                                     [nav_msgs/msg/Odometry](https://docs.ros.org/en/rolling/p/nav_msgs/msg/Odometry.html)                                                                                                                                    
     [Range](#displaytypesrange)                              Displays cones representing range measurements from sonar or IR range sensors. *Version: Electric+*                                            [sensor_msgs/msg/Range](https://docs.ros.org/en/rolling/p/sensor_msgs/msg/Range.html)                                                                                                                                    
     [RobotModel](#displaytypesrobotmodel)                    Shows a visual representation of a robot in the correct pose (as defined by the current TF transforms).                                                                                                                                                                                                                                                                 
     [TF](#displaytypestf)                                    Displays the [tf](https://index.ros.org/p/tf) transform hierarchy.                                                                                                                                                                                                                                                                                                      
     [Wrench](#displaytypeswrench)                            Draws a wrench as arrow (force) and arrow + circle (torque)                                                                                    [geometry_msgs/msg/WrenchStamped](https://docs.ros.org/en/rolling/p/geometry_msgs/msg/WrenchStamped.html)                                                                                                                
     [Twist](#displaytypestwist)                              Draws a twist as arrow (linear) and arrow + circle (angular)                                                                                   [geometry_msgs/msg/TwistStamped](https://docs.ros.org/en/rolling/p/geometry_msgs/msg/TwistStamped.html)                                                                                                                  
     [Oculus](https://index.ros.org/p/oculus_rviz_plugins)                          Renders the RViz scene to an Oculus headset                                                                                                                                                                                                                                                                                                                             
  -- --------------------------------------------------------------------------- -- ------------------------------------------------------------------------------------------------------------------------------------------- -- ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ --

<a id="Configs"></a>

### Configurations

Different configurations of displays are often useful for different uses
of the visualizer. A configuration useful for a full PR2 is not
necessarily useful for a test cart, for example. To this end, the
visualizer lets you load and save different configurations.

A configuration contains:

- Displays + their properties
- Tool properties
- Camera type + settings for the initial viewpoint



```wiki
Note: With RViz for Groovy the configuration file format has changed, from `.vcg`/INI to `.rviz`/YAML, probably also the internal config mechanism. Unfortunately "the RViz in Groovy is not backwards compatible" ([[http://answers.ros.org/question/53689/rviz-vcg-vs-rviz-fuerte-vs-groovy/|related question]]). So there is no way of opening or converting old .rviz config files in Groovy's RViz.
```



#### 0.4 and above

The global/local configs (referenced below) have been removed, in favor
of a "Recent Configs" menu:

![attachment:recent_configs.png](doc/recent_configs.png)

#### 0.3 and below

There are also some built-in configurations available:

![attachment:global_configs.png](doc/global_configs.png)

If you save a config in the default folder, it will also show up in the
"Local Configs" list:

![attachment:local_configs.png](doc/local_configs.png)

### Views Panel

There are a number of different camera types available in the
visualizer, and the list will grow as time goes on:

![attachment:camera_types.png](doc/camera_types.png)

Camera types consist both of different ways of controlling the camera
and different types of projection (Orthographic vs. Perspective).

#### The different camera types

##### Orbital Camera (default)

The orbital camera simply rotates around a focal point, while always
looking at that point. The focal point is visualized as a small disc
while you're moving the camera:

![width=100%](doc/focal_point.png)

###### Controls

- **Left mouse button**: Click and drag to rotate around the focal
  point.
- **Middle mouse button**: Click and drag to move the focal point in the
  plane formed by the camera's up and right vectors. The distance moved
  depends on the focal point \-- if there is an object on the focal
  point, and you click on top of it, it will stay under your mouse.
- **Right mouse button**: Click and drag to zoom in/out of the focal
  point. Dragging up zooms in, down zooms out.
- **Scrollwheel**: Zoom in/out of the focal point

##### FPS (first-person) Camera

The FPS camera is a first-person camera, so it rotates as if you're
looking with your head.

###### Controls

- **Left mouse button**: Click and drag to rotate. Control-click to pick
  the object under the mouse and look directly at it.
- **Middle mouse button**: Click and drag to move along the plane formed
  by the camera's up and right vectors
- **Right mouse button**: Click and drag to move along the camera's
  forward vector. Dragging up moves forward, down moves backward.
- **Scrollwheel**: Move forward/backward

##### Top-down Orthographic

The top-down orthographic camera always looks down along the Z axis (in
the robot frame), and is an orthographic view which means things do not
get smaller as they get farther away.

###### Controls

- **Left mouse button**: Click and drag to rotate around the Z axis
- **Middle mouse button**: Click and drag to move the camera along the
  XY plane
- **Right mouse button**: Click and drag to zoom the image
- **Scrollwheel**: Zoom the image

##### XY Orbit

Same as the orbital camera, with the focus point restricted to the XY
plane.

###### Controls

See orbital camera.

##### Third Person Follower

The camera maintains a constant viewing angle towards the target frame.
In contrast to XY Orbit the camera turns if the target frame yaws. This
could be handy if you are doing 3D mapping of a hallway with corners for
example.

###### Controls

See orbital camera.

#### Views

The views panel also lets you create different named views, which are
saved and can be switched between. A view consists of a target frame,
camera type and camera pose. You can save a view by clicking the **Save
Current** button.

![attachment:views.png](doc/views.png)

A view consists of:

- View controller type
- View configuration (position, orientation, etc. Possibly different for
  each view controller type.)
- The [Target Frame](#TargetFrame)

Views are saved per user, not in the
[config files](#Configs).

<a id="Frames"></a>

### Coordinate Frames

rviz uses the [tf](https://index.ros.org/p/tf) transform system for
transforming data from the coordinate frame it arrives in into a global
reference frame. There are two coordinate frames that are important to
know about in the visualizer. Here is a video that explains them both:

[Youtube](https://www.youtube.com/watch?v=nD1Faww4m2c)

<a id="FixedFrame"></a>

#### The Fixed Frame

The more-important of the two frames is the fixed frame. The fixed frame
is the reference frame used to denote the "world" frame. This is
usually the "map", or "world", or something similar, but can also
be, for example, your odometry frame.

If the fixed frame is erroneously set to, say, the base of the robot,
then all the objects the robot has ever seen will appear in front of the
robot, at the position relative to the robot at which they were
detected. For correct results, **the fixed frame should not be moving
relative to the world**.

If you change the fixed frame, all data currently being shown is cleared
rather than re-transformed.

<a id="TargetFrame"></a>

#### The Target Frame

The target frame is the reference frame for the camera view. For
example, if your target frame is the map, you'll see the robot driving
around the map. If your target frame is the base of the robot, the robot
will stay in the same place while everything else moves relative to it.

### Tools

The visualizer has a number of tools you can use on the toolbar:

#### Move Camera (Keyboard shortcut: m)

The **Move Camera** tool is the default tool. When this is selected, the
current View gets to do its thing when you click inside the 3d view.

<a id="Selection"></a>

#### Select (Keyboard shortcut: s)

The **Select** tool allows you to select items being displayed in the 3D
view. It supports single-point selection as well as click/drag box
selection.

![width=100%](doc/selection_highlight.png)
![width=100%](doc/selection_selected.png)

You can add to a selection with the **Shift** key, and remove from the
selection with the **Ctrl** key. If you want to move the camera around
while selecting without switching back to the **Move Camera** tool you
can hold down the **Alt** key.

The **f** key will focus the camera on the current selection.

[Youtube](https://www.youtube.com/watch?v=KGXD-D6GAG8)

#### 2D Nav Goal (Keyboard shortcut: g)

This tool lets you set a goal sent on the "goal" ROS topic. Click on a
location on the ground plane and drag to select the orientation:

![width=100%](doc/set_goal.png)

This tool works with the
[navigation](https://index.ros.org/p/navigation) stack.

#### 2D Pose Estimate (Keyboard shortcut: p)

This tool lets you set an initial pose to seed the localization system
(sent on the "initialpose" ROS topic). Click on a location on the
ground plane and drag to select the orientation:

![width=100%](doc/set_pose.png)

This tool works with the
[navigation](https://index.ros.org/p/navigation) stack.

### Time

The **Time** panel is mostly useful when running in a simulator: it
allows you to see how much [ROS Time](Clock) time has passed, vs. how
much "Wall Clock" (aka real) time has passed.

The time panel also lets you reset the visualizer's internal time state
\-- this causes a reset of all the displays, as well as a reset of
[tf](https://index.ros.org/p/tf)'s internal cache of data.

![width=100%](doc/time.png)

If you are not running in simulation, the time panel is mostly useless.
In most cases it can be closed and you will probably not even notice
(other than having a bit more screen real estate for the rest of rviz).

### Stereo

Rviz can render in 3D stereo if you have a graphics card, monitor, and
glasses that support that. You can read how to set this up
[here](http://wiki.ros.org/rviz/Tutorials/Rviz%20in%20Stereo).

### Plugins

rviz is setup so that new displays can be added through plugins. In
fact, even the built-in displays are loaded through the "default"
plugin. The end result for you, the user, is that there is a way to
load/unload plugins from the UI. (Note that as of
[this commit](http://code.ros.org/lurker/message/20120814.213049.12b192ce.en.html),
all plugins are loaded automatically - there is no more UI.) If you
select the **Plugins->Manage\...** menu item, it will pop up a dialog
letting you manage loading/unloading plugins:

![attachment:manage_plugins.png](doc/manage_plugins.png)

If you unload a plugin which has displays active, they will no longer
display anything, but will keep their settings:

![attachment:unloaded_plugin.png](doc/unloaded_plugin.png)

If you're a programmer and are looking to write a plugin, take a look
at the plugin tutorials:
[Plugins: New Display Type](#plugins-new-display-type)
,
[Plugins: New Dockable Panel](#plugins-new-dockable-panel)
and
[Plugins: New Tool Type](#plugins-new-tool-type)

## Troubleshooting

### Turning off hardware acceleration

If your system uses the Mesa graphics drivers (e.g. for Intel GPUs,
inside a VM), hardware acceleration can cause problems. To get around
this, disable this before running RViz:



```
export LIBGL_ALWAYS_SOFTWARE=1
rosrun rviz rviz
```



### Problems you may encounter

#### Help!  My data is not showing up!

RViz uses [tf](https://index.ros.org/p/tf) to transform data based on
the frame_id and stamp members in the message header
([roslib/msg/Header](https://docs.ros.org/en/rolling/p/roslib/msg/Header.html)).
[tf](https://index.ros.org/p/tf) issues are the most common reason for
data to fail to be displayed.

There are generally three reasons for failure along these lines: 1. You
don't have a [tf](https://index.ros.org/p/tf) transform tree set up.
Possibel solution in this case:

- Set both the
  [Fixed and Target Frames](#Frames) to the
  same value as what is specified in the frame_id for the topic that is
  not receiving data.
- Find a node that is supposed to be running but actually not, by
  following steps. 1. Run the following. Usually
  [robot_state_publisher](https://index.ros.org/p/robot_state_publisher)
  is supposed to publish `tf`. 

```
rostopic echo /tf
rostopic info /tf
```

 1. Run this,
  then you see it subscribes to `/joint_states`.
  

```
rosnode info robot_state_publisher
```

 Find the node that's supposed to publish the
  topic: 

```
rostopic echo /joint_states
rostopic info joint_states
```


- Check if `rosparam use_siim_time` returns `true`, but there's no
  `/clock` topic being published. This means you're expecting to run
  the robot on simulation but [`Gazebo`](gazebo) that publishes the
  topic might not been running. In this case run `rosparam set
  use_sim_time false`. 1. You have a transform tree. Make sure the
  [Fixed Frame](#FixedFrame) is set to a
  frame that exists in your system. You can use the
  [TF Display](#displaytypestf) to help see if you
  have your frames set right. 1. You have a transform tree, and the
  [Fixed Frame](#FixedFrame) exists in it.
  This is often a timing or frame problem. See the
  [tf troubleshooting page](https://index.ros.org/p/tf) for more
  information.

Another common reason for nothing showing up is if the data being
displayed is not visible from your current view. Try moving around,
zooming in/out, or possibly switching to the top-down orthographic view
to find out where things are.

#### OpenGL-related crashes

##### "Cannot create GL vertex buffer"



```
[ERROR] [1315474799.086848538]: Caught exception while loading: OGRE EXCEPTION(7:InternalErrorException): Cannot create GL vertex buffer in GLHardwareVertexBuffer::GLHardwareVertexBuffer at /tmp/buildd/ros-electric-visualization-common-1.6.0/debian/ros-electric-visualization-common/opt/ros/electric/stacks/visualization_common/ogre/build/ogre_src_v1-7-1/RenderSystems/GL/src/OgreGLHardwareVertexBuffer.cpp (line 46)
```

 This is caused by a lack of the
GL_ARB_vertex_buffer_object OpenGL extension. I have seen two causes for
this apparent lack:

- Running rviz remotely (which is not supported)
- Version mismatch between libGL.so and the OpenGL driver.

More details and a fix for the mismatch are at
[ROS Answers - rviz-in-ros-electric](http://answers.ros.org/question/2109/rviz-in-ros-electric?answer=3627#3627).

##### No OpenGL Support



```
OgreGLSupport.cpp:57: virtual void Ogre::GLSupport::initialiseExtensions(): Assertion `pcVer && "Problems getting GL version string using glGetString"' failed.
```



This means you don't have OpenGL support available. Running through a
virtualization environment that does not support hardware accelerated 3D
is a common cause of this, as is not having the correct drivers
installed under Linux.

In general, if there are proprietary graphics drivers for your hardware
in Linux, use them instead of the (non accelerated) open source ones.

##### "No GLX FBConfig support" under VirtualBox



```
OGRE EXCEPTION(3:RenderingAPIException): No GLX FBConfig support on
your display in GLXGLSupport::GLXGLSupport at OgreGLXGLSupport.cpp
```



Unfortunately, hardware accelerated 3D in !VirtualBox is still
experimental, and this is a known issue with Ogre + !VirtualBox.
<http://www.ogre3d.org/forums/viewtopic.php?f=2&t=49278&p=350053>

##### Segfault during startup

Various OpenGL or Ogre things can go wrong during startup. One of them
seems to relate to the render-to-texture system. Ogre supports 3
different modes, and rviz uses the "PBuffer" mode by default. Some
users have reported some modes cause a segfault during startup, but it
is not clear which should be used when.

If you have a problem and want to try another "RTT mode", run rviz
with the environment variable OGRE_RTT_MODE set to either "Copy",
"PBuffer", or "FBO". For example: 

```
export OGRE_RTT_MODE=Copy
```



For the discussion and to give feedback about what works and what
doesn't, please see
[this bug report](https://code.ros.org/trac/ros-pkg/ticket/4830#comment:16).

#### Other crashes

##### "Zero sized texture surface"



```
terminate called after throwing an instance of 'Ogre::RenderingAPIException' 
  what():  OGRE EXCEPTION(3:RenderingAPIException): Zero sized texture surface on texture NavViewMapTexture0 face 0 mipmap 0. Probably, the GL driver refused to create the texture. in GLTexture::_createSurfaceList at OgreGLTexture.cpp (line 394)
```



This is caused by using a
[Map Display](#displaytypesmap) on a graphics card
that does not support textures larger than 2048 pixels on a side.
**Fixed in version 0.3**

##### Segfault in i915_dri.so

This is a bug in the intel graphics driver on certain Linux systems \--
Ubuntu Intrepid and Jaunty are known to have this issue. There is
currently no known fix/workaround except upgrading to Ubuntu Karmic or
downgrading to Ubuntu Hardy.

The callstack for this crash looks similar to: 

```
#0  0x00007febd7378a8b in ?? () from /usr/lib/dri/i915_dri.so
#1  0x00007febd7390d8a in ?? () from /usr/lib/dri/i915_dri.so
#2  0x00007febd73868ef in _tnl_run_pipeline () from /usr/lib/dri/i915_dri.so
#3  0x00007febd72df7c4 in ?? () from /usr/lib/dri/i915_dri.so
#4  0x00007febd7386eb0 in _tnl_draw_prims () from /usr/lib/dri/i915_dri.so
#5  0x00007febd737f88e in ?? () from /usr/lib/dri/i915_dri.so
#6  0x00007febd72ac5d1 in intel_clear_tris () from /usr/lib/dri/i915_dri.so
#7  0x00007febd72aca67 in ?? () from /usr/lib/dri/i915_dri.so
#8  0x00007febd773394d in Ogre::GLRenderSystem::clearFrameBuffer (
    this=0x7febd7a24d28, buffers=<value optimized out>,
    colour=<value optimized out>, depth=1, stencil=0)
    at OgreGLRenderSystem.cpp:3119
#9  0x00007febebcee5f7 in Ogre::SceneManager::_renderScene (
    this=0x7febd7a629c8, camera=0x7febd7a29638, vp=0x7febd7a28cc8,
    includeOverlays=<value optimized out>) at OgreSceneManager.cpp:1345
#10 0x00007febebcc274c in Ogre::RenderTarget::updateImpl (this=0x7febd7a268a8)
    at OgreRenderTarget.cpp:113
#11 0x00007febebcc22dc in Ogre::RenderTarget::update (this=0x1f24288, swap=160)
    at OgreRenderTarget.cpp:501
#12 0x00007febebcae42f in Ogre::RenderSystem::_updateAllRenderTargets (
    this=<value optimized out>, swapBuffers=false) at OgreRenderSystem.cpp:112
#13 0x00007febebce0e55 in Ogre::Root::_updateAllRenderTargets (
    this=0x7febd7a21908) at OgreRoot.cpp:1136
...
```



and the output on the command line may include:


```
get fences failed: -1
param: 6, val: 0
```



##### Bad Drawable

(From
<http://www.cse.sc.edu/~jokane/teaching/574/notes-turtlebot-sim.pdf>

Depending on the speciﬁc hardware on which you run RViz, you may
sometimes see errors when you attempt to start RViz. This could be
either a dreaded "Segmentation Fault", or an error about something
called a "Bad Drawable". In both cases, the error is fatal but
intermittent. This is a symptom of a known bug when RViz is used with
certain video cards. (See Section 2). There are two workarounds you can
try.

- First, you can try setting the environment variable OGRE_RTT_MODE to
  one of these three strings: Copy, PBuffer, or FBO. This setting
  changes some of the internal details of how the window is rendered.
  Depending on your conﬁguration, you may have better success with one
  of these options than others.
- Second, since the problem is intermittent, you can simply try starting
  RViz again and again until it succeeds. The best way to do this is to
  use a launch ﬁle, and include respawn="true" in the node tag for
  RViz.

[ For more detail, see this ticket](https://code.ros.org/trac/ros-pkg/ticket/4830)

#### Multiple Monitors

Some graphics drivers don't like when a 3D accelerated application
spans multiple monitors. Some drivers even only accelerate the primary
display. In either of these cases rviz may become slow or unresponsive.

In the first case, simply prevent the 3D window from spanning multiple
monitors. In the second, open rviz on your primary display.

<a id="reportingabug"></a>

### How to make a usable bug report

If you haven't found a solution on this page, on
[ROS Answers](http://answers.ros.org), or a Google search (the
[Ogre3D](http://www.ogre3d.org) package has a great
[discussion forum](http://www.ogre3d.org/forums/) for instance), please
follow these instructions when reporting a bug.

We need a lot of data about a crash or other failure in order to
understand the cause. Please include as much of this data as you can.

- `rosrun rviz system_info.sh` This command prints basic information
  about your OS and graphics card. Include the output of this.
- `Ogre.log` Run rviz with the "-l" option `rosrun rviz rviz -l` to
  produce an "Ogre.log" file in the current directory. Include the
  Ogre.log file.
- rviz output. rviz prints a bunch of useful info at the start, like the
  Ogre version number, the RTT mode, etc. Plus lots of
  potentially-relevant warning and error messages. Include the rviz
  console output. If you have to leave some out to make it a reasonable
  size, leave in the start and end portions at least.
- Stack trace. Run rviz in gdb, wait for your crash to happen, then type
  "backtrace". Include the full results.
- Core file. A core file is a dump of all the memory in use by a program
  when it crashed, so gives even more info than a stack trace. To get a
  core file (in linux, specifically in the "bash" shell) do:
- `ulimit -c unlimited` to remove the core file size limit (default is
  size 0).
- run rviz and cause the crash.
- a file named "core" or similar (sometimes with a process ID number
  in the name) should appear in the current directory. Include the core
  file.

Include as much of this info as you can and report the bug on
[Rviz Github Issues](https://github.com/ros-visualization/rviz/issues)

Or ask a question about it on [ROS Answers](http://answers.ros.org)

Please search the existing tickets and questions before posting to make
sure yours is not a duplicate.

Thanks!

## DisplayTypes

  -- --------------------------------------------------------------------------- -- ------------------------------------------------------------------------------------------------------------------------------------------- -- ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ --
     **Name**                                                                       **Description**                                                                                                                                **Messages Used**                                                                                                                                                                                                        
     [Axes](#displaytypesaxes)                                Displays a set of Axes                                                                                                                                                                                                                                                                                                                                                  
     [Effort](#displaytypeseffort)                            Shows the effort being put into each revolute joint of a robot.                                                                                [sensor_msgs/msg/JointStates](https://docs.ros.org/en/rolling/p/sensor_msgs/msg/JointStates.html)                                                                                                                        
     [Camera](#displaytypescamera)                            Creates a new rendering window from the perspective of a camera, and overlays the image on top of it.                                          [sensor_msgs/msg/Image](https://docs.ros.org/en/rolling/p/sensor_msgs/msg/Image.html), [sensor_msgs/msg/CameraInfo](https://docs.ros.org/en/rolling/p/sensor_msgs/msg/CameraInfo.html)                                   
     [Grid](#displaytypesgrid)                                Displays a 2D or 3D grid along a plane                                                                                                                                                                                                                                                                                                                                  
     [Grid Cells](#displaytypesgridcells)                     Draws cells from a grid, usually obstacles from a costmap from the [navigation](https://index.ros.org/p/navigation) stack.                     [nav_msgs/msg/GridCells](https://docs.ros.org/en/rolling/p/nav_msgs/msg/GridCells.html)                                                                                                                                  
     [Image](#displaytypesimage)                              Creates a new rendering window with an Image. Unlike the Camera display, this display does not use a !CameraInfo. *Version: Diamondback+*      [sensor_msgs/msg/Image](https://docs.ros.org/en/rolling/p/sensor_msgs/msg/Image.html)                                                                                                                                    
     [InteractiveMarker](#displaytypesinteractivemarker)      Displays 3D objects from one or multiple Interactive Marker servers and allows mouse interaction with them. *Version: Electric+*               [visualization_msgs/msg/InteractiveMarker](https://docs.ros.org/en/rolling/p/visualization_msgs/msg/InteractiveMarker.html)                                                                                              
     [Laser Scan](#displaytypeslaserscan)                     Shows data from a laser scan, with different options for rendering modes, accumulation, etc.                                                   [sensor_msgs/msg/LaserScan](https://docs.ros.org/en/rolling/p/sensor_msgs/msg/LaserScan.html)                                                                                                                            
     [Map](#displaytypesmap)                                  Displays a map on the ground plane.                                                                                                            [nav_msgs/msg/OccupancyGrid](https://docs.ros.org/en/rolling/p/nav_msgs/msg/OccupancyGrid.html)                                                                                                                          
     [Markers](#displaytypesmarker)                           Allows programmers to display arbitrary primitive shapes through a topic                                                                       [visualization_msgs/msg/Marker](https://docs.ros.org/en/rolling/p/visualization_msgs/msg/Marker.html), [visualization_msgs/msg/MarkerArray](https://docs.ros.org/en/rolling/p/visualization_msgs/msg/MarkerArray.html)   
     [Path](#displaytypespath)                                Shows a path from the [navigation](https://index.ros.org/p/navigation) stack.                                                                  [nav_msgs/msg/Path](https://docs.ros.org/en/rolling/p/nav_msgs/msg/Path.html)                                                                                                                                            
     [Point](#displaytypespoint)                              Draws a point as a small sphere.                                                                                                               [geometry_msgs/msg/PointStamped](https://docs.ros.org/en/rolling/p/geometry_msgs/msg/PointStamped.html)                                                                                                                  
     [Pose](#displaytypespose)                                Draws a pose as either an arrow or axes.                                                                                                       [geometry_msgs/msg/PoseStamped](https://docs.ros.org/en/rolling/p/geometry_msgs/msg/PoseStamped.html)                                                                                                                    
     [Pose Array](#displaytypesposearray)                     Draws a "cloud" of arrows, one for each pose in a pose array                                                                                 [geometry_msgs/msg/PoseArray](https://docs.ros.org/en/rolling/p/geometry_msgs/msg/PoseArray.html)                                                                                                                        
     [Point Cloud(2)](#displaytypespointcloud)                Shows data from a point cloud, with different options for rendering modes, accumulation, etc.                                                  [sensor_msgs/msg/PointCloud](https://docs.ros.org/en/rolling/p/sensor_msgs/msg/PointCloud.html), [sensor_msgs/msg/PointCloud2](https://docs.ros.org/en/rolling/p/sensor_msgs/msg/PointCloud2.html)                       
     [Polygon](#displaytypespolygon)                          Draws the outline of a polygon as lines.                                                                                                       [geometry_msgs/msg/Polygon](https://docs.ros.org/en/rolling/p/geometry_msgs/msg/Polygon.html)                                                                                                                            
     [Odometry](#displaytypesodometry)                        Accumulates odometry poses from over time.                                                                                                     [nav_msgs/msg/Odometry](https://docs.ros.org/en/rolling/p/nav_msgs/msg/Odometry.html)                                                                                                                                    
     [Range](#displaytypesrange)                              Displays cones representing range measurements from sonar or IR range sensors. *Version: Electric+*                                            [sensor_msgs/msg/Range](https://docs.ros.org/en/rolling/p/sensor_msgs/msg/Range.html)                                                                                                                                    
     [RobotModel](#displaytypesrobotmodel)                    Shows a visual representation of a robot in the correct pose (as defined by the current TF transforms).                                                                                                                                                                                                                                                                 
     [TF](#displaytypestf)                                    Displays the [tf](https://index.ros.org/p/tf) transform hierarchy.                                                                                                                                                                                                                                                                                                      
     [Wrench](#displaytypeswrench)                            Draws a wrench as arrow (force) and arrow + circle (torque)                                                                                    [geometry_msgs/msg/WrenchStamped](https://docs.ros.org/en/rolling/p/geometry_msgs/msg/WrenchStamped.html)                                                                                                                
     [Twist](#displaytypestwist)                              Draws a twist as arrow (linear) and arrow + circle (angular)                                                                                   [geometry_msgs/msg/TwistStamped](https://docs.ros.org/en/rolling/p/geometry_msgs/msg/TwistStamped.html)                                                                                                                  
     [Oculus](https://index.ros.org/p/oculus_rviz_plugins)                          Renders the RViz scene to an Oculus headset                                                                                                                                                                                                                                                                                                                             
  -- --------------------------------------------------------------------------- -- ------------------------------------------------------------------------------------------------------------------------------------------- -- ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ --

## Markers: Sending Basic Shapes (C++)

### Intro

Unlike other displays, the
[Marker Display](#displaytypesmarker) lets you
visualize data in rviz without rviz knowing anything about interpreting
that data. Instead, primitive objects are sent to the display through
[visualization_msgs/msg/Marker](https://docs.ros.org/en/rolling/p/visualization_msgs/msg/Marker.html)
messages, which let you show things like arrows, boxes, spheres and
lines.

This tutorial will show you how to send the four basic shapes (boxes,
spheres, cylinders, and arrows). We'll create a program that sends out
a new marker every second, replacing the last one with a different
shape.

Note: The
[rviz_visual_tools](https://github.com/PickNikRobotics/rviz_visual_tools)
package offers convenience functions for C++ users.

### Create a Package

Before getting started, let's create a package called
`using_markers`, somewhere in your package path:



```
{#!wiki buildsystem catkin
{{{
catkin_create_pkg using_markers roscpp visualization_msgs
```

 }}}} 

```
{#!wiki buildsystem rosbuild
{{{
roscreate-pkg using_markers roscpp visualization_msgs
```

 }}}}

### Sending Markers

#### The Code

Paste the following into `src/basic_shapes.cpp`:

Source:
[basic_shapes.cpp](https://github.com/ros-visualization/visualization_tutorials/blob/indigo-devel/visualization_marker_tutorials/src/basic_shapes.cpp)



```cpp
/*
 * Copyright (c) 2010, Willow Garage, Inc.
 * All rights reserved.
 *
 * Redistribution and use in source and binary forms, with or without
 * modification, are permitted provided that the following conditions are met:
 *
 *     * Redistributions of source code must retain the above copyright
 *       notice, this list of conditions and the following disclaimer.
 *     * Redistributions in binary form must reproduce the above copyright
 *       notice, this list of conditions and the following disclaimer in the
 *       documentation and/or other materials provided with the distribution.
 *     * Neither the name of the Willow Garage, Inc. nor the names of its
 *       contributors may be used to endorse or promote products derived from
 *       this software without specific prior written permission.
 *
 * THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS"
 * AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE
 * IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE
 * ARE DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT OWNER OR CONTRIBUTORS BE
 * LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR
 * CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF
 * SUBSTITUTE GOODS OR SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS
 * INTERRUPTION) HOWEVER CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN
 * CONTRACT, STRICT LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE)
 * ARISING IN ANY WAY OUT OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED OF THE
 * POSSIBILITY OF SUCH DAMAGE.
 */

#include <ros/ros.h>
#include <visualization_msgs/Marker.h>

int main( int argc, char** argv )
{
  ros::init(argc, argv, "basic_shapes");
  ros::NodeHandle n;
  ros::Rate r(1);
  ros::Publisher marker_pub = n.advertise<visualization_msgs::Marker>("visualization_marker", 1);

  // Set our initial shape type to be a cube
  uint32_t shape = visualization_msgs::Marker::CUBE;

  while (ros::ok())
  {
    visualization_msgs::Marker marker;
    // Set the frame ID and timestamp.  See the TF tutorials for information on these.
    marker.header.frame_id = "/my_frame";
    marker.header.stamp = ros::Time::now();

    // Set the namespace and id for this marker.  This serves to create a unique ID
    // Any marker sent with the same namespace and id will overwrite the old one
    marker.ns = "basic_shapes";
    marker.id = 0;

    // Set the marker type.  Initially this is CUBE, and cycles between that and SPHERE, ARROW, and CYLINDER
    marker.type = shape;

    // Set the marker action.  Options are ADD, DELETE, and new in ROS Indigo: 3 (DELETEALL)
    marker.action = visualization_msgs::Marker::ADD;

    // Set the pose of the marker.  This is a full 6DOF pose relative to the frame/time specified in the header
    marker.pose.position.x = 0;
    marker.pose.position.y = 0;
    marker.pose.position.z = 0;
    marker.pose.orientation.x = 0.0;
    marker.pose.orientation.y = 0.0;
    marker.pose.orientation.z = 0.0;
    marker.pose.orientation.w = 1.0;

    // Set the scale of the marker -- 1x1x1 here means 1m on a side
    marker.scale.x = 1.0;
    marker.scale.y = 1.0;
    marker.scale.z = 1.0;

    // Set the color -- be sure to set alpha to something non-zero!
    marker.color.r = 0.0f;
    marker.color.g = 1.0f;
    marker.color.b = 0.0f;
    marker.color.a = 1.0;

    marker.lifetime = ros::Duration();

    // Publish the marker
    while (marker_pub.getNumSubscribers() < 1)
    {
      if (!ros::ok())
      {
        return 0;
      }
      ROS_WARN_ONCE("Please create a subscriber to the marker");
      sleep(1);
    }
    marker_pub.publish(marker);

    // Cycle between different shapes
    switch (shape)
    {
    case visualization_msgs::Marker::CUBE:
      shape = visualization_msgs::Marker::SPHERE;
      break;
    case visualization_msgs::Marker::SPHERE:
      shape = visualization_msgs::Marker::ARROW;
      break;
    case visualization_msgs::Marker::ARROW:
      shape = visualization_msgs::Marker::CYLINDER;
      break;
    case visualization_msgs::Marker::CYLINDER:
      shape = visualization_msgs::Marker::CUBE;
      break;
    }

    r.sleep();
  }
}
```



Now edit the `CMakeLists.txt` file in your `using_markers` package,
and add:



```
{#!wiki buildsystem rosbuild
{{{
rosbuild_add_executable(basic_shapes src/basic_shapes.cpp)
```

 }}}} 

```
{#!wiki buildsystem catkin
{{{
add_executable(basic_shapes src/basic_shapes.cpp)
target_link_libraries(basic_shapes ${catkin_LIBRARIES})
```

 }}}} to the
bottom.

#### The Code Explained

Ok, let's break down the code piece by piece: 

```cpp
#include <ros/ros.h>
#include <visualization_msgs/Marker.h>
```


You should have seen the `ROS` include by now. We also include the
[visualization_msgs/msg/Marker](https://docs.ros.org/en/rolling/p/visualization_msgs/msg/Marker.html)
message definition.



```cpp
int main( int argc, char** argv )
{
  ros::init(argc, argv, "basic_shapes");
  ros::NodeHandle n;
  ros::Rate r(1);
  ros::Publisher marker_pub = n.advertise<visualization_msgs::Marker>("visualization_marker", 1);
```

 This should look familiar. We initialize ROS,
and create a `ros::Publisher` on the `visualization_marker` topic.



```cpp
  uint32_t shape = visualization_msgs::Marker::CUBE;
```

 Here we create an integer to keep track of
what shape we're going to publish. The four types we'll be using here
all use the
[visualization_msgs/msg/Marker](https://docs.ros.org/en/rolling/p/visualization_msgs/msg/Marker.html)
message in the same way, so we can simply switch out the shape type to
demonstrate the four different shapes.



```cpp
  while (ros::ok())
  {
    visualization_msgs::Marker marker;
    // Set the frame ID and timestamp.  See the TF tutorials for information on these.
    marker.header.frame_id = "/my_frame";
    marker.header.stamp = ros::Time::now();
```

 This begins the meat of the program. First we
create a
[visualization_msgs/msg/Marker](https://docs.ros.org/en/rolling/p/visualization_msgs/msg/Marker.html),
and begin filling it out. The `header` here is a
[roslib/msg/Header](https://docs.ros.org/en/rolling/p/roslib/msg/Header.html),
which should be familiar if you've done the
[tf](https://index.ros.org/p/tf)
[tutorials](https://index.ros.org/p/tf). We set the `frame_id` member
to `/my_frame` as an example. In a running system this should be the
frame relative to which you want the marker's pose to be interpreted.



```cpp
    marker.ns = "basic_shapes";
    marker.id = 0;
```

 The namespace (`ns`) and `id` are used to
create a unique name for this marker. If a marker message is received
with the same `ns` and `id`, the new marker will replace the old
one.



```cpp
    marker.type = shape;
```

 This `type` field is what specifies the kind
of marker we're sending. The available types are enumerated in the
[visualization_msgs/msg/Marker](https://docs.ros.org/en/rolling/p/visualization_msgs/msg/Marker.html)
message. Here we set the type to our `shape` variable, which will
change every time through the loop.



```cpp
    marker.action = visualization_msgs::Marker::ADD;
```

 The `action` field is what specifies what to
do with the marker. The options are `visualization_msgs::Marker::ADD`
and `visualization_msgs::Marker::DELETE`. `ADD` is something of a
misnomer, it really means "create or modify". A new `action` has
been added to delete all markers in the particular Rviz display,
regardless of ID or namespace. The value is `3` and in future ROS
version the message will change to have value
`visualization_msgs::Marker::DELETEALL`.



```cpp
    marker.pose.position.x = 0;
    marker.pose.position.y = 0;
    marker.pose.position.z = 0;
    marker.pose.orientation.x = 0.0;
    marker.pose.orientation.y = 0.0;
    marker.pose.orientation.z = 0.0;
    marker.pose.orientation.w = 1.0;
```

 Here we set the pose of the marker. The
[geometry_msgs/msg/Pose](https://docs.ros.org/en/rolling/p/geometry_msgs/msg/Pose.html)
message consists of a
[geometry_msgs/msg/Vector3](https://docs.ros.org/en/rolling/p/geometry_msgs/msg/Vector3.html)
to specify the position and a
[geometry_msgs/msg/Quaternion](https://docs.ros.org/en/rolling/p/geometry_msgs/msg/Quaternion.html)
to specify the orientation. Here we set the position to the origin, and
the orientation to the identity orientation (note the 1.0 for `w`).



```cpp
    marker.scale.x = 1.0;
    marker.scale.y = 1.0;
    marker.scale.z = 1.0;
```

 Now we specify the scale of the marker. For
the basic shapes, a scale of 1 in all directions means 1 meter on a
side.



```cpp
    marker.color.r = 0.0f;
    marker.color.g = 1.0f;
    marker.color.b = 0.0f;
    marker.color.a = 1.0;
```

 The color of the marker is specified as a
[std_msgs/msg/ColorRGBA](https://docs.ros.org/en/rolling/p/std_msgs/msg/ColorRGBA.html).
Each member should be between 0 and 1. An alpha (`a`) value of 0 means
completely transparent (invisible), and 1 is completely opaque.



```cpp
    marker.lifetime = ros::Duration();
```

 The `lifetime` field specifies how long this
marker should stick around before being automatically deleted. A value
of `ros::Duration()` means never to auto-delete.

If a new marker message is received before the `lifetime` has been
reached, the `lifetime` will be reset to the value in the new marker
message.



```cpp
    while (marker_pub.getNumSubscribers() < 1)
    {
      if (!ros::ok())
      {
        return 0;
      }
      ROS_WARN_ONCE("Please create a subscriber to the marker");
      sleep(1);
    }
    marker_pub.publish(marker);
```

 We wait for the marker to have a subscriber
and we then publish the marker. Note that you can also use a
[latched publisher](https://index.ros.org/p/rospy) as an alternative to
this code.



```cpp
    switch (shape)
    {
    case visualization_msgs::Marker::CUBE:
      shape = visualization_msgs::Marker::SPHERE;
      break;
    case visualization_msgs::Marker::SPHERE:
      shape = visualization_msgs::Marker::ARROW;
      break;
    case visualization_msgs::Marker::ARROW:
      shape = visualization_msgs::Marker::CYLINDER;
      break;
    case visualization_msgs::Marker::CYLINDER:
      shape = visualization_msgs::Marker::CUBE;
      break;
    }
```

 This code lets us show all four shapes while
just publishing the one marker message. Based on the current shape, we
set what the next shape to publish will be.



```cpp
    r.sleep();
  }
```

 Sleep and loop back to the top.

#### Building the Code

You should be able to build the code with:



```
{#!wiki buildsystem catkin
{{{
$ cd %TOP_DIR_YOUR_CATKIN_WORKSPACE%
$ catkin_make
```

 }}}} 

```
{#!wiki buildsystem rosbuild
{{{
rosmake using_markers
```

 }}}}

#### Running the Code

You should be able to run the code with:



```
rosrun using_markers basic_shapes
```



### Viewing the Markers

Now that you're publishing markers, you need to set rviz up to view
them. First, make sure rviz is built:



```
rosmake rviz
```

 Now, run rviz:



```
rosrun using_markers basic_shapes
rosrun rviz rviz
```

 If you've never used rviz before, please see
the [User's Guide](#userguide) to get you started.



```wiki
The first thing to do, because we don't have any [[tf]] transforms setup, is to set the [[rviz/UserGuide#Frames|Fixed Frames]] to the frame we set the marker to above, `/my_frame`. In order to do so, set the Fixed Frame field to "/my_frame".
```



Next add a [Markers](#displaytypesmarker) display.
Notice that the default topic specified, `visualization_marker`, is
the same as the one being published.

You should now see a marker at the origin that changes shape every
second: ![Basic Shapes](doc/basic_shapes_tutorial.png)

### More Information

For more information on the different types of markers beyond the ones
shown here, please see the
[Markers Display Page](#displaytypesmarker)

## Markers: Points and Lines (C++)

### Intro

In the
[Markers: Basic Shapes](#markers-sending-basic-shapes-c)
you learned how to send simple shapes to rviz using visualization
markers. You can send more than just simple shapes though, and this
tutorial will introduce you to the `POINTS`, `LINE_STRIP` and
`LINE_LIST` marker types. For a full list of types, see the
[Marker Display page](#displaytypesmarker).

### Using Points, Line Strips, and Line Lists

The `POINTS`, `LINE_STRIP` and `LINE_LIST` markers all use the
`points` member of the
[visualization_msgs/msg/Marker](https://docs.ros.org/en/rolling/p/visualization_msgs/msg/Marker.html)
message. The `POINTS` type places a point at each point added. The
`LINE_STRIP` type uses each point as a vertex in a connected set of
lines, where point 0 is connected to point 1, 1 to 2, 2 to 3, etc. The
`LINE_LIST` type creates unconnected lines out of each pair of points,
i.e. point 0 to 1, 2 to 3, etc.

Anyway, let's get to the code:

#### The Code

Source:
[points_and_lines.cpp](https://github.com/ros-visualization/visualization_tutorials/blob/indigo-devel/visualization_marker_tutorials/src/points_and_lines.cpp)



```cpp
/*
 * Copyright (c) 2010, Willow Garage, Inc.
 * All rights reserved.
 *
 * Redistribution and use in source and binary forms, with or without
 * modification, are permitted provided that the following conditions are met:
 *
 *     * Redistributions of source code must retain the above copyright
 *       notice, this list of conditions and the following disclaimer.
 *     * Redistributions in binary form must reproduce the above copyright
 *       notice, this list of conditions and the following disclaimer in the
 *       documentation and/or other materials provided with the distribution.
 *     * Neither the name of the Willow Garage, Inc. nor the names of its
 *       contributors may be used to endorse or promote products derived from
 *       this software without specific prior written permission.
 *
 * THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS"
 * AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE
 * IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE
 * ARE DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT OWNER OR CONTRIBUTORS BE
 * LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR
 * CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF
 * SUBSTITUTE GOODS OR SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS
 * INTERRUPTION) HOWEVER CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN
 * CONTRACT, STRICT LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE)
 * ARISING IN ANY WAY OUT OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED OF THE
 * POSSIBILITY OF SUCH DAMAGE.
 */

#include <ros/ros.h>
#include <visualization_msgs/Marker.h>

#include <cmath>

int main( int argc, char** argv )
{
  ros::init(argc, argv, "points_and_lines");
  ros::NodeHandle n;
  ros::Publisher marker_pub = n.advertise<visualization_msgs::Marker>("visualization_marker", 10);

  ros::Rate r(30);

  float f = 0.0;
  while (ros::ok())
  {
    visualization_msgs::Marker points, line_strip, line_list;
    points.header.frame_id = line_strip.header.frame_id = line_list.header.frame_id = "/my_frame";
    points.header.stamp = line_strip.header.stamp = line_list.header.stamp = ros::Time::now();
    points.ns = line_strip.ns = line_list.ns = "points_and_lines";
    points.action = line_strip.action = line_list.action = visualization_msgs::Marker::ADD;
    points.pose.orientation.w = line_strip.pose.orientation.w = line_list.pose.orientation.w = 1.0;

    points.id = 0;
    line_strip.id = 1;
    line_list.id = 2;

    points.type = visualization_msgs::Marker::POINTS;
    line_strip.type = visualization_msgs::Marker::LINE_STRIP;
    line_list.type = visualization_msgs::Marker::LINE_LIST;

    // POINTS markers use x and y scale for width/height respectively
    points.scale.x = 0.2;
    points.scale.y = 0.2;

    // LINE_STRIP/LINE_LIST markers use only the x component of scale, for the line width
    line_strip.scale.x = 0.1;
    line_list.scale.x = 0.1;

    // Points are green
    points.color.g = 1.0f;
    points.color.a = 1.0;

    // Line strip is blue
    line_strip.color.b = 1.0;
    line_strip.color.a = 1.0;

    // Line list is red
    line_list.color.r = 1.0;
    line_list.color.a = 1.0;

    // Create the vertices for the points and lines
    for (uint32_t i = 0; i < 100; ++i)
    {
      float y = 5 * sin(f + i / 100.0f * 2 * M_PI);
      float z = 5 * cos(f + i / 100.0f * 2 * M_PI);

      geometry_msgs::Point p;
      p.x = (int32_t)i - 50;
      p.y = y;
      p.z = z;

      points.points.push_back(p);
      line_strip.points.push_back(p);

      // The line list needs two points for each line
      line_list.points.push_back(p);
      p.z += 1.0;
      line_list.points.push_back(p);
    }

    marker_pub.publish(points);
    marker_pub.publish(line_strip);
    marker_pub.publish(line_list);

    r.sleep();

    f += 0.04;
  }
}
```



#### The Code Explained

Now let's break down the code, skipping things that were explained in
the previous tutorial. The overall effect created is a rotating helix
with lines sticking upwards from each vertex.



```cpp
    visualization_msgs::Marker points, line_strip, line_list;
    points.header.frame_id = line_strip.header.frame_id = line_list.header.frame_id = "/my_frame";
    points.header.stamp = line_strip.header.stamp = line_list.header.stamp = ros::Time::now();
    points.ns = line_strip.ns = line_list.ns = "points_and_lines";
    points.action = line_strip.action = line_list.action = visualization_msgs::Marker::ADD;
    points.pose.orientation.w = line_strip.pose.orientation.w = line_list.pose.orientation.w = 1.0;
```



Here we create three
[visualization_msgs/msg/Marker](https://docs.ros.org/en/rolling/p/visualization_msgs/msg/Marker.html)
messages and initialize all of their shared data. We take advantage of
the fact that message members default to 0 and only set the `w` member
of the pose.



```cpp
    points.id = 0;
    line_strip.id = 1;
    line_list.id = 2;
```



We assign three different ids to the three markers. The use of the
`points_and_lines` namespace ensures they won't collide with other
broadcasters.



```cpp
    points.type = visualization_msgs::Marker::POINTS;
    line_strip.type = visualization_msgs::Marker::LINE_STRIP;
    line_list.type = visualization_msgs::Marker::LINE_LIST;
```



Here we set the marker types to `POINTS`, `LINE_STRIP` and
`LINE_LIST`.



```cpp
    // POINTS markers use x and y scale for width/height respectively
    points.scale.x = 0.2;
    points.scale.y = 0.2;

    // LINE_STRIP/LINE_LIST markers use only the x component of scale, for the line width
    line_strip.scale.x = 0.1;
    line_list.scale.x = 0.1;
```



The `scale` member means different things for these marker types. The
`POINTS` marker uses the `x` and `y` members for width and height
respectively, while the `LINE_STRIP` and `LINE_LIST` markers only
use the `x` component, which defines the line width. Scale values are
in meters.



```cpp
    // Points are green
    points.color.g = 1.0f;
    points.color.a = 1.0;

    // Line strip is blue
    line_strip.color.b = 1.0;
    line_strip.color.a = 1.0;

    // Line list is red
    line_list.color.r = 1.0;
    line_list.color.a = 1.0;
```



Here we set the points to green, the line strip to blue, and the line
list to red.



```cpp
    // Create the vertices for the points and lines
    for (uint32_t i = 0; i < 100; ++i)
    {
      float y = 5 * sin(f + i / 100.0f * 2 * M_PI);
      float z = 5 * cos(f + i / 100.0f * 2 * M_PI);

      geometry_msgs::Point p;
      p.x = (int32_t)i - 50;
      p.y = y;
      p.z = z;

      points.points.push_back(p);
      line_strip.points.push_back(p);

      // The line list needs two points for each line
      line_list.points.push_back(p);
      p.z += 1.0;
      line_list.points.push_back(p);
    }
```



We use sine and cosine to generate a helix. The `POINTS` and
`LINE_STRIP` markers both require only a point for each vertex, while
the `LINE_LIST` marker requires 2.

#### Viewing the Markers

Set up rviz the same way you did in the last tutorial, which is as
follows:

Edit the `CMakeLists.txt` file in your `using_markers` package, and
add to the bottom:



```
{#!wiki buildsystem rosbuild
{{{
rosbuild_add_executable(points_and_lines src/points_and_lines.cpp)
```

 Then, 

```
$ rosmake using_markers
```

 }}}}


```
{#!wiki buildsystem catkin
{{{
add_executable(points_and_lines src/points_and_lines.cpp)
target_link_libraries(points_and_lines ${catkin_LIBRARIES})
```

 Then, 

```
$ catkin_make
```

 }}}} Then,



```
$ rosrun rviz rviz &
$ rosrun using_markers points_and_lines
```

 You should see a rotating helix that looks
something like this:

![Basic Shapes](doc/points_and_lines_marker_tutorial.png)

### Next Steps

The [Marker Display page](#displaytypesmarker) has
a list of all the markers and options supported by rviz. Try out some of
the other markers!

## Interactive Markers: Getting Started

### Intro

Interactive markers are similar to the "regular" markers described in
the previous tutorials, however they allow the user to interact with
them by changing their position or rotation, clicking on them or
selecting something from a context menu assigned to each marker.

They are represented by the
[visualization_msgs/msg/InteractiveMarker](https://docs.ros.org/en/rolling/p/visualization_msgs/msg/InteractiveMarker.html)
message, which contains a context menu and several controls
([visualization_msgs/msg/InteractiveMarkerControl](https://docs.ros.org/en/rolling/p/visualization_msgs/msg/InteractiveMarkerControl.html)).
The controls define the different visual parts of the interactive
marker, can consist of several regular markers
([visualization_msgs/msg/Marker](https://docs.ros.org/en/rolling/p/visualization_msgs/msg/Marker.html))
and can each have a different function.

![The structure of an \[\[https://docs.ros.org/en/rolling/p/visualization_msgs/msg/InteractiveMarker.html\|visualization_msgs/msg/InteractiveMarker\]\] message](doc/interactive_marker_structure.png)

If you want to create a node providing a set of interactive markers, you
need to instantiate an `InteractiveMarkerServer` object. This will
handle the connection to the client (usually RViz) and make sure that
all changes you make are being transmitted and that your application is
being notified of all the actions the user performs on the interactive
markers.

![attachment:interactive_marker_architecture.png](doc/interactive_marker_architecture.png)

### Further Documentation

To find out more about how to use interactive markers, refer to this and
the following tutorials. The source code used can be found in the
[interactive_marker_tutorials](https://index.ros.org/p/interactive_marker_tutorials)
package.

For writing applications using interactive markers, you will most likely
use the interfaces provided in the
[interactive_markers](https://index.ros.org/p/interactive_markers)
package. Refer to the
[Code API](http://www.ros.org/doc/api/interactive_markers/html/) for
more information.

The messages used to describe interactive markers themselves contain a
detailed description of all their parameters. Of main interest are
[visualization_msgs/msg/InteractiveMarker](https://docs.ros.org/en/rolling/p/visualization_msgs/msg/InteractiveMarker.html),
[visualization_msgs/msg/InteractiveMarkerControl](https://docs.ros.org/en/rolling/p/visualization_msgs/msg/InteractiveMarkerControl.html)
and
[visualization_msgs/msg/InteractiveMarkerFeedback](https://docs.ros.org/en/rolling/p/visualization_msgs/msg/InteractiveMarkerFeedback.html).
The recommended way to create context menus is using the
[MenuHandler](http://www.ros.org/doc/api/interactive_markers/html/classinteractive__markers_1_1MenuHandler.html)
interface, so you will not have to deal with the underlying messages.

### The interactive_marker_tutorials Package

The best way to understand what interactive markers do is by trying out
the examples contained in the
[interactive_marker_tutorials](https://index.ros.org/p/interactive_marker_tutorials)
package. It contains five examples:
[simple_marker](#simple_marker),
[basic_controls](#basic_controls),
[menu](#menu),
[pong](#pong)
and
[cube](#cube).

#### How To Run The Tutorials

The procedure to run the tutorials is basically the same in all case.
E.g. to run **basic_controls**, open a terminal and type



```
rosrun interactive_marker_tutorials basic_controls
```



This will start the node which contains the interactive marker server.
Then, start RViz by running the following command in a separate
terminal:



```
rosrun rviz rviz
```



In RViz, do the following:

- Set the fixed frame to '/base_link'.
- **Add an 'Interactive Markers' display** by clicking on 'Add' in
  the 'Displays' panel.
- **Set the update topic of this display to
  '/basic_controls/update'.** This should immediately bring up several
  grey cubes in rviz.
- **Now select 'Interact' in the tool panel.** This will enable all
  interactive elements in the main view, which will bring up additional
  arrows and rings around the boxes. You can left-click on these
  controls and in some case on the box itself to change the pose of each
  interactive marker. Some markers have a context menu which you can
  access by right-clicking on them.
- **Add a 'Grid' display.** This is a useful visual clue for
  perceiving how the markers move in space while you drag them.

<a id="simple_marker"></a>

#### simple_marker

Code (C++):
<https://github.com/ros-visualization/visualization_tutorials/blob/indigo-devel/interactive_marker_tutorials/src/simple_marker.cpp>

Code (Python)
<https://github.com/ros-visualization/visualization_tutorials/blob/indigo-devel/interactive_marker_tutorials/scripts/simple_marker.py>

This example will display a minimalist marker in RViz. See
[Writing a Simple Interactive Marker Server](#interactive-markers-writing-a-simple-interactive-marker-server)
for more details.

![width=100%](doc/simple_marker.png)

<a id="basic_controls"></a>

#### basic_controls

Code (C++):
<https://github.com/ros-visualization/visualization_tutorials/blob/indigo-devel/interactive_marker_tutorials/src/basic_controls.cpp>

Code (Python):
<https://github.com/ros-visualization/visualization_tutorials/blob/indigo-devel/interactive_marker_tutorials/scripts/basic_controls.py>

Displays a selection of interactive markers that can be manipulated in
different ways. It is explained in more detail in the
[Basic Controls](#interactive-markers-basic-controls)
tutorial.

![width=100%](doc/basic_controls.png)

<a id="menu"></a>

#### menu

Code (C++):
<https://github.com/ros-visualization/visualization_tutorials/blob/indigo-devel/interactive_marker_tutorials/src/menu.cpp>

Code (Python):
<https://github.com/ros-visualization/visualization_tutorials/blob/indigo-devel/interactive_marker_tutorials/scripts/menu.py>

Shows how to manage a more complex context menu associated with an
interactive marker, including hiding entries and adding check boxes.

![width=100%](doc/menu.png)

<a id="pong"></a>

#### pong

Code (C++):
<https://github.com/ros-visualization/visualization_tutorials/blob/indigo-devel/interactive_marker_tutorials/src/pong.cpp>

Lets you play the classic arcade game with one or two players in rviz.
It is meant to \--(distract you from your work)\-\-- demonstrate the
two-way interaction between an interactive marker server and multiple
clients.

If you open two instances of RViz on different computers that are
connected to the same pong server, you can play against each other.
Otherwise, the computer will take control of the unused paddle.

![width=100%](doc/pong.png)

<a id="cube"></a>

#### cube

Code (C++):
<https://github.com/ros-visualization/visualization_tutorials/blob/indigo-devel/interactive_marker_tutorials/src/cube.cpp>

Code (Python):
<https://github.com/ros-visualization/visualization_tutorials/blob/indigo-devel/interactive_marker_tutorials/scripts/cube.py>

Demonstrates how to procedurally create and manage a large number of
interactive markers.

![width=100%](doc/cube.png)

## Interactive Markers: Writing a Simple Interactive Marker Server

### The simple_marker tutorial explained

If you run the simple_marker example from
[interactive_marker_tutorials](https://index.ros.org/p/interactive_marker_tutorials)
as described in the
[previous tutorial](#interactive-markers-getting-started),
you will see this in RViz:

![The simple_marker example showing in RViz](doc/rviz_Tutorials_Interactive%20Markers%3A%20Writing%20a%20Simple%20Interactive%20Marker%20Server_simple_marker.png)

It shows the single interactive marker provided by the server node.
Click on the arrow to move the box. What you will also see is that the
server node prints out the current position of the marker each time you
change it in RViz.

This is the code of the server node:

Source:
[simple_marker.cpp](https://github.com/ros-visualization/visualization_tutorials/blob/indigo-devel/interactive_marker_tutorials/src/simple_marker.cpp)



```cpp
#include <ros/ros.h>

#include <interactive_markers/interactive_marker_server.h>

void processFeedback(
    const visualization_msgs::InteractiveMarkerFeedbackConstPtr &feedback )
{
  ROS_INFO_STREAM( feedback->marker_name << " is now at "
      << feedback->pose.position.x << ", " << feedback->pose.position.y
      << ", " << feedback->pose.position.z );
}

int main(int argc, char** argv)
{
  ros::init(argc, argv, "simple_marker");

  // create an interactive marker server on the topic namespace simple_marker
  interactive_markers::InteractiveMarkerServer server("simple_marker");

  // create an interactive marker for our server
  visualization_msgs::InteractiveMarker int_marker;
  int_marker.header.frame_id = "base_link";
  int_marker.header.stamp=ros::Time::now();
  int_marker.name = "my_marker";
  int_marker.description = "Simple 1-DOF Control";

  // create a grey box marker
  visualization_msgs::Marker box_marker;
  box_marker.type = visualization_msgs::Marker::CUBE;
  box_marker.scale.x = 0.45;
  box_marker.scale.y = 0.45;
  box_marker.scale.z = 0.45;
  box_marker.color.r = 0.5;
  box_marker.color.g = 0.5;
  box_marker.color.b = 0.5;
  box_marker.color.a = 1.0;

  // create a non-interactive control which contains the box
  visualization_msgs::InteractiveMarkerControl box_control;
  box_control.always_visible = true;
  box_control.markers.push_back( box_marker );

  // add the control to the interactive marker
  int_marker.controls.push_back( box_control );

  // create a control which will move the box
  // this control does not contain any markers,
  // which will cause RViz to insert two arrows
  visualization_msgs::InteractiveMarkerControl rotate_control;
  rotate_control.name = "move_x";
  rotate_control.interaction_mode =
      visualization_msgs::InteractiveMarkerControl::MOVE_AXIS;

  // add the control to the interactive marker
  int_marker.controls.push_back(rotate_control);

  // add the interactive marker to our collection &
  // tell the server to call processFeedback() when feedback arrives for it
  server.insert(int_marker, &processFeedback);

  // 'commit' changes and send to all clients
  server.applyChanges();

  // start the ROS main loop
  ros::spin();
}
```



**What this does is the following:**

- Define a function *processFeedback* which handles feedback messages
  from RViz by printing out the position.
- Initialize roscpp.
- Create an interactive marker server object.
- Setup the interactive marker and add it to the server's collection.
- Enter the ROS message loop.

Note that when calling *insert*, the server object will internally only
push the new marker onto a waiting list. Once you call *applyChanges*,
it will incorporate it into it's publicly visible set of interactive
markers and send it to all connected clients.

That's all there is. You are now ready to go on to the next tutorial:
[Interactive Markers: Basic Controls](#interactive-markers-basic-controls).

## Interactive Markers: Basic Controls

### The basic_controls tutorial explained

![The basic_controls tutorial showing in RViz](doc/im_tutorials.png)

This tutorial shows you most of the common options you have for
designing interactive markers. The node providing will print all
feedback it gets from RViz on the command line.

All interactive markers contain a grey box, which in most cases will do
nothing more than move together with the rest of the controls. It will
show you how the coordinate frame of the Interactive Marker moves.

### Simple 6-DOF control

![The structure of an \[\[https://docs.ros.org/en/rolling/p/visualization_msgs/msg/InteractiveMarker.html\|visualization_msgs/msg/InteractiveMarker\]\] message](doc/6dof.png)

This shows how to control all 6 degrees of freedom using 6 separate
controls. Use the rings to rotate and the arrows to move the structure.

### Simple 6-DOF control (fixed orientation)

![The structure of an \[\[https://docs.ros.org/en/rolling/p/visualization_msgs/msg/InteractiveMarker.html\|visualization_msgs/msg/InteractiveMarker\]\] message](doc/6dof2.png)

Identical to the 6-DOF control, with the exception that the orientation
of the controls will stay fixed, independent of the orientation of the
frame being controlled.

Source:
[basic_controls.cpp](https://github.com/ros-visualization/visualization_tutorials/blob/groovy-devel/interactive_marker_tutorials/src/basic_controls.cpp)



```cpp
Marker makeBox( InteractiveMarker &msg )
{
  Marker marker;

  marker.type = Marker::CUBE;
  marker.scale.x = msg.scale * 0.45;
  marker.scale.y = msg.scale * 0.45;
  marker.scale.z = msg.scale * 0.45;
  marker.color.r = 0.5;
  marker.color.g = 0.5;
  marker.color.b = 0.5;
  marker.color.a = 1.0;

  return marker;
}

InteractiveMarkerControl& makeBoxControl( InteractiveMarker &msg )
{
  InteractiveMarkerControl control;
  control.always_visible = true;
  control.markers.push_back( makeBox(msg) );
  msg.controls.push_back( control );

  return msg.controls.back();
}
```



Source:
[basic_controls.cpp](https://github.com/ros-visualization/visualization_tutorials/blob/groovy-devel/interactive_marker_tutorials/src/basic_controls.cpp)



```cpp
void make6DofMarker( bool fixed, unsigned int interaction_mode, const tf::Vector3& position, bool show_6dof )
{
  InteractiveMarker int_marker;
  int_marker.header.frame_id = "base_link";
  tf::pointTFToMsg(position, int_marker.pose.position);
  int_marker.scale = 1;

  int_marker.name = "simple_6dof";
  int_marker.description = "Simple 6-DOF Control";

  // insert a box
  makeBoxControl(int_marker);
  int_marker.controls[0].interaction_mode = interaction_mode;

  InteractiveMarkerControl control;

  if ( fixed )
  {
    int_marker.name += "_fixed";
    int_marker.description += "\n(fixed orientation)";
    control.orientation_mode = InteractiveMarkerControl::FIXED;
  }

  if (interaction_mode != visualization_msgs::InteractiveMarkerControl::NONE)
  {
      std::string mode_text;
      if( interaction_mode == visualization_msgs::InteractiveMarkerControl::MOVE_3D )         mode_text = "MOVE_3D";
      if( interaction_mode == visualization_msgs::InteractiveMarkerControl::ROTATE_3D )       mode_text = "ROTATE_3D";
      if( interaction_mode == visualization_msgs::InteractiveMarkerControl::MOVE_ROTATE_3D )  mode_text = "MOVE_ROTATE_3D";
      int_marker.name += "_" + mode_text;
      int_marker.description = std::string("3D Control") + (show_6dof ? " + 6-DOF controls" : "") + "\n" + mode_text;
  }

  if(show_6dof)
  {
    control.orientation.w = 1;
    control.orientation.x = 1;
    control.orientation.y = 0;
    control.orientation.z = 0;
    control.name = "rotate_x";
    control.interaction_mode = InteractiveMarkerControl::ROTATE_AXIS;
    int_marker.controls.push_back(control);
    control.name = "move_x";
    control.interaction_mode = InteractiveMarkerControl::MOVE_AXIS;
    int_marker.controls.push_back(control);

    control.orientation.w = 1;
    control.orientation.x = 0;
    control.orientation.y = 1;
    control.orientation.z = 0;
    control.name = "rotate_z";
    control.interaction_mode = InteractiveMarkerControl::ROTATE_AXIS;
    int_marker.controls.push_back(control);
    control.name = "move_z";
    control.interaction_mode = InteractiveMarkerControl::MOVE_AXIS;
    int_marker.controls.push_back(control);

    control.orientation.w = 1;
    control.orientation.x = 0;
    control.orientation.y = 0;
    control.orientation.z = 1;
    control.name = "rotate_y";
    control.interaction_mode = InteractiveMarkerControl::ROTATE_AXIS;
    int_marker.controls.push_back(control);
    control.name = "move_y";
    control.interaction_mode = InteractiveMarkerControl::MOVE_AXIS;
    int_marker.controls.push_back(control);
  }

  server->insert(int_marker);
  server->setCallback(int_marker.name, &processFeedback);
  if (interaction_mode != visualization_msgs::InteractiveMarkerControl::NONE)
    menu_handler.apply( *server, int_marker.name );
}
```



The code section above shows how to construct the first two interactive
markers. After adding the grey box, 6 controls for each degree of
freedom are added. No markers are added to these controls, which will
result in RViz creating a set of colored rings and arrows as a default
visualization.

The only difference between the two is that in the second case, the
orientation mode is set to `InteractiveMarkerControl::FIXED`, while in
the first it is left at its default value, which is
`InteractiveMarkerControl::INHERIT`.

Note that the 3D controls (shown lower in this list) are constructed
using this function as well. For the simple 6-DOF controls shown above,
the block under `if(interaction_mode !=
InteractiveMarkerControl::NONE)` is ignored.

**NOTE:** The orientations in the above code snippet can be confusing.
If you compute the rotation matrices corresponding to each of the
quaternions, you can verify that the specified orientation is correct.

### 3D Controls

![The structure of an \[\[https://docs.ros.org/en/rolling/p/visualization_msgs/msg/InteractiveMarker.html\|visualization_msgs/msg/InteractiveMarker\]\] message](doc/move_rotate_3D.png)

These new marker types support various kinds of 3D motion with a mouse.

- MOVE_3D: Drawn as a box-marker in the tutorial, this interaction mode
  allows 3D translation of the marker (in the camera plane by default,
  and into/out-of the camera while holding shift).
- ROTATE_3D: Drawn as a box marker in this tutorial, this interacton
  mode allows 3D rotation of the marker (about the camera plane's
  vertical and horizontal axes by default, and about the axis
  perpendicular to the camera plane while holding shift).
- MOVE_ROTATE_3D: This interaction mode is the union of MOVE_3D
  (default) and ROTATE_3D (while holding ctrl). An interactive marker
  can have multiple redundant control types; in this tutorial, the box
  is a 3D control yet the marker also has a simple set of 6-DOF
  rings-and-arrows.

It is possible to write an Rviz plugin that allows 3D grabbing of these
markers using a 6D input device such as a Phantom Omni or Razer Hydra.
See <http://www.ros.org/wiki/interaction_cursor_rviz>.

### 6-DOF (Arbitrary Axes)

![The structure of an \[\[https://docs.ros.org/en/rolling/p/visualization_msgs/msg/InteractiveMarker.html\|visualization_msgs/msg/InteractiveMarker\]\] message](doc/random_dof.png)

Shows that controls are not limited to the unit axes but can work on any
arbitrary orientation.

Source:
[basic_controls.cpp](https://github.com/ros-visualization/visualization_tutorials/blob/groovy-devel/interactive_marker_tutorials/src/basic_controls.cpp)



```cpp
void makeRandomDofMarker( const tf::Vector3& position )
{
  InteractiveMarker int_marker;
  int_marker.header.frame_id = "base_link";
  tf::pointTFToMsg(position, int_marker.pose.position);
  int_marker.scale = 1;

  int_marker.name = "6dof_random_axes";
  int_marker.description = "6-DOF\n(Arbitrary Axes)";

  makeBoxControl(int_marker);

  InteractiveMarkerControl control;

  for ( int i=0; i<3; i++ )
  {
    control.orientation.w = rand(-1,1);
    control.orientation.x = rand(-1,1);
    control.orientation.y = rand(-1,1);
    control.orientation.z = rand(-1,1);
    control.interaction_mode = InteractiveMarkerControl::ROTATE_AXIS;
    int_marker.controls.push_back(control);
    control.interaction_mode = InteractiveMarkerControl::MOVE_AXIS;
    int_marker.controls.push_back(control);
  }

  server->insert(int_marker);
  server->setCallback(int_marker.name, &processFeedback);
}
```



The controls in this example are created by assigning random values to
the quaternions which determine the orientation of each control. RViz
will normalize these quaternions, so you don't have to worry about it
when creating an interactive marker.

### View-Facing 6-DOF

![The structure of an \[\[https://docs.ros.org/en/rolling/p/visualization_msgs/msg/InteractiveMarker.html\|visualization_msgs/msg/InteractiveMarker\]\] message](doc/view_facing.png)

This interactive marker can move and rotate in all directions. In
contrast to the previous examples, it does that using only two controls.
The outer ring rotates along the view axis of the camera in RViz. The
box moves in the camera plane, although it is not visually aligned with
the camera coordinate frame.

Source:
[basic_controls.cpp](https://github.com/ros-visualization/visualization_tutorials/blob/groovy-devel/interactive_marker_tutorials/src/basic_controls.cpp)



```cpp
void makeViewFacingMarker( const tf::Vector3& position )
{
  InteractiveMarker int_marker;
  int_marker.header.frame_id = "base_link";
  tf::pointTFToMsg(position, int_marker.pose.position);
  int_marker.scale = 1;

  int_marker.name = "view_facing";
  int_marker.description = "View Facing 6-DOF";

  InteractiveMarkerControl control;

  // make a control that rotates around the view axis
  control.orientation_mode = InteractiveMarkerControl::VIEW_FACING;
  control.interaction_mode = InteractiveMarkerControl::ROTATE_AXIS;
  control.orientation.w = 1;
  control.name = "rotate";

  int_marker.controls.push_back(control);

  // create a box in the center which should not be view facing,
  // but move in the camera plane.
  control.orientation_mode = InteractiveMarkerControl::VIEW_FACING;
  control.interaction_mode = InteractiveMarkerControl::MOVE_PLANE;
  control.independent_marker_orientation = true;
  control.name = "move";

  control.markers.push_back( makeBox(int_marker) );
  control.always_visible = true;

  int_marker.controls.push_back(control);

  server->insert(int_marker);
  server->setCallback(int_marker.name, &processFeedback);
}
```



### Quadrocopter

![The structure of an \[\[https://docs.ros.org/en/rolling/p/visualization_msgs/msg/InteractiveMarker.html\|visualization_msgs/msg/InteractiveMarker\]\] message](doc/quadrocopter.png)

This interactive marker has a constrained set of 4 degrees of freedom.
It can rotate around the z axis and move in all 3 dimensions. It it
realized using two controls: the green ring moves in the y-z plane and
rotates around the z-axis, while the two additional arrows move along z.

Click and drag the green ring to see how the combined movement and
rotation works: If the mouse cursor stays close to the ring, it will
only rotate. Once you move it further away, it will start following the
mouse.

Source:
[basic_controls.cpp](https://github.com/ros-visualization/visualization_tutorials/blob/groovy-devel/interactive_marker_tutorials/src/basic_controls.cpp)



```cpp
void makeQuadrocopterMarker( const tf::Vector3& position )
{
  InteractiveMarker int_marker;
  int_marker.header.frame_id = "base_link";
  tf::pointTFToMsg(position, int_marker.pose.position);
  int_marker.scale = 1;

  int_marker.name = "quadrocopter";
  int_marker.description = "Quadrocopter";

  makeBoxControl(int_marker);

  InteractiveMarkerControl control;

  control.orientation.w = 1;
  control.orientation.x = 0;
  control.orientation.y = 1;
  control.orientation.z = 0;
  control.interaction_mode = InteractiveMarkerControl::MOVE_ROTATE;
  int_marker.controls.push_back(control);
  control.interaction_mode = InteractiveMarkerControl::MOVE_AXIS;
  int_marker.controls.push_back(control);

  server->insert(int_marker);
  server->setCallback(int_marker.name, &processFeedback);
}
```



The creation of the interactive marker is analogous to the previous
examples, just that the interaction mode for one of the controls is set
to MOVE_ROTATE.

### Chess Piece

![The structure of an \[\[https://docs.ros.org/en/rolling/p/visualization_msgs/msg/InteractiveMarker.html\|visualization_msgs/msg/InteractiveMarker\]\] message](doc/chess_piece.png)

Click and drag the box or the surrounding Ring to move it in the x-y
plane. Once you let go of the mouse button, it will snap to one of the
grid fields. The way this works is that the basic_controls server
running outside of RViz will set the pose of the Interactive Marker to a
new value when it receives the pose from RViz. RViz will apply the
update once you stop dragging it.

Source:
[basic_controls.cpp](https://github.com/ros-visualization/visualization_tutorials/blob/groovy-devel/interactive_marker_tutorials/src/basic_controls.cpp)



```cpp
void makeChessPieceMarker( const tf::Vector3& position )
{
  InteractiveMarker int_marker;
  int_marker.header.frame_id = "base_link";
  tf::pointTFToMsg(position, int_marker.pose.position);
  int_marker.scale = 1;

  int_marker.name = "chess_piece";
  int_marker.description = "Chess Piece\n(2D Move + Alignment)";

  InteractiveMarkerControl control;

  control.orientation.w = 1;
  control.orientation.x = 0;
  control.orientation.y = 1;
  control.orientation.z = 0;
  control.interaction_mode = InteractiveMarkerControl::MOVE_PLANE;
  int_marker.controls.push_back(control);

  // make a box which also moves in the plane
  control.markers.push_back( makeBox(int_marker) );
  control.always_visible = true;
  int_marker.controls.push_back(control);

  // we want to use our special callback function
  server->insert(int_marker);
  server->setCallback(int_marker.name, &processFeedback);

  // set different callback for POSE_UPDATE feedback
  server->setCallback(int_marker.name, &alignMarker, visualization_msgs::InteractiveMarkerFeedback::POSE_UPDATE );
}
```



The major difference to the previous example is that an additional
feedback function is specified, which will be called instead of
**`processFeedback()`** when the pose of the marker gets updated. This
function modifies the pose of the marker and sends it back to RViz:

Source:
[basic_controls.cpp](https://github.com/ros-visualization/visualization_tutorials/blob/groovy-devel/interactive_marker_tutorials/src/basic_controls.cpp)



```cpp
void alignMarker( const visualization_msgs::InteractiveMarkerFeedbackConstPtr &feedback )
{
  geometry_msgs::Pose pose = feedback->pose;

  pose.position.x = round(pose.position.x-0.5)+0.5;
  pose.position.y = round(pose.position.y-0.5)+0.5;

  ROS_INFO_STREAM( feedback->marker_name << ":"
      << " aligning position = "
      << feedback->pose.position.x
      << ", " << feedback->pose.position.y
      << ", " << feedback->pose.position.z
      << " to "
      << pose.position.x
      << ", " << pose.position.y
      << ", " << pose.position.z );

  server->setPose( feedback->marker_name, pose );
  server->applyChanges();
}
```



### Pan / Tilt

![The structure of an \[\[https://docs.ros.org/en/rolling/p/visualization_msgs/msg/InteractiveMarker.html\|visualization_msgs/msg/InteractiveMarker\]\] message](doc/pan_tilt.png)

This example shows that you can combine frame aligned and
fixed-orientation controls in one Interactive Marker. The Pan control
will always stay in place, while the tilt control will rotate.

Source:
[basic_controls.cpp](https://github.com/ros-visualization/visualization_tutorials/blob/groovy-devel/interactive_marker_tutorials/src/basic_controls.cpp)



```cpp
void makePanTiltMarker( const tf::Vector3& position )
{
  InteractiveMarker int_marker;
  int_marker.header.frame_id = "base_link";
  tf::pointTFToMsg(position, int_marker.pose.position);
  int_marker.scale = 1;

  int_marker.name = "pan_tilt";
  int_marker.description = "Pan / Tilt";

  makeBoxControl(int_marker);

  InteractiveMarkerControl control;

  control.orientation.w = 1;
  control.orientation.x = 0;
  control.orientation.y = 1;
  control.orientation.z = 0;
  control.interaction_mode = InteractiveMarkerControl::ROTATE_AXIS;
  control.orientation_mode = InteractiveMarkerControl::FIXED;
  int_marker.controls.push_back(control);

  control.orientation.w = 1;
  control.orientation.x = 0;
  control.orientation.y = 0;
  control.orientation.z = 1;
  control.interaction_mode = InteractiveMarkerControl::ROTATE_AXIS;
  control.orientation_mode = InteractiveMarkerControl::INHERIT;
  int_marker.controls.push_back(control);

  server->insert(int_marker);
  server->setCallback(int_marker.name, &processFeedback);
}
```



### Context Menu

This example shows how to attach a simple-static menu to an interactive
marker. If you do not specify a custom marker for visualization (as in
the case of the grey box), RViz will create a text marker floating above
the Interactive Marker, which will enables you to open the context menu.

Source:
[basic_controls.cpp](https://github.com/ros-visualization/visualization_tutorials/blob/groovy-devel/interactive_marker_tutorials/src/basic_controls.cpp)



```cpp
void makeMenuMarker( const tf::Vector3& position )
{
  InteractiveMarker int_marker;
  int_marker.header.frame_id = "base_link";
  tf::pointTFToMsg(position, int_marker.pose.position);
  int_marker.scale = 1;

  int_marker.name = "context_menu";
  int_marker.description = "Context Menu\n(Right Click)";

  InteractiveMarkerControl control;

  control.interaction_mode = InteractiveMarkerControl::MENU;
  control.name = "menu_only_control";

  Marker marker = makeBox( int_marker );
  control.markers.push_back( marker );
  control.always_visible = true;
  int_marker.controls.push_back(control);

  server->insert(int_marker);
  server->setCallback(int_marker.name, &processFeedback);
  menu_handler.apply( *server, int_marker.name );
}
```



### Button

Button controls behave almost exactly like the Menu control in the
previous example. You can use this type to indicate to the user that a
left-click is the desired mode of interaction. RViz will use a different
mouse cursor for this type of control (ROS Groovy and above).

Source:
[basic_controls.cpp](https://github.com/ros-visualization/visualization_tutorials/blob/groovy-devel/interactive_marker_tutorials/src/basic_controls.cpp)



```cpp
void makeButtonMarker( const tf::Vector3& position )
{
  InteractiveMarker int_marker;
  int_marker.header.frame_id = "base_link";
  tf::pointTFToMsg(position, int_marker.pose.position);
  int_marker.scale = 1;

  int_marker.name = "button";
  int_marker.description = "Button\n(Left Click)";

  InteractiveMarkerControl control;

  control.interaction_mode = InteractiveMarkerControl::BUTTON;
  control.name = "button_control";

  Marker marker = makeBox( int_marker );
  control.markers.push_back( marker );
  control.always_visible = true;
  int_marker.controls.push_back(control);

  server->insert(int_marker);
  server->setCallback(int_marker.name, &processFeedback);
}
```



### Marker attached to a moving frame

This example shows what happens if you click on a marker that is
attached to a frame which moves relative to the fixed frame specified in
RViz. Click on the box to move and on the ring to rotate. As the
containing frame moves, the marker will continue moving relative to your
mouse even if you are holding it. The interactive marker header's stamp
must be ros::Time(0) (as it is by default if not set), so that rviz will
take the most recent tf frames to transform it.

Source:
[basic_controls.cpp](https://github.com/ros-visualization/visualization_tutorials/blob/groovy-devel/interactive_marker_tutorials/src/basic_controls.cpp)



```cpp
void makeMovingMarker( const tf::Vector3& position )
{
  InteractiveMarker int_marker;
  int_marker.header.frame_id = "moving_frame";
  tf::pointTFToMsg(position, int_marker.pose.position);
  int_marker.scale = 1;

  int_marker.name = "moving";
  int_marker.description = "Marker Attached to a\nMoving Frame";

  InteractiveMarkerControl control;

  control.orientation.w = 1;
  control.orientation.x = 1;
  control.orientation.y = 0;
  control.orientation.z = 0;
  control.interaction_mode = InteractiveMarkerControl::ROTATE_AXIS;
  int_marker.controls.push_back(control);

  control.interaction_mode = InteractiveMarkerControl::MOVE_PLANE;
  control.always_visible = true;
  control.markers.push_back( makeBox(int_marker) );
  int_marker.controls.push_back(control);

  server->insert(int_marker);
  server->setCallback(int_marker.name, &processFeedback);
}
```



### The surrounding code

To setup the server node, all that is needed is to create an instance of
**`InteractiveMarkerServer`** and pass all `InteractiveMarker`
messages to that object.

Note that you have to call **`applyChanges()`** after you have added,
updated or removed interactive markers, their pose, menus or feedback
functions. This will cause the `InteractiveMarkerServer` to apply all
scheduled changes to its internal state and send an update message to
all connected clients. This is done to make it possible to maintain a
coherent state and minimize data traffic between the server and its
clients.

Source:
[basic_controls.cpp](https://github.com/ros-visualization/visualization_tutorials/blob/groovy-devel/interactive_marker_tutorials/src/basic_controls.cpp)



```cpp
boost::shared_ptr<interactive_markers::InteractiveMarkerServer> server;
interactive_markers::MenuHandler menu_handler;
```

 Source:
[basic_controls.cpp](https://github.com/ros-visualization/visualization_tutorials/blob/groovy-devel/interactive_marker_tutorials/src/basic_controls.cpp)



```cpp
int main(int argc, char** argv)
{
  ros::init(argc, argv, "basic_controls");
  ros::NodeHandle n;

  // create a timer to update the published transforms
  ros::Timer frame_timer = n.createTimer(ros::Duration(0.01), frameCallback);

  server.reset( new interactive_markers::InteractiveMarkerServer("basic_controls","",false) );

  ros::Duration(0.1).sleep();

  menu_handler.insert( "First Entry", &processFeedback );
  menu_handler.insert( "Second Entry", &processFeedback );
  interactive_markers::MenuHandler::EntryHandle sub_menu_handle = menu_handler.insert( "Submenu" );
  menu_handler.insert( sub_menu_handle, "First Entry", &processFeedback );
  menu_handler.insert( sub_menu_handle, "Second Entry", &processFeedback );

  tf::Vector3 position;
  position = tf::Vector3(-3, 3, 0);
  make6DofMarker( false, visualization_msgs::InteractiveMarkerControl::NONE, position, true );
  position = tf::Vector3( 0, 3, 0);
  make6DofMarker( true, visualization_msgs::InteractiveMarkerControl::NONE, position, true );
  position = tf::Vector3( 3, 3, 0);
  makeRandomDofMarker( position );
  position = tf::Vector3(-3, 0, 0);
  make6DofMarker( false, visualization_msgs::InteractiveMarkerControl::ROTATE_3D, position, false );
  position = tf::Vector3( 0, 0, 0);
  make6DofMarker( false, visualization_msgs::InteractiveMarkerControl::MOVE_ROTATE_3D, position, true );
  position = tf::Vector3( 3, 0, 0);
  make6DofMarker( false, visualization_msgs::InteractiveMarkerControl::MOVE_3D, position, false );
  position = tf::Vector3(-3,-3, 0);
  makeViewFacingMarker( position );
  position = tf::Vector3( 0,-3, 0);
  makeQuadrocopterMarker( position );
  position = tf::Vector3( 3,-3, 0);
  makeChessPieceMarker( position );
  position = tf::Vector3(-3,-6, 0);
  makePanTiltMarker( position );
  position = tf::Vector3( 0,-6, 0);
  makeMovingMarker( position );
  position = tf::Vector3( 3,-6, 0);
  makeMenuMarker( position );
  position = tf::Vector3( 0,-9, 0);
  makeButtonMarker( position );

  server->applyChanges();

  ros::spin();

  server.reset();
}
```



A timer is set up to update the [tf](https://index.ros.org/p/tf)
transformation between `base_link` and `moving_frame`, which is done
in **`frameCallback()`**:

Source:
[basic_controls.cpp](https://github.com/ros-visualization/visualization_tutorials/blob/groovy-devel/interactive_marker_tutorials/src/basic_controls.cpp)



```cpp
void frameCallback(const ros::TimerEvent&)
{
  static uint32_t counter = 0;

  static tf::TransformBroadcaster br;

  tf::Transform t;

  ros::Time time = ros::Time::now();

  t.setOrigin(tf::Vector3(0.0, 0.0, sin(float(counter)/140.0) * 2.0));
  t.setRotation(tf::Quaternion(0.0, 0.0, 0.0, 1.0));
  br.sendTransform(tf::StampedTransform(t, time, "base_link", "moving_frame"));

  t.setOrigin(tf::Vector3(0.0, 0.0, 0.0));
  t.setRotation(tf::createQuaternionFromRPY(0.0, float(counter)/140.0, 0.0));
  br.sendTransform(tf::StampedTransform(t, time, "base_link", "rotating_frame"));

  counter++;
}
```



Finally, `processFeedback()` is used to print output to rosconsole
when feedback arrives:

Source:
[basic_controls.cpp](https://github.com/ros-visualization/visualization_tutorials/blob/groovy-devel/interactive_marker_tutorials/src/basic_controls.cpp)



```cpp
void processFeedback( const visualization_msgs::InteractiveMarkerFeedbackConstPtr &feedback )
{
  std::ostringstream s;
  s << "Feedback from marker '" << feedback->marker_name << "' "
      << " / control '" << feedback->control_name << "'";

  std::ostringstream mouse_point_ss;
  if( feedback->mouse_point_valid )
  {
    mouse_point_ss << " at " << feedback->mouse_point.x
                   << ", " << feedback->mouse_point.y
                   << ", " << feedback->mouse_point.z
                   << " in frame " << feedback->header.frame_id;
  }

  switch ( feedback->event_type )
  {
    case visualization_msgs::InteractiveMarkerFeedback::BUTTON_CLICK:
      ROS_INFO_STREAM( s.str() << ": button click" << mouse_point_ss.str() << "." );
      break;

    case visualization_msgs::InteractiveMarkerFeedback::MENU_SELECT:
      ROS_INFO_STREAM( s.str() << ": menu item " << feedback->menu_entry_id << " clicked" << mouse_point_ss.str() << "." );
      break;

    case visualization_msgs::InteractiveMarkerFeedback::POSE_UPDATE:
      ROS_INFO_STREAM( s.str() << ": pose changed"
          << "\nposition = "
          << feedback->pose.position.x
          << ", " << feedback->pose.position.y
          << ", " << feedback->pose.position.z
          << "\norientation = "
          << feedback->pose.orientation.w
          << ", " << feedback->pose.orientation.x
          << ", " << feedback->pose.orientation.y
          << ", " << feedback->pose.orientation.z
          << "\nframe: " << feedback->header.frame_id
          << " time: " << feedback->header.stamp.sec << "sec, "
          << feedback->header.stamp.nsec << " nsec" );
      break;

    case visualization_msgs::InteractiveMarkerFeedback::MOUSE_DOWN:
      ROS_INFO_STREAM( s.str() << ": mouse down" << mouse_point_ss.str() << "." );
      break;

    case visualization_msgs::InteractiveMarkerFeedback::MOUSE_UP:
      ROS_INFO_STREAM( s.str() << ": mouse up" << mouse_point_ss.str() << "." );
      break;
  }

  server->applyChanges();
}
```

## Plugins: New Display Type

```wiki
This tutorial can be found here: http://docs.ros.org/noetic/api/rviz_plugin_tutorials/html/display_plugin_tutorial.html
```

## Plugins: New Dockable Panel

```wiki
This tutorial has not been ported to Noetic.
```

## Plugins: New Tool Type

## Librviz: Incorporating RViz into a Custom GUI

## Rviz in Stereo

### Intro

3D stereo rendering displays a different view to each eye so that the
scene appears to have depth. If you have a stereo capable monitor and
stereo capable graphics card you can get Rviz to render its view in
stereo. This tutorial describes how to accomplish this.

### Hardware Requirements

To render in stereo you will need a graphics card capable of Quad-buffer
stereo. You may also need a stereo-capable monitor and/or a monitor that
can display at 120Hz.

#### Using NVIDIA hardware

On Linux NVIDIA Quadro cards support quad buffered stereo. There is
information about which cards support this feature
[here on the NVIDIA website](http://www.nvidia.com/object/quadro_pro_graphics_boards_linux.html).

Also see <http://www.zib.de/durmaz/3dVision.html> or try a web search
for other info on "quad buffer stereo linux".

There seem to be 2 options for displays:

##### Special 3D Monitor

Get a special monitor that comes with 3DVision glasses and has a built
in 3DVision IR transmitter. I have stereo working on an ASUS VG278H
monitor with an NVIDIA Quadro K4000 graphics adaptor. You will need to
connect the display directly to the graphics card with a DVI Dual-link
cable. (Single link DVI will not work. Display-port to DVI will not
work. HDMI will not work at 120Hz.) The monitor comes with active
3DVision glasses and has a built in IR transmitter, so you do not need a
separate IR transmitter and you do not need a "3 pin mini-din"
connector on your graphics card.

##### 3DVision glasses

Get 3DVision kit with active glasses and an IR transmitter (or
3DVision-Pro glasses with a radio transmitter). You will also need a
monitor with a refresh rate of at least 100Hz (120Hz is better).

On Linux you need to connect the IR (or radio) transmitter directly to
the graphics card. Transmitters that plug into USB do not work on Linux
(they may work on Mac but I have not tried). To connect directly to the
graphics card use the '3-pin mini-din to 1/8" stereo cable' that
comes with the 3DVision kit.

**Many NVIDIA cards that support stereo DO NOT come with a '3-pin
mini-din' connector on them.** If you do not see a round 3-pin
'mini-din' connector on the back of your graphics card (next to the
DVI/VGA/etc connectors) then you need to buy a separate "NVIDIA Quadro
Stereo Board Connector". PNY sells one: Search for part number
"QSP-STRBOARD-PB" **This will only work with Quadro cards that support
quad buffer stereo.** Check
[the NVIDIA website](http://www.nvidia.com/object/quadro_pro_graphics_boards_linux.html)
for your card to be sure your card will work before buying the board
connector.

On linux you can tell what kind of graphics card you have by running


```
lspci | grep VGA
```

 If it does not say "Quadro" then it probably
does not support stereo.

You will need to connect the display directly to the graphics card with
a DVI Dual-link cable. (Single link DVI will not work. Display-port to
DVI will not work. HDMI works at 60Hz which is too slow and you will
quickly get a headache.)

#### Using AMD hardware

I believe some high end AMD graphics cards support quad-buffer stereo,
but I do not know which ones. If you have information on this please add
it here.

### Setting up X (in Linux) to support stereo

#### NVIDIA

##### Install binary drivers

Be sure you are using the NVIDIA binary drivers. Run


```
sudo apt-get install nvidia-settings
  nvidia-settings
```

 If you are using the NVIDIA binary drivers this
will work \-- go on to the next step. If not the program will inform you
that you are not using the NVIDIA binary drivers.

Search the web for
[Install NVIDIA drivers](http://lmgtfy.com/?q=install+nvidia+linux+drivers)

##### Set resolution, refresh rate, and stereo mode

Run 

```
nvidia-settings
```

 Click on "X Server Display
Configuration". If you have multiple monitors choose the one you want
to setup for stereo. Select the Resolution (do not choose "Auto").
Select the refresh rate (to the right of "Resolution"). You want a
refresh rate at least 100Hz (120Hz or faster is better). Click
"Apply".

Assuming everything works you need to save these settings. Click the
button "Save to X Configuration File" and follow the prompts to save
the file as /tmp/xorg.conf

Now you have to add the stereo setting. Open a terminal and run these
commands: 

```
cd /tmp
  nvidia-xconfig -c xorg.conf -o xorg.conf --stereo=10
```

 Note: "10" means "NVIDIA 3D
VISION". If you have "NVIDIA 3D VISION PRO" use 11. For other
settings run **man nvidia-xconfig** and search for stereo.


```
sudo cp /etc/X11/xorg.conf /etc/X11/xorg.conf.original-no-stereo
  cp xorg.conf /etc/X11/xorg.conf
```

 Now restart X by logging out and logging back
in.

To verify that stereo is enabled run 

```
nvidia-settings
```



Click on "X Screen 0" and look at the "Stereo Mode" setting. It
should say "NVIDIA 3D Vision Stereo"

### Known-working Stereo Hardware

Please add to this section if you have stereo working on your system.

- WORKS: NVIDIA Quadro K4000, ASUS VG278H monitor (comes with 3DVision
  glasses), DVI dual-link cable. IR transmitter is built into the
  monitor.

### Testing stereo hardware

To verify that your stereo hardware is working run


```
sudo apt-get install mesa-utils
   glxgears -stereo
```



If you have multiple monitors, drag the gears window to the monitor with
stereo support. You should see a double image. Put on your 3D Glasses.
You should see the image in stereo. To see it better resize the window
(make it bigger) and use the arrow keys to rotate the gears around. If
it looks funny try running 

```
nvidia-settings
```

 click on "OpenGL
Settings" and check the "Exchange Stereo Eyes" button.

#### troubleshooting

I have found that once the computer goes to sleep or if the monitor is
turned off that the monitor stops transmitting the stereo signal to the
glasses after the computer wakes up and the monitor is turned on. If you
cannot get stereo to work try this: Shut down the computer. Leave the
monitor turned on. Power on the computer. Now it should work (at least
until the computer goes to sleep again).

### Building Rviz to render in stereo

Ogre (the graphics library that Rviz uses) does not currently support
stereo rendering by default. To enable stereo rendering you will have to
build Rviz and a custom version of Ogre from source.

Do not bother with this until you have confirmed that your graphics card
and monitor work in stereo (see
[Testing stereo hardware](http://wiki.ros.org/rviz/Tutorials/Rviz%20in%20Stereo#Testing_stereo_hardware)).
Rviz will not render in stereo if **glxgears -stereo** does not render
in stereo.

#### Building Ogre for Stereo

Get the sources, build and install. Rviz only works with versions of
Ogre older than 1.8, so checkout that tag.



```
cd $HOME
    mkdir my-ogre
    cd my-ogre
    hg clone https://bitbucket.org/sinbad/ogre
    cd ogre
    hg pull && hg update v1-8
    cd ..
    mkdir build
    cd build
    cmake -DOGRE_FULL_RPATH=ON -DOGRE_CONFIG_ENABLE_QUAD_BUFFER_STEREO=ON -DCMAKE_INSTALL_PREFIX:PATH="/usr/local" -DFREETYPE_INCLUDE_DIR:PATH="/usr/include/freetype2" -DFREETYPE_FT2BUILD_INCLUDE_DIR:PATH="/usr/include/freetype2" ../ogre
    sudo make install
```

 Notes:

- This installs Ogre into /usr/local, which is why you need sudo. You
  may change the install directory if you wish.
- You may also customize the cmake flags using
  [cmake-gui](https://cmake.org/cmake/help/v3.0/manual/cmake-gui.1.html).
  The most crucial thing is to enable
  OGRE_CONFIG_ENABLE_QUAD_BUFFER_STEREO.

#### Building Rviz for Stereo

First create a workspace to build Rviz. (If you already have a workspace
you can use the existing one instead of creating a new
"my-rviz-workspace" workspace.) 

```
cd $HOME
    mkdir -p my-rviz-workspace/src
    cd my-rviz-workspace/src
    git clone https://github.com/ros-visualization/rviz.git
    cd ..
    PKG_CONFIG_PATH=/usr/local/lib/pkgconfig:${PKG_CONFIG_PATH} catkin_make --cmake-args -DCMAKE_SHARED_LINKER_FLAGS:STRING=" -Wl,-rpath,/usr/local/lib" -DCMAKE_CXX_FLAGS:STRING="-DOGRE_STEREO_ENABLE=1" -DUseQt5:BOOL="0"
```



Run your new rviz compiled binary manually: 

```
roscore & ./devel/lib/rviz/rviz
```



If your hardware doesn't support quad buffer stereo rviz might segfault
at this point.

Add a display (e.g. an Axis Display) so there is something to look at.

If your HW supports stereo you should see a double image. Put on the
glasses to see it in stereo.

### Adjusting stereo properties in Rviz

Properties in the "View Controller" panel can be used to set
eye-separation, focal-distance, to swap the eyes, and disable stereo.

If you do not see the "Views" panel (by default in upper right) then
click the "Panels" menu item and check "Views".

In the "Current View" you will see some properties that can be used to
adjust the stereo rendering:

- **Enable Stereo Rendering**: uncheck this to turn off stereo.
- **Swap Stereo Eyes**: check this if Rviz has gotten confused and has
  swapped the left and right eyes.
- **Stereo Eye Separation**: Use larger values for greater stereo
  effect. Ideally this is the distance between your eyes (in meters).
- **Stereo Focal Distance**: Set this to the distance between your eyes
  and the monitor. Smaller values tend to produce a greater stereo
  effect.

## Tutorials

### Text-based Tutorials

- [Markers: Sending Basic Shapes (C++)](#markers-sending-basic-shapes-c):
  Shows how to use
  [visualization_msgs/msg/Marker](https://docs.ros.org/en/rolling/p/visualization_msgs/msg/Marker.html)
  messages to send basic shapes (cube, sphere, cylinder, arrow) to rviz.
- [Markers: Points and Lines (C++)](#markers-points-and-lines-c):
  Teaches how to use the
  [visualization_msgs/msg/Marker](https://docs.ros.org/en/rolling/p/visualization_msgs/msg/Marker.html)
  message to send points and lines to rviz.
- [Interactive Markers: Getting Started](#interactive-markers-getting-started):
  This tutorial explains what Interactive Marker are and teaches you
  some of the basic concepts.
- [Interactive Markers: Writing a Simple Interactive Marker Server](#interactive-markers-writing-a-simple-interactive-marker-server):
  This tutorial explains how to setup a minimalist server which manages
  a single interactive marker.
- [Interactive Markers: Basic Controls](#interactive-markers-basic-controls):
  This tutorial explains how the basic_controls tutorial code works.
- [Plugins: New Display Type](#plugins-new-display-type):
  How to write a plugin which adds a new display capability to RViz.
- [Plugins: New Dockable Panel](#plugins-new-dockable-panel):
  How to write a plugin which adds a new type of dock-able Panel widget
  to RViz.
- [Plugins: New Tool Type](#plugins-new-tool-type):
  How to write a plugin which adds a new tool to RViz.
- [Librviz: Incorporating RViz into a Custom GUI](#librviz-incorporating-rviz-into-a-custom-gui):
  How to write an application using an RViz visualization widget.
- [Rviz in Stereo](#rviz-in-stereo):
  Teaches how to set up Rviz to render in 3D Stereo.

### Video Tutorials

[Youtube](https://www.youtube.com/watch?v=gMyC_zt79j8)
[Youtube](https://www.youtube.com/watch?v=JHTdISEbxY4)
[Youtube](https://www.youtube.com/watch?v=n2jeqq3j69g)
[Youtube](https://www.youtube.com/watch?v=DT1BlGL6wB8)

## DisplayTypes/Axes

![Axes](doc/Axes.png)

The **Axes** display shows a set of axes, located at the origin of the
target frame.

[Youtube](https://www.youtube.com/watch?v=xLgA5eF54H0)

red - x green - y blue -z

  -- ---------- -- ------------------------------------ -- ------------------ -- ------------- --
                   **Properties**                                                              
     **Name**      **Description**                         **Valid Values**      **Default**   
     Length        The length of each axis, in meters      0.0001+               1             
     Radius        The radius of each axis, in meters      0.0001+               0.1           
  -- ---------- -- ------------------------------------ -- ------------------ -- ------------- --

## DisplayTypes/Effort

![Pose](doc/Effort.png)

The **Effort** display shows a
[sensor_msgs/msg/JointState](https://docs.ros.org/en/rolling/p/sensor_msgs/msg/JointState.html)/effort
message as circled arrows around each revolute joint in the robot.

  -- ------------------- -- -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- -- ---------------------------------------------- -- ------------------- --
                            **Properties**                                                                                                                                                                                                                                                              
     **Name**               **Description**                                                                                                                                                                                       **Valid Values**                                  **Default**         
     Topic                  The topic to subscribe to                                                                                                                                                                             Any valid [Graph Resource Name](Names#Graph)      Empty String        
     Alpha                  How opaque to draw the arrows.                                                                                                                                                                        \[0-1\]                                           1                   
     Width                  The width of the arrow, in meters                                                                                                                                                                     0.0001+                                           1                   
     Robot Description      The [parameter](Parameter Server) to retrieve the [urdf](https://index.ros.org/p/urdf) from. Uses `searchParam()` to search up the [parameter](Parameter Server) tree for the value specified.      Any valid [Graph Resource Name](Names#Graph)      robot_description   
  -- ------------------- -- -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- -- ---------------------------------------------- -- ------------------- --

## DisplayTypes/Camera

![Camera](doc/Camera.png)

The **Camera** display creates a new rendering window from the
perspective of a camera, and overlays the image from the camera on top
of it. For this display to work properly the
[sensor_msgs/msg/Image](https://docs.ros.org/en/rolling/p/sensor_msgs/msg/Image.html)
topic subscribed to must be part of a camera, and must have a
[sensor_msgs/msg/CameraInfo](https://docs.ros.org/en/rolling/p/sensor_msgs/msg/CameraInfo.html)
topic named `camera_info` alongside it. For example:



```
/wide_stereo/left/image_rect
/wide_stereo/left/camera_info
```

 The **Camera** display assumes a z-forward
x-right frame, rather than the normal x-forward y-left robot frame.

[Youtube](https://www.youtube.com/watch?v=0paK3dnKamY)

  -- ------------- -- ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- -- ---------------------------------------------- -- -------------- --
                      <style="text-align:center">**Properties**                                                                                                                                                                                                                                                                                                                      
     **Name**         **Description**                                                                                                                                                                                                                                                                                   **Valid Values**                                  **Default**    
     Alpha            The amount of transparency to apply to the image overlay                                                                                                                                                                                                                                          \[0-1\]                                           1              
     Image Topic      The [sensor_msgs/msg/Image](https://docs.ros.org/en/rolling/p/sensor_msgs/msg/Image.html) topic to subscribe to. The display will automatically generate the [sensor_msgs/msg/CameraInfo](https://docs.ros.org/en/rolling/p/sensor_msgs/msg/CameraInfo.html) topic based on the image topic.      Any valid [Graph Resource Name](Names#Graph)      Empty String   
  -- ------------- -- ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- -- ---------------------------------------------- -- -------------- --

### Supported Image Encodings

rviz currently supports RGB8, RGBA8, BGR8, BGRA8, MONO8, MONO16, bayer
encoded (treated as MONO8), 8UC4 and 8SC4 (treated as BGRA8), 8UC3 and
8SC3 (treated as BGR8), 8UC1 and 8SC1 (treated as MONO8), 16UC1 and
16SC1 (treated as MONO16).

## DisplayTypes/Grid

![Grid](doc/Grid.png)

The **Grid** display shows a grid of lines, centered at the origin of
the target frame.

[Youtube](https://www.youtube.com/watch?v=ZPPnE9n_Srs)

  -- ------------------- -- ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- -- ----------------------------------- -- ----------------- --
                            **Properties**                                                                                                                                                                                                                                                                                 
     **Name**               **Description**                                                                                                                                                                                                                       **Valid Values**                       **Default**       
     Plane Cell Count       The number of cells to draw in the plane of the grid                                                                                                                                                                                  1+                                     10                
     Normal Cell Count      The number of cells to draw along the normal of the grid. Setting this to anything but 0 makes the grid 3D                                                                                                                            0+                                     0                 
     Cell Size              The length, in meters, of the side of each cell                                                                                                                                                                                       0.0001+                                1                 
     Line Style             The rendering operation to use to draw the lines. *Lines* are the same width no matter how far away they are. *Billboards* have real-world width, so they get larger/smaller depending on how far away they are from the camera.      Lines, Billboards                      Lines             
     Line Width             The width of the lines, in meters. Only applicable if **Line Style** is set to *Billboards*                                                                                                                                           0.0001+                                0.03              
     Color                  The color of the lines                                                                                                                                                                                                                (\[0-255\], \[0-255\], \[0-255\])      (127, 127, 127)   
     Alpha                  The amount of transparency to apply to the lines                                                                                                                                                                                      \[0-1\]                                0.5               
     Plane                  The plane to draw the grid along                                                                                                                                                                                                      XY, XZ, YZ                             XY                
  -- ------------------- -- ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- -- ----------------------------------- -- ----------------- --

## DisplayTypes/GridCells

![GridCells](doc/GridCells.png)

The **!GridCells** display shows a
*[nav_msgs](https://index.ros.org/p/nav_msgs)::!GridCells* message, as
upwards-facing billboards.

[Youtube](https://www.youtube.com/watch?v=4HHCBtUHKfQ)

  -- ---------- -- -------------------------------------------------- -- ---------------------------------------- -- -------------- --
                   **Properties**                                                                                                   
     **Name**      **Description**                                       **Valid Values**                            **Default**    
     Color         The color of the cells                                (\[0-255\], \[0-255\], \[0-255\])           (25, 255, 0)   
     Alpha         The amount of transparency to apply to the cells      \[0-1\]                                     1              
     Topic         The topic to subscribe to                             Any valid [Graph Resource Name](Names)      Empty String   
  -- ---------- -- -------------------------------------------------- -- ---------------------------------------- -- -------------- --

## DisplayTypes/Image

The **Image** display creates a new rendering window with an image.

  -- ------------- -- ------------------------------------------------------------------------------------------------------------------ -- ---------------------------------------------- -- -------------- --
                      **Properties**                                                                                                                                                                         
     **Name**         **Description**                                                                                                       **Valid Values**                                  **Default**    
     Alpha            The amount of transparency to apply to the image overlay                                                              \[0-1\]                                           1              
     Image Topic      The [sensor_msgs/msg/Image](https://docs.ros.org/en/rolling/p/sensor_msgs/msg/Image.html) topic to subscribe to.      Any valid [Graph Resource Name](Names#Graph)      Empty String   
  -- ------------- -- ------------------------------------------------------------------------------------------------------------------ -- ---------------------------------------------- -- -------------- --

### Supported Image Encodings

rviz currently supports RGB8, RGBA8, BGR8, BGRA8, MONO8, MONO16, bayer
encoded (treated as MONO8), 8UC4 and 8SC4 (treated as BGRA8), 8UC3 and
8SC3 (treated as BGR8), 8UC1 and 8SC1 (treated as MONO8), 16UC1 and
16SC1 (treated as MONO16).

## DisplayTypes/InteractiveMarker

The **Interactive Markers** display acts as a client to one or multiple
**Interactive Marker Servers**, providing the functionality for the user
to interact with 3D objects received over ROS topics in the main view of
rviz. It uses the same set of visual primitives as the
[Marker](#displaytypesmarker) display.

The
[tutorials](#interactive-markers-getting-started)
will show you what interactive markers do and how they can be used.

![The basic_controls tutorial showing in RViz](doc/rviz_DisplayTypes_InteractiveMarker_basic_controls.png)

## DisplayTypes/LaserScan

![LaserScan](doc/LaserScan.png)

The **Laser Scan** display shows data from a
[sensor_msgs/msg/LaserScan](https://docs.ros.org/en/rolling/p/sensor_msgs/msg/LaserScan.html)
message.

[Youtube](https://www.youtube.com/watch?v=HoWaMyeowRg)

  -- ------------------------------ -- -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- -- -------------------------------------------------- -- -------------------------------------------------------------- --
                                       **Properties**                                                                                                                                                                                                                                                                                                                                                                         
     **Name**                          **Description**                                                                                                                                                                                                                                                   **Valid Values**                                      **Default**                                                    
     Selectable                        Whether or not this cloud is selectable using the selection tool.                                                                                                                                                                                                 True, False                                           True                                                           
     Style                             The rendering style to use when drawing the points, listed in order of computational expense. There are currently 4 rendering styles, [which are explained in the Rendering Styles section](#renderingstyles)          Points, Billboards, Billboard Spheres, Boxes          Billboards                                                     
     Channel                           Which channel(s) to use to color the points. This dropdown is dynamically populated based on the channels in the last cloud received. The individual channels are [explained in the Channels section](#channels).      Intensity, Color (RGB), Normal Sphere, Curvature      First option which has a corresponding channel in the cloud.   
     Alpha                             The amount of transparency to apply to the points. Note that this does not work perfectly, and you may see some rendering strangeness if this is set to anything but 1                                                                                            \[0-1\]                                               1                                                              
     Min Color                         For intensity channels, the color to assign to the minimum value. [See the Intensity Channel section for more information.](#intensitychannel)                                                                         (\[0-255\], \[0-255\], \[0-255\])                     (0, 0, 0)                                                      
     Min Color                         For intensity channels, the color to assign to the maximum value. [See the Intensity Channel section for more information.](#intensitychannel)                                                                         (\[0-255\], \[0-255\], \[0-255\])                     (255, 255, 255)                                                
     Billboard Size                    The size, in meters, to display the billboards (or boxes). This setting does not affect the *Points* rendering style                                                                                                                                              0.0001+                                               0.01                                                           
     Autocompute Intensity Bounds      Whether or not to auto-compute the "Min Intensity" and "Max Intensity" properties                                                                                                                                                                             True, False                                           True                                                           
     Min Intensity                     The minimum value to use for intensity channel coloring. [See the Intensity Channel section for more information.](#intensitychannel)                                                                                  \[-inf, < Max Intensity\]\]                          0                                                              
     Max Intensity                     The maximum value to use for intensity channel coloring. [See the Intensity Channel section for more information.](#intensitychannel)                                                                                  \[> Min Intensity, inf\]\]                           4096                                                           
     Decay Time                        The amount of time to keep a cloud/scan around before removing it. A value of 0 means to only display the most recent data.                                                                                                                                       0+                                                    0                                                              
     Topic                             The topic to subscribe to                                                                                                                                                                                                                                         Any valid [Graph Resource Name](Names#Graph)          Empty String                                                   
  -- ------------------------------ -- -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- -- -------------------------------------------------- -- -------------------------------------------------------------- --

<a id="renderingstyles"></a>

### Rendering Styles

  -- ------------------- -- ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------- -- ------------------------------------------------ --
     Points                 Points are a fixed size on-screen, currently 3 pixels by 3 pixels. This means you can often see more definition from far away, but as you get closer the density decreases.      ![Points](doc/Points.png)                        
     Billboards             Billboards are camera-facing quads, that have real-world size.                                                                                                                   ![Billboards](doc/Billboards.png)                
     Billboard Spheres      Similar to *Billboards*, but rendered such that they look like spheres, and provide some contrast so you can tell individual points apart if they are overlapping.               ![Billboard Spheres](doc/BillboardSpheres.png)   
     Boxes                  Cubes in the world.                                                                                                                                                              ![Boxes](doc/Boxes.png)                          
  -- ------------------- -- ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------- -- ------------------------------------------------ --

<a id="channels"></a>

### Channels

`PointCloud`s can have any number of channels associated with them. If
you're using a `LaserScan` display, the only available channel will
be the "Intensity" channel.

This section explains how the color/position of a point is computed for
each channel type.

<a id="intensitychannel"></a>

#### Intensity

Valid channel names: `intensity`, `intensities`

Intensity only affects the color of the point.

The intensity channel uses 4 values to compute the final color of the
point:

  -- --------------- -- ------- --
     Min Intensity      min_i   
     Max Intensity      max_i   
     Min Color          min_c   
     Max Color          max_c   
  -- --------------- -- ------- --

For each point:

- To compute the color value, we first compute a normalized intensity
  value based on `min_i` and `max_i`: 

```
norm_i = (i - min_i) / (max_i - min_i)
```


- Then to compute the color from that normalized intensity:
  

```
final_c = (norm_i * max_c) + ((1 - norm_i) * min_c)
```



#### RGB

Valid channel names: `rgb` (1 channel), `r`, `g`, `b` (3
channel)

RGB only affects the color of the point.

There are two ways to specify RGB: 1. 3 channels, named "r", "g",
and "b", with floating point values between 0 and 1. 1. 1 channel,
with the float in the channel reinterpreted as 3 single-byte values with
ranges from 0 to 255. `0xff0000` is red, `0xff00` is green, `0xff`
is blue.

- In C++,
  `int rgb = 0xff0000; float float_rgb = *reinterpret_cast<float*>(&rgb); `
- In Python,
  ` float_rgb = struct.unpack('f', struct.pack('i', 0xff0000))[0]`

#### Normal Sphere

Valid channel names: `nx`, `ny`, `nz` (all 3 required)

Normal Sphere only affects the position of the point.

For this channel, the "nx", "ny" and "nz" channels will be used to
position the points instead of the values in the points array.

#### Curvature

Valid channel names: `curvature`, `curvatures`

Curvature colors in the same way
[intensity](#intensitychannel)
does.

## DisplayTypes/Map

![X](doc/Map.png)

The **Map** display shows a
[nav_msgs/msg/OccupancyGrid](https://docs.ros.org/en/rolling/p/nav_msgs/msg/OccupancyGrid.html)
message. The occupancy grid is treated the way the
[navigation](https://index.ros.org/p/navigation) stack treats it. A
value of 100 is black (occupied), a value of 0 is white (unoccupied),
and anything else is gray (unknown).

[Youtube](https://www.youtube.com/watch?v=BvvYUYD11qA)

  -- ------------------- -- ---------------------------------------------------------------------------------------------- -- ---------------------------------------------- -- -------------- --
                            **Properties**                                                                                                                                                     
     **Name**               **Description**                                                                                   **Valid Values**                                  **Default**    
     Topic                  The topic to subscribe to                                                                         Any valid [Graph Resource Name](Names#Graph)      Empty String   
     Alpha                  The amount of transparency to apply to the map                                                    \[0-1\]                                           1              
     Request Frequency      How often to re-request the map, in seconds. A value of 0 means to never re-request the map.      0+                                                0              
  -- ------------------- -- ---------------------------------------------------------------------------------------------- -- ---------------------------------------------- -- -------------- --

## DisplayTypes/Marker

![Markers](doc/Markers.png)

The **Markers** display allows programmatic addition of various
primitive shapes to the 3D view by sending a
[visualization_msgs/msg/Marker](https://docs.ros.org/en/rolling/p/visualization_msgs/msg/Marker.html)
or
[visualization_msgs/msg/MarkerArray](https://docs.ros.org/en/rolling/p/visualization_msgs/msg/MarkerArray.html)
message.

The
[Markers: Basic Shapes](#markers-sending-basic-shapes-c)
tutorial begins a series of tutorials on sending markers.

[Youtube](https://www.youtube.com/watch?v=PqECn68KGFU)

  -- ---------- -- ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ -- ---------------------------------------------- -- ---------------------- --
                   <style="text-align:center">**Properties**                                                                                                                                                                                                                                                              
     **Name**      **Description**                                                                                                                                                                                                                   **Valid Values**                                  **Default**            
     Topic         The topic to subscribe to. Will automatically also subscribe to `<topic>_array`, assuming it is a [visualization_msgs/msg/MarkerArray](https://docs.ros.org/en/rolling/p/visualization_msgs/msg/MarkerArray.html) topic      Any valid [Graph Resource Name](Names#Graph)      visualization_marker   
  -- ---------- -- ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ -- ---------------------------------------------- -- ---------------------- --

### The Marker Message

#### Example Usage (C++/roscpp)

First, advertise on the `visualization_marker` topic:



```cplusplus
ros::Publisher vis_pub = node_handle.advertise<visualization_msgs::Marker>( "visualization_marker", 0 );
```

 After that it's as simple as filling out a
[visualization_msgs/msg/Marker](https://docs.ros.org/en/rolling/p/visualization_msgs/msg/Marker.html)
message and publishing it:



```cplusplus
visualization_msgs::Marker marker;
marker.header.frame_id = "base_link";
marker.header.stamp = ros::Time();
marker.ns = "my_namespace";
marker.id = 0;
marker.type = visualization_msgs::Marker::SPHERE;
marker.action = visualization_msgs::Marker::ADD;
marker.pose.position.x = 1;
marker.pose.position.y = 1;
marker.pose.position.z = 1;
marker.pose.orientation.x = 0.0;
marker.pose.orientation.y = 0.0;
marker.pose.orientation.z = 0.0;
marker.pose.orientation.w = 1.0;
marker.scale.x = 1;
marker.scale.y = 0.1;
marker.scale.z = 0.1;
marker.color.a = 1.0; // Don't forget to set the alpha!
marker.color.r = 0.0;
marker.color.g = 1.0;
marker.color.b = 0.0;
//only if using a MESH_RESOURCE marker type:
marker.mesh_resource = "package://pr2_description/meshes/base_v0/base.dae";
vis_pub.publish( marker );
```

 There is also a
[visualization_msgs/msg/MarkerArray](https://docs.ros.org/en/rolling/p/visualization_msgs/msg/MarkerArray.html)
message, which lets you publish many markers at once. In this case you
want to publish in the `visualization_marker_array` topic.

Note that the timestamp attached to the marker message above is
ros::Time(), which is time Zero (0). This is treated differently by RViz
than any other time. If you use ros::Time::now() or any other non-zero
value, rviz will only display the marker if that time is close enough to
the current time, where "close enough" depends on TF. With time 0
however, the marker will be displayed regardless of the current time.

**Don't forget to set `color.a = 1` or your marker will be
invisible!**

#### Message Parameters

`ns`

. Namespace for these markers. This plus the id form a unique
identifier.

`id`

. Unique id assigned to this marker. It is your responsibility to keep
these unique within your namespace.

`type`

. Type of marker (Arrow, Sphere, \...). The
[available types](#object-types)
are specified in the message definition.

`action`

. 0 = add/modify, 1 = (deprecated), 2 = delete, 3 = deleteall

`pose`

. Pose marker, specified as x/y/z position and x/y/z/w quaternion
orientation.

`scale`

. Scale of the marker. Applied before the position/orientation. A scale
of \[1,1,1\] means the object will be 1m by 1m by 1m.

`color`

. Color of the object, specified as r/g/b/a, with values in the range of
\[0, 1\]. Don't forget to set a or it will default to 0 and be
invisible.

`points`

. Only used for markers of type Points, Line strips, and
Line/Cube/Sphere lists. It's also used for the Arrow type, if you want
to specify the arrow start and end points.

`colors` \[1.1+\]

. Only used for markers that use the `points` member, specifies
per-vertex color (no alpha yet).

`lifetime`

. A duration value used to automatically delete the marker after this
period of time. The countdown resets if another marker of the same
namespace/id is received.

`frame_locked` \[1.1+\]

. Tells rviz to retransform the marker into the current location of the
specified frame every update cycle.

`text` \[1.1+\]

. The text string used for the `TEXT_VIEW_FACING` marker type

`mesh_resource` \[1.1+\]

. The resource location for the `MESH_RESOURCE` marker type. Can be
any mesh type supported by rviz (.stl or Ogre .mesh in 1.0, with the
addition of COLLADA in 1.1). The format is the URI-form used by
[resource_retriever](https://index.ros.org/p/resource_retriever),
including the `package:*` syntax.*

#### Object Types

##### Arrow (ARROW=0)

![Arrow](doc/ArrowMarker.png)

The arrow type provides two different ways of specifying where the arrow
should begin/end:

*Position/Orientation*

. Pivot point is around the tip of its tail. Identity orientation points
it along the +X axis. `scale.x` is the arrow length, `scale.y` is
the arrow width and `scale.z` is the arrow height.

*Start/End Points*

. You can also specify a start/end point for the arrow, using the
`points` member. If you put points into the `points` member, it will
assume you want to do things this way.

- The point at index 0 is assumed to be the start point, and the point
  at index 1 is assumed to be the end.
- `scale.x` is the shaft diameter, and `scale.y` is the head
  diameter. If `scale.z` is not zero, it specifies the head length.

##### Cube (CUBE=1)

![Cube](doc/CubeMarker.png)

Pivot point is at the center of the cube.

##### Sphere (SPHERE=2)

![Sphere](doc/SphereMarker.png)

Pivot point is at the center of the sphere.

`scale.x` is diameter in x direction, `scale.y` in y direction,
`scale.z` in z direction. By setting these to different values you get
an ellipsoid instead of a sphere.

##### Cylinder (CYLINDER=3)

![Cylinder](doc/CylinderMarker.png)

Pivot point is at the center of the cylinder.

`scale.x` is diameter in x direction, `scale.y` in y direction, by
setting these to different values you get an ellipse instead of a
circle. Use `scale.z` to specify the height.

##### Line Strip (LINE_STRIP=4)

![Line Strip](doc/LineStripMarker.png)

Line strips use the `points` member of the
[visualization_msgs/msg/Marker](https://docs.ros.org/en/rolling/p/visualization_msgs/msg/Marker.html)
message. It will draw a line between every two consecutive points, so
0-1, 1-2, 2-3, 3-4, 4-5\...

Line strips also have some special handling for `scale`: **only
`scale.x` is used** and it controls the width of the line segments.

Note that `pose` is still used (the points in the line will be
transformed by them), and the lines will be correct relative to the
frame id specified in the header.

In visualization 1.1+ will also optionally use the `colors` member for
per-vertex color.

##### Line List (LINE_LIST=5)

![Line List](doc/LineListMarker.png)

Line lists use the `points` member of the
[visualization_msgs/msg/Marker](https://docs.ros.org/en/rolling/p/visualization_msgs/msg/Marker.html)
message. It will draw a line between each pair of points, so 0-1, 2-3,
4-5, \...

Line lists also have some special handling for `scale`: **only
`scale.x` is used** and it controls the width of the line segments.

Note that `pose` is still used (the points in the line will be
transformed by them), and the lines will be correct relative to the
frame id specified in the header.

In visualization 1.1+ will also optionally use the `colors` member for
per-vertex color. The color of a line segment then gradually changes
from its start to end point.

##### Cube List (CUBE_LIST=6)

![Cube List](doc/CubeListMarker.png)

A cube list is a list of cubes with all the same properties except their
positions. Using this object type instead of a
[visualization_msgs/msg/MarkerArray](https://docs.ros.org/en/rolling/p/visualization_msgs/msg/MarkerArray.html)
allows rviz to batch-up rendering, which causes them to render much
faster. The caveat is that they all must have the same scale.

The `points` member of the
[visualization_msgs/msg/Marker](https://docs.ros.org/en/rolling/p/visualization_msgs/msg/Marker.html)
message is used for the position of each cube.

In visualization 1.1+ will also optionally use the `colors` member for
per-cube color.

##### Sphere List (SPHERE_LIST=7)

![Sphere List](doc/SphereListMarker.png)

A sphere list is a list of spheres with all the same properties except
their positions. Using this object type instead of a
[visualization_msgs/msg/MarkerArray](https://docs.ros.org/en/rolling/p/visualization_msgs/msg/MarkerArray.html)
allows rviz to batch-up rendering, which causes them to render much
faster. The caveat is that they all must have the same scale.

The `points` member of the
[visualization_msgs/msg/Marker](https://docs.ros.org/en/rolling/p/visualization_msgs/msg/Marker.html)
message is used for the position of each sphere.

Note that `pose` is still used (the points in the line will be
transformed by them), and the lines will be correct relative to the
frame id specified in the header.

In visualization 1.1+ will also optionally use the `colors` member for
per-sphere color.

##### Points (POINTS=8)

![Points](doc/PointsMarker.png)

Uses the `points` member of the
[visualization_msgs/msg/Marker](https://docs.ros.org/en/rolling/p/visualization_msgs/msg/Marker.html)
message.

Points have some special handling for `scale`: **`scale.x` is point
width, `scale.y` is point height**

Note that `pose` is still used (the points in the line will be
transformed by them), and the lines will be correct relative to the
frame id specified in the header.

In visualization 1.1+ will also use the `colors` member for per-point
color.

##### View-Oriented Text (TEXT_VIEW_FACING=9) \[1.1+\]

![View-Oriented Text](doc/text_view_facing_marker.png)

This marker displays text in a 3D spot in the world. The text always
appears oriented correctly to the view. Uses the `text` field in the
marker.

Only `scale.z` is used. `scale.z` specifies the height of an
uppercase "A".

##### Mesh Resource (MESH_RESOURCE=10) \[1.1+\]

![attachment:mesh_resource_marker.png](doc/mesh_resource_marker.png)

Uses the `mesh_resource` field in the marker. Can be any mesh type
supported by rviz (binary .stl or Ogre .mesh in 1.0, with the addition
of COLLADA (.dae) in 1.1). The format is the URI-form used by
[resource_retriever](https://index.ros.org/p/resource_retriever),
including the `package:*` syntax.*

An example of a mesh an its use is



```cplusplus
marker.type = visualization_msgs::Marker::MESH_RESOURCE;
marker.mesh_resource = "package://pr2_description/meshes/base_v0/base.dae";
```

 Scale on a mesh is relative. A scale of `(1.0,
1.0, 1.0)` means the mesh will display as the exact size specified in
the mesh file. A scale of `(1.0, 1.0, 2.0)` means the mesh will show
up twice as tall, but the same width/depth.

If the `mesh_use_embedded_materials` flag is set to true and the mesh
is of a type which supports embedded materials (such as COLLADA), the
material defined in that file will be used instead of the color defined
in the marker.

Since version **\[1.8\]**, even when `mesh_use_embedded_materials` is
true, if the marker color is set to anything other than r=0,g=0,b=0,a=0
the marker color and alpha will be used to tint the mesh with the
embedded material.

##### Triangle List (TRIANGLE_LIST=11) \[1.1+\]

![attachment:triangle_list_marker.png](doc/triangle_list_marker.png)

Uses the `points` and optionally `colors` members. Every set of 3
points is treated as a triangle, so indices 0-1-2, 3-4-5, etc.

Note that `pose` and `scale` are still used (the points in the line
will be transformed by them), and the lines will be correct relative to
the frame id specified in the header.

### Rendering Complexity Notes

A single marker is always less expensive to render than many markers.
For example, a single cube list can handle thousands of cubes, where we
will not be able to render thousands of individual cube markers.

## DisplayTypes/Path

![X](doc/Path.png)

The **Path** display shows a
[nav_msgs/msg/Path](https://docs.ros.org/en/rolling/p/nav_msgs/msg/Path.html)
as a line strip.

[Youtube](https://www.youtube.com/watch?v=rreGhJrl1TI)

  -- ---------- -- ------------------------------------------------- -- ---------------------------------------------- -- -------------- --
                   **Properties**                                                                                                        
     **Name**      **Description**                                      **Valid Values**                                  **Default**    
     Color         The color of the line                                (\[0-255\], \[0-255\], \[0-255\])                 (25, 255, 0)   
     Alpha         The amount of transparency to apply to the line      \[0-1\]                                           1              
     Topic         The topic to subscribe to                            Any valid [Graph Resource Name](Names#Graph)      Empty String   
  -- ---------- -- ------------------------------------------------- -- ---------------------------------------------- -- -------------- --

## DisplayTypes/Point

![Pose](doc/Point.png)

The **Point** display shows a
[geometry_msgs/msg/PointStamped](https://docs.ros.org/en/rolling/p/geometry_msgs/msg/PointStamped.html)
message as a sphere.

  -- ---------- -- --------------------------------------------------- -- ---------------------------------------------- -- -------------- --
                   **Properties**                                                                                                          
     **Name**      **Description**                                        **Valid Values**                                  **Default**    
     Topic         The topic to subscribe to                              Any valid [Graph Resource Name](Names#Graph)      Empty String   
     Color         The color of the arrow                                 (\[0-255\], \[0-255\], \[0-255\])                 (255, 25, 0)   
     Alpha         The amount of transparency to apply to the sphere      \[0-1\]                                           1              
     Radius        The radius of the spere, in meters                     0.0001+                                           0.1            
  -- ---------- -- --------------------------------------------------- -- ---------------------------------------------- -- -------------- --

## DisplayTypes/Pose

![Pose](doc/Pose.png)

The **Pose** display shows a
[geometry_msgs/msg/PoseStamped](https://docs.ros.org/en/rolling/p/geometry_msgs/msg/PoseStamped.html)
message as either an arrow or a set of axes.

[Youtube](https://www.youtube.com/watch?v=3AwcxbbYrso)

  -- -------------- -- -------------------------------------------------- -- ---------------------------------------------- -- -------------- --
                       **Properties**                                                                                                         
     **Name**          **Description**                                       **Valid Values**                                  **Default**    
     Topic             The topic to subscribe to                             Any valid [Graph Resource Name](Names#Graph)      Empty String   
     Shape             The shape to use to show the pose.                    Arrow, Axes                                       Arrow          
                       **Arrow Properties**                                                                                                   
     Color             The color of the arrow                                (\[0-255\], \[0-255\], \[0-255\])                 (255, 25, 0)   
     Alpha             The amount of transparency to apply to the arrow      \[0-1\]                                           1              
     Shaft Length      The length of the arrow shaft, in meters              0.0001+                                           1              
     Shaft Radius      The radius of the arrow shaft, in meters              0.0001+                                           0.1            
     Head Length       The length of the arrow head, in meters               0.0001+                                           1              
     Head Radius       The radius of the arrow head, in meters               0.0001+                                           0.1            
                       **Axes Properties**                                                                                                    
     Axes Length       The length of each axis, in meters                    0.0001+                                           1              
     Axes Radius       The radius of each axis, in meters                    0.0001+                                           1              
  -- -------------- -- -------------------------------------------------- -- ---------------------------------------------- -- -------------- --

## DisplayTypes/PoseArray

The **Pose Array** display shows a
[geometry_msgs/msg/PoseArray](https://docs.ros.org/en/rolling/p/geometry_msgs/msg/PoseArray.html)
message, as a collection of either 2D or 3D arrows, or coordinate axes.

![PoseArray with 2D arrows](doc/PoseArray.png)

[Youtube](https://www.youtube.com/watch?v=rO5cUkAXDlA)

  -- ---------- -- ------------------------------------------------------ -- ---------------------------------------------- -- -------------- --
                   <style="text-align:center">**Common Properties**                                                                       
     **Name**      **Description**                                           **Valid Values**                                  **Default**    
     Shape         The shape of the poses                                    Arrow (Flat), Arrow (3D), Axes                    Arrow (Flat)   
     Topic         The topic to subscribe to                                 Any valid [Graph Resource Name](Names#Graph)      Empty String   
  -- ---------- -- ------------------------------------------------------ -- ---------------------------------------------- -- -------------- --

### Arrow (Flat)

The arrows will point in the X direction of each Pose. And the face of
the arrow will be orthogonal to the Z axis.

  -- -------------- -- ----------------------------------------------- -- ----------------------------------- -- -------------- --
                       <style="text-align:center">**Properties**                                                            
     **Name**          **Description**                                    **Valid Values**                       **Default**    
     Color             The color of the arrows                            (\[0-255\], \[0-255\], \[0-255\])      (255, 25, 0)   
     Alpha             The transparency of the arrows                     \[0-1\]                                1              
     Arrow Length      The length of the arrows                                                                  0.3            
  -- -------------- -- ----------------------------------------------- -- ----------------------------------- -- -------------- --

### Arrow (3D)

Representation of the poses similar to the arrows from
[visualization_msgs/msg/Marker](https://docs.ros.org/en/rolling/p/visualization_msgs/msg/Marker.html).
The arrows will point in the X direction of each Pose.

![PoseArray with 3D arrows](doc/pose_array_arrows.png)

  -- -------------- -- ----------------------------------------------- -- ----------------------------------- -- -------------- --
                       <style="text-align:center">**Properties**                                                            
     **Name**          **Description**                                    **Valid Values**                       **Default**    
     Color             The color of the arrows                            (\[0-255\], \[0-255\], \[0-255\])      (255, 25, 0)   
     Alpha             The transparency of the arrows                     \[0-1\]                                1              
     Head Radius       The radius of the base of the arrow head                                                  0.03           
     Head Length       The length of the arrow head                                                              0.07           
     Shaft Radius      The radius of the arrow shaft                                                             0.01           
     Shaft Length      The length of the arrow shaft                                                             0.23           
  -- -------------- -- ----------------------------------------------- -- ----------------------------------- -- -------------- --

### Axes

Representation of the poses as coordinate axes.

![PoseArray with coordinate axes](doc/pose_array_axes.png)

  -- ------------- -- ----------------------------------------------- -- ------------------ -- ------------- --
                      <style="text-align:center">**Properties**                                          
     **Name**         **Description**                                    **Valid Values**      **Default**   
     Axes Radius      The radius of an axis leg                                                0.01          
     Axes Length      The length of an axis leg                                                0.3           
  -- ------------- -- ----------------------------------------------- -- ------------------ -- ------------- --

## DisplayTypes/PointCloud

![PointCloud](doc/PointCloud.png)

The **Point Cloud** display shows data from a (legacy)
[sensor_msgs/msg/PointCloud](https://docs.ros.org/en/rolling/p/sensor_msgs/msg/PointCloud.html)
message.

The **Point Cloud2** display shows data from a (recommended)
[sensor_msgs/msg/PointCloud2](https://docs.ros.org/en/rolling/p/sensor_msgs/msg/PointCloud2.html)
message. This display is compatible with the [Point Cloud Library](pcl)
native point cloud type
[pcl::PointCloud<T>](http://www.ros.org/doc/api/pcl/html/classpcl_1_1PointCloud.html),
when it is published with support from
[pcl_ros](https://index.ros.org/p/pcl_ros).

[Youtube](https://www.youtube.com/watch?v=eqwrmt6vOzQ)

  -- ------------------------------ -- --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- -- -------------------------------------------------- -- -------------------------------------------------------------- --
                                       **Properties**                                                                                                                                                                                                                                                                                                                                                                          
     **Name**                          **Description**                                                                                                                                                                                                                                                    **Valid Values**                                      **Default**                                                    
     Selectable                        Whether or not this cloud is selectable using the selection tool.                                                                                                                                                                                                  True, False                                           True                                                           
     Style                             The rendering style to use when drawing the points, listed in order of computational expense. There are currently 4 rendering styles, [which are explained in the Rendering Styles section](#renderingstyles)          Points, Billboards, Billboard Spheres, Boxes          Billboards                                                     
     Channel                           Which channel(s) to use to color the points. This dropdown is dynamically populated based on the channels in the last cloud received. The individual channels are [explained in the Channels section](#channels).      Intensity, Color (RGB), Normal Sphere, Curvature      First option which has a corresponding channel in the cloud.   
     Alpha                             The amount of transparency to apply to the points. Note that this does not work perfectly, and you may see some rendering strangeness if this is set to anything but 1                                                                                             \[0-1\]                                               1                                                              
     Min Color                         For intensity channels, the color to assign to the minimum value. [See the Intensity Channel section for more information.](#intensitychannel)                                                                         (\[0-255\], \[0-255\], \[0-255\])                     (0, 0, 0)                                                      
     Min Color                         For intensity channels, the color to assign to the maximum value. [See the Intensity Channel section for more information.](#intensitychannel)                                                                         (\[0-255\], \[0-255\], \[0-255\])                     (255, 255, 255)                                                
     Billboard Size                    The size, in meters, to display the billboards (or boxes). This setting does not affect the *Points* rendering style                                                                                                                                               0.0001+                                               0.01                                                           
     Autocompute Intensity Bounds      Whether or not to auto-compute the "Min Intensity" and "Max Intensity" properties                                                                                                                                                                              True, False                                           True                                                           
     Min Intensity                     The minimum value to use for intensity channel coloring. [See the Intensity Channel section for more information.](#intensitychannel)                                                                                  \[-inf, < Max Intensity\]\]                          0                                                              
     Max Intensity                     The maximum value to use for intensity channel coloring. [See the Intensity Channel section for more information.](#intensitychannel)                                                                                  \[> Min Intensity, inf\]\]                           4096                                                           
     Decay Time                        The amount of time to keep a cloud/scan around before removing it. A value of 0 means to only display the most recent data.                                                                                                                                        0+                                                    0                                                              
     Topic                             The topic to subscribe to                                                                                                                                                                                                                                          Any valid [Graph Resource Name](Names#Graph)          Empty String                                                   
  -- ------------------------------ -- --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- -- -------------------------------------------------- -- -------------------------------------------------------------- --

<a id="renderingstyles"></a>

### Rendering Styles

  -- ------------------- -- ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------- -- ------------------------------------------------ --
     Points                 Points are a fixed size on-screen, currently 3 pixels by 3 pixels. This means you can often see more definition from far away, but as you get closer the density decreases.      ![Points](doc/Points.png)                        
     Billboards             Billboards are camera-facing quads, that have real-world size.                                                                                                                   ![Billboards](doc/Billboards.png)                
     Billboard Spheres      Similar to *Billboards*, but rendered such that they look like spheres, and provide some contrast so you can tell individual points apart if they are overlapping.               ![Billboard Spheres](doc/BillboardSpheres.png)   
     Boxes                  Cubes in the world.                                                                                                                                                              ![Boxes](doc/Boxes.png)                          
  -- ------------------- -- ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------- -- ------------------------------------------------ --

<a id="channels"></a>

### Channels

`PointCloud`s can have any number of channels associated with them. If
you're using a `LaserScan` display, the only available channel will
be the "Intensity" channel.

This section explains how the color/position of a point is computed for
each channel type.

<a id="intensitychannel"></a>

#### Intensity

Valid channel names: `intensity`, `intensities`

Intensity only affects the color of the point.

The intensity channel uses 4 values to compute the final color of the
point:

  -- --------------- -- ------- --
     Min Intensity      min_i   
     Max Intensity      max_i   
     Min Color          min_c   
     Max Color          max_c   
  -- --------------- -- ------- --

For each point:

- To compute the color value, we first compute a normalized intensity
  value based on `min_i` and `max_i`: 

```
norm_i = (i - min_i) / (max_i - min_i)
```


- Then to compute the color from that normalized intensity:
  

```
final_c = (norm_i * max_c) + ((1 - norm_i) * min_c)
```



#### RGB

Valid channel names: `rgb` (1 channel), `r`, `g`, `b` (3
channel)

RGB only affects the color of the point.

There are two ways to specify RGB: 1. 3 channels, named "r", "g",
and "b", with floating point values between 0 and 1. 1. 1 channel,
with the float in the channel reinterpreted as 3 single-byte values with
ranges from 0 to 255. `0xff0000` is red, `0xff00` is green, `0xff`
is blue.

- In C++,
  `int rgb = 0xff0000; float float_rgb = *reinterpret_cast<float*>(&rgb); `
- In Python,
  ` float_rgb = struct.unpack('f', struct.pack('i', 0xff0000))[0]`

#### Normal Sphere

Valid channel names: `nx`, `ny`, `nz` (all 3 required)

Normal Sphere only affects the position of the point.

For this channel, the "nx", "ny" and "nz" channels will be used to
position the points instead of the values in the points array.

#### Curvature

Valid channel names: `curvature`, `curvatures`

Curvature colors in the same way
[intensity](#intensitychannel)
does.

## DisplayTypes/Polygon

![Polygon](doc/Polygon.png)

The **Polygon** display shows a
[geometry_msgs/msg/PolygonStamped](https://docs.ros.org/en/rolling/p/geometry_msgs/msg/PolygonStamped.html)
as a line strip, with the last point in the strip reconnecting to the
first.

[Youtube](https://www.youtube.com/watch?v=1um2Ghg-5ko)

  -- ---------- -- ------------------------------------------------------- -- ---------------------------------------------- -- -------------- --
                   **Properties**                                                                                                              
     **Name**      **Description**                                            **Valid Values**                                  **Default**    
     Color         The color of the line strip                                (\[0-255\], \[0-255\], \[0-255\])                 (25, 255, 0)   
     Alpha         The amount of transparency to apply to the line strip      \[0-1\]                                           1              
     Topic         The topic to subscribe to                                  Any valid [Graph Resource Name](Names#Graph)      Empty String   
  -- ---------- -- ------------------------------------------------------- -- ---------------------------------------------- -- -------------- --

## DisplayTypes/Odometry

![Odometry](doc/Odometry.png)

The **Odometry** display accumulates a
[nav_msgs/msg/Odometry](https://docs.ros.org/en/rolling/p/nav_msgs/msg/Odometry.html)
message over time, showing them as arrows.

[Youtube](https://www.youtube.com/watch?v=LdO4BEKZMWE)

  -- -------------------- -- ---------------------------------------------------------------------------------------------------------------------------- -- ---------------------------------------------- -- -------------- --
                             **Properties**                                                                                                                                                                                   
     **Name**                **Description**                                                                                                                 **Valid Values**                                  **Default**    
     Color                   The color of the arrows                                                                                                         (\[0-255\], \[0-255\], \[0-255\])                 (255, 25, 0)   
     Topic                   The topic to subscribe to                                                                                                       Any valid [Graph Resource Name](Names#Graph)      Empty String   
     Position Tolerance      The linear distance, in meters, by which the odometry must change to cause a new arrow to spawn                                 0.0001+                                           0.1            
     Angle Tolerance         The angular distance by which the odometry must change to cause a new arrow to spawn                                            \[0.0001, 1\]\]                                   0.1            
     Keep                    The number of arrows to keep before new arrows start causing old ones to disappear. 0 means an infinite number (dangerous)      0+                                                100            
  -- -------------------- -- ---------------------------------------------------------------------------------------------------------------------------- -- ---------------------------------------------- -- -------------- --

## DisplayTypes/Range

![Range](doc/RangeDisplay.png)

The **Range** display shows range measurements. Each one is a cone
starting at the origin of the frame given in the header of the
[sensor_msgs/msg/Range](https://docs.ros.org/en/rolling/p/sensor_msgs/msg/Range.html)
message and fanning out in the +X direction of that frame.

To display multiple ranges (like from a robot with several sonars),
publish a TF frame at each sonar location. Publish the range messages
with the corresponding frame_id in each header. Then in rviz, in the
Range display properties, set "Buffer Length" to the number of range
sensors on your robot.

  -- --------------- -- ------------------------------------------------------------------------------------------------------------------- -- ------------------ -- ------------- --
                        **Properties**                                                                                                                                             
     **Name**           **Description**                                                                                                        **Valid Values**      **Default**   
     Topic              The topic on which to listen for Range messages.                                                                                                           
     Color              The color of the range cones                                                                                                                               
     Alpha              Opacity of the range cones, 0 is transparent, 1 is opaque.                                                             0-1                   0.5           
     Buffer Length      The number of range measurements to show on this topic. Only the most recent (Buffer Length) cones will be shown.      1+                    1             
  -- --------------- -- ------------------------------------------------------------------------------------------------------------------- -- ------------------ -- ------------- --

## DisplayTypes/RobotModel

![RobotModel](doc/RobotModel.png)

The **Robot Model** display shows links of a robot (defined by a
[urdf](https://index.ros.org/p/urdf)), in their correct poses according
to the [tf](https://index.ros.org/p/tf) transform tree.

[Youtube](https://www.youtube.com/watch?v=fgVjUKUXO-8)

  -- ------------------- -- -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- -- ---------------------------------------------- -- ------------------- --
                            **Properties**                                                                                                                                                                                                                                                              
     **Name**               **Description**                                                                                                                                                                                       **Valid Values**                                  **Default**         
     Visual Enabled         Enables drawing the [visual](https://index.ros.org/p/urdf) representation of the robot                                                                                                                True, False                                       True                
     Collision Enabled      Enables drawing the [collision](https://index.ros.org/p/urdf) representation of the robot                                                                                                             True, False                                       False               
     Update Rate            The rate at which to update the pose of each link, in seconds. Setting this to a small value will have performance implications                                                                       0.01+                                             0.1                 
     Alpha                  The amount of transparency to apply to the links                                                                                                                                                      \[0-1\]                                           1                   
     Robot Description      The [parameter](Parameter Server) to retrieve the [urdf](https://index.ros.org/p/urdf) from. Uses `searchParam()` to search up the [parameter](Parameter Server) tree for the value specified.      Any valid [Graph Resource Name](Names#Graph)      robot_description   
     TF Prefix              New in cturtle. Sets the TF prefix to prepend to the link names loaded from the urdf                                                                                                                  Any valid tf prefix                               empty               
                            **Per-link Properties**                                                                                                                                                                                                                                                     
     Show Trail             Draws a trail behind the link. The trail originates from the origin of the link.                                                                                                                      True, False                                       False               
     Show Axes              Draws axes at the origin of the link.                                                                                                                                                                 True, False                                       False               
  -- ------------------- -- -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- -- ---------------------------------------------- -- ------------------- --

### URDF

The `Robot Description` parameter must be embedded xml, not the path
to the file on disc. You can load the XML with a launch file:


```
<launch>
    <param name="robot_description" textfile="$(find packagename)/model.xml" />
</launch>
```



The Robot Model display requires the URDF to have a visual or collision
tag defined in order to view your robot. See the `<visual>` and
`<collision>` sections on the
[Link XML Format](https://index.ros.org/p/urdf)

## DisplayTypes/TF

![X](doc/TF.png)

The **TF** display shows the [tf](https://index.ros.org/p/tf) transform
tree. There are three optional pieces of data to display: the frame
name, the frame axes, and an arrow from the frame to its parent.

If the axes are displayed, the X axis is indicated in red, the Y axis is
indicated in green, and the Z axis is indicated in blue.

[Youtube](https://www.youtube.com/watch?v=dQyIpsMUQSw)

  -- ------------- -- --------------------------------------------------------------------- -- ------------------ -- ---------------------------- --
                      **Properties**                                                                                                              
     **Name**         **Description**                                                          **Valid Values**      **Default**                  
     Show Names       Toggles whether or not to display the frame names                        True, False           True                         
     Show Axes        Toggles whether or not to display the frame axes                         True, False           True                         
     Show Arrows      Toggles whether or not to display arrows from child to parent            True, False           True                         
     All Enabled      Toggles whether all the frames should be shown                           True, False           True                         
                      **Per-Frame Properties**                                                                                                    
     Enabled          Toggle whether to show this frame                                        True, False           (value of "All Enabled")   
     Parent           Shows the name of this frame's parent                                                                                      
     Position         Shows the position of the frame, in the fixed frame's reference                                                            
     Orientation      Shows the orientation of the frame, in the fixed frame's reference                                                         
  -- ------------- -- --------------------------------------------------------------------- -- ------------------ -- ---------------------------- --

## DisplayTypes/Wrench

![Pose](doc/Wrench.png)

The **Wrench** display shows a
[geometry_msgs/msg/WrenchStamped](https://docs.ros.org/en/rolling/p/geometry_msgs/msg/WrenchStamped.html)
message as an arrow for force and arrow plus circles for torque.

  -- -------------- -- ------------------------------------------------------------------------------------------- -- ---------------------------------------------- -- ---------------- --
                       **Properties**                                                                                                                                                    
     **Name**          **Description**                                                                                **Valid Values**                                  **Default**      
     Topic             The topic to subscribe to                                                                      Any valid [Graph Resource Name](Names#Graph)      Empty String     
     Force Color       The color of the force arrow                                                                   (\[0-255\], \[0-255\], \[0-255\])                 (204, 51, 51)    
     Torque Color      The color of the torque arrow                                                                  (\[0-255\], \[0-255\], \[0-255\])                 (204, 204, 51)   
     Alpha             The opacity of the arrows. Can be anything between 1 and 0: 1 is opaque, 0 is transparent      \[0-1\]                                           1                
     Arrow Scale       Scale of arrows                                                                                0.0001+                                           1                
     Arrow Width       The width of arrows, in meters                                                                 0.0001+                                           1                
  -- -------------- -- ------------------------------------------------------------------------------------------- -- ---------------------------------------------- -- ---------------- --

## DisplayTypes/Twist

The **Twist** display shows a
[geometry_msgs/msg/TwistStamped](https://docs.ros.org/en/rolling/p/geometry_msgs/msg/TwistStamped.html)
message as an arrow for linear and arrow plus circles for angular
components. Please refer to similar
[Wrench](#displaytypeswrench).

  -- --------------- -- ------------------------------------------------------------------------------------------- -- ---------------------------------------------- -- ---------------- --
                        **Properties**                                                                                                                                                    
     **Name**           **Description**                                                                                **Valid Values**                                  **Default**      
     Topic              The topic to subscribe to                                                                      Any valid [Graph Resource Name](Names#Graph)      Empty String     
     Linear Color       The color of the linear arrow                                                                  (\[0-255\], \[0-255\], \[0-255\])                 (204, 51, 51)    
     Angular Color      The color of the angular arrow                                                                 (\[0-255\], \[0-255\], \[0-255\])                 (204, 204, 51)   
     Alpha              The opacity of the arrows. Can be anything between 1 and 0: 1 is opaque, 0 is transparent      \[0-1\]                                           1                
     Arrow Scale        Scale of arrows                                                                                0.0001+                                           1                
     Arrow Width        The width of arrows, in meters                                                                 0.0001+                                           1                
  -- --------------- -- ------------------------------------------------------------------------------------------- -- ---------------------------------------------- -- ---------------- --
