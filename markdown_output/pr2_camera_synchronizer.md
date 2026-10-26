## System Overview

This section gives an overview of the PR2's camera systems. Some
readers may want to skip directly to
[the following section](#UsingOnThePr2) for a more practical discussion
of how to use the robot's cameras, or to the [ROS API](#ROS_API) for a
detailed description of the pr2_camera_synchronizer parameters.

### Hardware Components

![The robot's cameras\|align="right"](attachment:PR2Cameras.png)

The following hardware components are involved in producing vision data
on the PR2:

- A color [wge100](wge100_camera) camera on each forearm.
- A wide field-of-view color [wge100](wge100_camera) stereo camera pair
  on the head.
- A narrow field-of-view black and white [wge100](wge100_camera) stereo
  camera on the head.
- A high resolution GC2450C [Prosilica](prosilica_camera) camera on the
  head.
- A texture projector on the head to project a texture on objects that
  are being viewed by the stereo cameras.
- Digital outputs on the PR2 motor controller boards that are used to
  synchronously trigger cameras.

### Synchronization Constraints

Synchronization between these pieces of hardware is needed because of
system constraints:

- The stereo camera pairs are made up of two independent monocular
  WGE100 cameras. In order to get synchronized triggering of these
  cameras, they must be triggered from a common source.
- A single trigger signal is fed to both stereo camera pairs. The
  triggering protocol allows the stereo cameras to have different
  exposure phases, but their frame rate must match.
- Cameras must be triggered synchronously with the texture projector. To
  get a textured image the exposure must coincide with projection. To
  get an untextured image the exposure must not intersect with
  projection.
- The texture projector must be fired at at least 40Hz to avoid very
  unpleasant flickering.
- The texture projector's pulse length is limited in hardware to avoid
  damaging the projector LED. The maximum pulse length is 2
  milliseconds, but this value may be reduced if pulses are too close
  together.
- The Prosilica camera does not have a trigger line, and is usually used
  with long exposure times. Hence, to get untextured images from the
  Prosilica camera, the normal texture projector firing must be
  inhibited during Prosilica camera exposures. An exposure line from the
  Prosilica camera is connected to an inhibit input on the texture
  projector controller board to allow this inhibition to occur.

[![Overview of the Camera Systems\|width="750"](attachment:CameraOverview.png)](attachment:CameraOverview.png)

### Software Components

The variety of hardware components involved implies that a variety of
software components are involved in producing camera images:

- A [wge100_camera_node](wge100_camera) per WGE100 camera.
- A [wge100_multi_configurator](wge100_camera) for each stereo pair,
  which replicates its parameters to each camera's driver.
- A [prosilica_node](prosilica_camera) for the Prosilica camera.
- [pr2_controller_manager](pr2_controller_manager) with suitable
  controllers running:
- One [MultiTriggerController](ethercat_trigger_controllers) per WGE100
  camera trigger line. I.e., one for each forearm camera, and one for
  both of the stereo cameras.
- Two [MultiTriggerController](ethercat_trigger_controllers) for the
  projector, one to trigger the projector and one to determine whether
  to activate inhibition by the prosilica camera.
- One [ProjectorController](ethercat_trigger_controllers) to enable the
  projector.
- A pr2_camera_syncronizer node in charge of setting the triggers and
  camera drivers into triggering states that are consistent with the
  user's desires.

## Working With the WGE100 Cameras on the PR2

The various components involved in PR2 camera synchronization expose a
large number of options to the user. This section is designed to
highlight the options that the user should be using to configure the
cameras on the PR2. All the necessary nodes and controllers to work with
the WGE100 cameras are brought up automatically when the pr2 robot is
started.

It is not recommended that the user adjust parameters that are not
listed below as they are likely to leave the system in a non functioning
state.

This section shows how to use the `reconfigure_gui` to set these
parameters, they can be set just as easily using any other
[dynamic_reconfigure](dynamic_reconfigure) mechanism as demonstrated in
[these tutorials](dynamic_reconfigure/Tutorials).

### Setting Frame Rates and Projector Modes via the Synchronizer

Frame rates and projector modes should be set using
[dynamic_reconfigure](dynamic_reconfigure) on the
pr2_camera_synchronizer_node. For <example:

```
$ rosrun dynamic_reconfigure reconfigure_gui /camera_synchronizer_node
```

>

The synchronizer will make a best-effort attempt at using the rates and
modes you requested, but may have to
[round to the nearest possible rate or use a different mode](#Synchronization_Strategy).
In that case, the GUI and parameter will reflect the rates and modes
that were actually set.

### Other Camera Settings

Many WGE100 settings not managed by the synchronizer can be set directly
with the cameras by using [dynamic_reconfigure](dynamic_reconfigure). A
detailed list of which parameters can be set in this way without
conflicting with the synchronizer can be found
[below](#SafeParameterLists).

For the forearm cameras, the camera node (`forearm_camera_l` or
`forearm_camera_r`) should be configured directly. For the stereo
pairs, the wge100_multi_configurator node (`wide_stereo_both` or
`narrow_stereo_both`) should be configured; this node controls both
cameras of a stereo pair, and will dispatch configuration changes to
both underlying camera nodes.

For the wide stereo camera:

```
$ rosrun dynamic_reconfigure reconfigure_gui /wide_stereo_both
```



For the narrow stereo camera:

```
$ rosrun dynamic_reconfigure reconfigure_gui /narrow_stereo_both
```



For the right forearm camera:

```
$ rosrun dynamic_reconfigure reconfigure_gui /forearm_camera_r
```



For the left forearm camera:

```
$ rosrun dynamic_reconfigure reconfigure_gui /forearm_camera_l
```



#### Setting Image Levels

Many image level parameters can be safely set:

- **Shared Image Levels**: `brightness`, `black_level`.

<!-- -->

- **Untextured Image Levels**: `auto_exposure`, `exposure`,
  `auto_gain`, `gain`, `companding`

<!-- -->

- **Textured Image Levels**: `auto_gain_alternate`,
  `gain_alternate`, `companding`

Please refer to the [wge100_camera](wge100_camera#Wge100CameraNode)
documentation for details on what these parameters mean.

#### Setting Region of Interest

(Region of Interest is currently broken)

The following parameters can be set: `width`, `height`,
`horizontal_binning`, `vertical_binning`, `horizontal_offset`,
`vertical_offset`, `mirror_x`, `mirror_y`, `rotate_180`.

Please refer to the [wge100_camera](wge100_camera#Wge100CameraNode)
documentation for details on what these parameters mean.

Note 1: the `camera_info` stored in the camera is only valid for the
region of interest parameters that were used when it was created. The
`wge100_camera_node` will refuse to use `camera_info` with the wrong
width and height, but will not detect changes in the other parameters.

Note 2: if the data rate needed by region of interest settings is too
high, the WGE100 camera will fail to stream the images, and you will
have to select lower-bandwidth settings.

## Image Topics

Images from the wide stereo camera and forearm cameras are published in
the **wide_stereo**, **forearm_r** and **forearm_l** namespaces, whether
they are textured or not.

To facilitate using the narrow stereo camera in
**[AlternatingProjector](#AlternatingProjector)** mode, textured images
from the narrow stereo camera are always published in the
**narrow_stereo_textured** namespace, and untextured images are always
published in the **narrow_stereo** namespace.

## Resetting the WGE100 Cameras

Due to unresolved firmware bugs, it may happen that a WGE100 camera will
become unresponsive. The unresponsiveness of the camera can be verified
by running:

```
$ rosrun wge100_camera discover lan0
Found camera serial://1800023 name://forearm_l MAC: 00:24:cd:00:00:f0 iface: lan0 current IP: 10.68.0.42, PCB rev: C HDL rev: 504 FW rev: 202
Found camera serial://3001038 name://wide_stereo_r MAC: 00:24:cd:00:01:01 iface: lan0 current IP: 10.68.0.46, PCB rev: C HDL rev: 504 FW rev: 202
Found camera serial://3001039 name://wide_stereo_l MAC: 00:24:cd:00:00:fc iface: lan0 current IP: 10.68.0.45, PCB rev: C HDL rev: 504 FW rev: 202
Found camera serial://2701021 name://narrow_stereo_r MAC: 00:24:cd:00:01:02 iface: lan0 current IP: 10.68.0.44, PCB rev: C HDL rev: 504 FW rev: 202
Found camera serial://1800031 name://forearm_r MAC: 00:24:cd:00:00:ea iface: lan0 current IP: 10.68.0.41, PCB rev: C HDL rev: 504 FW rev: 202
Found camera serial://2701031 name://narrow_stereo_l MAC: 00:24:cd:00:01:03 iface: lan0 current IP: 10.68.0.43, PCB rev: C HDL rev: 504 FW rev: 202
```



If one of the cameras does not show up after a couple of attempts, it
may have crashed.

The easiest way to reset all the WGE100 cameras while ROS is running on
the PR2 is to use the `camera_reset` option to true in the
`camera_synchronizer_node` options. This will raise the camera's
trigger signal for a few seconds, telling the camera to reset itself.
The reset will take about 5-10 seconds.

```
$ rosrun dynamic_reconfigure dynparam /camera_synchronizer_node camera_reset true
```



Note: This will only work if the trigger controllers are running.

Alternatively, a single camera can be reset when ROS is not running by
using the `reconfigure_cam` utility in `wge100_camera`. For
<example:

```
$ rosrun wge100_camera reconfigure_cam name://wide_stereo_l
```

>

## Synchronization Strategy

### Projector Modes

In a running PR2, many cameras may be simultaneously in use by different
users. Whether the projector should be on at any given time is a
combination of the operating modes requested by the user of each camera.
The settings of a user's camera depend on whether the projector is on
or off. To avoid spurious changes in the settings of one user's camera
when another user's camera is reconfigured, the pr2_camera_synchronizer
is organized so that there is a master `projector_mode` setting, and a
`_trig_mode` setting for each camera.

Users request the `_trig_mode` that their camera should be in, and
the synchronizer decides on the projector state based on the current
`projector_mode`. For a given `projector_mode`, the
pr2_camera_synchronizer ensures that the settings of one camera do not
depend on the `trig_mode` of the other cameras. In a typical use of
the synchronizer, the `projector_mode` is set once and for all by a
high-level decision, and users can adjust `_trig_mode` at will.

The synchronizer can be in one of three modes, depending on which
strategy it should use:

- **!ProjectorOff**: The projector is never pulsing. Triggering modes
  that require the projector will be refused by the synchronizer. The
  stereo cameras, and each forearm camera can independently select their
  frame rates. Exposure times are limited only by the frame rate.
- **!ProjectorOn**: The projector is always pulsing. Cameras trigger at
  divisors of half the projector triggering rate (even divisors for
  cameras that are alternating between textured and non-textured
  frames). Exposure times for non-textured images are limited by the
  time between two projector pulses.
- **!ProjectorAuto**: Everything is configured as if the projector was
  pulsing, except that the projector is only actually turned on if one
  of the cameras needs it. This way a change in configuration for one of
  the cameras that causes the projector to be activated or disactivated
  do not change the timing of the other cameras.

The recommended operating mode is **!ProjectorAuto**. **!ProjectorOff**
can be used if longer exposures are needed or if the projector is deemed
too unpleasant. **!ProjectorOn** will most likely not be used in
practice.

### Trigger Modes

A variety of triggering modes are available for the WGE100 cameras.
Because different cameras have different constraints, all triggering
modes are not available for all cameras.

- Projector agnostic modes: Cameras in these modes are not synchronous
  with the projector, which may lead to flashing of the texture.
- **!InternalTrigger**: The camera generates its own triggering. This
  mode is applicable only for the forearm cameras, as the two cameras in
  a stereo pair need to be triggered simultaneously from a common
  source.
- **!IgnoreProjector**: The camera is triggered by a motor controller
  board, but no attempt is made to synchronize the camera's triggering
  with the projector triggering, so the camera's frame rate is
  independent of the projector rate. This mode is available on all PR2
  WGE100 cameras.
- Projector aware modes: These modes are not available when the
  projector is in the **!ProjectorOff** mode. They will automatically be
  switched to **!IgnoreProjector** in that case.
- **!WithProjector**: The camera is triggered in phase with the
  projector, resulting in a textured image. The exposure time is set to
  coincide with the duration of the projector pulse. This mode is
  available on all PR2 WGE100 cameras. On the narrow stereo camera,
  images produced in this mode are published to the
  `narrow_stereo_textured` namespace (this does not apply for other
  cameras).
- **!WithoutProjector**: The camera is triggered out of phase with the
  projector, resulting in an untextured image. The maximum exposure time
  is set to the interval between the projector pulses. This mode is
  available on all PR2 WGE100 cameras.
- **!AlternatingProjector**: Textured and untextured frames are
  alternated. The exposure times are set as in the non-alternating
  modes. This mode is only available on the narrow stereo camera as it
  requires special support from the imager chip. Textured images are
  published to the `narrow_stereo_textured` namespace, and untextured
  images are published to the `narrow_stereo` namespace.

### Camera Frame Rates

In many cases, the camera frame rate must be some suitable divisor of
the ```projector_rate```. When a user sets the frame rate for a
camera, the synchronizer will round that rate to the nearest suitable
rate, and report the rounded value back to the user via the
[dynamic_reconfigure](dynamic_reconfigure) mechanism.

The ```projector_rate``` is not affected by the camera settings.
When it is set, it is simply rounded to the nearest divisor of 1 kHz.
Again the rounded value is reported back via the
[dynamic_reconfigure](dynamic_reconfigure) mechanism.

### Projector Waveform

The pr2_camera_synchronizer operates with a standard waveform that
repeats after four pulses. The pulses in one period are numbered 1 to 4.
The waveform is entirely determined by three parameters:

- **projector_rate**: The average number of times the projector pulses
  per second. This is an average because the spacing between pulses
  varies within the four pulse pattern.
- **projector_pulse_length**: The time that the projector is on for one
  projector pulse. The projector driver protection circuitry may in some
  cases limit the pulse length to be lower than this value.
- **projector_pulse_shift**: Introduces asymmetry in the pulses. It
  varies from 0 to 1 with increasing asymmetry.

![](attachment:Waveform.png)

The timing of the pulses is as follows, where 'T=1/projector_rate' is
the average pulse period:

- Pulses 1 and 3 are spaced by about one pulse-length more than '2T'.
  Cameras that are in the **!AlternatingProjector** mode expose during
  pulse 1, and just before pulse 3.
- Pulses 2 and 4 are spaced by exactly '2T'. Cameras in the
  **!WithProjector** mode expose during pulses 2 and 4.
- The spacing between pulses 1 and 2 varies from 'T' to just under one
  pulse length less than '2T', depending on the value of
  **projector_pulse_shift**. Cameras that are in the
  **!WithoutProjector** mode have their exposure end just before pulses
  2 and 4. The start of the exposure depends on the exposure time, which
  is bounded by the time interval between pulses 3 and 4. Adjusting the
  **projector_pulse_shift** parameter allows the exposure time of
  **!WithoutProjector** cameras to be increased. However, the shift
  comes at the cost of more unpleasant flickering of the projected
  texture and potential reduction in length of pulses 1 and 3, if the
  projector board determines that the inter-pulse spacing has been too
  short.

### Interaction with the Prosilica Camera

(Not implemented yet.)

To avoid having texture in images taken by the Prosilica camera, the
**prosilica_projector_inhibit** option can be turned on. In this case,
an exposure signal from the Prosilica camera directly inhibits firing of
the projector. When the projector is inhibited the WGE100 cameras will
continue to be triggered as if the projector was active, so some frames
that should be textured may be partially textured or not textured at
all.

### Implementation Limitations

The current implementation has certain timing limitations that may be
removed in future versions.

- Camera and projector periods must be multiples of the 1ms Ethercat
  interval. In particular rates that are a multiple of 120 Hz cannot
  currently be achieved exactly, which could lead to flickering when
  fluorescent lighting is used on 60 Hz AC power.

<!-- -->

- Resolution of triggering and projecting is limited to 1ms Ethercat
  intervals. 1ms guard times have been incorporated into all the
  triggering signals and exposure limits.

### Multiple PR2 Robots

The phase of the camera triggering is set absolutely relative to a ROS
time of 0. Hence, if multiple robots have their clocks synchronized with
sub-millisecond resolution, and their projector rates match, their
projectors will fire synchronously. As a result images that are supposed
to be textured will see the texture from both robots, and images that
are supposed to be untextured should not see texture from either robot.

On the other hand, the Prosilica camera projector inhibition will not
work between robots. Therefore, Prosilica images from one robot may see
texture projected by the other, even if **prosilica_projector_inhibit**
is true.

## ROS API



```clearsilver
node.0 {
name=pr2_camera_synchronizer
desc=Node to set up triggering of the PR2 forearm cameras, stereo cameras and texture projector. It is configured via [[dynamic_reconfigure]].
Note: For clarity, the service calls and dynamic_reconfigure connections that the pr2_camera_synchronizer makes to configure cameras/triggers are not shown.
# Autogenerated param section. Do not hand edit.
param {
group.0 {
name=Dynamically Reconfigurable Parameters
desc=See the [[dynamic_reconfigure]] package for details on dynamically reconfigurable parameters.
0.name= ~projector_rate
0.default= 60.0
0.type= double
0.desc=Projector pulse frequency in Hz. Range: 40.0 to 120.0
1.name= ~projector_pulse_length
1.default= 0.002
1.type= double
1.desc=Length of the projector pulses in s. At high currents the hardware may limit the pulse length. Range: 0.001 to 0.002
2.name= ~projector_pulse_shift
2.default= 0.0
2.type= double
2.desc=How far off-center the intermediate projector pulses are. Zero is on-center, one is touching the following pulse. Range: 0.0 to 1.0
3.name= ~projector_mode
3.default= 2
3.type= int
3.desc=Indicates whether the projector should be off, on when in use or on all the time. Possible values are: !ProjectorOff (1): The projector is always off., !ProjectorAuto (2): The projector is on if one of the cameras is using it., !ProjectorOn (3): The projector is always on.
4.name= ~prosilica_projector_inhibit
4.default= False
4.type= bool
4.desc=Indicates if the projector should turn off when the prosilica camera is exposing. 
5.name= ~stereo_rate
5.default= 30.0
5.type= double
5.desc=Indicates the frame rate for both stereo cameras in Hz. (Gets rounded to suitable divisors of projector_rate.) Range: 1.0 to 60.0
6.name= ~wide_stereo_trig_mode
6.default= 4
6.type= int
6.desc=Indicates the triggering mode of the wide stereo camera. Possible values are: !IgnoreProjector (2): The camera's frequency can be set independently of the projector frequency. There is no deterministic phase relation between projector firing and camera triggering., !WithProjector (3): The camera always exposes while the projector is on., !WithoutProjector (4): The camera always exposes while the projector is off.
7.name= ~narrow_stereo_trig_mode
7.default= 4
7.type= int
7.desc=Indicates the triggering mode of the narrow stereo camera. Possible values are: !IgnoreProjector (2): The camera's frequency can be set independently of the projector frequency. There is no deterministic phase relation between projector firing and camera triggering., !WithProjector (3): The camera always exposes while the projector is on., !WithoutProjector (4): The camera always exposes while the projector is off., !AlternateProjector (5): The camera alternates between frames with and without the projector.
8.name= ~forearm_r_rate
8.default= 30.0
8.type= double
8.desc=Indicates the frame rate for the right forearm camera in Hz. (Gets rounded to suitable divisors of projector_rate.) Range: 1.0 to 60.0
9.name= ~forearm_r_trig_mode
9.default= 1
9.type= int
9.desc=Indicates the triggering mode of the right forearm camera. Possible values are: !InternalTrigger (1): The camera does not use the trigger input., !IgnoreProjector (2): The camera's frequency can be set independently of the projector frequency. There is no deterministic phase relation between projector firing and camera triggering., !WithProjector (3): The camera always exposes while the projector is on., !WithoutProjector (4): The camera always exposes while the projector is off.
10.name= ~forearm_l_rate
10.default= 30.0
10.type= double
10.desc=Indicates the frame rate for the left forearm camera in Hz. (Gets rounded to suitable divisors of projector_rate.) Range: 1.0 to 60.0
11.name= ~forearm_l_trig_mode
11.default= 1
11.type= int
11.desc=Indicates the triggering mode of the left forearm camera. Possible values are: !InternalTrigger (1): The camera does not use the trigger input., !IgnoreProjector (2): The camera's frequency can be set independently of the projector frequency. There is no deterministic phase relation between projector firing and camera triggering., !WithProjector (3): The camera always exposes while the projector is on., !WithoutProjector (4): The camera always exposes while the projector is off.
12.name= ~projector_tweak
12.default= 0.0
12.type= double
12.desc=Adds a time shift in seconds to the projector timing. Useful for debugging but not in normal use. Range: -0.1 to 0.1
13.name= ~camera_reset
13.default= False
13.type= bool
13.desc=Does a hard reset of all the cameras using a long pulse on the trigger line. This parameter resets itself to false after 3 to 4 seconds. 
}
}
# End of autogenerated section. You may edit below.
```


