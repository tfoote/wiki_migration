![\|width=\"333\",height=\"200\"](attachment:Logo-white-medium.jpg)

## Description

The purpose of the asr_flir_ptu_driver package is to grant control over
pan-tilt-units (PTU) being manufactured by FLIR using ROS. This is
achieved by making the movement of the pan-tilt-unit as well as it\'s
configuration, like the movement speed or acceleration that is used,
accessable by messages over topics. Therefore this package offers a free
and ROS-integrated way to control FLIR pan-tilt-units with ease. You can
see a PTU with a typical use case below.

![height=\"317\",width=\"764\"\|width=\"410\",height=\"170\"](attachment:PTU.png)

## Functionality

The following functionalities are offered by asr_flir_ptu_driver:

-   \'\'\'PTU movement\'\'\' The most basic functionality of
    asr_flir_ptu_driver is the control of the movement of a FLIR
    pan-tilt-unit. Movement means hereby the rotation arround the pan or
    tilt axis, illustrated below with the movement direction.\'\'\'
    ![height=\"320\",width=\"695\"\|width=\"640\",height=\"294\"](attachment:ptu_movement.png)
    \'\'\' The movement arround the pan and tilt axis is limited and
    influenced by several factors. First of all the movement is
    restricted by the physical limits of the PTU. These values are
    absolute and can not be extended. Furthermore it is possible to set
    more restricitve pan/tilt limits. Influencing factors for the
    movement are acceleration, start-up speed and maximum speed (whch
    can not be extended beyond a certain limit). The acceleration is
    static during the movement and only changes from positive to
    negative when changing from acceleration to deceleration. Therefore
    the speed starts as the start-up speed, equals a ramp until it
    reaches the maximum speed, stays at maxiumum speed until the
    deceleration phase begins and decelerates equivalent to the
    acceleration. The behaviour is illustrated exemplarily below. Pan
    and tilt rotation works independendly, so to speak acceleration
    phase, deceleration phase and maximum speed phase do not get
    synchronized.
-   ![height=\"388\",width=\"400\"\|width=\"260\",height=\"252\"](attachment:acceleration_model.png)
-   \'\'\'PTU configuration\'\'\' Another functionality of
    asr_flir_ptu_driver is the configuration of the PTU\'s values. As
    mentioned in the point above the PTU\'s movement is influenced by
    several factors, as position and speed limits, start-up speed,
    acceleration and maximum speed. The configuration of this values is
    made possible by this package.
-   \'\'\'Definition of forbidden\'\'\' \'\'\'areas \'\'\'Furthermore,
    the asr_flir_ptu_driver allows to define so called forbidden areas.
    These forbidden areas can be imagined as rectangles being defined by
    a maximum and minimum pan/tilt value. You can see such a forbidden
    area illustrated below (the rotation angles of pan/tilt are
    illustrated in a 2d coordiante system).\'\'\'
    ![height=\"600\",width=\"727\"\|width=\"516\",height=\"425\"](attachment:forbidden_areas.png)
    \'\'\' The main purpouse of such forbidden areas is to restrict the
    PTU movement in a finer granularity than the minimum and maximum
    values for pan and tilt can. How the forbidden areas are interpreted
    depends on the usage of asr_flir_ptu_driver. It is never possible to
    end a movement inside a forbidden area (except the checking for
    those forbidden areas is explicitly turned off). Moving through
    forbidden areas is usually possible, as a path prediction for a PTU
    movement is very resource intensive due to the non-static speed and
    independent movement of both axis. Nevertheless there is a service
    available to perform this path prediction. Using the pan/tilt
    coordiantes returned by this service prevents movement through
    forbidden areas (forbidden area checking should be turned off if you
    use points obtained by the path prediction service because these
    points can lie minimal inside a forbidden area, e.g for a 1/1000
    degree).

```{=html}
<!-- -->
```
-   \'\'\'Path prediction \'\'\'As mentioned in the section above, path
    prediction is a tool that is necessary if passing through a
    forbidden area should not happen. To prevent this, path prediction
    calculates the intersection point with the first forbidden area the
    PTU path passes through. This point can then be used as the new end
    point. The path prediction automatically calculates whether the new
    path to the point hits another forbidden area (this is possible
    because of changed times for the phases of acceleration, maximum
    speed and deceleration). This is how the path prediction works:
-   The path gets discretized by taking several points along the path
    and connecting them directly (linear).
-   For each of these linear path segments a cut between the associated
    line and the lines implied by each forbidden area are calculated
    (lines implied by the points of the associated corners of the
    forbidden areas).
-   Now it has to be checked if the found point lies between the two
    points of the path segment and the two points of the \"border\" of
    the forbidden area. Therefore it is checked if the point lies within
    the bounding rectangle defined by both points and extended by a
    tolerance value. Furthermore, it is checked if the point\'s distance
    from the line is less than the same tolerance value (using distance
    calculation based on Hesse normal form). If the check is successful
    for both, the two points of the path segment and the two points of
    the forbidden area \"border\" and the check point is legit. An
    illustration can be found below.
-   The path segments get processed one after another, for each path
    segment all forbidden area borders are checked. If a legit
    intersection point is found, the checking continues for the same
    path segment with the reaming forbidden area \"borders\" of all
    forbidden areas, then the nearsest legit intersection point (from
    the start point) is chosen and the checking is ended. .
    ![height=\"310\",width=\"600\"\|width=\"584\",height=\"301\"](attachment:intersection_calculation.png)

## Usage

To use this package it is important that you have a FLIR pan-tilt-unit
connected to your system using a serial port (except you only want to
use the simulation). Make sure that the PTU is fully powered and
initialized before you start the software of this package.

### Needed packages

The asr_flir_ptu_driver package needs no other software to work.

### Needed software

-   [Boost (1.54.0.1)](http://www.boost.org/)
-   [wxWidget (3.0.2)](https://www.wxwidgets.org/downloads/)

### Needed hardware

The asr_flir_ptu_driver package is intended for the use with
pan-tilt-units of the manufacturer FLIR. The package is confirmed to be
working with the PTU-46-17.5 model (from Directed Perception before
being acquired by FLIR), but should be working with a broad range of
their other pan-tilt-units.

### Start system

First of all you will have to install the needed software shown in
section 3.2. Then download the package from github, place it inside a
catkin workspace and build it.

Before starting any software it is possible to configure the PTU driver
using the ptu_properties.yaml located in the param-Folder. The meanings
of all parameters will be explained in the corresponding section 4.3.

As soon as you have configured the PTU as you desire you can either
start a real PTU or a simulation. How to do this is described in the
subsections of 3.4.

As soon as you launched the real PTU/simulation, you can interact with
it in two ways:

. \'\'\'1. Use the GUI\'\'\' To communicate with the PTU a built in GUI
is delivered which allows to move the PTU arround as well as the
configuration of parameters. When launching the GUI you have to decide
whether you want simple forbidden area checking or path prediction. If
you want to use simple forbidden area checking use\'\' \'\'
```
roslaunch asr_flir_ptu_driver ptu_gui.launch
``` This setting will result in the following
behaviour: If you a endpoint for a movement which is inside a forbidden
area it will be rejected, nothing will happen. If you choose an endpoint
outside a forbidden area and the path from the current position will
move through a forbidden area, this will happen and nothing will be
rejected. The other option is to launch the GUI using path_prediction.
This is done by using ```
roslaunch asr_flir_ptu_driver ptu_gui.launch path_prediction:=true
``` Using path_prediction the
behaviour will be the following: If you select an endpoint that will lie
within a forbidden area, the path the PTU would take will be predicted
and it will stop at the point it would hit the forbidden area. If the
endpoint does not lie within a forbidden area but the path from the
current position would pass through a forbidden area, it will stop at
the point where the path would hit the forbidden area. Be aware that
acceleration and maximum speed for the axis are used for the
calculation, so the path is no direct line from the current point to the
end point. Pan and tilt movements are independent, so one movement can
end before the other.\'\'\' \'\'\' \'\'\'Be aware:\'\'\' path prediction
does not work with simulation No matter how you start the GUI and
whether you are using simulation or a real PTU the GUI will look like
this: ![\|width=\"595\",height=\"366\"](attachment:GUI.png) Originally
the GUI was not only developed for controlling the PTU, but also for
visualizing the data delivered by a stereo camera system being mounted
upon it. Therefore it is possible to enter up to 2 topics (1) that
publish picture data (sensor_msgs::Image) and to visualize them (2). The
PTU itself publishes its current status over a topic (e.g. it\'s
position). This topic has to be selected (3), usually it will look like
\"/asr_flir_ptu/driver/\" or \"/asr_flir_ptu_driver/ptu\_\". Below it is
possible to enter the position the PTU shall rotate to in degrees for
pan and tilt (4), right of it it is possible to modify the maximum and
minimum pan/tilt values. Be aware that they cannot be set to a freely
high/low value because of restrictions of the physical form of the PTU.
These so called \"hardware limits\" can not be extended, limits out of
them will be rejected. Below, further settings like acceleration,
maxiumum speed, \... for the pan and tilt axis can be set (5). Finally,
you can send your changes/selected movement position to the PTU all
together by pressing the \"Update\" button (6). After you pressed the
update button, mark the \"listen for update\" box directly above to read
the response from the PTU - this will modify the values in the PTU to
the current values of the PTU. It is recommended to mark this directly
after starting the GUI. Always remove the mark after the update is done
because it is going to prevent you from entereing any new values in the
fields. \'\'\'2. Use messages/topics\'\'\' The use of messages for
manual communication with the PTU is not advised as the GUI wraps this
in a more user friendly way. Messages and communication over topics
should rather be used if you have a program that needs to communicate
with the PTU. Check out
[asr_flir_ptu_controller](asr_flir_ptu_controller) if you need an
actionserver for the communication. To tell the PTU to move to a certain
point, use a \'\'asr_flir_ptu_driver::State\'\' message sent over the
\'\'/asr_flir_ptu_driver/state_cmd\'\' topic by default. The last part
of the topic (after the last /) can be modified by use of the parameter
\'\'/asr_flir_ptu_driver/topicStateCommand\'\' (default value is defined
in param/rosCommands.yaml). To pass pan and tilt positions to the PTU,
use the \'\'position\'\' field of the \'\'sensor_msgs::!JointState\'\'
included in the \'\'asr_flir_ptu_driver::State\'\' message. Set the pan
value at position 0 and the tilt value at position 1. Set the
\'\'no_check_forbidden_area\'\' field of the state message to false to
prohibit the movement to end inside a forbidden area (so to speak the
movement will be rejected if the pan and tilt positions you pass to the
PTU via this message lie within a forbidden area). The current position
and state can be read from the \'\'/asr_flir_ptu_driver/ptu_state\'\'
topic. The current position and whether the movement has finished is
available there. The last part of the topic can be configured just as
the other topic above, but with the use of the
\'\'/asr_flir_ptu_driver/ptuTopicState\'\' parameter. Several other
functionalities are availabe via services. Invoke
\'\'/asr_flir_ptu_driver/path_prediction\'\' to check for collision with
a forbidden area. The \'\'asr_flir_ptu_driver::Predict\'\' takes the
possible endpoint as request and as soon as the service returns, the
response contains the collision point. If the returned point equals the
point put in, no collision occured. Send the returned point as endpoint
for the movement to the PTU as described above, but set
\'\'no_check_forbidden_area\'\' to true (with the returned point
forbidden areas are no problem, but the check could cause a problem that
does not exists because of the point being a little bit unprecise and
could be a little bit inside the forbidden area). There is also a
service available to check if a point lies within a forbidden area and
can be invoked with \'\'/asr_flir_ptu_driver/validation_service\'\'
using \'\'asr_flir_ptu_driver::Validate\'\'. Input the values for pan
and tilt, \'\'margin\'\' describes a possible distance the point is
allowed to lie outside the pan/tilt limits. The service will return if
the point you passed to it is valid, and it will return a new endpoint
being within the pan/tilt limits (if a point lies out of the limits but
within the margin outside the limits, it is set to the limit in the
return value). There is also a service to acquire the current limits for
pan/tilt and the forbidden areas. Invoke
\'\'/asr_flir_ptu_driver/get_range service\'\' with
\'\'asr_flir_ptu_driver::Range\'\' to get them. No special input is
required. If you changed values on the parameter server (not for the
topic names but for the PTU, like the speed for pan) use the
\'\'/asr_flir_ptu_driver/update_settings\'\' service to make the PTU use
them using \'\'std_srvs::Empty\'\'. A description of all the parameters
configurable and their location can be found in section 4.3. The last
part of all service topics can be modified just as the message topics
within rosCommands.yaml. Parameter names are
\'\'servicePathPrediction\'\', \'\'serviceValidation\'\',
\'\'serviceRange\'\' and \'\'s\'\'erviceSettingsUpdate. Advanced usage
of messages and topics will be described in the tutorials.

#### Simulation

If you want to simulate the behaviour a FLIR PTU in a basic way you need
to launch the package the following way:

```
roslaunch asr_flir_ptu_driver ptu_left_mock.launch
``` The simulation provides basic functions, like
the simulation of movements after getting a movement command, the check
if a position lies within a forbidden area, the setting of forbidden
areas and the setting of maximum and minimum values for pan and tilt.

Be aware that it is not possible to use some advanced functions -
especially the path prediction - with the simulation.

Note: If you are using the simulation and want to get a behaviour as
accurate as possible, set the hardware limits of the pan and tilt
movement in the ptu_properties.yaml file in the param folder (arguments
are named mock_pan_min, \...). Try to find them for example in the
manual and set them in the ptu_properties.yaml in degrees (not radians).

#### Real

To start asr_flir_ptu_driver with a real PTU you need to connect and
power up the PTU first.

As soon as the initialization of the PTU after the power up is done
(when it stops moving) start the PTU driver using

```
roslaunch asr_flir_ptu_driver ptu_left.launch
``` Afterwards, the PTU will perform another set of
movements. As soon as these movements ended, it is possible to send
instructions to the PTU using messages or the GUI.

## ROS Nodes

### Subscribed Topics

Using the ptu_left.launch launchfile the topics shown below will be
found under \'\'/asr_flir_ptu_driver\'\'.

\'\'state_cmd\'\'

-   Type: asr_flir_ptu_driver::State
-   Usage: Used to send new pan/tilt position to the ptu. Usage
    explained in detail in 3.4.2 and in the tutorials.

### Published Topics

Using the ptu_left.launch launchfile the topics shown below will be
found under \'\'/asr_flir_ptu_driver\'\'.

\'\'ptu_state\'\'

-   Type: asr_flir_ptu_driver::State
-   Usage: Used to read the current PTU position and if the PTU movement
    is finished or not. Let \'\'msg\'\' be a message published on the
    topic. The current pan/tilt value can be found under
    msg.state.position\[0/1\], msg.finished determines if the current
    movement is finished and msg.seq_num can be used to find out if the
    received message is related to the last sent new position (same
    seq_num).

\'\'state\'\'

-   Type: sensor_msgs::!JointState
-   Usage: Do not use, use \'\'ptu_state\'\' instead. Outdated legacy
    topic, still in use in some other parts of the asr project.

### Parameters

Using the ptu_left.launch launchfile all parameters shown below will be
found under \'\'/asr_flir_ptu_driver\'\'.

\'\'\'PTU setting parameters:\'\'\'

\'\'pan_min_angle\'\'

-   Type: double
-   Semantic: Degree
-   Explanation: The minimum pan angle the PTU is allowed to use.

\_pan_max_angle\_

-   Type: double
-   Semantic: Degree
-   Explanation: The maximum pan angle the PTU is allowed to use.

\_pan_base_speed\_

-   Type: int
-   Semantic: Positions/Second
-   Explanation: The speed at which the pan movement of the PTU
    starts/stops instantly.

\_pan_target_speed\_

-   Type: int
-   Semantic: Positions/Second
-   Explanation: The speed the PTU shall accelerate to on pan axis
    during a movement.

\_pan_upper_speed\_

-   Type: int
-   Semantic: Positions/Second
-   Explanation: The upper limit for \'\'pan_target_speed\'\'

\_pan_accel\_

-   Type: int
-   Semantic: Position/Second²
-   Explanation: The acceleration for the pan movement.

\_pan_hold\_

-   Type: int
-   Semantic: 0 = PTU_OFF_POWER, 1 = PTU_LOW_POWER, 2 = PTU_REG_POWER
-   Explanation: The power level of the PTU pan axis when not moving.

\_pan_move\_

-   Type: double
-   Semantic: 0 = PTU_LOW_POWER, 1 = PTU_REG_POWER, 2 = PTU_HI_POWER
-   Explanation: The power level of the PTU pan axis when moving.

\'\'tilt_min_angle\'\'

-   Type: int
-   Semantic: Degree
-   Explanation: The minimum tilt angle the PTU is allowed to use.

\'\'tilt_max_angle\'\'

-   Type: int
-   Semantic: Degree
-   Explanation: the maximum tilt angle the PTU is allowed to use.

\'\'tilt_base_speed\'\'

-   Type: int
-   Semantic: Positions/Second
-   Explanation: The speed at which the tilt movement of the PTU
    starts/stops instantly.

\'\'tilt_target_speed\'\'

-   Type: int
-   Semantic: Positions/Second
-   Explanation: The speed the PTU shall accelerate to on tilt axis
    during a movement.

\'\'tilt_upper_speed\'\'

-   Type: int
-   Semantic: Positions/Second
-   Explanation: The upper limit for \'\'tilt_target_speed.\'\'

\'\'tilt_accel\'\'

-   Type: int
-   Semantic: Positions/Second²
-   Explanation: The acceleration for the tilt movement.

\'\'tilt_hold\'\'

-   Type: int
-   Semantic: 0 = PTU_OFF_POWER, 1 = PTU_LOW_POWER, 2 = PTU_REG_POWER
-   Explanation: The power level of the PTU tilt axis when not moving.

\'\'tilt_move\'\'

-   Type: int
-   Semantic: 0 = PTU_LOW_POWER, 1 = PTU_REG_POWER, 2 = PTU_HI_POWER
-   Explanation: The power level of the tilt pan axis when moving.

\'\'speed_control\'\'

-   Type: bool
-   Explanation: To use speed control mode or not. Leave on false in the
    current state of the software.

\'\'computation_tolerance\'\'

-   Type: double
-   Semantic: Degree
-   Explanation: Tolerance for computation error (eg. conversion from
    steps to degree, float/double multiplication etc.). There should be
    no need to change this parameter

\'\'distance_factor\'\'

-   Type: int
-   Explanation: Number of points that will be used to approximate paths
    (when the path prediction is used). Higher number -\> higher
    accuracy -\> higher runtime.

\'\'forbidden_pan_min\'\'

-   Type: double\[\]
-   Semantic: Degree
-   Explanation: The minimal pan values for forbidden areas. The value
    at i defines together with the values at i in
    \'\'forbidden_pan_max\'\', \'\'forbidden_tilt_min\'\' and
    \'\'forbidden_tilt_max\'\' a forbidden area (the included area).

\'\'forbidden_pan_max\'\'

-   Type: double\[\]
-   Semantic: Degree
-   Explanation: The maximum pan values for forbidden areas. The value
    at i defines together with the values at i in
    \'\'forbidden_pan_min\'\', \'\'forbidden_tilt_min\'\' and
    \'\'forbidden_tilt_max\'\' a forbidden area (the included area).

\'\'forbidden_tilt_min\'\'

-   Type: double\[\]
-   Semantic: Degree
-   Explanation: The minimum tilt values for forbidden areas. The value
    at i defines together with the values at i in
    \'\'forbidden_pan_min\'\', \'\'forbidden_pan_max\'\' and
    \'\'forbidden_tilt_max\'\' a forbidden area (the included area).

\'\'forbidden_tilt_max\'\'

-   Type: double\[\]
-   Semantic: Degree
-   Explanation: The maximum tilt values for forbidden areas. The value
    at i defines together with the values at i in
    \'\'forbidden_pan_min\'\', \'\'forbidden_pan_max\'\' and
    \'\'forbidden_tilt_min\'\' a forbidden area (the included area).

\'\'mock_pan_min_hardware_limit\'\'

-   Type: double
-   Semantic: Degree
-   Explanation: The minimum hardware limit for pan movement of the mock
    (equivalent to physical constraints that limit the movement of a
    real PTU).

\'\'mock_pan_max_hardware_limit\'\'

-   Type: double
-   Semantic: Degree
-   Explanation: The maximum hardware limit for pan movement of the mock
    (equivalent to physical constraints that limit the movement of a
    real PTU).

\'\'mock_tilt_min_hardware_limit\'\'

-   Type: double
-   Semantic: Degree
-   Explanation: The minimum hardware limit for tilt movement of the
    mock (equivalent to physical constraints that limit the movement of
    a real PTU).

\'\'mock_tilt_max_hardware_limit\'\'

-   Type: double
-   Semantic: Degree
-   Explanation: The maximum hardware limit for tilt movement of the
    mock (equivalent to physical constraints that limit the movement of
    a real PTU).

\'\'port\'\'

-   Type: string
-   Explanation: The name of the port the PTU is connected to.

\'\'baud\'\'

-   Type: int
-   Explanation: The baud rate for the PTU.

\'\'mockPTU\'\'

-   Type: boolean
-   Explanation: Determines whether to use the mock (true) or a real PTU
    (false).

\'\'update_rate\'\'

-   Type: int
-   Explanation: Update rate for the ROS node (ros::Rate).

```{=html}
<!-- -->
```
-   Name parameters:\*

\'\'ptu_base_frame\'\'

-   Type: string
-   Explanation: Name of the base frame (tf).

\'\'ptu_pan_frame\'\'

-   Type: string
-   Explanation: Name of the pan frame (tf).

\'\'ptu_pan_frame_rotated\'\'

-   Type: string
-   Explanation: Name of the rotated pan frame (tf).

\'\'ptu_tilt_frame\'\'

-   Type: string
-   Explanation: Name of the tilt frame (tf).

\'\'ptu_tilt_frame_rotated\'\'

-   Type: string
-   Explanation: Name of the rotated tilt frame (tf).

Changing of the following parameters is not advised but possible. Use
remap instead.

\'\'topicStateCommand\'\'

-   Type: string
-   Explanation: Name of the topic the PTU subscribes to to get new
    positions to move to.

\'\'topicState\'\'

-   Type: string
-   Explanation: Name of the topic that publishes the current state of
    the PTU, outdated.

\'\'ptuTopicState\'\'

-   Type: string
-   Explanation: Name of the topic that publishes the current state of
    the PTU (position + if finished or not).

\'\'serviceValidation\'\'

-   Type: string
-   Explanation: Name of the service that is used to validate possible
    pan/tilt values.

\'\'serviceAlive\'\'

-   Type: string
-   Explanation: Name of a service that is used to check if the driver
    is alive.

\'\'servicePathPrediction\'\'

-   Type: string
-   Explanation: Name of the service to perform a path prediction

\'\'serviceSettingsUpdate\'\'

-   Type: string
-   Explanation: Name of the service for updating all settings.

\'\'serviceSpeedControlUpdate\'\'

-   Type: string
-   Explanation: Name of the service for updating the speed settings.

\'\'serviceRange\'\'

-   Type: string
-   Explanation: Name of the service for getting the range (max/min
    values for pan/tilt + forbidden areas).

### Needed Services

There are no external services needed. Nevertheless, if the GUI is used,
it uses a few services offered by the driver, therefore always start
\'\'ptu_left.launch\'\' before \'\'ptu_gui.launch\'\'

### Provided Services

Using the ptu_left.launch launchfile the services shown below will be
found under \'\'/asr_flir_ptu_driver\'\'.

\'\'validation_service\'\'

-   Type: asr_flir_ptu_driver::Predict
-   Usage: This method is used to determine if the PTU can move to a
    possible new pan and tilt position. Enter the pan and tilt values in
    the corresponding request field of the service request. You are free
    to set a specific \'\'margin\'\' (corresponding field of the service
    request, set to 0 if you do not want to use it). If the points are
    out of the bounds of the ptu movement space (pan/tilt limits) but
    within the margin, the point gets set to the border (e.g. margin =
    2.5, pan upper limit = 110, pan value = 111 -\> pan value will be
    set to 110 in the return value). The margin only affects pan/tilt
    limits, not forbidden areas. The validity of the point with respect
    to the margin can be determined by the response field \'\'is_valid.
    \'\'If you have set any margin other than 0, use the pan and tilt
    values found in the response for further requests (because of
    possible corrections done to the values).

\_alive_service\_

-   Type: std_srvs::Empty
-   Usage: A service that does nothing. Used to bind a program to the
    node executing the driver for checking if the driver is still alive,
    e.g. via \'\'if\'\'-Statement.

\_path_prediction\_

-   Type: asr_flir_ptu_driver::Predict
-   Usage: The predict service is used to perform path prediction from
    the current position of the PTU to a new position defined by the
    request parameters \'\'pan\'\' and \'\'tilt\'\'. The path prediction
    will determine the first point that collides with any forbidden area
    and will contain the new pan and tilt values for the collision point
    in its response (if no collision occurs the input values will be
    found in the response). You still have to make sure that the point
    lies within pan/tilt limits. The quality of the result is directly
    affected by the parameter \'\'distance_factor\'\'.

\_update_settings\_

-   Type: std_srvs::Empty
-   Usage: Used to update all parameters listed in the Parameter section
    (you can change the values on the parameter server, calling this
    service will forward them to the program), EXCEPT:
    \'\'ptu_base_frame\'\', \'\'update_rate\'\', all mock hardware
    limits, \'\'baud\'\', \'\'port\'\', \'\'mockPTU\'\'

\_update_speed_control\_

-   Type: std_srvs::Empty
-   Usage: Used to update the following speed settings (first set them
    on the parameter server, then forward them using this service):
    \'\'speed_control\'\', \'\'pan_target_speed\'\',
    \'\'tilt_target_speed\'\'

\_get_range\_

-   Type: asr_flir_ptu_driver::Range
-   Usage: This service provides the caller with the current pan/tilt
    limits as well as the forbidden areas in its response. There are no
    fields that need to be filled out in the request.

## Tutorials

These tutorials will cover the usage of asr_flir_ptu_driver with an own
node communicating over services and topics. It will be explained how
certain goals can be achieved. Before starting your own program

```
roslaunch asr_flir_ptu_driver ptu_left.launch
``` needs to be invoked from the terminal to start
the PTU. Make sure it is connected. Configure the forbidden areas in the
\'\'ptu_properties.yaml \'\'as you need them (details on forbidden areas
in Chapter 2). Then continue with the tutorials below:

-   [Movement Tutorial](asr_flir_ptu_driver/DriverMovementTutorial)
-   [Advanced Movement Tutorial](asr_flir_ptu_driver/AdvancedMovementTutorial)
-   [Settings Tutorial](asr_flir_ptu_driver/SettingsTutorial)
