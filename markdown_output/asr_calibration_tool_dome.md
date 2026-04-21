![\|width="333",height="200"](attachment:Logo-white-medium.jpg)

## Description

This package provides a tools for tracking calibration data for the
kinematic chain of the PdB -Dome. It provides a data-tracking for
recording 6D positions of Flock of Birds data glove and a checkerboard
mounted on it. The checkerboard is tracked with the stereo camera
system. With this construction, the kinematic chain is closed. The
recorded data is written to a file and can be used for the
asr_kinematic_chain_optimizer.

## Functionality

The idea of this calibration process is to close the kinematic chain,
track several hundred datasets, describe a default TF-configuration and
minimize the distances. In addition, the PTU pan- and tilt-angle are
also tracked. Dataset are the tracked training data. Each value is a
configuration of a non-fix joint. A whole dataset (one row) contains all
variables of a kinematic chain (See
[asr_kinematic_chain_optimizer](asr_kinematic_chain_optimizer) for
further information). A sample Dataset is shown in the following
picture:

![\|height="143",width="420"](attachment:calibration_data.png)

This can be done with the following steps:

1\. Define a kinematic chain as best as you could, or use the old
kinematic chain. The format is shown in
[asr_kinematic_chain_optimizer](asr_kinematic_chain_optimizer) package.
Define also a goal function (e. g. Position of Frame1 and Frame2 should
be equal. (See
[asr_kinematic_chain_optimizer](http://wiki.ros.org/asr_kinematic_chain_optimizer)
for further information). Make sure that all non-fixed Frames are
parameterized (like PTU).

2\. Construct something, so the kinematic chain is closed. In this case
a tracker of the [Flock of Birds magnet-tracking](asr_flock_of_birds)
system is attached on a checkerboard detector. Define a transformation
between the two tracked frames like you did in 1.

3\. Collect several datasets, further described in section "Usage"

4\. Run the
[asr_kinematic_chain_optimizer](http://wiki.ros.org/asr_kinematic_chain_optimizer)
with you frames and datasets as inputfiles.

## Usage

To collect the datasets you first have to start the ptu, Flock of Birds
server, the camera system, the checkerboard_detector and finally the
datatracker (Have a look at 3.4. Start System). Now ensure that both
trackers are located as well as the ptu is started well:

e\. g.:



```
rostopic echo /fob_objects
```

 

```
rostopic echo /ptu_driver/state
```




```
rostopic echo /checkerboard_detector/objectdetection_pose
```

 If there are data published on each topic, you
can capture data with any key but 'e' (use 'e' for exit the
trackertool). Now just move your construction around in the working area
and collect as much datasets as you like. Capture your data so, the
datasets are well distributed in your working area and not all from one
position. If you feel satisfied with your tracking press 'e' and exit
the tracker tool. Now calibrate your kinematic chain with the kinematic
chain optimizer.

### Needed packages

-   [asr_msgs](asr_msgs)
-   ([asr_flock_of_birds](asr_flock_of_birds)) for data-tracking
-   ([asr_flir_ptu_driver](asr_flir_ptu_driver)) for data-tracking
-   ([asr_kinematic_chain_optimizer](asr_kinematic_chain_optimizer)) for
    calibration

### Needed software

-   ros-kinetic-checkerboard-detector

### Needed hardware

-   Pan-Tilt-Unit (PTU)
-   Guppy-Stereo-Camera System
-   Flock_of_birds magnet-tracking system
-   Some Tracking-Construction to close the cinematic chain shown in the
    following picture:

![checkerboad_tracker.jpg\|height="252",width="449"](attachment:checkerboad_tracker.jpg)
![height="252",width="449"](attachment:i61p124.jpg)
![height="252",width="450"](attachment:i61p81.jpg)

Left: The FoB-magnettracker is attached to a checkerboard.

Mid: Sample detection in the middle of the working area. The datatracker
runs on the PC in the background.

Right: Checkerboard detector and PTU-Controll-Gui runs on an separated
system to get some flexibility

### Start system



```
rosrun asr_flock_of_birds flock_of_birds_remote.sh

roslaunch asr_flir_ptu_driver ptu_left.launch

roslaunch asr_resources_for_vision guppy_head_full_pbd.launch

(roslaunch asr_flir_ptu_driver ptu_gui.launch)

roslaunch asr_calibration_tool_dome checkerboard_detector_single.launch
```



## ROS Nodes

### Subscribed Topics

-   FoB-Tracker: /fob_objects

```{=html}
<!-- -->
```
-   PTU: /ptu_driver/state

```{=html}
<!-- -->
```
-   Checkerborad Detector: */checkerboard_detector/objectdetection_pose*
