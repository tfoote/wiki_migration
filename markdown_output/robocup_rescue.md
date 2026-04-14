## Mission Statement

Building software for autonomous robots is a challenging,
multi-disciplinary and time consuming task. Researchers often
sub-optimally solve all topics and reinvent the wheel instead to provide
great solutions in their central research area. In order to overcome
this problem we propose a common software development based on ROS with
the following goals:

-   share and reuse of world-class solutions for common problems in USAR
    robots
-   accelerate the development of search and rescue robots
-   lower the entry-bar for new research groups
-   continuous development of a common software framework
-   train new people with existing software packages

## Available Software

### SLAM

-   [hector_slam](hector_slam) is a stack that provides a SLAM approach
    and associated tools that have been successfully used by numerous
    [RoboCup Rescue League](http://wiki.robocup.org/wiki/Robot_League)
    participants, including Best in Class Autonomy and overall
    competition champions.

### Navigation

-   [hector_exploration_planner](hector_exploration_planner) is a
    package that provides a path planner for generating both goals and
    plans for the exploration of unknown environments.

### Simulation

-   [hector_nist_arenas_gazebo](hector_nist_arenas_gazebo) is a stack
    that provides tools for the fast and intuitive creation of simulated
    NIST standard test arenas like those in the RRL competition.

### Optris Thermal Imager

-   [optris_drivers](optris_drivers) is a stack wrapping the binary
    driver for Optris thermal imager devices.

### QR code and victim detection

-   The [hector_vision](hector_vision) stack contains two packages that
    provide [QR code detection](hector_qrcode_detection) on arbitrary
    camera images and [victim (heat) detection](hector_heat_detection)
    based on thermal imaging. hector_qrcode_detection uses the
    [zbar](http://zbar.sourceforge.net) library internally. Both
    packages publish detections as
    [worldmodel_msgs/ImagePercept](worldmodel_msgs) messages that
    [hector_object_tracker](hector_object_tracker) can track and
    visualize as markers in [rviz](rviz) or
    [in the GeoTIFF map](hector_worldmodel_geotiff_plugins).

### Manipulation

-   The [tedusar_manipulation](tedusar_manipulation) stack provides
    packages for semi-autonomouse manipulation. The packages are the
    outcome of a short-term visit of team TEDUSAR Graz at team Hector
    Darmstadt.

## Tutorials for the hector_stack

## Users

-   Team Stabilize, Rajamangala University of Technology Phra Nakhon,
    Thailand
-   [Team BARTLAB](http://www.bartlab.org), Mahidol University, Thailand
-   [Team Hector Darmstadt](https://www.facebook.com/TeamHectorDarmstadt),
    Technische Universität Darmstadt, Germany
-   [Team TEDUSAR](http://www.facebook.com/tedusar), Technische
    Universität Graz, Graz, Austria - University Maribor, Maribor,
    Slovenia
-   Team MRL
-   Team Socrob RESCUE, Lisbon, Portugal
-   [RRT-Team FH-Wels](http://rrt.fh-wels.at), University of Applied
    Sciences Upper Austria - Campus Wels
-   Team ResCube, Hungary
-   others

## Roadmap

### Software under development

-   2D costmap determination from octomap
-   Mono/Stereo Vision-based 6D-SLAM

### Ideas looking for developers

-   Victim detection (based on thermal images, RGB or RGBD cameras,
    motion, sound)

## Events

In order to push this idea forward several workshops and summer schools
took place. The different events serve as synchronization points, where
new requirements are discussed and prototypes are developed. Future
events are already planned. Stay tuned!

-   ROS Workshop for RoboCup Rescue teams, Koblenz, Germany, 2010
-   [Workshop on Standard Robotic Software Architecture for RoboCupRescue based on ROS](http://tinyurl.com/rosworkshop),
    Koblenz, Germany, 2011
-   [ROS RoboCup Rescue Summer School 2012](http://tedusar.eu/cms/en/summerschool2012),
    Graz, Austria, 2012
-   [SSRR Summer School 2012](http://wiki.ssrrsummerschool.org/doku.php?id=2012:home),
    Alanya, Turkey, 2012
-   [Rescue Robotics Camp 2013](http://www.ist.tugraz.at/ssrr13/Main_Page) -
    colocated with SSRR 2013, Linkoeping, Sweden, November 2013

## Links/Literature

\[1\] Stefan Kohlbrecher, Karen Petersen, Gerald Steinbauer, Johannes
Maurer, Peter Lepej, Suzana Uran, Rodrigo Ventura, Christian Dornhege,
Andreas Hertle, Raymond Sheh, Johannes Pellenz, \"Community-Driven
Development of Standard Software Modules for Search and Rescue Robots\",
Proc. IEEE International Symposium on Safety, Security and Rescue
Robotics (SSRR), November 2012.

\[2\] S. Kohlbrecher, J. Meyer, O. von Stryk, and U. Klingauf. A
flexible and scalable slam system with full 3d motion estimation. In
Proc. IEEE International Symposium on Safety, Security and Rescue
Robotics (SSRR), November 2011.

\[3\] Stephan Wirth and Johannes Pellenz. Exploration transform: A
stable exploring algorithm for robots in rescue environments.
Proceedings of the IEEE International Workshop on Safety, Security and
Rescue Robotics (SSRR), 2007.

\[4\] Stefan Kohlbrecher and Johannes Meyer and Thorsten Graber and
Karen Petersen and Oskar von Stryk and Uwe Klingauf. Hector open source
modules for autonomous mapping and navigation with rescue robots.
Proceedings RoboCup Symposium 2013
