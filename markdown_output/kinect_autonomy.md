# Introduction

This project and wiki page is the product of a semester long independent
study conducted for the Civil and Mechanical Engineering Department.
Additional assistance and expertise was received from the Robotics
Research Center within the Department of Electrical Engineering and
Computer Science at The United States Military Academy at West Point.

## Purpose

The purpose of this project was to develop a system that allows a user
to control an autonomous vehicle through the use of hand and arm
signals, similar to how military personnel ground guide vehicles during
motor pool operations. Currently the Army is beginning to integrate more
unmanned and autonomously capable assets into the fighting force.
However, in order to effectively interface with these systems, the
operator must complete extensive training on the equipment in order to
be considered qualified a qualified operator. The goal for this project
was to assess the possibility of giving autonomous/unmanned vehicles the
capability of being controlled via some means that does not require any
additional training on behalf of the individual, or the units that have
access to these assets.

## Assessment of Success

The success and viability of this system was determined based on ease of
use, possibility for future expansion, cost of implementation, and the
feasibility for implementation within the military. Each of these
categories was considered when determining the success of the system.
However, a large focus was placed on assessing the feasibility of
implementation for military and combat uses without the need for
additional training.

# Development

## Initial Approach

The initial idea behind this project was to make use of a motion capture
camera, that has the ability to track a user\'s movements, as a means of
converting certain poses or gestures into digital input into a RoS
controllable robot. The first camera that was to be used in this project
was made by Orbbec. This camera was initially selected because it has
high quality sensors, and it was thought that an open source platform
would make developing a project from scratch easier than having to
overcome the inevitable software conflicts involved with using a sensor
with preloaded software, like the Kinect sensor made by Microsoft.

