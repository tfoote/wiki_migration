## API Stability

This package is in an **experimental** stage.

## System Dependencies

Python and ROS need to be installed on your system. This package has
been tested under Python 2.7 under ROS fuerte, Ubuntu precise.

## Installing the robot_script Package

Check out the robot_script package, and `rosmake` to ready the package
for operation. Currently installation is via checkout from Github:


```
git clone https://github.com/paepcke-willow-garage/robot_script.git
cd robot_script
rosmake
```

 To get the latest version after you've already
installed the facility, type the following into a terminal window after
switching to `robot_script` directory: 

```
git pull
rosmake
```



An apt-get package is in the works.

## Example

The following code snippet checks whether the head tilt joint is roughly
at 30 degrees. If so, the head is pointed such that pan is -100 degrees,
tilt is at -20. The head will take 5 seconds to reach its destination.
The statement following this conditional will proceed immediately, not
awaiting the head's motion to complete:



```
if aboutEq('head_tilt_joint', 30):
    pr2.lookAt(-100, -20 , 5, wait=False)
else:
    pr2.lookAt(+100, +30 , 5, wait=False)
```



The next line moves the robot 30cm straight forward, maintaining a zero
rotation of its body. The parameters are x (forward/back), y
(left/right), and body rotation (degrees):

`pr2.moveBase(place=(0.3,0.0,0.0))`

## Command List

Here is a complete list of commands. Details in the following section.

-   `pr2.openGripper(side)`
-   `pr2.closeGripper(side)`
-   `pr2.tiltHead(degreesTilt, duration=1.0, wait=True)`:
-   `pr2.rotateHead(degreesPan, duration=1.0, wait=True)`
-   `pr2.lookAt(degreesPan, degreesTilt, duration=1.0, wait=True)`
-   `pr2.moveArmJoint(jointName, newAngle, duration=2.0, wait=True)`
-   `pr2.moveArmJoint([jointName1, jointName2, ...],[newAngle1, newAngle2, ...],duration=2.0, wait=True)`
-   `pr2.moveBase(place=(x,y,z), rotation=deg, duration=3)`
-   `pr2.getSensorReading(sensorName)`
-   `pr2.aboutEq(jointName, value)`
-   `pr2.setTorso(height, duration=10.0, wait=True)`
-   `pr2.pause(seconds)`

**Advanced: Motion Methods:**

-   `myMotion = Motion(aMotionFunction)`
-   `motion.start(anyArgsThatTheMotionFunctionTakes)`
-   `motion.pause()`
-   `motion.resume()`
-   `motion.stop()`
-   `motion.sleep_while_running()`
-   `motion.is_done()`

**Advanced: EventSimulator Methods:**

-   `start(schedule, callbackFunction, repeat=False)`
-   `getEventQueue()`
-   `stop()`

## Detail Statement Definitions

For all definitions we assume that the script includes the following
head statements:



```
from robot_scripting import PR2RobotScript as pr2
from robot_scripting import aboutEq
from robot_scripting import FullPose

# When a function takes a parameter called 'side',
# use LEFT, RIGHT, or BOTH:

LEFT  = pr2.LEFT
RIGHT = pr2.RIGHT
BOTH  = pr2.BOTH
```



### Gripper and Head

`pr2.openGripper(side)` Opens one or both robot grippers all the way.
`pr2.closeGripper(side)` Closes one or both robot grippers all the way.
`pr2.tiltHead(degreesTilt, duration=1.0, wait=True)`: Tilts the head
forward or back. Range is 60 to -30 degrees
`pr2.rotateHead(degreesPan, duration=1.0, wait=True)` Pans the head from
side to side. Range is 180 to -180.
`pr2.lookAt(degreesPan, degreesTilt, duration=1.0, wait=True)` Combines
pan and tilt into one smooth motion.

### Moving the arm joints one at a time, or together

`pr2.moveArmJoint(jointName, newAngle, duration=2.0, wait=True)` or:
`pr2.moveArmJoint([jointName1, jointName2, ...],[newAngle1, newAngle2, ...],duration=2.0, wait=True)`
Notice that the first form names one joint, and one angle. The second
form allows for multiple joints and their angles to be named together
for one smooth motion.

