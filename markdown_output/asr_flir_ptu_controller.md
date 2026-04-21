![\|width="333",height="200"](attachment:Logo-white-medium.jpg)

## Description

The asr_flir_ptu_controller is closely connected to the
[asr_flir_ptu_driver](asr_flir_ptu_driver) as it grants access to the
PTU just as the mentioned package. The difference between both packages
is that asr_flir_ptu_controller uses
[asr_flir_ptu_driver](asr_flir_ptu_driver) to make the PTU accessible
for actionservers by offering an action client that takes new position
commands for the pan and tilt values of the pan and executes them with
the help of [asr_flir_ptu_driver](asr_flir_ptu_driver). The package
supports the taking of new position goals, constant feedback of the
movement and a check if the movement ended successfully. Not fulfillabe
goals get filtered out from the beginning - they get rejected.

## Functionality

The asr_flir_ptu_controller serves a single purpose: It makes the
movement of a Flir pan-tilt-unit accessable by a *ros::!ActionClient*.
The functionality by asr_flir_ptu_controller will be shown below in a
sequence diagram. For knowledge of the invoked functions check out
[asr_flir_ptu_driver](asr_flir_ptu_driver).

![height="1030",width="584"](attachment:interaction.png)

Basic knowledge of the PTU movement (e.g. orientation of axis, movement
area, etc.) can be obtained from the documentation of
asr_flir_ptu_driver. A lot of functionalities, especially the
configuration of forbidden areas, are only available in the
asr_flir_ptu_driver and cannot be accessed from here.
asr_flir_ptu_controller extends the basic functionalities of movement
and forbidden area checking by wrapping them them inside an Action
offered by an !ActionServer, making invocations easy and offering the
opportunity to use the !ActionServer in context of a more complex
control logic. However, the controller restricts the opportunities of
the asr_flir_ptu_driver somehow as it forces the check for forbidden
areas and does not allow path_prediction.

## Usage

It is crucial for the usage of this package that you have an instance of
asr_flir_ptu_driver running. Furthermore, if you are not using the
simulation mode of the asr_flir_ptu_driver, you must have a Flir PTU.
The asr_flir_ptu_controller can be used with all models the
asr_flir_ptu_driver can use, as it does only access them over it.

### Needed packages

-   [asr_flir_ptu_driver](asr_flir_ptu_driver)

### Needed software

