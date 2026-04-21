[Youtube](https://www.youtube.com/watch?v=Ge-lT_kD2OE)

## Hardware

*Information on the wouse hardware can be found [here](/hardware).*

## Concept

### Wincing as an Accessible Run-stop Gesture

One challenge in making assistive robots safe for persons with severe
motor impairments is the decreased ability of these users to escape a
robot malfunction or activate a traditional run-stop. Wincing (closing
the eyes quickly and tightly) may provide a recognizable signal over
which many motor-impaired persons retain voluntary control. In addition,
wincing is a natural reaction to unpleasant stimuli (i.e. pain, sudden
fear, etc.) which would normally indicate for the activation of a
run-stop when interacting with a robot. Together, this suggests that
wincing may be well suited to serving as a run-stop activation signal
for users with severe motor impairments.

### Wearable Wince-detection

The use of wincing as an accessible run-stop gesture requires a method
of wince detection which is usable by motor-impaired persons. Many
different methods may be possible, including EEG, EMG, EOG
(Electrooculogram), or wearable cameras. However, with the exception of
cameras, these techniques typically require prepared electrical contacts
on the skin, and are non-trivial to don/doff. In an attempt to overcome
these challenges, we have developed a prototype wearable wince-detection
system, called the wouse.

### The Wouse Device

The wouse (from "wince mouse") is, most basically, the
position-tracking components of an optical mouse mounted inside the
temple of a pair of safety goggles. By placing the optical sensor near
the skin of the temple, just behind the corner of the eye, the sensor
reports the movement of the skin. This region of the skin tends to move
very little, except for being pulled forward when the eyes are closed
tightly (as in wincing and other similar facial expressions.) To report
skin movement consistently and accurately, the device must be properly
fitted to the user, so that the mouse portion does not move with the
skin, but is still close enough to detect motion.

### Data Processing

The wouse software uses a 2-class Support Vector Machine to discriminate
mouse movement representative of wincing from the motions caused by
other facial expressions or the external mechanical manipulations of the
face seen during self-care tasks such as shaving or wiping. Training
data is collected (preferably from the desired user) using a training
script, and the filtered, normalized and used to train the SVM
classifier. When running, the wouse filters and normalizes incoming data
before classifying motions as wincing or non-wincing. If a wince is
detected, a signal is sent to place the robot in a low-power run-stopped
mode.

## Software

### Install/Setup

1\. Check out the latest version of the wouse ROS package (from link
above).

2\. As the superuser, run the provided script for adding a udev rule for
the wouse. (This assumes you are using a swiftpoint SM300, if this is
not the case, you will need to write your own rule, using the provided
script as a template). ```
roscd wouse/scripts/
sudo ./setup.sh
``` 3. Plug the wouse USB
connector into the computer. Run: ```
sudo cat /dev/wouse
``` and move the
wouse against a surface (so that the mouse can sense movement). Garbage
output should appear in the terminal.

This script should only need to be run once. Afterwards, the computer
should not treat the wouse as a normal mouse (it cannot click or
accidentally move the cursor), and the ROS nodes should be able to
access the device file (required to read movement data) without being
run as the superuser (which is both inconvenient and dangerous).

Properly using the wouse requires a series of steps. The following
assumes you have the most recent version of the ROS package (see Source
link at top of page), and have working wouse hardware (see previous
section).

### Providing training data

The wouse software uses a Support Vector Machine (SVM) classifier to
discriminate between wincing and non-wincing motions recognized by the
mouse. To do this properly, the SVM must be trained. This is best done
with data from the desired end user, as this will help to account for
variations in facial movement and structure, different hardware designs,
and the preferred seating of the glasses, among other sources of
variability. Training involves collecting labelled examples of wincing
and non-wincing movements.

A script is provided which selects at random from a series of
expressions and actions (Fear, Surprise, Sadness, Joy, Disgust, Anger,
Head Shaking, Head Nodding, and Wincing). Each action/expression will be
printed to a terminal, and the user should perform that action or assume
that expression for the duration it is displayed on the screen, before
moving on to the next expression. This script can be run with:
```
rosrun wouse train.py filename -l ### -d ##
```

-   *filename* is the **required** filename in which to store collected
    data. This is a .csv file in *wouse/data*/

```{=html}
<!-- -->
```
-   The *-l* arg is the total length (duration) in seconds of the
    training session (*-l 600* runs for 10 minutes).

```{=html}
<!-- -->
```
-   The *-d* arg is the duration in seconds to spend in each expression
    (*-t 3.5* gives a new expression every 3.5 seconds).

Multiple sessions run with the same filename will append new data so
that data collection can be performed in multiple sessions. Delete old
files if you wish to write over the contained data.

### Pre-processing Training Data

The training data needs to be processed into the feature vectors of
interest. Currently this is performed by *wouse/scripts/data_parser.py*
which takes any number of data files' filenames as inputs. In the data
processing, mouse movements with a Euclidean magnitude < 2.5 are
ignored. This seems to be the significant majority of the data produced
by the wouse, which is also typically uninformative noise. Subsequently,
a feature vector is produced for each of the remaining points,
consisting of the instantaneous magnitude and direction of that mouse
event, in addition to the (inclusive) number of events in the preceding
250ms (a measure of the rate of event occurrence), the total magnitude,
and average direction of events in this window. This produces a 5-vector
descriptor. Each descriptor is saved in a list, along with a list of
matching labels (wince or not-wince).

### Using the Wouse

The complete wouse system, when running, consists of three ROS nodes:
two on the machine which the wouse in plugged in to, and one on the
robot itself. The first node on the local (wouse) machine reads the
mouse data from a linux device file and published a
geometry_msgs/Vector3Stamped with the data. This data is received (on
the same machine) by the second node (*wouse.py*), which normalizes the
data and classifies the event as a wince or non-wince. If a wince is
detected, it makes a service call to the node on the robot, which
engages the 'run-stop' behaviour. The *wouse.py* node on the local
machine also maintains a regular 'heartbeat' of service calls to the
*run_stop_server.py* node on the robot. Currently, if this signal is
lost, the robot beeps every 10s, but does not run-stop the robot.

Each of the 'moving parts' in the system have been abstracted apart
for easier development and research. In a 'production' system, each of
these functions should likely be condensed into a single node inside the
real-time framework of the robot, which will enable significantly
stronger guarantees on operation, and easily halt the robot if failures
occur.

To actually use the wouse with a PR2, **on the robot**, first run:
```
rosrun wouse run_stop_server.py
```

This will bring up the node which communicates with the power-board
node, and is responsible for run-stopping the robot.

Then, **on the machine with the wouse**, run: ```
roslaunch wouse wouse.launch
```

This will launch both the local nodes. The *wouse.py* will read in the
formatted training data from the specified pickle file, and trains an
SVM classifier (using the scikit-learn library). The pickle file should
be specified using the args in */wouse/launch/wouse.launch*. This file
will issue a warning and exit if it fails to find the run-stop service
of the run_stop_server on the robot (above), which should be started
first, for this reason.

Once both nodes are running, if a wince is detected by the wouse, it
should signal a run-stop to the robot, which should halt the motors and
place the power boards into standby.

#### evdev_listener vs. mouse_listener.py

There are two ways to read the device files for the wouse. The preferred
method is to use the evdev_listener node in conjunction with the udev
rule included in the hardware setup script (above). This udev rule will
cause the machine with the wouse to create a device file, */dev/wouse*,
whenever the usb plug is plugged in. The evdev_listener will then read
the evdev event's from this file as the mouse reports movement. The
file (modified from a version originally by Derek King) includes
significantly better error-checking, including confirming the name of
the device and available functions. In addition, the use of the udev
rule also prevents the X-server from treating the wouse as a regular
mouse and moving the cursor. However, it is somewhat more difficult to
setup.

The second method is *mouse_listener.py*, which reads PS/2-formatted
bytes from a /dev/input/mouse# file. This method publishes the same
information as the evdev_listener, and can be used interchangeably with
it. In addition, it does not require the use of the udev rules, and so
may be preferred if experimenting with different mice, as linux produces
PS/2 mouse data files readily for most mice. The drawbacks are less
error-checking for the device type, and that the X-server will still use
the wouse as a mouse to move the cursor, which is typically undesirable
(though this may be acceptable for testing.)

When no udev-rule is used, evdev_listener can still read data from
*/dev/input/event#*, where the *\#* corresponds to the wouse. The
X-server will continue to use the wouse to move the cursor, however.
Similarly, even when the udev rule is used, a */dev/input/mouse#* file
is still created, which may be read with mouse_listener.py, and the
X-server will continue ignoring the wouse.

The *wouse.launch* launch file contains arguments for specifying the
method to use, and the linux device file where the wouse data can be
read to receive new data. The default uses the evdev_listener to read
evdev data from /dev/wouse.

All three files can also be run independently from the commandline, with
both listeners accepting the device file-path to read from, and the
wouse node taking the file-path of the svm training data, as their only
(and required) arguments.

### Recovering from a run-stop

There are two ways to restore the robot's function after a run-stop is
triggered by the wouse.

#### Physical Run-stop

A physical run-stop may be triggered (having no effect) and reactivated,
which will proceed through the normal recovery procedures, resetting the
power boards and resetting the motors.

#### Desktop Launcher

A python script is provided, ```
python ...???.../wouse/scripts/reset_wouse.py
``` which will reset
the power boards and motors.

For easier access, a desktop launcher may be created to run
*wouse/reset_wouse_launcher.sh*, which will invoke the python script.
This allows a disabled user to easily reset the robot after a wouse
run-stop without needing to reach a physical run-stop or type commands
into a terminal.