The joints and their legal ranges are:

-   l_shoulder_pan_joint (-130 to 40 deg) or r_shoulder_pan_joint (40 to
    -130 deg)
-   l_shoulder_lift_joint or r_shoulder_lift_joint (80 to -130 deg)
-   l_upper_arm_roll_joint(-224 to 44 deg) or r_upper_arm_roll_joint (44
    to -224 deg)
-   l_elbow_flex_joint or r_elbow_flex_joint (133 to 0 deg)
-   l_forearm_roll_joint or r_forearm_roll_joint (continuous)
-   l_wrist_flex_joint or r_wrist_flex_joint (130 to 0 deg)
-   l_wrist_roll_joint or r_wrist_roll_joint (continuous)

### Moving the whole robot (the base)

Scripts can move the robot's body (also called its `base`) to a
place, and rotate its body at the same time:

-   `pr2.moveBase(place=(x,y,z), rotation=deg, duration=3)` For the PR2
    robot the z axis is always zero. But for ROS controlled aircraft
    this dimension is required.

### Reading joint values

It is often useful to check the angle of a joint. This information is
obtained by the command:

-   `pr2.getSensorReading(sensorName)` In the future, sensors other than
    joints may be added.

When setting a robot joint to a specific value, such as 30 degrees, the
mechanics often do not zero in on that precise angle. Instead a joint
sensor might read 30.05, or 29.9. In order to allow for these
inaccuracies when checking a joint angle, use the following command in
your conditional statements:

-   aboutEq(jointName, value) Example: 

```
if aboutEq('head_pan_joint', 60):
    do one thing
else:
    do another thing
```



Currently recognized joint names: 'base', 'bl_caster_l_wheel_joint',
'bl_caster_rotation_joint', 'bl_caster_r_wheel_joint',
'br_caster_l_wheel_joint', 'br_caster_rotation_joint',
'br_caster_r_wheel_joint', 'fl_caster_l_wheel_joint',
'fl_caster_rotation_joint', 'fl_caster_r_wheel_joint',
'fr_caster_l_wheel_joint', 'fr_caster_rotation_joint',
'fr_caster_r_wheel_joint', 'head_pan_joint', 'head_tilt_joint',
'laser_tilt_mount_joint', 'l_elbow_flex_joint',
'l_forearm_roll_joint', 'l_gripper_joint',
'l_gripper_l_finger_joint', 'l_gripper_l_finger_tip_joint',
'l_gripper_motor_screw_joint', 'l_gripper_motor_slider_joint'
'l_gripper_r_finger_joint', 'l_gripper_r_finger_tip_joint',
'l_shoulder_lift_joint', 'l_shoulder_pan_joint',
'l_upper_arm_roll_joint', 'l_wrist_flex_joint',
'l_wrist_roll_joint', 'r_elbow_flex_joint',
'r_forearm_roll_joint', 'r_gripper_joint',
'r_gripper_l_finger_joint', 'r_gripper_l_finger_tip_joint',
'r_gripper_motor_screw_joint', 'r_gripper_motor_slider_joint',
'r_gripper_r_finger_joint', 'r_gripper_r_finger_tip_joint',
'r_shoulder_lift_joint', 'r_shoulder_pan_joint',
'r_upper_arm_roll_joint', 'r_wrist_flex_joint',
'r_wrist_roll_joint', 'torso_lift_joint',
'torso_lift_motor_screw_joint'.

