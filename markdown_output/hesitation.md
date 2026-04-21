## Description

The main application for this package is to be used with a robotic arm,
such as in the PR2 or the WAM, where the published points represent the
position of the end effector at different timesteps.

Four types of end-effector trajectories are currently implemented in the
package:

-   Reach-and-retract: Moves from one point to another following a
    quintic Hermite expression of humanlike motion;
-   Robotic avoidance (RA): If collision is detected, abruptly stops and
    rests on the same position for some amount of time, then returns to
    the original point;
-   R-type hesitation: If collision is detected, follows an AHP-based
    hesitation gesture and immediately returns to the original point;
-   P-type hesitation: If collision is detected, follows an AHP-based
    hesitation gesture and jerkily dwells for some instants, expressing
    persistance. The duration of the persistance is set by the user with
    a parameter defined as mode. If the resource becomes available
    before the persistance ends, it will try to reach the destination
    point again.

This package uses ROS standard data type geometric_msgs/Point and
publishes reference trajectory points to the topic /traj_points.

Current version of this package only produces 2D motion (XZ plane with X
assumed to be the dominant axis that goes through the initial and target
position).

This package has been successfully tested in ROS Electric and Fuerte. It
may not work with previous versions of ROS.

## Usage

Make sure that roscore is running; if it is not, launch one.



```
$ roscore
```



Build the package in your machine.



```
$ rosbuild --pre-clean hesitation
```

 or



```
$ make
```



Type the following command to launch the necessary servers.



```
$ roslaunch hesitation hesitation_ready.launch
```



Now you are ready to launch the trajectory generator. Open a new
terminal. Usage is:



```
$ rosrun hesitation trajectory_generator [frequency] [xi] [yi] [zi] [xf] [yf] [zf] [mode]
```



where each argument is described below:

-   frequency: the frequency on which the points are being sent to the
    topic (Hz)
-   xi, yi, zi: initial Cartesian position (meters)
-   xf, yf, zf: final Cartesian position (meters)
-   mode: type of motion to follow if collision detected: -2 for short
    robotic avoidance; -1 for long robotic avoidance; 0 for R-type
    hesitation; 1 to 9 for P-type with 1-9 loops.

The difference between short RA and long RA is the amount of time spent
at the collision point when it is detected. Short RA remains at the same
position for only half the time compared to long RA.

Note that since only XZ motion is currently available, the \[yf\]
parameter is not used, so it can take any value. But \[yi\] is defined
as the Y-plane coordinate on space and should be a valid parameter.

An example of launching the generator with valid parameters and to
follow a P-type motion is provided below:



```
$ rosrun hesitation trajectory_generator 100 0.6 -0.3 0.2 1.0 -0.3 0.1 1
```



The output should look like this:



```
[ INFO] [1348784846.143523089]: Z-axis motion follows: -1.840170x^2 +2.694272x + -0.754102 
[ INFO] [1348784846.144614183]: a: 0.256600, b: 0.633975, vel: 0.111111, pos: 0.626795 
[ INFO] [1348784846.145699819]: Coefficients successfully calculated. 
[ INFO] [1348784846.145818661]: tf:0.564237; pos:0.702885; 0.319977x^5 + -0.451358x^4 + 0.000000x^3 + 0.128300x^2 +0.111111x + 0.626795 
[ INFO] [1348784846.145844513]: tf:0.608616; pos:0.720966; -0.159351x^5 + 0.242459x^4 + 0.000000x^3 + -0.159092x^2 +0.093737x + 0.702885 
[ INFO] [1348784846.146816742]: Coefficients for p-type successfully calculated. 
[ INFO] [1348784846.146941125]: tf:0.564237; pos:0.728416; 0.051196x^5 + -0.072217x^4 + 0.000000x^3 + 0.020528x^2 +0.009405x + 0.720966 
[ INFO] [1348784846.146984776]: tf:0.608616; pos:0.726213; -0.025496x^5 + 0.038793x^4 + 0.000000x^3 + -0.025455x^2 +0.006625x + 0.728416 
[ INFO] [1348784848.673912967, 9715.371000000]: Spline 1 called 
[ INFO] [1348784849.101139962, 9716.176000000]: Going for reach 
[ INFO] [1348784850.633578156, 9718.588000000]: Retracting 
[ INFO] [1348784852.685514142, 9721.833000000]: Dwelling
```



To verify that the trajectory is being correctly generated, you can use
rxplot. In another terminal, type



```
$ rxplot /traj_points/x /traj_points/z
```



A new window should be opened, showing the format of X-axis and Z-axis
trajectories in function of time.

The default setting is reach-and-retract trajectory. To change it to
hesitation (depending on the mode value set), the /collision_topic must
be activated. For simulation purposes, a talker node can be used as
following:



```
$ rosrun hesitation collision_talker [0 or 1] [freq]
```



where:

-   0 or 1 define if there is collision (1) or not (0) happening;
-   freq is the frequency of sending messages from collision_talker to
    trajectory_generator (Hz)

Note: collision_talker is a dummy program that can simulate the
sensoring in the resource. For real applications, this node should be
replaced by a sensor reading giving a boolean output.

As an example, you can launch



```
$ rosrun hesitation collision_talker 1 1
```



That will inform the generator that collision has been detected and it
will keep sending these messages each second. Make sure that it gets
called at least twice -- after launching it once and seeing as output



```
$ rosbuild --pre-clean hesitation
```

0

you can Ctrl+C and stop the talker. The motion should switch from
reach-and-retract to hesitation.
