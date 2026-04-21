## Introduction

This package is basically an OpenSceneGraph (OSG) adaptation of the
[Interactive Markers](../interactive_markers) client writen for
rviz/Ogre. Most of the code has been taken from the rviz sources, and
adapted to use OSG data types and facilities when possible. It allows
the creation of Interactive Markers in OpenSceneGraph applications.

## Setting an Interactive Markers client in OSG

Let's have a look to the `osg_interactive_markers_demo.cpp` example,
inside the `osg_interactive_markers` package:

```cplusplus
#include <osgViewer/Viewer>
#include <osgViewer/ViewerEventHandlers>
#include <osg/Group>
#include <osgGA/TrackballManipulator>
#include <osgGA/GUIEventHandler>

#include <osg_interactive_markers/interactive_marker_display.h>
#include <osg_utils/osg_utils.h>
#include <osg_utils/frame_manager.h>

using namespace osg_utils;
using namespace osg_interactive_markers;

int main(int argc, char *argv[])
{

   osg::Group *root=new osg::Group();

   osgViewer::Viewer viewer;

   viewer.setSceneData( root );
   viewer.setUpViewInWindow (0, 0, 800, 600);

   osgGA::TrackballManipulator* tb = new osgGA::TrackballManipulator;
   tb->setHomePosition( osg::Vec3f(20,20,20), osg::Vec3f(0,-15,0), osg::Vec3f(0,0,1) );
   viewer.setCameraManipulator( tb );

   viewer.addEventHandler( new osgViewer::StatsHandler );
   viewer.addEventHandler(new osgViewer::WindowSizeHandler);

   ros::init(argc, argv, "osg_interactive_markers");

   boost::shared_ptr<FrameManager> frame_manager = FrameManager::instance();
   frame_manager->setFixedFrame("/base_link");
   InteractiveMarkerDisplay marker_cli("osg_im","/basic_controls/update", root, *(frame_manager->getTFClient()));

   viewer.realize();
   viewer.frame();
    
    ros::WallTime last_wall_time = ros::WallTime::now();
    ros::Time last_ros_time = ros::Time::now();
    while( !viewer.done() && ros::ok())
    {
	ros::spinOnce();
        
        viewer.frame();
       
        ros::WallTime current_wall_time=ros::WallTime::now();
        ros::Time current_ros_time=ros::Time::now();
	marker_cli.update((current_wall_time-last_wall_time).toSec(), (current_ros_time-last_ros_time).toSec());
	last_wall_time=current_wall_time;
	last_ros_time=current_ros_time;
    }
    return 0;
}
```

The example above creates an OpenSceneGraph application that listens for
Interactive Markers in the `basic_controls/update` topic. By running the
above example and the
[Interactive Markers: Getting Started](../rviz/Tutorials/Interactive Markers: Getting Started)
tutorial in different terminals you should see something like the
following:

```
$ rosrun osg_interactive_markers osg_interactive_markers_demo
```

```
$ rosrun interactive_marker_tutorials basic_controls
```

![OSG Interactive Markers\|width=640](attachment:osg_interactive_markers.png)

Unlike in rviz, here you need to press the Control key for enabling
interaction. For instance, if you want to interact with a marker, you
have to press the Control key, and then click on the marker and drag.

Let's have a look to the code required for setting the Interactive
Markers client. First you need to create a FrameManager instance and set
the fixed frame where you expect the markers to be referenced to. After
that, InteractiveMarkerDisplay is the main class you have to
instantiate, giving as input the topic where to listen to Interactive
Markers, a node in your OSG scene that will hold the geometry, and a TF
client:

```cplusplus
boost::shared_ptr<FrameManager> frame_manager = FrameManager::instance();
frame_manager->setFixedFrame("/base_link");
InteractiveMarkerDisplay marker_cli("osg_im","/basic_controls/update", root, *(frame_manager->getTFClient()));
```

Then you need to call the update method at each iteration in your main
loop, with the Wall and ROS ellapsed times as arguments:

```cplusplus
   ...
   marker_cli.update((current_wall_time-last_wall_time).toSec(), (current_ros_time-last_ros_time).toSec());
   ...
```

## What does not work

`osg_interactive_markers` does not currently offer all the potential of
Interactive Markers. However, the most frequent use cases should be
supported.

This is a list of the functionality still not implemented:

-   Fixed-orientation controls
-   View facing controls
-   Menus
-   The following marker types: line strips, line lists and points.