For legal values of these joints, see
[the PR2 manual](http://pr2support.willowgarage.com/wiki/PR2%20Manual/Chapter8#Joint_Limits_and_Types).
As mentioned in examples, all `robot_script` angles are expressed in
degrees, all distances in meters. Both units may be positive or
negative.

### Raising/lowering the torso

-   `pr2.setTorso(height, duration=10.0, wait=True)` The PR2's torso
    can range from 0.3 meters (30cm) to 0 meters.

### Temporarily pausing execution

-   `pr2.pause(seconds)`

### More examples

-   `pr2.tiltHead(15 + pr2.getSensorReading("head_tilt_joint"), 1)`
    Raise the head tilt to 15 degrees above where it currently points.
    Take one second to do it.

```{=html}
<!-- -->
```
-   `joints = ['l_shoulder_lift_joint', 'l_forearm_roll_joint', 'l_wrist_flex_joint']`
    `   values = [-70, -90, -70]`
    `  pr2.moveArmJoint(joints, values, duration=2.0, wait=False)`

## Advanced Facilities

A script function will often cause the robot to run through some
sequence of gestures. Maybe the function makes the robot's right arm
wave. The function might be written to have the robot wave twice, and
then stop, the function returning after the waving is done. Or the
function might be written to have the robot wave continuously.

### Running Multiple Functions in Parallel

What if you want the robot to not only wave, but also to rotate from
side to side, as if taking in a big crowd, and you have a second
function that causes the robot to do just that? You want the waving
function and the rotate function to run at the same time.

You accomplish this parallelism by creating `Motion` objects from the
waving and the rotating functions. Like this:

A script function will often cause the robot to run through some
sequence of gestures. Maybe the function makes the robot's right arm
wave. The function might be written to have the robot wave twice, and
then stop, the function returning after the waving is done. Or the
function might be written to have the robot wave continuously.


```
from robot_scripting import Motion

    def waverFunc(motion):
       # make the waving happen

    def rotatorFunc(motion):
       # make the rotating back and forth happen

    myWaver   = Motion(waverFunc)
    myRotator = Motion(rotatorFunc)
```



Notice that part of creating a Motion object is to specify the function
that accomplishes the respective motion. A motion function needs to
ensure just one condition: it must accept at least one argument, the
motion object itself. We will see shortly why it is useful for motion
functions to have a hold of the motion objects that call them.

Once you defined the motion objects, you can start, pause, resume, and
stop them. Like this:



```
myRotator.start()
    myRotator.pause()
    myRotator.resume()
    myRotator.stop()
```



You may define motion functions that take more than the obligatory first
argument. For example, you might want to define the waving function like
this:



```
def waverFunc(motion, howOften):
        for i in range(howOften):
            # make the waving happen
```



Then, to start the waving motion:



```
myWaver.start(4) # wave four times
```



Notice that you don't pass the motion object to `myWaver`'s
`start()` method. Within a motion function you can call any of the
robot_script motions you like. But if you wish to do nothing for a
while, do it like this:



```
motion.sleep_while_running(numOfSeconds)
```



That is, don't call the Python sleep function. The reason is that the
special sleep_while_running() method of the Motion class ensures that
you can stop your motion function at any time. The use of this sleeping
method is the reason why all motion functions take their Motion object
as first argument.

If you wish to learn whether a motion function has finished its work,
you can use



```
git pull
rosmake
```

0 That method on the Motion class returns True
or False. Of course, you write a motion function as an infinite loop,
like 'wave forever,' then `motion.is_done()` will never turn True.

If you sometimes want to use the business part of a motion function as
the work horse of some part of your script, and sometimes as part of a
parallel motion, the best idiom is to 'factor out' the common
capability:



```
git pull
rosmake
```

1

Sometimes it is necessary that a script is notified when some event
occurs. For example, a separate program may be using the robot's camera
to find human faces in its surroundings. The script is to take some
action, like wave its arm, whenever a face is found. How can the face
finding program 'talk' to the script?

The answer is `robot_script`'s `EventSimulator` class. This
facility can be used to debug a script by creating events, and
delivering them to the script at specified times. Or the facility can be
combined with the actual event-producing program, and function as the
bridge between that program, and the script. This combination is
accomplished by an expert user, who will subclass `EventSimulator`.
The code contains instructions.

### Receiving Events from an EventSimulator or Sensors

The script may receive event notifications by one of two means. The
event simulator can call one of the script functions when an event
occurs. That function is the script's *callback function.* That
function implements the robot reaction to the event. This mechnism works
well when the reaction to the events are of short duration. Here is a
schematic of what happens. The green part is the only area end users
needs to worry about. Their script is a collection of functions that may
call each other. One of the functions (the middle one in the picture),
functions as an event handler. This function is called by 'the system'
whenever an event occurs, and it might call the other script functions.
We'll see soon how a function is made into a handler function.

![](attachment:synchronousEvents.png)

The handler function reacts to the event, and then returns. Notice the
infinite loop at the bottom of the Method-1 picture. The loop does
nothing. In fact, the entire script does nothing, unless an event
occurs! But note as well that while the handler function processes the
call from the event system, no new events can be attended to. Events
from sensors may even be lost.

When events take longer to handle, or when many events arrive in bursts,
it is better to use the second event delivery channel: a queue. Every
event simulator provides a data queue. When the simulator calls the
script's callback function, that function may **return** any
information that might be needed when the event is *eventually* handled
by other parts of the script. For example, the callback function might
record the time when the event occurred. The simulator will place the
returned value into its data queue, where the script may pick it up in
its main loop at any time. If many events occur in quick succession,
they are all added to the queue. Python queues allow a script to pause
until an event appears in the queue. The Method-2 picture below shows
the principle.

![](attachment:asynchronousEvents.png)

As in Method-1, the event handler function is called by the system when
an event occurs. However, in this case the handler function computes a
(hopefully) quick piece of information, and returns that information.
The event system stuffs that returned information into the data queue.
Notice that the event loop is now different, in that it listens at the
end of the queue for new information to arrive from the yellow portion
of the diagram. Once such information arrives (i.e. the information that
the handler function returned), then the main loop might call various
script functions to process the event. With this way of organizing the
workings of your script, new events are captured and added to the data
queue even while a previous event is processed.

Here is the logic of a silly example in which the camera captures a
piece of text on a nearby wall, a direction sign, maybe. The simulator
delivers the text to a script, which prints out the words in all upper
case. In the first delivery method, the callback function immediately
prints out the upper-cased text, and returns nothing to the simulator.

In contrast, using the second method, the callback function performs the
case conversion, but does not print out the result. Instead, the
function returns the result to the simulator. The simulator places the
newly upper cased text in its out queue. When the script services the
queue, it finds the word, and prints it.

Here is the code, which assumes the existence of the fictitious
WordFinder. We will do a runnable example in a moment.



```
git pull
rosmake
```

2 The above code defines a callback function,
`printWord()`, which prints the word it receives. Then the script
enters a sleep loop. Whenever the independently running WordFinder
discovers a word, it calls the script's `printWord()` function.

Here is the same example using the second event delivery method:


```
git pull
rosmake
```

3 The code above again first defines a callback
function. In this case, however, the callback function returns the
upper-cased word. The script then creates the WordFinder instance, and
starts it, passing the callback function. The `get()` method on the
Queue instance hangs until a word is available. In this example, a
timeout is added to the `get()` call. This exit hatch is optional.

### Scheduling EventSimulator Events

Say you don't have a fancy word or face finder. Or you will have one in
the future, but want to debug the robot reactions to the discovery
events. You can create a very simple schedule that the EventSimulator
will work through. A schedule is an OrderedDict, a Python data structure
that is just like a Python dictionary, but remembers the order in which
items were added. Let's simulate the word finder. Here is the code:


```
git pull
rosmake
```

4 The schedule's keys are floating point
numbers that indicate the number of seconds after the script's start
when the respective event is to be triggered. When the event is
triggered, the EventSimulator will invoke the callback function with the
value of the schedule entry. For instance, at 2 seconds after the script
starts, the EventSimulator will call `printWord('This')`. At 5
seconds after the script start, the call `printWord('is')` will be
made, and so on. The keys in the schedule must be numbers in seconds.
But the corresponding values may be any Python datastructure. Whatever
is there will be the parameter to the `printWord()` call.

Here are the methods on the `EventSimulator` class:

`start(schedule, callbackFunction, repeat=False)` The `repeat`
parameter allows a script to specify that the EventSimulator is to run
through the schedule over and over again. `getEventQueue()` Return the
EventSimulator's event queue. `stop()` Stop the EventSimulator.
