## Motivation

There are two main motivations for this manipulation research:
developing behavior-based tabletop manipulation techniques and utilizing
arm perceptual data for abnormality or collision detection.

### Behavior-based Manipulation

For most human-robot interaction (HRI) applications, it is important to
have predictable behavior. Not only does this make HRI research more
safe, but it is also more comforting to naive users. In addition,
repeatable behavior can be more precisely characterized. While arm
planning has made significant advancements in recent years, it is far
from a mature science. Planning-based manipulation often demonstrates
unpredictable behavior such as grasping objects using strange motions,
while behavior-based approaches will move reliably to their predefined
goals. Also, these motions can more easily integrated into larger design
applications since their parameters are easily understandable. When
adding manipulation to a suite of other robot actions, developers can
use those motions naively knowing the conditions under which they
succeed.

The complexity of planning also generates issues. While calculating
plans in task space is now relatively quick, computing plans for many
different object grasps can multiply the time requirements, making the
manipulation much slower. Also, planning algorithms often consume a
large percentage of system resources, leaving less room for simultaneous
processes. Furthermore, planning is sometimes not complete, often
reporting unwarranted failure due to sensor noise or mis-calibration.
This utility attempts to sidestep all of the problems associated with
planning by exploiting a generally applicable property of tabletop
manipulation, that the object is cleared for grasping above. Our
technique is designed to be a faster and lighter behavior-based response
to tabletop manipulation and was inspired by the research presented in
Advait Jain and Charles C. Kemp's "EL-E: An Assistive Mobile
Manipulator that Autonomously Fetches Objects from Flat Surfaces".

### Robotic Arm Perception

While there has been much research into using specific sensors like
vision or pressure sensors to prevent environmental collisions, it is
just as important to detect them when they occur. Collision detection
can be used both in safety assurance to avoid damaging itself or the
environment, or as a tool to achieve the specified goals. This package
primarily does the latter, exploiting the fact that during an overhead
grasp, the gripper must either collide with the object in the palm of
the gripper, or the table, in which case the object is between the
fingertips. Functionality also exists which attempts to differentiate
between desired collisions and unexpected abnormalities by supplying an
expected z-collision goal. This domain is well suited for collision
detection by nature of the parameterization of the arm trajectories. The
actions are crafted in such a way that expected perceptions should be
similar to nearby grasps in the overhead grasping space. In this much
smaller and smoother space, clean grasps can be sampled and compared to
perception monitored in real-time.

## Grasping Details

[Youtube](https://www.youtube.com/watch?v=http://www.youtube.com/watch?v=fUDIk505lVo)

### Grasping

The overhead grasping process requires only three inputs, the x-y
location on the table, and the gripper z-orientation. When called, the
arm moves to the grasp configuration at a predefined height and moves
directly down using interpolated IK. The IK calls are biased to prefer
joint angles which keep the elbows up and away from the table. Motion
continues for 30cm or until a collision is detected. It is assumed that
when a collision is detected, the gripper has collided with either the
object or the table. The gripper then closes on the object, and lifts
the object back to its initial grasping position.

### Vision

The [tabletop_object_detector](tabletop_object_detector) package is
interfaced to detect objects and the
[object_manipulator](object_manipulator) package is used to find their
pose. When grasping the closest object to a point, the poses of all the
objects on the table are found, the closest x-y object is selected, and
the rotation is found by aligning the gripper with the z-rotation of the
bounding box. The box is identified by projecting the object's point
cloud into the table and using PCA to find the major and minor axis and
the minimum and maximum points along these directions to find the edges.
The robot is blind for the remainder of the grasp.

### Collision Detection

Collisions are detected by monitoring almost every arm sensor available:
the accelerometer in the gripper, the joint angles, joint velocities,
joint efforts, fingertip pressures, and the FK pose of the gripper.
Abnormalities are detected by collecting grasp data over the space of
overhead grasp configurations. For each x-y-rotation configuration
region, nearby sensor data is processed to find expected sensor values
and the variance of those values at each time step along the grasp
trajectory. When monitoring an actual grasp, a z-test is performed for
each sensor value at each time step to determine the probability this
sensor value was sampled from the expected sensor data. An abnormality
is reported when the joint probability of all of the sensor streams
following the model (with a naive independence assumption) falls below a
threshold. This approach is similar to Peter Pastor et. al.'s failure
condition detection described in "Skill Learning and Performance
Prediction for Manipulation", accepted for publication in the
proceedings of the 2011 International Conference on Robotics and
Automation. While their technique uses single z-tests over each
coordinate, this method uses a joint probability over all coordinates
simultaneously.

### Laser Control

The [laser_interface](laser_interface) package offers functionality that
allows users to point and click at locations in the world using a laser
pointer "mouse" so that users can naturally direct the robot to
perform actions at those places. This grasping package contains a demo
which allows users to control tabletop manipulation using only the laser
pointer. By pointing at an object on a table and double-clicking, the
PR2 will grasp the closest object. When the object is in hand,
double-clicking on a point on the table will place the object at that
location. Also, double-clicking on a point away and above the table (at
a person, ideally) will have the robot hand the object to the person.
The pressure sensors are monitored to determine when to release the
object.

## Collecting Data

To monitor sensor data, model sensor data must first be collected. These
two commands will first, collect grasp data by trying a series of grasps
over the desired sampling space, and second, process the data gathered.


```
rosrun pr2_overhead_grasping overhead_grasping.py --cdata
rosrun pr2_overhead_grasping overhead_grasping.py --pdata
```

 The first command requires robot supervision as
it will be moving the entire time. The second command can be run
overnight. Both of these commands can take several hours depending on
the size of the grasping space established by the parameters. Currently,
all parameters for the grasping package are set at the top of
overhead_grasping.py.

## Running the Demos

Before running the demos, the pipeline must be launched which runs
helper nodes used by the main node. Run this launch file in the
background before running the demos: 

```
roslaunch pr2_overhead_grasping simple_grasp_pipeline.launch
```

 There are
currently three modes of grasping demonstration.


```
rosrun pr2_overhead_grasping overhead_grasping.py --randgrasp
rosrun pr2_overhead_grasping overhead_grasping.py --visiongrasp
rosrun pr2_overhead_grasping overhead_grasping.py --lasergrasp
```

 The first mode tries random grasp motions in
its sampled space repeatedly so that the sensitivity and different grasp
patterns can be quickly evaluated. The second mode uses vision to grasp
the object closest to a point near the middle of the table. After
grasping the object, it places it in a random location. The third mode
is laser controlled. Refer to the [laser_interface](laser_interface)
documentation on how to get the laser pointing started (the launch file
and user interface in this package must be called separately).
