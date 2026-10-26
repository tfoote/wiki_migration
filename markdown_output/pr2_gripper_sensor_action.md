[Youtube](https://www.youtube.com/watch?v=IKxh5ZNqYY0)

[ TRO Publication ](http://fling.seas.upenn.edu/~jrom/wiki/uploads/Projects/touch2_rerevised.pdf )

## Overview

Tactile feedback provides critical information for completing any
sensitive manipulation task. Often this tactile feedback needs to be
used for closed-loop control to obtain a responsive and reliable system.
The package
[pr2_gripper_sensor_controller](pr2_gripper_sensor_controller) achieves
this by bypassing the ROS messaging system and integrating sensory
feedback with gripper control in real-time. This
[pr2_gripper_sensor_action](pr2_gripper_sensor_action) package is used
to communicate with the
[pr2_gripper_sensor_controller](pr2_gripper_sensor_controller) at a
higher level, and allows the user to send target goals to the real-time
controller. Currently this package provides several capabilities in the
form of action servers including:

- **Position Control** for changing the gripper aperture to a certain
  size.
- **Force Control** for grasping things with a specified force value
  within the gripper.
- **Contact Finding** for closing the gripper until contact has been
  made with a user-defined combination of finger contacts, and then
  stopping abruptly.
- **Slip Control** for holding an object with force control and
  observing the tactile sensors for any sign of object slippage. The
  controller automatically increases the grip force upon any sign of
  slip.
- **Event Detection** for detecting a variety of events that may happen
  at the gripper including: Impacts with the hand/arm, contact with the
  sides of the fingers, slip across the gripper fingerpads.
- **Grabbing** a higher-level behavior that is provided as a convenience
  for the user. Grab strings together several of the actions above to
  achieve a useful goal of delicately grasping an unknown object with
  hardness sensing and slip control.
- **Releasing** a higher-level behavior that strings together several
  lower level actions to detect contact between the object and
  environment and quickly open the gripper.

Additional details on how all of these methods are actually implemented
can be found in the recently submitted Transactions on Robotics paper
(link available upon acceptance).

Below you can see a diagram of how these various action servers
communicate with the real-time
[pr2_gripper_sensor_controller](pr2_gripper_sensor_controller).

![alt text\|width=780](attachment:wiki_control_flow_diagram_action.png)

### Who Should Not Use This Package?

Users who merely want to open or close the gripper with maximum joint
effort do **not** need to use this package. If you are not worried about
damaging the object being grasped, and are not interested in the signals
generated during this interaction, you should refer to the simpler
[pr2_gripper_action](pr2_gripper_action) package.

### Who Should Use This Package?

If you want to do any of the following things this is probably a good
package for you to use:

- Interact with anything in the environment that the gripper is capable
  of damaging when it applies maximum joint effort.
- Close the gripper aperture until either finger makes contact with the
  environment , and quickly stop the gripper motion.
- Detect when anything in the environment impacts the hand/arm of the
  robot.
- Detect when anything in the environment impacts the fingers of the
  robot.
- Detect when something is slipping or vibrating against the robot's
  fingers.
- Hold objects with (hopefully) the minimum amount of force necessary to
  manipulate them without having them slip out of the fingers.
- Do force control with something held between the gripper fingers.
- Conserve power by applying the minimum joint effort required to hold
  an object.
- Protect your gripper from damage and overuse by not applying undue
  force and stress to the fingers and drive mechanism.
- Do position control of the gripper while still having access to any of
  the other functionality discussed in this list.

## ROS API

The [pr2_gripper_sensor_action](pr2_gripper_sensor_action) package
contains a set of action nodes. The
[pr2_gripper_sensor_action](pr2_gripper_sensor_action) nodes provide
implementations of `SimpleActionServer` (see
[ actionlib documentation](actionlib )). The various actions subscribe
and publish to a series of messages found in
[pr2_gripper_sensor_msgs](pr2_gripper_sensor_msgs), but this API is not
intended for use outside of the pr2_gripper_sensor_\* packages. The
public API for the various action servers is described in the following
subsections, as well as a high-level description of what the node does.

### API Stability

- The ROS API is REVIEWED and UNSTABLE
- The C++ API is UNREVIEWED and UNSTABLE

### ROS Parameters

This package relies on several parameters being loaded onto the ROS
[param server](Parameter Server). Currently this is done when the node
is [launched](#Launching) by invoking the
`pr2_gripper_sensor_controller.yaml` file from the
[pr2_gripper_sensor_controller](pr2_gripper_sensor_controller) package.
If you wish to permanently edit any of the below values you should see
this file.

Many users may wish to modify some of these values temporarily and
repeatedly during program run time. This can be done by loading a new
value for the parameter below onto the param server, and then invoking
the [`reload_params` service](#ROS Services) to push these changes
into the real-time controller.

All the parameters listed below are currently loaded within the
namespace of the real-time controller for each of the two PR2 grippers,
`r_gripper_sensor_controller` and `l_gripper_sensor_controller`. A
`\*` below indicates that the parameter is not reloadable with the
[`reload_params` service](#ROS Services).



```clearsilver
param {
  1.name= close_speed
  1.default= 0.02 m/s
  1.type= double
  1.desc= The speed at which to close the gripper during the [[#Action APIs|find_contact action]]. Speed should always be positive.

  2.name= max_joint_effort
  2.default= -1.0 N
  2.type= double
  2.desc= The maximum amount of force to allow the virtual gripper parallel joint to apply during the various [[#Action APIs|actions]]. A value of -1 results in unlimited effort.

  3.name= fingertip_force_limit
  3.default= -1.0 N
  3.type= double
  3.desc= The maximum amount of force to allow the gripper to apply as measured by the fingertip sensors during a few of the force-feedback [[#Action APIs|actions]]. A value of -1 results in unlimited force.

  4.name= deformation_limit
  4.default= 0.03 m
  4.type= double
  4.desc= The maximum amount of deformation to allow after contact with several of the force-feedback [[#Action APIs|actions]]. A value of -1 results in unlimited deformation being allowed.

  5.name= force_lightest
  5.default= 1.2 N
  5.type= double
  5.desc= The minimum amount of force that any force-feedback [[#Action APIs|actions]] apply. All force-control actions that are commanded to lower forces will default to this value. This value is also used to help determine when the gripper is empty.

  6.name= hp_force_trigger
  6.default= 0.1 N
  6.type= double
  6.desc= The value of high-frequency force distrubance necessary to trigger contact with the gripper.

  7.name= force_servo_force_tolerance
  7.default= 0.3 N
  7.type= double
  7.desc= The force tolerance that any force-feedback actions need to be within (relative to the desired force) to be considered successful.

  8.name= force_servo_velocity_tolerance
  8.default= 0.001 m/s
  8.type= double
  8.desc= The velocity tolerance that any force-feedback actions need to be within (relative to 0) to be considered successful.

  9.name= slip_servo_start_force
  9.default= -1.0 N
  9.type= double
  9.desc= The force to immediately try and servo to once the [[#Action APIs|slip-servo action]] has been called. A value of -1.0 results in using whatever force is currently being experienced when the action was first called.

  10.name= position_servo_position_tolerance
  10.default= 0.01 m
  10.type= double
  10.desc= The position tolerance that any position-feedback actions need to be within (relative to the desired position) to be considered successful.

  11.name= position_open
  11.default= 0.09 m
  11.type= double
  11.desc= The maximum open position of the gripper. Used as a waypoint to move toward for several of the actions.

  12.name= joint_name*
  12.default= l(r)_gripper_joint
  12.type= string
  12.desc= The joint we want our controller to control.

  13.name= accelerometer_name*
  13.default= l(r)_gripper_motor
  13.type= string
  13.desc= The string that can be used to get a C++ handle to the palm accelerometer.

  14.name= left_pressure_sensor_name*
  14.default= l(r)_gripper_motorl(r)_finger_tip
  14.type= string
  14.desc= The string that can be used to get a C++ handle to the left finger pressure sensor.

  15.name= right_pressure_sensor_name*
  15.default= l(r)_gripper_motorr_finger_tip
  15.type= string
  15.desc= The string that can be used to get a C++ handle to the right finger pressure sensor.


}
```



### Action APIs

All of the action APIs below have example names for the right (r)
gripper. The same API is available for the left gripper simply by
replacing the (r) in the beginning of each name with (l).

Users should refer to the
[ tutorials](pr2_gripper_sensor_action/Tutorials ) section for specific
examples on using the action nodes defined below.

#### Beginner

##### grab

- **Description:** When called the `grab` action will open the gripper
  to the value of the param `position_open`, then close at param
  `close_speed` until finding 2-fingered contact with an object. It
  will then attempt to estimate how hard to hold the object, apply this
  force, and move into the `slip_servo` control mode. The `grab`
  action actually strings together the various actions of
  `gripper_action`, `find_contact`, `force_servo`, and
  `slip_servo` (in that order) to delicately grab an object and firmly
  hold onto it during manipulation. In addition to stringing these
  actions together it uses the feedback between the `find_contact` and
  `force_servo` actions to estimate object hardness, and attempts to
  grasp the object with a reasonable force to lift and manipulate it.
  This action returns successfully when the gripper has entered the slip
  servo mode. A diagram of these events can be seen below.

![alt text\|width=780](attachment:grab_diagram.png)

- **Topic Name:**`/r_gripper_sensor_controller/grab`
- action definition:
- goal:
  [PR2GripperGrabCommand.msg](http://www.ros.org/doc/api/pr2_gripper_sensor_msgs/html/msg/PR2GripperGrabCommand.html)
- result:
  [PR2GripperGrabData.msg](http://www.ros.org/doc/api/pr2_gripper_sensor_msgs/html/msg/PR2GripperGrabData.html)
- feedback:
  [PR2GripperGrabData.msg](http://www.ros.org/doc/api/pr2_gripper_sensor_msgs/html/msg/PR2GripperGrabData.html)
- A call to `gripper_action`, `force_servo`, `find_contact`,
  `slip_servo`, or `grab` will result in the current action goal
  being cancelled. Cancelling of this action for any other reason will
  stop sending commands to the gripper motor.
- Please see the associated sub-actions to understand the various
  [parameters](#ROS Parameters) that modify the behavior of this action.
  The parameter `position_open` is the only parameter not listed as
  part of the sub-actions below.

##### release

- **Description:** When called `release` will not change the control
  mode of the gripper, but rather it waits for a result from the
  `event_detector` action. This event can be controlled by the user as
  part of the input Command, defined below. Immediately after this event
  occurs `release` transitions the gripper to the `position_open`
  param value using the `gripper_action` position control action.
- **Topic Name:**`/r_gripper_sensor_controller/release`
- action definition:
- goal:
  [PR2GripperReleaseCommand.msg](http://www.ros.org/doc/api/pr2_gripper_sensor_msgs/html/msg/PR2GripperReleaseCommand.html)
- result:
  [PR2GripperReleaseData.msg](http://www.ros.org/doc/api/pr2_gripper_sensor_msgs/html/msg/PR2GripperReleaseData.html)
- feedback:
  [PR2GripperReleaseData.msg](http://www.ros.org/doc/api/pr2_gripper_sensor_msgs/html/msg/PR2GripperReleaseData.html)
- A call to `gripper_action`, `force_servo`, `find_contact`,
  `slip_servo`, or `grab` will result in the current action goal
  being cancelled. Cancelling of this action for any other reason will
  stop sending commands to the gripper motor.
- Please see the associated sub-actions to understand the various
  [parameters](#ROS Parameters) that modify the behavior of this action.
  The parameter `position_open` is the only parameter not listed as
  part of the sub-actions below.

#### Advanced

##### gripper_action

- **Description:** action node to provide position-control of the
  gripper aperture based on gripper virtual parallel joint position
  feedback. This action returns successfully when the desired position
  has been achieved within ``.
- **Topic Name:**`/r_gripper_sensor_controller/gripper_action`
- action definition:
- goal:
  [Pr2GripperCommandGoal.msg](http://www.ros.org/doc/api/pr2_controllers_msgs/html/msg/Pr2GripperCommandGoal.html)
- result:
  [Pr2GripperCommandResult.msg](http://www.ros.org/doc/api/pr2_controllers_msgs/html/msg/Pr2GripperCommandResult.html)
- feedback:
  [Pr2GripperCommandResult.msg](http://www.ros.org/doc/api/pr2_controllers_msgs/html/msg/Pr2GripperCommandResult.html)
- A call to `gripper_action`, `force_servo`, `find_contact`,
  `slip_servo`, or `grab` will result in the current action goal
  being cancelled. Cancelling of this action for any other reason will
  stop sending commands to the gripper motor.
- /!\\ : values input for the goal message parameter `max_effort` will
  replace the param server value of `max_joint_effort` and be used for
  all subsequent action calls (for all actions in this library).
- The following [parameters](#ROS Parameters) alter the performance of
  this action, and can be reloaded using the
  [reload_parameters service](#ROS Services):
- `max_joint_effort`
- `position_servo_position_tolerance`

##### force_servo

- **Description:** action node to provide force-control of the gripper
  joint based on the contact force reported by the tactile sensors of
  the PR2 finger. The implementation of this force servoing algorithm
  assumes that the gripper is making contact with both fingers, and
  cannot be used for single finger contact. The force servoing algorithm
  will attempt to move the gripper joint to maintain the desired force
  level **on the gripper finger currently experiencing the minimum
  amount of force**. The force sensing relies on information coming from
  the pressure-sensitive arrays on the PR2 gripper, specifically the
  flat fingerpad area. Objects that contact other locations on the
  gripper (such as the palm) will not be detected. This action returns
  successfully when the fingerpad force is within
  `force_servo_force_tolerance` of the desired force, and the velocity
  of the gripper is within `force_servo_velocity_tolerance` of zero.
- **Topic Name:**`/r_gripper_sensor_controller/force_servo`
- action definition:
- goal:
  [PR2GripperForceServoCommand.msg](http://www.ros.org/doc/api/pr2_gripper_sensor_msgs/html/msg/PR2GripperForceServoCommand.html)
- result:
  [PR2GripperForceServoData.msg](http://www.ros.org/doc/api/pr2_gripper_sensor_msgs/html/msg/PR2GripperForceServoData.html)
- feedback:
  [PR2GripperForceServoData.msg](http://www.ros.org/doc/api/pr2_gripper_sensor_msgs/html/msg/PR2GripperForceServoData.html)
- The speed of motion during force servo is not controlled, so if it is
  known beforehand that gripper is moving through open space with no
  contact it may be desirable (although not necessary) to use an
  alternative action, such as `find_contact`.
- Any force below the minimum param `force_lightest` will be
  automatically increased to equal `force_lightest`. You cannot
  command negative (opening forces) as the `fingertip_force` input.
- A call to `gripper_action`, `force_servo`, `find_contact`,
  `slip_servo`, or `grab` will result in the current action goal
  being cancelled. Cancelling of this action for any other reason will
  stop sending commands to the gripper motor.
- The following [parameters](#ROS Parameters) alter the performance of
  this action, and can be reloaded using the
  [reload_parameters service](#ROS Services):
- `max_joint_effort`
- `fingertip_force_limit`
- `deformation_limit`
- `force_lightest`
- `force_servo_force_tolerance`
- `force_servo_velocity_tolerance`

##### find_contact

- **Description:** action node to close the gripper at the param server
  velocity value `close_speed` and stop immediately once the
  user-specified finger contact conditions have been met (using sensing
  from the PR2 finger tactile sensors). The user is free to specify
  either the left/right finger, or both contacts. The contact sensing
  relies on information coming from the pressure-sensitive arrays on the
  PR2 gripper, specifically the flat fingerpad area. Objects that
  contact other locations on the gripper (such as the palm) will not be
  detected. This action returns successfully when the conditions defined
  by the message variable `contact_conditions` have been met.
- **Topic Name:**`/r_gripper_sensor_controller/find_contact`
- action definition:
- goal:
  [PR2GripperFindContactCommand.msg](http://www.ros.org/doc/api/pr2_gripper_sensor_msgs/html/msg/PR2GripperFindContactCommand.html)
- result:
  [PR2GripperFindContactData.msg](http://www.ros.org/doc/api/pr2_gripper_sensor_msgs/html/msg/PR2GripperFindContactData.html)
- feedback:
  [PR2GripperFindContactData.msg](http://www.ros.org/doc/api/pr2_gripper_sensor_msgs/html/msg/PR2GripperFindContactData.html)
- The parameter `zero_fingertip_sensors` should be used to
  periodically recalibrate the fingertip pressure array readings to
  achieve the best possible performance results. It is advisable that
  any time `find_contact` is called and it is known that the gripper
  fingers are not contacting the environment this flag be set to
  `true` to recalibrate the fingertip sensors. This flag should
  **never** be set to true when the gripper is in contact with the
  environment.
- Contact is considered to have occured when the force on the fingerpad
  meets or exceeds the param value `force_lightest`, or the high
  frequency force content exceeds `hp_force_trigger`.
- A call to `gripper_action`, `force_servo`, `find_contact`,
  `slip_servo`, or `grab` will result in the current action goal
  being cancelled. Cancelling of this action for any other reason will
  stop sending commands to the gripper motor.
- The following [parameters](#ROS Parameters) alter the performance of
  this action, and can be reloaded using the
  [reload_parameters service](#ROS Services):
- `close_speed`
- `max_joint_effort`
- `hp_force_trigger`

##### slip_servo

- **Description:** action node to use a force servoing algorithm similar
  to `force_servo`, but also monitor the finger-mounted pressure
  sensors for signs of disturbance. When a disturbance, such as
  vibrating contact or slip is detect, the slip servo algorithm
  increases the force applied at the gripper as a percentage of the
  already-applied grip force. `slip_servo` relies on information
  coming from the pressure-sensitive arrays on the PR2 gripper,
  specifically the flat fingerpad area. Objects that contact other
  locations on the gripper (such as the palm) will not be detected. This
  action never returns successfully, but rather it is used to put the
  real-time controller into the slip servo mode.
- **Topic Name:**`/r_gripper_sensor_controller/slip_servo`
- action definition:
- goal:
  [PR2GripperSlipServoCommand.msg](http://www.ros.org/doc/api/pr2_gripper_sensor_msgs/html/msg/PR2GripperSlipServoCommand.html)
- result:
  [PR2GripperSlipServoData.msg](http://www.ros.org/doc/api/pr2_gripper_sensor_msgs/html/msg/PR2GripperSlipServoData.html)
- feedback:
  [PR2GripperSlipServoData.msg](http://www.ros.org/doc/api/pr2_gripper_sensor_msgs/html/msg/PR2GripperSlipServoData.html)
- Slip is considered to have occurred when the high frequency fingerpad
  force content exceeds a value define by the product of the param
  `slip_servo_gain` and the current fingerpad force (see TRO paper for
  additional detail).
- A call to `gripper_action`, `force_servo`, `find_contact`,
  `slip_servo`, or `grab` will result in the current action goal
  being cancelled. Cancelling of this action for any other reason will
  stop sending commands to the gripper motor.
- The following [parameters](#ROS Parameters) alter the performance of
  this action, and can be reloaded using the
  [reload_parameters service](#ROS Services):
- `max_joint_effort`
- `fingertip_force_limit`
- `deformation_limit`
- `force_lightest`
- `slip_servo_force_tolerance`
- `slip_servo_start_force`

##### event_detector

- **Description:** action node that can be used to monitor sensor
  signals of the PR2 palm-mounted accelerometer, fingertip pressure
  sensor fingerpad, and fingertip pressure sensor periphery cells. The
  user can specify a variety of different conditions which will trigger
  the action to return a result. Particularly, the user can specify how
  much acceleration they are looking for (good for detecting contacts
  between the arm or objects held in the gripper and the world), or how
  much slip to trigger on. The user can also specify whether they want
  to trigger upon impacts with the sides of the fingers. This action is
  particularly useful when placing objects down and finding the contact
  event, or detecting contacts with the hand/arm during motion. This
  action returns successfully when conditions defined in the message
  vaiable `trigger_conditions` have been met.
- **Topic Name:**`/r_gripper_sensor_controller/event_detector`
- action definition:
- goal:
  [PR2GripperEventDetectorCommand.msg](http://www.ros.org/doc/api/pr2_gripper_sensor_msgs/html/msg/PR2GripperEventDetectorCommand.html)
- result:
  [PR2GripperEventDetectorData.msg](http://www.ros.org/doc/api/pr2_gripper_sensor_msgs/html/msg/PR2GripperEventDetectorData.html)
- feedback:
  [PR2GripperEventDetectorData.msg](http://www.ros.org/doc/api/pr2_gripper_sensor_msgs/html/msg/PR2GripperEventDetectorData.html)
- A call to `gripper_action`, `force_servo`, `find_contact`,
  `slip_servo`, or `grab` will result in the current action goal
  being cancelled. Cancelling of this action for any other reason will
  stop sending commands to the gripper motor.

### ROS Services

Currently three [services](Services) are provided to the user. These
services communicate directly with the
[pr2_gripper_sensor_controller](pr2_gripper_sensor_controller) package.
Most users will generally not need to use them, however, advanced users
may find them to come in handy. All services communicate using the
standard Empty Request and Response message types.

##### zero_fingertip_sensors

- **Description:** a service that is used to optionally re-calibrate the
  fingertip sensors. The fingertip sensor no-load reading is naturally a
  non-zero value, and it tends to drift over time (as more contacts
  occur). This calibration is done once when loading the controllers,
  and any time the `find_contact` action is called with the
  `zero_fingertip_sensors` flag as `true`. Users may use this
  service to re-calibrate the sensors themselves, which is especially
  useful if you do not intend to call `find_contact` often. This
  service should only be called when the fingerpads are not in contact
  with the environment.
- **Service
  Name:**`/r_gripper_sensor_controller/zero_fingertip_sensors`

##### reload_params

- **Description:** a service that causes the controller to fetch
  [parameters](#ROS Parameters) from the param-server and load them into
  the controller. This service should be called anytime the user wants
  to edit the param-server values and push them to the controller. It
  can be used at any time during execution.
- **Service Name:**`/r_gripper_sensor_controller/reload_params`

##### stop_motor_output

- **Description:** a service that can be called at any time to force the
  real-time controller into a state that commands no force output to the
  gripper joint. This service can be used as an emergency shutoff. After
  calling this service any further action calls to control the gripper
  will take the gripper out of this shutoff mode.
- **Service Name:**`/r_gripper_sensor_controller/stop_motor_output`

## Hardware Dependecies

Please refer to the
[pr2_gripper_sensor_controller](pr2_gripper_sensor_controller) page to
understand the hardware dependencies necessary for this package to run
properly.

## Running the Action Nodes

### Compiling

If you are not using pre-built libraries it is necessary to compile the
real-time controller
[pr2_gripper_sensor_controller](pr2_gripper_sensor_controller) **prior**
to launching the PR2. By compiling the
[pr2_gripper_sensor_action](pr2_gripper_sensor_action) library before
launching the robot the
[pr2_gripper_sensor_controller](pr2_gripper_sensor_controller) package
will be automatically included as a dependency.

Compiling can be done simply by typing: 

```
rosmake pr2_gripper_sensor_action
```



Which will build all action nodes and their dependencies.

### Launching

All nodes for both the left and right gripper, as well as the
appropriate real-time controllers for both grippers, can be loaded
simply by executing the following launch script:


```
roslaunch pr2_gripper_sensor_action pr2_gripper_sensor_actions.launch
```


