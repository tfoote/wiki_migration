# What is visp_ros

[visp_ros](visp_ros) is an extension of [ViSP](https://visp.inria.fr)
library developed by Inria [Rainbow](https://team.inria.fr/rainbow/)
team. While ViSP is independent to ROS, in [visp_ros](visp_ros) we
benefit from ROS features.

![](attachment:visp_ros.png)

[visp_ros](visp_ros) contains a library:

-   with new C++ classes (vpROSGrabber, vpROSRobot, vpROSRobotPioneer,
    vpROSRobotFrankaCoppeliasim) that could be used like usual
    [ViSP classes](https://visp-doc.inria.fr/doxygen/visp-daily/classes.html).
    They are based on ROS, but to use them there is no need to know so
    much about ROS;
-   that makes possible to use ROS in a transparent way, either by
    building classical binaries without catkin, either by building ROS
    nodes with catkin but without the need to write ROS specific code;
-   where creating a ROS node out of ViSP becomes simple.

[visp_ros](visp_ros) contains also a set of ROS nodes that allow to
control specific hardware such as for the moment:

-   robots that can be controlled only in our lab due to proprietary
    drivers: Afma6 gantry robot, Biclops PT head, ADEPT Viper 650 and
    850 robots described
    [here](https://team.inria.fr/rainbow/research/robotics-platforms/);
-   other robots that anyone can buy and use with open-source drivers
    interfaced in ViSP: Pioneer mobile robot, Parrot bebop2 drone

[visp_ros](visp_ros) contains also a tutorial that shows how to simulate
a Franka Panda robot using
[CoppeliaSim](https://www.coppeliarobotics.com/).

To illustrate [visp_ros](visp_ros) behavior let us focus on a visual
servoing example.

# Visual servoing example

In this example we consider the visual servo of a robot equipped with a
firewire camera.

## Using ViSP

With ViSP, images from a firewire camera connected to a computer running
Ubuntu or Fedora can be acquired using vp1394TwoGrabber class. There are
also some specific classes like vpRobotAfma6, vpRobotViper850,
vpRobotPioneer that are wrapper over robot controllers.

Implementing a visual servo with ViSP is resumed in the next image:

![](attachment:visual-servo-visp.png)

The corresponding code looks like the following:

```
#include <visp/vpImage.h> 
#include <visp/vp1394TwoGrabber.h> 
#include <visp/vpRobotViper850.h>

int main() 
{
  vpImage<unsigned char> I; 
  vpRobotViper850 robot; 
  robot.init();

  vp1394TwoGrabber g; 
  g.open(I); 

  while(1) {
    g.acquire(I); 
    // Visual servoing code 
    robot.setVelocity(vpRobot::CAMERA_FRAME, v);
  }
}
```

## Using visp_ros

Using [visp_ros](visp_ros) allows to completely separate the code that
is specific to the material (frame grabber, robot) from the one that
does the visual servoing.

In [visp_ros](visp_ros) we introduce a new class named vpROSGrabber that
is able to subscribe to an image topic. This class can be used to
replace any ViSP grabber. We also introduce vpROSRobot that is able to
publish cmd_vel velocities on a given topic.

![](attachment:visual-servo-ros.png)

Now using visp_ros, we can do the same by subscribing to the
/camera/image_raw topic and by publishing velocities to the
/myrobot/cmd_vel topic.

```
#include <visp/vpImage.h> 
#include <visp_ros/vpROSGrabber.h>
#include <visp_ros/vpROSRobot.h>

int main() 
{
  vpImage<unsigned char> I; 
  vpROSRobot robot; 
  robot.setCmdVelTopic("/myrobot/cmd_vel");
  robot.init();

  vpROSGrabber g; 
  g.setImageTopic("/camera/image_raw");
  g.open(I); 

  while(1) {
    g.acquire(I); 
    // Visual servoing code 
    robot.setVelocity(vpRobot::CAMERA_FRAME, v);
  }
}
```

It is also possible to subscribe to a jpeg topic named for example
\"/camera/image_jpg\" using the following code: ```
...
  vpROSGrabber g; 
  g.setImageTopic("/camera/image_jpg"); // Name of the compressed topic
  g.setImageTransport("jpeg");          // Type of compression. Must differ from "raw"
  g.open(I); 
  ...
```

This
[tutorial](http://docs.ros.org/en/noetic/api/visp_ros/html/tutorial-ros-grabber.html)
highlights vpROSGrabber usage.

## Using visp_ros to produce a ROS node

With minor changes, it is possible to modify the previous example in
order to create a ROS node that does the visual servoing in a complete
transparent way just by passing argc and argv parameters.

![](attachment:visual-servo-ros-node.png)

```
#include <visp/vpImage.h> 
#include <visp_ros/vpROSGrabber.h>
#include <visp_ros/vpROSRobot.h>

int main(int argc, char **argv) 
{
  vpImage<unsigned char> I; 
  vpROSRobot robot; 
  robot.setCmdVelTopic("/myrobot/cmd_vel");
  robot.init(argc, argv);

  vpROSGrabber g; 
  g.setImageTopic("/camera/image_raw");
  g.open(argc, argv); 

  while(1) {
    g.acquire(I); 
    // Visual servoing code 
    robot.setVelocity(vpRobot::CAMERA_FRAME, v);
  }
}
```

# Controlling a Parrot Bebop2 drone by Visual-Servoing

Using [visp_ros](visp_ros) allows to do visual servoing with the Parrot
Bebop 2 drone. The following video shows an example.

[Youtube](https://www.youtube.com/watch?v=le07g-RRsJM)

This
[tutorial](http://wiki.ros.org/visp_ros/Tutorials/How%20to%20do%20visual%20servoing%20with%20Parrot%20Bebop%202%20drone%20and%20visp_ros)
explains how to proceed.

# FrankaSim: Simulating Franka robot using CoppeliaSim

Using [visp_ros](visp_ros) makes possible to simulate a Franka robot in
position, velocity and force control. All the rendering and sensing is
done through [CoppeliaSim](https://www.coppeliarobotics.com/) while the
geometric and dynamic model is handled in [visp_ros](visp_ros).
Communication between [visp_ros](visp_ros) and
[CoppeliaSim](https://www.coppeliarobotics.com/) is done using ROS.

The simulation is a physical simulation with a model that has been
accurately identified from a real Franka robot. All the details are in
the [paper](http://rainbow-doc.irisa.fr/publi/publi/Gaz19a-eng.html):

\'\'C. Gaz, M. Cognetti, A. Oliva, P. Robuffo Giordano, A. De Luca,
Dynamic Identification of the Franka Emika Panda Robot With Retrieval of
Feasible Parameters Using Penalty-Based Optimization. IEEE RA-L,
2019\'\'.

If you are using this simulator we would appreciate that you cite this
[paper](http://rainbow-doc.irisa.fr/publi/publi/Gaz19a-eng.html).

The following video shows an example of Image-Based Visual-Servoing
performed with a simulated Franka robot.

[Youtube](https://www.youtube.com/watch?v=02Bx093Fuak)

There is a tutorial that explains how to start with this simulator to
implement an image-based or position-based visual-servoing, or also an
impedance controller, but right now this tutorial doesn\'t appear in
visp_ros
[C++ API documentation](http://docs.ros.org/noetic/api/visp_ros/html/index.html).
To generate this tutorial from source code we suggest to
[instructions](https://github.com/lagadic/visp_ros#build-documentation-and-tutorials)
described in \'\'\'Build documentation and tutorials\'\'\' section using
rosdoc_lite to generate the package Doxygen documentation.

# Installation

The tutorial
[ How to install visp_ros](http://wiki.ros.org/visp_ros/Tutorials/Howto_install_visp_ros)
explains how to build and install [visp_ros](visp_ros) in a catkin
workspace.

You may also find installation instructions
[here](https://github.com/lagadic/visp_ros#readme).

# Documentation

-   See
    [ C++ API](http://docs.ros.org/noetic/api/visp_ros/html/index.html)
    documentation
-   See
    [ tutorials](http://docs.ros.org/noetic/api/visp_ros/html/index.html)