As far as the methodology was concerned for how the user\'s poses would
be recognized and converted into input for the robot, there were a few
ideas I was considering. The first idea came from a user named
[TanvirParhar](http://wiki.ros.org/TanvirParhar) who published a RoS
Wiki page, and package called
[neuro_gesture_kinect](http://wiki.ros.org/action/fullsearch/TanvirParhar/neuro_gesture_kinect?action=fullsearch&context=180&value=linkto:"TanvirParhar/neuro_gesture_kinect").
The concept of this package was to use a method of \"training\" the
camera to recognize certain gestures by giving the sensor a series of
the same gesture. This series would then be stored, and at runtime the
input being received from the user would then be compared against a
previously compiled log of gestures. If the user input matched one of
the gestures stored in the log then a move command would be sent to the
robot

The second approach was to use the reference frames that were generated
by the camera, and fixed to each of the user\'s joints, and compare the
change in these reference frames to the fixed coordinate axes on the
camera as a means of determining the user\'s joint/body position in
space relative to the camera. Based on the determined body position, if
the input matched the orientation of the reference frame for a given
pose, that was predefined in the program, then a move command would be
sent to the robot.

## Revision 1.0 - The Camera

After experimenting with the Orbbec sensor for a few weeks, and trying
to integrate the camera into the RoS framework it was determined that
the open source community did not have an effective means of tracking a
user\'s body movements or seamlessly integrating with the RoS
environment. At this point, the decision was made to use the Kinect v2.0
sensor from Microsoft as it natively comes with the ability to track a
user\'s joint position. The downside of this camera is that it is not
open source, so the opportunities for expanding or fine tuning the
sensor for this specific project were greatly limited. To track a user
within RoS, using the Kinect sensor, a package called
[openni_tracker](http://wiki.ros.org/action/fullsearch/openni_tracker?action=fullsearch&context=180&value=linkto:"openni_tracker")
was used. The documentation for this package is fairly straightforward,
and does not require any dependencies. This package is nice because once
the user is calibrated by the camera, the generated reference frames can
be visualized using
[rviz](http://wiki.ros.org/action/fullsearch/rviz?action=fullsearch&context=180&value=linkto:"rviz")
making the development process much easier since a lot of guess work was
taken out of the equation.

## Revision 1.1 - Pose Recognition

The initial approach for pose recognition was to use the RoS package
called
[neuro_gesture_kinect](http://wiki.ros.org/action/fullsearch/TanvirParhar/neuro_gesture_kinect?action=fullsearch&context=180&value=linkto:"TanvirParhar/neuro_gesture_kinect")
created by [TanvirParhar](http://wiki.ros.org/TanvirParhar). After
downloading the various dependencies for this package and struggling
with the limited documentation detailing how to implement the package I
determined that it was taking too much time to get the program to a
useable level and began thinking of other means to detect specific
gestures.

I first started with figuring out how the Kinect sensor was determining
the position and orientation of the user\'s joints in space. The
conclusion that I came to was that the camera sets itself as a fixed
reference frame, and everything else in the world that moves is fixed
spatially based on the movement relative to the Kinect. When the
[openni_tracker](http://wiki.ros.org/action/fullsearch/openni_tracker?action=fullsearch&context=180&value=linkto:"openni_tracker")
package prompts the user to calibrate using the Psi pose it is using
this preprogrammed pose as a reference point that the sensor is able to
recognize, and fix the positons of the user\'s joints in space. Once the
calibration is complete, any movement by the user are published to the
[tf](http://wiki.ros.org/action/fullsearch/tf?action=fullsearch&context=180&value=linkto:"tf")
node where the displacement and rotation of each of the joints, relative
to the sensor, can be seen. Using this information in conjunction with
visualizing the movement of each of the joint fixed coordinate systems
in
[rviz](http://wiki.ros.org/action/fullsearch/rviz?action=fullsearch&context=180&value=linkto:"rviz")
led me to the idea of finding a fixed joint position value in the /tf
node (AKA a gesture), and using a series of conditional statements to
determine if the user\'s body position fell within the predefined limits
for the values previously determined for a specific pose.

My initial idea when using the joint transformations was to determine if
a pose was being made by the user based on the rotation of the joints
relative to the sensor. For this approach I examined the change in
rotation for my right elbow. The challenge I ran into with this approach
is that the
[tf](http://wiki.ros.org/action/fullsearch/tf?action=fullsearch&context=180&value=linkto:"tf")
node uses a quaternion based reference frame rather than roll, pitch,
and yaw (RPY) to define the rotation of a joint in space. The reason for
this is to prevent a phenomena referred to as gimbal lock.
\"[Gimbal lock](https://en.wikipedia.org/wiki/Gimbal_lock) is the loss
of one degree of freedom in a three-dimensional, three-gimbal mechanism
that occurs when the axes of two of the three gimbals are driven into a
parallel configuration, \"locking\" the system into rotation in a
degenerate two-dimensional space (Gimbal Lock, Wikipedia).\" In order to
overcome this I converted from quaternion to RPY to make more sense of
the output.

After a week of testing this approach it was found that the rotational
reference frame of a given joint was different every time the program
was restarted. As a result of this, there was no way to accurately
determine whether or not the user was in fact issuing a gesture to the
sensor. For this reason using the rotational positon of a specific joint
in space would not have yielded the fine-tuned control that was required
of the autonomous vehicle during motor pool operations. The next
approach was to use the translation of a joint in space relative to the
sensor. For this method the position of a joint in space is resolved
based on its displacement from the calibration \"Psi pose\". Since the
\"Psi pose\" is used as the \"zero\" for all other joint positions
relative to the Kinect, the translational reference frame remains
constant between program instances and allows for predictable and
accurate joint position recognition

## Revision 1.2 - Dynamic Tracking

The design aspect for this project was to develop the ability to
dynamically track the user with the sensor mounted to the vehicle.
However, after a few weeks of research it was determined that I was
limited by the capabilities of the sensor that I was working with. Since
the Microsoft Kinect sensor defines its position in space as the origin,
and it requires the user to calibrate themselves to the camera before it
is able to locate and track their body movements. When the sensor is
mounted on a moving vehicle the Kinect is no longer able to determine
its position in space, and therefore it cannot maintain its lock on the
user. In order to overcome this problem I propose two possible
alternatives. The first is to use a different sensor that is capable of
dynamically updating its own position in space to redefine its origin,
and allow for a continual lock on the user\'s body orientation as both
the vehicle and the operator move through space. The second option is to
set up an array of stationary cameras in the motor pool that cross-talk
with each other to produce a 360 degree web in order to allow user
tracking within a specified area.

# Implementation

## Required Hardware

-   Kinect v2.0 Sensor
-   Turtle Bot

## Dependencies

It is expected that all of the listed dependencies should function
correctly prior to beginning this walkthrough. Follow the installation
tutorials on the linked RoS wiki pages for installation/implementation
assistance.

-   [openni_kinect](http://wiki.ros.org/action/fullsearch/openni_kinect?action=fullsearch&context=180&value=linkto:"openni_kinect")
-   [openni_tracker](http://wiki.ros.org/action/fullsearch/openni_tracker?action=fullsearch&context=180&value=linkto:"openni_tracker")
-   [turtlebot_bringup](http://wiki.ros.org/turtlebot_bringup)
-   [Tutorials](http://wiki.ros.org/turtlebot_bringup/Tutorials)
-   [TurtleBot Bringup](http://wiki.ros.org/action/fullsearch/turtlebot_bringup/Tutorials/indigo/TurtleBot%20Bringup?action=fullsearch&context=180&value=linkto:"turtlebot_bringup/Tutorials/indigo/TurtleBot+Bringup")
-   [rviz](http://wiki.ros.org/action/fullsearch/rviz?action=fullsearch&context=180&value=linkto:"rviz")
-   gesture.py (see link to my GitHub page for file)
-   GitHub: <https://github.com/GunnerPatterson/ROS-Kinect-Autonomy>
-   The most up to date version of Python
-   RoS (version: Indigo)

## Walkthrough

It is highly recommended to complete the first eleven lessons of the
beginner intro to RoS tutorial on the RoS wiki before following this
walkthrough. The reason behind this is that, in the essence of time, it
is assumed that the reader has a very basic understanding of how RoS
works, how to interact with RoS, and how each of the different
components (ex. publisher and listener) interface with each other to
send and receive data.

The following instructions for setting up the Kinect sensor come from
[TanvirParhar](http://wiki.ros.org/TanvirParhar) who outlined how he
installed all of the drivers for the Kinect sensor to make it work with
OpenNI.

### Setting up the Kinect Sensor

\"First of all download the suitable drivers from
[here](http://www.mira-project.org/downloads/3rdparty/bin-linux/). Start
by intalling the suitable OpenNI driver, preferably the latest one. The
OpenNI drivers are needed for the functioning of packages like
openni_launch and software like RTABMap, or libraries like PCL, etc.

Once the tar file is downloaded, go to the directory where it is
downloaded and uncompress it, by using:

```
$  tar -zxvf filename.tar.gz
``` or simply double-click it to open it with
Archive Manager. Then install the driver by:

```
$  sudo ./install.sh
``` Next Download the NITE middleware, form the
[same place](http://www.mira-project.org/downloads/3rdparty/bin-linux/).
Again uncompress it and install it.

```
$  tar -zxvf filename.tar.gz
$  sudo ./install.sh
``` Now, it\'s time to install the Openni_launch
for ROS. Simply type:

```
$  sudo apt-get install ros-<rosdistro>-openni-launch
``` At this point, to check everything is
installed, just connect the Kinect and type:

```
$  roslaunch openni_launch openni.launch
``` If the launch file runs, then all the drivers
are working fine.\"

### Downloading the Autonomy Script

For this portion, my gesture recognition script can be found on my
GitHub [page](https://github.com/GunnerPatterson/ROS-Kinect-Autonomy).
The script\'s name is \"gesture.py\". The other two scripts on the page
are: \"gesture_comment.py\" and \"quat_to_rpy.py\". The
\"gesture_comment.py\" script contains the same code as \"gesture.py\",
but it is fully commented to describe how everything works. The
\"quat_to_rpy.py\" script simply converts any outputs that are in
quaternion to the RPY frame. However, for the purposes of this
walkthrough this script will not be used.

Once the \"gesture.py\" script has been successfully installed, ensure
it is saved in the Source (/src) directory that within your catkin
workspace (/catkin_ws). For my instance, my /catkin_ws directory can be
found in the /home directory. To navigate to this file location and save
the python file in the /src folder, your command line path should look
somewhat similar to this:

```
$  cd home/catkin_ws/src/
``` Once the \"gesture.py\" script file is saved in
this directory it can now communicate with all of the other nodes within
RoS. \'\'\'It is imperative that this script is in this file location in
the catkin workspace source folder or else the python file will NOT be
able to interface with the Kinect sensor or the Turtle Bot.\'\'\'

### Putting Everything Together

The first step in bringing all of these pieces together in order to
control the Turtle Bot is to start roscore, to do this in the terminal
type:

```
$  roscore
``` Once roscore initializes successfully, open a
new terminal window and navigate to the location of the \"gesture.py\"
script, and run the script.

```
$  cd home/catkin_ws/src/
$  ./gesture.py
``` Once the script is up and running you will not
see any output from the python file for the time being until a user is
being tracked by openni_tracker. Before we can start tracking a user, we
first have to initialize and start the Turtle Bot. To do this,
physically turn on your Turtle Bot and plug it in to the computer. Then
open yet another terminal window and type:

```
$  roslaunch turtlebot_bringup minimal.launch
``` You should hear an audible noise come from the
Turtle Bot once it has been initialized. Now we are ready to start the
body tracking service to begin controlling the robot. To do this type:

```
$  rosrun openni_tracker openni_tracker
``` At this point position yourself in front of the
Kinect sensor, and wait until the program identifies a new user. Once a
new user has been identified, assume the
[Psi Pose](http://3.bp.blogspot.com/-t9FxKt9JUts/TWfK4juSF7I/AAAAAAAABBI/36-uvouIG7I/s320/PsiPose.gif)
to calibrate the Kinect sensor to your body. Hold this pose until the
program has successfully calibrated itself.

\'\'\'The body tracking will NOT work until you have successfully
calibrated the Kinect sensor. Also note that the python script will NOT
work if the user is not defined as USER 1. If a different user number is
assigned type CTRL + C in the terminal and enter the previous command
again until User 1 is defined as the current user.\'\'\'

#### How to Control the Robot

Once the calibration has completed place your arms down at your side.

-   To move the robot forward hold your right arm directly out to your
    side.
-   To move the robot backwards hold your left arm directly out to your
    side.
-   To turn the robot to the left hold your left arm directly above your
    head.
-   To turn the robot to the right hold your right arm directly above
    your head.
-   To stop moving the robot simply place your arms back down by your
    sides.

NOTE: The robot can only handle one gesture at a time, and will not
perform combined movements. The first gesture that is recognized is the
movement that will take place

### Vizualizing the Refrence Frames

. For this portion of the walkthrough close everything that was
previously running, and open a new terminal. An option to visualize the
different reference frames that are fixed to each of the user\'s joints
is to utilize a program called
[rviz](http://wiki.ros.org/action/fullsearch/rviz?action=fullsearch&context=180&value=linkto:"rviz").
Before starting the openni_tracker type:

```
$  sudo ./install.sh
```0 . This will start the rviz program. In order
to display the reference frames the user needs to be tracked by the
Kinect sensor. To do this start the openni_tracker service like we did
earlier when controlling the robot:

```
$  sudo ./install.sh
```1 Once you are being tracked by the sensor go in
to rviz (be careful to move out of view of the sensor) and add a /tf
window. This allows you to specifically track the outputs of the
transformation node (/tf). Then set the openni_depth_frame as the fixed
frame. This defines the sensor as the origin in space so that the
program knows where to generate the coordinate axes. At this point you
should see an array of reference frames that are labeled according to
their body part (the \"X\" axis is red, the \"Y\" axis is green, and the
\"Z\" axis is blue).

Another option is to output the data of the /tf node to show the
numerical values for the position and rotation of each of the reference
frames. To do this type in a new terminal window:

```
$  sudo ./install.sh
```2 . The output from this command shows the
numerical orientations of all of the different joint reference frames as
the body parts move through space.

# Conclusion

## Accomplishments

The primary objective of this independent study was to develop a system
that allows a user to control an autonomous vehicle through the use of
hand and arm signals. Throughout the course of this project I was able
to develop the ability to control a Turtle Bot running the Ros operating
system by using motion capture technology. However, the ability to mount
the sensor on the robot and dynamically track the user was not achieved
in this project.

## Future of the Project

Upon completion of this project, an analysis was done to determine the
practicality of continuing development. In order to determine if this
independent study was worthwhile the user needed to be able to maintain
consistent and predictable control over the robot. The learning curve to
physically control the robot also needed to be short and straightforward
in order to limit the amount of time and money required to implement
this system in an operational environment. After controlling the robot
myself and becoming very familiar with its capabilities it is was
determined that maintaining consistent and predictable control was not
an issue. Additionally, while at West Point\'s Projects Day I had the
opportunity to teach a group of middle schoolers how to control the
robot. Within, five minutes of my instruction all of the kids were
easily maneuvering the robot without any additional help. This served as
a proof of concept for the ease of use of the system.

The program could primarily be improved to dynamically track a user,
rather than requiring the user to remain in a fixed area in front of a
stationary camera. This would provide better freedom of maneuver for the
system as well less constraints as to where this system could be
implemented. This program could be expanded by testing its functionality
on multiple different kinds of autonomous vehicles, with different
steering configurations to determine if there are any other further
limitations to the system. Overall, there is room for expansion and
further development within this area of study. However, I believe that
this project could serve a potential easy solution to a overlooked and
underappreciated problem that will only become more prevalent as our
military progresses technologically.
