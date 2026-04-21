![](attachment:Screenshot.png)

## Usage

### Server (PR2)

The web interface is served directly from the robot on port 8000 using
roswww. To launch the web server and other back-end services:
```
roslaunch hrl_pr2_lib openni_kinect.launch
roslaunch assistive_teleop assistive_teleop.launch
```

### Client (Desktop)

Point a Chrome web browser to: ```
http://PR2HOSTNAME:8000/assistive_teleop/hz_tab_interface.html
``` where
PR2HOSTNAME is the hostname of the robot on which the above launch file
was run.

## Interface

### Feedback

#### Video

The interface provides visual feedback using the
[mjeg_server](http://www.ros.org/wiki/mjpeg_server) from
\`bosch-ros-pkg\` to stream images from the PR2\'s right wide_stereo
camera, either of the forearm cameras, and an added kinect sensor on the
head of the robot. The forearm camera image streams are rotated using
the [image_rotate](http://www.ros.org/wiki/image_rotate) package so that
the image is always \'right-side-up\'. Buttons beneath the image stream
allow for user camera selection. Also, when using *Normal Approach*, the
camera stream will be modified to include an arrow indicating the point
in the image and normal direction which has been selected, in order to
provide confirmation that the robot is attempting the desired behavior.

#### Text

Text feedback is displayed beneath the video, providing an indication of
the action currently being taken by the robot. While somewhat trivial
for low-level, immediately responsive control, this becomes extremely
valuable for longer-term, semi-autonomous behaviors, so that the user is
constantly aware of what the robot is doing.

### Control

In order to manage the PR2\'s many degrees of freedom, control of the
robot has been heavily subdivided based on the part of the robot being
controlled and the form of control being used. Under the default
controls tab, the selection of a component to control is placed on the
left, and alters the actions performed by the control inputs. All
motions (except base movement) are performed in discrete movements. The
relative step size for a given input can be adjusted (+/-100% of the
default) with the slider to the left of the command buttons. The scaling
value will remain set for each portion separately, but will reset when
the page is refreshed.

#### Control Head

When **Control Head** is selected, the control inputs provide arrows for
looking up(\^), down(v), left(\<), and right(\>). In addition, the
center button will point the head at the base of the robot, which can be
used for navigation while driving. Lastly, this also exposes controls to
direct the head to persistently follow either the left or right gripper.

#### Control Right/Left Arm

**Control Right/Left Arm** provides access to low-level control of the
arm position of the PR2. The arrow buttons send commands in either the
\`/torso_lift_link\` or \'l/r_gripper_tool_frame\', as selected in the
dropdown menu. These commands attempt to move the arm a small distance
in the given direction while maintaining the gripper pose, or else
rotate the gripper about the tool frame while maintaining this
end-effector position.

Additionally, this sub-division also exposes controls for performing a
**Normal Approach**, which will attempt to place the gripper
perpendicular to any arbitrarily indicated point visible in the kinect
image. This is performed by selecting *Normal Approach* for the desired
arm, and clicking a desired point on the image. Using
[pixel_2_3d](http://www.ros.org/wiki/pixel_2_3d) to determine the
associated 3D point in space and a vector normal to the surface at that
point, the interface attempts to use move_arm motion planning to place
the gripper 20cm away from the point, with the tips of the gripper
pointing perpendicular to the surface.

In combination with this function are controls to *Advance* and
*Retreat* the gripper. These commands will move the gripper directly
forward or backward along the current orientation, allowing for easy
grasping and manipulation at arbitrary gripper orientations. While
designed for use with *Normal Approach*, these functions are completely
general, and will work at any point in time when using the interface to
control the robot.

#### Control Right/Left Hand

Selecting **Control Right/Left Hand** exposes controls for directly
commanding the joints of the PR2\'s \'wrist\': Forearm Roll, Wrist Flex,
and Wrist Roll. The position of the arm is determined by the origin of
the \`/wrist_roll_link\`, and so these commands can extend the reach of
the PR2 by extending the wrist flex beyond the current position of the
arm.

#### Control Base

When **Control Base** is selected, control inputs are exposed for
driving the robot forward/backward, strafing left/right, and turning in
place. Driving is the only motion which receives velocity inputs, and
consistent motion can be achieved with a click-and-hold.

#### Sliders (Persistent)

The torso height of the robot is controlled using a slider, which both
receives commands and reports the current position. Adjust the height of
the robot by moving the slider bar to the desired position. Once the
goal is sent, the slider will display the motion of the torso, as the
current position continues to be updated.

#### Image (Persistent)

Currently, clicking anywhere on the image defaults to pointing the head
to look at the 3D point associated with the image point where the click
occurs, as returned by [pixel_2_3d](http://www.ros.org/wiki/pixel_2_3d).

Similarly, the open/close state of the grippers is controlled by
sliders, with the grippers being open at the top of the bar, and closed
at the bottom. These sliders also report the current position of the
gripper, and will display changes over time if the grippers are sent
large commands.

#### Run-Stop (Persistent)

At the bottom of the interface, a large button labeled *STOP ROBOT* acts
as a user-controlled run-stop, and immediately halts the PR2\'s motors.
This replaces the interface with a warning message, and a *Reactivate*
button to restart the motors. Be careful of the movement of the robot
when run-stopped (gravity acting on head and arms, spring tension in
arms, etc. ) as well as the possibility of the robot dropping any held
objects.

## Acknowledgements

First and foremost, the work depends upon the insight, drive, and
feedback of Henry Evans, as well as the support of his family.

This package depends heavily upon the
[rosbridge_suite](http://www.ros.org/wiki/rosbridge_suite) and
[mjpeg_server](http://www.ros.org/wiki/mjpeg_server) packages.