-   [Boost (1.54.0.1)](http://www.boost.org/)

### Needed hardware

To run the asr_flir_ptu_driver no special hardware is needed, but it is
recommended to use a real Flir PTU together with asr_flir_ptu_driver
unless you only need some simulation.

### Start system

Install the software mentioned above, place the packages inside a catkin
workspace and build them.

Being mounted upon the [asr_flir_ptu_driver](asr_flir_ptu_driver) it is
necessary that you have a running instance of asr_flir_ptu_driver, so
start it **first**.

After starting the asr_flir_ptu_driver, start the
asr_flir_ptu_controller. Interaction is then done over the ActionServer
launched by asr_flir_ptu_controller.

How to use the corresponding "goal" topic can be found in subsection
4.1.

#### Simulation

asr_flir_ptu_controller has no separate simulation mode. Simply launch
it as described in 3.4.2, but start the asr_flir_ptu_driver in
simulation mode and you will have a working simulation.

#### Real

As the [asr_flir_ptu_driver](asr_flir_ptu_driver) has no simulation mode
itself, launching it real is the only option you have. Little to no
configuration needs to be done before launch if you did not change the
topic names used by asr_flir_ptu_driver. Otherwise you need to adjust
the corrsponding topic names found in the ptu_controller_settings.yaml
file in the param folder. Most of the values there should be fine,
nevertheless two should be reconsidered: *maxSteps* and *margin. *The
first one describes the maximum amount of steps that will be done before
a movement is considered a failure. A step means hereby a spin of ROS
(to be totally fair, it means a publishing from the asr_flir_ptu_driver
about his current position, what happens each spin). The second one
describes the margin parameter known from asr_flir_ptu_driver. You can
set this parameter freely, it is limited by the minimum of the
width/height of the pan/tilt movement area divided by 2.

Usually no configuring should be necessary.

First start the asr_flir_ptu_driver as known from the tutorial.

Then start the asr_flir_ptu_controller using

roslaunch asr_flir_ptu_controller ptu_controller.launch

From that point on you can use the !ActionServer offered by
asr_flir_ptu_controller.

## ROS Nodes

### Subscribed Topics

*/asr_flir_ptu_driver/ptu_state*

All topics below are subscribed by the !ActionServer of
asr_flir_ptu_controller by default. They use a custom defined message
which can be found inside the action folder of the package.

*/ptu_controller_actionlib/cancel*

-   Type: actionlib_msgs::GoalID
-   Usage: Default !ActionServer topic to cancel a current goal.

*/ptu_controller_actionlib/goal*

-   Type: asr_flir_ptu_controller::PTUMovementActionGoal
-   Usage: !ActionServer topic for sending a new goal. Includes a
    sensor_msgs::!JointState *target_joint. *Use
    target_joint.position\[0\] to store the pan value the PTU shall move
    to and target_joint.position\[1\] to store the tilt value. Setting
    target_joint.velocity\[0\] or target_joint.velocity\[1\] to a value
    != 0 will result in the rejection of the goal.

### Published Topics

_/asr_flir_ptu_driver/state_cmd_

-   Type: asr_flir_ptu_driver::State
-   Usage: Used by the asr_flir_ptu_controller to send movement commands
    to the asr_flir_ptu_driver.

All published topics by the asr_flir_ptu_controller are related to the
!ActionServer and should not be invoked from the command line. Use an
!ActionClient or some tool design for interacting with !ActionServers.
Most of them are based on a custom !ActionServer message that can be
found inside the action folder of the package.

*/ptu_controller_actionlib/feedback*

-   Type: asr_flir_ptu_controller::PTUMovementActionFeedback
-   Usage: This topic is used by asr_flir_ptu_controller to publish
    constant feedback to progress of the currently active goal. The
    message contains a sensor_msgs::!JointState called *base_joint* as
    well as a float called *percentage. *Current pan and tilt values can
    be obtained by reading base_joint.position\[0\] for the current pan
    value and base_joint.position\[1\] for the current tilt value. As
    the name indicates, *percentage* contains the current percentage of
    completion of the movement represented by a number between 0.0 and
    1.0;

*/ptu_controller_actionlib/result*

-   Type: asr_flir_ptu_controller::PTUMovementActionResult
-   Usage: The topic on which the !ActionServer publishes the result of
    a goal. Contains a sensor_msgs::!JointState called *end_joint*. The
    final values for pan/tilt can be obtained by reading
    end_joint.position\[0\]/end_joint.position\[1\].

*/ptu_controller_actionlib/status*

-   Type: actionlib_msgs::!GoalStatusArray
-   Usage: Default !ActionServer status topic.

### Parameters

_/PTUController/actionServerName_

-   Type: string
-   Explanation: Namespace under which the !ActionServer will publish
    its topics (goal, feedback,\...)

*/PTUController/commandTopicName*

-   Type: string
-   Explanation: Name of the topic where the asr_flir_ptu_driver
    publishes its current state. Only modify if you changed it in
    asr_flir_ptu_driver.

*/PTUController/margin*

-   Type: double
-   Explanation: The margin value used by asr_flir_ptu_driver
    (explanation in the corresponding documentation). Short: All values
    out of bounds but within bounds + margin will be set to the bounds.
    Modification is usually not needed.

*/PTUController/maxSteps*

-   Type: int
-   Explanation: This value references the maximum amount of updates
    from the PTU about its position before the !ActionServer of
    asr_flir_ptu_controller will abort the current goal. This value
    should be fairly high as this case should usually not happen, it is
    a simple protection against the case when the PTU would never reach
    the desired location.

*/PTUController/serviceAlive*

-   Type: string
-   Explanation: Name of the alive service of asr_flir_ptu_driver. If
    you adjusted it there, adjust it here accordingly.

*/PTUController/serviceValidation*

-   Type: string
-   Explanation: Name if the validation service of asr_flir_ptu_driver.
    If you adjusted it there, adjust it here accordingly.

*/PTUController/topicName*

-   Type: string
-   Explanation: Name of the topic the asr_flir_ptu_driver takes new
    position commands from. Only adjust if adjusted in
    asr_flir_ptu_driver.

### Needed Services

_/asr_flir_ptu_driver/validation_service_

-   Type: asr_flir_ptu_driver::Predict
-   Usage: The asr_flir_ptu_driver uses this service to validate
    pan/tilt values received via the goal topic of the !ActionServer.
    Getting negative response here results in a rejection of a goal.

*/asr_flir_ptu_driver/alive_service*

-   Type: std_srvs::Empty
-   Usage: The asr_flir_ptu_controller uses this service to check if the
    asr_flir_ptu_driver is alive (binding to the "publisher").

# 5. Tutorials

## 5.1. Usage with own code

No detailed tutorial will be given here on how to use the
asr_flir_ptu_controller with your own code, as it is very self
explaining.

Nevertheless there exists a very long code example on how to use the
Goal/\....-callbacks offered by the asr_flir_ptu_controller. Move to the
src folder of the package and have a look at the
PTUControllerClient.cpp. It is a piece of code that was used to test the
behaviour of the !ActionServer provided during development and remained
here as an example for the usage. Be aware that some of the expected
reactions of this program depend on the configuration of the
[asr_flir_ptu_driver](asr_flir_ptu_driver) and the PTU you are using -
executing it without adapting it to your data is not recommended. Just
use it as an example for usage.

If you do not know how to use a !ActionServer check out the
[corresponding ROS tutorials](http://wiki.ros.org/actionlib/Tutorials).
